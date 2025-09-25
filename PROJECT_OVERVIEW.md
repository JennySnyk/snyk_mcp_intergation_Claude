# Snyk MCP Server with Claude Desktop & Claude Code - Project Overview

This project provides a complete setup guide and automation tools for integrating Snyk security scanning with **both Claude Desktop and Claude Code** using the Model Context Protocol (MCP).

> **Universal Compatibility**: This setup works seamlessly with both Claude Desktop (standalone application) and Claude Code (VS Code extension). Both applications share the same MCP configuration system.

## 📁 Project Structure

```
snyk-mcp-claude-setup/
├── README.md                           # Comprehensive setup guide
├── QUICK_START.md                      # Fast setup for experienced users
├── PROJECT_OVERVIEW.md                 # This file
├── examples/
│   ├── claude_desktop_config.json      # Basic configuration
│   ├── claude_desktop_config_advanced.json  # Advanced configuration
│   └── claude_desktop_config_multi_org.json # Multi-organization setup
└── scripts/
    ├── install_snyk.sh                 # Automated Snyk CLI installation
    └── setup_claude_config.py          # Interactive configuration setup
```

## 🎯 What This Project Provides

### 1. **Complete Documentation**
- Step-by-step installation guide
- Configuration examples for different use cases
- Troubleshooting tips and common solutions
- Security best practices

### 2. **Automation Scripts**
- **`install_snyk.sh`**: Automatically installs Snyk CLI on macOS/Linux
- **`setup_claude_config.py`**: Interactive Python script to configure Claude Desktop

### 3. **Configuration Templates**
- **Basic**: Simple setup with just API token
- **Advanced**: Includes organization settings, logging, and thresholds
- **Multi-org**: Support for multiple Snyk organizations

### 4. **Ready-to-Use Examples**
- Copy-paste configuration files
- Environment variable examples
- Usage scenarios and prompts

## 🚀 Quick Setup Options

### Option 1: Automated Setup (Recommended)
```bash
git clone <this-repo>
cd snyk-mcp-claude-setup
./scripts/install_snyk.sh
snyk auth
python3 scripts/setup_claude_config.py
```

### Option 2: Manual Setup
1. Install Snyk CLI (`brew install snyk` or `npm install -g snyk`)
2. Authenticate (`snyk auth`)
3. Copy configuration from `examples/` to Claude Desktop config
4. Restart Claude Desktop

### Option 3: Desktop Extensions (If Available)
**Claude Desktop:**
1. Open Claude Desktop → Settings → Extensions
2. Install Snyk extension from directory
3. Configure API token

**Claude Code:**
1. Open VS Code with Claude Code extension
2. Use Command Palette → "Claude: Configure MCP Servers"
3. Configure Snyk server as needed

## 🔧 Available Snyk Tools in Claude

Once configured, both Claude Desktop and Claude Code will have access to these Snyk security tools:

| Tool | Purpose | Example Usage |
|------|---------|---------------|
| `snyk_sca_scan` | Open source vulnerability scanning | "Scan my package.json for vulnerabilities" |
| `snyk_code_scan` | Static application security testing | "Review my Python code for security issues" |
| `snyk_iac_scan` | Infrastructure as Code scanning | "Check my Terraform files for misconfigurations" |
| `snyk_container_scan` | Container image vulnerability scanning | "Scan this Docker image: node:18-alpine" |
| `snyk_sbom_scan` | Software Bill of Materials scanning | "Analyze this SBOM file for vulnerabilities" |
| `snyk_aibom` | AI Bill of Materials generation | "Generate an AI BOM for this Python project" |
| `snyk_auth` | Authentication management | "Authenticate with Snyk" |
| `snyk_auth_status` | Check authentication status | "Check if Snyk is properly authenticated" |
| `snyk_trust` | Trust project directories | "Trust this project directory for scanning" |
| `snyk_version` | Get CLI version information | "What version of Snyk CLI is installed?" |

## 💡 Use Cases

### Development Workflow Integration
- **Pre-commit scanning**: "Scan my changes before I commit them"
- **Dependency review**: "Check if any of my dependencies have known vulnerabilities"
- **Code security review**: "Review this function for security issues"

### DevOps and Infrastructure
- **Container security**: "Audit all container images in my Docker Compose file"
- **IaC validation**: "Review my Kubernetes manifests for security best practices"
- **CI/CD integration**: "Help me set up security scanning in my GitHub Actions"

### Compliance and Reporting
- **Security audits**: "Generate a security report for this project"
- **SBOM generation**: "Create a software bill of materials for compliance"
- **Vulnerability tracking**: "Track the security status of my applications"

## 🔒 Security Considerations

### API Token Management
- Store tokens securely (never in version control)
- Use organization-specific tokens for team environments
- Rotate tokens regularly
- Consider using environment variables for sensitive data

### Project Trust
- Only trust necessary directories with `snyk trust`
- Review scan results before taking action
- Understand the security implications of automated scanning

### Network and Privacy
- Snyk MCP server communicates with Snyk's cloud services
- Code snippets may be sent to Snyk for analysis (depending on scan type)
- Review Snyk's privacy policy for data handling details

## 🛠 Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| "Snyk not authenticated" | Run `snyk auth --check` and re-authenticate if needed |
| "Command not found" | Ensure Snyk CLI is installed and in PATH |
| "Permission denied" | Use `snyk trust /path/to/project` |
| MCP server won't start | Check Claude Desktop logs and config syntax |
| Tools not appearing | Restart Claude Desktop after configuration changes |

## 📚 Additional Resources

- **Snyk Documentation**: [docs.snyk.io](https://docs.snyk.io)
- **MCP Specification**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Claude Desktop Support**: [support.claude.com](https://support.claude.com)
- **Snyk Community**: [community.snyk.io](https://community.snyk.io)

## 🤝 Contributing

This project serves as a comprehensive guide for integrating Snyk with Claude Desktop. Contributions are welcome for:

- Additional configuration examples
- Platform-specific setup instructions
- Troubleshooting solutions
- Use case documentation
- Script improvements

## 📄 License

This project is provided as educational material. Please refer to Snyk's and Anthropic's respective terms of service for their products.

---

**Created**: September 25, 2025  
**Last Updated**: September 25, 2025  
**Version**: 1.0.0
