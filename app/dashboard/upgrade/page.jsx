'use client'
import React from 'react'
import { Button } from '../../../components/ui/button'
import { Check } from 'lucide-react'
import { planData, faqData } from '../../../utils/planData'

function UpgradePage() {
    return (
        <div className="py-12">
            <div className="text-center mb-12">
                <h1 className="text-4xl font-bold text-gray-900 mb-4">
                    Choose Your Plan
                </h1>
                <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                    Upgrade your interview preparation with AI-powered feedback and advanced features
                </p>
            </div>

            <div className="flex justify-center">
                <div className="grid md:grid-cols-2 gap-8 max-w-4xl">
                    {planData.map((plan, index) => {
                        const IconComponent = plan.icon
                        return (
                            <div 
                                key={plan.id} 
                                className={`relative bg-white rounded-2xl shadow-lg border-2 p-8 w-80 ${
                                    plan.popular 
                                        ? 'border-blue-500 transform scale-105' 
                                        : 'border-gray-200'
                                }`}
                            >
                                {plan.popular && (
                                    <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                                        <span className="bg-blue-500 text-white px-4 py-2 rounded-full text-sm font-semibold">
                                            Most Popular
                                        </span>
                                    </div>
                                )}

                                <div className="text-center mb-8">
                                    <div className="flex justify-center mb-4">
                                        <div className={`p-3 rounded-full ${
                                            plan.popular 
                                                ? 'bg-blue-100 text-blue-600' 
                                                : 'bg-gray-100 text-gray-600'
                                        }`}>
                                            <IconComponent className="w-6 h-6" />
                                        </div>
                                    </div>
                                    
                                    <h3 className="text-2xl font-bold text-gray-900 mb-2">
                                        {plan.name}
                                    </h3>
                                    
                                    <div className="mb-4">
                                        <span className="text-4xl font-bold text-gray-900">
                                            {plan.price}
                                        </span>
                                        <span className="text-gray-600 ml-1">
                                            /{plan.period}
                                        </span>
                                    </div>
                                    
                                    <p className="text-gray-600">
                                        {plan.description}
                                    </p>
                                </div>

                                <ul className="space-y-4 mb-8">
                                    {plan.features.map((feature, featureIndex) => (
                                        <li key={featureIndex} className="flex items-start">
                                            <Check className="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" />
                                            <span className="text-gray-700">{feature}</span>
                                        </li>
                                    ))}
                                </ul>

                                <Button 
                                    variant={plan.buttonVariant}
                                    className={`w-full py-3 text-lg font-semibold ${
                                        plan.popular 
                                            ? 'bg-blue-600 hover:bg-blue-700 text-white' 
                                            : ''
                                    }`}
                                    disabled={plan.disabled}
                                >
                                    {plan.buttonText}
                                </Button>
                            </div>
                        )
                    })}
                </div>
            </div>

            {/* FAQ Section */}
            <div className="mt-16 max-w-4xl mx-auto">
                <h2 className="text-2xl font-bold text-center text-gray-900 mb-8">
                    Frequently Asked Questions
                </h2>
                
                <div className="grid md:grid-cols-2 gap-8">
                    {faqData.map((faq, index) => (
                        <div key={index}>
                            <h3 className="font-semibold text-gray-900 mb-2">
                                {faq.question}
                            </h3>
                            <p className="text-gray-600">
                                {faq.answer}
                            </p>
                        </div>
                    ))}
                </div>
            </div>

            {/* Contact Section */}
            <div className="mt-12 text-center">
                <p className="text-gray-600">
                    Have questions? <span className="text-blue-600 font-medium cursor-pointer hover:underline">Contact our support team</span>
                </p>
            </div>
        </div>
    )
}

export default UpgradePage 