'use client'
import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { UserButton } from '@clerk/nextjs'
import { usePathname } from 'next/navigation'
import { useEffect } from 'react'

function Header() {
    const pathname = usePathname();
    useEffect(() => {
        console.log(pathname);
    }, [pathname]);
  return (
    <div className='flex justify-between items-center p-4 bg-secondary shadow-sm'>
        <Image src="/logo.svg" alt="logo" width={67} height={41} />
        <ul className='hidden md:flex gap-4'>
            <li className={`text-sm font-medium hover:text-primary transition-all hover:font-bold cursor-pointer ${pathname === '/dashboard'  ? 'text-primary font-bold' : ''}`}>
                <Link href="/">Dashboard</Link>
            </li>
            <li className={`text-sm font-medium hover:text-primary transition-all hover:font-bold cursor-pointer ${pathname === '/dashboard/questions'  ? 'text-primary font-bold' : ''}`}>
                <Link href="/">Questions</Link>
            </li>
            <li className={`text-sm font-medium hover:text-primary transition-all hover:font-bold cursor-pointer ${pathname === '/dashboard/upgrade'  ? 'text-primary font-bold' : ''}`}>
                <Link href="/">Upgrade</Link>
            </li>
            <li className={`text-sm font-medium hover:text-primary transition-all hover:font-bold cursor-pointer ${pathname === '/dashboard/how'  ? 'text-primary font-bold' : ''}`}>
                <Link href="/">How it works</Link>
            </li>
        </ul>
        <UserButton />
    </div>
  )
}

export default Header