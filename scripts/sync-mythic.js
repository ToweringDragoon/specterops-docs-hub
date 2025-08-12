const fs = require('fs');
const path = require('path');
const { Octokit } = require('@octokit/rest');

class MythicSyncer {
  constructor(token) {
    this.octokit = new Octokit({ auth: token });
    this.repo = { owner: 'MythicMeta', repo: 'Mintlify_Documentation' };
    this.outputDir = './mythic';
  }

  async syncDocs() {
    console.log('🔮 Syncing Mythic documentation...');
    
    try {
      // Get the repository tree
      const { data: tree } = await this.octokit.rest.git.getTree({
        ...this.repo,
        tree_sha: 'main',
        recursive: true
      });

      // Filter for relevant files
      const docFiles = tree.tree.filter(item => 
        item.type === 'blob' && 
        (item.path.endsWith('.md') || 
         item.path.endsWith('.mdx') || 
         item.path === 'mint.json')
      );

      // Create output directory
      if (!fs.existsSync(this.outputDir)) {
        fs.mkdirSync(this.outputDir, { recursive: true });
      }

      // Process each file
      for (const file of docFiles) {
        await this.processFile(file);
      }

      console.log(`✅ Mythic sync complete. Processed ${docFiles.length} files.`);
    } catch (error) {
      console.error('❌ Mythic sync failed:', error);
      throw error;
    }
  }

  async processFile(file) {
    try {
      const { data: content } = await this.octokit.rest.git.getBlob({
        ...this.repo,
        file_sha: file.sha
      });

      const fileContent = Buffer.from(content.content, 'base64').toString('utf-8');
      
      let processedContent;
      if (file.path === 'mint.json') {
        processedContent = this.processMintConfig(fileContent);
      } else {
        processedContent = this.processMarkdown(fileContent, file.path);
      }
      
      const outputPath = path.join(this.outputDir, file.path);
      const outputDir = path.dirname(outputPath);
      
      if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
      }
      
      fs.writeFileSync(outputPath, processedContent);
      console.log(`📄 Processed: ${file.path}`);
    } catch (error) {
      console.error(`❌ Failed to process ${file.path}:`, error);
    }
  }

  processMarkdown(content, filePath) {
    let processed = content;

    // Add frontmatter if missing
    if (!processed.startsWith('---')) {
      const title = this.extractTitle(processed, filePath);
      processed = `---
title: "${title}"
description: "Mythic C2 Framework documentation"
icon: "wand-magic-sparkles"
---

${processed}`;
    }

    // Fix relative links to absolute GitHub links
    processed = processed.replace(
      /\]\((?!http|#)(.*?)\)/g,
      '](https://github.com/MythicMeta/Mintlify_Documentation/blob/main/$1)'
    );

    // Fix image links
    processed = processed.replace(
      /!\[(.*?)\]\((?!http)(.*?)\)/g,
      '![$1](https://raw.githubusercontent.com/MythicMeta/Mintlify_Documentation/main/$2)'
    );

    return processed;
  }

  processMintConfig(content) {
    const config = JSON.parse(content);
    
    // Adapt configuration for subdirectory
    const adaptedConfig = {
      ...config,
      navigation: this.adaptNavigation(config.navigation || [])
    };

    return JSON.stringify(adaptedConfig, null, 2);
  }

  adaptNavigation(nav) {
    return nav.map(item => {
      if (typeof item === 'string') {
        return `mythic/${item}`;
      }
      if (item.pages) {
        return {
          ...item,
          pages: this.adaptNavigation(item.pages)
        };
      }
      return item;
    });
  }

  extractTitle(content, filePath) {
    // Try to extract title from first heading
    const headingMatch = content.match(/^#\s+(.+)$/m);
    if (headingMatch) return headingMatch[1];
    
    // Fallback to filename
    return path.basename(filePath, path.extname(filePath))
      .replace(/[-_]/g, ' ')
      .replace(/\b\w/g, l => l.toUpperCase());
  }
}

// Run the sync
const syncer = new MythicSyncer(process.env.GITHUB_TOKEN);
syncer.syncDocs().catch(console.error);