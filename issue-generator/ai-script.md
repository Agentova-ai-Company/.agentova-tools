# 🤖 SCRIPT IA - CRÉATION D'ISSUES AGENTOVA

## 🎯 **ACTIVATION SIMPLE**

### **Mode unique : Création de nouvelles issues**
`@issue-create` - Aide à créer une nouvelle issue en posant les bonnes questions et en générant le fichier draft

## 🚀 **PROCESSUS : QUESTIONS + ÉCRITURE + SAUVEGARDE**

## 🤔 **1. QUESTIONS OBLIGATOIRES POUR CRÉER UNE ISSUE**

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

### **Questions Techniques Supplémentaires :**
17. **"As-tu regardé des exemples similaires dans le code existant ?"**
18. **"Quelle est la mécanique technique EXACTE que tu veux réutiliser ?"**
19. **"Y a-t-il des callbacks/hooks existants à modifier ou créer ?"**
20. **"Comment s'intègre cette feature avec l'architecture actuelle ?"**

## 📝 **2. ÉCRITURE EXACTE DES RÉPONSES**

**RÈGLE ABSOLUE** : ✅ ÉCRIRE UNIQUEMENT ce que Samy dit ✅

### **OBLIGATOIRE : Sauvegarde dans drafts/**
**Format du fichier** : `.agentova-tools/issue-generator/drafts/[titre-court].md`

```markdown
# [TITRE DE L'ISSUE]

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
*Issue créée le [DATE] avec les explications*
```

## 🔧 **3. WORKFLOW OBLIGATOIRE**

### **Étapes à suivre EXACTEMENT :**
1. 🔍 **Consulter `.cursor/` rules** pour comprendre l'architecture si nécessaire
2. 🔍 **Analyser le code existant** avec `codebase_search` si nécessaire
3. 🤔 **Poser TOUTES les questions** de compréhension (1 à 20)
4. 💾 **OBLIGATOIRE : Sauvegarder dans `.agentova-tools/issue-generator/drafts/`** 
5. ✅ **Validation utilisateur du draft**
6. 🔄 **Modifications possibles du fichier draft**
7. ✅ **TERMINÉ - Pas de publication automatique**

### **RÈGLE CRITIQUE : DRAFTS UNIQUEMENT**
- ✅ **TOUJOURS** créer le fichier dans `drafts/` 
- ✅ **Format .md** pour le draft
- ✅ **Permettre modifications** du fichier draft
- ✅ **PAS de publication automatique** - Seulement génération du fichier

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

### **💾 Gestion des fichiers drafts :**
1. **OBLIGATOIRE** : Sauvegarder dans `drafts/` après avoir posé toutes les questions
2. **Format de nom** : `[titre-court].md`
3. **Permettre modifications** du fichier draft par l'utilisateur
4. **TERMINÉ** - Pas de publication, juste génération du fichier

---

## 🚨 **DIFFICULTÉS RENCONTRÉES & SOLUTIONS**

### **📍 Problème 1 : Format des fichiers**
**Règle :** Utiliser un format de nom simple et clair
**Solution :** Format simplifié pour les drafts :
```
.agentova-tools/issue-generator/drafts/[titre-court].md
```
- **Nom simple** : Pas de date, juste le titre court
- **Extension .md** obligatoire
- **Pas de publication** automatique

### **📍 Problème 2 : Gestion des Drafts**
**Apprentissage :** TOUJOURS sauvegarder dans `drafts/` 
**Workflow correct :**
1. ✅ Créer le draft : `.agentova-tools/issue-generator/drafts/[titre-court].md`
2. ✅ Validation utilisateur
3. ✅ Modifications possibles du draft
4. ✅ TERMINÉ - Pas de publication automatique

### **📍 Problème 3 : Consultation Architecture**
**Apprentissage :** Utiliser `fetch_rules` pour comprendre les projets
**Pattern obligatoire :**
```
fetch_rules(["api-agent-agentova-ai/README", 
             "sass-agentova-ai/README"])
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

## 🎯 **OBJECTIF : ZERO INVENTION - 100% QUESTIONS + ÉCRITURE + DRAFTS UNIQUEMENT**

L'IA pose toutes les questions, écrit exactement ce que Samy explique dans un fichier draft, permet les modifications, et c'est TERMINÉ ! Pas de publication automatique sur GitHub.