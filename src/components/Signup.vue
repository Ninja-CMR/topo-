<template>
  <div 
    class="min-h-screen flex flex-col justify-center items-center px-4 py-8 bg-[#FAF8F6] transition-all duration-700 ease-in-out"
    :class="{ 'opacity-0 scale-95 pointer-events-none filter blur-xs': isRedirecting }"
  >
    <!-- Card Container -->
    <div class="w-full max-w-md bg-white rounded-[20px] shadow-[0_2px_8px_rgba(28,20,16,0.08)] border border-[#E9E4DF] p-6 sm:p-8 transition-transform duration-500">
      
      <!-- Brand Logo & Header -->
      <div class="text-center mb-5 flex flex-col items-center justify-center">
        <img
          src="../assets/logoTopo.png"
          alt="topo. logo"
          class="h-20 w-auto object-contain -mb-1"
        />
        <p class="text-[#6B5F56] text-sm">
          Crée ton compte développeur et écoute tes utilisateurs.
        </p>
      </div>

      <!-- Alert Notification -->
      <div v-if="errorMessage" class="mb-4 p-3.5 bg-[#FEE2E2] border border-[#FCA5A5] text-[#B91C1C] text-sm rounded-[10px] flex items-center gap-2.5">
        <svg class="w-5 h-5 flex-shrink-0 text-[#B91C1C]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
        <span>{{ errorMessage }}</span>
      </div>

      <div v-if="successMessage" class="mb-4 p-3.5 bg-[#DCFCE7] border border-[#86EFAC] text-[#15803D] text-sm rounded-[10px] flex items-center gap-2.5 animate-pulse">
        <svg class="w-5 h-5 flex-shrink-0 text-[#15803D]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>{{ successMessage }}</span>
      </div>

      <!-- Signup Form -->
      <form @submit.prevent="handleSignUp" class="space-y-4">
        <!-- Field 1: Nom complet -->
        <div>
          <label for="name" class="block text-sm font-semibold text-[#1C1410] mb-1.5">
            Nom complet
          </label>
          <input
            id="name"
            v-model="form.name"
            type="text"
            placeholder="Ex: Jean Dupont"
            required
            :disabled="isLoading || isRedirecting"
            class="w-full h-12 px-3.5 text-sm bg-white border border-[#D6CEC7] rounded-[10px] text-[#1C1410] placeholder-[#8C8077] focus:outline-none focus:border-[#FD711A] focus:ring-2 focus:ring-[#FD711A]/25 transition-all disabled:bg-[#F3EFEA]"
          />
        </div>

        <!-- Field 2: Adresse email -->
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
            :disabled="isLoading || isRedirecting"
            class="w-full h-12 px-3.5 text-sm bg-white border border-[#D6CEC7] rounded-[10px] text-[#1C1410] placeholder-[#8C8077] focus:outline-none focus:border-[#FD711A] focus:ring-2 focus:ring-[#FD711A]/25 transition-all disabled:bg-[#F3EFEA]"
          />
        </div>

        <!-- Field 3: Numéro de téléphone -->
        <div>
          <label for="phone" class="block text-sm font-semibold text-[#1C1410] mb-1.5">
            Numéro de téléphone (WhatsApp)
          </label>
          <div class="relative">
            <input
              id="phone"
              v-model="form.phone"
              type="tel"
              placeholder="+237 6XX XX XX XX"
              required
              :disabled="isLoading || isRedirecting"
              class="w-full h-12 px-3.5 text-sm bg-white border border-[#D6CEC7] rounded-[10px] text-[#1C1410] placeholder-[#8C8077] focus:outline-none focus:border-[#FD711A] focus:ring-2 focus:ring-[#FD711A]/25 transition-all disabled:bg-[#F3EFEA]"
            />
          </div>
          <span class="text-xs text-[#8C8077] mt-1 block">Utile pour recevoir tes alertes et relier WhatsApp.</span>
        </div>

        <!-- Field 4: Mot de passe avec toggle visibilité -->
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
              minlength="6"
              :disabled="isLoading || isRedirecting"
              class="w-full h-12 pl-3.5 pr-11 text-sm bg-white border border-[#D6CEC7] rounded-[10px] text-[#1C1410] placeholder-[#8C8077] focus:outline-none focus:border-[#FD711A] focus:ring-2 focus:ring-[#FD711A]/25 transition-all disabled:bg-[#F3EFEA]"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-3 text-[#6B5F56] hover:text-[#1C1410] focus:outline-none p-1 transition-colors cursor-pointer"
              :title="showPassword ? 'Masquer le mot de passe' : 'Afficher le mot de passe'"
            >
              <!-- Eye Icon -->
              <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
              <!-- Eye Off Icon -->
              <svg v-else class="w-5 h-5 text-[#FD711A]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858-5.908a10.025 10.025 0 013.122-.563c4.478 0 8.268 2.943 9.542 7a10.025 10.025 0 01-4.132 5.411m-4.692-4.692a3 3 0 00-4.243-4.243M3 3l18 18" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="isLoading || isRedirecting"
          class="w-full h-12 mt-2 bg-[#FD711A] hover:bg-[#E35D08] active:bg-[#B84A06] text-[#1C1410] font-bold text-sm rounded-[14px] shadow-[0_8px_24px_rgba(253,113,26,0.30)] hover:shadow-lg transition-all duration-300 flex items-center justify-center cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <span v-if="!isLoading && !isRedirecting">Créer mon compte topo.</span>
          <span v-else class="flex items-center gap-2.5">
            <svg class="animate-spin h-5 w-5 text-[#1C1410]" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span v-if="isLoading">Création du compte...</span>
            <span v-else-if="isRedirecting">Préparation du topoBoard...</span>
          </span>
        </button>
      </form>

      <!-- Footer Link -->
      <div class="mt-6 text-center text-xs text-[#6B5F56]">
        Déjà un compte ?
        <router-link to="/login" class="text-[#B84A06] font-semibold hover:underline">
          Se connecter
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

const form = reactive({
  name: '',
  email: '',
  phone: '',
  password: ''
})

const isLoading = ref(false)
const isRedirecting = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handleSignUp = async () => {
  isLoading.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
      body: JSON.stringify({

        email: form.email,
        password: form.password,
        user_metadata: {
          full_name: form.name,
          phone: form.phone
        }
      })
    })


    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail || 'Erreur lors de l’inscription.')
    }

    // Reset previous storage keys completely
    localStorage.removeItem('user_signup_response')
    localStorage.removeItem('topo_token')
    localStorage.removeItem('topo_user')

    localStorage.setItem('user_signup_response', JSON.stringify(data))
    if (data.session?.access_token) {
      localStorage.setItem('topo_token', data.session.access_token)
    }
    if (data.user) {
      localStorage.setItem('topo_user', JSON.stringify(data.user))
    }

    isLoading.value = false
    isRedirecting.value = true
    successMessage.value = 'Compte créé avec succès ! Préparation de votre espace topoBoard...'

    // Latence de 3 secondes exacte avec transition fluide vers /create-topoboard
    setTimeout(() => {
      router.push('/create-topoboard')
    }, 3000)

  } catch (err: any) {
    isLoading.value = false
    isRedirecting.value = false
    errorMessage.value = err.message || 'Impossible de se connecter au serveur.'
  }
}
</script>
