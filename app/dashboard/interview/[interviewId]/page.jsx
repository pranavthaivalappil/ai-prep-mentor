'use client'
import React, { useEffect, useState } from 'react'
import { db } from '../../../../utils/db'
import { MockInterview } from '../../../../utils/schema'
import { eq } from 'drizzle-orm'
import Webcam from 'react-webcam'
import { WebcamIcon, Play, Settings, Info, Camera, CameraOff } from 'lucide-react'
import { Button } from '../../../../components/ui/button'
import Link from 'next/link'

function Interview({params}) {
    const resolvedParams = React.use(params)
    const [interviewDetails, setInterviewDetails] = useState(null);
    const [webcamEnabled, setWebcamEnabled] = useState(false);

    useEffect(()=>{
        console.log(resolvedParams.interviewId)
        GetInterviewDetails()
    },[resolvedParams.interviewId])

    const GetInterviewDetails = async()=>{
        const resp = await db.select().from(MockInterview).where(eq(MockInterview.mockInterviewId, resolvedParams.interviewId))
        setInterviewDetails(resp[0]);
    }

  return (
        <div className='min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-2'>
            <div className='max-w-7xl mx-auto'>
                
                {/* Compact Header */}
                <div className='text-center mb-4'>
                    <h1 className='text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-2'>
                        AI Mock Interview
                    </h1>
                    <p className='text-sm text-gray-600 max-w-2xl mx-auto'>
                        Practice your interview skills with our AI-powered system
                    </p>
                </div>

                {/* Compact Main Content Grid */}
                <div className='grid lg:grid-cols-3 gap-2'>
                    
                    {/* Left Column - Interview Details */}
                    <div className='lg:col-span-1 space-y-4'>
                        
                        {/* Interview Info Card */}
                        {interviewDetails ? (
                            <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-4'>
                                <div className='flex items-center mb-3'>
                                    <Info className='w-4 h-4 text-blue-600 mr-2' />
                                    <h2 className='text-base font-semibold text-gray-800'>Interview Details</h2>
                                </div>
                                
                                <div className='space-y-3'>
                                    <div className='bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-3'>
                                        <h3 className='font-medium text-gray-700 text-xs mb-1'>Position</h3>
                                        <p className='text-gray-900 font-semibold text-sm'>{interviewDetails.jobPosition}</p>
                                    </div>
                                    
                                    <div className='bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg p-3'>
                                        <h3 className='font-medium text-gray-700 text-xs mb-1'>Tech Stack & Description</h3>
                                        <p className='text-gray-900 text-sm'>{interviewDetails.jobDescr}</p>
                                    </div>
                                    
                                    <div className='bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg p-3'>
                                        <h3 className='font-medium text-gray-700 text-xs mb-1'>Experience Level</h3>
                                        <p className='text-gray-900 text-sm'>{interviewDetails.jobLocation}</p>
                                    </div>
                                </div>
                            </div>
                        ) : (
                            <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-4'>
                                <div className='animate-pulse space-y-3'>
                                    <div className='h-4 bg-gray-200 rounded-lg w-3/4'></div>
                                    <div className='h-16 bg-gray-200 rounded-lg'></div>
                                    <div className='h-14 bg-gray-200 rounded-lg'></div>
                                    <div className='h-12 bg-gray-200 rounded-lg'></div>
                                </div>
                            </div>
                        )}

                        {/* Instructions Card */}
                        <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 p-4'>
                            <div className='flex items-center mb-3'>
                                <Settings className='w-4 h-4 text-indigo-600 mr-2' />
                                <h2 className='text-base font-semibold text-gray-800'>Quick Tips</h2>
                            </div>
                            
                            <div className='space-y-2'>
                                <div className='flex items-start space-x-3'>
                                    <div className='w-2 h-2 bg-indigo-500 rounded-full mt-2 flex-shrink-0'></div>
                                    <p className='text-gray-700 text-sm'>Enable your camera for the best experience</p>
                                </div>
                                <div className='flex items-start space-x-3'>
                                    <div className='w-2 h-2 bg-purple-500 rounded-full mt-2 flex-shrink-0'></div>
                                    <p className='text-gray-700 text-sm'>Speak clearly and maintain eye contact</p>
                                </div>
                                <div className='flex items-start space-x-3'>
                                    <div className='w-2 h-2 bg-blue-500 rounded-full mt-2 flex-shrink-0'></div>
                                    <p className='text-gray-700 text-sm'>Take your time to think before answering</p>
                                </div>
                                <div className='flex items-start space-x-3'>
                                    <div className='w-2 h-2 bg-green-500 rounded-full mt-2 flex-shrink-0'></div>
                                    <p className='text-gray-700 text-sm'>Practice makes perfect - you can retake anytime</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right Column - Webcam and Controls */}
                    <div className='lg:col-span-2 space-y-4'>
                        
                        {/* Webcam Card */}
                        <div className='bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border border-white/50 overflow-hidden'>
                            
                            {/* Compact Webcam Header */}
                            <div className='bg-gradient-to-r from-gray-50 to-gray-100 px-4 py-3 border-b border-gray-200'>
                                <div className='flex items-center justify-between'>
                                    <div className='flex items-center space-x-2'>
                                        <Camera className='w-4 h-4 text-gray-700' />
                                        <h2 className='text-base font-semibold text-gray-800'>Camera Preview</h2>
                                    </div>
                                    <div className='flex items-center space-x-2'>
                                        <div className={`w-2.5 h-2.5 rounded-full ${webcamEnabled ? 'bg-green-400' : 'bg-red-400'} shadow-lg`}></div>
                                        <span className='text-xs font-medium text-gray-600'>
                                            {webcamEnabled ? 'Live' : 'Offline'}
                                        </span>
                                    </div>
                                </div>
                            </div>

                            {/* Compact Webcam Content */}
                            <div className='p-4'>
                                <div className='relative rounded-lg overflow-hidden bg-gray-900' style={{aspectRatio: '16/9', height: '320px'}}>
                                    {webcamEnabled ? (
                                        <Webcam
                                            onUserMedia={() => setWebcamEnabled(true)}
                                            onUserMediaError={() => setWebcamEnabled(false)}
                                            mirrored={true}
                                            className='w-full h-full object-cover'
                                        />
                                    ) : (
                                        <div className='flex flex-col items-center justify-center h-full text-gray-400'>
                                            <WebcamIcon className='w-8 h-8 mb-1 opacity-50' />
                                            <p className='text-xs font-medium'>Camera Disabled</p>
                                            <p className='text-xs text-center px-2'>
                                                Click Enable
                                            </p>
                                        </div>
                                    )}
                                    
                                    {/* Compact Camera overlay */}
                                    {webcamEnabled && (
                                        <div className='absolute top-1 right-1'>
                                            <div className='bg-black/20 backdrop-blur-sm rounded px-1.5 py-0.5'>
                                                <span className='text-white text-xs'>Ready</span>
                                            </div>
                                        </div>
                                    )}
                                </div>

                                {/* Camera Controls and Start Button */}
                                <div className='flex gap-3 mt-4'>
                                    <Button
                                        onClick={() => setWebcamEnabled(!webcamEnabled)}
                                        variant={webcamEnabled ? "destructive" : "default"}
                                        className='flex-1 h-10 text-sm font-medium'
                                    >
                                        {webcamEnabled ? (
                                            <>
                                                <CameraOff className='w-4 h-4 mr-2' />
                                                Disable Camera
                                            </>
                                        ) : (
                                            <>
                                                <Camera className='w-4 h-4 mr-2' />
                                                Enable Camera
                                            </>
                                        )}
                                    </Button>
                                    
                                    {webcamEnabled ? (
                                        <Link href={'/dashboard/interview/' + resolvedParams.interviewId + '/start'}>
                                            <Button
                                                className='flex-[2] h-10 text-sm font-semibold bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 hover:from-blue-700 hover:via-purple-700 hover:to-indigo-700 text-white shadow-lg hover:shadow-xl transform hover:scale-[1.02] transition-all duration-300'
                                            >
                                                <Play className='w-4 h-4 mr-2' />
                                                Start AI Interview
                                            </Button>
                                        </Link>
                                    ) : (
                                        <Button
                                            disabled={true}
                                            className='flex-[2] h-10 text-sm font-semibold bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 hover:from-blue-700 hover:via-purple-700 hover:to-indigo-700 text-white shadow-lg hover:shadow-xl transform hover:scale-[1.02] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none'
                                        >
                                            <Play className='w-4 h-4 mr-2' />
                                            Start AI Interview
                                        </Button>
                                    )}
                                </div>
                                
                                {!webcamEnabled && (
                                    <p className='text-sm text-gray-500 mt-3 text-center flex items-center justify-center'>
                                        <Info className='w-4 h-4 mr-1' />
                                        Camera must be enabled to start the interview
                                    </p>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
  )
}

export default Interview