const mongoose = require('mongoose');

const userAnswerSchema = new mongoose.Schema({
  mockInterviewId: {
    type: String,
    required: true,
    index: true // Add index for faster queries
  },
  question: {
    type: String,
    required: true
  },
  correctAns: {
    type: String
  },
  userAns: {
    type: String,
    required: true
  },
  feedback: {
    type: String,
    maxlength: 5000 // Limit feedback length
  },
  rating: {
    type: String,
    validate: {
      validator: function(v) {
        if (!v) return true;
        const num = parseInt(v);
        return num >= 0 && num <= 10;
      },
      message: 'Rating must be between 0 and 10'
    }
  },
  // Additional feedback fields
  assessment: {
    type: String,
    enum: ['Excellent', 'Good', 'Average', 'Needs Improvement', '']
  },
  strengths: [{
    type: String,
    maxlength: 500
  }],
  improvements: [{
    type: String,
    maxlength: 500
  }],
  suggestions: {
    type: String,
    maxlength: 1000
  },
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  }
}, {
  timestamps: true
});

// Compound index for efficient queries
userAnswerSchema.index({ mockInterviewId: 1, userId: 1 });
userAnswerSchema.index({ userId: 1, createdAt: -1 });

// Method to sanitize feedback before saving
userAnswerSchema.pre('save', function(next) {
  // Remove non-ASCII characters from feedback
  if (this.feedback) {
    this.feedback = this.feedback.replace(/[^\x00-\x7F]/g, "");
  }
  if (this.suggestions) {
    this.suggestions = this.suggestions.replace(/[^\x00-\x7F]/g, "");
  }
  next();
});

module.exports = mongoose.model('UserAnswer', userAnswerSchema);

