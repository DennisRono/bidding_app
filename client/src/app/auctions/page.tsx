import Footer from '@/components/Footer'
import Header from '@/components/Header'
import ViewAuctions from '@/views/view-auctions'
import React from 'react'

const Auctions = () => {
  return (
    <div>
      <Header />
      <div className="p-2 min-h-[80vh]">
        <ViewAuctions />
      </div>
      <Footer />
    </div>
  )
}

export default Auctions
