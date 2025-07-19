# AI Interview Mocker

AI-powered mock interview platform with real-time feedback and performance tracking.

## Features

Generate role-specific interview questions using Google Gemini AI, receive detailed feedback on answers, and track performance over time. Built with the MERN stack featuring JWT authentication, Razorpay payment integration, and a responsive React interface.

## Tech Stack

**Backend:** Node.js, Express.js, MongoDB, Mongoose, JWT, bcrypt, Google Gemini AI, Razorpay

**Frontend:** React 19, Vite, React Router, Axios, Tailwind CSS, Radix UI

## Project Structure

```
mern-ai-interview-mocker/
├── backend/                 # Express.js API
│   ├── config/             # Database configuration
│   ├── models/             # Mongoose models
│   ├── routes/             # API routes
│   ├── controllers/        # Business logic
│   ├── middleware/         # Authentication, etc.
│   ├── services/           # External services (AI)
│   └── server.js           # Entry point
│
├── frontend/                # React SPA
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── routes/         # React Router setup
│   │   ├── services/       # API integration
│   │   ├── context/        # Global state
│   │   └── utils/          # Helper functions
│   └── index.html          # HTML entry point
│
└── Documentation files
```

## Installation

### Prerequisites

Node.js v18+, MongoDB, Google Gemini API key

### Clone and Install

```bash
git clone https://github.com/pranavthaivalappil/ai-prep-mentor.git
cd ai-prep-mentor

cd backend && npm install
cd ../frontend && npm install
```

### Configuration

Create `backend/.env`:
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai-interview-mocker
JWT_SECRET=your_secret_key_here
GEMINI_API_KEY=your_gemini_api_key
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_secret
PORT=5000
FRONTEND_URL=http://localhost:5173
```

Create `frontend/.env`:
```env
VITE_API_URL=http://localhost:5000/api
VITE_RAZORPAY_KEY_ID=your_razorpay_key_id
```

### Run

```bash
# Terminal 1
cd backend && npm run dev

# Terminal 2
cd frontend && npm run dev
```

Open http://localhost:5173

## Documentation

- [SETUP_AND_RUN.md](./SETUP_AND_RUN.md) - Complete setup guide
- [BACKEND_COMPLETE.md](./BACKEND_COMPLETE.md) - Backend documentation
- [FRONTEND_COMPLETE.md](./FRONTEND_COMPLETE.md) - Frontend documentation

## API Endpoints

### Authentication
```
POST   /api/auth/signup       - Register new user
POST   /api/auth/signin       - Login user
GET    /api/auth/me           - Get current user
PUT    /api/auth/profile      - Update profile
PUT    /api/auth/password     - Change password
```

### Interviews
```
POST   /api/interviews/create           - Create interview
GET    /api/interviews                  - Get user's interviews
GET    /api/interviews/:id              - Get specific interview
PUT    /api/interviews/:id/status       - Update status
DELETE /api/interviews/:id              - Delete interview
GET    /api/interviews/stats            - Get statistics
```

### Feedback
```
POST   /api/feedback/submit             - Submit answer
GET    /api/feedback/:interviewId       - Get feedback
GET    /api/feedback/:interviewId/answers  - Get answers
POST   /api/feedback/generate/:answerId    - Generate feedback
```

### Payment
```
POST   /api/payment/create-order        - Create Razorpay order
POST   /api/payment/verify              - Verify payment
GET    /api/payment/history             - Payment history
```

## Security

Password hashing with bcrypt, JWT token-based authentication, protected API routes, input validation and sanitization, MongoDB injection protection, CORS configuration.

## Development

```bash
# Backend
cd backend
npm run dev    # Development with auto-reload
npm start      # Production server

# Frontend
cd frontend
npm run dev      # Development server
npm run build    # Production build
npm run preview  # Preview production build
```

## License

ISC License


