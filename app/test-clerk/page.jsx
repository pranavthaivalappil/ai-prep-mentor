'use client'
import { useAuth, useUser } from '@clerk/nextjs'

export default function TestClerk() {
  const { isLoaded, userId, sessionId } = useAuth()
  const { user } = useUser()

  if (!isLoaded) {
    return <div className="p-8">Loading Clerk...</div>
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Clerk Test Page</h1>
      
      <div className="space-y-4">
        <div>
          <strong>Auth Status:</strong> {userId ? 'Signed In' : 'Not Signed In'}
        </div>
        
        <div>
          <strong>User ID:</strong> {userId || 'None'}
        </div>
        
        <div>
          <strong>Session ID:</strong> {sessionId || 'None'}
        </div>
        
        <div>
          <strong>User Email:</strong> {user?.primaryEmailAddress?.emailAddress || 'None'}
        </div>

        <div className="space-x-4 mt-6">
          <a href="/sign-in" className="bg-blue-500 text-white px-4 py-2 rounded">
            Go to Sign In
          </a>
          <a href="/sign-up" className="bg-green-500 text-white px-4 py-2 rounded">
            Go to Sign Up
          </a>
        </div>
      </div>
    </div>
  )
} 