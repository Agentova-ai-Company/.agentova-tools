# 🏗️ CONTEXTE PROJETS AGENTOVA - RÈGLES GLOBALES

## 📋 **LES 3 PROJETS RÉELS**

### 🎯 **sass-agentova-ai** (Projet principal)
- **Type** : Application web React + Firebase
- **Structure** :
  - `client/` : Frontend React avec modules (ChatModule, CustomAgentModule, etc.)
  - `server/` : Firebase Functions + repositories
  - `shared/` : Types TypeScript partagés
- **Rôle** : Interface principale pour créer et gérer les agents IA
- **Technologies** : React, Next.js, Firebase Functions, PostgreSQL
- **Modules principaux** : Chat, Agents personnalisés, Campagnes, Automations

### 🤖 **api-agent-agentova-ai** (API IA)
- **Type** : API Python FastAPI
- **Structure** :
  - `app/` : API endpoints
  - `ai/` : Logique IA et modèles
  - `models/` : Modèles de données
- **Rôle** : Backend IA qui traite les conversations et génère les réponses
- **Technologies** : Python, FastAPI, modèles IA
- **Fonctions** : Traitement NLP, génération réponses, sessions chat

### 💬 **chat-widget-agentova-ai** (Widget embeddable)
- **Type** : Widget JavaScript embeddable
- **Structure** :
  - `src/` : Code du widget
  - `public/` : Assets statiques
- **Rôle** : Widget de chat à intégrer sur les sites web des clients
- **Technologies** : Vanilla JavaScript, Webpack
- **Fonctions** : Interface chat client, communication avec l'API

## 🔧 **ARCHITECTURE TECHNIQUE**

### 🎨 **Frontend (sass-agentova-ai/client/)**
- **Modules** : ChatModule, CustomAgentModule, CampaignModule, ReplyModule, etc.
- **Services** : Classes statiques avec `workspaceId` en premier paramètre
- **Hooks** : React Query + `useWorkspaceContext()`
- **Composants** : Props typées + `useCallback` handlers

### 🔐 **Backend (sass-agentova-ai/server/)**
- **Firebase Functions** : Validation cascade (auth → params → workspace → métier)
- **Repositories** : Pattern singleton + Pool PostgreSQL + isolation workspace
- **Sécurité** : `validateAuth()` + `verifyWorkspaceToken()` obligatoire
- **Types** : Tous dans `shared/types.ts` + enums obligatoires

### 🤖 **IA (api-agent-agentova-ai/)**
- **Endpoints** : FastAPI avec streaming SSE
- **Sessions** : Gestion conversation + contexte
- **Modèles** : Integration LLM pour génération réponses

### 💬 **Widget (chat-widget-agentova-ai/)**
- **Integration** : Script embeddable + iframe
- **Communication** : WebSocket/API vers sass-agentova-ai

## 🏷️ **ASSIGNATIONS PAR EXPERTISE**

### 👨‍💻 **Développeurs suggérés** :
- **Frontend React** : Expert modules + hooks + UI
- **Backend Firebase** : Expert Functions + repositories + sécurité
- **IA/API Python** : Expert FastAPI + modèles + NLP
- **Widget JavaScript** : Expert vanilla JS + intégration
- **DevOps** : Expert déploiement + infrastructure

### 📦 **Projets par composant** :
- **Interface utilisateur** → sass-agentova-ai (client/)
- **Logique métier** → sass-agentova-ai (server/) 
- **Intelligence artificielle** → api-agent-agentova-ai
- **Integration client** → chat-widget-agentova-ai

## 🎯 **PATTERNS OBLIGATOIRES**

### 🔐 **Sécurité workspace-centric** :
- `workspace_id` TOUJOURS en premier paramètre
- `WHERE workspace_id = $1` dans TOUTES les requêtes SQL
- Validation token workspace à chaque appel
- Rôles : ADMIN/EDITOR/VIEWER selon contexte

### 📝 **Types et Enums** :
- Tous les types dans `shared/types.ts`
- JAMAIS de strings littérales → utiliser enums
- Interfaces explicites pour props React

### 🏗️ **Structure obligatoire** :
```
FRONTEND (sass-agentova-ai/client/):
- modules/     # Modules métier (ChatModule, etc.)
- components/  # Composants réutilisables
- services/    # Classes statiques API
- hooks/       # Hooks React Query

BACKEND (sass-agentova-ai/server/):
- functions/   # Firebase Functions
- db/repositories/  # Accès données
- shared/      # Types partagés

IA API (api-agent-agentova-ai/):
- app/         # Endpoints FastAPI
- ai/          # Logique IA
- models/      # Modèles données

WIDGET (chat-widget-agentova-ai/):
- src/         # Code widget
- public/      # Assets
```

## 🎯 **QUESTIONS INTELLIGENTES À POSER**

### 📋 **Questions par projet** :

#### sass-agentova-ai :
- "Quels modules sont impactés ? (Chat/CustomAgent/Campaign/Reply/etc.)"
- "Côté client : nouveaux composants/hooks/services ?"
- "Côté serveur : nouvelles functions/repositories ?"
- "Nouveaux types dans shared/types.ts ?"
- "Rôles workspace requis ? (ADMIN/EDITOR/VIEWER)"

#### api-agent-agentova-ai :
- "Nouveaux endpoints FastAPI ?"
- "Modifications logique IA/NLP ?"
- "Nouveaux modèles de données ?"
- "Impact sur les sessions de chat ?"

#### chat-widget-agentova-ai :
- "Modifications interface widget ?"
- "Nouvelles fonctionnalités integration ?"
- "Communication avec sass-agentova-ai ?"

### 🔍 **Questions techniques essentielles** :
1. **Quel(s) projet(s)** sont impactés et pourquoi ?
2. **Quels fichiers/classes** seront modifiés exactement ?
3. **Nouveaux composants/functions** à créer ?
4. **Base de données** : nouvelles tables/colonnes ?
5. **Sécurité** : quels rôles workspace nécessaires ?
6. **Tests** : quoi tester spécifiquement ?

## 🏷️ **LABELS GITHUB AUTOMATIQUES**

### Par type :
- `type:feature` - Nouvelle fonctionnalité
- `type:bug` - Correction problème
- `type:enhancement` - Amélioration
- `type:infrastructure` - Technique

### Par projet :
- `project:sass` - sass-agentova-ai
- `project:api` - api-agent-agentova-ai  
- `project:widget` - chat-widget-agentova-ai

### Par composant :
- `component:frontend` - Interface utilisateur
- `component:backend` - Logique serveur
- `component:ai` - Intelligence artificielle
- `component:widget` - Widget embeddable

### Par priorité :
- `priority:critical` - Bloquant
- `priority:high` - Important
- `priority:medium` - Normal
- `priority:low` - Quand possible

---

**Ce contexte permet de poser les bonnes questions et créer des issues précises !** 🎯
