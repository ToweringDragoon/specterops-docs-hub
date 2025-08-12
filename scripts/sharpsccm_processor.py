#!/usr/bin/env python3
"""
SharpSCCM Documentation Processor
Processes the SharpSCCM GitHub wiki into Mintlify format
"""

import subprocess
import yaml
import re
from pathlib import Path
import os
import json

def process():
    """Main processing function for SharpSCCM"""
    
    tool_info = {
        "name": "SharpSCCM",
        "category": "utilities",
        "repo": "Mayyhem/SharpSCCM",
        "description": "Post-exploitation tool for Microsoft SCCM"
    }
    
    print(f"Processing {tool_info['name']}...")
    
    # Create directory
    tool_dir = Path(f"docs/{tool_info['category']}/sharpsccm")
    tool_dir.mkdir(parents=True, exist_ok=True)
    
    # Process the wiki
    pages = process_wiki(tool_info, tool_dir)
    
    if pages:
        print(f"✅ Successfully processed {len(pages)} pages")
        return {
            "tool": tool_info,
            "pages": pages,
            "success": True
        }
    else:
        print("❌ Failed to process wiki")
        return {
            "tool": tool_info,
            "pages": [],
            "success": False
        }

def process_wiki(tool_info, tool_dir):
    """Process the GitHub wiki"""
    
    wiki_url = f"https://github.com/{tool_info['repo']}.wiki.git"
    clone_dir = "temp_sharpsccm_wiki"
    
    try:
        # Clone wiki
        result = subprocess.run([
            'git', 'clone', wiki_url, clone_dir
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"  No wiki found or clone failed")
            return []
        
        wiki_path = Path(clone_dir)
        md_files = list(wiki_path.glob("*.md"))
        
        if not md_files:
            return []
        
        print(f"  Found {len(md_files)} wiki pages")
        
        # Process each page
        pages = []
        for md_file in md_files:
            page_path = process_wiki_page(md_file, tool_dir, tool_info)
            if page_path:
                pages.append(page_path)
        
        # Cleanup
        subprocess.run(['rm', '-rf', clone_dir], check=False)
        
        return pages
        
    except Exception as e:
        print(f"  Error processing wiki: {e}")
        if os.path.exists(clone_dir):
            subprocess.run(['rm', '-rf', clone_dir], check=False)
        return []

def process_wiki_page(md_file, tool_dir, tool_info):
    """Process a single wiki page"""
    
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Map wiki filenames to clean URLs
        filename_mapping = {
            "Home.md": ("index", "SharpSCCM"),
            "Command-Line-Usage.md": ("command-line-usage", "Command Line Usage"),
            "local.md": ("local", "Local Commands"),
            "get.md": ("get", "Get Commands"),
            "invoke.md": ("invoke", "Invoke Commands"),
            "exec.md": ("exec", "Exec Commands")
        }
        
        if md_file.name in filename_mapping:
            output_name, title = filename_mapping[md_file.name]
        else:
            # Fallback for any new pages
            clean_name = re.sub(r'[^\w\s-]', '', md_file.stem)
            clean_name = clean_name.strip().lower().replace(' ', '-')
            output_name = clean_name
            title = md_file.stem.replace('-', ' ').replace('_', ' ')
        
        # Fix wiki links
        content = fix_wiki_links(content)
        
        # Fix image links
        content = fix_image_links(content, tool_info['repo'])
        
        # Create frontmatter
        frontmatter = {
            "title": title,
            "description": f"SharpSCCM - {title}"
        }
        
        # Write the file
        output_file = tool_dir / f"{output_name}.md"
        write_markdown_file(output_file, frontmatter, content)
        
        print(f"    Created: {output_name}.md")
        return f"docs/{tool_info['category']}/sharpsccm/{output_name}"
        
    except Exception as e:
        print(f"    Error processing {md_file.name}: {e}")
        return None

def fix_wiki_links(content):
    """Fix [[Wiki Links]] to proper markdown links"""
    
    def fix_link(match):
        page_name = match.group(1)
        
        # Map known links
        link_mapping = {
            "Home": "./index",
            "Command Line Usage": "./command-line-usage",
            "Command-Line-Usage": "./command-line-usage",
            "local": "./local",
            "get": "./get",
            "invoke": "./invoke",
            "exec": "./exec"
        }
        
        if page_name in link_mapping:
            return f"[{page_name}]({link_mapping[page_name]})"
        else:
            # Default conversion
            clean_link = re.sub(r'[^\w\s-]', '', page_name)
            clean_link = clean_link.strip().lower().replace(' ', '-')
            return f"[{page_name}](./{clean_link})"
    
    return re.sub(r'\[\[([^\]]+)\]\]', fix_link, content)

def fix_image_links(content, repo):
    """Fix relative image links to point to GitHub"""
    
    return re.sub(
        r'!\[([^\]]*)\]\((?!https?)([^)]+)\)',
        rf'![\1](https://github.com/{repo}/wiki/\2)',
        content
    )

def write_markdown_file(file_path, frontmatter, content):
    """Write markdown file with frontmatter"""
    
    yaml_content = yaml.dump(frontmatter, default_flow_style=False)
    full_content = f"---\n{yaml_content}---\n\n{content}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

if __name__ == "__main__":
    result = process()
    if result["success"]:
        print(f"✅ {result['tool']['name']} processed successfully")
    else:
        print(f"❌ {result['tool']['name']} processing failed")