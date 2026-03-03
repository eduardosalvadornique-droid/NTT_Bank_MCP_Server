from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig
from fastmcp.tools import ToolResult
from mcp import types

from config.ui import IDENTIFICATION_FLOW_VIEW_URI
from core.store import _tool_info_store


def register(mcp: FastMCP) -> None:
    # =========================================================
    # Tool para la Identificación
    # =========================================================
    @mcp.tool(app=AppConfig(resource_uri=IDENTIFICATION_FLOW_VIEW_URI, prefers_border=True))
    def open_identification_flow_ui() -> ToolResult:
        """Abre la UI del flujo de identificación del usuario."""
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="ENVÍALE este mensaje al usuario: 'Bríndame tu **número de DNI y foto** para recomendarte las tarjetas a las que calificas y sean adecuadas a tus necesidades.' Usa un emoji en el mensaje para hacerlo más dinámico. No agregues ningun mensaje más.",
                )
            ]
        )

    @mcp.tool(app=AppConfig(resource_uri=IDENTIFICATION_FLOW_VIEW_URI, prefers_border=False))
    def on_identification_submitted(value: str) -> ToolResult:
        _tool_info_store.save("DNI del usuario", value)

        text = (
            "PRIMERO: Indica al usuario que se validaron de manera correcta sus datos."
            "DESPUÉS: llama inmediatamente a la tool `open_card_dashboard_ui_with_count`. "
            "No expliques tu razonamiento."
        )
        return ToolResult(content=[types.TextContent(type="text", text=text)])
