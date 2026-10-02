<template>
  <div class="min-h-screen bg-[#FAF8F6] flex flex-col font-sans text-[#1C1410]">
    
    <!-- Top Header Navigation -->
    <header class="w-full bg-white border-b border-[#E9E4DF] px-6 py-3.5 flex items-center justify-between sticky top-0 z-30 shadow-xs">
      <div class="flex items-center gap-3">
        <Logo />
        <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-[#FD711A]/10 text-[#FD711A]">
          Studio de Création
        </span>
      </div>
      <div class="flex items-center gap-4">
        <button
          @click="goHome"
          class="text-xs text-[#8C8077] hover:text-[#1C1410] font-semibold underline cursor-pointer"
        >
          Retour à l'accueil
        </button>
      </div>
    </header>

    <!-- Main Workspace (Layout 2 Colonnes) -->
    <div class="flex-1 flex flex-col lg:flex-row overflow-hidden">
      
      <!-- LEFT SIDEBAR: COLLAPSIBLE ACCORDION SECTIONS -->
      <aside class="w-full lg:w-[460px] bg-white border-r border-[#E9E4DF] p-6 overflow-y-auto max-h-[calc(100vh-61px)] flex flex-col justify-between shrink-0">
        <div class="space-y-4">
          
          <div class="mb-4">
            <h2 class="text-xl font-extrabold text-[#1C1410] tracking-tight">Configuration topoBoard</h2>
            <p class="text-xs text-[#6B5F56] mt-1">Clique sur chaque section ci-dessous pour la déplier et la personnaliser.</p>
          </div>

          <!-- SECTION 1: ACCORDION INFORMATIONS SOLUTION -->
          <div class="border border-[#E9E4DF] rounded-[14px] overflow-hidden transition-all">
            <button
              @click="toggleSection(1)"
              class="w-full p-4 bg-[#FAF8F6] hover:bg-[#F3EFEA] flex items-center justify-between font-bold text-xs text-[#1C1410] transition-colors cursor-pointer"
            >
              <span class="flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-[#FD711A]/15 text-[#FD711A] flex items-center justify-center text-[10px]">1</span>
                Informations de la solution
              </span>
              <svg
                class="w-4 h-4 transition-transform duration-200"
                :class="{ 'rotate-180': openSection === 1 }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <div v-show="openSection === 1" class="p-4 bg-white space-y-3 border-t border-[#E9E4DF]">
              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Nom de ton produit / app</label>
                <input
                  v-model="config.productName"
                  type="text"
                  placeholder="Ex: PaySaaS App"
                  class="w-full h-10 px-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all"
                />
              </div>

              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Lien / URL de la solution</label>
                <input
                  v-model="config.productUrl"
                  type="url"
                  placeholder="https://paysaas.cm"
                  class="w-full h-10 px-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all"
                />
              </div>

              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Logo URL (Optionnel)</label>
                <input
                  v-model="config.logoUrl"
                  type="url"
                  placeholder="https://paysaas.cm/logo.png"
                  class="w-full h-10 px-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all"
                />
              </div>
            </div>
          </div>

          <!-- SECTION 2: ACCORDION HOOK & DESCRIPTION -->
          <div class="border border-[#E9E4DF] rounded-[14px] overflow-hidden transition-all">
            <button
              @click="toggleSection(2)"
              class="w-full p-4 bg-[#FAF8F6] hover:bg-[#F3EFEA] flex items-center justify-between font-bold text-xs text-[#1C1410] transition-colors cursor-pointer"
            >
              <span class="flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-[#FD711A]/15 text-[#FD711A] flex items-center justify-center text-[10px]">2</span>
                Message d'accroche & Description
              </span>
              <svg
                class="w-4 h-4 transition-transform duration-200"
                :class="{ 'rotate-180': openSection === 2 }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <div v-show="openSection === 2" class="p-4 bg-white space-y-3 border-t border-[#E9E4DF]">
              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Message d'accroche (Titre)</label>
                <input
                  v-model="config.hookMessage"
                  type="text"
                  placeholder="Ex: Donne-nous ton avis en 30 sec !"
                  class="w-full h-10 px-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all"
                />
              </div>

              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Description courte</label>
                <textarea
                  v-model="config.description"
                  rows="2"
                  placeholder="Ex: Ton retour nous permet de corriger les bugs..."
                  class="w-full p-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all resize-none"
                ></textarea>
              </div>
            </div>
          </div>

          <!-- SECTION 3: ACCORDION FORMULAIRE D'AVIS -->
          <div class="border border-[#E9E4DF] rounded-[14px] overflow-hidden transition-all">
            <button
              @click="toggleSection(3)"
              class="w-full p-4 bg-[#FAF8F6] hover:bg-[#F3EFEA] flex items-center justify-between font-bold text-xs text-[#1C1410] transition-colors cursor-pointer"
            >
              <span class="flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-[#FD711A]/15 text-[#FD711A] flex items-center justify-center text-[10px]">3</span>
                Questions du formulaire d'avis
              </span>
              <svg
                class="w-4 h-4 transition-transform duration-200"
                :class="{ 'rotate-180': openSection === 3 }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <div v-show="openSection === 3" class="p-4 bg-white space-y-3 border-t border-[#E9E4DF]">
              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Question principale</label>
                <input
                  v-model="config.feedbackQuestion"
                  type="text"
                  placeholder="Ex: Qu'as-tu pensé de ta visite ?"
                  class="w-full h-10 px-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all"
                />
              </div>

              <div class="flex items-center gap-4 text-xs font-medium text-[#1C1410]">
                <label class="flex items-center gap-1.5 cursor-pointer">
                  <input type="checkbox" v-model="config.allowRating" class="accent-[#FD711A]" />
                  Note par étoiles (1-5)
                </label>
                <label class="flex items-center gap-1.5 cursor-pointer">
                  <input type="checkbox" v-model="config.allowWhatsAppContact" class="accent-[#FD711A]" />
                  Champ WhatsApp
                </label>
              </div>
            </div>
          </div>

          <!-- SECTION 4: ACCORDION STYLE & CTA -->
          <div class="border border-[#E9E4DF] rounded-[14px] overflow-hidden transition-all">
            <button
              @click="toggleSection(4)"
              class="w-full p-4 bg-[#FAF8F6] hover:bg-[#F3EFEA] flex items-center justify-between font-bold text-xs text-[#1C1410] transition-colors cursor-pointer"
            >
              <span class="flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-[#FD711A]/15 text-[#FD711A] flex items-center justify-center text-[10px]">4</span>
                Style, Couleur & Bouton CTA
              </span>
              <svg
                class="w-4 h-4 transition-transform duration-200"
                :class="{ 'rotate-180': openSection === 4 }"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <div v-show="openSection === 4" class="p-4 bg-white space-y-3 border-t border-[#E9E4DF]">
              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Texte du bouton CTA</label>
                <input
                  v-model="config.ctaText"
                  type="text"
                  placeholder="Ex: Envoyer mon retour"
                  class="w-full h-10 px-3 text-xs bg-white border border-[#D6CEC7] rounded-[8px] focus:outline-none focus:border-[#FD711A] transition-all"
                />
              </div>

              <div>
                <label class="block text-xs font-semibold text-[#1C1410] mb-1">Couleur principale (Brand Color)</label>
                <div class="flex items-center gap-3">
                  <input
                    v-model="config.brandColor"
                    type="color"
                    class="w-10 h-10 rounded-[8px] border border-[#D6CEC7] cursor-pointer"
                  />
                  <span class="text-xs font-mono font-bold text-[#6B5F56] uppercase">{{ config.brandColor }}</span>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- SUBMIT CREATE BUTTON -->
        <div class="pt-6 mt-6 border-t border-[#E9E4DF]">
          <button
            @click="handleCreateTopoBoard"
            :disabled="isCreating"
            class="w-full h-12 bg-[#FD711A] hover:bg-[#E35D08] active:bg-[#B84A06] text-[#1C1410] font-extrabold text-sm rounded-[14px] shadow-[0_8px_24px_rgba(253,113,26,0.30)] hover:shadow-lg transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50"
          >
            <svg v-if="!isCreating" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span v-if="!isCreating">Créer mon topoBoard</span>
            <span v-else>Création du topoBoard...</span>
          </button>
        </div>
      </aside>

      <!-- RIGHT LIVE PREVIEW -->
      <main class="flex-1 bg-[#FAF8F6] p-6 lg:p-10 flex flex-col items-center justify-center relative overflow-hidden">
        
        <div class="w-full max-w-2xl bg-white border border-[#E9E4DF] rounded-[24px] shadow-sm p-8 relative min-h-[500px] flex flex-col justify-between">
          
          <div class="w-full flex items-center justify-between pb-6 border-b border-[#F3EFEA]">
            <div class="flex items-center gap-3">
              <img
                :src="config.logoUrl || 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=100'"
                alt="Logo Solution"
                class="w-8 h-8 rounded-lg object-cover bg-[#FAF8F6] border border-[#E9E4DF]"
              />
              <span class="font-extrabold text-base text-[#1C1410]">
                {{ config.productName || 'Nom de la Solution' }}
              </span>
            </div>
            
            <a
              :href="formattedProductUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="text-xs font-mono font-bold text-[#FD711A] bg-[#FD711A]/10 hover:bg-[#FD711A]/20 px-3 py-1.5 rounded-full border border-[#FD711A]/30 flex items-center gap-1.5 transition-all group"
            >
              <span>{{ config.productUrl || 'https://paysaas.cm' }}</span>
              <svg class="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
            </a>
          </div>

          <div class="my-auto text-center py-8">
            <h2 class="text-2xl font-black text-[#1C1410] mb-2">
              {{ config.hookMessage || 'Message d\'accroche pour vos visiteurs' }}
            </h2>
            <p class="text-xs text-[#6B5F56] max-w-md mx-auto leading-relaxed">
              {{ config.description || 'Description courte de votre solution pour encourager les retours d\'expérience.' }}
            </p>
          </div>

          <div
            class="p-5 rounded-[20px] shadow-lg border border-[#E9E4DF] bg-white max-w-sm w-full transition-all duration-300 mx-auto"
            :style="{ borderColor: config.brandColor + '50' }"
          >
            <div class="flex items-center gap-2 mb-3">
              <div class="w-3 h-3 rounded-full" :style="{ backgroundColor: config.brandColor }"></div>
              <span class="text-xs font-bold text-[#1C1410]">{{ config.feedbackQuestion }}</span>
            </div>

            <div v-if="config.allowRating" class="flex gap-1.5 justify-center mb-3 text-amber-400">
              <span v-for="i in 5" :key="i" class="text-lg cursor-pointer hover:scale-125 transition-transform">★</span>
            </div>

            <textarea
              placeholder="Écris ton retour ici..."
              rows="2"
              class="w-full text-xs p-2.5 border border-[#E9E4DF] rounded-[10px] resize-none focus:outline-none mb-2"
            ></textarea>

            <input
              v-if="config.allowWhatsAppContact"
              type="tel"
              placeholder="Ton numéro WhatsApp (+237...)"
              class="w-full text-xs h-9 px-3 border border-[#E9E4DF] rounded-[10px] focus:outline-none mb-3"
            />

            <button
              class="w-full h-10 text-white font-bold text-xs rounded-[10px] shadow-xs cursor-pointer"
              :style="{ backgroundColor: config.brandColor }"
            >
              {{ config.ctaText || 'Envoyer l\'avis' }}
            </button>
          </div>

        </div>

      </main>

    </div>

    <!-- MODAL DE CONFIRMATION AVEC REDIRECTION VERS L'ACCUEIL UNIFIÉ -->
    <div
      v-if="createdTopoBoardUrl"
      class="fixed inset-0 bg-[#1C1410]/70 backdrop-blur-xs flex items-center justify-center p-4 z-50 animate-fade-in"
    >
      <div class="bg-white rounded-[24px] max-w-md w-full p-6 sm:p-8 shadow-2xl border border-[#E9E4DF] text-center space-y-6">
        
        <div class="w-16 h-16 rounded-full bg-[#DCFCE7] border border-[#86EFAC] text-[#15803D] flex items-center justify-center mx-auto shadow-xs">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
          </svg>
        </div>

        <div>
          <h3 class="text-2xl font-black text-[#1C1410]">topoBoard créé avec succès !</h3>
          <p class="text-xs text-[#6B5F56] mt-1.5">Ton widget est sauvegardé dans Supabase et disponible sur ton accueil.</p>
        </div>

        <div class="bg-[#FAF8F6] p-3 rounded-[12px] border border-[#E9E4DF] flex items-center justify-between gap-2">
          <input
            type="text"
            readonly
            :value="createdTopoBoardUrl"
            class="text-xs text-[#1C1410] font-mono bg-transparent w-full focus:outline-none"
          />
          <button
            @click="copyLink"
            class="px-3 py-1.5 bg-white border border-[#D6CEC7] rounded-[8px] text-xs font-bold text-[#1C1410] hover:bg-[#FAF8F6] cursor-pointer shrink-0 flex items-center gap-1.5"
          >
            <svg v-if="!copied" class="w-4 h-4 text-[#6B5F56]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
            <svg v-else class="w-4 h-4 text-[#15803D]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span>{{ copied ? 'Copié' : 'Copier' }}</span>
          </button>
        </div>

        <div class="space-y-3">
          <a
            :href="whatsappShareUrl"
            target="_blank"
            class="w-full h-12 bg-[#25D366] hover:bg-[#20bd5a] text-white font-extrabold text-xs rounded-[14px] shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all"
          >
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
              <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-0.999 3.648 3.742-.981z"/>
            </svg>
            Partager sur WhatsApp
          </a>

          <button
            @click="goHome"
            class="w-full h-11 bg-[#FAF8F6] hover:bg-[#F3EFEA] border border-[#E9E4DF] text-[#1C1410] font-bold text-xs rounded-[14px] flex items-center justify-center gap-2 cursor-pointer transition-all"
          >
            Retourner à l'accueil &rarr;
          </button>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import Logo from './Logo.vue'
import { API_BASE_URL, getCurrentUserId } from '../config'

const router = useRouter()
const isCreating = ref(false)
const createdTopoBoardUrl = ref('')
const copied = ref(false)
const openSection = ref<number | null>(1)

const config = reactive({
  productName: 'PaySaaS App',
  productUrl: 'https://paysaas.cm',
  logoUrl: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=100',
  hookMessage: 'Donne-nous ton avis en 30 secondes !',
  description: 'Ton retour nous permet de corriger les bugs et d\'ajouter les fonctionnalités que tu demandes.',
  feedbackQuestion: 'Qu\'as-tu pensé de ta visite sur PaySaaS ?',
  allowRating: true,
  allowWhatsAppContact: true,
  ctaText: 'Envoyer mon retour',
  brandColor: '#FD711A'
})

const toggleSection = (sectionIndex: number) => {
  openSection.value = openSection.value === sectionIndex ? null : sectionIndex
}

const formattedProductUrl = computed(() => {
  const url = config.productUrl || 'https://paysaas.cm'
  return url.startsWith('http://') || url.startsWith('https://') ? url : `https://${url}`
})

const handleCreateTopoBoard = async () => {
  isCreating.value = true
  try {
    const userId = getCurrentUserId()

    const payload = {
      product_name: config.productName,
      product_url: config.productUrl,
      logo_url: config.logoUrl,
      hook_message: config.hookMessage,
      description: config.description,
      feedback_question: config.feedbackQuestion,
      allow_rating: config.allowRating,
      allow_whatsapp_contact: config.allowWhatsAppContact,
      cta_text: config.ctaText,
      brand_color: config.brandColor
    }

    const apiUrl = userId 
      ? `${API_BASE_URL}/api/topoboards/?user_id=${userId}`
      : `${API_BASE_URL}/api/topoboards/`


    const res = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
      body: JSON.stringify(payload)
    })



    const baseUrl = `${window.location.origin}/board`

    if (res.ok) {
      const savedBoard = await res.json()
      createdTopoBoardUrl.value = `${baseUrl}/${savedBoard.id}`
    } else {
      const errData = await res.json().catch(() => ({}))
      console.error('Erreur API création topoBoard:', errData)
      alert(`Erreur lors de la création du topoBoard: ${errData.detail || 'Erreur serveur'}`)
    }
  } catch (err: any) {
    console.error('Erreur de connexion API:', err)
    alert('Impossible de contacter le serveur backend. Vérifiez votre connexion.')
  } finally {
    isCreating.value = false
  }
}



const copyLink = () => {
  navigator.clipboard.writeText(createdTopoBoardUrl.value)
  copied.value = true
  setTimeout(() => { copied.value = false }, 2000)
}

const whatsappShareUrl = computed(() => {
  const message = `Salut ! Donne ton avis sur ${config.productName} via notre topoBoard : ${createdTopoBoardUrl.value}`
  return `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`
})

const goHome = () => {
  router.push('/create-topoboard')
}
</script>
