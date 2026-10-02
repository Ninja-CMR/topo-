# topo. — Design System

> **topo.** aide les développeurs à demander, collecter et centraliser les avis et retours utilisateurs directement sur **WhatsApp**.
> Version 1.0 · Couleur de marque extraite du logo : `#FD711A`

---

## 1. Univers & positionnement

### 1.1 Essence de la marque
topo. est un outil **d'écoute**. Là où les outils de feedback classiques sont froids (formulaires, tableurs, emails), topo. mise sur la **conversation** : un retour client, c'est un message, pas un ticket.

| Axe | Ce que topo. est | Ce que topo. n'est pas |
|---|---|---|
| Ton | Chaleureux, direct, humain | Corporate, jargonneux |
| Look | Arrondi, lumineux, généreux | Anguleux, sombre, dense |
| Énergie | Optimiste, vive, rapide | Agressive, bruyante |
| Cible | Développeurs, indie hackers, startups, équipes produit | Grandes DSI, back-offices complexes |

### 1.2 Mood (mots-clés)
**Chaleureux · Conversationnel · Friendly · Énergique · Simple · Rond · Lumineux · Rapide · Confiance**

Moodboard mental : la simplicité d'une app de messagerie + la clarté d'un dashboard développeur moderne (Linear, Vercel, Stripe) + la chaleur d'un orange vif.

### 1.3 Le point « . » — élément signature
Le point final du logo est l'ADN visuel de topo. Il sert de :
- **Ponctuation de marque** : titres de landing et hero → `Écoutez vos utilisateurs.`
- **Indicateur de notification / nouveau retour** (pastille orange)
- **Loader** (trois points qui pulsent)
- **Puce de liste** (bullet orange rond)

> Règle : le point orange est utilisé **avec parcimonie** (1 à 2 fois par écran) pour garder sa force.

### 1.4 Logo
- Wordmark en minuscules `topo.` — orange `#FD711A` sur fond clair.
- Sur fond orange ou sombre : version **blanche** ou **encre** (`#1C1410`).
- Zone de protection : au minimum la hauteur du « o » autour du logo.
- Taille minimale : **72 px** de large (digital), **20 mm** (print).
- Interdits : étirer, ajouter une ombre, changer la typographie, mettre sur un fond orange proche (< 3:1).

---

## 2. Couleurs

### 2.1 Palette principale — Orange topo.

| Token | Hex | Usage |
|---|---|---|
| `orange-50` | `#FFF5EC` | Fonds de sections, états sélectionnés légers |
| `orange-100` | `#FFE8D3` | Badges, fonds de hover discrets |
| `orange-200` | `#FFD0A6` | Bordures actives douces |
| `orange-300` | `#FFB070` | Illustrations, graphiques secondaires |
| `orange-400` | `#FF8F42` | Hover clair, accents |
| **`orange-500`** | **`#FD711A`** | **Couleur de marque, boutons primaires, CTA** |
| `orange-600` | `#E35D08` | Hover bouton primaire |
| `orange-700` | `#B84A06` | **Texte orange sur fond clair** (contraste AA) |
| `orange-800` | `#8A3704` | Pressed, texte sur `orange-100` |
| `orange-900` | `#5C2503` | Texte très accentué |

### 2.2 Neutres chauds
Les neutres sont légèrement **teintés chaud** pour s'harmoniser avec l'orange (jamais de gris bleuté pur).

| Token | Hex | Usage |
|---|---|---|
| `ink` | `#1C1410` | Titres, texte principal, texte sur orange |
| `neutral-800` | `#2E241E` | Surfaces sombres (dark mode) |
| `neutral-700` | `#4A3F37` | Texte secondaire fort |
| `neutral-600` | `#6B5F56` | Texte secondaire |
| `neutral-500` | `#8C8077` | Placeholders, icônes inactives |
| `neutral-400` | `#B3A89F` | Bordures fortes, désactivé |
| `neutral-300` | `#D6CEC7` | Bordures |
| `neutral-200` | `#E9E4DF` | Séparateurs |
| `neutral-100` | `#F4F1EE` | Fond d'app / zones secondaires |
| `neutral-50` | `#FAF8F6` | Fond de page |
| `white` | `#FFFFFF` | Cartes, surfaces |

### 2.3 Couleurs sémantiques

| Rôle | Fond | Texte/Icône | Usage |
|---|---|---|---|
| Succès | `#DCFCE7` | `#15803D` | Message envoyé, retour traité |
| Alerte | `#FEF3C7` | `#92400E` | Template en attente de validation Meta |
| Erreur | `#FEE2E2` | `#B91C1C` | Échec d'envoi, numéro invalide |
| Info | `#DBEAFE` | `#1D4ED8` | Astuces, notifications neutres |

> L'orange étant la couleur de marque, **ne pas l'utiliser pour une erreur ni une alerte**. Éviter aussi le jaune vif près de l'orange.

### 2.4 Sentiment des retours (spécifique topo.)

| Sentiment | Couleur | Emoji | Hex |
|---|---|---|---|
| Positif | Vert | 😊 | `#16A34A` |
| Neutre | Gris chaud | 😐 | `#8C8077` |
| Négatif | Rouge | 😞 | `#DC2626` |
| Suggestion / Idée | Violet doux | 💡 | `#7C3AED` |
| Bug signalé | Rouge-rose | 🐞 | `#E11D48` |

> Toujours doubler la couleur avec une **icône ou un label** (accessibilité daltonisme).

### 2.5 Univers WhatsApp
Le vert WhatsApp est un repère **externe** : il n'est jamais une couleur de topo., il sert seulement à signaler le canal.

| Élément | Hex |
|---|---|
| Vert WhatsApp (badge canal) | `#25D366` |
| Vert foncé (en-tête de preview) | `#075E54` |
| Bulle sortante (envoyée) | `#D9FDD3` |
| Bulle entrante (reçue) | `#FFFFFF` |
| Fond de conversation | `#EFEAE2` |

### 2.6 Dark mode (optionnel v1.1)

| Token | Hex |
|---|---|
| `bg` | `#16100C` |
| `surface` | `#211914` |
| `surface-raised` | `#2E241E` |
| `border` | `#3D3129` |
| `text` | `#F7F3EF` |
| `text-muted` | `#B3A89F` |
| `primary` | `#FF8A3D` (orange légèrement éclairci) |

### 2.7 Règles d'usage (60 / 30 / 10)
- **60 %** neutres clairs (fonds, cartes)
- **30 %** encre / neutres foncés (texte, structure)
- **10 %** orange (actions, accents, marque)

---

## 3. Contrastes & accessibilité

Le `#FD711A` est vif mais **n'atteint pas 4.5:1 avec du blanc** (≈ 2.8:1). Règles :

| Combinaison | Ratio approx. | Verdict |
|---|---|---|
| Encre `#1C1410` sur orange `#FD711A` | ≈ 6.6:1 | ✅ AA / AAA gros texte → **texte des boutons primaires** |
| Blanc sur orange `#FD711A` | ≈ 2.8:1 | ⚠️ Réservé aux très grands textes décoratifs (≥ 32 px bold) ou au logo |
| Orange-700 `#B84A06` sur blanc | ≈ 5.4:1 | ✅ AA → liens et texte orange |
| Encre sur blanc | ≈ 17:1 | ✅ AAA |
| `neutral-600` sur blanc | ≈ 5.9:1 | ✅ AA → texte secondaire |
| `neutral-500` sur blanc | ≈ 3.8:1 | ⚠️ Placeholders / texte non essentiel uniquement |

**Règles de base**
- Texte courant : ≥ **4.5:1**. Gros texte (≥ 24 px ou ≥ 18.5 px bold) : ≥ **3:1**.
- Composants UI (bordures de champs, icônes porteuses de sens) : ≥ **3:1**.
- **Focus visible** : anneau `2px` orange-500 + offset `2px` (jamais supprimé).
- Ne jamais communiquer une info par la couleur seule.
- Respecter `prefers-reduced-motion` et `prefers-color-scheme`.

---

## 4. Typographie

Le logo utilise une sans-serif **ultra-grasse aux terminaisons très arrondies** (style *Nunito Black / Baloo*). On reprend cette énergie pour les titres, avec une police neutre et lisible pour l'interface.

### 4.1 Familles

| Rôle | Police | Poids | Fallback |
|---|---|---|---|
| **Display / Titres** | **Nunito** | 700, 800, 900 | `'Nunito', 'Baloo 2', system-ui, sans-serif` |
| **Interface / Corps** | **Inter** | 400, 500, 600 | `'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif` |
| **Code / Clés API / Webhooks** | **JetBrains Mono** | 400, 500 | `'JetBrains Mono', ui-monospace, Menlo, monospace` |

> Option légère (performance) : tout en **Nunito** + Inter limité à 2 graisses. Charger avec `font-display: swap`, sous-ensemble latin + latin-ext (accents français).

### 4.2 Échelle typographique

| Token | Taille | Line-height | Poids | Police | Usage |
|---|---|---|---|---|---|
| `display-xl` | 56 px / 3.5 rem | 1.05 | 900 | Nunito | Hero landing |
| `display` | 44 px / 2.75 rem | 1.1 | 800 | Nunito | Titres de sections marketing |
| `h1` | 32 px / 2 rem | 1.2 | 800 | Nunito | Titre de page |
| `h2` | 24 px / 1.5 rem | 1.25 | 800 | Nunito | Titre de section |
| `h3` | 20 px / 1.25 rem | 1.3 | 700 | Nunito | Titre de carte |
| `h4` | 16 px / 1 rem | 1.4 | 700 | Nunito | Sous-titre |
| `body-lg` | 18 px / 1.125 rem | 1.6 | 400 | Inter | Intro, landing |
| **`body`** | **16 px / 1 rem** | **1.5** | **400** | Inter | **Texte par défaut** |
| `body-sm` | 14 px / 0.875 rem | 1.5 | 400 | Inter | Tableaux, métadonnées |
| `label` | 14 px | 1.2 | 600 | Inter | Labels de champs, boutons |
| `caption` | 12 px / 0.75 rem | 1.4 | 500 | Inter | Horodatage, aide |
| `code` | 13 px | 1.5 | 400 | JetBrains Mono | Snippets |

### 4.3 Règles
- **Minuscules** pour la marque et les titres courts (cohérent avec `topo.`), sentence case ailleurs. **Pas de MAJUSCULES** sauf micro-labels (`caption` + letter-spacing `0.06em`).
- Letter-spacing titres : `-0.02em` (≥ 32 px) ; corps : `0`.
- Longueur de ligne : **45–75 caractères** (≈ `max-width: 65ch`).
- Taille minimale sur mobile : **14 px** (16 px pour les champs → évite le zoom iOS).
- Alignement du texte : **à gauche** (jamais justifié). Centré uniquement pour hero, empty states et titres courts.

---

## 5. Espacements, grille & agencement

### 5.1 Échelle d'espacement (base 4 px)

| Token | Valeur | Usage |
|---|---|---|
| `space-1` | 4 px | Micro-écart icône/texte |
| `space-2` | 8 px | Écart interne serré |
| `space-3` | 12 px | Padding de petits composants |
| `space-4` | 16 px | **Padding standard**, gap par défaut |
| `space-5` | 20 px | |
| `space-6` | 24 px | Padding de cartes, gap entre cartes |
| `space-8` | 32 px | Séparation de blocs |
| `space-10` | 40 px | |
| `space-12` | 48 px | Séparation de sections |
| `space-16` | 64 px | Sections marketing |
| `space-24` | 96 px | Grandes respirations landing |

> Mood « généreux » : on préfère **plus d'air** que trop dense. Padding de carte par défaut : `24 px` desktop, `16 px` mobile.

### 5.2 Breakpoints (mobile-first)

| Nom | Largeur | Comportement |
|---|---|---|
| `xs` | < 480 px | Mobile : 1 colonne, navigation basse |
| `sm` | ≥ 480 px | Grand mobile |
| `md` | ≥ 768 px | Tablette : 2 colonnes, sidebar repliée |
| `lg` | ≥ 1024 px | Desktop : sidebar fixe |
| `xl` | ≥ 1280 px | Large : contenu centré |
| `2xl` | ≥ 1536 px | Max-width du contenu |

### 5.3 Grille
- **12 colonnes**, gouttière `24 px` (desktop) / `16 px` (mobile), marges latérales `16 px` mobile · `32 px` desktop.
- Largeur max du contenu : **1200 px** (dashboard) · **1120 px** (marketing) · **720 px** (lecture / formulaires).

### 5.4 Layout du dashboard développeur

```
┌─────────┬───────────────────────────────────────────┐
│         │  Topbar (64 px) : recherche · projet · 👤 │
│ Sidebar ├───────────────────────────────────────────┤
│ 248 px  │  Titre de page + actions primaires        │
│         │  ┌───────┐ ┌───────┐ ┌───────┐ (KPI)      │
│ topo.   │  └───────┘ └───────┘ └───────┘            │
│ ─────── │  ┌──────────────────┐ ┌────────────────┐  │
│ Retours │  │ Liste des retours │ │ Détail / chat  │  │
│ Campagne│  │ (master)          │ │ (detail)       │  │
│ Contacts│  └──────────────────┘ └────────────────┘  │
│ Insights│                                           │
│ Réglages│                                           │
└─────────┴───────────────────────────────────────────┘
```

- **Sidebar** : 248 px (72 px repliée, icônes seules). Item actif : fond `orange-50`, texte `orange-700`, barre gauche 3 px `orange-500`.
- **Topbar** : 64 px, fond blanc, bordure basse `neutral-200`.
- **Pattern master-detail** pour les retours (type boîte mail) : liste à gauche (≈ 40 %), conversation à droite (≈ 60 %). Sur mobile : écran liste → écran détail (push).
- **Mobile** : navigation **en bas** (5 items max), bouton d'action principal flottant (FAB 56 px, rond, orange).

### 5.5 Alignement
- Tout est calé sur la grille de **4 px**.
- Alignement vertical **centré** pour icône + texte ; **baseline** pour valeur + unité (ex. `128 retours`).
- Actions primaires **à droite** en haut de page (desktop), **en bas, pleine largeur** (mobile).
- Dans un formulaire : labels **au-dessus** des champs, un seul champ par ligne (sauf paires logiques : prénom/nom).
- Chiffres de KPI et colonnes numériques : `font-variant-numeric: tabular-nums`, alignés à droite.

---

## 6. Arrondis (border-radius)

Le logo est **très rond** : l'interface doit l'être aussi. Plus un élément est petit et interactif, plus il peut être arrondi.

| Token | Valeur | Usage |
|---|---|---|
| `radius-xs` | 6 px | Tags compacts, tooltips, code inline |
| `radius-sm` | 10 px | **Champs de saisie, petits boutons** |
| `radius-md` | 14 px | **Boutons standards, menus déroulants** |
| `radius-lg` | 20 px | **Cartes, modales, panneaux** |
| `radius-xl` | 28 px | Grandes cartes hero, bottom sheets |
| `radius-full` | 9999 px | Pastilles, badges, avatars, FAB, toggles, chips |

Règles :
- **Rayon imbriqué** : `radius-enfant = radius-parent − padding` (ex. carte 20 px avec padding 8 px → élément interne 12 px).
- Jamais de coins droits (0 px) sauf pour des éléments pleine largeur collés au bord de l'écran.
- Bulles de chat : 18 px avec le coin « queue » à 4 px.
- Cohérence : **un seul rayon par famille de composant**.

---

## 7. Élévation, bordures & effets

### 7.1 Ombres (douces, teintées chaud)

| Token | Valeur | Usage |
|---|---|---|
| `shadow-xs` | `0 1px 2px rgba(28,20,16,.06)` | Champs, boutons secondaires |
| `shadow-sm` | `0 2px 8px rgba(28,20,16,.08)` | Cartes |
| `shadow-md` | `0 8px 24px rgba(28,20,16,.10)` | Menus, popovers |
| `shadow-lg` | `0 16px 48px rgba(28,20,16,.14)` | Modales |
| `shadow-brand` | `0 8px 24px rgba(253,113,26,.30)` | CTA primaire en hover / hero |

### 7.2 Bordures
- Épaisseur standard : **1 px** `neutral-200` (cartes), `neutral-300` (champs).
- Focus / sélection : **2 px** `orange-500`.
- Préférer **ombre légère + bordure fine** plutôt que bordures épaisses.

### 7.3 Mouvement

| Token | Durée | Courbe | Usage |
|---|---|---|---|
| `fast` | 120 ms | `ease-out` | Hover, press |
| `base` | 200 ms | `cubic-bezier(.2,.8,.2,1)` | Ouverture de menu, onglets |
| `slow` | 320 ms | `cubic-bezier(.2,.8,.2,1)` | Modales, bottom sheets |

- Micro-interaction signature : le point orange « pop » (scale 0 → 1.2 → 1) à l'arrivée d'un nouveau retour.
- Skeletons plutôt que spinners pour les listes.
- Désactiver les animations non essentielles avec `prefers-reduced-motion`.

---

## 8. Iconographie & illustrations

- Bibliothèque recommandée : **Lucide** ou **Phosphor (rounded)**.
- Style : **trait 1.75–2 px**, extrémités **arrondies**, jamais de pleins anguleux.
- Tailles : 16 px (inline) · 20 px (boutons, listes) · 24 px (navigation) · 32+ px (empty states).
- Couleur : `neutral-600` par défaut, `orange-700` si actif, jamais plus de 2 couleurs par icône.
- Illustrations : formes **rondes et organiques**, bulles de dialogue, points, étincelles ; palette orange + neutres chauds + une touche de vert WhatsApp. Pas de 3D réaliste.
- Emojis : autorisés dans le **contenu** (réactions, sentiments, messages WhatsApp), pas pour remplacer les icônes d'interface.

---

## 9. Composants clés

### 9.1 Boutons

| Variante | Fond | Texte | Bordure | Usage |
|---|---|---|---|---|
| **Primaire** | `orange-500` | `ink` | — | 1 seul par écran |
| Primaire hover | `orange-600` + `shadow-brand` | `ink` | — | |
| Secondaire | `white` | `ink` | 1 px `neutral-300` | Actions alternatives |
| Doux (tonal) | `orange-50` | `orange-700` | — | Actions contextuelles |
| Fantôme | transparent | `neutral-700` | — | Actions tertiaires |
| Destructif | `#DC2626` | `white` | — | Suppression (avec confirmation) |

| Taille | Hauteur | Padding X | Texte | Radius |
|---|---|---|---|---|
| `sm` | 36 px | 14 px | 14 px / 600 | `radius-md` |
| **`md`** | **44 px** | **20 px** | **15 px / 600** | **`radius-md`** |
| `lg` | 52 px | 28 px | 16 px / 700 | `radius-lg` ou `full` |

- **Zone tactile minimale : 44 × 44 px**.
- État `disabled` : fond `neutral-200`, texte `neutral-500` (pas d'opacité seule).
- État `loading` : spinner à 3 points, largeur du bouton conservée.

### 9.2 Champs de saisie
- Hauteur **48 px**, radius `10 px`, bordure 1 px `neutral-300`, fond blanc, padding X 14 px.
- Focus : bordure + anneau `orange-500` (3 px à 25 % d'opacité).
- Erreur : bordure `#DC2626` + message dessous (12–14 px) avec icône ; jamais seulement en rouge.
- Label au-dessus (14 px / 600), aide en `caption` sous le champ.
- Input numéro de téléphone : sélecteur de pays + **format E.164 auto**, drapeau, validation en direct.

### 9.3 Cartes
- Fond blanc, radius `20 px`, bordure 1 px `neutral-200`, `shadow-sm`, padding 24 px.
- Carte cliquable : hover → `shadow-md` + translateY(-2 px).
- **Carte de retour (feedback card)** : avatar (ou initiale) · nom / numéro masqué · horodatage · extrait du message (2 lignes) · tags sentiment + catégorie · pastille orange si non lu.

### 9.4 Tags, badges & chips
- Hauteur 24–28 px, radius `full`, texte 12–13 px / 600, padding X 10 px.
- Fond = couleur sémantique à 12 % + texte à 700 de la même teinte.
- Chips filtrables : 36 px de haut, état actif `orange-100` + bordure `orange-400`.

### 9.5 Prévisualisation WhatsApp (composant signature)
Le développeur doit **voir exactement** ce que son utilisateur recevra.
- Cadre de téléphone épuré, fond `#EFEAE2`, en-tête `#075E54`.
- Bulle sortante `#D9FDD3`, radius 18 px (coin bas-droit 4 px), texte 14.5 px, heure en `caption`.
- Boutons de réponse rapide affichés comme sur WhatsApp (blancs, texte bleu `#027EB5`).
- Affichage côte à côte avec l'éditeur de message (split view), mise à jour en temps réel.

### 9.6 Tableaux & listes
- Hauteur de ligne 56 px (confort) / 44 px (dense, option).
- En-têtes : `caption` majuscules discrètes, fond `neutral-50`.
- Zébrage **interdit** ; survol de ligne `neutral-50`.
- Sur mobile : transformer les tableaux en **cartes empilées**.

### 9.7 Graphiques
- Série principale `orange-500`, secondaires `orange-300`, `neutral-400`, `#7C3AED`.
- Évolution du sentiment : vert / gris / rouge avec légende textuelle.
- Barres arrondies (radius 6 px en haut), grilles très discrètes (`neutral-200`), pas de 3D.
- Toujours un état vide parlant et un résumé en une phrase (« 72 % de retours positifs cette semaine »).

### 9.8 Navigation, modales, toasts
- **Modale** : radius 20–28 px, largeur 480 px (max 640 px), overlay `rgba(28,20,16,.5)`, fermeture par `Esc` et clic extérieur.
- **Bottom sheet** (mobile) : radius haut 28 px, poignée 36 × 4 px.
- **Toast** : en bas à droite (desktop) / en haut (mobile), 4 s, radius `14 px`, icône sémantique, action « Annuler » quand possible.
- **Onglets** : soulignement 3 px `orange-500` arrondi, texte actif `ink` 600.

### 9.9 États vides & chargement
- Illustration ronde + titre `h3` + 1 phrase + **1 action claire**.
- Ex. : « Aucun retour pour l'instant. Envoie ta première campagne WhatsApp pour que les premiers avis arrivent. [Créer une campagne] »
- Skeletons arrondis (même radius que le composant final), animation shimmer 1.4 s.

---

## 10. Hacks ergonomiques & bonnes pratiques UX

### 10.1 Pour une app de collecte de feedback (côté développeur)
1. **Time-to-first-feedback < 5 min** : onboarding en 3 étapes max → connecter WhatsApp → choisir un modèle → envoyer. Afficher une barre de progression.
2. **Templates prêts à l'emploi** : NPS, note 1–5, « Qu'est-ce qui manque ? », bug report, satisfaction post-support. Le développeur personnalise, il ne part jamais d'une page blanche.
3. **Inbox unifiée type email** : statuts (`Nouveau`, `En cours`, `Traité`), assignation, raccourcis clavier (`J/K` naviguer, `E` archiver, `R` répondre, `T` taguer).
4. **Tags automatiques** (sentiment, thème : bug / idée / prix / UX) avec possibilité de corriger en un clic.
5. **Recherche omniprésente** : `Cmd/Ctrl + K` (palette de commandes) pour naviguer, filtrer, créer.
6. **Filtres sauvegardables** (« Bugs négatifs de la semaine ») visibles comme chips.
7. **Insight avant donnée** : en haut du dashboard, une phrase résumée (« Le paiement est cité dans 14 retours négatifs ») avant les graphiques.
8. **Actions groupées** : sélection multiple + barre d'actions flottante.
9. **Export / intégrations** : Notion, Slack, GitHub Issues, CSV, webhooks. Le bouton « Créer une issue » depuis un retour est un gain de temps majeur.
10. **Documentation inline** : snippets copiables avec bouton « Copier » (feedback visuel « Copié ✓ »), clés API masquées par défaut avec bouton « Afficher ».

### 10.2 Pour l'expérience WhatsApp (côté utilisateur final)
Le design se prolonge dans les messages eux-mêmes : c'est là que se joue le taux de réponse.
1. **Réduire l'effort de réponse** : privilégier les **boutons de réponse rapide** (max 3 boutons, ≈ 20 caractères chacun) et les **listes** (jusqu'à 10 options) plutôt que la saisie libre.
2. **Une question à la fois**, message court (idéalement < 300 caractères), tutoiement ou vouvoiement selon le produit.
3. **Question fermée d'abord, ouverte ensuite** : « Note ta commande ⭐ » puis « Qu'est-ce qui aurait pu être mieux ? ».
4. **Annoncer la durée** : « 2 questions, 30 secondes ».
5. **Remercier et conclure** : confirmer la réception et, si possible, annoncer ce qui sera fait du retour.
6. **Respecter le cadre WhatsApp Business** : consentement (opt-in) obligatoire, modèles de messages soumis à validation par Meta pour initier une conversation, fenêtre de **24 h** pour répondre librement après un message de l'utilisateur, possibilité de se désabonner (« STOP »). L'interface doit **guider et alerter** le développeur (statut du template, fenêtre restante, quotas).
7. **Fréquence maîtrisée** : afficher un indicateur de « fatigue » et plafonner les relances (1 relance max recommandée).
8. **Prévisualisation obligatoire** avant envoi + envoi de test vers son propre numéro.
9. **Multilingue** : détection de langue du retour, réponses modèles FR / EN, jamais de texte tronqué (prévoir +30 % de longueur).
10. **Respect de la vie privée** : numéros masqués par défaut (`+237 6•• ••• •42`), anonymisation en un clic, mention RGPD / consentement visible.

### 10.3 Ergonomie générale
- **Mobile-first** : les développeurs consultent aussi leurs retours depuis leur téléphone. Zone du pouce : actions principales en bas.
- **Légèreté** : pages < 200 KB hors données, images en WebP/SVG, tolérance aux connexions lentes, mode hors-ligne lecture seule si possible.
- **Loi de Fitts** : cibles tactiles ≥ 44 px, boutons principaux grands et proches du pouce/curseur.
- **Loi de Hick** : max **5–7 items** dans une navigation, menus déroulants regroupés.
- **Hiérarchie claire** : une action primaire (orange plein) par écran, le reste en secondaire/fantôme.
- **Feedback immédiat** : toute action déclenche une réponse visuelle < 100 ms (état optimiste, toast, changement de bouton).
- **Prévention des erreurs** : confirmation pour actions destructives (saisir le nom du projet pour supprimer), annulation (`undo`) plutôt que dialogue quand possible.
- **Messages d'erreur humains** : dire *quoi* + *pourquoi* + *comment corriger*. Ex. : « Ce numéro n'a pas l'air valide. Ajoute l'indicatif du pays, par exemple +237. »
- **Valeurs par défaut intelligentes** et mémoire des derniers choix.
- **Densité adaptative** : option « Confortable / Compact » dans les réglages.
- **Accessibilité** : navigation clavier complète, ordre de tabulation logique, `aria-label` sur icônes, textes alternatifs, lecteur d'écran testé sur les composants clés.

---

## 11. Voix & ton (microcopy)

| Principe | Exemple |
|---|---|
| **Direct et simple** | « Envoie ta campagne » plutôt que « Procéder à l'envoi de la campagne » |
| **Chaleureux sans excès** | « Bien joué, ta première campagne est partie. » |
| **Précis** | « 12 réponses reçues en 2 h » plutôt que « Plusieurs réponses » |
| **Humain en cas d'erreur** | « Oups, WhatsApp n'a pas répondu. Réessaie dans un instant. » |
| **Ponctuation signature** | Titres courts qui se terminent par un point : « Écoute tes utilisateurs. » |

- Tutoiement par défaut dans l'app (public développeurs), vouvoiement configurable pour les messages envoyés aux clients finaux.
- Emojis : 0 à 1 par message d'interface, plus libres dans les modèles WhatsApp.
- Boutons : verbes d'action à l'infinitif ou à l'impératif (« Créer une campagne », « Copier la clé »).
- Jamais de jargon non expliqué (« webhook », « opt-in » → info-bulle au premier usage).

---

## 12. Design tokens (CSS)

```css
:root {
  /* Marque */
  --orange-50:  #FFF5EC;
  --orange-100: #FFE8D3;
  --orange-200: #FFD0A6;
  --orange-300: #FFB070;
  --orange-400: #FF8F42;
  --orange-500: #FD711A; /* couleur du logo */
  --orange-600: #E35D08;
  --orange-700: #B84A06;
  --orange-800: #8A3704;
  --orange-900: #5C2503;

  /* Neutres chauds */
  --ink:         #1C1410;
  --neutral-800: #2E241E;
  --neutral-700: #4A3F37;
  --neutral-600: #6B5F56;
  --neutral-500: #8C8077;
  --neutral-400: #B3A89F;
  --neutral-300: #D6CEC7;
  --neutral-200: #E9E4DF;
  --neutral-100: #F4F1EE;
  --neutral-50:  #FAF8F6;
  --white:       #FFFFFF;

  /* Sémantique */
  --success-bg: #DCFCE7; --success: #15803D;
  --warning-bg: #FEF3C7; --warning: #92400E;
  --error-bg:   #FEE2E2; --error:   #B91C1C;
  --info-bg:    #DBEAFE; --info:    #1D4ED8;

  /* WhatsApp (canal uniquement) */
  --wa-green:    #25D366;
  --wa-dark:     #075E54;
  --wa-bubble-out: #D9FDD3;
  --wa-bubble-in:  #FFFFFF;
  --wa-chat-bg:    #EFEAE2;

  /* Typographie */
  --font-display: 'Nunito', 'Baloo 2', system-ui, sans-serif;
  --font-ui:      'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-mono:    'JetBrains Mono', ui-monospace, Menlo, monospace;

  /* Arrondis */
  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-full: 9999px;

  /* Ombres */
  --shadow-xs: 0 1px 2px rgba(28,20,16,.06);
  --shadow-sm: 0 2px 8px rgba(28,20,16,.08);
  --shadow-md: 0 8px 24px rgba(28,20,16,.10);
  --shadow-lg: 0 16px 48px rgba(28,20,16,.14);
  --shadow-brand: 0 8px 24px rgba(253,113,26,.30);

  /* Espacements */
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px; --space-12: 48px; --space-16: 64px;

  /* Mouvement */
  --ease: cubic-bezier(.2,.8,.2,1);
  --dur-fast: 120ms; --dur-base: 200ms; --dur-slow: 320ms;
}
```

### Exemple Tailwind (`tailwind.config.js`)

```js
export default {
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#FFF5EC', 100: '#FFE8D3', 200: '#FFD0A6', 300: '#FFB070',
          400: '#FF8F42', 500: '#FD711A', 600: '#E35D08', 700: '#B84A06',
          800: '#8A3704', 900: '#5C2503',
        },
        ink: '#1C1410',
        warm: {
          50: '#FAF8F6', 100: '#F4F1EE', 200: '#E9E4DF', 300: '#D6CEC7',
          400: '#B3A89F', 500: '#8C8077', 600: '#6B5F56', 700: '#4A3F37', 800: '#2E241E',
        },
      },
      fontFamily: {
        display: ['Nunito', 'Baloo 2', 'system-ui', 'sans-serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
      },
      borderRadius: { xs: '6px', sm: '10px', md: '14px', lg: '20px', xl: '28px' },
      boxShadow: {
        brand: '0 8px 24px rgba(253,113,26,.30)',
      },
    },
  },
};
```

---

## 13. Checklist de cohérence

- [ ] Un seul bouton primaire orange par écran
- [ ] Texte sur orange en **encre**, jamais en blanc (sauf très grand titre décoratif)
- [ ] Texte orange sur fond clair en `orange-700` minimum
- [ ] Arrondis ≥ 10 px sur tous les composants interactifs
- [ ] Titres en Nunito 800/900, interface en Inter
- [ ] Zones tactiles ≥ 44 px
- [ ] Focus visible sur tous les éléments interactifs
- [ ] Sentiment = couleur **+** icône/label
- [ ] Prévisualisation WhatsApp avant tout envoi
- [ ] Le point orange « . » utilisé avec parcimonie

---

*topo. — écoute tes utilisateurs.*
