/* eslint-disable @typescript-eslint/no-explicit-any */
type FetchOptions = {
  method?: 'GET' | 'POST' | 'DELETE' | 'PATCH' | 'PUT'
  headers?: Record<string, string>
  body?: any
  retryCount?: number
}

const refreshToken = async (token: string, retries = 3): Promise<string> => {
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/login`,
      {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh_token: token }),
      }
    )

    if (!response.ok) {
      throw new Error('Failed to refresh token')
    }

    const data = await response.json()
    return data.access_token
  } catch (error: any) {
    console.log(error)
    if (retries > 0) {
      console.log(`Retrying... attempts left: ${retries}`)
      await new Promise((resolve) => setTimeout(resolve, 1000))
      refreshToken(token, retries - 1)
    }
    throw new Error('Failed to refresh access token after multiple attempts')
  }
}

export async function api(
  endpoint: string,
  options: FetchOptions = { method: 'GET' },
  maxRetries: number = 3,
  addAuthorization: boolean = true
): Promise<Response> {
  const fetchOptions: RequestInit = {
    method: options.method ?? 'GET',
    headers: {
      'Content-Type': options.headers?.['Content-Type'] || 'application/json',
      ...(addAuthorization && { Authorization: `Bearer ` }),
      ...options.headers,
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
    cache: 'no-cache',
    redirect: 'follow',
  }

  const fetchApi = async (retriesLeft: number): Promise<Response> => {
    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/${endpoint}`,
        fetchOptions
      )

      if (response.ok) {
        return response
      }

      if (response.status === 401) {
        console.log('Token Expired, Trying to refresh!')
        const newToken = await refreshToken('')
        if (newToken) {
          // Update Authorization header with the new token
          fetchOptions.headers = {
            ...fetchOptions.headers,
            Authorization: `Bearer ${newToken}`,
          }

          return await fetchApi(retriesLeft)
        } else {
          console.log('Unable to refresh token')
          return response
        }
      }

      return response
    } catch (error) {
      console.log(error)
      if (retriesLeft > 0) {
        console.log(`Retrying... attempts left: ${retriesLeft}`)
        return fetchApi(retriesLeft - 1)
      }

      console.log('Maximum retry attempts reached')
      return new Response(
        JSON.stringify({ message: 'Failed after many retries' }),
        { status: 500 }
      )
    }
  }

  return fetchApi(maxRetries)
}
