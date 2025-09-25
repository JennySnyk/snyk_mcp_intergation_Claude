#!/bin/bash

# Snyk CLI Installation Script for macOS/Linux
# This script installs the Snyk CLI and sets it up for MCP usage

set -e

echo "🔧 Installing Snyk CLI..."

# Check if we're on macOS or Linux
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "📱 Detected macOS"
    
    # Check if Homebrew is installed
    if command -v brew &> /dev/null; then
        echo "🍺 Using Homebrew to install Snyk CLI..."
        brew tap snyk/tap
        brew install snyk
    elif command -v npm &> /dev/null; then
        echo "📦 Using npm to install Snyk CLI..."
        npm install -g snyk
    else
        echo "❌ Neither Homebrew nor npm found. Please install one of them first."
        exit 1
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Detected Linux"
    
    if command -v npm &> /dev/null; then
        echo "📦 Using npm to install Snyk CLI..."
        npm install -g snyk
    else
        echo "❌ npm not found. Please install Node.js and npm first."
        exit 1
    fi
else
    echo "❌ Unsupported operating system: $OSTYPE"
    exit 1
fi

# Verify installation
echo "✅ Verifying Snyk CLI installation..."
if command -v snyk &> /dev/null; then
    SNYK_VERSION=$(snyk --version)
    echo "🎉 Snyk CLI installed successfully!"
    echo "📋 Version: $SNYK_VERSION"
    
    # Check if version is compatible (1.1298.0 or later)
    REQUIRED_VERSION="1.1298.0"
    if [[ "$(printf '%s\n' "$REQUIRED_VERSION" "$SNYK_VERSION" | sort -V | head -n1)" == "$REQUIRED_VERSION" ]]; then
        echo "✅ Version is compatible with MCP server"
    else
        echo "⚠️  Warning: Version $SNYK_VERSION may not be compatible with MCP server"
        echo "   Required version: $REQUIRED_VERSION or later"
    fi
else
    echo "❌ Snyk CLI installation failed"
    exit 1
fi

echo ""
echo "🚀 Next steps:"
echo "1. Authenticate with Snyk: snyk auth"
echo "2. Configure Claude Desktop with your Snyk token"
echo "3. Restart Claude Desktop"
echo ""
echo "📚 For detailed setup instructions, see the README.md file"
