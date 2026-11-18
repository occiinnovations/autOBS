import requests
from mcp.server.mcpserver import MCPServer
import os
from dotenv import load_dotenv

load_dotenv()

mcp = MCPServer("nodary")
KEY = open(os.getenv("MASTER_KEY_PATH")).read()


@mcp.tool(description=KEY)
def run(num: int) -> str:
    try:
        r = requests.post(
            f'http://{os.getenv("my_HOST")}:{int(os.getenv("my_API_PORT"))}/{num}', timeout=5)
        return f"HTTP {r.status_code}"
    except Exception as e:
        return f"Failed: {e}"


mcp.run()
