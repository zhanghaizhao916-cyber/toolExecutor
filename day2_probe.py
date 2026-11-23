from tool_manager import ToolManager



manager = ToolManager()

manager.register_tool("label", label)

print(manager.execute_tool("label",{"text": "打印失败", "prefix": "告警", "suffix": "。"} ))
print(manager.execute_tool("label",	{"text": "打印失败", "suffix": "。"} ))
print(manager.execute_tool("label",	{"text": "打印失败", "prefix": "告警"} ))
print(manager.execute_tool("label", {"text": "打印失败", "prefix": "告警", "suffix": 1}))