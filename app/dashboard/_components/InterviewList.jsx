'use client'
import React, { useEffect, useState } from 'react'
import { db } from '../../../utils/db'
import { MockInterview } from '../../../utils/schema'
import { eq, desc } from 'drizzle-orm'
import { useUser } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'
import { Button } from '../../../components/ui/button'
import { Play, BarChart3, Trash2 } from 'lucide-react'
import moment from 'moment'

function InterviewList() {
    const { user } = useUser()
    const [interviewList, setInterviewList] = useState([])
    const [loading, setLoading] = useState(true)
    const router = useRouter()

    useEffect(() => {
        if (user) {
            GetInterviewList()
        }
    }, [user])

    const GetInterviewList = async () => {
        try {
            const result = await db.select()
                .from(MockInterview)
                .where(eq(MockInterview.createdBy, user?.primaryEmailAddress?.emailAddress))
                .orderBy(desc(MockInterview.createdAt))

            setInterviewList(result)
        } catch (error) {
            console.error('Error fetching interviews:', error)
        } finally {
            setLoading(false)
        }
    }

    const DeleteInterview = async (interviewId) => {
        if (window.confirm("Delete this interview?")) {
            try {
                await db.delete(MockInterview)
                    .where(eq(MockInterview.mockInterviewId, interviewId))
                GetInterviewList()
            } catch (error) {
                console.error('Error deleting interview:', error)
            }
        }
    }

    if (loading) {
        return <div className='my-5'><p>Loading interviews...</p></div>
    }

    if (interviewList.length === 0) {
        return (
            <div className='my-5'>
                <h2 className='font-bold text-lg mb-3'>Previous Interviews</h2>
                <p className='text-gray-500'>No interviews created yet.</p>
            </div>
        )
    }

    return (
        <div className='my-5'>
            <h2 className='font-bold text-lg mb-3'>Previous Interviews</h2>
            <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
                {interviewList.map((interview) => (
                    <div key={interview.id} className='border rounded-lg p-4 bg-white'>
                        <h3 className='font-semibold text-md mb-2'>{interview.jobPosition}</h3>
                        <p className='text-sm text-gray-600 mb-2'>{interview.jobDescr}</p>
                        <p className='text-xs text-gray-500 mb-3'>
                            Created {moment(interview.createdAt).fromNow()}
                        </p>
                        
                        <div className='flex gap-2'>
                            <Button
                                onClick={() => router.push(`/dashboard/interview/${interview.mockInterviewId}`)}
                                size="sm"
                                className='flex-1'
                            >
                                <Play className='w-4 h-4 mr-1' />
                                Start
                            </Button>
                            <Button
                                onClick={() => router.push(`/dashboard/interview/${interview.mockInterviewId}/feedback`)}
                                variant="outline"
                                size="sm"
                                className='flex-1'
                            >
                                <BarChart3 className='w-4 h-4 mr-1' />
                                Feedback
                            </Button>
                            <Button
                                onClick={() => DeleteInterview(interview.mockInterviewId)}
                                variant="outline"
                                size="sm"
                                className='text-red-600'
                            >
                                <Trash2 className='w-4 h-4' />
                            </Button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default InterviewList 