const fs = require('fs');
const path = require('path');
const { Octokit } = require('@octokit/rest');

class BloodHoundSyncer {
  constructor(token) {
    this.octokit = new Octokit({ auth: token });
    this.repo = { owner: 'SpecterOps', repo: 'bloodhound-docs' };
    this.outputDir = './bloodhound';
  }

  async syncDocs() {
    console.log('🩸 Syncing BloodHound documentation...');
    
    try {
      // Get the repository tree
      const { data: tree } = await this.octokit.rest.git.getTree({
        ...this.repo,
        tree_sha: 'main',
        recursive: true
      });

      // Filter for .md and .mdx files
      const docFiles = tree.tree.filter(item => 
        item.type === 'blob' && 
        (item.path.endsWith('.md') || item.path.endsWith('.mdx'))
      );

      // Create output directory
      if (!fs.existsSync(this.outputDir)) {
        fs.mkdirSync(this.outputDir, { recursive: true });
      }

      // Process each file
      for (const file of docFiles) {
        await this.processFile(file);
      }

      // Get and process Mintlify config if exists
      await this.processMintConfig();

      console.log(`✅ BloodHound sync complete. Processed ${docFiles.length} files.`);
    } catch (error) {
      console.error('❌ BloodHound sync failed:', error);
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
      const processedContent = this.processMarkdown(fileContent, file.path);
      
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

  async processMintConfig() {
    try {
      const { data: content } = await this.octokit.rest.repos.getContent({
        ...this.repo,
        path: 'mint.json'
      });

      if (content.type === 'file') {
        const config = JSON.parse(Buffer.from(content.content, 'base64').toString('utf-8'));
        const adaptedConfig = this.adaptMintConfig(config, 'bloodhound');
        
        fs.writeFileSync(
          path.join(this.outputDir, 'mint.json'),
          JSON.stringify(adaptedConfig, null, 2)
        );
      }
    } catch (error) {
      console.log('ℹ️  No mint.json found in BloodHound docs');
    }
  }

  processMarkdown(content, filePath) {
    // Add BloodHound-specific processing
    let processed = content;

    // Add frontmatter if missing
    if (!processed.startsWith('---')) {
      const title = this.extractTitle(processed, filePath);
      processed = `---
title: "${title}"
description: "BloodHound documentation"
icon: "droplet"
---

${processed}`;
    }

    // Fix relative links to absolute GitHub links
    processed = processed.replace(
      /\]\((?!http|#)(.*?)\)/g,
      '](https://github.com/SpecterOps/bloodhound-docs/blob/main/$1)'
    );

    // Fix image links
    processed = processed.replace(
      /!\[(.*?)\]\((?!http)(.*?)\)/g,
      '![$1](https://raw.githubusercontent.com/SpecterOps/bloodhound-docs/main/$2)'
    );

    return processed;
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

  adaptMintConfig(config, prefix) {
    // Adapt navigation paths for subdirectory
    const adaptNavigation = (nav) => {
      return nav.map(item => {
        if (typeof item === 'string') {
          return `${prefix}/${item}`;
        }
        if (item.pages) {
          return {
            ...item,
            pages: adaptNavigation(item.pages)
          };
        }
        return item;
      });
    };

    return {
      ...config,
      navigation: adaptNavigation(config.navigation || [])
    };
  }
}

// Run the sync
const syncer = new BloodHoundSyncer(process.env.GITHUB_TOKEN);
syncer.syncDocs().catch(console.error);