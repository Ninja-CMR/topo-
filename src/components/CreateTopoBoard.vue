<template>
  <div class="min-h-screen bg-[#FAF8F6] flex flex-col justify-between p-6 md:p-12 relative overflow-hidden select-none font-sans text-[#1C1410]">
    
    <!-- Background Animated Pop & Respawn User Avatar Bubbles -->
    <div class="absolute inset-0 pointer-events-none z-0 overflow-hidden">
      <div
        v-for="bubble in bubbles"
        :key="bubble.id"
        class="absolute flex items-center gap-2.5 bg-white/90 backdrop-blur-md px-3.5 py-2 rounded-full border border-[#E9E4DF] shadow-[0_6px_20px_rgba(28,20,16,0.08)] bubble-pop"
        :style="{
          left: bubble.left + '%',
          top: bubble.top + '%',
          animationDuration: bubble.duration + 's',
          animationDelay: bubble.delay + 's'
        }"
      >
        <img :src="bubble.avatar" :alt="bubble.name" class="w-8 h-8 rounded-full object-cover border border-[#FD711A]/40 flex-shrink-0" />
        <div class="flex flex-col text-left">
          <span class="text-[11px] font-bold text-[#1C1410] leading-none mb-0.5">{{ bubble.name }}</span>
          <span class="text-[10px] text-[#6B5F56] font-medium leading-none">{{ bubble.comment }}</span>
        </div>
      </div>
    </div>

    <!-- Top Header Navigation -->
    <header class="w-full max-w-5xl mx-auto flex items-center justify-between pb-8 relative z-10">
      <div class="flex items-center gap-3">
        <Logo />
      </div>
      <div class="flex items-center gap-4">
        <span v-if="userName" class="text-sm font-medium text-[#6B5F56]">
          Bienvenue, <strong class="text-[#1C1410]">{{ userName }}</strong>
        </span>
        <button
          @click="handleLogout"
          class="text-xs text-[#8C8077] hover:text-[#1C1410] font-semibold underline cursor-pointer"
        >
          Déconnexion
        </button>
      </div>
    </header>

    <!-- MAIN VIEW 1: HERO & CONDITIONALLY RENDERED BOARDS LIST (HOME) -->
    <div v-if="!selectedBoard" class="w-full max-w-5xl mx-auto flex-1 flex flex-col justify-center relative z-10 my-4 space-y-10">
      
      <!-- Main Content Hero Section -->
      <section class="text-center flex flex-col items-center">
        <h1 class="text-3xl sm:text-5xl font-extrabold text-[#1C1410] tracking-tight mb-4 max-w-2xl leading-tight">
          Prêt à collecter les retours de tes utilisateurs ?
        </h1>
        <p class="text-[#6B5F56] text-base sm:text-lg mb-8 max-w-xl">
          Crée ton premier <strong class="text-[#1C1410]">topoBoard</strong> en quelques secondes pour centraliser tes bugs, suggestions et intégrer WhatsApp.
        </p>

        <!-- Main Action CTA Button -->
        <button
          @click="goToStudio"
          class="w-full sm:w-auto px-8 py-4 bg-[#FD711A] hover:bg-[#E35D08] active:bg-[#B84A06] text-[#1C1410] font-extrabold text-lg rounded-[16px] shadow-[0_10px_30px_rgba(253,113,26,0.35)] hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200 flex items-center justify-center gap-3 cursor-pointer group"
        >
          <svg class="w-6 h-6 transition-transform duration-200 group-hover:rotate-90" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4" />
          </svg>
          <span>Créer un topoBoard</span>
        </button>
      </section>

      <!-- SECTION MES TOPOBOARDS (S'AICHE UNIQUEMENT SI AU MOINS 1 TOPOBOARD EST CRÉÉ) -->
      <section v-if="userBoards.length > 0" class="bg-white/90 backdrop-blur-md border border-[#E9E4DF] rounded-[24px] p-6 sm:p-8 shadow-xs space-y-6">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-xl font-extrabold text-[#1C1410] flex items-center gap-2">
              <svg class="w-5 h-5 text-[#FD711A]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
              Mes topoBoards actifs
            </h2>
            <p class="text-xs text-[#6B5F56] mt-0.5">Clique sur un topoBoard pour consulter tous les avis reçus.</p>
          </div>
          <span class="text-xs font-bold bg-[#FAF8F6] border border-[#E9E4DF] px-3 py-1.5 rounded-full text-[#6B5F56]">
            Total: {{ userBoards.length }}
          </span>
        </div>

        <!-- Boards Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          <div
            v-for="board in userBoards"
            :key="board.id"
            @click="openBoardDetails(board)"
            class="bg-white border border-[#E9E4DF] hover:border-[#FD711A] rounded-[18px] p-5 shadow-xs hover:shadow-md transition-all cursor-pointer flex flex-col justify-between group"
          >
            <div>
              <div class="flex items-center justify-between mb-3">
                <div class="flex items-center gap-2">
                  <div class="w-8 h-8 rounded-lg bg-[#FAF8F6] border border-[#E9E4DF] flex items-center justify-center font-bold text-sm text-[#FD711A]">
                    {{ board.product_name ? board.product_name.charAt(0) : 'T' }}
                  </div>
                  <div>
                    <h3 class="font-extrabold text-sm text-[#1C1410] group-hover:text-[#FD711A] transition-colors">
                      {{ board.product_name }}
                    </h3>
                    <span class="text-[11px] text-[#8C8077] font-mono block truncate max-w-[150px]">
                      {{ board.product_url }}
                    </span>
                  </div>
                </div>
                <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#15803D]/10 text-[#15803D]">Actif</span>
              </div>
              <p class="text-xs text-[#6B5F56] line-clamp-2 mb-3 leading-relaxed">
                {{ board.hook_message }}
              </p>
            </div>

            <div class="pt-3 border-t border-[#F3EFEA] flex items-center justify-between text-xs">
              <span class="text-[#6B5F56] font-semibold flex items-center gap-1.5">
                <svg class="w-4 h-4 text-[#FD711A]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
                <strong class="text-[#1C1410]">{{ board.responses ? board.responses.length : 0 }}</strong> avis
              </span>
              <span class="text-[#FD711A] font-bold group-hover:translate-x-1 transition-transform flex items-center gap-1">
                Voir avis &rarr;
              </span>
            </div>
          </div>
        </div>
      </section>

      <!-- Templates Section -->
      <section class="w-full max-w-5xl mx-auto border-t border-[#E9E4DF] pt-10 mt-6 relative z-10">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h2 class="text-xl font-bold text-[#1C1410]">Modèles & Templates</h2>
            <p class="text-xs text-[#6B5F56] mt-0.5">Choisis un modèle préconfiguré pour démarrer encore plus vite.</p>
          </div>
          <span class="text-xs bg-[#E9E4DF] text-[#6B5F56] px-2.5 py-1 rounded-full font-semibold">
            Module bientôt disponible
          </span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-5">
          <div
            v-for="template in templates"
            :key="template.id"
            class="bg-white/80 backdrop-blur-sm border border-[#E9E4DF] rounded-[16px] p-5 opacity-70 hover:opacity-90 transition-all cursor-not-allowed relative group"
          >
            <div class="w-10 h-10 rounded-[12px] bg-[#FAF8F6] border border-[#E9E4DF] flex items-center justify-center mb-4 text-[#FD711A]">
              <component :is="template.icon" />
            </div>
            <h3 class="font-bold text-[#1C1410] text-sm mb-1">{{ template.title }}</h3>
            <p class="text-xs text-[#6B5F56] leading-relaxed mb-3">{{ template.description }}</p>
            <span class="inline-block text-[11px] font-semibold text-[#8C8077] bg-[#F3EFEA] px-2 py-0.5 rounded-md">
              {{ template.tag }}
            </span>
          </div>
        </div>
      </section>

    </div>

    <!-- MAIN VIEW 2: RESPONSES DETAILS -->
    <div v-else class="w-full max-w-5xl mx-auto flex-1 flex flex-col justify-center relative z-10 my-4 space-y-6">
      
      <button
        @click="selectedBoard = null"
        class="text-xs font-bold text-[#6B5F56] hover:text-[#1C1410] flex items-center gap-2 cursor-pointer w-fit"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        <span>Retour à l'accueil</span>
      </button>

      <!-- Header topoBoard -->
      <div class="bg-white p-6 rounded-[20px] border border-[#E9E4DF] shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-3 mb-1">
            <h2 class="text-2xl font-black text-[#1C1410]">{{ selectedBoard.product_name }}</h2>
            <span class="text-xs font-mono bg-[#FAF8F6] px-2.5 py-1 rounded-md border border-[#E9E4DF] text-[#6B5F56] truncate max-w-[150px]">
              {{ selectedBoard.id }}
            </span>
          </div>
          <p class="text-xs text-[#6B5F56]">Question posée : <strong>{{ selectedBoard.feedback_question }}</strong></p>
        </div>

        <a
          :href="'https://api.whatsapp.com/send?text=' + encodeURIComponent('Donne ton avis sur ' + selectedBoard.product_name + ' : ' + getBoardShareUrl(selectedBoard.id))"
          target="_blank"
          class="px-4 py-2.5 bg-[#25D366] hover:bg-[#20bd5a] text-white font-extrabold text-xs rounded-[12px] shadow-sm flex items-center gap-2 transition-all cursor-pointer w-fit"
        >
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-0.999 3.648 3.742-.981z"/>
          </svg>
          Partager sur WhatsApp
        </a>
      </div>

      <!-- Métriques Google Forms -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] text-center">
          <span class="text-xs text-[#6B5F56] font-semibold">Total Avis Reçus</span>
          <div class="text-3xl font-black text-[#1C1410] mt-1">{{ selectedBoard.responses ? selectedBoard.responses.length : 0 }}</div>
        </div>
        <div class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] text-center">
          <span class="text-xs text-[#6B5F56] font-semibold">Note Moyenne</span>
          <div class="text-3xl font-black text-[#FD711A] mt-1">
            {{ averageRating(selectedBoard.responses || []) }} <span class="text-sm font-normal text-[#6B5F56]">/ 5 ★</span>
          </div>
        </div>
        <div class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] text-center">
          <span class="text-xs text-[#6B5F56] font-semibold">Contacts WhatsApp</span>
          <div class="text-3xl font-black text-[#15803D] mt-1">
            {{ whatsappCount(selectedBoard.responses || []) }}
          </div>
        </div>
      </div>

      <!-- Feed des avis -->
      <div class="space-y-4">
        <h3 class="text-xs font-extrabold uppercase tracking-wider text-[#6B5F56] px-1">
          Avis des utilisateurs ({{ selectedBoard.responses ? selectedBoard.responses.length : 0 }})
        </h3>

        <div v-if="!selectedBoard.responses || selectedBoard.responses.length === 0" class="bg-white p-6 rounded-[16px] border border-[#E9E4DF] text-center text-xs text-[#6B5F56]">
          Aucun avis reçu pour l'instant. Partage ton lien pour commencer !
        </div>

        <div
          v-else
          v-for="resp in selectedBoard.responses"
          :key="resp.id"
          class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] shadow-xs space-y-2.5 transition-all duration-300"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="text-amber-400 font-bold text-sm">
                {{ '★'.repeat(resp.rating || 5) }}<span class="text-gray-300">{{ '★'.repeat(5 - (resp.rating || 5)) }}</span>
              </span>
              <span class="text-xs text-[#8C8077] font-medium">• {{ resp.created_at ? new Date(resp.created_at).toLocaleDateString() : 'Récent' }}</span>
            </div>
            <span v-if="resp.whatsapp" class="text-xs bg-[#25D366]/10 text-[#15803D] px-2.5 py-1 rounded-full font-mono flex items-center gap-1.5 font-bold">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
                <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-0.999 3.648 3.742-.981z"/>
              </svg>
              {{ resp.whatsapp }}
            </span>
          </div>
          <p class="text-xs text-[#1C1410] leading-relaxed font-medium bg-[#FAF8F6] p-3 rounded-[10px] border border-[#E9E4DF]">
            "{{ resp.comment }}"
          </p>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, h } from 'vue'
import { useRouter } from 'vue-router'
import Logo from './Logo.vue'

const router = useRouter()
const userName = ref('')
const selectedBoard = ref<any>(null)
const userBoards = ref<any[]>([])
let timer: any = null

const bubbles = [
  { id: 1, name: 'Sonia K.', comment: 'Excellente idée cette feature !', avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150', left: 5, top: 12, duration: 6, delay: 0 },
  { id: 2, name: 'Marc A.', comment: 'Bug signalé sur iOS', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150', left: 78, top: 15, duration: 7, delay: 1.2 },
  { id: 3, name: 'Aicha B.', comment: 'WhatsApp relié en 2 min !', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150', left: 8, top: 58, duration: 6.5, delay: 2.5 },
  { id: 4, name: 'Paul M.', comment: '+1 pour le dark mode', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150', left: 82, top: 55, duration: 8, delay: 0.8 },
  { id: 5, name: 'Carine T.', comment: 'Design hyper propre', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150', left: 45, top: 6, duration: 7.5, delay: 1.8 }
]

const currentUserId = ref('')

const getBoardShareUrl = (id: string) => {
  return `${window.location.origin}/board/${id}`
}

const fetchUserBoards = async () => {
  try {
    const url = currentUserId.value 
      ? `http://localhost:8000/api/topoboards/?user_id=${currentUserId.value}`
      : 'http://localhost:8000/api/topoboards/'
    
    const res = await fetch(url)
    if (res.ok) {
      const data = await res.json()
      userBoards.value = data
      
      if (selectedBoard.value) {
        const updated = data.find((b: any) => b.id === selectedBoard.value.id)
        if (updated) {
          selectedBoard.value = updated
        }
      }
    }
  } catch (err) {
    console.error('Erreur synchronisation API:', err)
  }
}

onMounted(() => {
  const topoUserStr = localStorage.getItem('topo_user')
  const savedData = localStorage.getItem('user_signup_response')
  
  if (topoUserStr) {
    try {
      const parsedUser = JSON.parse(topoUserStr)
      currentUserId.value = parsedUser?.id || ''
      userName.value = parsedUser?.user_metadata?.full_name || parsedUser?.email || ''
    } catch (e) {
      console.error(e)
    }
  } else if (savedData) {
    try {
      const parsed = JSON.parse(savedData)
      currentUserId.value = parsed?.user?.id || ''
      userName.value = parsed?.user?.user_metadata?.full_name || parsed?.user?.email || ''
    } catch (e) {
      console.error(e)
    }
  }
  
  fetchUserBoards()

  // Polling automatique discret en arrière-plan sans élément visuel superflu
  timer = setInterval(() => {
    fetchUserBoards()
  }, 3000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

const handleLogout = () => {
  localStorage.removeItem('user_signup_response')
  localStorage.removeItem('topo_token')
  localStorage.removeItem('topo_user')
  currentUserId.value = ''
  userName.value = ''
  userBoards.value = []
  router.push('/login')
}


const goToStudio = () => {
  router.push('/studio')
}

const openBoardDetails = (board: any) => {
  selectedBoard.value = board
}

const averageRating = (responses: any[]) => {
  if (!responses || !responses.length) return '0'
  const sum = responses.reduce((acc, r) => acc + (r.rating || 5), 0)
  return (sum / responses.length).toFixed(1)
}

const whatsappCount = (responses: any[]) => {
  if (!responses) return 0
  return responses.filter(r => !!r.whatsapp).length
}

const templates = [
  {
    id: 1,
    title: 'Feedback SaaS Standard',
    description: 'Collecte les rapports de bugs, requêtes de fonctionnalités et suggestions de tes utilisateurs.',
    tag: 'SaaS / Web App',
    icon: () => h('svg', { class: 'w-5 h-5', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 01-2-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z' })
    ])
  },
  {
    id: 2,
    title: 'Support WhatsApp Direct',
    description: 'Relie les tickets utilisateurs directement à ton compte WhatsApp pour répondre en direct.',
    tag: 'WhatsApp Integration',
    icon: () => h('svg', { class: 'w-5 h-5', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z' })
    ])
  },
  {
    id: 3,
    title: 'Roadmap Publique',
    description: 'Affiche la liste des fonctionnalités en cours de développement et laisse tes utilisateurs voter.',
    tag: 'Roadmap & Votes',
    icon: () => h('svg', { class: 'w-5 h-5', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' })
    ])
  }
]
</script>

<style scoped>
@keyframes popAndRespawn {
  0% { opacity: 0; transform: scale(0.3) translateY(20px); }
  15% { opacity: 1; transform: scale(1.05) translateY(0px); }
  25%, 75% { opacity: 1; transform: scale(1) translateY(-6px); }
  88% { opacity: 1; transform: scale(1.15); }
  95% { opacity: 0; transform: scale(1.4) blur(4px); }
  100% { opacity: 0; transform: scale(0.3) translateY(20px); }
}

.bubble-pop {
  animation: popAndRespawn ease-in-out infinite;
}
</style>
