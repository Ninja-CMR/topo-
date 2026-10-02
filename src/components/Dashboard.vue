<template>
  <div class="min-h-screen bg-[#FAF8F6] flex flex-col font-sans text-[#1C1410]">
    
    <!-- Top Navigation Header -->
    <header class="w-full bg-white border-b border-[#E9E4DF] px-6 py-3.5 flex items-center justify-between sticky top-0 z-30 shadow-xs">
      <div class="flex items-center gap-3">
        <Logo />
        <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-[#15803D]/10 text-[#15803D] flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-[#15803D] animate-pulse"></span>
          Mon Espace Personnel
        </span>
      </div>
      <div class="flex items-center gap-4">
        <button
          @click="goToStudio"
          class="px-4 py-2 bg-[#FD711A] hover:bg-[#E35D08] text-[#1C1410] font-bold text-xs rounded-[10px] shadow-xs flex items-center gap-1.5 transition-all cursor-pointer"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Nouveau topoBoard
        </button>
        <button
          @click="handleLogout"
          class="text-xs text-[#8C8077] hover:text-[#1C1410] font-semibold underline cursor-pointer"
        >
          Déconnexion
        </button>
      </div>
    </header>

    <!-- Main Dashboard Body -->
    <main class="w-full max-w-6xl mx-auto p-6 md:p-10 flex-1">
      
      <!-- User Welcome Banner -->
      <div class="mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-6 rounded-[20px] border border-[#E9E4DF] shadow-xs">
        <div>
          <h1 class="text-2xl font-extrabold text-[#1C1410]">Tableau de Bord topoBoards</h1>
          <p class="text-xs text-[#6B5F56] mt-1">Consulte tes formulaires actifs et analyse les retours enregistrés.</p>
        </div>
        <div class="flex items-center gap-3">
          <div class="px-3 py-1.5 bg-[#FAF8F6] border border-[#E9E4DF] rounded-[10px] text-xs">
            Total Boards: <strong class="text-[#FD711A]">{{ boards.length }}</strong>
          </div>
          <div class="px-3 py-1.5 bg-[#FAF8F6] border border-[#E9E4DF] rounded-[10px] text-xs">
            Avis reçus: <strong class="text-[#15803D]">{{ totalResponsesCount }}</strong>
          </div>
        </div>
      </div>

      <!-- MAIN VIEW: BOARDS LIST OR RESPONSES DETAIL -->
      <div v-if="!selectedBoard">
        <h2 class="text-lg font-bold text-[#1C1410] mb-4">Tes topoBoards créés</h2>
        
        <!-- Boards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="board in boards"
            :key="board.id"
            @click="openBoardDetails(board)"
            class="bg-white border border-[#E9E4DF] hover:border-[#FD711A] rounded-[20px] p-6 shadow-xs hover:shadow-md transition-all cursor-pointer flex flex-col justify-between group"
          >
            <div>
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-[#FAF8F6] border border-[#E9E4DF] flex items-center justify-center font-bold text-sm text-[#FD711A]">
                    {{ board.productName.charAt(0) }}
                  </div>
                  <div>
                    <h3 class="font-extrabold text-sm text-[#1C1410] group-hover:text-[#FD711A] transition-colors">
                      {{ board.productName }}
                    </h3>
                    <a :href="board.productUrl" target="_blank" @click.stop class="text-[11px] text-[#8C8077] hover:underline font-mono">
                      {{ board.productUrl }}
                    </a>
                  </div>
                </div>
                <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-[#15803D]/10 text-[#15803D]">Actif</span>
              </div>

              <p class="text-xs text-[#6B5F56] line-clamp-2 mb-4">
                {{ board.hookMessage }}
              </p>
            </div>

            <div class="pt-4 border-t border-[#F3EFEA] flex items-center justify-between text-xs">
              <span class="text-[#6B5F56] font-medium">
                💬 <strong class="text-[#1C1410]">{{ board.responses.length }}</strong> avis reçus
              </span>
              <span class="text-[#FD711A] font-bold group-hover:translate-x-1 transition-transform flex items-center gap-1">
                Voir les réponses &rarr;
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- GOOGLE FORMS STYLE RESPONSES VIEW -->
      <div v-else class="space-y-6">
        
        <!-- Back Navigation Button -->
        <button
          @click="selectedBoard = null"
          class="text-xs font-bold text-[#6B5F56] hover:text-[#1C1410] flex items-center gap-2 cursor-pointer mb-2"
        >
          &larr; Retour à la liste de mes topoBoards
        </button>

        <!-- Board Details Header Header -->
        <div class="bg-white p-6 rounded-[20px] border border-[#E9E4DF] shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-3 mb-1">
              <h2 class="text-2xl font-black text-[#1C1410]">{{ selectedBoard.productName }}</h2>
              <span class="text-xs font-mono bg-[#FAF8F6] px-2.5 py-1 rounded-md border border-[#E9E4DF] text-[#6B5F56]">
                {{ selectedBoard.id }}
              </span>
            </div>
            <p class="text-xs text-[#6B5F56]">Question posée : <strong>{{ selectedBoard.feedbackQuestion }}</strong></p>
          </div>

          <!-- Quick Share Links -->
          <div class="flex items-center gap-3">
            <a
              :href="'https://api.whatsapp.com/send?text=' + encodeURIComponent('Donne ton avis sur ' + selectedBoard.productName + ' : ' + selectedBoard.shareUrl)"
              target="_blank"
              class="px-3.5 py-2 bg-[#25D366] text-white font-bold text-xs rounded-[10px] flex items-center gap-2 hover:bg-[#20bd5a] transition-all cursor-pointer"
            >
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-0.999 3.648 3.742-.981z"/>
              </svg>
              Partager sur WhatsApp
            </a>
          </div>
        </div>

        <!-- Google Forms Metrics Bar -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] text-center">
            <span class="text-xs text-[#6B5F56] font-semibold">Total Réponses</span>
            <div class="text-3xl font-black text-[#1C1410] mt-1">{{ selectedBoard.responses.length }}</div>
          </div>
          <div class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] text-center">
            <span class="text-xs text-[#6B5F56] font-semibold">Note Moyenne</span>
            <div class="text-3xl font-black text-[#FD711A] mt-1">
              {{ averageRating(selectedBoard.responses) }} <span class="text-base font-normal">/ 5 ★</span>
            </div>
          </div>
          <div class="bg-white p-5 rounded-[16px] border border-[#E9E4DF] text-center">
            <span class="text-xs text-[#6B5F56] font-semibold">Contacts WhatsApp Reçus</span>
            <div class="text-3xl font-black text-[#15803D] mt-1">
              {{ whatsappCount(selectedBoard.responses) }}
            </div>
          </div>
        </div>

        <!-- Responses Feed (Like Google Forms Response Cards) -->
        <div class="space-y-4">
          <h3 class="text-sm font-extrabold uppercase tracking-wider text-[#6B5F56] px-1">
            Détail des Avis Reçus ({{ selectedBoard.responses.length }})
          </h3>

          <div
            v-for="resp in selectedBoard.responses"
            :key="resp.id"
            class="bg-white p-6 rounded-[18px] border border-[#E9E4DF] shadow-xs space-y-3"
          >
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="text-amber-400 font-bold text-sm">
                  {{ '★'.repeat(resp.rating) }}<span class="text-gray-300">{{ '★'.repeat(5 - resp.rating) }}</span>
                </span>
                <span class="text-xs text-[#8C8077] font-medium">• {{ resp.date }}</span>
              </div>
              <span v-if="resp.whatsapp" class="text-xs bg-[#25D366]/10 text-[#15803D] px-2.5 py-1 rounded-full font-mono flex items-center gap-1">
                💬 {{ resp.whatsapp }}
              </span>
            </div>

            <p class="text-sm text-[#1C1410] leading-relaxed font-medium bg-[#FAF8F6] p-3.5 rounded-[12px] border border-[#E9E4DF]">
              "{{ resp.comment }}"
            </p>
          </div>
        </div>

      </div>

    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import Logo from './Logo.vue'

const router = useRouter()
const selectedBoard = ref<any>(null)

// Mock Data pour les topoBoards créés et leurs réponses style Google Forms
const boards = ref([
  {
    id: 'board_89a3f2',
    productName: 'PaySaaS App',
    productUrl: 'https://paysaas.cm',
    hookMessage: 'Donne-nous ton avis en 30 secondes !',
    feedbackQuestion: 'Qu\'as-tu pensé de ta visite sur PaySaaS ?',
    shareUrl: 'https://topo.cm/board/89a3f2',
    responses: [
      { id: 1, rating: 5, comment: 'Application ultra rapide pour les paiements Orange et MTN Money au Cameroun !', whatsapp: '+237 699 00 11 22', date: 'Il y a 10 min' },
      { id: 2, rating: 4, comment: 'Le design est superbe mais ajoutez une confirmation par SMS.', whatsapp: '+237 677 44 55 66', date: 'Il y a 1 heure' },
      { id: 3, rating: 5, comment: 'Support très réactif sur WhatsApp. Bravo !', whatsapp: '+237 655 88 99 00', date: 'Hier' }
    ]
  },
  {
    id: 'board_41c9b0',
    productName: 'KamerShop Online',
    productUrl: 'https://kamershop.cm',
    hookMessage: 'Un problème lors de ta commande ? Dis-le nous !',
    feedbackQuestion: 'Comment s\'est passée ton expérience d\'achat ?',
    shareUrl: 'https://topo.cm/board/41c9b0',
    responses: [
      { id: 10, rating: 3, comment: 'Les prix sont bons mais la livraison a pris 2 jours de plus.', whatsapp: '+237 690 12 34 56', date: 'Il y a 3 heures' },
      { id: 11, rating: 5, comment: 'Excellent produit conforme aux photos !', whatsapp: '', date: 'Il y a 2 jours' }
    ]
  }
])

const totalResponsesCount = computed(() => {
  return boards.value.reduce((acc, b) => acc + b.responses.length, 0)
})

const openBoardDetails = (board: any) => {
  selectedBoard.value = board
}

const averageRating = (responses: any[]) => {
  if (!responses.length) return 0
  const sum = responses.reduce((acc, r) => acc + r.rating, 0)
  return (sum / responses.length).toFixed(1)
}

const whatsappCount = (responses: any[]) => {
  return responses.filter(r => !!r.whatsapp).length
}

const goToStudio = () => {
  router.push('/studio')
}

const handleLogout = () => {
  localStorage.removeItem('user_signup_response')
  localStorage.removeItem('topo_token')
  localStorage.removeItem('topo_user')
  router.push('/login')
}

</script>
