from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig
from fastmcp.tools import ToolResult
from mcp import types

from config.ui import BENEFITS_VIEW_URI
from core.store import _tool_info_store


def register(mcp: FastMCP) -> None:
    # =========================================================
    # Tool para seleccionar el tipo de beneficios
    # =========================================================
    @mcp.tool(app=AppConfig(resource_uri=BENEFITS_VIEW_URI, prefers_border=True))
    def open_benefits_ui() -> ToolResult:
        """Abre la UI para seleccionar el tipo de beneficios (cashback, millas, descuentos, etc)."""
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="ENVÍALE este mensaje al usuario: '¿Qué buscas principalmente en una tarjeta de crédito?'. Usa un emoji en el mensaje para hacerlo más dinámico. No agregues ningun mensaje más.",
                )
            ]
        )

    @mcp.tool(app=AppConfig(resource_uri=BENEFITS_VIEW_URI, prefers_border=True))
    def on_benefit_selected(value: str) -> ToolResult:
        # print(f"[tool] on_benefit_selected value={value!r}")
        messages = {
            "cb": "El usuario eligió Cashback.",
            "mv": "El usuario eligió Millas / Viaje.",
            "dl": "El usuario eligió Descuentos locales.",
            "rg": "El usuario eligió Recompensas generales.",
        }
        label = messages.get(value, f"Recibí: {value}")
        _tool_info_store.save("Beneficio elegido", label)
        text = (
            "PRIMERO: Indica al usuario que se registró su Benficio de interes."
            "DESPUÉS: llama inmediatamente a la tool `open_identification_flow_ui`. "
            "NO expliques tu razonamiento."
        )
        return ToolResult(content=[types.TextContent(type="text", text=text)])
