# 🎯 SYSTÈME INTELLIGENT DE CRÉATION D'ISSUES GITHUB AGENTOVA

## 🎥 **VIDÉO EXPLICATIVE COMPLÈTE**

**🔗 [Regarder la vidéo Loom - Tout est expliqué dedans](https://www.loom.com/share/8c449e4962e14699a1266c0d8da08f36?sid=498c9e05-cd88-4284-9138-2d5da1356619)**

Cette vidéo montre en détail comment utiliser le système de création de drafts d'issues.

## 🧩 **COMPRÉHENSION - À QUOI ÇA SERT**

Ce système permet de créer des drafts d'issues ultra-détaillées en utilisant l'intelligence artificielle. Il inclut aussi des outils pour récupérer de la documentation technique.

**🎯 Objectifs principaux :**
- **Drafts d'issues intelligents** : Transformer une demande floue en spécifications techniques précises sauvegardées localement
- **Documentation** : Récupérer facilement toute la documentation d'un site web

## 🏗️ **ARCHITECTURE RÉELLE**

```
.agentova-tools/
├── issue-generator/           # 🎯 Système principal de création de drafts d'issues
│   ├── ai-script.md          # 📋 Guide complet pour l'IA
│   └── drafts/              # 💾 Drafts générés (format: [titre-court].md)
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

## 🚀 **UTILISATION - 2 OUTILS PRINCIPAUX**

### **🎯 1. Créer un draft d'issue**

```
@issue-create
```

L'IA va poser toutes les questions nécessaires et générer un draft détaillé dans le dossier `drafts/`.

### **🕷️ 2. Récupérer de la documentation**

```bash
# Télécharger toutes les pages d'un site de documentation
python site-scaper/site-scraper.py https://docs.example.com

# Voir le guide complet
cat site-scaper/USAGE-SITE-SCRAPER.md
```

**⚠️ Note :** Ce scraper est utile mais Cursor a maintenant une fonctionnalité intégrée pour récupérer la documentation web. Le scraper reste utile pour certains cas spécifiques.

### **📋 3. Résultat : Draft généré**

Après avoir utilisé `@issue-create`, tu obtiendras :

```
.agentova-tools/issue-generator/drafts/[titre-court].md
```

**Le draft contient :**
- 🎯 Spécifications techniques précises
- 📁 Fichiers exacts à modifier
- ⚠️ Points critiques
- ✅ Critères de validation

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
3. **L'IA génère un fichier draft markdown ultra-détaillé** 
4. **Sauvegarde locale** dans `drafts/[titre-court].md`
5. **Modifications possibles** du draft généré

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
- 🤔 **20 questions obligatoires** à poser pour chaque draft
- 📝 **Format exact** du fichier markdown à générer
- 🔧 **Règles absolues** (jamais inventer, toujours demander)
- 💾 **Sauvegarde obligatoire** dans `drafts/[titre-court].md`
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

## 🚨 **CHECKLIST AVANT DE CRÉER UN DRAFT D'ISSUE**

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

Un draft d'issue ultra-détaillé sauvegardé localement avec :
- 🎯 **Objectif précis** et contexte métier
- 📁 **Fichiers exacts** à modifier avec emplacements
- 🔧 **Spécifications techniques** complètes  
- ⚠️ **Points critiques** à ne pas rater
- ✅ **Critères de validation** clairs

**L'objectif :** Un draft prêt à être utilisé pour créer une issue GitHub manuellement !

---

*🎯 Système de création de drafts d'issues Agentova - Transforme des demandes floues en spécifications précises sauvegardées localement*
