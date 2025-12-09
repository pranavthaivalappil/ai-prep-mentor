const express = require('express');
const router = express.Router();
const {
  submitAnswer,
  getFeedback,
  generateFeedbackForAnswer,
  getInterviewAnswers
} = require('../controllers/feedbackController');
const { protect } = require('../middleware/auth.middleware');

// All routes are protected
router.use(protect);

// Feedback routes
router.post('/submit', submitAnswer);
router.get('/:interviewId', getFeedback);
router.get('/:interviewId/answers', getInterviewAnswers);
router.post('/generate/:answerId', generateFeedbackForAnswer);

module.exports = router;

