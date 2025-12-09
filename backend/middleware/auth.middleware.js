const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Protect routes - verify JWT token
exports.protect = async (req, res, next) => {
  try {
    let token;
    
    // Get token from Authorization header
    if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
      token = req.headers.authorization.split(' ')[1];
    }
    
    // Check if token exists
    if (!token) {
      return res.status(401).json({ 
        success: false, 
        message: 'Not authorized to access this route. Please login.' 
      });
    }
    
    try {
      // Verify token
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      
      // Get user from database (exclude password)
      req.user = await User.findById(decoded.id).select('-password');
      
      if (!req.user) {
        return res.status(401).json({ 
          success: false, 
          message: 'User not found' 
        });
      }
      
      next();
    } catch (error) {
      return res.status(401).json({ 
        success: false, 
        message: 'Not authorized, token failed' 
      });
    }
    
  } catch (error) {
    console.error('Auth middleware error:', error);
    res.status(500).json({ 
      success: false, 
      message: 'Server error in authentication' 
    });
  }
};

// Restrict to specific subscription types
exports.restrictTo = (...subscriptionTypes) => {
  return (req, res, next) => {
    if (!subscriptionTypes.includes(req.user.subscriptionType)) {
      return res.status(403).json({
        success: false,
        message: 'You do not have permission to perform this action. Please upgrade your subscription.'
      });
    }
    next();
  };
};

// Check interview limit for free users
exports.checkInterviewLimit = async (req, res, next) => {
  try {
    if (req.user.subscriptionType === 'free') {
      const monthStart = new Date();
      monthStart.setDate(1);
      monthStart.setHours(0, 0, 0, 0);
      
      const Interview = require('../models/Interview');
      const interviewCount = await Interview.countDocuments({
        createdBy: req.user._id,
        createdAt: { $gte: monthStart }
      });
      
      if (interviewCount >= 3) {
        return res.status(403).json({
          success: false,
          message: 'You have reached your monthly interview limit (3). Please upgrade to Pro for unlimited interviews.',
          limit: true
        });
      }
    }
    next();
  } catch (error) {
    console.error('Interview limit check error:', error);
    next(error);
  }
};

// Generate JWT token
exports.generateToken = (userId) => {
  return jwt.sign({ id: userId }, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRE || '30d'
  });
};

