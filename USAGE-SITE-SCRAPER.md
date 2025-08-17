# 📥 Site Scraper - Usage Simple

## 🎯 **Objectif**
Script simple pour télécharger toutes les pages HTML d'un site web (utile pour récupérer de la documentation).

## 🚀 **Usage Rapide**

### **Installation des dépendances:**
```bash
cd .agentova-tools
pip install -r requirements.txt
```

### **Usage basique:**
```bash
# Télécharger toutes les pages d'un site
python site-scraper.py https://example.com

# Avec dossier de sortie personnalisé
python site-scraper.py https://docs.example.com --output-dir ./doc-pages

# Limiter le nombre de pages
python site-scraper.py https://example.com --max-pages 50

# Avec délai plus long (respectueux)
python site-scraper.py https://example.com --delay 2.0
```

## ⚙️ **Options Disponibles**

| Option | Court | Défaut | Description |
|--------|-------|--------|-------------|
| `--output-dir` | `-o` | `./downloaded-pages` | Dossier où sauvegarder les pages HTML |
| `--max-pages` | `-m` | `100` | Nombre maximum de pages à télécharger |
| `--delay` | `-d` | `1.0` | Délai entre chaque requête (en secondes) |

## 📁 **Résultat**

Le script crée un dossier avec:
- **Fichiers HTML** : Une page = un fichier `.html`
- **Noms sécurisés** : URLs converties en noms de fichiers valides
- **Index pour homepage** : La page d'accueil devient `index.html`
- **Pas de doublons** : Auto-numérotation si conflits

## 🔧 **Exemple Concret**

```bash
# Télécharger la documentation de Google ADK
python site-scraper.py https://cloud.google.com/vertex-ai/generative-ai/docs/adk/python --output-dir ./google-adk-docs --max-pages 200 --delay 1.5
```

**Résultat:**
```
./google-adk-docs/
├── index.html
├── getting-started.html
├── api-reference.html
├── examples.html
└── ...
```

## ⚠️ **Filtres Automatiques**

Le script ignore automatiquement:
- **Autres domaines** (reste sur le même site)
- **Fichiers binaires** : PDF, images, archives, etc.
- **Ressources** : CSS, JavaScript

## 🎯 **Cas d'Usage Parfaits**

✅ **Documentation techniques**  
✅ **Sites de knowledge base**  
✅ **Wikis internes**  
✅ **Blogs techniques**  

---

**Prêt à télécharger ! Donne-moi juste l'URL du site 🚀**
