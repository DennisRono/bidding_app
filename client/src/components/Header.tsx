import Link from 'next/link'
import React from 'react'
import { Button } from './ui/button'

const Header = () => {
  return (
    <div className="h-16 border-b border-gray-500 shadow-sm">
      <div className="max-w-7xl w-full h-full flex items-center justify-between px-4">
        <div className="">
          <h1 className="font-bold text-2xl">Bidding App</h1>
        </div>
        <div className="">
          <Link href="/biddings">
            <Button>Get Started</Button>
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Header
