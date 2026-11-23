from tool_manager import ToolManager


def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix}, {name}"


manager = ToolManager()
manager.register_tool("greet", greet)

print(greet(name="小明"))
print(manager.execute_tool("greet", {"name": "小明"}))