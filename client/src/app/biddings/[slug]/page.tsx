/* eslint-disable @typescript-eslint/no-explicit-any */
'use client'
import Footer from '@/components/Footer'
import Header from '@/components/Header'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card'
import { api } from '@/lib/api'
import Image from 'next/image'
import React, { useEffect, useState } from 'react'
import { format } from 'date-fns'

interface Product {
  product_description: string
  id: number
  end_time: Date
  product_image_urls: string[]
  product_name: string
  starting_price: number
  created_at: Date
}

const ProductListingPage = () => {
  const [products, setProducts] = useState([])
  const fetchProducts = async () => {
    const res: any = await api('products')
    const result = await res.json()
    if (res.ok) {
      setProducts(result)
    } else {
      throw new Error(result?.message ?? result?.detail)
    }
  }
  useEffect(() => {
    fetchProducts()
  }, [])

  console.log(products)
  return (
    <div>
      <Header />
      <div className="max-w-7xl flex flex-wrap justify-start gap-4">
        {Array.isArray(products) &&
          products.map((product: Product, i) => (
            <Card className="!w-[300px]" key={i}>
              <CardHeader></CardHeader>
              <CardContent>
                <div className="relative w-full overflow-hidden">
                  <Image
                    src="https://res.cloudinary.com/eleving-vehicle-finance/image/upload/f_auto,q_auto,w_750,h_420,c_fill/production_ke/hj8emZiE6aYDorOm2js0aSOs8tOx6ajxot16ipem"
                    alt=""
                    width={300}
                    height={300}
                    priority={false}
                  />
                </div>
              </CardContent>
              <CardFooter>
                <div className="w-full flex justify-between">
                  <div className="">
                    <p className="">
                      Bid End Time:{' '}
                      {format(product.end_time, 'MM/dd/yyyy hh:mm')}
                    </p>
                  </div>
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

export default ProductListingPage
