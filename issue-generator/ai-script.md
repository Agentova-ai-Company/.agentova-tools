# 🤖 SCRIPT IA - AMÉLIORATION D'ISSUES AGENTOVA

## 🎯 **ACTIVATION SIMPLE**

### **Mode unique : Amélioration d'issues existantes**
`@issue-improve` - Récupère toutes les issues et aide à les améliorer en posant les bonnes questions

## 🚀 **PROCESSUS : QUESTIONS + ÉCRITURE**

## 📋 **1. RÉCUPÉRATION AUTOMATIQUE DES ISSUES**

L'IA récupère automatiquement toutes les issues avec :
```bash
python3 github-api.py list sass open
python3 github-api.py list api open  
python3 github-api.py list widget open
```
Tu es déjà dans le fichier pas besoin de retourner à la racine De donner le chemin global

## 🤔 **2. QUESTIONS OBLIGATOIRES POUR CHAQUE ISSUE**

**RÈGLE ABSOLUE** : ❌ JAMAIS inventer d'informations ❌ 

### **Questions pour comprendre le QUOI :**
1. **"Explique-moi exactement ce qu'il faut développer/corriger. Sois très précis !"**
2. **"Quel est le vrai problème qu'on résout ? Pourquoi c'est important maintenant ?"**

### **Questions pour identifier le PROJET :**
3. **"C'est sur quel projet : sass-agentova-ai / api-agent-agentova-ai / chat-widget-agentova-ai ?"**
4. **"Si je ne connais pas le projet, je consulte @.cursor/ pour comprendre l'architecture"**

### **Questions pour identifier les FICHIERS :**
5. **"Quels fichiers précis il faut modifier ?"**
6. **"Quelles classes/fonctions/composants exacts ?"**
7. **"Il faut créer quoi de nouveau ?"**

### **Questions pour comprendre l'EXISTANT :**
8. **"Est-ce qu'il y a déjà des parties développées ? Lesquelles ?"**
9. **"Y a-t-il des cas spéciaux à gérer ? Des pièges à éviter ?"**

### **Questions pour la VALIDATION :**
10. **"Comment on sait que c'est réussi ? Quoi tester exactement ?"**
11. **"As-tu fait une vidéo Loom pour expliquer visuellement ?"**

### **Questions pour les POINTS CRITIQUES :**
12. **"Sur quoi il faut ABSOLUMENT pas se planter ?"**
13. **"Est-ce qu'il y a des choses où le dev devra venir te parler avant de décider ?"**

### **Questions pour les FICHIERS/CLASSES TECHNIQUES :**
14. **"Maintenant explique-moi quels fichiers et classes exactes il faut modifier"**
15. **"Quelles nouvelles classes/composants/services il faut créer ?"**
16. **"Y a-t-il des dépendances avec d'autres issues ?"**

## 📝 **3. ÉCRITURE EXACTE DES RÉPONSES**

**RÈGLE ABSOLUE** : ✅ ÉCRIRE UNIQUEMENT ce que Samy dit ✅

### **Format du fichier** : `github-issues/drafts/YYYY-MM-DD-issue-[numero]-enhanced.md`

```markdown
# ISSUE #[NUMERO] - [TITRE_ORIGINAL] (VERSION AMÉLIORÉE)

## 🎯 QU'EST-CE QU'IL FAUT FAIRE EXACTEMENT
[ÉCRIRE EXACTEMENT CE QUE SAMY EXPLIQUE]

## 🤔 POURQUOI ON FAIT ÇA
[ÉCRIRE EXACTEMENT CE QUE SAMY EXPLIQUE]

## 📁 FICHIERS ET CLASSES À MODIFIER
**Projet concerné :** [CE QUE SAMY PRÉCISE]
[LISTER EXACTEMENT CE QUE SAMY INDIQUE]

## ⚠️ POINTS CRITIQUES
[ÉCRIRE EXACTEMENT CE QUE SAMY SOULIGNE]

## 🔧 DÉTAILS TECHNIQUES
[ÉCRIRE EXACTEMENT CE QUE SAMY PRÉCISE]

## 🎥 RESSOURCES
**Vidéo Loom :** [LIEN SI SAMY EN DONNE UN]
**Discussion requise :** [CE QUE SAMY INDIQUE]

## ✅ VALIDATION
[ÉCRIRE EXACTEMENT CE QUE SAMY DÉCRIT]

---
*Issue améliorée le [DATE] avec les explications de Samy*
```

## 🔧 **RÈGLES OBLIGATOIRES**

### **❌ JAMAIS inventer d'informations**
1. **UNIQUEMENT poser des questions** et attendre les réponses de Samy
2. **ÉCRIRE EXACTEMENT** ce que Samy explique, rien d'autre  
3. **Si je ne connais pas un projet** → consulter `.cursor/` pour comprendre

### **🤔 Communication intelligente :**
1. **TOUJOURS demander la vidéo Loom** 
2. **INSISTER sur les détails** - "sois très précis", "quels fichiers EXACTS"
3. **CREUSER les cas particuliers** - "y a-t-il des pièges ?"
4. **IDENTIFIER ce qui existe déjà**
5. **CLARIFIER les points critiques**

---

## 🚨 **DIFFICULTÉS RENCONTRÉES & SOLUTIONS**

### **📍 Problème 1 : Publication GitHub API**
**Erreur rencontrée :** `title is too long (maximum is 256 characters)`
**Cause :** L'argument du contenu était interprété comme le titre
**Solution :** Utiliser la syntaxe correcte pour update :
```bash
python3 github-api.py update sass [numero] "" "$(cat fichier.md)"
```
- **Titre vide** ("") en 4ème position 
- **Body du markdown** en 5ème position
- **Ordre crucial** : [repo] [number] [title] [body]

### **📍 Problème 2 : Gestion des Drafts**
**Apprentissage :** TOUJOURS sauvegarder dans `drafts/` avant publication
**Workflow correct :**
1. ✅ Créer le draft : `.agentova-tools/drafts/issue-[numero]-nom.md`
2. ✅ Validation utilisateur
3. ✅ Publication avec `github-api.py update`

### **📍 Problème 3 : Consultation Architecture**
**Apprentissage :** Utiliser `fetch_rules` pour comprendre les projets
**Pattern obligatoire :**
```
fetch_rules(["api-agent-agentova-ai/agentova-architecture", 
             "sass-agentova-ai/agentova-backend", 
             "sass-agentova-ai/agentova-frontend"])
```

### **📍 Problème 4 : Identification des Fichiers Exacts**
**Difficulté :** Identifier précisément les classes/fichiers à modifier
**Solution :** Utiliser `codebase_search` + `read_file` en parallèle :
```
codebase_search("How are callbacks implemented?", ["api-agent-agentova-ai"])
codebase_search("Where are custom agent modules?", ["sass-agentova-ai/client"])
```

### **📍 Problème 5 : Compréhension Patterns Existants**
**Apprentissage :** Analyser les patterns existants AVANT de proposer la structure
**Exemples essentiels :**
- `socialScheduler.ts` pour les tâches programmées
- `campaignService.ts` pour les services
- `CustomAgentModule.tsx` pour l'interface

---

## 🔧 **AMÉLIORATIONS DU PROCESSUS**

### **✅ Questions Techniques Supplémentaires :**
17. **"As-tu regardé des exemples similaires dans le code existant ?"**
18. **"Quelle est la mécanique technique EXACTE que tu veux réutiliser ?"**
19. **"Y a-t-il des callbacks/hooks existants à modifier ou créer ?"**
20. **"Comment s'intègre cette feature avec l'architecture actuelle ?"**

### **✅ Workflow Obligatoire Amélioré :**
1. 🔍 **Consulter `.cursor/` rules** pour comprendre l'architecture
2. 🔍 **Analyser le code existant** avec `codebase_search`
3. 🤔 **Poser TOUTES les questions** de compréhension
4. 💾 **Sauvegarder dans drafts/** 
5. ✅ **Validation utilisateur**
6. 🚀 **Publication avec syntax correcte GitHub API**

### **✅ Format GitHub API Correct :**
```bash
# Pour mettre à jour uniquement le body (sans changer le titre)
python3 github-api.py update [repo] [numero] "" "$(cat .agentova-tools/drafts/fichier.md)"

# Pour créer une nouvelle issue
python3 github-api.py create [repo] "Titre" "$(cat .agentova-tools/drafts/fichier.md)"
```

---

## 🎯 **OBJECTIF : ZERO INVENTION - 100% QUESTIONS + ÉCRITURE**

Le développeur lit l'issue améliorée et comprend EXACTEMENT quoi faire grâce aux explications de Samy !