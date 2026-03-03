from fastmcp import FastMCP

from config.ui import (
    FRONTEND_ORIGIN,
    CARD_DASHBOARD_VIEW_URI,
    CARD_DASHBOARD_VIEW_READONLY_URI,
    _RESOURCE_APP,
)
from core.wrappers import _wrapper_html


def register(mcp: FastMCP) -> None:
    @mcp.resource(CARD_DASHBOARD_VIEW_URI, app=_RESOURCE_APP)
    def card_dashboard_view() -> str:
        iframe_src = f"{FRONTEND_ORIGIN}/card-dashboard"
        return _wrapper_html(
            iframe_src=iframe_src,
            event_type="open_link",
            tool_name="unknown",
            iframe_height="420px",
        )

    @mcp.resource(CARD_DASHBOARD_VIEW_READONLY_URI, app=_RESOURCE_APP)
    def card_dashboard_readonly_view() -> str:
        iframe_src = f"{FRONTEND_ORIGIN}/card-dashboard?hideApplyButton=true"
        return _wrapper_html(
            iframe_src=iframe_src,
            event_type="open_link",
            tool_name="unknown",
            iframe_height="420px",
        )
