import React from 'react'
import { Header } from './_components/Header'

function DashboardLayout({children}) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
      <Header />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {children}
      </main>
      
      {/* Footer */}
      <footer className="mt-auto py-6 px-4 text-center">
        <div className="max-w-7xl mx-auto space-y-2">
          <p className="text-sm text-gray-500">
            Made with ❤️ by <span className="font-semibold text-gray-700">Pranav</span>
          </p>
          <p className="text-xs text-gray-400">
            Powered by <span className="font-medium text-blue-600">Google Gemini AI</span>
          </p>
        </div>
      </footer>
    </div>
  )
}

export default DashboardLayout