# 🎯 SYSTÈME INTELLIGENT DE CRÉATION D'ISSUES GITHUB AGENTOVA

## 🧩 **COMPRÉHENSION - À QUOI ÇA SERT**

Ce système permet d'améliorer et créer des issues GitHub ultra-détaillées en utilisant l'intelligence artificielle. Il inclut aussi des outils pour récupérer de la documentation technique.

**🎯 Objectifs principaux :**
- **Issues intelligentes** : Transformer une demande floue en spécifications techniques précises
- **Documentation** : Récupérer facilement toute la documentation d'un site web

## 🏗️ **ARCHITECTURE RÉELLE**

```
.agentova-tools/
├── issue-generator/           # 🎯 Système principal d'amélioration d'issues
│   ├── ai-script.md          # 📋 Guide complet pour l'IA
│   └── drafts/              # 💾 Brouillons générés
├── site-scaper/              # 🕷️ Outils de scraping documentation
│   ├── site-scraper.py       # Script de téléchargement sites web
│   └── USAGE-SITE-SCRAPER.md # Guide d'utilisation du scraper
├── project-context.md        # 🏗️ Contexte global des 3 projets Agentova
├── github-api.py            # 🔧 Scripts interaction GitHub API
├── requirements.txt          # 📦 Dépendances Python
└── README.md                # 📖 Ce fichier
```

## 🛠️ **INSTALLATION**

### **1. Structure de dossier obligatoire**

**⚠️ CRITIQUE :** Tous les projets Agentova doivent être dans le même dossier parent :

```
📁 Agentova/ (dossier parent)
├── 📁 .agentova-tools/          # 🎯 Ce système
├── 📁 sass-agentova-ai/         # 🚀 Projet principal (React/Firebase)
├── 📁 api-agent-agentova-ai/    # 🤖 API IA (FastAPI/Google ADK)
└── 📁 chat-widget-agentova-ai/  # 💬 Widget de chat
```



### **2. Configuration GitHub API (optionnelle)**

**Pour utiliser `github-api.py` qui récupère les issues existantes :**

```bash
# Dans .agentova-tools/
pip install -r requirements.txt
```

```bash
# Créer un fichier .env dans .agentova-tools/
echo "GITHUB_TOKEN=votre_token_github_ici" > .env
```

**Comment obtenir un token GitHub :**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Créer un nouveau token avec permission "repo"
3. Copier le token dans le fichier `.env`

**⚠️ Sans token :** `github-api.py` ne fonctionnera pas, mais l'amélioration d'issues via Cursor fonctionne quand même.

## 🚀 **UTILISATION - 2 OUTILS PRINCIPAUX**

### **🎯 1. Améliorer une issue**

```
@issue-improve
```

L'IA va automatiquement récupérer toutes les issues GitHub et vous aider à les améliorer.

### **🕷️ 2. Récupérer de la documentation**

```bash
# Télécharger toutes les pages d'un site de documentation
python site-scaper/site-scraper.py https://docs.example.com

# Voir le guide complet
cat site-scaper/USAGE-SITE-SCRAPER.md
```

**⚠️ Note :** Ce scraper est utile mais Cursor a maintenant une fonctionnalité intégrée pour récupérer la documentation web. Le scraper reste utile pour certains cas spécifiques.

### **📋 3. Lister les issues existantes**

```bash
# Lister toutes les issues ouvertes du projet principal
python github-api.py list sass

# Lister pour les autres projets
python github-api.py list api
python github-api.py list widget
```

**Nécessite :** Configuration du token GitHub dans `.env`

### **📋 ÉTAPES OBLIGATOIRES AVANT DE COMMENCER**

**⚠️ CRITICAL :** Il faut ABSOLUMENT charger ces 3 fichiers dans Cursor :

1. **📂 Glisser le dossier `.cursor/`** du projet concerné
2. **📄 Attacher `project-context.md`** (contexte global des 3 projets)  
3. **📄 Attacher `ai-script.md`** (guide complet pour l'IA)

**Exemple pour une issue sass-agentova-ai :**
```
📂 Fichiers à attacher OBLIGATOIREMENT :
├── 📁 .agentova-tools/project-context.md # ✅ OBLIGATOIRE - Contexte global
├── 📁 .agentova-tools/ai-script.md       # ✅ OBLIGATOIRE - Guide IA
├── 📁 sass-agentova-ai/.cursor/          # ✅ OBLIGATOIRE - Règles projet
└── 📁 api-agent-agentova-ai/.cursor/     # ✅ OBLIGATOIRE - Règles projet
```

### **🤔 Ce qui va se passer**

1. **L'IA pose des questions précises** selon `ai-script.md`
2. **Tu réponds avec les détails techniques**
3. **L'IA génère un fichier markdown ultra-détaillé** 
4. **Validation** puis publication automatique sur GitHub

## 📚 **FICHIERS CRITIQUES À CONNAÎTRE**

### **🏗️ `project-context.md` - LE FICHIER ESSENTIEL**

**⚠️ CRITICAL :** Ce fichier contient TOUT le contexte des 3 projets Agentova :

- 📋 **Structure des 3 projets** (sass-agentova-ai, api-agent-agentova-ai, chat-widget-agentova-ai)
- 🏗️ **Architecture technique** détaillée (Frontend, Backend, IA, Widget)
- 🎯 **Patterns obligatoires** (sécurité workspace-centric, types, etc.)
- 🏷️ **Assignations par expertise** (qui développe quoi)
- 🤔 **Questions intelligentes** à poser pour chaque projet

**Sans ce fichier, l'IA ne peut pas :**
- ❌ Comprendre l'architecture Agentova
- ❌ Poser les bonnes questions techniques
- ❌ Respecter les patterns établis
- ❌ Identifier les bons fichiers à modifier

### **📋 `ai-script.md` - LE GUIDE COMPLET**

Ce fichier contient :
- 🤔 **16 questions obligatoires** à poser pour chaque issue
- 📝 **Format exact** du fichier markdown à générer
- 🔧 **Règles absolues** (jamais inventer, toujours demander)
- 🚨 **Solutions aux problèmes** rencontrés précédemment

### **⚙️ Règles `.cursor/` - L'ARCHITECTURE PROJET**

Chaque projet a ses propres règles dans `.cursor/` :
- 🏗️ **Patterns architecturaux** spécifiques
- 🔐 **Sécurité workspace-centric** 
- 📊 **Validation des données**
- 🎯 **Conventions de nommage**

## 🎯 **LES 3 PROJETS AGENTOVA**

### **📱 sass-agentova-ai** - Projet principal
- **Frontend** : React + modules (ChatModule, CustomAgentModule, etc.)
- **Backend** : Firebase Functions + repositories PostgreSQL
- **Sécurité** : Workspace-centric obligatoire

### **🤖 api-agent-agentova-ai** - API IA  
- **Type** : FastAPI + Google ADK
- **Rôle** : Traitement IA, génération réponses agents
- **Communication** : SSE streaming pour chat temps réel

### **💬 chat-widget-agentova-ai** - Widget embeddable
- **Type** : JavaScript vanilla embeddable
- **Rôle** : Interface chat pour sites clients

## 🚨 **CHECKLIST AVANT D'AMÉLIORER UNE ISSUE**

### ✅ **Vérifications OBLIGATOIRES :**

1. [ ] **📁 Structure** : Tous les projets dans le même dossier parent Agentova ?
2. [ ] **📄 project-context.md** : Fichier attaché dans Cursor ?  
3. [ ] **📄 ai-script.md** : Guide IA attaché dans Cursor ?
4. [ ] **📁 .cursor/** : Règles du projet concerné attachées ?
5. [ ] **📁 shared/** : Types du projet attachés si nécessaire ?

### ❌ **Erreurs qui font échouer le processus :**

- **Oublier `project-context.md`** → L'IA ne comprend pas l'architecture
- **Oublier `ai-script.md`** → L'IA ne pose pas les bonnes questions  
- **Mélanger les règles** de plusieurs projets → Incohérences
- **Ne pas identifier le projet** → Spécifications génériques inutiles

## 🎯 **RÉSULTAT ATTENDU**

Une issue GitHub ultra-détaillée avec :
- 🎯 **Objectif précis** et contexte métier
- 📁 **Fichiers exacts** à modifier avec emplacements
- 🔧 **Spécifications techniques** complètes  
- ⚠️ **Points critiques** à ne pas rater
- ✅ **Critères de validation** clairs

**L'objectif :** N'importe quel développeur peut implémenter sans poser de questions !

---

*🎯 Système d'amélioration d'issues Agentova - Transforme des demandes floues en spécifications précises*
