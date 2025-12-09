const express = require('express');
const router = express.Router();
const {
  createInterview,
  getUserInterviews,
  getInterviewById,
  updateInterviewStatus,
  deleteInterview,
  getInterviewStats
} = require('../controllers/interviewController');
const { protect, checkInterviewLimit } = require('../middleware/auth.middleware');

// All routes are protected
router.use(protect);

// Interview routes
router.post('/create', checkInterviewLimit, createInterview);
router.get('/', getUserInterviews);
router.get('/stats', getInterviewStats);
router.get('/:interviewId', getInterviewById);
router.put('/:interviewId/status', updateInterviewStatus);
router.delete('/:interviewId', deleteInterview);

module.exports = router;

