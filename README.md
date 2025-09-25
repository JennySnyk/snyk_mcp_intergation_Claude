# Setting up Snyk MCP Server with Claude Desktop

This guide will walk you through setting up the Snyk MCP (Model Context Protocol) server to work with Claude Desktop, enabling AI-powered security scanning directly in your conversations with Claude.

## What is Snyk MCP Server?

The Snyk MCP server integrates Snyk's security scanning capabilities into AI workflows using the Model Context Protocol (MCP). This allows AI assistants like Claude to autonomously run security scans and identify vulnerabilities in your code, dependencies, containers, and infrastructure as code.

## Prerequisites

Before you begin, ensure you have:

1. **Claude Desktop** installed on your system
2. **Snyk CLI v1.1298.0 or later** 
3. **A Snyk account** (free or paid)
4. **Node.js** (for some dependency scanning features)
5. **Git** (for repository scanning)

## Step 1: Install Snyk CLI

### macOS (using Homebrew)
```bash
brew tap snyk/tap
brew install snyk
```

### macOS/Linux (using npm)
```bash
npm install -g snyk
```

### Windows (using Scoop)
```bash
scoop bucket add snyk https://github.com/snyk/scoop-snyk
scoop install snyk
```

### Verify Installation
```bash
snyk --version
```

You should see version 1.1298.0 or later.

## Step 2: Authenticate with Snyk

1. **Get your Snyk API token:**
   - Go to [Snyk Account Settings](https://app.snyk.io/account)
   - Copy your API token

2. **Authenticate the CLI:**
   ```bash
   snyk auth
   ```
   
   Or set the token directly:
   ```bash
   snyk config set api=YOUR_API_TOKEN
   ```

3. **Verify authentication:**
   ```bash
   snyk auth --check
   ```

## Step 3: Configure Claude Desktop for Snyk MCP

### Option A: Using Desktop Extensions (Recommended)

1. **Open Claude Desktop**
2. **Navigate to Settings > Extensions**
3. **Look for Snyk in the extensions directory**
   - If available, click "Install" and follow the prompts
   - Configure your Snyk API token when prompted

### Option B: Manual Configuration

If the Snyk extension isn't available in the directory, you can configure it manually:

1. **Locate Claude Desktop config file:**
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

2. **Create or edit the configuration file:**

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

3. **Replace `YOUR_SNYK_API_TOKEN`** with your actual Snyk API token

4. **Restart Claude Desktop**

## Step 4: Verify the Setup

1. **Open a new conversation in Claude Desktop**
2. **Look for the Snyk tools** in the available tools list (usually shown with a 🔧 icon)
3. **Test the connection** by asking Claude to check the Snyk authentication status

Example prompt:
```
Can you check if Snyk is properly authenticated and show me the available Snyk tools?
```

## Available Snyk MCP Tools

Once configured, Claude will have access to these Snyk security tools:

- **`snyk_sca_scan`** - Scan for open source vulnerabilities
- **`snyk_code_scan`** - Static application security testing (SAST)
- **`snyk_iac_scan`** - Infrastructure as Code security scanning
- **`snyk_container_scan`** - Container image vulnerability scanning
- **`snyk_sbom_scan`** - Software Bill of Materials scanning
- **`snyk_aibom`** - AI Bill of Materials generation
- **`snyk_auth`** - Authentication management
- **`snyk_auth_status`** - Check authentication status
- **`snyk_trust`** - Trust folders for scanning
- **`snyk_version`** - Get Snyk CLI version

## Usage Examples

### Basic Security Scan
```
Please scan this project directory for security vulnerabilities: /path/to/your/project
```

### Code Security Analysis
```
Can you run a SAST scan on my Python application in /Users/jenny/my-app and explain any security issues found?
```

### Container Security Check
```
Please scan this Docker image for vulnerabilities: node:18-alpine
```

### Infrastructure as Code Review
```
Review my Terraform files in ./infrastructure for security misconfigurations
```

## Troubleshooting

### Common Issues

1. **"Snyk not authenticated" error:**
   - Run `snyk auth --check` to verify authentication
   - Re-authenticate with `snyk auth` if needed

2. **"Command not found" error:**
   - Ensure Snyk CLI is properly installed and in your PATH
   - Restart your terminal/Claude Desktop after installation

3. **"Permission denied" errors:**
   - Use `snyk trust /path/to/project` to trust the project directory
   - Ensure you have read permissions for the files being scanned

4. **MCP server not starting:**
   - Check the Claude Desktop logs for error messages
   - Verify the configuration file syntax is correct
   - Ensure the Snyk CLI version is 1.1298.0 or later

### Debug Mode

Enable debug logging by modifying your configuration:

```json
{
  "mcpServers": {
    "snyk": {
      "command": "snyk",
      "args": ["mcp", "-t", "stdio"],
      "env": {
        "SNYK_TOKEN": "YOUR_SNYK_API_TOKEN",
        "SNYK_LOG_LEVEL": "debug"
      }
    }
  }
}
```

### Check Logs

- **macOS:** `~/Library/Logs/Claude/mcp-server-snyk.log`
- **Windows:** `%LOCALAPPDATA%\Claude\Logs\mcp-server-snyk.log`

## Environment Variables

You can customize the Snyk MCP server behavior using these environment variables:

- `SNYK_TOKEN` - Your Snyk API token
- `SNYK_ORG` - Default organization ID
- `SNYK_LOG_LEVEL` - Logging level (error, warn, info, debug)
- `SNYK_CFG_DISABLE_ANALYTICS` - Disable analytics (true/false)

## Security Best Practices

1. **Keep your API token secure** - Never commit it to version control
2. **Use organization-specific tokens** for team environments
3. **Regularly rotate your API tokens**
4. **Review scan results carefully** before making changes
5. **Trust only necessary directories** to minimize security risks

## Advanced Configuration

### Multiple Organizations

If you work with multiple Snyk organizations:

```json
{
  "mcpServers": {
    "snyk-org1": {
      "command": "snyk",
      "args": ["mcp", "-t", "stdio"],
      "env": {
        "SNYK_TOKEN": "TOKEN_FOR_ORG1",
        "SNYK_ORG": "org1-id"
      }
    },
    "snyk-org2": {
      "command": "snyk",
      "args": ["mcp", "-t", "stdio"],
      "env": {
        "SNYK_TOKEN": "TOKEN_FOR_ORG2",
        "SNYK_ORG": "org2-id"
      }
    }
  }
}
```

### Custom Severity Thresholds

Configure default severity thresholds:

```json
{
  "mcpServers": {
    "snyk": {
      "command": "snyk",
      "args": ["mcp", "-t", "stdio"],
      "env": {
        "SNYK_TOKEN": "YOUR_SNYK_API_TOKEN",
        "SNYK_SEVERITY_THRESHOLD": "high"
      }
    }
  }
}
```

## Getting Help

- **Snyk Documentation:** [docs.snyk.io](https://docs.snyk.io)
- **Claude Desktop Support:** [support.claude.com](https://support.claude.com)
- **MCP Documentation:** [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Snyk Community:** [community.snyk.io](https://community.snyk.io)

## What's Next?

Once you have Snyk MCP server running with Claude Desktop, you can:

1. **Integrate security scanning** into your development workflow
2. **Automate vulnerability detection** in CI/CD pipelines
3. **Generate security reports** for compliance
4. **Create custom security policies** for your organization
5. **Scale security practices** across your development team

The combination of Claude's AI capabilities with Snyk's security expertise provides a powerful platform for building secure applications efficiently.
