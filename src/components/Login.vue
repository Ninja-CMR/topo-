<template>
  <div class="min-h-screen flex flex-col justify-center items-center px-4 py-8 bg-[#FAF8F6]">
    <div class="w-full max-w-md bg-white rounded-[20px] shadow-[0_2px_8px_rgba(28,20,16,0.08)] border border-[#E9E4DF] p-6 sm:p-8">
      
      <!-- Logo -->
      <div class="text-center mb-5 flex flex-col items-center justify-center">
        <img
          src="../assets/logoTopo.png"
          alt="topo. logo"
          class="h-20 w-auto object-contain -mb-1"
        />
        <p class="text-[#6B5F56] text-sm">
          Connecte-toi à ton espace topo.
        </p>
      </div>

      <!-- Alert Notification -->
      <div v-if="errorMessage" class="mb-4 p-3.5 bg-[#FEE2E2] border border-[#FCA5A5] text-[#B91C1C] text-sm rounded-[10px] flex items-center gap-2.5">
        <svg class="w-5 h-5 flex-shrink-0 text-[#B91C1C]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
        <span>{{ errorMessage }}</span>
      </div>

      <div v-if="successMessage" class="mb-4 p-3.5 bg-[#DCFCE7] border border-[#86EFAC] text-[#15803D] text-sm rounded-[10px] flex items-center gap-2.5">
        <svg class="w-5 h-5 flex-shrink-0 text-[#15803D]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>{{ successMessage }}</span>
      </div>

      <!-- Login Form -->
      <form @submit.prevent="handleLogin" class="space-y-4">
        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-semibold text-[#1C1410] mb-1.5">
            Adresse email
          </label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="dev@exemple.cm"
            required
            class="w-full h-12 px-3.5 text-sm bg-white border border-[#D6CEC7] rounded-[10px] text-[#1C1410] placeholder-[#8C8077] focus:outline-none focus:border-[#FD711A] focus:ring-2 focus:ring-[#FD711A]/25 transition-all"
          />
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-semibold text-[#1C1410] mb-1.5">
            Mot de passe
          </label>
          <div class="relative flex items-center">
            <input
              id="password"
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="••••••••"
              required
              class="w-full h-12 pl-3.5 pr-11 text-sm bg-white border border-[#D6CEC7] rounded-[10px] text-[#1C1410] placeholder-[#8C8077] focus:outline-none focus:border-[#FD711A] focus:ring-2 focus:ring-[#FD711A]/25 transition-all"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-3 text-[#6B5F56] hover:text-[#1C1410] focus:outline-none p-1 transition-colors cursor-pointer"
            >
              <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
              <svg v-else class="w-5 h-5 text-[#FD711A]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858-5.908a10.025 10.025 0 013.122-.563c4.478 0 8.268 2.943 9.542 7a10.025 10.025 0 01-4.132 5.411m-4.692-4.692a3 3 0 00-4.243-4.243M3 3l18 18" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="isLoading"
          class="w-full h-12 mt-2 bg-[#FD711A] hover:bg-[#E35D08] active:bg-[#B84A06] text-[#1C1410] font-bold text-sm rounded-[14px] shadow-[0_8px_24px_rgba(253,113,26,0.30)] hover:shadow-lg transition-all duration-200 flex items-center justify-center cursor-pointer disabled:opacity-50"
        >
          <span v-if="!isLoading">Se connecter</span>
          <span v-else>Connexion en cours...</span>
        </button>
      </form>

      <!-- Footer Link -->
      <div class="mt-6 text-center text-xs text-[#6B5F56]">
        Pas encore de compte ?
        <router-link to="/signup" class="text-[#B84A06] font-semibold hover:underline">
          Créer un compte
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { API_BASE_URL } from '../config'

const router = useRouter()
const showPassword = ref(false)

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const form = reactive({
  email: '',
  password: ''
})

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''
  try {
    const res = await fetch(`${API_BASE_URL}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })

    const data = await res.json()
    if (!res.ok) throw new Error(data.detail || 'Identifiants invalides.')
    
    // Clear any previous user state completely
    localStorage.removeItem('user_signup_response')
    localStorage.setItem('topo_token', data.access_token)
    if (data.user) {
      localStorage.setItem('topo_user', JSON.stringify(data.user))
    }
    
    successMessage.value = 'Connexion réussie ! Redirection...'
    setTimeout(() => {
      router.push('/create-topoboard')
    }, 1000)
  } catch (err: any) {
    errorMessage.value = err.message
  } finally {
    isLoading.value = false
  }
}

</script>
