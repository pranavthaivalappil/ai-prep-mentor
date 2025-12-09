import { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { ArrowLeft } from 'lucide-react';
import { interviewAPI } from '../services/api';

export default function InterviewPage() {
  const { interviewId } = useParams();
  const [interview, setInterview] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchInterview();
  }, [interviewId]);

  const fetchInterview = async () => {
    try {
      const response = await interviewAPI.getById(interviewId);
      setInterview(response.data.data);
    } catch (error) {
      console.error('Error fetching interview:', error);
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

  if (!interview) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p>Interview not found</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto">
        <Link to="/dashboard">
          <Button variant="outline" className="mb-6">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Dashboard
          </Button>
        </Link>

        <div className="bg-white rounded-lg shadow-lg p-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">{interview.jobPosition}</h1>
          <p className="text-gray-600 mb-6">{interview.jobDescription}</p>
          <p className="text-sm text-gray-500 mb-8">Experience: {interview.jobExperience} years</p>

          <div className="mb-8">
            <h2 className="text-xl font-semibold mb-4">Questions ({interview.jsonMockResp?.length || 0})</h2>
            <ul className="space-y-2">
              {interview.jsonMockResp?.map((q, index) => (
                <li key={index} className="p-4 bg-gray-50 rounded">
                  <p className="font-medium">{index + 1}. {q.question}</p>
                  <span className="text-sm text-gray-500">{q.type}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="flex space-x-4">
            <Link to={`/dashboard/interview/${interviewId}/start`} className="flex-1">
              <Button className="w-full">Start Interview</Button>
            </Link>
            <Link to={`/dashboard/interview/${interviewId}/feedback`}>
              <Button variant="outline">View Feedback</Button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

