from typing import Optional

from fastmcp import FastMCP
from fastmcp.tools import ToolResult
from mcp import types

from config.knowledge_base import (
    ID_DOCUMENTO_BASE,
    LINK_DOCUMENTO_BASE,
    NOMBRE_DOCUMENTO_BASE,
    TEXTO_BASE_CONOCIMIENTO,
)


def register(mcp: FastMCP) -> None:
    @mcp.tool
    def obtener_base_conocimiento_ntt_bank(consulta: Optional[str] = None) -> ToolResult:
        """Tool para usarla cuando se realicen consultas generales sobre el banco o los productos de NTT Bank."""
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="Responde a la consulta de manera dinámica usando emojis,se amigable, clara y conciso.",
                )
            ],
            structured_content={
                "exito": True,
                "id_documento": ID_DOCUMENTO_BASE,
                "nombre_documento": NOMBRE_DOCUMENTO_BASE,
                "link_documento": LINK_DOCUMENTO_BASE,
                "consulta_recibida": consulta,
                "contenido": TEXTO_BASE_CONOCIMIENTO,
            },
        )


