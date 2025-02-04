import Footer from '@/components/Footer'
import Header from '@/components/Header'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card'
import Image from 'next/image'
import React from 'react'

const page = () => {
  return (
    <div>
      <Header />
      <div className="max-w-7xl flex flex-wrap justify-start gap-4">
        {Array.from({ length: 20 }).map((_, i) => (
          <Card className="!w-[300px]" key={i}>
            <CardHeader></CardHeader>
            <CardContent>
              <div className="relative w-full overflow-hidden">
                <Image
                  src="https://res.cloudinary.com/eleving-vehicle-finance/image/upload/f_auto,q_auto,w_750,h_420,c_fill/production_ke/hj8emZiE6aYDorOm2js0aSOs8tOx6ajxot16ipem"
                  alt=""
                  width={300}
                  height={300}
                />
              </div>
            </CardContent>
            <CardFooter>
              <div className="w-full flex justify-end">
                <Button>Make Bid</Button>
              </div>
            </CardFooter>
          </Card>
        ))}
      </div>
      <Footer />
    </div>
  )
}

export default page
