import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            
            # Test the 'add' tool
            result = await session.call_tool("add", {"a": 10, "b": 5})
            print(f"Add result: {result.content[0].text}")
            
            # Test the 'greet' tool
            result = await session.call_tool("greet", {"name": "Developer"})
            print(f"Greet result: {result.content[0].text}")

asyncio.run(main())