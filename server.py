from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("MyFirstServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Generate a greeting message"""
    return f"Hello, {name}! Welcome to MCP."

@mcp.resource("info://server")
def get_info() -> str:
    """Returns basic server info"""
    return "This is my first MCP server running in GitHub Codespaces!"

if __name__ == "__main__":
    mcp.run()