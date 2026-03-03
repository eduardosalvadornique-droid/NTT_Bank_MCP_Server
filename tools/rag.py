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
    # =========================================================
    # Tool RAG
    # =========================================================
    @mcp.tool
    def obtener_base_conocimiento_ntt_bank(consulta: Optional[str] = None) -> ToolResult:
        """Tool que devuelve el documento completo de información institucional de NTT Bank y sus productos.
        Usarla cuando se realicen consultas generales sobre el banco o los productos.
        """
        return ToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text="Responde a la pregunta usando SOLO la información de 'contenido'.",
                )
            ],
            structured_content={
                "exito": True,
                "Instrucciones para responder": "Responde a la consulta de manera dinámica usando emojis,se amigable, clara y conciso.",
                "id_documento": ID_DOCUMENTO_BASE,
                "nombre_documento": NOMBRE_DOCUMENTO_BASE,
                "link_documento": LINK_DOCUMENTO_BASE,
                "consulta_recibida": consulta,
                "contenido": TEXTO_BASE_CONOCIMIENTO,
            },
        )
