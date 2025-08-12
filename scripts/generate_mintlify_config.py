#!/usr/bin/env python3
"""
Generate Mintlify configuration based on processed tools
"""

import json

def generate_config():
    """Generate mint.json from processing results"""
    
    # Load processing results
    try:
        with open("_processing_results.json", "r") as f:
            results = json.load(f)
    except FileNotFoundError:
        print("❌ No processing results found")
        return
    
    # Base configuration
    config = {
        "$schema": "https://mintlify.com/schema.json",
        "name": "SpecterOps Documentation Hub",
        "logo": {
            "light": "/logo/light.png",
            "dark": "/logo/dark.png"
        },
        "favicon": "/favicon.ico",
        "colors": {
            "primary": "#FF4B4B",
            "light": "#FF6B6B", 
            "dark": "#E53E3E"
        },
        "topbarCtaButton": {
            "name": "SpecterOps",
            "url": "https://specterops.io"
        },
        "navigation": results.get("navigation", []),
        "footerSocials": {
            "github": "https://github.com/SpecterOps"
        },
        "search": {
            "prompt": "Search SpecterOps tools and documentation..."
        }
    }
    
    # Write configuration
    with open("mint.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Generated mint.json with {len(config['navigation'])} navigation groups")

if __name__ == "__main__":
    generate_config()