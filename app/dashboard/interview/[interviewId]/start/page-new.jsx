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

    // Speech to Text Hook
    const {
        error,
        interimResult,
        isRecording,
        results,
        startSpeechToText,
        stopSpeechToText,
        setResults
    } = useSpeechToText({
        continuous: true,
        useLegacyResults: false
    })

    useEffect(()=>{
        setIsMounted(true)
        GetInterviewDetails()
    },[resolvedParams.interviewId])

    // Update userAnswer when results change
    useEffect(() => {
        if (results.length > 0) {
            const transcript = results.map(result => result.transcript).join(' ')
            setUserAnswer(transcript)
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
        
        const confirmEnd = window.confirm("Are you sure you want to end the interview?")
        if (confirmEnd) {
            router.push('/dashboard/interview/' + resolvedParams.interviewId + '/feedback')
        }
    }

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
                        AI Mock Interview (New Speech Recognition)
                    </h1>
                    <p className='text-gray-600'>
                        Question {activeQuestionIndex + 1} of {mockInterviewQuestions?.length}
                    </p>
                </div>

                {/* Speech Error Alert */}
                {error && (
                    <div className='mb-6 max-w-4xl mx-auto'>
                        <div className='bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3'>
                            <AlertCircle className='w-5 h-5 text-red-600 mt-0.5 flex-shrink-0' />
                            <div className='flex-1'>
                                <p className='text-sm text-red-800'>Speech Recognition Error: {error}</p>
                                <p className='text-xs text-red-600 mt-1'>Please check your microphone permissions and try again.</p>
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
                                <Lightbulb className='w-4 h-4 text-blue-600 mr-2' />
                                <h3 className='text-base font-semibold text-gray-800'>Note</h3>
                            </div>
                            <p className='text-sm text-gray-600'>
                                Click "Record Answer" to start speech recognition. The new implementation should work better!
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
                                            {isRecording ? 'Recording' : 'Live'}
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
                                    >
                                        {isRecording ? (
                                            <>
                                                <MicOff className='w-5 h-5 mr-2' />
                                                Stop Recording
                                            </>
                                        ) : (
                                            <>
                                                <Mic className='w-5 h-5 mr-2' />
                                                Record Answer
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
                                            {showAnswer ? 'Hide User Answer' : 'Show User Answer'}
                                        </Button>
                                    )}
                                </div>

                                {/* Live Transcription Display */}
                                {isRecording && (
                                    <div className='mt-4 p-4 bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg border border-green-200'>
                                        <div className='flex items-center mb-3'>
                                            <div className='w-2 h-2 bg-red-500 rounded-full animate-pulse mr-2'></div>
                                            <h4 className='text-sm font-semibold text-green-800'>Live Transcription:</h4>
                                            <span className='ml-auto text-xs text-green-600'>Listening...</span>
                                        </div>
                                        <div className='bg-white p-3 rounded border min-h-[60px]'>
                                            {userAnswer || interimResult ? (
                                                <p className='text-sm text-gray-900 leading-relaxed'>
                                                    <span className='text-gray-900'>{userAnswer}</span>
                                                    <span className='text-gray-500 italic'> {interimResult}</span>
                                                </p>
                                            ) : (
                                                <p className='text-sm text-gray-500 italic'>
                                                    Start speaking to see transcription...
                                                </p>
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