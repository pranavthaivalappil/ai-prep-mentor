import React from 'react'

function DashboardLayout({children}) {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto">
        {children}
      </div>
    </div>
  )
}

export default DashboardLayout