const mongoose = require('mongoose');

const interviewSchema = new mongoose.Schema({
  mockInterviewId: {
    type: String,
    required: true,
    unique: true,
    index: true // Add index for faster queries
  },
  jsonMockResp: {
    type: Array, // Store questions as array directly (not JSON string)
    required: true,
    validate: {
      validator: function(v) {
        return Array.isArray(v) && v.length > 0;
      },
      message: 'Questions array must not be empty'
    }
  },
  jobPosition: {
    type: String,
    required: [true, 'Job position is required'],
    trim: true
  },
  jobDescription: {
    type: String,
    required: [true, 'Job description is required'],
    trim: true
  },
  jobExperience: {
    type: Number,
    required: [true, 'Job experience is required'],
    min: 0,
    max: 50
  },
  createdBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
    index: true // Add index for faster user queries
  },
  status: {
    type: String,
    enum: ['pending', 'in-progress', 'completed'],
    default: 'pending'
  },
  completedAt: {
    type: Date
  }
}, {
  timestamps: true
});

// Index for efficient queries
interviewSchema.index({ createdBy: 1, createdAt: -1 });

// Virtual for getting answers
interviewSchema.virtual('answers', {
  ref: 'UserAnswer',
  localField: 'mockInterviewId',
  foreignField: 'mockInterviewId'
});

// Method to get interview with answers
interviewSchema.methods.getWithAnswers = async function() {
  await this.populate('answers');
  return this;
};

module.exports = mongoose.model('Interview', interviewSchema);

