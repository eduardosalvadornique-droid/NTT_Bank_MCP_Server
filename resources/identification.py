from fastmcp import FastMCP

from config.ui import FRONTEND_ORIGIN, IDENTIFICATION_FLOW_VIEW_URI, _RESOURCE_APP
from core.wrappers import _wrapper_html


def register(mcp: FastMCP) -> None:
    @mcp.resource(IDENTIFICATION_FLOW_VIEW_URI, app=_RESOURCE_APP)
    def identification_flow_view() -> str:
        return _wrapper_html(
            iframe_src=f"{FRONTEND_ORIGIN}/identification-flow",
            event_type="identification_send_data",
            tool_name="on_identification_submitted",
            iframe_height="280px",
        )
