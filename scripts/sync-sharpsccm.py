import os
import requests
import json
import re
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class SharpSCCMSyncer:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {token}',
            'User-Agent': 'SpecterOps-Doc-Syncer'
        })
        self.base_url = 'https://github.com/Mayyhem/SharpSCCM/wiki'
        self.api_url = 'https://api.github.com/repos/Mayyhem/SharpSCCM'
        self.output_dir = Path('./sharpsccm')

    def sync_docs(self):
        print('🔨 Syncing SharpSCCM wiki...')
        
        try:
            # Create output directory
            self.output_dir.mkdir(exist_ok=True)
            
            # Get wiki pages
            wiki_pages = self.get_wiki_pages()
            
            # Process each page
            for page in wiki_pages:
                self.process_wiki_page(page)
            
            # Create navigation file
            self.create_navigation(wiki_pages)
            
            print(f'✅ SharpSCCM sync complete. Processed {len(wiki_pages)} pages.')
            
        except Exception as e:
            print(f'❌ SharpSCCM sync failed: {e}')
            raise

    def get_wiki_pages(self):
        """Get all wiki pages from the GitHub API"""
        try:
            response = self.session.get(f'{self.api_url}/wiki/pages')
            if response.status_code == 200:
                return response.json()
            else:
                # Fallback: scrape the wiki main page for links
                return self.scrape_wiki_pages()
        except:
            return self.scrape_wiki_pages()

    def scrape_wiki_pages(self):
        """Scrape wiki pages if API is unavailable"""
        print('📄 Scraping wiki pages from web interface...')
        
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        pages = []
        
        # Look for wiki navigation or page list
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '/wiki/' in href and href != '/wiki/':
                page_name = href.split('/wiki/')[-1]
                if page_name and page_name not in ['Home', '_history']:
                    pages.append({
                        'title': page_name.replace('-', ' '),
                        'url': f'{self.base_url}/{page_name}',
                        'filename': f'{page_name.lower()}.md'
                    })
        
        # Always include Home page
        pages.insert(0, {
            'title': 'Home',
            'url': self.base_url,
            'filename': 'index.md'
        })
        
        return pages

    def process_wiki_page(self, page):
        """Process a single wiki page"""
        try:
            if 'url' in page:
                url = page['url']
            else:
                url = f"{self.base_url}/{page.get('title', 'Home')}"
            
            print(f'📄 Processing: {page.get("title", "Unknown")}')
            
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the wiki content
            content_div = soup.find('div', {'id': 'wiki-content'}) or \
                         soup.find('div', {'class': 'markdown-body'}) or \
                         soup.find('article')
            
            if not content_div:
                print(f'⚠️  No content found for {page.get("title")}')
                return
            
            # Convert HTML to Markdown
            markdown_content = self.html_to_markdown(content_div, page)
            
            # Write to file
            filename = page.get('filename', f"{page.get('title', 'unknown').lower().replace(' ', '-')}.md")
            filepath = self.output_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            print(f'✅ Saved: {filename}')
            
        except Exception as e:
            print(f'❌ Failed to process {page.get("title")}: {e}')

    def html_to_markdown(self, content_div, page):
        """Convert HTML content to Markdown with proper frontmatter"""
        
        # Extract text content and basic formatting
        markdown_lines = []
        
        # Add frontmatter
        title = page.get('title', 'SharpSCCM Documentation')
        markdown_lines.extend([
            '---',
            f'title: "{title}"',
            'description: "SharpSCCM post-exploitation tool documentation"',
            'icon: "hammer"',
            '---',
            ''
        ])
        
        # Process content
        for element in content_div.children:
            if hasattr(element, 'name'):
                md_line = self.convert_element_to_markdown(element)
                if md_line:
                    markdown_lines.append(md_line)
        
        return '\n'.join(markdown_lines)

    def convert_element_to_markdown(self, element):
        """Convert HTML element to Markdown"""
        if not hasattr(element, 'name'):
            text = str(element).strip()
            return text if text else None
        
        tag = element.name.lower()
        text = element.get_text().strip()
        
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            return f"{'#' * level} {text}"
        
        elif tag == 'p':
            # Handle paragraphs with potential formatting
            return self.process_paragraph(element)
        
        elif tag == 'ul':
            items = []
            for li in element.find_all('li'):
                items.append(f"- {li.get_text().strip()}")
            return '\n'.join(items)
        
        elif tag == 'ol':
            items = []
            for i, li in enumerate(element.find_all('li'), 1):
                items.append(f"{i}. {li.get_text().strip()}")
            return '\n'.join(items)
        
        elif tag == 'code':
            return f"`{text}`"
        
        elif tag == 'pre':
            code_element = element.find('code')
            if code_element:
                return f"```\n{code_element.get_text()}\n```"
            return f"```\n{text}\n```"
        
        elif tag == 'a':
            href = element.get('href', '#')
            # Convert relative links to absolute GitHub links
            if href.startswith('/'):
                href = f"https://github.com/Mayyhem/SharpSCCM{href}"
            return f"[{text}]({href})"
        
        elif tag == 'strong' or tag == 'b':
            return f"**{text}**"
        
        elif tag == 'em' or tag == 'i':
            return f"*{text}*"
        
        elif tag == 'blockquote':
            return f"> {text}"
        
        return text if text else None

    def process_paragraph(self, p_element):
        """Process paragraph with mixed content"""
        result = []
        
        for child in p_element.children:
            if hasattr(child, 'name'):
                if child.name == 'a':
                    href = child.get('href', '#')
                    if href.startswith('/'):
                        href = f"https://github.com/Mayyhem/SharpSCCM{href}"
                    result.append(f"[{child.get_text()}]({href})")
                elif child.name == 'code':
                    result.append(f"`{child.get_text()}`")
                elif child.name == 'strong':
                    result.append(f"**{child.get_text()}**")
                elif child.name == 'em':
                    result.append(f"*{child.get_text()}*")
                else:
                    result.append(child.get_text())
            else:
                result.append(str(child))
        
        return ''.join(result).strip()

    def create_navigation(self, pages):
        """Create navigation structure for Mintlify"""
        nav_structure = {
            "name": "SharpSCCM",
            "navigation": [
                {
                    "group": "Getting Started",
                    "pages": []
                },
                {
                    "group": "Documentation",
                    "pages": []
                }
            ]
        }
        
        # Organize pages
        for page in pages:
            filename = page.get('filename', f"{page.get('title', '').lower()}.md")
            page_path = f"sharpsccm/{filename.replace('.md', '')}"
            
            title = page.get('title', '')
            if title.lower() in ['home', 'index', 'getting started']:
                nav_structure["navigation"][0]["pages"].append(page_path)
            else:
                nav_structure["navigation"][1]["pages"].append(page_path)
        
        # Save navigation
        with open(self.output_dir / 'navigation.json', 'w') as f:
            json.dump(nav_structure, f, indent=2)

if __name__ == "__main__":
    import sys
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print('❌ GITHUB_TOKEN environment variable required')
        sys.exit(1)
    
    syncer = SharpSCCMSyncer(token)
    syncer.sync_docs()