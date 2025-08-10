# MCP Blog Server

A Model Context Protocol (MCP) server that provides blog management tools through a simple API interface. This server allows AI assistants to interact with a blog system to retrieve, search, and create blog posts.

## 🚀 Features

- **Get Blogs**: Retrieve all available blog posts
- **Search Blogs**: Search for blogs by name/query
- **Create Blog**: Add new blog posts to the system
- **MCP Integration**: Fully compatible with MCP-compatible AI assistants

## 🛠️ Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd mcp-by-gokogua
   ```

2. **Create a virtual environment**:

   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   uv add "mcp[cli]" httpx
   ```

## 🔧 Configuration

### Claude Desktop Configuration

To use this MCP server with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "gokogua-blog": {
      "command": "uv",
      "args": ["--directory", "/path/to/your/project", "run", "main.py"]
    }
  }
}
```

**Note**: Replace `/path/to/your/project` with the actual path to your project directory.

## 🚀 Usage

### Running the Server

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the MCP server
uv run main.py
```

### Available Tools

The server provides three main tools:

1. **`get_blogs()`** - Retrieves all blog posts from the API
2. **`search_blogs(query: str)`** - Searches for blogs matching the given query
3. **`create_blog(name: str)`** - Creates a new blog post with the specified name

### API Endpoint

The server connects to a mock API at:

```
https://6898a797ddf05523e55f7ac1.mockapi.io/blogs/Blogs
```

## 🏗️ Project Structure

```
mcp-by-gokogua/
├── main.py              # Main MCP server implementation
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This documentation
└── .venv/               # Virtual environment (created during setup)
```

## 🔌 MCP Integration

This server implements the Model Context Protocol (MCP) using FastMCP, providing a standardized way for AI assistants to interact with external tools and data sources.

### Transport

The server uses `stdio` transport, making it compatible with most MCP clients.

## 🧪 Testing

To test the server functionality:

1. Start the server using `uv run main.py`
2. Use an MCP-compatible client to connect
3. Test the available tools through the MCP interface

## 📝 Dependencies

- **mcp**: Model Context Protocol implementation
- **httpx**: Modern HTTP client for Python
- **FastMCP**: Fast MCP server framework

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:

1. Check that Python 3.10+ is installed
2. Verify all dependencies are installed correctly
3. Ensure the virtual environment is activated
4. Check the API endpoint is accessible

## 🔗 Related Links

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [HTTPX Documentation](https://www.python-httpx.org/)
