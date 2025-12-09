import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { Brain, LogOut, Plus } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { interviewAPI } from '../services/api';

export default function DashboardPage() {
  const { user, logout } = useAuth();
  const [interviews, setInterviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showAddDialog, setShowAddDialog] = useState(false);
  const [formData, setFormData] = useState({
    jobPosition: '',
    jobDescription: '',
    jobExperience: ''
  });
  const [creating, setCreating] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    fetchInterviews();
  }, []);

  const fetchInterviews = async () => {
    try {
      const response = await interviewAPI.getAll();
      setInterviews(response.data.data);
    } catch (error) {
      console.error('Error fetching interviews:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateInterview = async (e) => {
    e.preventDefault();
    setCreating(true);
    
    try {
      const response = await interviewAPI.create(formData);
      if (response.data.success) {
        alert('Interview created successfully!');
        navigate(`/dashboard/interview/${response.data.data.mockInterviewId}`);
      }
    } catch (error) {
      alert(error.response?.data?.message || 'Error creating interview');
    } finally {
      setCreating(false);
      setShowAddDialog(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <nav className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <Brain className="h-8 w-8 text-blue-600" />
              <span className="ml-2 text-xl font-bold text-gray-900">PrepMentor</span>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-gray-700">Hello, {user?.name}</span>
              <Button variant="outline" onClick={logout}>
                <LogOut className="w-4 h-4 mr-2" />
                Logout
              </Button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900">My Interviews</h1>
          <Button onClick={() => setShowAddDialog(true)}>
            <Plus className="w-4 h-4 mr-2" />
            Create Interview
          </Button>
        </div>

        {loading ? (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          </div>
        ) : interviews.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-600">No interviews yet. Create your first interview!</p>
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {interviews.map((interview) => (
              <div key={interview._id} className="bg-white rounded-lg shadow p-6">
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{interview.jobPosition}</h3>
                <p className="text-sm text-gray-600 mb-4">{interview.jobDescription}</p>
                <Link to={`/dashboard/interview/${interview.mockInterviewId}`}>
                  <Button size="sm" className="w-full">View Details</Button>
                </Link>
              </div>
            ))}
          </div>
        )}

        {/* Add Interview Dialog */}
        {showAddDialog && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg p-8 max-w-md w-full">
              <h2 className="text-2xl font-bold mb-4">Create New Interview</h2>
              <form onSubmit={handleCreateInterview} className="space-y-4">
                <div>
                  <label className="block text-sm font-medium mb-2">Job Position</label>
                  <input
                    className="w-full p-2 border rounded"
                    placeholder="e.g., Software Engineer"
                    value={formData.jobPosition}
                    onChange={(e) => setFormData({...formData, jobPosition: e.target.value})}
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-2">Job Description</label>
                  <textarea
                    className="w-full p-2 border rounded"
                    rows={3}
                    placeholder="React, Node.js, MongoDB..."
                    value={formData.jobDescription}
                    onChange={(e) => setFormData({...formData, jobDescription: e.target.value})}
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-2">Years of Experience</label>
                  <input
                    type="number"
                    className="w-full p-2 border rounded"
                    placeholder="3"
                    value={formData.jobExperience}
                    onChange={(e) => setFormData({...formData, jobExperience: e.target.value})}
                    required
                    min="0"
                    max="50"
                  />
                </div>
                <div className="flex space-x-4">
                  <Button type="button" variant="outline" onClick={() => setShowAddDialog(false)} className="flex-1">
                    Cancel
                  </Button>
                  <Button type="submit" disabled={creating} className="flex-1">
                    {creating ? 'Creating...' : 'Create'}
                  </Button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

