'use client'
import React from 'react'
import { CheckCircle, ArrowRight } from 'lucide-react'
import { Button } from '../../../components/ui/button'
import Link from 'next/link'

function PaymentSuccessPage() {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 to-blue-50 px-4">
            <div className="max-w-md w-full bg-white rounded-2xl shadow-lg p-8 text-center">
                <div className="mb-6">
                    <CheckCircle className="w-16 h-16 text-green-500 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-gray-900 mb-2">
                        Payment Successful!
                    </h1>
                    <p className="text-gray-600">
                        Your subscription has been activated successfully. You now have access to all Pro features.
                    </p>
                </div>

                <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
                    <h3 className="font-semibold text-green-800 mb-2">
                        What's Next?
                    </h3>
                    <ul className="text-sm text-green-700 space-y-1 text-left">
                        <li>• Unlimited mock interviews</li>
                        <li>• Advanced AI feedback</li>
                        <li>• Up to 15 questions per interview</li>
                        <li>• Custom job descriptions</li>
                        <li>• Priority support</li>
                    </ul>
                </div>

                <div className="space-y-3">
                    <Link href="/dashboard" className="block">
                        <Button className="w-full bg-blue-600 hover:bg-blue-700 text-white">
                            Go to Dashboard
                            <ArrowRight className="w-4 h-4 ml-2" />
                        </Button>
                    </Link>
                    
                    <Link href="/dashboard/interview/new" className="block">
                        <Button variant="outline" className="w-full">
                            Start Your First Pro Interview
                        </Button>
                    </Link>
                </div>

                <div className="mt-6 pt-4 border-t border-gray-200">
                    <p className="text-sm text-gray-500">
                        Need help? <span className="text-blue-600 cursor-pointer hover:underline">Contact Support</span>
                    </p>
                </div>
            </div>
        </div>
    )
}

export default PaymentSuccessPage 