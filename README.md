#  AI Prep Mentor - AI-Powered Mock Interview Platform

An intelligent, full-stack mock interview preparation platform built using the MERN stack. The application leverages Google Gemini AI to conduct interactive mock interviews, evaluate user responses in real-time, generate structured feedback, and includes a premium payment system integrated with Razorpay.

---

## Key Features

*   ** Interactive AI Mock Interviews:** Conduct mock interviews tailored to specific job descriptions, experience levels, and technology stacks.
*   ** Real-Time Evaluation & Feedback:** Automated parsing of answers using Google Gemini AI, offering key improvement suggestions and expected answers.
*   ** Razorpay Premium Integration:** Subscriptions or credit packs to unlock advanced premium features.
*   ** Secure User Auth:** Robust JWT and bcrypt-based authorization flows.
*   ** Performance Dashboard:** Detailed analytics tracking mock interview scores, historical progress, and growth over time.
*   ** Modern UI/UX:** Clean, dark-themed responsive design powered by React, TailwindCSS, and Lucide React.

---

##  Technology Stack

### Backend
*   **Node.js & Express.js** → Core application server.
*   **MongoDB & Mongoose** → Database modeling and storage.
*   **Google Gemini AI (`@google/generative-ai`)** → Intelligent interview simulation and evaluation.
*   **Razorpay SDK** → Payment gateway integration.
*   **JSON Web Tokens (JWT) & bcryptjs** → Secure authorization and password hashing.

### Frontend
*   **React (Vite)** → Modern Single Page Application (SPA) structure.
*   **TailwindCSS** → Custom utility-first styling.
*   **React Router DOM** → Front-end client routing.
*   **Axios** → Promise-based HTTP client for API requests.
*   **Lucide React & Radix UI** → Icon packs and accessibility-compliant UI components.

---

##  Project Structure

```text
mern-ai-interview-mocker/
├── backend/                  # Express Backend Application
│   ├── config/               # Database and configuration files
│   ├── controllers/          # Business logic handlers
│   ├── middleware/           # Auth and validation middleware
│   ├── models/               # MongoDB Mongoose schemas
│   ├── routes/               # API endpoint routing
│   ├── services/             # Third-party integrations (Gemini, Razorpay)
│   └── server.js             # Entrypoint server script
├── frontend/                 # Vite + React Client Application
│   ├── public/               # Static assets
│   └── src/                  # Components, pages, and React hooks
└── README.md                 # Main project documentation
```

---

##  Getting Started

### Prerequisites
*   Node.js (v18.x or later)
*   npm or yarn
*   A running MongoDB database (local or MongoDB Atlas cluster)
*   A Gemini API Key (obtain from [Google AI Studio](https://aistudio.google.com/))
*   A Razorpay developer account (optional, for payments)

---

### Installation & Local Setup

#### 1. Clone the repository
```bash
git clone https://github.com/pranavthaivalappil/ai-prep-mentor.git
cd mern-ai-interview-mocker
```

#### 2. Configure Backend Environment
Navigate to the `backend` folder, create a `.env` file, and populate it:
```bash
cd backend
# Create .env and paste the configuration below
```

##### `backend/.env` template:
```env
PORT=5000
NODE_ENV=development
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/ai-interview-mocker?retryWrites=true&w=majority
JWT_SECRET=your_jwt_secret_token_here
GEMINI_API_KEY=your_gemini_api_key_here
FRONTEND_URL=http://localhost:5173

# Razorpay Keys (optional for payment workflow)
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
```

Install backend dependencies and run in development mode:
```bash
npm install
npm run dev
```

---

#### 3. Configure Frontend Environment
Navigate to the `frontend` folder, create a `.env` file, and configure the backend URL:
```bash
cd ../frontend
# Create .env and paste the configuration below
```

##### `frontend/.env` template:
```env
VITE_API_BASE_URL=http://localhost:5000/api
```

Install frontend dependencies and start Vite dev server:
```bash
npm install
npm run dev
```

---

## 🌐 Deploying with Vercel

To configure and pull environment variables from Vercel CLI locally:
```bash
# Link the project if not already linked
npx vercel link

# Pull environment variables
npx vercel env pull .env --environment=production
```

---

## 📄 License
This project is licensed under the ISC License.
