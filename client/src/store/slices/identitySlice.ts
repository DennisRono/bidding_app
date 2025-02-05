/* eslint-disable @typescript-eslint/no-explicit-any */
import { PayloadAction, createSlice } from '@reduxjs/toolkit'

interface User {
  full_name: string | null | undefined
  user_id: string | null | undefined
  email: string | null | undefined
  role: 'admin' | 'user' | null | undefined
  [key: string]: any
}

interface LoggedState {
  is_logged: boolean
  access_token: string | null | undefined
  refresh_token: string | null | undefined
  user: User
  loginExpiration: number | null
}

const initialState: LoggedState = {
  is_logged: false,
  access_token: null,
  refresh_token: null,
  user: {
    full_name: '',
    phone_number: '',
    user_id: null,
    email: null,
    user_state: null,
    role: null,
  },
  loginExpiration: null,
}

const loggedSlice = createSlice({
  name: 'identity',
  initialState,
  reducers: {
    setIdentity: (
      state,
      action: PayloadAction<{
        is_logged: boolean
        access_token: string
        refresh_token: string
        user: User
      }>
    ) => {
      state.is_logged = action.payload.is_logged
      state.user = action.payload.user
      if (action.payload.is_logged) {
        // Set expiration to 30 days from now
        state.loginExpiration = Date.now() + 30 * 24 * 60 * 60 * 1000
      } else {
        state.loginExpiration = null
      }
    },
    checkLoginExpiration: (state) => {
      if (state.loginExpiration && Date.now() > state.loginExpiration) {
        state.is_logged = false
        state.user = initialState.user
        state.loginExpiration = null
      }
    },
  },
})

export const { setIdentity, checkLoginExpiration } = loggedSlice.actions
export default loggedSlice.reducer
