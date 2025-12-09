'use client'
import { Button } from "../components/ui/button";
import Link from "next/link";
import { Check, Star, Zap, Brain, Target, BarChart3, Clock, Users } from "lucide-react";
import { useAuth } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function Home() {
  const { isSignedIn, isLoaded } = useAuth();
  const router = useRouter();

  // Removed auto-redirect to allow visiting home page while signed in
  // and to fix back navigation issues
  const features = [
    {
      icon: Brain,
      title: "AI-Powered Feedback",
      description: "Get detailed, personalized feedback on your interview responses using advanced AI technology."
    },
    {
      icon: Target,
      title: "Realistic Mock Interviews",
      description: "Practice with industry-specific questions tailored to your target job role and experience level."
    },
    {
      icon: BarChart3,
      title: "Performance Analytics",
      description: "Track your progress over time with detailed analytics and improvement suggestions."
    },
    {
      icon: Clock,
      title: "Flexible Scheduling",
      description: "Practice anytime, anywhere. No need to coordinate with human interviewers."
    }
  ];

  const steps = [
    {
      step: "1",
      title: "Sign Up & Set Goals",
      description: "Create your account and tell us about your target role and experience level."
    },
    {
      step: "2",
      title: "Take Mock Interviews",
      description: "Answer AI-generated questions specific to your industry and position."
    },
    {
      step: "3",
      title: "Get AI Feedback",
      description: "Receive detailed analysis on your responses, body language, and communication skills."
    },
    {
      step: "4",
      title: "Improve & Succeed",
      description: "Apply the feedback and track your improvement until you land your dream job."
    }
  ];



  const faq = [
    {
      question: "How does the AI feedback work?",
      answer: "Our AI analyzes your responses using Google Gemini AI, evaluating content quality, structure, relevance, and communication effectiveness to provide detailed, actionable feedback."
    },
    {
      question: "Can I practice for specific job roles?",
      answer: "Yes! You can customize your mock interviews based on job descriptions, industry, experience level, and specific skills you want to focus on."
    },
    {
      question: "Is there a free trial?",
      answer: "Yes, we offer a free plan with 3 mock interviews per month and basic AI feedback to help you get started."
    },
    {
      question: "How accurate is the AI feedback?",
      answer: "Our AI is trained on thousands of successful interview responses and provides feedback comparable to experienced human interviewers, with the added benefit of consistency and availability 24/7."
    }
  ];

  return (
    <div className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className="border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <div className="flex-shrink-0 flex items-center">
                <Brain className="h-8 w-8 text-blue-600" />
                <span className="ml-2 text-xl font-bold text-gray-900">PrepMentor</span>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              {isSignedIn ? (
                <Link href="/dashboard">
                  <Button>Dashboard</Button>
                </Link>
              ) : (
                <>
              <Link href="/sign-in">
                <Button variant="outline">Sign In</Button>
              </Link>
              <Link href="/sign-up">
                <Button>Get Started</Button>
              </Link>
                </>
              )}
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative bg-gradient-to-r from-blue-600 to-purple-700">
        <div className="absolute inset-0 bg-black opacity-50"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 text-center">
          <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">
            Ace Your Next Interview with 
            <span className="block text-yellow-400">AI-Powered Practice</span>
          </h1>
          <p className="text-xl text-gray-200 max-w-3xl mx-auto mb-8">
            Get personalized feedback, practice with realistic scenarios, and boost your confidence 
            with our advanced AI interview preparation platform.
          </p>
          <div className="space-x-4">
            <Link href="/sign-up">
              <Button size="lg" className="bg-yellow-500 hover:bg-yellow-600 text-black font-semibold">
                Start Free Trial
              </Button>
            </Link>
            <Link href="#features">
              <Button size="lg" variant="outline" className="text-white border-white/80 bg-white/10 backdrop-blur-sm hover:bg-white/20 hover:border-yellow-400 hover:text-yellow-400 transition-all duration-300">
                Learn More
              </Button>
            </Link>
          </div>
          <div className="mt-8 flex justify-center items-center space-x-8 text-gray-300">
            <div className="flex items-center">
              <Users className="w-5 h-5 mr-2" />
              <span>10,000+ Users</span>
            </div>
            <div className="flex items-center">
              <Star className="w-5 h-5 mr-2 text-yellow-400" />
              <span>4.9/5 Rating</span>
            </div>
            <div className="flex items-center">
              <Check className="w-5 h-5 mr-2 text-green-400" />
              <span>AI-Powered</span>
            </div>
          </div>
          
          {/* Made with Love */}
          <div className="mt-12 pt-8 border-t border-white/20">
            <p className="text-blue-100 text-sm">
              Made with ❤️ by <span className="font-semibold text-white">Pranav</span>
            </p>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Why Choose PrepMentor?
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Our platform combines cutting-edge AI technology with proven interview techniques 
              to give you the edge in your job search.
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => {
              const IconComponent = feature.icon;
              return (
                <div key={index} className="text-center">
                  <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <IconComponent className="w-8 h-8 text-blue-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-2">{feature.title}</h3>
                  <p className="text-gray-600">{feature.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              How It Works
            </h2>
            <p className="text-xl text-gray-600">
              Get started in minutes and see improvement in your interview skills
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {steps.map((step, index) => (
              <div key={index} className="text-center">
                <div className="bg-blue-600 text-white w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                  {step.step}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">{step.title}</h3>
                <p className="text-gray-600">{step.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Simple, Transparent Pricing
            </h2>
            <p className="text-xl text-gray-600">
              Choose the plan that fits your interview preparation needs
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
            {/* Free Plan */}
            <div className="bg-white rounded-2xl shadow-lg border-2 border-gray-200 p-8">
              <div className="text-center mb-8">
                <Star className="w-12 h-12 text-gray-600 mx-auto mb-4" />
                <h3 className="text-2xl font-bold text-gray-900 mb-2">Free</h3>
                <div className="mb-4">
                  <span className="text-4xl font-bold text-gray-900">₹0</span>
                  <span className="text-gray-600 ml-1">/forever</span>
                </div>
                <p className="text-gray-600">Perfect for getting started</p>
              </div>
              
              <ul className="space-y-4 mb-8">
                <li className="flex items-start">
                  <Check className="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">3 Mock Interviews per month</span>
                </li>
                <li className="flex items-start">
                  <Check className="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">Basic AI feedback</span>
                </li>
                <li className="flex items-start">
                  <Check className="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">5 Questions per interview</span>
                </li>
              </ul>
              
              <Link href="/sign-up">
                <Button variant="outline" className="w-full py-3 text-lg">
                  Get Started Free
                </Button>
              </Link>
            </div>

            {/* Pro Plan */}
            <div className="bg-white rounded-2xl shadow-lg border-2 border-blue-500 p-8 relative transform scale-105">
              <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                <span className="bg-blue-500 text-white px-4 py-2 rounded-full text-sm font-semibold">
                  Most Popular
                </span>
              </div>
              
              <div className="text-center mb-8">
                <Zap className="w-12 h-12 text-blue-600 mx-auto mb-4" />
                <h3 className="text-2xl font-bold text-gray-900 mb-2">Pro</h3>
                <div className="mb-4">
                  <span className="text-4xl font-bold text-gray-900">₹299</span>
                  <span className="text-gray-600 ml-1">/month</span>
                </div>
                <p className="text-gray-600">Best for regular practice</p>
              </div>
              
              <ul className="space-y-4 mb-8">
                <li className="flex items-start">
                  <Check className="w-5 h-5 text-gray-400 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-500 italic">Unlimited Mock Interviews - To be implemented in future</span>
                </li>
                <li className="flex items-start">
                  <Check className="w-5 h-5 text-gray-400 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-500 italic">Advanced AI feedback with detailed analysis - To be implemented in future</span>
                </li>
                <li className="flex items-start">
                  <Check className="w-5 h-5 text-gray-400 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-500 italic">Up to 15 Questions per interview - To be implemented in future</span>
                </li>

                <li className="flex items-start">
                  <Check className="w-5 h-5 text-gray-400 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-500 italic">Priority email support - To be implemented in future</span>
                </li>
              </ul>
              
              <Link href="/dashboard/upgrade">
                <Button className="w-full py-3 text-lg bg-blue-600 hover:bg-blue-700">
                  Upgrade to Pro
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>



      {/* FAQ */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Frequently Asked Questions
            </h2>
          </div>
          
          <div className="space-y-8">
            {faq.map((item, index) => (
              <div key={index} className="bg-white rounded-lg p-6 shadow-md">
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{item.question}</h3>
                <p className="text-gray-600">{item.answer}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-blue-600">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
            Ready to Ace Your Next Interview?
          </h2>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Join thousands of job seekers who have improved their interview skills and landed their dream jobs.
          </p>
          <Link href="/sign-up">
            <Button size="lg" className="bg-yellow-500 hover:bg-yellow-600 text-black font-semibold mr-4">
              Start Free Trial
            </Button>
          </Link>
          <Link href="/sign-in">
            <Button size="lg" variant="outline">
              Sign In
            </Button>
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div className="col-span-2">
              <div className="flex items-center mb-4">
                <Brain className="h-8 w-8 text-blue-400" />
                <span className="ml-2 text-xl font-bold">PrepMentor</span>
              </div>
              <p className="text-gray-400 max-w-md">
                Empowering job seekers with AI-powered interview preparation. 
                Practice, improve, and succeed in your career journey.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4">Product</h3>
              <ul className="space-y-2 text-gray-400">
                <li><Link href="#features" className="hover:text-white">Features</Link></li>
                <li><Link href="#pricing" className="hover:text-white">Pricing</Link></li>
                <li><Link href="/sign-up" className="hover:text-white">Sign Up</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4">Support</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white">Help Center</a></li>
                <li><a href="#" className="hover:text-white">Contact Us</a></li>
                <li><a href="#" className="hover:text-white">Privacy Policy</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2025 PrepMentor. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
