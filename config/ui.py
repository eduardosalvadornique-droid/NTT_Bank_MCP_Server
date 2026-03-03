from fastmcp.server.apps import AppConfig, ResourceCSP, ResourcePermissions

# =========================================================
# Configuración UI
# =========================================================
FRONTEND_ORIGIN = (
    "https://mcp-front-test-arfbbch0f8hkgqex.canadacentral-01.azurewebsites.net"
)

RANGE_EARNINGS_VIEW_URI = "ui://catalog/range-earnings.html"
BENEFITS_VIEW_URI = "ui://catalog/benefits.html"
CARD_DASHBOARD_VIEW_URI = "ui://catalog/card-dashboard.html"
CARD_DASHBOARD_VIEW_READONLY_URI = "ui://catalog/card-dashboard-readonly.html"
IDENTIFICATION_FLOW_VIEW_URI = "ui://catalog/identification-flow.html"

_RESOURCE_APP = AppConfig(
    csp=ResourceCSP(
        resource_domains=["https://unpkg.com", FRONTEND_ORIGIN],
        frame_domains=[FRONTEND_ORIGIN],
    ),
    permissions=ResourcePermissions(
        camera={},
        microphone={},
    ),
    prefers_border=False,
)
