from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig
from fastmcp.tools import ToolResult
from mcp import types

from config.ui import RANGE_EARNINGS_VIEW_URI
from core.rules import evaluar_tarjeta
from core.store import _tool_info_store


def register(mcp: FastMCP) -> None:
    # =========================================================
    # Tool para el rango salarial
    # =========================================================
    @mcp.tool(app=AppConfig(resource_uri=RANGE_EARNINGS_VIEW_URI, prefers_border=True))
    def open_range_earnings_ui() -> ToolResult:
        """Usar cuando la intención sea obtener/conseguir/aplicar a una tarjeta.
        Abre la UI para seleccionar un rango salarial (earnings).
        Usar cuando el usuario quiera iniciar solicitud de tarjeta.
        Esta tool SIEMPRE inicia el flujo de solicitud de tarjeta.
        """
        _tool_info_store.save("Cantidad de tarjetas", None)
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="ENVÍA ESTE MENSAJE AL USUARIO: '¿Cuál es tu ingreso mensual?'. Usa un emoji en el mensaje para hacerlo más dinámico. NO agregues ningun mensaje más.",
                )
            ]
        )

    @mcp.tool(app=AppConfig(resource_uri=RANGE_EARNINGS_VIEW_URI, prefers_border=True))
    def on_range_selected(value: str) -> ToolResult:
        # print(f"[tool] on_range_selected value={value!r}")
        mensaje, tarjetas, mejor_tarjeta = evaluar_tarjeta(value)
        _tool_info_store.save("Seleccion de rango salarial", mensaje)
        _tool_info_store.save("Cantidad de tarjetas", tarjetas)
        _tool_info_store.save("Mejor tarjeta", mejor_tarjeta)
        text = (
            "PRIMERO: Indica al usuario que se registró su Rango Salarial."
            "DESPUÉS: llama inmediatamente a la tool `open_benefits_ui`. "
            "NO expliques tu razonamiento."
        )
        return ToolResult(content=[types.TextContent(type="text", text=text)])
