"use client"

import React, { useState } from 'react'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../../../components/ui/dialog"
import { Button } from "../../../components/ui/button"
import { Input } from "../../../components/ui/input"
import { Textarea } from "../../../components/ui/textarea"
import { generateInterviewQuestions } from "../../../utils/gemini"
import { v4 as uuidv4 } from 'uuid';
import moment from 'moment'
import { useUser } from '@clerk/nextjs'
import { db } from '../../../utils/db'
import { MockInterview } from '../../../utils/schema'
import { useRouter } from 'next/navigation'

function AddNewInterview() {
  const [isOpen, setIsOpen] = useState(false)
  const [jobPosition, setJobPosition] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [jobExperience, setJobExperience] = useState('')
  const [loading, setLoading] = useState(false)
  const [jsonResponse, setJsonResponse] = useState([])
  const {user} = useUser()
  const router = useRouter()
  const onSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    const InputPrompt = "Job Position: " + jobPosition + 
        ", Job Description: " + jobDescription + 
        ", Job Experience: " + jobExperience + " years"
    
    try {
      console.log('Generating interview questions...')
      
      // Generate interview questions using Gemini API
      const result = await generateInterviewQuestions(
        jobPosition, 
        jobDescription, 
        jobExperience
      );
      
      if (result.success) {
        console.log('Generated Questions:', result.data)
        setJsonResponse(result.data);

        // Convert questions array to JSON string for database storage
        const MockJsonResp = JSON.stringify(result.data);

        const resp = await db.insert(MockInterview).values({
          mockInterviewId: uuidv4(),
          jobPosition: jobPosition,  
          jobDescr: jobDescription,
          jobLocation: jobExperience + " years experience", // Using experience as location for now
          jsonMockResp: MockJsonResp,
          createdBy: user?.primaryEmailAddress?.emailAddress
        }).returning({mockId: MockInterview.mockInterviewId})

        console.log("inserted mock interview id: ",resp[0].mockId)
        console.log(resp)
        router.push(`/dashboard/interview/${resp[0].mockId}`)
        alert('Interview questions generated successfully!')
      } else {
        console.error('Failed to generate questions:', result.error)
        alert('Failed to generate interview questions. Please try again.')
      }
      
    } catch (error) {
      console.error('Error:', error)
      alert('An error occurred. Please try again.')
    } finally {
      setLoading(false)
      setIsOpen(false)
      // Reset form
      setJobPosition('')
      setJobDescription('')
      setJobExperience('')
    }
  }

  return (
    <div>
      <Dialog open={isOpen} onOpenChange={setIsOpen}>
        <DialogTrigger asChild>
          <div className='p-8 border rounded-lg flex flex-col items-center justify-center hover:shadow-md cursor-pointer bg-gray-50 hover:bg-gray-100 transition-all relative'>
            <div className='absolute top-2 right-2 bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded-full font-medium'>
              ✨ AI Powered
            </div>
            <h2 className='text-lg font-bold text-gray-800 mb-2'>+ Add New Interview</h2>
            <p className='text-gray-600 text-center text-sm'>Create a new AI mock interview</p>
          </div>
        </DialogTrigger>
        
        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>Create New Mock Interview</DialogTitle>
            <DialogDescription>
              Add details about your job position to create a customized mock interview
            </DialogDescription>
          </DialogHeader>
          
          <form onSubmit={onSubmit}>
            <div className="grid gap-4 py-4">
              <div className="grid gap-2">
                <label htmlFor="jobPosition" className="text-sm font-medium">
                  Job Position
                </label>
                <Input
                  id="jobPosition"
                  placeholder="Ex. Full Stack Developer"
                  value={jobPosition}
                  onChange={(e) => setJobPosition(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>
              
              <div className="grid gap-2">
                <label htmlFor="jobDescription" className="text-sm font-medium">
                  Job Description/Tech Stack
                </label>
                <Textarea
                  id="jobDescription"
                  placeholder="Ex. React, Angular, NodeJS, MySQL etc"
                  rows={3}
                  value={jobDescription}
                  onChange={(e) => setJobDescription(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>
              
              <div className="grid gap-2">
                <label htmlFor="jobExperience" className="text-sm font-medium">
                  Years of Experience
                </label>
                <Input
                  id="jobExperience"
                  type="number"
                  placeholder="Ex. 5"
                  max={50}
                  min={0}
                  value={jobExperience}
                  onChange={(e) => setJobExperience(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>
            </div>
            
            <DialogFooter>
              <Button 
                type="button" 
                variant="outline" 
                onClick={() => setIsOpen(false)}
                disabled={loading}
              >
                Cancel
              </Button>
              <Button 
                type="submit"
                disabled={loading}
              >
                {loading ? 'Generating AI Questions ...' : 'Start Interview'}
              </Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>
    </div>
  )
}

export default AddNewInterview

