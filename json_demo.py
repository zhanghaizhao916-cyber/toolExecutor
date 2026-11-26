from tool_manager import ToolManager
import tools
import json
from typing import Callable
with open("tasks.json", "r", encoding="utf-8") as file:
    tasks = json.load(file)

manager = ToolManager()
manager.register_tool("add", tools.add)
manager.register_tool("multiply", tools.multiply)
failure_counts = {}

for task in tasks:
    name = task["name"]
    args = task["args"]
    result = manager.execute_tool(name, args)
    print(result)
    if isinstance(result, str):
        failure_counts[name] = failure_counts.get(name, 0) + 1
print(failure_counts)