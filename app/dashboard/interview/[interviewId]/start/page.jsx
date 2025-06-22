'use client'
import React, { useEffect, useState } from 'react'
import { db } from '../../../../../utils/db'
import { MockInterview } from '../../../../../utils/schema'
import { eq } from 'drizzle-orm'
import Webcam from 'react-webcam'
import { WebcamIcon, Lightbulb, Volume2, Mic, MicOff, SkipForward, CheckCircle, AlertCircle } from 'lucide-react'
import { Button } from '../../../../../components/ui/button'
import { useRouter } from 'next/navigation'
import useSpeechToText from 'react-hook-speech-to-text'

function StartInterview({params}) {
    const resolvedParams = React.use(params)
    const [interviewDetails, setInterviewDetails] = useState(null)
    const [mockInterviewQuestions, setMockInterviewQuestions] = useState([])
    const [activeQuestionIndex, setActiveQuestionIndex] = useState(0)
    const [userAnswer, setUserAnswer] = useState('')
    const [showAnswer, setShowAnswer] = useState(false)
    const [isMounted, setIsMounted] = useState(false)
    const router = useRouter()

    // Speech to text hook with configuration
    const {
        error,
        interimResult,
        isRecording,
        results,
        startSpeechToText,
        stopSpeechToText,
        setResults,
    } = useSpeechToText({
        continuous: true,
        useLegacyResults: false
    })

    useEffect(()=>{
        setIsMounted(true)
        GetInterviewDetails()
    },[resolvedParams.interviewId])

    // Update user answer when speech recognition results change
    useEffect(() => {
        if (results.length > 0) {
            const speechText = results.map(result => result.transcript).join(' ')
            setUserAnswer(speechText)
        }
    }, [results])

    const GetInterviewDetails = async()=>{
        const resp = await db.select().from(MockInterview).where(eq(MockInterview.mockInterviewId, resolvedParams.interviewId))
        
        const jsonMockResp = JSON.parse(resp[0].jsonMockResp)
        setMockInterviewQuestions(jsonMockResp)
        setInterviewDetails(resp[0])
    }

    const StartStopRecording = async () => {
        if (isRecording) {
            console.log('🛑 Stopping speech recognition...')
            stopSpeechToText()
        } else {
            console.log('🚀 Starting speech recognition...')
            // Clear previous results when starting new recording
            setResults([])
            setUserAnswer('')
            startSpeechToText()
        }
    }

    const textToSpeech = (text) => {
        if (isMounted && typeof window !== 'undefined' && 'speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel()
                const utterance = new SpeechSynthesisUtterance(text)
                utterance.rate = 0.9
                utterance.pitch = 1
                utterance.volume = 1
                window.speechSynthesis.speak(utterance)
            } catch (error) {
                console.log('Speech synthesis error:', error)
            }
        }
    }

    const EndInterview = () => {
        if (isRecording) {
            stopSpeechToText()
        }
        
        const confirmEnd = window.confirm("Are you sure you want to end the interview? This will take you to the feedback page.")
        
        if (confirmEnd) {
            router.push('/dashboard/interview/' + resolvedParams.interviewId + '/feedback')
        }
    }

    // Don't render anything until mounted to prevent hydration issues
    if (!isMounted) {
        return (
            <div className='min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-4 flex items-center justify-center'>
                <div className='text-center'>
                    <div className='animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4'></div>
                    <p className='text-gray-600'>Loading Interview...</p>
                </div>
            </div>
        )
    }

    return (
        <div className='min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-4'>
            <div className='max-w-7xl mx-auto'>
                
                {/* Header */}
                <div className='text-center mb-6'>
                    <h1 className='text-3xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-2'>
                        AI Mock Interview
                    </h1>
                    <p className='text-gray-600'>
                        Question {activeQuestionIndex + 1} of {mockInterviewQuestions?.length}
                    </p>
                    <p className='text-green-600 text-sm mt-2'>
                        🎤 Speech Recognition Mode - Speak naturally to answer
                    </p>
                </div>

                {/* Error Alert */}
                {error && (
                    <div className='mb-6 max-w-4xl mx-auto'>
                        <div className='bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3'>
                            <AlertCircle className='w-5 h-5 text-red-600 mt-0.5 flex-shrink-0' />
                            <div className='flex-1'>
                                <p className='text-sm text-red-800'>Speech Recognition Error: {error}</p>
                                <p className='text-xs text-red-600 mt-1'>
                                    Make sure you're using Chrome and have allowed microphone access.
                                </p>
                            </div>
                        </div>
                    </div>
                )}

                {/* Main Content Grid */}
                <div className='grid lg:grid-cols-2 gap-6'>
                    
                    {/* Left Column - Questions */}
                    <div className='space-y-4'>
                        
                        {/* Current Question Card */}
                        <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-6'>
                            <div className='flex items-center mb-4'>
                                <Lightbulb className='w-5 h-5 text-yellow-600 mr-2' />
                                <h2 className='text-xl font-semibold text-gray-800'>Interview Question</h2>
                            </div>
                            
                            <div className='bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-4 mb-4'>
                                <p className='text-gray-900 text-lg leading-relaxed'>
                                    {mockInterviewQuestions[activeQuestionIndex]?.question}
                                </p>
                            </div>

                            <div className='flex items-center space-x-2 text-sm text-gray-600 mb-4'>
                                <Button
                                    onClick={() => textToSpeech(mockInterviewQuestions[activeQuestionIndex]?.question)}
                                    variant="outline"
                                    size="sm"
                                    className='flex items-center space-x-2'
                                >
                                    <Volume2 className='w-4 h-4' />
                                    <span>Listen to Question</span>
                                </Button>
                            </div>

                            {/* Question Navigation */}
                            <div className='flex gap-3'>
                                <Button
                                    disabled={activeQuestionIndex === 0}
                                    onClick={() => setActiveQuestionIndex(activeQuestionIndex - 1)}
                                    variant="outline"
                                    className='flex-1'
                                >
                                    Previous
                                </Button>
                                
                                <Button
                                    disabled={activeQuestionIndex === mockInterviewQuestions?.length - 1}
                                    onClick={() => setActiveQuestionIndex(activeQuestionIndex + 1)}
                                    className='flex-1'
                                >
                                    <SkipForward className='w-4 h-4 mr-2' />
                                    Next Question
                                </Button>
                            </div>
                        </div>

                        {/* Note Section */}
                        <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-4'>
                            <div className='flex items-center mb-3'>
                                <Lightbulb className='w-4 h-4 text-green-600 mr-2' />
                                <h3 className='text-base font-semibold text-gray-800'>Speech Recognition</h3>
                            </div>
                            <p className='text-sm text-gray-600'>
                                Click "Start Recording" and speak your answer naturally. The speech recognition will capture your response in real-time.
                            </p>
                        </div>
                    </div>

                    {/* Right Column - Webcam and Recording */}
                    <div className='space-y-4'>
                        
                        {/* Webcam Card */}
                        <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 overflow-hidden'>
                            
                            {/* Webcam Header */}
                            <div className='bg-gradient-to-r from-gray-50 to-gray-100 px-4 py-3 border-b border-gray-200'>
                                <div className='flex items-center justify-between'>
                                    <div className='flex items-center space-x-2'>
                                        <WebcamIcon className='w-4 h-4 text-gray-700' />
                                        <h2 className='text-lg font-semibold text-gray-800'>Your Video</h2>
                                    </div>
                                    <div className='flex items-center space-x-2'>
                                        <div className={`w-2 h-2 rounded-full shadow-lg ${isRecording ? 'bg-red-400' : 'bg-green-400'}`}></div>
                                        <span className='text-xs font-medium text-gray-600'>
                                            {isRecording ? 'Recording' : 'Ready'}
                                        </span>
                                    </div>
                                </div>
                            </div>

                            {/* Webcam Content */}
                            <div className='p-4'>
                                <div className='relative rounded-lg overflow-hidden bg-gray-900' style={{aspectRatio: '16/9', height: '280px'}}>
                                    <Webcam
                                        mirrored={true}
                                        className='w-full h-full object-cover'
                                        key="webcam-component"
                                    />
                                    
                                    {/* Recording indicator */}
                                    {isRecording && (
                                        <div className='absolute top-3 left-3'>
                                            <div className='bg-red-600 backdrop-blur-sm rounded-lg px-3 py-1 flex items-center space-x-2'>
                                                <div className='w-2 h-2 bg-white rounded-full animate-pulse'></div>
                                                <span className='text-white text-xs font-medium'>Recording</span>
                                            </div>
                                        </div>
                                    )}
                                </div>

                                {/* Recording Controls */}
                                <div className='mt-4 space-y-3'>
                                    <Button
                                        onClick={StartStopRecording}
                                        variant={isRecording ? "destructive" : "default"}
                                        className='w-full h-12 text-lg font-semibold'
                                        disabled={error}
                                    >
                                        {isRecording ? (
                                            <>
                                                <MicOff className='w-5 h-5 mr-2' />
                                                Stop Recording
                                            </>
                                        ) : (
                                            <>
                                                <Mic className='w-5 h-5 mr-2' />
                                                Start Recording
                                            </>
                                        )}
                                    </Button>

                                    {/* Show User Answer Button */}
                                    {userAnswer && !isRecording && (
                                        <Button
                                            onClick={() => setShowAnswer(!showAnswer)}
                                            variant="outline"
                                            className='w-full h-10 text-sm font-medium'
                                        >
                                            {showAnswer ? 'Hide Your Answer' : 'Show Your Answer'}
                                        </Button>
                                    )}
                                </div>

                                {/* Live Speech Recognition Display */}
                                {isRecording && (
                                    <div className='mt-4 p-4 bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg border border-green-200'>
                                        <div className='flex items-center mb-3'>
                                            <div className='w-2 h-2 bg-red-500 rounded-full animate-pulse mr-2'></div>
                                            <h4 className='text-sm font-semibold text-green-800'>Listening...</h4>
                                            <span className='ml-auto text-xs text-green-600'>Speak now</span>
                                        </div>
                                        
                                        <div className='space-y-3'>
                                            {/* Interim Results */}
                                            {interimResult && (
                                                <div className='p-3 bg-yellow-50 rounded border border-yellow-200'>
                                                    <p className='text-sm text-yellow-800 italic'>"{interimResult}"</p>
                                                    <span className='text-xs text-yellow-600'>Processing...</span>
                                                </div>
                                            )}
                                            
                                            {/* Final Results */}
                                            {userAnswer && (
                                                <div className='p-3 bg-white rounded border border-green-300'>
                                                    <p className='text-sm text-gray-900 leading-relaxed'>{userAnswer}</p>
                                                    <span className='text-xs text-green-600'>Captured</span>
                                                </div>
                                            )}
                                            
                                            {/* No speech detected */}
                                            {isRecording && !interimResult && !userAnswer && (
                                                <div className='p-3 bg-blue-50 rounded border border-blue-200'>
                                                    <p className='text-sm text-blue-800'>🎤 Start speaking to see your words appear here...</p>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                )}

                                {/* Saved Answer Display */}
                                {userAnswer && !isRecording && showAnswer && (
                                    <div className='mt-4 p-4 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg border border-blue-200'>
                                        <div className='flex items-center justify-between mb-3'>
                                            <h4 className='text-sm font-semibold text-blue-800'>Your Recorded Answer:</h4>
                                            <Button
                                                onClick={() => {
                                                    setUserAnswer('')
                                                    setResults([])
                                                }}
                                                variant="outline"
                                                size="sm"
                                                className='text-xs'
                                            >
                                                Clear Answer
                                            </Button>
                                        </div>
                                        <div className='bg-white p-3 rounded border'>
                                            <p className='text-sm text-gray-900 leading-relaxed'>{userAnswer}</p>
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>

                        {/* End Interview Button */}
                        <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-4'>
                            <Button
                                onClick={EndInterview}
                                className='w-full h-12 text-lg font-semibold bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-700 hover:to-emerald-700 text-white'
                            >
                                <CheckCircle className='w-5 h-5 mr-2' />
                                End Interview
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default StartInterview
