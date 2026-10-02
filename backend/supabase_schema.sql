-- ========================================================
-- SCRIPT SQL DE CONFIGURATION DU PROJET SUPABASE (TOPO.CM)
-- A exécuter dans l'éditeur SQL de votre Dashboard Supabase
-- ========================================================

-- 1. Table des topoBoards (Formulaires créés par les utilisateurs)
CREATE TABLE IF NOT EXISTS public.topoboards (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    product_name TEXT NOT NULL,
    product_url TEXT NOT NULL,
    logo_url TEXT,
    hook_message TEXT NOT NULL,
    description TEXT,
    feedback_question TEXT NOT NULL,
    allow_rating BOOLEAN DEFAULT true,
    allow_whatsapp_contact BOOLEAN DEFAULT true,
    cta_text TEXT DEFAULT 'Envoyer mon retour',
    brand_color VARCHAR(10) DEFAULT '#FD711A',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Table des Réponses / Avis des utilisateurs
CREATE TABLE IF NOT EXISTS public.responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    topoboard_id UUID REFERENCES public.topoboards(id) ON DELETE CASCADE NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL,
    whatsapp TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 3. Activer la sécurité au niveau des lignes (Row Level Security - RLS)
ALTER TABLE public.topoboards ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.responses ENABLE ROW LEVEL SECURITY;

-- 4. Politiques de Sécurité (RLS Policies)

-- Politiques pour public.topoboards :
-- A. Les utilisateurs enregistrés peuvent lire leurs propres topoBoards
CREATE POLICY "Utilisateurs voient leurs propres topoboards"
ON public.topoboards FOR SELECT
USING (auth.uid() = user_id);

-- B. Les utilisateurs connectés peuvent créer un topoBoard
CREATE POLICY "Utilisateurs créent des topoboards"
ON public.topoboards FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- C. Lecture publique des topoBoards (pour les visiteurs du widget)
CREATE POLICY "Lecture publique des topoboards"
ON public.topoboards FOR SELECT
USING (true);

-- Politiques pour public.responses :
-- A. Tout le monde peut envoyer un avis (INSERT public)
CREATE POLICY "Tout le monde peut envoyer un avis"
ON public.responses FOR INSERT
WITH CHECK (true);

-- B. Le propriétaire du topoBoard peut lire les avis de son topoBoard
CREATE POLICY "Propriétaire lit les avis de son topoboard"
ON public.responses FOR SELECT
USING (
    EXISTS (
        SELECT 1 FROM public.topoboards
        WHERE topoboards.id = responses.topoboard_id
        AND topoboards.user_id = auth.uid()
    )
);
