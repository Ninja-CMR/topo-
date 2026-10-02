export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export const getCurrentUserId = (): string => {
  try {
    const topoUser = localStorage.getItem('topo_user')
    if (topoUser) {
      const parsed = JSON.parse(topoUser)
      if (parsed?.id) return parsed.id
      if (parsed?.user?.id) return parsed.user.id
    }
    const signupData = localStorage.getItem('user_signup_response')
    if (signupData) {
      const parsed = JSON.parse(signupData)
      if (parsed?.user?.id) return parsed.user.id
      if (parsed?.id) return parsed.id
    }
  } catch (e) {
    console.error('Error reading current user ID:', e)
  }
  return ''
}

