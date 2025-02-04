import Footer from '@/components/Footer'
import Header from '@/components/Header'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardFooter } from '@/components/ui/card'
import { ChartNoAxesGantt } from 'lucide-react'
import Image from 'next/image'
import React from 'react'

const page = () => {
  return (
    <div>
      <Header />
      <div className="max-w-7xl flex flex-wrap justify-start gap-4 p-2">
        {Array.from({ length: 2 }).map((_, i) => (
          <Card className="!w-[300px] p-2" key={i}>
            <CardContent className="!p-0">
              <div className="relative w-full overflow-hidden">
                <Image
                  src="https://res.cloudinary.com/eleving-vehicle-finance/image/upload/f_auto,q_auto,w_750,h_420,c_fill/production_ke/hj8emZiE6aYDorOm2js0aSOs8tOx6ajxot16ipem"
                  alt=""
                  width={300}
                  height={300}
                />
              </div>
              <div className="">
                <div className="flex">
                  <div className="flex">
                    <ChartNoAxesGantt size={20} />
                    <span>10</span>
                  </div>
                </div>
                <h1 className="leading-tight line-clamp-2 overflow-ellipsis font-bold text-lg">
                  Company A
                </h1>
              </div>
            </CardContent>
            <CardFooter className="!p-0">
              <div className="w-full flex justify-end">
                <Button>View Catalog</Button>
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
