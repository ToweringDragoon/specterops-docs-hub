const fs = require('fs');
const path = require('path');

class NavigationUpdater {
  constructor() {
    this.mainConfigPath = './mint.json';
    this.toolsDir = ['./bloodhound', './mythic', './sharpsccm'];
  }

  updateMainNavigation() {
    console.log('🧭 Updating main navigation...');

    try {
      // Load main configuration
      const mainConfig = JSON.parse(fs.readFileSync(this.mainConfigPath, 'utf-8'));
      
      // Update navigation for each tool
      const updatedNavigation = [
        {
          "group": "Welcome",
          "pages": [
            "introduction",
            "quickstart"
          ]
        },
        {
          "group": "Tools Overview",
          "pages": [
            "tools/bloodhound",
            "tools/mythic", 
            "tools/sharpsccm"
          ]
        }
      ];

      // Add tool-specific navigation
      for (const toolDir of this.toolsDir) {
        const toolName = path.basename(toolDir);
        const toolNav = this.getToolNavigation(toolDir, toolName);
        
        if (toolNav && toolNav.length > 0) {
          updatedNavigation.push({
            "group": `${this.capitalize(toolName)} Documentation`,
            "pages": toolNav
          });
        }
      }

      // Update main config
      mainConfig.navigation = updatedNavigation;
      
      // Add tab configurations
      mainConfig.tabs = [
        {
          "name": "BloodHound",
          "url": "bloodhound"
        },
        {
          "name": "Mythic",
          "url": "mythic"
        },
        {
          "name": "SharpSCCM",
          "url": "sharpsccm"
        }
      ];

      // Write updated configuration
      fs.writeFileSync(this.mainConfigPath, JSON.stringify(mainConfig, null, 2));
      console.log('✅ Main navigation updated successfully');

    } catch (error) {
      console.error('❌ Failed to update navigation:', error);
      throw error;
    }
  }

  getToolNavigation(toolDir, toolName) {
    const navigation = [];
    
    try {
      if (!fs.existsSync(toolDir)) {
        console.log(`⚠️  Tool directory ${toolDir} not found`);
        return navigation;
      }

      // Check for tool-specific mint.json
      const toolMintPath = path.join(toolDir, 'mint.json');
      if (fs.existsSync(toolMintPath)) {
        const toolConfig = JSON.parse(fs.readFileSync(toolMintPath, 'utf-8'));
        return this.extractNavigationPages(toolConfig.navigation || [], toolName);
      }

      // Check for navigation.json (for wiki-based tools like SharpSCCM)
      const navPath = path.join(toolDir, 'navigation.json');
      if (fs.existsSync(navPath)) {
        const navConfig = JSON.parse(fs.readFileSync(navPath, 'utf-8'));
        return this.extractNavigationPages(navConfig.navigation || [], toolName);
      }

      // Fallback: scan for markdown files
      return this.scanForMarkdownFiles(toolDir, toolName);

    } catch (error) {
      console.error(`❌ Failed to get navigation for ${toolName}:`, error);
      return navigation;
    }
  }

  extractNavigationPages(navStructure, toolName) {
    const pages = [];
    
    const extractPages = (items, prefix = '') => {
      for (const item of items) {
        if (typeof item === 'string') {
          // Ensure proper prefixing
          const page = item.startsWith(toolName) ? item : `${toolName}/${item}`;
          pages.push(page);
        } else if (item.pages) {
          extractPages(item.pages, prefix);
        }
      }
    };

    extractPages(navStructure);
    return pages;
  }

  scanForMarkdownFiles(toolDir, toolName) {
    const pages = [];
    
    try {
      const files = this.getAllMarkdownFiles(toolDir);
      
      // Sort files to ensure consistent ordering
      files.sort((a, b) => {
        // Prioritize index files
        if (a.includes('index') || a.includes('home')) return -1;
        if (b.includes('index') || b.includes('home')) return 1;
        return a.localeCompare(b);
      });

      for (const file of files) {
        const relativePath = path.relative(toolDir, file);
        const pagePath = `${toolName}/${relativePath.replace(/\.mdx?$/, '')}`;
        pages.push(pagePath);
      }

    } catch (error) {
      console.error(`❌ Failed to scan ${toolName} for markdown files:`, error);
    }

    return pages;
  }

  getAllMarkdownFiles(dir) {
    const files = [];
    
    const scanDir = (currentDir) => {
      const items = fs.readdirSync(currentDir, { withFileTypes: true });
      
      for (const item of items) {
        const fullPath = path.join(currentDir, item.name);
        
        if (item.isDirectory()) {
          scanDir(fullPath);
        } else if (item.name.endsWith('.md') || item.name.endsWith('.mdx')) {
          files.push(fullPath);
        }
      }
    };

    scanDir(dir);
    return files;
  }

  capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  generateTabConfigs() {
    console.log('📑 Generating tab configurations...');

    const tabConfigs = {
      bloodhound: this.generateTabConfig('bloodhound', 'BloodHound'),
      mythic: this.generateTabConfig('mythic', 'Mythic'),
      sharpsccm: this.generateTabConfig('sharpsccm', 'SharpSCCM')
    };

    // Write individual tab configs
    for (const [tool, config] of Object.entries(tabConfigs)) {
      const configPath = path.join(`./${tool}`, 'mint.json');
      const configDir = path.dirname(configPath);
      
      if (!fs.existsSync(configDir)) {
        fs.mkdirSync(configDir, { recursive: true });
      }
      
      // Merge with existing config if present
      let existingConfig = {};
      if (fs.existsSync(configPath)) {
        try {
          existingConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
        } catch (error) {
          console.warn(`⚠️  Failed to parse existing config for ${tool}:`, error);
        }
      }
      
      const mergedConfig = { ...existingConfig, ...config };
      fs.writeFileSync(configPath, JSON.stringify(mergedConfig, null, 2));
    }

    console.log('✅ Tab configurations generated');
  }

  generateTabConfig(tool, displayName) {
    const navigation = this.getToolNavigation(`./${tool}`, tool);
    
    return {
      "name": `${displayName} Documentation`,
      "navigation": [
        {
          "group": "Overview",
          "pages": navigation.slice(0, 3) // First few pages
        },
        {
          "group": "Documentation",
          "pages": navigation.slice(3) // Rest of the pages
        }
      ].filter(group => group.pages.length > 0)
    };
  }
}

// Run the updater
const updater = new NavigationUpdater();
updater.updateMainNavigation();
updater.generateTabConfigs();

console.log('🎯 Navigation update complete!');