import React from 'react'
import { Button } from './ui/button'
import Link from 'next/link'

const Landing = () => {
  return (
    <div className="h-[90vh] relative">
      <div className="max-w-7xl mx-auto h-full flex flex-col items-center justify-center gap-4">
        <div className="">
          <h1 className="font-bold text-6xl text-center mb-4">
            Lorem ipsum dolor sit amet consectetur adipisicing.
          </h1>
          <p className="text-base text-center">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus
            modi explicabo cumque, quis illo repellat?
          </p>
          <Link href="/biddings">
            <Button>Get Started</Button>
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Landing
