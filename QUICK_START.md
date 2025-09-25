# Quick Start Guide: Snyk MCP Server with Claude Desktop & Claude Code

Get up and running with Snyk security scanning in **Claude Desktop and Claude Code** in just a few minutes!

> **Works with both**: This setup is compatible with Claude Desktop (standalone app) and Claude Code (VS Code extension).

## 🚀 One-Command Setup (macOS/Linux)

```bash
# Clone this repository
git clone https://github.com/your-username/snyk-mcp-claude-setup.git
cd snyk-mcp-claude-setup

# Run the installation script
./scripts/install_snyk.sh

# Authenticate with Snyk
snyk auth

# Configure Claude Desktop
python3 scripts/setup_claude_config.py
```

## 📋 Manual Setup (3 Steps)

### Step 1: Install Snyk CLI

**macOS (Homebrew):**
```bash
brew tap snyk/tap && brew install snyk
```

**macOS/Linux (npm):**
```bash
npm install -g snyk
```

### Step 2: Authenticate
```bash
snyk auth
```

### Step 3: Configure Claude Desktop/Claude Code

Copy the basic configuration to your Claude configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

> **Note**: Both Claude Desktop and Claude Code use the same configuration file.

```json
{
  "mcpServers": {
    "snyk": {
      "command": "snyk",
      "args": ["mcp", "-t", "stdio"],
      "env": {
        "SNYK_TOKEN": "YOUR_SNYK_API_TOKEN"
      }
    }
  }
}
```

Get your API token from: https://app.snyk.io/account

## ✅ Test Your Setup

1. **Restart Claude Desktop or reload VS Code (for Claude Code)**
2. **Open a new conversation**
3. **Ask Claude:**
   ```
   Can you check if Snyk is properly authenticated and show me the available security tools?
   ```

## 🔧 Available Security Tools

Once configured, you can ask Claude to:

- **Scan for vulnerabilities:** "Scan my project for security issues"
- **Check dependencies:** "Analyze the open source dependencies in this project"
- **Review code security:** "Run a SAST scan on my Python code"
- **Audit containers:** "Check this Docker image for vulnerabilities"
- **Validate IaC:** "Review my Terraform files for security misconfigurations"

## 🆘 Need Help?

- **Authentication issues:** Run `snyk auth --check`
- **Permission errors:** Use `snyk trust /path/to/project`
- **Version issues:** Ensure Snyk CLI is v1.1298.0+

For detailed troubleshooting, see the full [README.md](README.md).

## 🎯 Next Steps

- Explore the [examples/](examples/) directory for advanced configurations
- Check out the [full documentation](README.md) for enterprise setups
- Join the [Snyk Community](https://community.snyk.io) for support
