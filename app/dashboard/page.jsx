import React from 'react'
import AddNewInterview from './_components/AddNewInterview'
import InterviewList from './_components/InterviewList'

export default function Dashboard() {
  return (
    <div className="p-8">
      <div className="mb-6">
        <h1 className='font-bold text-2xl'>Dashboard</h1>
        <p className='text-gray-600'>Create and manage your mock interviews</p>
      </div>

      <div className='grid grid-cols-1 md:grid-cols-3 gap-4 mb-8'>
        <AddNewInterview/>
      </div>

      <InterviewList />
    </div>
  )
}
