import React from 'react'
import Header from './_components/Header'

function DashboardLayout({children}) {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto">
        <Header />
        {children}
      </div>
    </div>
  )
}

export default DashboardLayout