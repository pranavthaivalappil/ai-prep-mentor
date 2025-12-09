import { GoogleGenerativeAI } from "@google/generative-ai";

// Debug API key
const apiKey = process.env.NEXT_PUBLIC_GEMINI_API_KEY;
console.log('Environment Debug:');
console.log('API Key first 10 chars:', apiKey ? apiKey.substring(0, 10) + '...' : 'NOT FOUND');
console.log('API Key length:', apiKey ? apiKey.length : 0);
console.log('Expected format: AIzaSy...');

// Initialize Gemini AI
const genAI = new GoogleGenerativeAI(apiKey);

export async function generateInterviewQuestions(jobPosition, jobDescription, jobExperience) {
  try {
    console.log('API Key exists:', !!process.env.NEXT_PUBLIC_GEMINI_API_KEY);
    console.log('Input data:', { jobPosition, jobDescription, jobExperience });
    
    // Get the generative model - Updated to use current model name
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
    console.log('Model initialized successfully');

    // Get question count from environment variable, default to 5
    const questionCount = process.env.NEXT_PUBLIC_INTERVIEW_QUESTION_COUNT || 5;

    // Create the prompt
    const prompt = `
    Generate ${questionCount} interview questions for the following job position:
    
    Job Position: ${jobPosition}
    Job Description/Tech Stack: ${jobDescription}
    Years of Experience: ${jobExperience}
    
    Please provide questions that are:
    1. Relevant to the job position and tech stack
    2. Appropriate for ${jobExperience} years of experience
    3. Mix of technical and behavioral questions
    4. Professional and realistic
    
    Format the response as a JSON array of objects with the following structure:
    [
      {
        "question": "Your interview question here",
        "type": "technical" or "behavioral"
      }
    ]
    
    Only return the JSON array, no additional text.
    `;

    console.log('Sending request to Gemini API...');
    
    // Generate content
    const result = await model.generateContent(prompt);
    console.log('API Response received');
    
    const response = await result.response;
    let text = response.text();
    
    console.log('Raw response text:', text);
    
    // Clean the response text - remove markdown code blocks if present
    text = text.trim();
    if (text.startsWith('```json')) {
      text = text.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    } else if (text.startsWith('```')) {
      text = text.replace(/^```\s*/, '').replace(/\s*```$/, '');
    }
    
    console.log('Cleaned text for parsing:', text);
    
    // Parse the JSON response
    try {
      const questions = JSON.parse(text);
      console.log('Successfully parsed questions:', questions);
      return {
        success: true,
        data: questions
      };
    } catch (parseError) {
      console.error('JSON Parse Error:', parseError);
      console.error('Raw text that failed to parse:', text);
      return {
        success: false,
        error: 'Failed to parse interview questions'
      };
    }
    
  } catch (error) {
    console.error('Gemini API Error:', error);
    console.error('Error details:', {
      message: error.message,
      status: error.status,
      statusText: error.statusText
    });
    return {
      success: false,
      error: `API Error: ${error.message}`
    };
  }
}

export async function generateFollowUpQuestion(originalQuestion, userAnswer) {
  try {
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

    const prompt = `
    Based on the following interview question and candidate's answer, generate a relevant follow-up question:
    
    Original Question: ${originalQuestion}
    Candidate's Answer: ${userAnswer}
    
    Generate a follow-up question that:
    1. Builds upon their answer
    2. Digs deeper into their knowledge
    3. Is professional and relevant
    4. Tests their understanding further
    
    Return only the follow-up question, no additional text.
    `;

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const followUpQuestion = response.text().trim();
    
    return {
      success: true,
      data: followUpQuestion
    };
    
  } catch (error) {
    console.error('Error generating follow-up question:', error);
    return {
      success: false,
      error: 'Failed to generate follow-up question'
    };
  }
}

export async function generateFeedback(question, userAnswer, jobPosition) {
  try {
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

    const prompt = `
    As an expert interviewer for ${jobPosition}, provide detailed feedback on the candidate's answer:
    
    Question: ${question}
    Candidate's Answer: ${userAnswer}
    
    Please provide:
    1. Overall assessment (Excellent/Good/Average/Needs Improvement)
    2. Strengths in their answer (max 2 points)
    3. Areas for improvement (max 2 points)
    4. Specific suggestions for better responses (keep concise)
    5. A numerical rating out of 10
    
    IMPORTANT: Keep feedback concise and under 1000 characters. Use only ASCII characters.
    
    Format your response as JSON:
    {
      "rating": "number out of 10",
      "assessment": "Overall assessment",
      "strengths": ["strength 1", "strength 2"],
      "improvements": ["improvement 1", "improvement 2"],
      "suggestions": "Specific suggestions for better responses",
      "feedback": "Detailed paragraph feedback (max 500 characters)"
    }
    
    Only return valid JSON, no additional text.
    `;

    const result = await model.generateContent(prompt);
    const response = await result.response;
    let text = response.text().trim();
    
    // Clean the response text
    if (text.startsWith('```json')) {
      text = text.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    } else if (text.startsWith('```')) {
      text = text.replace(/^```\s*/, '').replace(/\s*```$/, '');
    }
    
    try {
      const feedback = JSON.parse(text);
      
      // Sanitize and validate the feedback data
      const sanitizedFeedback = {
        rating: feedback.rating ? String(feedback.rating).substring(0, 10) : '5',
        assessment: feedback.assessment ? String(feedback.assessment).substring(0, 100) : 'Average',
        strengths: Array.isArray(feedback.strengths) 
          ? feedback.strengths.slice(0, 3).map(s => String(s).substring(0, 200))
          : ['Response provided'],
        improvements: Array.isArray(feedback.improvements) 
          ? feedback.improvements.slice(0, 3).map(i => String(i).substring(0, 200))
          : ['Could be more detailed'],
        suggestions: feedback.suggestions ? String(feedback.suggestions).substring(0, 500) : 'Practice more examples',
        feedback: feedback.feedback ? String(feedback.feedback).substring(0, 1000) : 'Feedback generated successfully'
      };
      
      return {
        success: true,
        data: sanitizedFeedback
      };
    } catch (parseError) {
      console.error('JSON Parse Error:', parseError);
      // Return default feedback if parsing fails
      return {
        success: true,
        data: {
          rating: '5',
          assessment: 'Average',
          strengths: ['Answer provided'],
          improvements: ['Could be more specific'],
          suggestions: 'Practice with more detailed examples',
          feedback: 'Your answer shows basic understanding. Consider providing more specific examples and technical details.'
        }
      };
    }
    
  } catch (error) {
    console.error('Error generating feedback:', error);
    return {
      success: false,
      error: 'Failed to generate feedback'
    };
  }
} 