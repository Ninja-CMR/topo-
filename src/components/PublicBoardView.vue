<template>
  <div class="min-h-screen bg-[#FAF8F6] flex flex-col items-center justify-center p-4 sm:p-6 font-sans text-[#1C1410] select-none relative overflow-hidden">
    
    <!-- Background subtle gradient glow -->
    <div
      class="absolute w-[500px] h-[500px] rounded-full blur-3xl opacity-20 pointer-events-none -z-10 transition-colors duration-500"
      :style="{ backgroundColor: board?.brand_color || '#FD711A' }"
    ></div>

    <!-- State 1: Loading -->
    <div v-if="isLoading" class="text-center space-y-3">
      <div class="w-8 h-8 border-3 border-t-transparent border-[#FD711A] rounded-full animate-spin mx-auto"></div>
      <p class="text-xs text-[#6B5F56] font-medium">Chargement du topoBoard...</p>
    </div>

    <!-- State 2: Error / Not Found -->
    <div v-else-if="error" class="bg-white p-8 rounded-[24px] border border-[#E9E4DF] shadow-lg text-center max-w-md w-full space-y-4">
      <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center mx-auto">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
      </div>
      <h2 class="text-lg font-extrabold text-[#1C1410]">topoBoard introuvable</h2>
      <p class="text-xs text-[#6B5F56]">{{ error }}</p>
    </div>

    <!-- State 3: Public Feedback Form -->
    <div v-else-if="!submitted" class="w-full max-w-lg bg-white border border-[#E9E4DF] rounded-[24px] shadow-xl p-6 sm:p-8 space-y-6 relative">
      
      <!-- Solution Header -->
      <div class="flex items-center justify-between pb-5 border-b border-[#F3EFEA]">
        <div class="flex items-center gap-3">
          <img
            :src="board?.logo_url || 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=100'"
            alt="Logo Solution"
            class="w-10 h-10 rounded-xl object-cover border border-[#E9E4DF] bg-[#FAF8F6]"
          />
          <div>
            <h1 class="font-black text-base text-[#1C1410]">{{ board?.product_name }}</h1>
            <a
              v-if="board?.product_url"
              :href="formattedProductUrl"
              target="_blank"
              class="text-[11px] text-[#FD711A] hover:underline font-mono truncate max-w-[180px] block"
            >
              {{ board?.product_url }}
            </a>
          </div>
        </div>

        <span class="text-[10px] font-bold px-2.5 py-1 rounded-full bg-[#FAF8F6] border border-[#E9E4DF] text-[#6B5F56]">
          Avis Testeur
        </span>
      </div>

      <!-- Hook & Description -->
      <div class="text-center space-y-2">
        <h2 class="text-xl font-black text-[#1C1410] leading-tight">
          {{ board?.hook_message || 'Donne-nous ton avis !' }}
        </h2>
        <p v-if="board?.description" class="text-xs text-[#6B5F56] leading-relaxed">
          {{ board?.description }}
        </p>
      </div>

      <!-- Form Box -->
      <form @submit.prevent="submitResponse" class="space-y-4">
        
        <div>
          <label class="block text-xs font-bold text-[#1C1410] mb-2">
            {{ board?.feedback_question || "Qu'as-tu pensé de ta visite ?" }}
          </label>
          
          <!-- Rating Stars -->
          <div v-if="board?.allow_rating !== false" class="flex items-center justify-center gap-2 py-2">
            <button
              v-for="star in 5"
              :key="star"
              type="button"
              @click="rating = star"
              class="text-2xl transition-transform hover:scale-125 focus:outline-none cursor-pointer"
              :class="star <= rating ? 'text-amber-400' : 'text-gray-200'"
            >
              ★
            </button>
          </div>
        </div>

        <!-- Feedback Textarea -->
        <div>
          <label class="block text-xs font-semibold text-[#6B5F56] mb-1">Tes remarques ou suggestions</label>
          <textarea
            v-model="comment"
            required
            rows="4"
            placeholder="Dis-nous ce qui t'a plu ou les difficultés rencontrées..."
            class="w-full text-xs p-3.5 border border-[#D6CEC7] rounded-[12px] focus:outline-none focus:border-[#FD711A] transition-all resize-none bg-white"
          ></textarea>
        </div>

        <!-- Optional WhatsApp -->
        <div v-if="board?.allow_whatsapp_contact !== false">
          <label class="block text-xs font-semibold text-[#6B5F56] mb-1">Ton WhatsApp (Optionnel pour qu'on te réponde)</label>
          <input
            v-model="whatsapp"
            type="tel"
            placeholder="Ex: +237 6xx xxx xxx"
            class="w-full text-xs h-10 px-3.5 border border-[#D6CEC7] rounded-[12px] focus:outline-none focus:border-[#FD711A] transition-all bg-white"
          />
        </div>

        <!-- Submit CTA Button -->
        <button
          type="submit"
          :disabled="isSubmitting"
          class="w-full h-12 text-white font-extrabold text-sm rounded-[14px] shadow-md hover:shadow-lg transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50"
          :style="{ backgroundColor: board?.brand_color || '#FD711A' }"
        >
          <span v-if="!isSubmitting">{{ board?.cta_text || 'Envoyer mon retour' }}</span>
          <span v-else class="flex items-center gap-2">
            <svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
            </svg>
            Envoi en cours...
          </span>
        </button>
      </form>

      <!-- Footer powered by -->
      <div class="text-center pt-2 border-t border-[#F3EFEA]">
        <span class="text-[10px] text-[#8C8077]">Propulsé par <strong class="text-[#1C1410]">Topo.cm</strong></span>
      </div>

    </div>

    <!-- State 4: Thank You / Success Screen -->
    <div v-else class="w-full max-w-md bg-white border border-[#E9E4DF] rounded-[24px] shadow-xl p-8 text-center space-y-6">
      
      <div class="w-16 h-16 rounded-full bg-[#DCFCE7] border border-[#86EFAC] text-[#15803D] flex items-center justify-center mx-auto shadow-xs">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
        </svg>
      </div>

      <div class="space-y-2">
        <h2 class="text-2xl font-black text-[#1C1410]">Merci pour ton retour !</h2>
        <p class="text-xs text-[#6B5F56] leading-relaxed">
          Ton avis a été bien transmis à l'équipe de <strong>{{ board?.product_name }}</strong>.
        </p>
      </div>

      <div class="space-y-3 pt-2">
        <a
          v-if="board?.product_url"
          :href="formattedProductUrl"
          target="_blank"
          class="w-full h-11 bg-[#FAF8F6] hover:bg-[#F3EFEA] border border-[#E9E4DF] text-[#1C1410] font-bold text-xs rounded-[12px] flex items-center justify-center gap-2 cursor-pointer transition-all"
        >
          <span>Retourner sur {{ board?.product_name }}</span>
          &rarr;
        </a>

        <button
          @click="submitted = false"
          class="text-xs text-[#8C8077] hover:text-[#1C1410] font-semibold underline cursor-pointer"
        >
          Envoyer un autre avis
        </button>
      </div>

    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { API_BASE_URL } from '../config'

const route = useRoute()
const boardId = route.params.id as string

const board = ref<any>(null)
const isLoading = ref(true)
const error = ref('')

const rating = ref(5)
const comment = ref('')
const whatsapp = ref('')
const isSubmitting = ref(false)
const submitted = ref(false)

const formattedProductUrl = computed(() => {
  if (!board.value?.product_url) return '#'
  const url = board.value.product_url
  return url.startsWith('http://') || url.startsWith('https://') ? url : `https://${url}`
})

const fetchBoardDetails = async () => {
  isLoading.value = true
  error.value = ''
  try {
    const res = await fetch(`${API_BASE_URL}/api/topoboards/${boardId}`, {
      headers: {
        'ngrok-skip-browser-warning': 'true'
      }
    })
    if (res.ok) {
      board.value = await res.json()
    } else {
      error.value = "Ce topoBoard n'existe pas ou a été supprimé."
    }
  } catch (err) {
    console.error('Erreur chargement topoBoard:', err)
    error.value = "Impossible de se connecter au serveur."
  } finally {
    isLoading.value = false
  }
}

const submitResponse = async () => {
  if (!comment.value.trim()) return
  isSubmitting.value = true
  try {
    const payload = {
      rating: rating.value,
      comment: comment.value,
      whatsapp: whatsapp.value || null
    }

    const res = await fetch(`${API_BASE_URL}/api/topoboards/${boardId}/responses`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
      body: JSON.stringify(payload)
    })



    if (res.ok) {
      submitted.value = true
    } else {
      alert("Une erreur est survenue lors de l'envoi de votre avis.")
    }
  } catch (err) {
    console.error('Erreur envoi avis:', err)
    alert("Impossible de contacter le serveur.")
  } finally {
    isSubmitting.value = false
  }
}

onMounted(() => {
  fetchBoardDetails()
})
</script>
