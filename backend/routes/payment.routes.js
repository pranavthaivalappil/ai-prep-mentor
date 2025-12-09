const express = require('express');
const router = express.Router();
const {
  createOrder,
  verifyPayment,
  getPaymentHistory
} = require('../controllers/paymentController');
const { protect } = require('../middleware/auth.middleware');

// All routes are protected
router.use(protect);

// Payment routes
router.post('/create-order', createOrder);
router.post('/verify', verifyPayment);
router.get('/history', getPaymentHistory);

module.exports = router;

