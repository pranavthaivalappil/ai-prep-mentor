# Razorpay Integration Setup

## Prerequisites
1. Create a Razorpay account at [razorpay.com](https://razorpay.com)
2. Get your API keys from the Razorpay dashboard

## Environment Variables
Create a `.env.local` file in your project root with:

```env
RAZORPAY_KEY_ID=your_razorpay_key_id_here
RAZORPAY_KEY_SECRET=your_razorpay_key_secret_here
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your_nextauth_secret_here
```

## Getting Razorpay Keys

### Test Mode (For Development)
1. Login to Razorpay Dashboard
2. Switch to "Test Mode" 
3. Go to Settings → API Keys
4. Generate Test Keys
5. Use these keys in your `.env.local`

### Live Mode (For Production)
1. Complete KYC verification
2. Switch to "Live Mode"
3. Generate Live Keys
4. Update production environment variables

## Features Included

✅ **Order Creation** - `/api/razorpay/create-order`
✅ **Payment Verification** - `/api/razorpay/verify-payment` 
✅ **React Hook** - `useRazorpay()` for easy integration
✅ **UI Integration** - Updated upgrade page with payment flow
✅ **Success Page** - Payment confirmation page
✅ **Error Handling** - Proper error states and user feedback

## Testing Payments

Use these test card details in Test Mode:
- **Card Number**: 4111 1111 1111 1111
- **Expiry**: Any future date
- **CVV**: Any 3 digits
- **Name**: Any name

## Security Notes

🔒 **Never expose** `RAZORPAY_KEY_SECRET` in client-side code
🔒 **Always verify** payment signatures on server-side
🔒 **Use HTTPS** in production
🔒 **Validate** all payment data before processing

## Payment Flow

1. User clicks "Upgrade to Pro"
2. Order created via `/api/razorpay/create-order`
3. Razorpay checkout modal opens
4. User completes payment
5. Payment verified via `/api/razorpay/verify-payment`
6. User redirected to success page
7. Database updated with subscription status

## Support

For Razorpay-specific issues, check:
- [Razorpay Documentation](https://razorpay.com/docs/)
- [Razorpay Node.js SDK](https://github.com/razorpay/razorpay-node) 