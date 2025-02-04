export const api = async (
  endpoint: string,
  method: 'GET' | 'POST' | 'DELETE' | 'PATCH' | 'PUT' = 'GET',
  data = {},
  headers = { 'Content-Type': 'application/json' }
) => {
  try {
    const res = await fetch(endpoint, {
      method,
      body: JSON.stringify(data),
      headers: {
        ...headers,
      },
    })
    return res
  } catch (error) {
    return error
  }
}
