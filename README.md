# 🎓 AI Mock Interview - MERN Stack

> **Complete MERN Stack Application for AI-Powered Interview Preparation**  
> *Migrated from Next.js to MERN Stack*

**Made with ❤️ by Pranav**

---

## 📖 Project Overview

A full-stack web application that helps job seekers practice interviews with AI-powered feedback. Built with **MongoDB, Express.js, React, and Node.js (MERN)**.

### ✨ Features

- 🤖 **AI-Powered Question Generation** using Google Gemini AI
- 📊 **Detailed Performance Feedback** with ratings and suggestions
- 🔐 **Secure Authentication** with JWT tokens
- 💳 **Payment Integration** with Razorpay
- 📱 **Responsive Design** works on all devices
- 🎯 **Role-Specific Questions** based on job description
- 📈 **Performance Tracking** and analytics

---

## 🏗️ Tech Stack

### Backend
- **Node.js** - JavaScript runtime
- **Express.js** - Web framework
- **MongoDB** - NoSQL database
- **Mongoose** - ODM for MongoDB
- **JWT** - Authentication
- **Bcrypt** - Password hashing
- **Google Gemini AI** - Question & feedback generation
- **Razorpay** - Payment processing

### Frontend
- **React 19** - UI library
- **Vite** - Build tool
- **React Router** - Navigation
- **Axios** - HTTP client
- **Tailwind CSS** - Styling
- **Lucide React** - Icons
- **Radix UI** - Accessible components

---

## 📁 Project Structure

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

---

## 🚀 Quick Start

### Prerequisites
- Node.js (v18+)
- MongoDB (Atlas account or local)
- Gemini API key
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/pranavthaivalappil/ai-prep-mentor.git
cd ai-prep-mentor

# Install backend dependencies
cd backend
npm install

# Install frontend dependencies
cd ../frontend
npm install
```

### Configuration

**1. Backend Environment (`backend/.env`):**
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai-interview-mocker
JWT_SECRET=your_secret_key_here
GEMINI_API_KEY=your_gemini_api_key
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_secret
PORT=5000
NODE_ENV=development
FRONTEND_URL=http://localhost:5173
```

**2. Frontend Environment (`frontend/.env`):**
```env
VITE_API_URL=http://localhost:5000/api
VITE_RAZORPAY_KEY_ID=your_razorpay_key_id
```

### Running the Application

**Terminal 1 - Backend:**
```bash
cd backend
npm run dev
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Open Browser:** http://localhost:5173

---

## 📚 Documentation

- **[SETUP_AND_RUN.md](./SETUP_AND_RUN.md)** - Complete setup guide
- **[BACKEND_COMPLETE.md](./BACKEND_COMPLETE.md)** - Backend documentation
- **[FRONTEND_COMPLETE.md](./FRONTEND_COMPLETE.md)** - Frontend documentation
- **[MERN_MIGRATION_GUIDE.md](./MERN_MIGRATION_GUIDE.md)** - From Next.js to MERN
- **[CODE_COMPARISON.md](./CODE_COMPARISON.md)** - Code examples

---

## 🎯 API Endpoints

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

---

## 💻 Usage Flow

1. **Sign Up** - Create an account
2. **Create Interview** - Enter job details (position, description, experience)
3. **View Questions** - AI generates relevant questions
4. **Take Interview** - Answer each question
5. **Get Feedback** - AI analyzes responses and provides feedback
6. **Track Progress** - View performance over time

---

## 🔐 Security Features

- Password hashing with bcrypt (10 salt rounds)
- JWT token-based authentication
- Protected API routes
- Input validation and sanitization
- MongoDB injection protection
- CORS configuration
- Environment variable management

---

## 🧪 Testing

### Backend Testing
```bash
cd backend

# Test health endpoint
curl http://localhost:5000/health

# Test signup
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","password":"test123"}'
```

### Frontend Testing
1. Open http://localhost:5173
2. Sign up with test credentials
3. Create a new interview
4. Complete the interview flow
5. Check feedback generation

---

## 🚀 Deployment

### Backend (Railway/Render)
1. Push code to GitHub
2. Connect repository to Railway/Render
3. Add environment variables
4. Deploy

### Frontend (Vercel/Netlify)
1. Push code to GitHub
2. Connect repository to Vercel/Netlify
3. Set build command: `npm run build`
4. Set output directory: `dist`
5. Add environment variables
6. Deploy

---

## 📊 Database Schema

### User Model
```javascript
{
  name: String,
  email: String (unique),
  password: String (hashed),
  subscriptionType: 'free' | 'pro',
  interviewCount: Number,
  createdAt: Date
}
```

### Interview Model
```javascript
{
  mockInterviewId: String (UUID),
  jsonMockResp: Array,
  jobPosition: String,
  jobDescription: String,
  jobExperience: Number,
  createdBy: ObjectId (User),
  status: 'pending' | 'in-progress' | 'completed',
  createdAt: Date
}
```

### UserAnswer Model
```javascript
{
  mockInterviewId: String,
  question: String,
  userAns: String,
  feedback: String,
  rating: String,
  assessment: String,
  strengths: [String],
  improvements: [String],
  suggestions: String,
  userId: ObjectId (User),
  createdAt: Date
}
```

---

## 🎨 UI Components

- **Button** - Reusable button with variants
- **Input** - Text input field
- **Textarea** - Multiline text input
- **Dialog** - Modal dialog
- **Protected Routes** - Authentication guards
- **Loading States** - Spinners and skeletons

---

## 🛠️ Development

### Backend Development
```bash
cd backend
npm run dev    # Start with nodemon (auto-reload)
npm start      # Start production server
```

### Frontend Development
```bash
cd frontend
npm run dev      # Start dev server
npm run build    # Build for production
npm run preview  # Preview production build
```

---

## 📦 Dependencies

### Backend Dependencies
- express - Web framework
- mongoose - MongoDB ODM
- jsonwebtoken - JWT authentication
- bcryptjs - Password hashing
- @google/generative-ai - Gemini AI
- razorpay - Payment gateway
- cors - CORS middleware
- dotenv - Environment variables

### Frontend Dependencies
- react - UI library
- react-router-dom - Routing
- axios - HTTP client
- tailwindcss - Styling
- lucide-react - Icons
- @radix-ui - UI primitives

---

## 🐛 Known Issues

None currently! 🎉

If you find any issues:
1. Check environment variables
2. Verify MongoDB connection
3. Check API keys are valid
4. Review console logs

---

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

ISC License - Feel free to use for learning purposes

---

## 👨‍💻 Author

**Pranav**
- Portfolio: [Your Portfolio URL]
- LinkedIn: [Your LinkedIn]
- GitHub: [@pranavthaivalappil](https://github.com/pranavthaivalappil)
- Email: [Your Email]

---

## 🙏 Acknowledgments

- Google Gemini AI for question generation
- Razorpay for payment processing
- MongoDB Atlas for database hosting
- Vercel/Netlify for frontend hosting
- Railway/Render for backend hosting

---

## 📈 Project Stats

- **Total Lines of Code:** 5000+
- **Files Created:** 50+
- **API Endpoints:** 20+
- **UI Components:** 15+
- **Development Time:** 1-2 weeks
- **Tech Stack:** MERN

---

## 🎓 Learning Outcomes

From this project, you learned:
- ✅ Full-stack MERN development
- ✅ JWT authentication
- ✅ MongoDB database design
- ✅ RESTful API development
- ✅ React SPA with routing
- ✅ State management
- ✅ AI API integration
- ✅ Payment gateway integration
- ✅ Deployment strategies

---

## 🔮 Future Enhancements

- [ ] Video interview recording
- [ ] Speech-to-text for answers
- [ ] Interview analytics dashboard
- [ ] Email notifications
- [ ] Interview sharing
- [ ] Mobile app (React Native)
- [ ] AI voice interviewer
- [ ] Resume analysis
- [ ] Job matching

---

## 📞 Support

For issues or questions:
- Create an issue on GitHub
- Email: [your-email]
- Check documentation files

---

## ⭐ Show Your Support

If you found this project helpful:
- ⭐ Star the repository
- 🍴 Fork the project
- 📢 Share with friends
- 💬 Provide feedback

---

## 📝 Changelog

### Version 2.0.0 (December 2025) - MERN Migration
- ✅ Migrated from Next.js to MERN Stack
- ✅ Separate backend and frontend architecture
- ✅ MongoDB database integration
- ✅ Express.js REST API
- ✅ React + Vite frontend
- ✅ Enhanced documentation

### Version 1.0.0 (Previous)
- ✅ Next.js implementation
- ✅ Basic interview functionality

---

**🎉 Thank you for using AI Mock Interview!**

**Made with ❤️ and lots of ☕**
