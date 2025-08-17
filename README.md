# 🎯 SYSTÈME INTELLIGENT DE CRÉATION D'ISSUES GITHUB AGENTOVA

## 📋 **VUE D'ENSEMBLE**

Ce système révolutionne la création d'issues GitHub en utilisant l'intelligence artificielle pour guider et structurer le processus. Il garantit que chaque issue contient tous les détails techniques nécessaires pour les développeurs.

## 🏗️ **ARCHITECTURE**

```
.agentova-tools/
├── .cursor/                   # Configuration Cursor pour l'IA
│   ├── rules/
│   │   └── issue-management.mdc
│   └── issue-creator-instructions.md
├── github-issues/             # Gestion complète des issues
│   ├── templates/             # Templates par type d'issue
│   │   ├── feature.md
│   │   ├── bugfix.md
│   │   ├── enhancement.md
│   │   └── infrastructure.md
│   ├── drafts/               # Brouillons en cours de création
│   └── scripts/              # Scripts API GitHub
│       └── github-api.js
├── documentation/            # Documentation partagée
│   ├── project-overview.md
│   ├── architecture-global.md
│   └── development-guidelines.md
└── README.md                 # Ce fichier
```

## 🚀 **DÉMARRAGE RAPIDE**

### 1. **Configuration initiale :**
```bash
cd .agentova-tools/github-issues/scripts
npm init -y
npm install @octokit/rest dotenv
```

### 2. **Variables d'environnement :**
```bash
# Créer .env dans scripts/
GITHUB_TOKEN=your_github_token_here
GITHUB_OWNER=votre-organisation
GITHUB_REPO_SASS=sass-agentova-ai
GITHUB_REPO_MOBILE=agentova-mobile
GITHUB_REPO_ADMIN=agentova-admin
```

### 3. **Utilisation avec Cursor :**
```
@issue-creator Nouvelle fonctionnalité : Amélioration du chat avec IA
```

## 🎯 **WORKFLOW COMPLET**

### **Étape 1 : Déclenchement**
L'utilisateur déclenche la création avec une commande Cursor :
- `@issue-creator [description]`
- `🎯 Nouvelle issue : [description]`
- `Créer une issue pour [description]`

### **Étape 2 : Questionnaire intelligent**
L'IA pose des questions structurées selon le type d'issue :

#### 📝 **Pour une FEATURE :**
1. **Contexte métier** : Pourquoi cette fonctionnalité ?
2. **Spécifications techniques** : Quels composants modifier ?
3. **Interface utilisateur** : Comment ça doit apparaître ?
4. **Critères d'acceptation** : Comment valider la réussite ?
5. **Dépendances** : Quels autres éléments sont impactés ?

#### 🐛 **Pour un BUG :**
1. **Reproduction** : Étapes exactes pour reproduire
2. **Environnement** : OS, navigateur, version
3. **Impact** : Gravité et utilisateurs affectés
4. **Comportement** : Attendu vs actuel

### **Étape 3 : Validation**
L'IA vérifie :
- ✅ Complétude des informations
- ✅ Cohérence avec l'architecture Agentova
- ✅ Respect des patterns établis
- ✅ Sécurité workspace-centric

### **Étape 4 : Génération**
- Création d'un draft dans `drafts/`
- Application du template approprié
- Suggestion de labels et assignations
- Validation finale par l'utilisateur

### **Étape 5 : Publication**
- Création automatique sur GitHub
- Application des labels
- Notification de l'équipe
- Archivage du draft

## 📋 **TYPES D'ISSUES SUPPORTÉS**

| Type | Template | Usage |
|------|----------|-------|
| 🚀 **Feature** | `feature.md` | Nouvelles fonctionnalités |
| 🐛 **Bug** | `bugfix.md` | Corrections de problèmes |
| ⚡ **Enhancement** | `enhancement.md` | Améliorations existantes |
| 🏗️ **Infrastructure** | `infrastructure.md` | Modifications techniques |

## 🎯 **PROJETS SUPPORTÉS**

- **sass-agentova-ai** : Projet principal (React/Firebase)
- **agentova-mobile** : Application mobile (React Native)
- **agentova-admin** : Interface d'administration

## 🔧 **CONFIGURATION AVANCÉE**

### **Labels automatiques :**
- `type:feature`, `type:bug`, `type:enhancement`, `type:infrastructure`
- `priority:high`, `priority:medium`, `priority:low`
- `component:frontend`, `component:backend`, `component:shared`
- `project:sass`, `project:mobile`, `project:admin`

### **Assignation intelligente :**
- Frontend → Développeurs React
- Backend → Développeurs Firebase
- Mobile → Développeurs React Native
- Infrastructure → DevOps/Lead

## 📊 **AVANTAGES**

### ✅ **Pour le Product Owner :**
- Processus guidé et structuré
- Aucun détail technique oublié
- Issues complètes dès la création
- Vision globale des 3 projets

### ✅ **Pour les Développeurs :**
- Spécifications claires et complètes
- Contexte technique détaillé
- Critères d'acceptation précis
- Moins d'aller-retours

### ✅ **Pour l'Équipe :**
- Standardisation des issues
- Amélioration de la communication
- Traçabilité et documentation
- Gain de temps global

## 🛠️ **MAINTENANCE**

### **Mise à jour des templates :**
Les templates dans `templates/` peuvent être modifiés selon l'évolution des besoins.

### **Amélioration de l'IA :**
Les instructions dans `.cursor/` peuvent être affinées pour améliorer la pertinence des questions.

### **Nouveaux projets :**
Ajouter simplement un nouveau repository dans la configuration.

## 📞 **SUPPORT**

Pour toute question ou amélioration du système, créer une issue en utilisant... ce même système ! 😉

---

*Système créé pour optimiser la gestion des issues dans l'écosystème Agentova* 🎯
