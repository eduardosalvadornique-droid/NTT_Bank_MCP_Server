import os

from fastmcp import FastMCP

from tools import rag, range_earnings, benefits, identification, cards
from resources import range_earnings as range_earnings_resources
from resources import benefits as benefits_resources
from resources import identification as identification_resources
from resources import cards as cards_resources

# =========================================================
# Servidor MCP
# =========================================================
mcp = FastMCP("NTT Bank")

# =========================================================
# Registro de Tools
# =========================================================
rag.register(mcp)
range_earnings.register(mcp)
benefits.register(mcp)
identification.register(mcp)
cards.register(mcp)

# =========================================================
# Registro de Resources
# =========================================================
range_earnings_resources.register(mcp)
benefits_resources.register(mcp)
identification_resources.register(mcp)
cards_resources.register(mcp)

# =========================================================
# Run
# =========================================================
if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "streamable-http")
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "80"))
    mcp.run(transport=transport, host=host, port=port)
