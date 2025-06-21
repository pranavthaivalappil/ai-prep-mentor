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

function AddNewInterview() {
  const [isOpen, setIsOpen] = useState(false)
  const [jobPosition, setJobPosition] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [jobExperience, setJobExperience] = useState('')

  const onSubmit = (e) => {
    e.preventDefault()
    console.log('Form submitted:', { jobPosition, jobDescription, jobExperience })
    // Here you'll add the tutorial's logic later
    setIsOpen(false)
  }

  return (
    <div>
      <Dialog open={isOpen} onOpenChange={setIsOpen}>
        <DialogTrigger asChild>
          <div className='p-10 border-2 border-gray-200 rounded-lg flex flex-col items-center justify-center hover:scale-105 hover:shadow-md cursor-pointer transition-all bg-gray-50 hover:bg-gray-100'>
            <h2 className='text-lg text-center font-bold text-gray-800'>+ Add New Interview</h2>
            <p className='text-gray-500 text-center mt-2'>Create a new AI mock interview</p>
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
                  value={jobExperience}
                  onChange={(e) => setJobExperience(e.target.value)}
                />
              </div>
            </div>
            
            <DialogFooter>
              <Button type="button" variant="outline" onClick={() => setIsOpen(false)}>
                Cancel
              </Button>
              <Button type="submit">Start Interview</Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>
    </div>
  )
}

export default AddNewInterview

