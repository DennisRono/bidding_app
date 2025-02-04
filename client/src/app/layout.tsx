import type { Metadata } from 'next'
import '@/styles/output.css'

export const metadata: Metadata = {
  title: 'Bidding Application',
  description: 'Bid for products in our app',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
