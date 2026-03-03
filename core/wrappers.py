from typing import Optional

# =========================================================
# Funciones complementarias
# =========================================================
def _wrapper_html(
    *,
    iframe_src: str,
    event_type: Optional[str] = None,
    tool_name: Optional[str] = None,
    iframe_height: str = "460px",
) -> str:
    return f"""<!doctype html>
<html>
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
    <style>
      html, body {{
        margin: 0;
        padding: 0;
        width: 100%;
        height: auto;
        overflow: hidden;
        background: transparent;
      }}

      #iframe-container {{
        width: 100%;
        height: {iframe_height};
      }}

      iframe {{
        width: 100%;
        height: 100%;
        border: 0;
        display: block;
      }}
    </style>
  </head>
  <body>
    <div id="iframe-container">
      <iframe
        id="app"
        src="{iframe_src}"
        allow="camera; microphone; clipboard-read; clipboard-write; fullscreen"
        referrerpolicy="strict-origin-when-cross-origin"
      ></iframe>
    </div>

    <script type=\"module\">
      import {{ App }} from "https://unpkg.com/@modelcontextprotocol/ext-apps@0.4.0/app-with-deps";

      const app = new App({{ name: "Catalog UI Wrapper", version: "1.0.0" }});
      await app.connect();

      const iframe = document.getElementById("app");
      let lastSentAt = 0;

      window.addEventListener("message", async (ev) => {{
        const data = ev.data || {{}};
        const expectedOrigin = new URL("{iframe_src}").origin;

        if (ev.origin !== expectedOrigin) return;

        if (data.type === "open_link" && typeof data.url === "string") {{
          const result = await app.openLink({{ url: data.url }});
          if (result?.isError) {{
            await app.sendMessage({{
              role: "user",
              content: [{{ type: "text", text: `No pude abrir el link automáticamente. Aquí está: ${{data.url}}` }}],
            }});
          }}
          return;
        }}

        if (ev.source !== iframe.contentWindow) return;

        if (data.type === "dashboard_count_request" && ev.source === iframe.contentWindow) {{
          const toolResult = await app.callServerTool({{
            name: "get_dashboard_count",
            arguments: {{}}
          }});

          const structured = toolResult?.structuredContent ?? toolResult?.structured_content ?? null;
          const count = structured?.count ?? null;

          iframe.contentWindow?.postMessage(
            {{ type: "dashboard_count_response", value: count }},
            '*'
          );
          return;
        }}

        if (data.type !== "{event_type}") return;

        const value = data.value;

        const now = Date.now();
        if (now - lastSentAt < 400) return;
        lastSentAt = now;

        const toolResult = await app.callServerTool({{
          name: "{tool_name}",
          arguments: {{ value }}
        }});

        const text = toolResult?.content?.find(c => c.type === "text")?.text
          ?? `Selección: ${{value}}`;
        const structured = toolResult?.structuredContent ?? toolResult?.structured_content ?? null;
        const nextUiUri = structured?.next_ui_uri;

        await app.sendMessage({{
          role: "user",
          content: [{{ type: "text", text }}]
        }});
      }});
    </script>
  </body>
</html>"""
