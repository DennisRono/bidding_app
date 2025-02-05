'use client'
import React, { useEffect, useState } from 'react'
import { api } from '@/lib/api'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { format } from 'date-fns'
import { Skeleton } from '@/components/ui/skeleton'
import Link from 'next/link'

interface AuctionType {
  id: string
  auction_name: string
  auction_description: string
  start_time: Date
  end_time: Date
}

const ViewAuctions = () => {
  const [isFetching, setIsFetching] = useState<boolean>(false)
  const [auctions, setAuctions] = useState<[]>([])

  const fetchAuctions = async () => {
    try {
      setIsFetching(true)
      const res = await api('auction', {
        method: 'GET',
      })
      const data = await res.json()
      if (res.ok) {
        setAuctions(data)
      } else {
        throw new Error(data.message)
      }
    } catch (error) {
      console.log(error)
    } finally {
      setIsFetching(false)
    }
  }

  useEffect(() => {
    fetchAuctions()
  }, [])

  if (isFetching) {
    return <LoaderSkeleton />
  }

  return (
    <div className="grid grid-cols-4">
      {Array.isArray(auctions) &&
        auctions.map((auction: AuctionType, i) => (
          <Card key={i}>
            <CardHeader>
              <CardTitle>{auction.auction_name}</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription>{auction.auction_description}</CardDescription>
              <p className="text-xs text-muted-foreground mt-2">
                Start Date:{' '}
                {format(new Date(auction.start_time), 'dd/MM/yyyy HH:mm aa')}
              </p>
              <p className="text-xs text-muted-foreground">
                End Date:{' '}
                {format(new Date(auction.end_time), 'dd/MM/yyyy HH:mm aa')}
              </p>
            </CardContent>
            <CardFooter>
              <Link href={`/auctions/${auction.id}`}>
                <Button>View Auction</Button>
              </Link>
            </CardFooter>
          </Card>
        ))}
    </div>
  )
}

const LoaderSkeleton = () => {
  return (
    <div className="w-full grid grid-cols-4 gap-4">
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
      <Skeleton className="h-40" />
    </div>
  )
}

export default ViewAuctions
