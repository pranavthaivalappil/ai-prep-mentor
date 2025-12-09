const UserAnswer = require('../models/UserAnswer');
const Interview = require('../models/Interview');
const { generateFeedback } = require('../services/gemini.service');

/**
 * @desc    Submit an answer for a question
 * @route   POST /api/feedback/submit
 * @access  Private
 */
exports.submitAnswer = async (req, res) => {
  try {
    const { mockInterviewId, question, userAns, correctAns } = req.body;

    // Validation
    if (!mockInterviewId || !question || !userAns) {
      return res.status(400).json({
        success: false,
        message: 'Please provide mockInterviewId, question, and userAns'
      });
    }

    // Verify the interview belongs to the user
    const interview = await Interview.findOne({
      mockInterviewId,
      createdBy: req.user._id
    });

    if (!interview) {
      return res.status(404).json({
        success: false,
        message: 'Interview not found'
      });
    }

    // Create the answer
    const answer = await UserAnswer.create({
      mockInterviewId,
      question,
      correctAns: correctAns || '',
      userAns,
      userId: req.user._id
    });

    console.log('✅ Answer submitted for interview:', mockInterviewId);

    res.status(201).json({
      success: true,
      message: 'Answer submitted successfully',
      data: answer
    });

  } catch (error) {
    console.error('Submit answer error:', error);
    res.status(500).json({
      success: false,
      message: error.message || 'Error submitting answer'
    });
  }
};

/**
 * @desc    Get feedback for an interview
 * @route   GET /api/feedback/:interviewId
 * @access  Private
 */
exports.getFeedback = async (req, res) => {
  try {
    const { interviewId } = req.params;

    // Get interview details
    const interview = await Interview.findOne({
      mockInterviewId: interviewId,
      createdBy: req.user._id
    });

    if (!interview) {
      return res.status(404).json({
        success: false,
        message: 'Interview not found'
      });
    }

    // Get all answers for this interview
    let answers = await UserAnswer.find({
      mockInterviewId: interviewId,
      userId: req.user._id
    }).sort({ createdAt: 1 });

    // Generate feedback for answers that don't have it yet
    const feedbackPromises = answers.map(async (answer) => {
      if (!answer.feedback && answer.userAns && answer.userAns.length > 10) {
        try {
          console.log('🤖 Generating feedback for answer:', answer._id);
          
          const feedbackResp = await generateFeedback(
            answer.question,
            answer.userAns,
            interview.jobPosition
          );

          if (feedbackResp.success) {
            const feedbackData = feedbackResp.data;

            // Update the answer with feedback
            answer.feedback = feedbackData.feedback;
            answer.rating = feedbackData.rating;
            answer.assessment = feedbackData.assessment;
            answer.strengths = feedbackData.strengths;
            answer.improvements = feedbackData.improvements;
            answer.suggestions = feedbackData.suggestions;

            await answer.save();

            return answer;
          }
        } catch (error) {
          console.error('Error generating feedback for answer:', error);
          // Return answer without feedback if generation fails
          return answer;
        }
      }
      return answer;
    });

    // Wait for all feedback to be generated
    answers = await Promise.all(feedbackPromises);

    // Calculate overall rating
    const validRatings = answers
      .filter(a => a.rating && !isNaN(parseInt(a.rating)))
      .map(a => parseInt(a.rating));

    const overallRating = validRatings.length > 0
      ? validRatings.reduce((sum, r) => sum + r, 0) / validRatings.length
      : 0;

    res.json({
      success: true,
      data: {
        interview: {
          jobPosition: interview.jobPosition,
          jobDescription: interview.jobDescription,
          jobExperience: interview.jobExperience
        },
        answers,
        overallRating: Math.round(overallRating * 10) / 10,
        totalQuestions: answers.length
      }
    });

  } catch (error) {
    console.error('Get feedback error:', error);
    res.status(500).json({
      success: false,
      message: 'Error fetching feedback'
    });
  }
};

/**
 * @desc    Generate feedback for a specific answer
 * @route   POST /api/feedback/generate/:answerId
 * @access  Private
 */
exports.generateFeedbackForAnswer = async (req, res) => {
  try {
    const { answerId } = req.params;

    // Get the answer
    const answer = await UserAnswer.findOne({
      _id: answerId,
      userId: req.user._id
    });

    if (!answer) {
      return res.status(404).json({
        success: false,
        message: 'Answer not found'
      });
    }

    // Get interview details
    const interview = await Interview.findOne({
      mockInterviewId: answer.mockInterviewId
    });

    if (!interview) {
      return res.status(404).json({
        success: false,
        message: 'Interview not found'
      });
    }

    // Generate feedback
    const feedbackResp = await generateFeedback(
      answer.question,
      answer.userAns,
      interview.jobPosition
    );

    if (!feedbackResp.success) {
      return res.status(500).json({
        success: false,
        message: 'Failed to generate feedback'
      });
    }

    const feedbackData = feedbackResp.data;

    // Update answer with feedback
    answer.feedback = feedbackData.feedback;
    answer.rating = feedbackData.rating;
    answer.assessment = feedbackData.assessment;
    answer.strengths = feedbackData.strengths;
    answer.improvements = feedbackData.improvements;
    answer.suggestions = feedbackData.suggestions;

    await answer.save();

    res.json({
      success: true,
      message: 'Feedback generated successfully',
      data: answer
    });

  } catch (error) {
    console.error('Generate feedback error:', error);
    res.status(500).json({
      success: false,
      message: 'Error generating feedback'
    });
  }
};

/**
 * @desc    Get all answers for an interview
 * @route   GET /api/feedback/:interviewId/answers
 * @access  Private
 */
exports.getInterviewAnswers = async (req, res) => {
  try {
    const { interviewId } = req.params;

    const answers = await UserAnswer.find({
      mockInterviewId: interviewId,
      userId: req.user._id
    }).sort({ createdAt: 1 });

    res.json({
      success: true,
      count: answers.length,
      data: answers
    });

  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Error fetching answers'
    });
  }
};

