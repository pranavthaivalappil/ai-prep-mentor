import { Link } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { Brain, Star, Target, BarChart3, Clock } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function HomePage() {
  const { isAuthenticated } = useAuth();

  const features = [
    {
      icon: Brain,
      title: "AI-Powered Feedback",
      description: "Get detailed, personalized feedback using advanced AI technology."
    },
    {
      icon: Target,
      title: "Realistic Mock Interviews",
      description: "Practice with industry-specific questions tailored to your role."
    },
    {
      icon: BarChart3,
      title: "Performance Analytics",
      description: "Track your progress with detailed analytics."
    },
    {
      icon: Clock,
      title: "Flexible Scheduling",
      description: "Practice anytime, anywhere."
    }
  ];

  return (
    <div className="min-h-screen bg-white">
      <nav className="border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <Brain className="h-8 w-8 text-blue-600" />
              <span className="ml-2 text-xl font-bold text-gray-900">PrepMentor</span>
            </div>
            <div className="flex items-center space-x-4">
              {isAuthenticated ? (
                <Link to="/dashboard">
                  <Button>Dashboard</Button>
                </Link>
              ) : (
                <>
                  <Link to="/login">
                    <Button variant="outline">Sign In</Button>
                  </Link>
                  <Link to="/signup">
                    <Button>Get Started</Button>
                  </Link>
                </>
              )}
            </div>
          </div>
        </div>
      </nav>

      <section className="relative bg-gradient-to-r from-blue-600 to-purple-700">
        <div className="absolute inset-0 bg-black opacity-50"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 text-center">
          <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">
            Ace Your Next Interview with 
            <span className="block text-yellow-400">AI-Powered Practice</span>
          </h1>
          <p className="text-xl text-gray-200 max-w-3xl mx-auto mb-8">
            Get personalized feedback, practice with realistic scenarios, and boost your confidence
          </p>
          <Link to="/signup">
            <Button size="lg" className="bg-yellow-500 hover:bg-yellow-600 text-black font-semibold">
              Start Free Trial
            </Button>
          </Link>
        </div>
      </section>

      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Why Choose PrepMentor?
            </h2>
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

      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <div className="flex items-center justify-center mb-4">
            <Brain className="h-8 w-8 text-blue-400" />
            <span className="ml-2 text-xl font-bold">PrepMentor</span>
          </div>
          <p className="text-gray-500 mt-4">© 2025 PrepMentor. Made with ❤️ by Pranav</p>
        </div>
      </footer>
    </div>
  );
}

