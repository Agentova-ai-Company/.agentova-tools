#!/usr/bin/env python3
"""
Script simple pour interagir avec GitHub API
Usage: python github-api.py [action] [options]
"""

import requests
import sys
import os
from dotenv import load_dotenv

# Charger automatiquement le fichier .env
load_dotenv()

# Configuration
GITHUB_OWNER = 'Agentova-ai-Company'  # Username GitHub en dur

# Projets Agentova
REPOS = {
    'sass': 'sass-agentova-ai',
    'api': 'api-agent-agentova-ai', 
    'widget': 'chat-widget-agentova-ai'
}

def get_headers():
    """Récupère les headers avec le token GitHub depuis .env"""
    github_token = os.environ.get('GITHUB_TOKEN')
    
    if not github_token:
        raise Exception("❌ Token GITHUB_TOKEN non trouvé dans .env")
    
    return {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/json'
    }

def list_issues(repo_key='sass', state='open'):
    """Liste les issues d'un repo"""
    owner = GITHUB_OWNER
        
    repo = REPOS.get(repo_key, repo_key)
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    
    params = {'state': state}
    response = requests.get(url, headers=get_headers(), params=params)
    
    if response.status_code == 200:
        issues = response.json()
        print(f"\n📋 Issues {state} pour {repo} ({len(issues)} issues):")
        print("=" * 80)
        
        for issue in issues:
            labels = [label['name'] for label in issue['labels']]
            assignees = [assignee['login'] for assignee in issue['assignees']] if issue['assignees'] else []
            
            print(f"\n🎫 Issue #{issue['number']}: {issue['title']}")
            print(f"   📅 Créée: {issue['created_at'][:10]} par {issue['user']['login']}")
            print(f"   📅 Modifiée: {issue['updated_at'][:10]}")
            print(f"   🏷️  Labels: {', '.join(labels) if labels else 'Aucun'}")
            print(f"   👤 Assigné(s): {', '.join(assignees) if assignees else 'Personne'}")
            print(f"   🔗 URL: {issue['html_url']}")
            
            # Description/Body
            if issue['body']:
                print(f"   📝 Description:")
                # Limiter la description pour l'affichage
                body_lines = issue['body'].strip().split('\n')
                for i, line in enumerate(body_lines[:10]):  # Max 10 lignes
                    print(f"      {line}")
                if len(body_lines) > 10:
                    print(f"      ... ({len(body_lines) - 10} lignes supplémentaires)")
            else:
                print(f"   📝 Description: Aucune")
            
            print("-" * 80)
    else:
        print(f"❌ Erreur {response.status_code}: {response.text}")

def create_issue(repo_key, title, body, labels=None, assignees=None):
    """Crée une nouvelle issue"""
    owner = GITHUB_OWNER
        
    repo = REPOS.get(repo_key, repo_key)
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    
    data = {
        'title': title,
        'body': body
    }
    
    if labels:
        data['labels'] = labels
    if assignees:
        data['assignees'] = assignees
    
    response = requests.post(url, headers=get_headers(), json=data)
    
    if response.status_code == 201:
        issue = response.json()
        print(f"✅ Issue créée: #{issue['number']} - {issue['title']}")
        print(f"   URL: {issue['html_url']}")
        return issue['number']
    else:
        print(f"❌ Erreur {response.status_code}: {response.text}")
        return None

def update_issue(repo_key, issue_number, title=None, body=None, labels=None, assignees=None):
    """Met à jour une issue existante"""
    owner = GITHUB_OWNER
        
    repo = REPOS.get(repo_key, repo_key)
    url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    
    data = {}
    if title:
        data['title'] = title
    if body:
        data['body'] = body
    if labels:
        data['labels'] = labels
    if assignees:
        data['assignees'] = assignees
    
    response = requests.patch(url, headers=get_headers(), json=data)
    
    if response.status_code == 200:
        issue = response.json()
        print(f"✅ Issue #{issue_number} mise à jour")
        return True
    else:
        print(f"❌ Erreur {response.status_code}: {response.text}")
        return False

def close_issue(repo_key, issue_number):
    """Ferme une issue"""
    owner = GITHUB_OWNER
        
    repo = REPOS.get(repo_key, repo_key)
    url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    
    data = {'state': 'closed'}
    response = requests.patch(url, headers=get_headers(), json=data)
    
    if response.status_code == 200:
        print(f"✅ Issue #{issue_number} fermée")
        return True
    else:
        print(f"❌ Erreur {response.status_code}: {response.text}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python github-api.py list [repo] [state]")
        print("  python github-api.py create [repo] [title] [body] [labels] [assignees]")
        print("  python github-api.py update [repo] [number] [title] [body] [labels] [assignees]")
        print("  python github-api.py close [repo] [number]")
        print("\nRepos disponibles: sass, api, widget")
        return
    
    action = sys.argv[1]
    
    # Test du token .env
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("❌ Token GITHUB_TOKEN non trouvé dans .env")
        print("Créez un fichier .env avec : GITHUB_TOKEN=votre_token_github")
        return
    
    if action == 'list':
        repo = sys.argv[2] if len(sys.argv) > 2 else 'sass'
        state = sys.argv[3] if len(sys.argv) > 3 else 'open'
        list_issues(repo, state)
    
    elif action == 'create':
        if len(sys.argv) < 5:
            print("Usage: python github-api.py create [repo] [title] [body]")
            return
        repo = sys.argv[2]
        title = sys.argv[3]
        body = sys.argv[4]
        labels = sys.argv[5].split(',') if len(sys.argv) > 5 else None
        assignees = sys.argv[6].split(',') if len(sys.argv) > 6 else None
        create_issue(repo, title, body, labels, assignees)
    
    elif action == 'update':
        if len(sys.argv) < 4:
            print("Usage: python github-api.py update [repo] [number] [title] [body]")
            return
        repo = sys.argv[2]
        number = int(sys.argv[3])
        title = sys.argv[4] if len(sys.argv) > 4 else None
        body = sys.argv[5] if len(sys.argv) > 5 else None
        update_issue(repo, number, title, body)
    
    elif action == 'close':
        if len(sys.argv) < 4:
            print("Usage: python github-api.py close [repo] [number]")
            return
        repo = sys.argv[2]
        number = int(sys.argv[3])
        close_issue(repo, number)
    
    else:
        print(f"Action inconnue: {action}")

if __name__ == '__main__':
    main()
