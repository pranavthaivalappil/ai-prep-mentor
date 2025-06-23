'use client'
import React, { useEffect, useState } from 'react'
import { db } from '../../../../../utils/db'
import { UserAnswer, MockInterview } from '../../../../../utils/schema'
import { eq } from 'drizzle-orm'
import { useRouter } from 'next/navigation'
import { Button } from '../../../../../components/ui/button'
import { 
    Trophy, 
    TrendingUp, 
    CheckCircle, 
    AlertTriangle, 
    ArrowLeft, 
    Star,
    Target,
    Brain,
    BookOpen,
    Home
} from 'lucide-react'
import { generateFeedback } from '../../../../../utils/gemini'

function FeedbackPage({ params }) {
    const resolvedParams = React.use(params)
    const [feedbackList, setFeedbackList] = useState([])
    const [interviewDetails, setInterviewDetails] = useState(null)
    const [loading, setLoading] = useState(true)
    const [overallRating, setOverallRating] = useState(0)
    const router = useRouter()

    useEffect(() => {
        GetFeedback()
    }, [])

    const GetFeedback = async () => {
        try {
            setLoading(true)
            
            // Get interview details
            const interviewResp = await db.select()
                .from(MockInterview)
                .where(eq(MockInterview.mockInterviewId, resolvedParams.interviewId))
            
            setInterviewDetails(interviewResp[0])
            
            // Get user answers
            const result = await db.select()
                .from(UserAnswer)
                .where(eq(UserAnswer.mockInterviewIdRef, resolvedParams.interviewId))
                .orderBy(UserAnswer.id)

            console.log('User answers fetched:', result)
            
            // Generate feedback for each answer if not already generated
            const feedbackPromises = result.map(async (answer) => {
                if (!answer.feedback && answer.userAns?.length > 10) {
                    try {
                        const feedbackResp = await generateFeedback(
                            answer.question,
                            answer.userAns,
                            interviewResp[0]?.jobPosition
                        )
                        
                        if (feedbackResp.success) {
                            const feedbackData = feedbackResp.data
                            
                            // Sanitize and truncate feedback if necessary
                            const sanitizedFeedback = feedbackData.feedback
                                ? feedbackData.feedback.substring(0, 5000).replace(/[^\x00-\x7F]/g, "") // Remove non-ASCII characters and limit length
                                : 'Feedback generation failed'
                            
                            const sanitizedRating = feedbackData.rating
                                ? feedbackData.rating.toString().substring(0, 10)
                                : '0'
                            
                            try {
                                // Update the answer with feedback
                                await db.update(UserAnswer)
                                    .set({
                                        feedback: sanitizedFeedback,
                                        rating: sanitizedRating
                                    })
                                    .where(eq(UserAnswer.id, answer.id))
                                
                                return {
                                    ...answer,
                                    feedback: sanitizedFeedback,
                                    rating: sanitizedRating,
                                    assessment: feedbackData.assessment,
                                    strengths: feedbackData.strengths,
                                    improvements: feedbackData.improvements,
                                    suggestions: feedbackData.suggestions
                                }
                            } catch (dbError) {
                                console.error('Database update error:', dbError)
                                // Return the answer with generated feedback even if DB update fails
                                return {
                                    ...answer,
                                    feedback: sanitizedFeedback,
                                    rating: sanitizedRating,
                                    assessment: feedbackData.assessment,
                                    strengths: feedbackData.strengths,
                                    improvements: feedbackData.improvements,
                                    suggestions: feedbackData.suggestions
                                }
                            }
                        }
                    } catch (error) {
                        console.error('Error generating feedback:', error)
                        // Return answer with basic feedback on error
                        return {
                            ...answer,
                            feedback: 'Unable to generate detailed feedback at this time.',
                            rating: 'N/A',
                            assessment: 'Error in analysis'
                        }
                    }
                }
                return answer
            })
            
            const feedbackResults = await Promise.all(feedbackPromises)
            setFeedbackList(feedbackResults)
            
            // Calculate overall rating
            const validRatings = feedbackResults
                .filter(item => item.rating)
                .map(item => parseInt(item.rating))
            
            if (validRatings.length > 0) {
                const avgRating = validRatings.reduce((sum, rating) => sum + rating, 0) / validRatings.length
                setOverallRating(Math.round(avgRating * 10) / 10)
            }
            
        } catch (error) {
            console.error('Error fetching feedback:', error)
        } finally {
            setLoading(false)
        }
    }

    const getRatingColor = (rating) => {
        const numRating = parseInt(rating)
        if (numRating >= 8) return 'text-green-600 bg-green-100'
        if (numRating >= 6) return 'text-blue-600 bg-blue-100'
        if (numRating >= 4) return 'text-yellow-600 bg-yellow-100'
        return 'text-red-600 bg-red-100'
    }

    const getOverallAssessment = (rating) => {
        if (rating >= 8) return { text: 'Excellent Performance!', icon: Trophy, color: 'text-green-600' }
        if (rating >= 6) return { text: 'Good Performance', icon: TrendingUp, color: 'text-blue-600' }
        if (rating >= 4) return { text: 'Average Performance', icon: Target, color: 'text-yellow-600' }
        return { text: 'Needs Improvement', icon: AlertTriangle, color: 'text-red-600' }
    }

    if (loading) {
        return (
            <div className='min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-4 flex items-center justify-center'>
                <div className='text-center'>
                    <div className='animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4'></div>
                    <p className='text-gray-600'>Generating your feedback...</p>
                </div>
            </div>
        )
    }

    const assessment = getOverallAssessment(overallRating)
    const AssessmentIcon = assessment.icon

    return (
        <div className='min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-4'>
            <div className='max-w-4xl mx-auto'>
                
                {/* Header */}
                <div className='text-center mb-8'>
                    <h1 className='text-4xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-4'>
                        Interview Feedback
                    </h1>
                    <p className='text-gray-600 text-lg'>
                        {interviewDetails?.jobPosition} • {interviewDetails?.jobLocation}
                    </p>
                </div>

                {/* Overall Rating Card */}
                <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-6 mb-6'>
                    <div className='text-center'>
                        <div className='flex justify-center items-center mb-4'>
                            <AssessmentIcon className={`w-12 h-12 ${assessment.color} mr-3`} />
                            <div>
                                <h2 className={`text-2xl font-bold ${assessment.color}`}>
                                    {assessment.text}
                                </h2>
                                <div className='flex items-center justify-center mt-2'>
                                    <Star className='w-6 h-6 text-yellow-500 mr-2' />
                                    <span className='text-3xl font-bold text-gray-800'>
                                        {overallRating}/10
                                    </span>
                                </div>
                            </div>
                        </div>
                        <p className='text-gray-600'>
                            Based on {feedbackList.length} answered questions
                        </p>
                    </div>
                </div>

                {/* Individual Question Feedback */}
                <div className='space-y-6 mb-8'>
                    {feedbackList.map((feedback, index) => (
                        <div key={index} className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 overflow-hidden'>
                            
                            {/* Question Header */}
                            <div className='bg-gradient-to-r from-gray-50 to-gray-100 px-6 py-4 border-b border-gray-200'>
                                <div className='flex items-center justify-between'>
                                    <h3 className='text-lg font-semibold text-gray-800'>
                                        Question {index + 1}
                                    </h3>
                                    {feedback.rating && (
                                        <div className={`px-3 py-1 rounded-full text-sm font-semibold ${getRatingColor(feedback.rating)}`}>
                                            {feedback.rating}/10
                                        </div>
                                    )}
                                </div>
                                <p className='text-gray-700 mt-2 leading-relaxed'>
                                    {feedback.question}
                                </p>
                            </div>

                            <div className='p-6 space-y-4'>
                                
                                {/* User Answer */}
                                <div>
                                    <div className='flex items-center mb-2'>
                                        <Brain className='w-4 h-4 text-blue-600 mr-2' />
                                        <h4 className='text-sm font-semibold text-gray-800'>Your Answer:</h4>
                                    </div>
                                    <div className='bg-blue-50 rounded-lg p-4 border border-blue-200'>
                                        <p className='text-gray-900 leading-relaxed'>
                                            {feedback.userAns || 'No answer provided'}
                                        </p>
                                    </div>
                                </div>

                                {/* AI Feedback */}
                                {feedback.feedback && (
                                    <div>
                                        <div className='flex items-center mb-2'>
                                            <BookOpen className='w-4 h-4 text-green-600 mr-2' />
                                            <h4 className='text-sm font-semibold text-gray-800'>AI Feedback:</h4>
                                        </div>
                                        <div className='bg-green-50 rounded-lg p-4 border border-green-200'>
                                            <p className='text-gray-900 leading-relaxed'>
                                                {feedback.feedback}
                                            </p>
                                        </div>
                                    </div>
                                )}

                                {/* Strengths and Improvements */}
                                {(feedback.strengths || feedback.improvements) && (
                                    <div className='grid md:grid-cols-2 gap-4 mt-4'>
                                        {feedback.strengths && (
                                            <div>
                                                <div className='flex items-center mb-2'>
                                                    <CheckCircle className='w-4 h-4 text-green-600 mr-2' />
                                                    <h5 className='text-sm font-semibold text-gray-800'>Strengths:</h5>
                                                </div>
                                                <ul className='space-y-1'>
                                                    {feedback.strengths.map((strength, idx) => (
                                                        <li key={idx} className='text-sm text-gray-700 flex items-start'>
                                                            <span className='w-1.5 h-1.5 bg-green-500 rounded-full mt-2 mr-2 flex-shrink-0'></span>
                                                            {strength}
                                                        </li>
                                                    ))}
                                                </ul>
                                            </div>
                                        )}
                                        
                                        {feedback.improvements && (
                                            <div>
                                                <div className='flex items-center mb-2'>
                                                    <TrendingUp className='w-4 h-4 text-blue-600 mr-2' />
                                                    <h5 className='text-sm font-semibold text-gray-800'>Areas for Improvement:</h5>
                                                </div>
                                                <ul className='space-y-1'>
                                                    {feedback.improvements.map((improvement, idx) => (
                                                        <li key={idx} className='text-sm text-gray-700 flex items-start'>
                                                            <span className='w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 mr-2 flex-shrink-0'></span>
                                                            {improvement}
                                                        </li>
                                                    ))}
                                                </ul>
                                            </div>
                                        )}
                                    </div>
                                )}

                                {/* Suggestions */}
                                {feedback.suggestions && (
                                    <div className='mt-4 p-4 bg-purple-50 rounded-lg border border-purple-200'>
                                        <h5 className='text-sm font-semibold text-purple-800 mb-2'>💡 Suggestions for Improvement:</h5>
                                        <p className='text-sm text-purple-700 leading-relaxed'>
                                            {feedback.suggestions}
                                        </p>
                                    </div>
                                )}
                            </div>
                        </div>
                    ))}
                </div>

                {/* Action Buttons */}
                <div className='flex flex-col sm:flex-row gap-4 justify-center'>
                    <Button
                        onClick={() => router.push('/dashboard')}
                        className='flex items-center justify-center space-x-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-6 py-3'
                    >
                        <Home className='w-5 h-5' />
                        <span>Back to Dashboard</span>
                    </Button>
                    
                    <Button
                        onClick={() => router.push(`/dashboard/interview/${resolvedParams.interviewId}`)}
                        variant="outline"
                        className='flex items-center justify-center space-x-2 px-6 py-3'
                    >
                        <ArrowLeft className='w-5 h-5' />
                        <span>Retake Interview</span>
                    </Button>
                </div>
            </div>
        </div>
    )
}

export default FeedbackPage 