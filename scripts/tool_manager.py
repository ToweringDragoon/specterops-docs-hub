#!/usr/bin/env python3
"""
Tool Manager - Orchestrates processing of all tools
"""

import importlib.util
import json
from pathlib import Path

# Tool configuration - add new tools here
TOOLS = [
    {
        "name": "sharpsccm",
        "processor": "sharpsccm_processor",
        "enabled": True
    }
    # Add new tools like this:
    # {
    #     "name": "mythic",
    #     "processor": "mythic_processor", 
    #     "enabled": True
    # }
]

def process_all_tools():
    """Process all enabled tools"""
    
    results = []
    scripts_dir = Path(__file__).parent
    
    # Clear docs directory
    docs_dir = Path("docs")
    if docs_dir.exists():
        import shutil
        shutil.rmtree(docs_dir)
    
    print("🔄 Processing all enabled tools...\n")
    
    for tool_config in TOOLS:
        if not tool_config["enabled"]:
            print(f"⏭️  Skipping {tool_config['name']} (disabled)")
            continue
        
        processor_name = tool_config["processor"]
        processor_file = scripts_dir / f"{processor_name}.py"
        
        if not processor_file.exists():
            print(f"❌ Processor not found: {processor_file}")
            continue
        
        # Load and run the processor
        try:
            spec = importlib.util.spec_from_file_location(processor_name, processor_file)
            processor_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(processor_module)
            
            # Run the processor
            result = processor_module.process()
            results.append(result)
            
        except Exception as e:
            print(f"❌ Error processing {tool_config['name']}: {e}")
            results.append({
                "tool": {"name": tool_config['name']},
                "success": False,
                "error": str(e)
            })
    
    # Generate summary
    print(f"\n📊 Processing Summary:")
    successful = [r for r in results if r.get("success", False)]
    failed = [r for r in results if not r.get("success", False)]
    
    print(f"  ✅ Successful: {len(successful)}")
    print(f"  ❌ Failed: {len(failed)}")
    
    for result in successful:
        tool_name = result["tool"]["name"]
        page_count = len(result.get("pages", []))
        print(f"    - {tool_name}: {page_count} pages")
    
    # Save results for the workflow
    save_results(results)
    
    return results

def save_results(results):
    """Save processing results for workflow use"""
    
    # Create navigation structure
    navigation = []
    
    for result in results:
        if not result.get("success", False):
            continue
        
        tool = result["tool"]
        pages = result.get("pages", [])
        
        if pages:
            # Group by category if we have it
            category = tool.get("category", "tools")
            category_title = category.replace("-", " ").title()
            
            # Find or create category group
            category_group = None
            for group in navigation:
                if group["group"] == category_title:
                    category_group = group
                    break
            
            if not category_group:
                category_group = {
                    "group": category_title,
                    "pages": []
                }
                navigation.append(category_group)
            
            # Add pages to category
            category_group["pages"].extend(pages)
    
    # Save navigation config
    config = {
        "navigation": navigation,
        "tools_processed": len([r for r in results if r.get("success", False)]),
        "total_pages": sum(len(r.get("pages", [])) for r in results if r.get("success", False))
    }
    
    with open("_processing_results.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"\n💾 Saved processing results: {config['tools_processed']} tools, {config['total_pages']} pages")

if __name__ == "__main__":
    process_all_tools()