# AI Interview Mocker - Backend

Express.js + MongoDB + Node.js backend for AI Interview Mocker application.

## 🚀 Features

- ✅ RESTful API with Express.js
- ✅ MongoDB database with Mongoose ODM
- ✅ JWT-based authentication
- ✅ Google Gemini AI integration
- ✅ Razorpay payment integration
- ✅ Interview management
- ✅ AI-powered feedback generation

## 📦 Installation

```bash
# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Update .env with your credentials
```

## 🔧 Environment Variables

Create a `.env` file in the backend directory:

```env
# MongoDB
MONGODB_URI=mongodb://localhost:27017/ai-interview-mocker

# JWT
JWT_SECRET=your_secret_key_here
JWT_EXPIRE=30d

# Gemini AI
GEMINI_API_KEY=your_gemini_api_key
INTERVIEW_QUESTION_COUNT=5

# Razorpay
RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_secret

# Server
PORT=5000
NODE_ENV=development
FRONTEND_URL=http://localhost:5173
```

## 🏃 Running the Server

```bash
# Development mode (with nodemon)
npm run dev

# Production mode
npm start
```

## 📝 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/signin` - Login user
- `GET /api/auth/me` - Get current user (Protected)
- `PUT /api/auth/profile` - Update profile (Protected)
- `PUT /api/auth/password` - Update password (Protected)

### Interviews
- `POST /api/interviews/create` - Create new interview (Protected)
- `GET /api/interviews` - Get user's interviews (Protected)
- `GET /api/interviews/:interviewId` - Get specific interview (Protected)
- `PUT /api/interviews/:interviewId/status` - Update interview status (Protected)
- `DELETE /api/interviews/:interviewId` - Delete interview (Protected)
- `GET /api/interviews/stats` - Get statistics (Protected)

### Feedback
- `POST /api/feedback/submit` - Submit answer (Protected)
- `GET /api/feedback/:interviewId` - Get feedback for interview (Protected)
- `GET /api/feedback/:interviewId/answers` - Get all answers (Protected)
- `POST /api/feedback/generate/:answerId` - Generate feedback for answer (Protected)

### Payment
- `POST /api/payment/create-order` - Create payment order (Protected)
- `POST /api/payment/verify` - Verify payment (Protected)
- `GET /api/payment/history` - Get payment history (Protected)

## 🏗️ Project Structure

```
backend/
├── config/
│   └── db.js                 # Database connection
├── models/
│   ├── User.js              # User model
│   ├── Interview.js         # Interview model
│   └── UserAnswer.js        # User answer model
├── routes/
│   ├── auth.routes.js       # Auth routes
│   ├── interview.routes.js  # Interview routes
│   ├── feedback.routes.js   # Feedback routes
│   └── payment.routes.js    # Payment routes
├── controllers/
│   ├── authController.js    # Auth logic
│   ├── interviewController.js
│   ├── feedbackController.js
│   └── paymentController.js
├── middleware/
│   └── auth.middleware.js   # JWT authentication
├── services/
│   └── gemini.service.js    # AI integration
├── server.js                # Entry point
├── .env                     # Environment variables
└── package.json
```

## 🔒 Security Features

- Password hashing with bcrypt
- JWT token-based authentication
- Protected routes with middleware
- Request validation
- MongoDB injection protection
- CORS configuration

## 📊 Database Models

### User
- name, email, password
- subscriptionType (free/pro)
- interviewCount
- timestamps

### Interview
- mockInterviewId (UUID)
- jsonMockResp (array of questions)
- jobPosition, jobDescription, jobExperience
- createdBy (user reference)
- status (pending/in-progress/completed)
- timestamps

### UserAnswer
- mockInterviewId, question, userAns
- feedback, rating, assessment
- strengths, improvements, suggestions
- userId (user reference)
- timestamps

## 🧪 Testing

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test API root
curl http://localhost:5000/api
```

## 🚀 Deployment

### Railway
```bash
railway login
railway init
railway up
```

### Render
1. Connect GitHub repository
2. Add environment variables
3. Deploy

## 📝 Notes

- Free users: Limited to 3 interviews per month
- Pro users: Unlimited interviews
- AI feedback generated using Google Gemini AI
- Payment processing via Razorpay

---

**Made with ❤️ by Pranav**

