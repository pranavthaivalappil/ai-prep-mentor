import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { interviewAPI, feedbackAPI } from '../services/api';

export default function StartInterviewPage() {
  const { interviewId } = useParams();
  const [interview, setInterview] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    fetchInterview();
  }, [interviewId]);

  const fetchInterview = async () => {
    try {
      const response = await interviewAPI.getById(interviewId);
      setInterview(response.data.data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmitAnswer = async () => {
    if (!answer.trim()) {
      alert('Please provide an answer');
      return;
    }

    setSubmitting(true);
    try {
      await feedbackAPI.submitAnswer({
        mockInterviewId: interviewId,
        question: interview.jsonMockResp[currentQuestion].question,
        userAns: answer
      });

      if (currentQuestion < interview.jsonMockResp.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
        setAnswer('');
      } else {
        // Interview complete
        navigate(`/dashboard/interview/${interviewId}/feedback`);
      }
    } catch (error) {
      alert('Error submitting answer');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  const question = interview?.jsonMockResp[currentQuestion];

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-8">
          <div className="mb-6">
            <p className="text-sm text-gray-500 mb-2">
              Question {currentQuestion + 1} of {interview?.jsonMockResp?.length}
            </p>
            <h2 className="text-2xl font-bold text-gray-900">{question?.question}</h2>
            <span className="text-sm text-gray-500 mt-2 inline-block">Type: {question?.type}</span>
          </div>

          <div className="mb-6">
            <label className="block text-sm font-medium mb-2">Your Answer:</label>
            <textarea
              className="w-full p-4 border rounded-lg min-h-[200px]"
              placeholder="Type your answer here..."
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              disabled={submitting}
            />
          </div>

          <div className="flex justify-end space-x-4">
            <Button
              variant="outline"
              onClick={() => navigate(`/dashboard/interview/${interviewId}`)}
              disabled={submitting}
            >
              Cancel
            </Button>
            <Button onClick={handleSubmitAnswer} disabled={submitting}>
              {submitting ? 'Submitting...' : 
               currentQuestion < interview.jsonMockResp.length - 1 ? 'Next Question' : 'Finish Interview'}
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}

