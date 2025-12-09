import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { Home, Star } from 'lucide-react';
import { feedbackAPI } from '../services/api';

export default function FeedbackPage() {
  const { interviewId } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchFeedback();
  }, [interviewId]);

  const fetchFeedback = async () => {
    try {
      const response = await feedbackAPI.getFeedback(interviewId);
      setData(response.data.data);
    } catch (error) {
      console.error('Error fetching feedback:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-8 mb-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">Interview Feedback</h1>
          <p className="text-gray-600 mb-6">{data?.interview?.jobPosition}</p>

          <div className="flex items-center justify-center mb-8">
            <div className="text-center">
              <div className="flex items-center justify-center mb-2">
                <Star className="w-12 h-12 text-yellow-500" />
              </div>
              <p className="text-4xl font-bold text-gray-900">{data?.overallRating}/10</p>
              <p className="text-gray-600">Overall Rating</p>
            </div>
          </div>
        </div>

        {data?.answers?.map((answer, index) => (
          <div key={index} className="bg-white rounded-lg shadow-lg p-8 mb-6">
            <h3 className="text-lg font-semibold mb-4">Question {index + 1}: {answer.question}</h3>
            
            <div className="mb-4">
              <p className="text-sm font-medium text-gray-700 mb-2">Your Answer:</p>
              <p className="text-gray-900 bg-blue-50 p-4 rounded">{answer.userAns}</p>
            </div>

            {answer.feedback && (
              <>
                <div className="mb-4">
                  <p className="text-sm font-medium text-gray-700 mb-2">Rating: {answer.rating}/10</p>
                </div>
                <div className="mb-4">
                  <p className="text-sm font-medium text-gray-700 mb-2">Feedback:</p>
                  <p className="text-gray-900 bg-green-50 p-4 rounded">{answer.feedback}</p>
                </div>
              </>
            )}
          </div>
        ))}

        <div className="flex justify-center space-x-4">
          <Link to="/dashboard">
            <Button>
              <Home className="w-4 h-4 mr-2" />
              Back to Dashboard
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

