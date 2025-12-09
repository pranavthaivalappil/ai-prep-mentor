const Interview = require('../models/Interview');
const UserAnswer = require('../models/UserAnswer');
const { generateInterviewQuestions } = require('../services/gemini.service');
const { v4: uuidv4 } = require('uuid');

/**
 * @desc    Create a new interview
 * @route   POST /api/interviews/create
 * @access  Private
 */
exports.createInterview = async (req, res) => {
  try {
    const { jobPosition, jobDescription, jobExperience } = req.body;

    // Validation
    if (!jobPosition || !jobDescription || jobExperience === undefined) {
      return res.status(400).json({
        success: false,
        message: 'Please provide all required fields: jobPosition, jobDescription, jobExperience'
      });
    }

    console.log('Creating interview for:', { jobPosition, jobExperience, userId: req.user._id });

    // Generate questions using Gemini AI
    const result = await generateInterviewQuestions(
      jobPosition,
      jobDescription,
      jobExperience
    );

    if (!result.success) {
      return res.status(500).json({
        success: false,
        message: 'Failed to generate interview questions',
        error: result.error
      });
    }

    // Create interview in MongoDB
    const interview = await Interview.create({
      mockInterviewId: uuidv4(),
      jsonMockResp: result.data,
      jobPosition,
      jobDescription,
      jobExperience,
      createdBy: req.user._id,
      status: 'pending'
    });

    console.log('✅ Interview created:', interview.mockInterviewId);

    res.status(201).json({
      success: true,
      message: 'Interview created successfully',
      data: interview
    });

  } catch (error) {
    console.error('Create interview error:', error);
    res.status(500).json({
      success: false,
      message: error.message || 'Error creating interview'
    });
  }
};

/**
 * @desc    Get all interviews for the current user
 * @route   GET /api/interviews
 * @access  Private
 */
exports.getUserInterviews = async (req, res) => {
  try {
    const interviews = await Interview.find({ createdBy: req.user._id })
      .sort({ createdAt: -1 })
      .select('-jsonMockResp'); // Exclude questions for list view

    res.json({
      success: true,
      count: interviews.length,
      data: interviews
    });
  } catch (error) {
    console.error('Get interviews error:', error);
    res.status(500).json({
      success: false,
      message: 'Error fetching interviews'
    });
  }
};

/**
 * @desc    Get a single interview by ID
 * @route   GET /api/interviews/:interviewId
 * @access  Private
 */
exports.getInterviewById = async (req, res) => {
  try {
    const interview = await Interview.findOne({
      mockInterviewId: req.params.interviewId,
      createdBy: req.user._id
    });

    if (!interview) {
      return res.status(404).json({
        success: false,
        message: 'Interview not found'
      });
    }

    res.json({
      success: true,
      data: interview
    });
  } catch (error) {
    console.error('Get interview error:', error);
    res.status(500).json({
      success: false,
      message: 'Error fetching interview'
    });
  }
};

/**
 * @desc    Update interview status
 * @route   PUT /api/interviews/:interviewId/status
 * @access  Private
 */
exports.updateInterviewStatus = async (req, res) => {
  try {
    const { status } = req.body;

    if (!['pending', 'in-progress', 'completed'].includes(status)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid status value'
      });
    }

    const interview = await Interview.findOneAndUpdate(
      {
        mockInterviewId: req.params.interviewId,
        createdBy: req.user._id
      },
      {
        status,
        ...(status === 'completed' && { completedAt: new Date() })
      },
      { new: true }
    );

    if (!interview) {
      return res.status(404).json({
        success: false,
        message: 'Interview not found'
      });
    }

    res.json({
      success: true,
      message: 'Interview status updated',
      data: interview
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Error updating interview status'
    });
  }
};

/**
 * @desc    Delete an interview
 * @route   DELETE /api/interviews/:interviewId
 * @access  Private
 */
exports.deleteInterview = async (req, res) => {
  try {
    const interview = await Interview.findOneAndDelete({
      mockInterviewId: req.params.interviewId,
      createdBy: req.user._id
    });

    if (!interview) {
      return res.status(404).json({
        success: false,
        message: 'Interview not found'
      });
    }

    // Also delete associated answers
    await UserAnswer.deleteMany({ mockInterviewId: req.params.interviewId });

    res.json({
      success: true,
      message: 'Interview deleted successfully'
    });
  } catch (error) {
    console.error('Delete interview error:', error);
    res.status(500).json({
      success: false,
      message: 'Error deleting interview'
    });
  }
};

/**
 * @desc    Get interview statistics
 * @route   GET /api/interviews/stats
 * @access  Private
 */
exports.getInterviewStats = async (req, res) => {
  try {
    const totalInterviews = await Interview.countDocuments({ createdBy: req.user._id });
    const completedInterviews = await Interview.countDocuments({
      createdBy: req.user._id,
      status: 'completed'
    });

    // Get average rating
    const answers = await UserAnswer.find({ userId: req.user._id });
    const ratings = answers
      .filter(a => a.rating && !isNaN(parseInt(a.rating)))
      .map(a => parseInt(a.rating));

    const averageRating = ratings.length > 0
      ? ratings.reduce((sum, r) => sum + r, 0) / ratings.length
      : 0;

    res.json({
      success: true,
      stats: {
        totalInterviews,
        completedInterviews,
        pendingInterviews: totalInterviews - completedInterviews,
        averageRating: Math.round(averageRating * 10) / 10,
        totalAnswers: answers.length
      }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Error fetching statistics'
    });
  }
};

