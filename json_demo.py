import tools
from tool_manager import ToolManager
import json
import sys

if len(sys.argv) != 2:
    raise SystemExit("用法：python json_demo.py <请求文件>")

filename = sys.argv[1]

try:
    with open(filename, encoding="utf-8") as f:
        request = json.load(f)
except FileNotFoundError:
    raise SystemExit(f"找不到文件：{filename}")
except json.JSONDecodeError:
    raise SystemExit(f"JSON格式错误：")
manger = ToolManager()
manger.register_tool("add", tools.add)
manger.register_tool("multiply", tools.multiply)
print(manger.execute_tool(request["name"], request["args"]))