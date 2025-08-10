from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("gokogua-blog")

mock_api_url = "https://6898a797ddf05523e55f7ac1.mockapi.io/blogs/Blogs"

@mcp.tool()
def get_blogs():
    response = httpx.get(mock_api_url)
    return response.json()

@mcp.tool()
def search_blogs(query: str):
    response = httpx.get(mock_api_url, params={"name": query})
    return response.json()

@mcp.tool()
def create_blog(name: str):
    response = httpx.post(mock_api_url, json={"name": name})
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")
