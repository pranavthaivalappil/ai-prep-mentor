import React from 'react'
import { UserButton } from '@clerk/nextjs'

export default function Dashboard() {
  return (
    <div className="p-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <UserButton />
      </div>
      <p className="text-gray-600">Welcome to your dashboard!</p>
    </div>
  )
}
