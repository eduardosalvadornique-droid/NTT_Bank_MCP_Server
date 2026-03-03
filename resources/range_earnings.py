from fastmcp import FastMCP

from config.ui import FRONTEND_ORIGIN, RANGE_EARNINGS_VIEW_URI, _RESOURCE_APP
from core.wrappers import _wrapper_html


def register(mcp: FastMCP) -> None:
    @mcp.resource(RANGE_EARNINGS_VIEW_URI, app=_RESOURCE_APP)
    def range_earnings_view() -> str:
        return _wrapper_html(
            iframe_src=f"{FRONTEND_ORIGIN}/range-earings",
            event_type="range_earnings_selected",
            tool_name="on_range_selected",
            iframe_height="280px",
        )
