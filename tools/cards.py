from typing import Optional

from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig
from fastmcp.tools import ToolResult
from mcp import types

from config.ui import CARD_DASHBOARD_VIEW_URI, CARD_DASHBOARD_VIEW_READONLY_URI
from core.store import _tool_info_store


def register(mcp: FastMCP) -> None:
    # =========================================================
    # Tool para mostrar todas las tarjetas de crédito (solo lectura)
    # =========================================================
    @mcp.tool(app=AppConfig(resource_uri=CARD_DASHBOARD_VIEW_READONLY_URI, prefers_border=False))
    def open_card_dashboard_ui_readonly() -> ToolResult:
        """Usar cuando la intención sea ver/explorar tarjetas sin aplicar.
        Ejemplos: "ver tarjetas", "mostrar tarjetas", "qué tarjetas hay".
        """
        _tool_info_store.save("Cantidad de tarjetas", None)
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="SOLO Indica al usuario que se le está mostrando las tarjetas y si desea obtener alguna para ayudarlo a obtenerla (usa moticones). NO INDIQUES NADA MÁS.",
                )
            ]
        )

    # =========================================================
    # Tool genérica de tarjetas
    # =========================================================
    @mcp.tool(app=AppConfig(resource_uri=CARD_DASHBOARD_VIEW_URI, prefers_border=False))
    def open_card_dashboard_ui() -> ToolResult:
        """Tool genérica de tarjetas.
        Preferencia de uso:
        - Si el usuario solo quiere ver/explorar tarjetas, usar `open_card_dashboard_ui_readonly`.
        - Si vienes del flujo de tarjetas usar `open_card_dashboard_ui_with_count`.
        """
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="Abriendo Ui de tarjetas seleccionadas.. (no envies este mensaje al usuario).",
                )
            ]
        )

    @mcp.tool(app=AppConfig(resource_uri=CARD_DASHBOARD_VIEW_URI, prefers_border=False))
    def open_card_dashboard_ui_with_count(count: Optional[int] = None) -> ToolResult:
        """Usar al final del flujo evaluado/personalizado de identificación.
        No usar para intención genérica de explorar tarjetas.
        """
        mejor_tarjeta = _tool_info_store.get("Mejor tarjeta")
        benficio = _tool_info_store.get("Beneficio elegido")
        nombre = "Eduardo"
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text=(
                        f"ENVÍALE este mensaje al usuario, completa en los espacios <..>: '**{nombre}**, según tu historial crediticio e ingresos aplicas a las siguientes tarjetas.**Te recomiendo la {mejor_tarjeta}**, te da <colocar algo relacionado al bendicio, por ejemplo, 3,000 millas o 2% de cashback inicial> {benficio} de bienvenida y podrían servirte para <colocar alguna actividad interesante relacionada al beneficio>. **¿Quieres que la gestione y te la lleven a tu casa?**'. Usa unos 3 emojis distribuidos en el mensaje para hacerlo más dinámico. No agregues ningun mensaje más."
                    ),
                )
            ]
        )

    @mcp.tool(app=AppConfig(resource_uri=CARD_DASHBOARD_VIEW_URI, prefers_border=False))
    def get_dashboard_count() -> ToolResult:
        """Devuelve el count actual para que el frontend del dashboard lo consulte al cargar."""
        count = _tool_info_store.get("Cantidad de tarjetas")
        safe_count = count if isinstance(count, int) and count > 0 else None
        # print(f"[tool] tool ejecutada y el count es {safe_count}")
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text=f"dashboard_count={safe_count if safe_count is not None else 'no_definido'}",
                )
            ],
            structured_content={"count": safe_count},
        )
