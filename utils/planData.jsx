import { Star, Zap } from 'lucide-react'

export const planData = [
    {
        id: 'free',
        name: "Free",
        price: "₹0",
        period: "Forever",
        description: "Perfect for getting started",
        features: [
            "3 Mock Interviews per month",
            "Basic AI feedback",
            "5 Questions per interview"
        ],
        buttonText: "Current Plan",
        buttonVariant: "outline",
        popular: false,
        icon: Star,
        disabled: true
    },
    {
        id: 'pro',
        name: "Pro",
        price: "₹299",
        period: "per month",
        description: "Best for regular practice",
        features: [
            "Unlimited Mock Interviews",
            "Advanced AI feedback with detailed analysis",
            "Up to 15 Questions per interview",
            "Custom job descriptions",
            "Interview history & analytics",
            "Priority email support"
        ],
        buttonText: "Upgrade to Pro",
        buttonVariant: "default",
        popular: true,
        icon: Zap,
        disabled: false
    }
]

export const faqData = [
    {
        question: "Can I cancel my subscription anytime?",
        answer: "Yes, you can cancel your subscription at any time. You'll continue to have access until the end of your billing period."
    },
    {
        question: "Is there a money-back guarantee?",
        answer: "We offer a 7-day money-back guarantee. If you're not satisfied, we'll refund your payment."
    },
    {
        question: "How does the AI feedback work?",
        answer: "Our AI analyzes your responses using Google Gemini AI and provides detailed feedback on content, structure, and delivery."
    },
    {
        question: "Can I upgrade or downgrade my plan?",
        answer: "Yes, you can change your plan at any time. Changes will be reflected in your next billing cycle."
    }
]
