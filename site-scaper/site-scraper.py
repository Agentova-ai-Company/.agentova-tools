#!/usr/bin/env python3
"""
Script simple pour télécharger toutes les pages d'un site web comme TEXTE PUR

Usage: 
  python site-scraper.py https://example.com [--output-dir ./downloaded-pages] [--max-pages 100] [--delay 1]

Fonctionnalités:
- Crawl récursif de toutes les pages d'un domaine
- Extraction TEXTE PUR (sans HTML, CSS, JS)
- Rate limiting configurable
- Gestion des erreurs simple
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import time
import argparse
import re
from pathlib import Path
from typing import Set, List
import logging

class SiteScraper:
    def __init__(self, base_url: str, output_dir: str = "./downloaded-pages", 
                 max_pages: int = 100, delay: float = 1.0,
                 required_path: str = None, excluded_paths: list = None):
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.output_dir = Path(output_dir)
        self.max_pages = max_pages
        self.delay = delay
        self.required_path = required_path  # Ex: "/docs/v3"
        self.excluded_paths = excluded_paths or []  # Ex: ["/docs/v3/sdks", "/docs/v3/notifications"]
        
        # État du scraping
        self.visited_urls: Set[str] = set()
        self.to_visit: List[str] = [base_url]
        self.failed_urls: List[str] = []
        self.downloaded_count = 0
        
        # Configuration
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Agentova Simple HTML Downloader 1.0'
        })
        
        # Setup logging
        self._setup_logging()
        
        # Créer dossier output
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def _setup_logging(self):
        """Configure le système de logging simple"""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def _is_valid_url(self, url: str) -> bool:
        """Vérifie si l'URL doit être téléchargée"""
        parsed = urlparse(url)
        
        # Même domaine uniquement
        if parsed.netloc != self.domain:
            return False
        
        # Vérifier le chemin requis (si spécifié)
        if self.required_path and not parsed.path.startswith(self.required_path):
            return False
        
        # Vérifier les chemins exclus
        for excluded_path in self.excluded_paths:
            if parsed.path.startswith(excluded_path):
                return False
        
        # Filtres simples d'extensions
        excluded_extensions = {'.pdf', '.zip', '.exe', '.dmg', '.jpg', '.png', '.gif', '.svg', '.ico', '.css', '.js'}
        if any(url.lower().endswith(ext) for ext in excluded_extensions):
            return False
        
        return True
    
    def _normalize_url(self, url: str) -> str:
        """Normalise une URL (supprime fragments)"""
        parsed = urlparse(url)
        # Supprime le fragment (#)
        normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        # Supprime trailing slash sauf pour root
        if normalized.endswith('/') and len(parsed.path) > 1:
            normalized = normalized[:-1]
        return normalized
    
    def _extract_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        """Extrait tous les liens valides d'une page"""
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href'].strip()
            if not href or href.startswith('#'):
                continue
            
            # Convertir en URL absolue
            absolute_url = urljoin(current_url, href)
            normalized_url = self._normalize_url(absolute_url)
            
            if self._is_valid_url(normalized_url) and normalized_url not in self.visited_urls:
                links.append(normalized_url)
        
        return list(set(links))  # Supprimer doublons
    
    def _extract_text_content(self, html_content: str) -> str:
        """Extrait uniquement le contenu principal du HTML (sans header/nav/footer)"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Supprimer complètement ces éléments
        for tag in soup.find_all(['script', 'style', 'noscript', 'iframe', 'embed', 'object']):
            tag.decompose()
        
        # Supprimer les éléments de navigation/header/footer mais de façon plus ciblée
        for unwanted in soup.select('header, nav, footer'):
            unwanted.decompose()
        
        # Supprimer seulement les éléments les plus évidents de navigation
        unwanted_selectors = [
            '[class*="navigation"]', '[class*="navbar"]', '[class*="sidebar"]', 
            '[id*="navigation"]', '[class*="breadcrumb"]'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()
        
        # Essayer de trouver le contenu principal de façon plus permissive
        main_content = (
            soup.find('main') or 
            soup.find('article') or 
            soup.find('div', class_=lambda x: x and 'content' in x.lower()) or
            soup.find('div', id=lambda x: x and 'content' in x.lower()) or
            soup.body or
            soup
        )
        
        # Extraire le texte
        text = main_content.get_text(separator='\n', strip=True)
        
        # Nettoyer le texte (supprimer lignes vides multiples)
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        return '\n'.join(lines)
    
    def _save_html_page(self, url: str, html_content: str):
        """Sauvegarde une page HTML nettoyée"""
        # Créer nom de fichier sûr à partir de l'URL
        url_path = urlparse(url).path
        if url_path == '/' or url_path == '':
            filename = 'index'
        else:
            filename = re.sub(r'[^\w\-_.]', '_', url_path.strip('/').replace('/', '_'))
        
        # Vérifier si le fichier existe déjà
        text_path = self.output_dir / f"{filename}.txt"
        if text_path.exists():
            self.logger.info(f"⏭️ Fichier existe déjà: {filename}.txt (ignoré)")
            return filename
        
        # Extraire texte pur
        text_content = self._extract_text_content(html_content)
        
        # Sauvegarder texte pur
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        self.logger.info(f"💾 Téléchargé (texte pur): {filename}.txt")
        return filename
    
    def download_page(self, url: str) -> bool:
        """Télécharge une page HTML"""
        try:
            # Vérifier si fichier existe déjà avant téléchargement
            url_path = urlparse(url).path
            if url_path == '/' or url_path == '':
                filename = 'index'
            else:
                filename = re.sub(r'[^\w\-_.]', '_', url_path.strip('/').replace('/', '_'))
            
            text_path = self.output_dir / f"{filename}.txt"
            if text_path.exists():
                self.logger.info(f"⏭️ URL déjà téléchargée: {url} (ignoré)")
                return True
            
            self.logger.info(f"📥 Téléchargement: {url}")
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Sauvegarder HTML
            self._save_html_page(url, response.text)
            self.downloaded_count += 1
            
            # Parser pour extraire liens
            soup = BeautifulSoup(response.content, 'html.parser')
            new_links = self._extract_links(soup, url)
            
            # Ajouter nouveaux liens à la liste
            for link in new_links:
                if link not in self.visited_urls and link not in self.to_visit:
                    self.to_visit.append(link)
            
            self.logger.info(f"✅ {url} - Trouvé {len(new_links)} nouveaux liens")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sur {url}: {e}")
            self.failed_urls.append(url)
            return False
    
    def run(self):
        """Lance le téléchargement complet"""
        self.logger.info(f"🚀 Début du téléchargement de {self.base_url}")
        self.logger.info(f"📁 Sortie: {self.output_dir}")
        self.logger.info(f"⚙️ Max pages: {self.max_pages}, Délai: {self.delay}s")
        
        while self.to_visit and self.downloaded_count < self.max_pages:
            url = self.to_visit.pop(0)
            
            if url in self.visited_urls:
                continue
            
            self.visited_urls.add(url)
            
            if self.download_page(url):
                pass  # Downloaded successfully
            
            # Rate limiting
            if self.delay > 0:
                time.sleep(self.delay)
            
            # Progression
            if self.downloaded_count % 10 == 0 and self.downloaded_count > 0:
                self.logger.info(f"📊 Progression: {self.downloaded_count}/{self.max_pages} pages, {len(self.to_visit)} en attente")
        
        # Résumé final
        self.logger.info(f"🎉 Téléchargement terminé!")
        self.logger.info(f"✅ Pages téléchargées: {self.downloaded_count}")
        self.logger.info(f"❌ Pages échouées: {len(self.failed_urls)}")
        self.logger.info(f"📁 Fichiers HTML dans: {self.output_dir}")
        
        if self.failed_urls:
            self.logger.info(f"❌ URLs échouées: {', '.join(self.failed_urls[:5])}{'...' if len(self.failed_urls) > 5 else ''}")

def main():
    parser = argparse.ArgumentParser(description='Téléchargeur simple de pages HTML')
    parser.add_argument('url', help='URL de base du site à télécharger')
    parser.add_argument('--output-dir', '-o', default='./downloaded-pages', 
                       help='Dossier de sortie (défaut: ./downloaded-pages)')
    parser.add_argument('--max-pages', '-m', type=int, default=100,
                       help='Nombre maximum de pages à télécharger (défaut: 100)')
    parser.add_argument('--delay', '-d', type=float, default=1.0,
                       help='Délai entre requêtes en secondes (défaut: 1.0)')
    parser.add_argument('--required-path', '-r', 
                       help='Chemin requis (ex: /docs/v3)')
    parser.add_argument('--exclude-paths', '-e', nargs='*', default=[],
                       help='Chemins à exclure (ex: /docs/v3/sdks /docs/v3/notifications)')
    
    args = parser.parse_args()
    
    # Validation URL
    if not args.url.startswith(('http://', 'https://')):
        args.url = 'https://' + args.url
    
    print(f"🔧 Configuration:")
    print(f"   URL: {args.url}")
    print(f"   Sortie: {args.output_dir}")
    print(f"   Max pages: {args.max_pages}")
    print(f"   Délai: {args.delay}s")
    if args.required_path:
        print(f"   Chemin requis: {args.required_path}")
    if args.exclude_paths:
        print(f"   Chemins exclus: {', '.join(args.exclude_paths)}")
    print()
    
    # Lancer téléchargeur
    scraper = SiteScraper(
        base_url=args.url,
        output_dir=args.output_dir,
        max_pages=args.max_pages,
        delay=args.delay,
        required_path=args.required_path,
        excluded_paths=args.exclude_paths
    )
    
    scraper.run()

if __name__ == '__main__':
    main()
