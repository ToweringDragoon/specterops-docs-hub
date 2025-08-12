import json
import subprocess
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import re
import yaml
import os

class RealisticDocsProcessor:
    def __init__(self):
        # Realistic tool configuration - focus on what actually works
        self.tools_config = {
            "core-platforms": [
                {
                    "name": "BloodHound Community Edition",
                    "repo": "SpecterOps/BloodHound",
                    "source_type": "github_readme_plus",  # README + docs folder
                    "docs_paths": ["README.md", "docs/"],
                    "external_link": "https://bloodhound.specterops.io",
                    "description": "Attack path analysis for Active Directory and Azure environments",
                    "subdomain": "bloodhound"
                },
                {
                    "name": "Ghostwriter",
                    "repo": "GhostManager/Ghostwriter",
                    "source_type": "github_readme_plus",
                    "docs_paths": ["README.md", "docs/"],
                    "external_link": "https://specterops.gitbook.io/ghostwriter",
                    "description": "Project management and reporting engine for red teams",
                    "subdomain": "ghostwriter"
                },
                {
                    "name": "Nemesis",
                    "repo": "SpecterOps/Nemesis",
                    "source_type": "github_wiki",  # This might actually work
                    "description": "Offensive data enrichment pipeline",
                    "subdomain": "nemesis"
                }
            ],
            "c2-frameworks": [
                {
                    "name": "Mythic C2",
                    "repo": "its-a-feature/Mythic",
                    "source_type": "github_readme_plus",
                    "docs_paths": ["README.md"],
                    "external_link": "https://docs.mythic-c2.net",
                    "description": "Multi-platform, collaborative red teaming C2 framework",
                    "subdomain": "mythic"
                }
            ],
            "utilities": [
                {
                    "name": "SharpSCCM",
                    "repo": "Mayyhem/SharpSCCM", 
                    "source_type": "github_wiki",  # Try wiki, fallback to README
                    "description": "Post-exploitation tool for Microsoft SCCM"
                },
                {
                    "name": "SharpHound",
                    "repo": "BloodHoundAD/SharpHound",
                    "source_type": "github_readme_plus",
                    "docs_paths": ["README.md"],
                    "description": "Official data collector for BloodHound",
                    "subdomain": "sharphound"
                }
            ]
        }
    
    def process_all_tools(self):
        """Process all tools with realistic expectations"""
        all_tools = {}
        
        for category, tools in self.tools_config.items():
            print(f"\n🔄 Processing category: {category}")
            
            for tool_config in tools:
                print(f"  📋 Processing {tool_config['name']}...")
                
                safe_name = re.sub(r'[^\w\-]', '_', tool_config['name'].lower()).replace(' ', '_')
                tool_dir = Path(f"docs/tools/{category}/{safe_name}")
                tool_dir.mkdir(parents=True, exist_ok=True)
                
                # Process based on what's actually feasible
                success = False
                
                if tool_config.get('source_type') == 'github_wiki':
                    success = self.try_github_wiki(tool_config, tool_dir)
                
                if not success:
                    # Fallback to reliable GitHub content
                    success = self.process_github_content(tool_config, tool_dir)
                
                if success:
                    all_tools[f"{category}/{safe_name}"] = {
                        "name": tool_config['name'],
                        "category": category
                    }
                    print(f"    ✅ Successfully processed")
                else:
                    print(f"    ❌ Failed to process")
        
        return all_tools
    
    def try_github_wiki(self, tool_config, tool_dir):
        """Try to process GitHub wiki - return True if successful"""
        repo = tool_config['repo']
        
        try:
            # Check if wiki exists by trying to clone it
            wiki_repo_url = f"https://github.com/{repo}.wiki.git"
            clone_dir = f"temp_wiki_{repo.split('/')[-1]}"
            
            result = subprocess.run([
                'git', 'clone', wiki_repo_url, clone_dir
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"    ⚠️  No wiki repository found")
                return False
            
            wiki_path = Path(clone_dir)
            md_files = list(wiki_path.glob("*.md"))
            
            if not md_files:
                print(f"    ⚠️  Wiki exists but no markdown files found")
                subprocess.run(['rm', '-rf', clone_dir], check=False)
                return False
            
            # Process wiki files
            for md_file in md_files:
                page_name = "index" if md_file.name == "Home.md" else md_file.stem.lower().replace(' ', '-')
                
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Basic cleanup
                content = self.clean_wiki_content(content, repo)
                
                # Create frontmatter
                title = md_file.stem.replace('-', ' ').replace('_', ' ')
                if title.lower() == "home":
                    title = tool_config['name']
                
                frontmatter = {
                    "title": f'"{title}"',
                    "description": f'"{title} - {tool_config["description"]}"'
                }
                
                # Write page
                self.write_page(tool_dir / f"{page_name}.md", frontmatter, content)
            
            subprocess.run(['rm', '-rf', clone_dir], check=False)
            print(f"    📄 Processed {len(md_files)} wiki pages")
            return True
            
        except Exception as e:
            print(f"    ❌ Error processing wiki: {e}")
            if os.path.exists(clone_dir):
                subprocess.run(['rm', '-rf', clone_dir], check=False)
            return False
    
    def process_github_content(self, tool_config, tool_dir):
        """Process GitHub repository content - reliable fallback"""
        repo = tool_config['repo']
        
        try:
            clone_dir = f"temp_{repo.split('/')[-1]}"
            subprocess.run([
                'git', 'clone', '--depth', '1',
                f'https://github.com/{repo}.git', clone_dir
            ], check=True, capture_output=True)
            
            docs_paths = tool_config.get('docs_paths', ['README.md'])
            content_parts = []
            
            # Process each documentation path
            for docs_path in docs_paths:
                source_path = Path(clone_dir) / docs_path
                
                if source_path.is_file():
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if content.strip():
                            content = self.fix_github_links(content, repo)
                            content_parts.append(content)
                
                elif source_path.is_dir():
                    # Process markdown files in docs directory
                    for md_file in source_path.rglob("*.md"):
                        try:
                            with open(md_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if content.strip():
                                    content = self.fix_github_links(content, repo)
                                    
                                    # Create section header
                                    section_name = md_file.stem.replace('-', ' ').replace('_', ' ').title()
                                    content_parts.append(f"## {section_name}\n\n{content}")
                        except:
                            continue
            
            if content_parts:
                # Create main documentation page
                frontmatter = {
                    "title": f'"{tool_config["name"]}"',
                    "description": f'"{tool_config["description"]}"'
                }
                
                # Add external link if available
                body = f"# {tool_config['name']}\n\n"
                
                if tool_config.get('external_link'):
                    body += f'<Card title="Complete Documentation" icon="external-link" href="{tool_config["external_link"]}">\n'
                    body += f'  View the full interactive documentation\n'
                    body += '</Card>\n\n'
                
                body += f'<Card title="GitHub Repository" icon="github" href="https://github.com/{repo}">\n'
                body += f'  {repo}\n'
                body += '</Card>\n\n'
                
                body += f"{tool_config['description']}\n\n"
                body += "\n\n".join(content_parts)
                
                self.write_page(tool_dir / "index.md", frontmatter, body)
                
                subprocess.run(['rm', '-rf', clone_dir], check=False)
                return True
            
        except Exception as e:
            print(f"    ❌ Error processing GitHub content: {e}")
            if os.path.exists(clone_dir):
                subprocess.run(['rm', '-rf', clone_dir], check=False)
        
        return False
    
    def clean_wiki_content(self, content, repo):
        """Clean up wiki content for better display"""
        # Convert [[Wiki Links]] to proper markdown
        def replace_wiki_link(match):
            page_name = match.group(1)
            safe_name = page_name.lower().replace(' ', '-').replace('_', '-')
            return f"[{page_name}](./{safe_name})"
        
        content = re.sub(r'\[\[([^\]]+)\]\]', replace_wiki_link, content)
        
        # Fix image links to point to GitHub
        repo_base = f"https://github.com/{repo}/wiki"
        content = re.sub(
            r'!\[([^\]]*)\]\((?!http)([^)]+)\)',
            rf'![\1]({repo_base}/\2)',
            content
        )
        
        return content
    
    def fix_github_links(self, content, repo):
        """Fix relative links in GitHub content"""
        repo_base = f"https://github.com/{repo}/blob/main"
        
        # Fix relative image links
        content = re.sub(
            r'!\[([^\]]*)\]\((?!http)([^)]+)\)',
            rf'![\1]({repo_base}/\2)',
            content
        )
        
        # Fix relative documentation links
        content = re.sub(
            r'\[([^\]]+)\]\((?!http)([^)]+\.md)\)',
            rf'[\1]({repo_base}/\2)',
            content
        )
        
        return content
    
    def write_page(self, file_path, frontmatter, content):
        """Write a page with frontmatter"""
        yaml_fm = yaml.dump(frontmatter, default_flow_style=False)
        full_content = f"---\n{yaml_fm}---\n\n{content}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

def main():
    """Main processing function"""
    processor = RealisticDocsProcessor()
    result = processor.process_all_tools()
    
    print(f"\n🎉 Processing complete!")
    print(f"Successfully processed {len(result)} tools")
    
    for tool_path, tool_data in result.items():
        print(f"  📁 {tool_data['name']}")

if __name__ == "__main__":
    main()