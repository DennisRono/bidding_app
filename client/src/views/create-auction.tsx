'use client'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { Loader2 } from 'lucide-react'
import { api } from '@/lib/api'

const formSchema = z.object({
  companyName: z.string().min(2, {
    message: 'Company name must be at least 2 characters.',
  }),
  description: z.string().min(10, {
    message: 'Description must be at least 10 characters.',
  }),
  biddingDate: z.string().nonempty({
    message: 'Bidding date is required.',
  }),
  startingBid: z.number().min(1, {
    message: 'Starting bid must be at least 1.',
  }),
})

export default function CreateAuction() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      companyName: '',
      description: '',
      biddingDate: '',
      startingBid: 0,
    },
  })

  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      setIsSubmitting(true)
      const res = await api('create-auction', { method: 'POST', body: values })
      const data = await res.json()
      if (res.ok) {
        // clear input fields
        form.reset()
      } else {
        throw new Error(data.message)
      }
    } catch (error) {
      console.log(error)
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="flex-1 rounded-md">
      <h2 className="text-2xl font-bold mb-6">Create an Auction</h2>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            control={form.control}
            name="companyName"
            render={({ field }) => (
              <FormItem>
                <FormLabel>
                  Company Name <span className="text-red">*</span>
                </FormLabel>
                <FormControl>
                  <Input
                    placeholder="Company Name"
                    {...field}
                    className="p-5"
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="description"
            render={({ field }) => (
              <FormItem>
                <FormLabel>
                  Description <span className="text-red">*</span>
                </FormLabel>
                <FormControl>
                  <Textarea
                    placeholder="Description of the auction item"
                    {...field}
                    className="p-5"
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="biddingDate"
            render={({ field }) => (
              <FormItem>
                <FormLabel>
                  Bidding Date <span className="text-red">*</span>
                </FormLabel>
                <FormControl>
                  <Input type="date" {...field} className="p-5" />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="startingBid"
            render={({ field }) => (
              <FormItem>
                <FormLabel>
                  Starting Bid <span className="text-red">*</span>
                </FormLabel>
                <FormControl>
                  <Input type="number" {...field} className="p-5" />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <div className="flex justify-end w-full">
            <Button
              type="submit"
              className="w-min px-8 text-white bg-indigo-600 hover:bg-indigo-700"
              disabled={isSubmitting}
            >
              {isSubmitting ? (
                <div className="flex items-center justify-center gap-2">
                  <Loader2 className="h-4 w-6 animate-spin" />
                  <span>Submitting...</span>
                </div>
              ) : (
                'Create Auction'
              )}
            </Button>
          </div>
        </form>
      </Form>
    </div>
  )
}
