import { useState } from 'react';

export const useRazorpay = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const loadRazorpayScript = () => {
    return new Promise((resolve) => {
      if (window.Razorpay) {
        resolve(true);
        return;
      }

      const script = document.createElement('script');
      script.src = 'https://checkout.razorpay.com/v1/checkout.js';
      script.onload = () => resolve(true);
      script.onerror = () => resolve(false);
      document.body.appendChild(script);
    });
  };

  const processPayment = async (planData, userDetails = {}) => {
    try {
      setLoading(true);
      setError(null);

      // Load Razorpay script
      const isLoaded = await loadRazorpayScript();
      if (!isLoaded) {
        throw new Error('Failed to load Razorpay SDK');
      }

      // Create order on server
      const response = await fetch('/api/razorpay/create-order', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          amount: planData.amount,
          planId: planData.id,
        }),
      });

      const orderData = await response.json();
      
      if (!orderData.success) {
        throw new Error(orderData.error || 'Failed to create order');
      }

      // Razorpay checkout options
      const options = {
        key: orderData.key,
        amount: orderData.amount,
        currency: orderData.currency,
        name: 'AI Interview Mocker',
        description: `${planData.name} Plan Subscription`,
        image: '/logo.svg',
        order_id: orderData.orderId,
        handler: async (response) => {
          try {
            // Verify payment on server
            const verifyResponse = await fetch('/api/razorpay/verify-payment', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                razorpay_order_id: response.razorpay_order_id,
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_signature: response.razorpay_signature,
                planId: planData.id,
                userEmail: userDetails.email,
              }),
            });

            const verifyData = await verifyResponse.json();
            
            if (verifyData.success) {
              // Payment successful
              window.location.href = '/dashboard?payment=success';
            } else {
              throw new Error('Payment verification failed');
            }
          } catch (error) {
            console.error('Payment verification error:', error);
            setError('Payment verification failed');
          }
        },
        prefill: {
          name: userDetails.name || '',
          email: userDetails.email || '',
          contact: userDetails.phone || '',
        },
        notes: {
          plan: planData.name,
        },
        theme: {
          color: '#2563eb',
        },
        modal: {
          ondismiss: () => {
            setLoading(false);
          },
        },
      };

      const paymentObject = new window.Razorpay(options);
      paymentObject.open();
      
    } catch (error) {
      console.error('Payment error:', error);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return {
    processPayment,
    loading,
    error,
    setError,
  };
}; 