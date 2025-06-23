"use client"
import { UserButton } from '@clerk/nextjs'
import Image from 'next/image'
import { usePathname, useRouter } from 'next/navigation'
import React from 'react'

export const Header = () => {
    const path = usePathname()
    const router = useRouter()

    return (
        <nav className='sticky top-0 z-50 flex items-center justify-between px-6 py-4 bg-white/80 backdrop-blur-md border-b border-white/20 shadow-lg shadow-black/5'>
            <div className='flex items-center'>
                <Image 
                    src={'/logo.svg'} 
                    alt='logo' 
                    width={120} 
                    height={40}
                    className='cursor-pointer'
                    onClick={() => router.push('/dashboard')}
                />
            </div>
            
            <div className='hidden md:flex items-center space-x-8'>
                <button
                    onClick={() => router.push('/dashboard')}
                    className={`text-sm font-medium transition-all duration-200 px-3 py-2 rounded-lg ${
                        path === '/dashboard' 
                            ? 'text-blue-600 bg-blue-50/80 backdrop-blur-sm' 
                            : 'text-gray-700 hover:text-blue-600 hover:bg-white/60'
                    }`}
                >
                    Dashboard
                </button>
                <button
                    onClick={() => router.push('/dashboard/interviews')}
                    className={`text-sm font-medium transition-all duration-200 px-3 py-2 rounded-lg ${
                        path === '/dashboard/interviews' 
                            ? 'text-blue-600 bg-blue-50/80 backdrop-blur-sm' 
                            : 'text-gray-700 hover:text-blue-600 hover:bg-white/60'
                    }`}
                >
                    My Interviews
                </button>
                <button
                    onClick={() => router.push('/dashboard/upgrade')}
                    className={`text-sm font-medium transition-all duration-200 px-3 py-2 rounded-lg ${
                        path === '/dashboard/practice' 
                            ? 'text-blue-600 bg-blue-50/80 backdrop-blur-sm' 
                            : 'text-gray-700 hover:text-blue-600 hover:bg-white/60'
                    }`}
                >
                    Upgrade
                </button>
                <button
                    onClick={() => router.push('/dashboard/help')}
                    className={`text-sm font-medium transition-all duration-200 px-3 py-2 rounded-lg ${
                        path === '/dashboard/help' 
                            ? 'text-blue-600 bg-blue-50/80 backdrop-blur-sm' 
                            : 'text-gray-700 hover:text-blue-600 hover:bg-white/60'
                    }`}
                >
                    Help
                </button>
            </div>

            <div className='flex items-center bg-white/40 backdrop-blur-sm rounded-full p-2'>
                <UserButton afterSignOutUrl="/" />
            </div>
        </nav>
    )
}