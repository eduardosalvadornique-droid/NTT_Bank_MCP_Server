from fastmcp import FastMCP

from config.ui import FRONTEND_ORIGIN, BENEFITS_VIEW_URI, _RESOURCE_APP
from core.wrappers import _wrapper_html


def register(mcp: FastMCP) -> None:
    @mcp.resource(BENEFITS_VIEW_URI, app=_RESOURCE_APP)
    def benefits_view() -> str:
        return _wrapper_html(
            iframe_src=f"{FRONTEND_ORIGIN}/benefit-options",
            event_type="benefits_selected",
            tool_name="on_benefit_selected",
            iframe_height="280px",
        )
