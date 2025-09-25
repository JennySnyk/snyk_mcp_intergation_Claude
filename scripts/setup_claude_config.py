#!/usr/bin/env python3
"""
Claude Desktop Configuration Setup Script for Snyk MCP Server

This script helps you configure Claude Desktop to work with the Snyk MCP server
by creating or updating the claude_desktop_config.json file.
"""

import json
import os
import sys
import platform
from pathlib import Path

def get_claude_config_path():
    """Get the path to Claude Desktop configuration file based on OS."""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif system == "Windows":
        return Path(os.environ.get("APPDATA", "")) / "Claude" / "claude_desktop_config.json"
    else:
        # Linux or other Unix-like systems
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"

def load_existing_config(config_path):
    """Load existing configuration or return empty dict."""
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️  Warning: Could not read existing config: {e}")
            return {}
    return {}

def save_config(config_path, config):
    """Save configuration to file."""
    # Create directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

def get_snyk_token():
    """Get Snyk token from user input or environment."""
    # Check environment variable first
    token = os.environ.get('SNYK_TOKEN')
    if token:
        print(f"🔑 Found Snyk token in environment variable")
        return token
    
    # Ask user for token
    print("\n🔑 Snyk API Token Required")
    print("You can find your token at: https://app.snyk.io/account")
    token = input("Enter your Snyk API token: ").strip()
    
    if not token:
        print("❌ Token is required to continue")
        sys.exit(1)
    
    return token

def main():
    print("🔧 Snyk MCP Server Configuration Setup for Claude Desktop")
    print("=" * 60)
    
    # Get configuration file path
    config_path = get_claude_config_path()
    print(f"📁 Configuration file: {config_path}")
    
    # Load existing configuration
    config = load_existing_config(config_path)
    
    # Initialize mcpServers if it doesn't exist
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    # Get Snyk token
    snyk_token = get_snyk_token()
    
    # Ask for additional configuration
    print("\n⚙️  Additional Configuration (optional)")
    org_id = input("Snyk Organization ID (press Enter to skip): ").strip()
    severity = input("Default severity threshold [low/medium/high/critical] (press Enter for 'medium'): ").strip() or "medium"
    
    # Build Snyk MCP server configuration
    snyk_config = {
        "command": "snyk",
        "args": ["mcp", "-t", "stdio"],
        "env": {
            "SNYK_TOKEN": snyk_token
        }
    }
    
    # Add optional configurations
    if org_id:
        snyk_config["env"]["SNYK_ORG"] = org_id
    
    if severity in ["low", "medium", "high", "critical"]:
        snyk_config["env"]["SNYK_SEVERITY_THRESHOLD"] = severity
    
    # Add to configuration
    config["mcpServers"]["snyk"] = snyk_config
    
    # Ask if user wants to overwrite existing snyk configuration
    if "snyk" in config.get("mcpServers", {}):
        overwrite = input("\n⚠️  Snyk MCP server already configured. Overwrite? [y/N]: ").strip().lower()
        if overwrite != 'y':
            print("❌ Configuration cancelled")
            sys.exit(0)
    
    try:
        # Save configuration
        save_config(config_path, config)
        print(f"\n✅ Configuration saved successfully!")
        print(f"📁 File: {config_path}")
        
        # Display next steps
        print("\n🚀 Next Steps:")
        print("1. Restart Claude Desktop")
        print("2. Open a new conversation")
        print("3. Look for Snyk tools in the available tools list")
        print("4. Test with: 'Can you check if Snyk is properly authenticated?'")
        
        # Display configuration summary
        print(f"\n📋 Configuration Summary:")
        print(f"   • Snyk Token: {'*' * (len(snyk_token) - 4) + snyk_token[-4:]}")
        if org_id:
            print(f"   • Organization: {org_id}")
        print(f"   • Severity Threshold: {severity}")
        
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
