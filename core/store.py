# =========================================================
# Configuración para guardar valores
# =========================================================
class ToolInfoStore:
    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def save(self, tool_name: str, value: str) -> str:
        self._data[tool_name] = value
        return value

    def get(self, tool_name: str) -> str | None:
        return self._data.get(tool_name)

    def summary_text(self) -> str:
        return " | ".join(f"{tool_name}: {value}" for tool_name, value in self._data.items())


_tool_info_store = ToolInfoStore()
