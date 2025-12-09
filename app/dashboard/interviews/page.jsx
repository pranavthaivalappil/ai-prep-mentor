'use client'
import React, { useEffect, useState } from 'react'
import { db } from '../../../utils/db'
import { MockInterview } from '../../../utils/schema'
import { eq, desc } from 'drizzle-orm'
import { useUser } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'
import { Button } from '../../../components/ui/button'
import { Play, BarChart3, Trash2, Plus, Calendar, Briefcase } from 'lucide-react'
import moment from 'moment'

function MyInterviewsPage() {
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
        return (
            <div className="py-8">
                <div className="text-center">
                    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
                    <p className="text-gray-600">Loading your interviews...</p>
                </div>
            </div>
        )
    }

    return (
        <div className="py-8">
            {/* Header */}
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-3xl font-bold text-gray-900">My Interviews</h1>
                    <p className="text-gray-600 mt-2">
                        Manage and review all your mock interviews
                    </p>
                </div>
                <Button 
                    onClick={() => router.push('/dashboard')}
                    className="flex items-center space-x-2"
                >
                    <Plus className="w-4 h-4" />
                    <span>Create New Interview</span>
                </Button>
            </div>

            {/* Stats */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div className="bg-white p-6 rounded-lg border border-gray-200">
                    <div className="flex items-center">
                        <div className="p-2 bg-blue-100 rounded-lg">
                            <Briefcase className="w-6 h-6 text-blue-600" />
                        </div>
                        <div className="ml-4">
                            <p className="text-sm font-medium text-gray-600">Total Interviews</p>
                            <p className="text-2xl font-bold text-gray-900">{interviewList.length}</p>
                        </div>
                    </div>
                </div>
                
                <div className="bg-white p-6 rounded-lg border border-gray-200">
                    <div className="flex items-center">
                        <div className="p-2 bg-green-100 rounded-lg">
                            <Calendar className="w-6 h-6 text-green-600" />
                        </div>
                        <div className="ml-4">
                            <p className="text-sm font-medium text-gray-600">This Month</p>
                            <p className="text-2xl font-bold text-gray-900">
                                {interviewList.filter(interview => 
                                    moment(interview.createdAt).isAfter(moment().startOf('month'))
                                ).length}
                            </p>
                        </div>
                    </div>
                </div>
                
                <div className="bg-white p-6 rounded-lg border border-gray-200">
                    <div className="flex items-center">
                        <div className="p-2 bg-purple-100 rounded-lg">
                            <BarChart3 className="w-6 h-6 text-purple-600" />
                        </div>
                        <div className="ml-4">
                            <p className="text-sm font-medium text-gray-600">Success Rate</p>
                            <p className="text-2xl font-bold text-gray-900">85%</p>
                        </div>
                    </div>
                </div>
            </div>

            {/* Interview List */}
            {interviewList.length === 0 ? (
                <div className="text-center py-12 bg-white rounded-lg border border-gray-200">
                    <Briefcase className="w-16 h-16 text-gray-400 mx-auto mb-4" />
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">No interviews yet</h3>
                    <p className="text-gray-600 mb-6">Create your first AI mock interview to get started!</p>
                    <Button 
                        onClick={() => router.push('/dashboard')}
                        className="flex items-center space-x-2 mx-auto"
                    >
                        <Plus className="w-4 h-4" />
                        <span>Create Interview</span>
                    </Button>
                </div>
            ) : (
                <div className="space-y-4">
                    {interviewList.map((interview) => (
                        <div key={interview.id} className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow">
                            <div className="flex items-center justify-between">
                                <div className="flex-1">
                                    <div className="flex items-center space-x-4">
                                        <div className="flex-1">
                                            <h3 className="text-lg font-semibold text-gray-900 mb-1">
                                                {interview.jobPosition}
                                            </h3>
                                            <p className="text-sm text-gray-600 mb-2">
                                                {interview.jobDescr}
                                            </p>
                                            <div className="flex items-center text-xs text-gray-500 space-x-4">
                                                <span className="flex items-center">
                                                    <Calendar className="w-3 h-3 mr-1" />
                                                    Created {moment(interview.createdAt).fromNow()}
                                                </span>
                                                <span>{interview.jobLocation}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div className="flex items-center space-x-2">
                                    <Button
                                        onClick={() => router.push(`/dashboard/interview/${interview.mockInterviewId}/feedback`)}
                                        variant="outline"
                                        size="sm"
                                    >
                                        <BarChart3 className="w-4 h-4 mr-1" />
                                        Feedback
                                    </Button>
                                    <Button
                                        onClick={() => router.push(`/dashboard/interview/${interview.mockInterviewId}`)}
                                        size="sm"
                                    >
                                        <Play className="w-4 h-4 mr-1" />
                                        Start
                                    </Button>
                                    <Button
                                        onClick={() => DeleteInterview(interview.mockInterviewId)}
                                        variant="outline"
                                        size="sm"
                                        className="text-red-600 hover:text-red-700"
                                    >
                                        <Trash2 className="w-4 h-4" />
                                    </Button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    )
}

export default MyInterviewsPage 