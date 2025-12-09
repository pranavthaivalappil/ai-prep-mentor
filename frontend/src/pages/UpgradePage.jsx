import { Link } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { Check, Zap, ArrowLeft } from 'lucide-react';

export default function UpgradePage() {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto">
        <Link to="/dashboard">
          <Button variant="outline" className="mb-6">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Dashboard
          </Button>
        </Link>

        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Upgrade to Pro</h1>
          <p className="text-xl text-gray-600">Unlock unlimited interviews and advanced features</p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          <div className="bg-white rounded-lg shadow-lg p-8 border-2 border-gray-200">
            <h3 className="text-2xl font-bold mb-4">Free Plan</h3>
            <p className="text-3xl font-bold mb-6">₹0<span className="text-base font-normal text-gray-600">/forever</span></p>
            <ul className="space-y-3 mb-6">
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>3 Mock Interviews per month</span>
              </li>
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>Basic AI feedback</span>
              </li>
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>5 Questions per interview</span>
              </li>
            </ul>
            <Button variant="outline" className="w-full" disabled>Current Plan</Button>
          </div>

          <div className="bg-white rounded-lg shadow-lg p-8 border-2 border-blue-500 relative">
            <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
              <span className="bg-blue-500 text-white px-4 py-1 rounded-full text-sm font-semibold">
                Most Popular
              </span>
            </div>
            <div className="flex items-center mb-4">
              <Zap className="w-8 h-8 text-blue-600 mr-2" />
              <h3 className="text-2xl font-bold">Pro Plan</h3>
            </div>
            <p className="text-3xl font-bold mb-6">₹299<span className="text-base font-normal text-gray-600">/month</span></p>
            <ul className="space-y-3 mb-6">
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>Unlimited Mock Interviews</span>
              </li>
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>Advanced AI feedback</span>
              </li>
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>Up to 15 Questions per interview</span>
              </li>
              <li className="flex items-start">
                <Check className="w-5 h-5 text-green-500 mr-2 mt-0.5" />
                <span>Priority support</span>
              </li>
            </ul>
            <Button className="w-full bg-blue-600 hover:bg-blue-700">
              Upgrade Now
            </Button>
            <p className="text-sm text-gray-500 text-center mt-4">
              Payment integration coming soon
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

