import type { Metadata } from 'next'
import '@/styles/output.css'
import Providers from '@/store/redux-provider'

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
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
