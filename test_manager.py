import unittest
import tools
from tool_manager import ToolManager
class TestToolManager(unittest.TestCase):
    #add正常测试
    def test_add(self):
        manager = ToolManager()
        manager.register_tool("add", tools.add)
        result = manager.execute_tool("add", {"a": 3, "b" : 6})
        self.assertEqual(result, 9)
    #add少参数测试
    def test_add_missing_argument(self):
        manager = ToolManager()
        manager.register_tool("add", tools.add)
        result = manager.execute_tool("add", {"a": 3})
        self.assertEqual(result, "参数错误")
    #add传错参数严格测试
    def test_add_invalid_type(self):
        manager = ToolManager()
        manager.register_tool("add", tools.add)
        result = manager.execute_tool("add", {"a": True, "b": 3})
        self.assertEqual(result, f"参数类型错误: {True}")
    #multiply正常测试
    def test_multiply(self):
        manager = ToolManager()
        manager.register_tool("multiply", tools.multiply)
        reslut = manager.execute_tool("multiply", {"a": 3, "b": 4})
        self.assertEqual(reslut, 12)
    #默认值不传参数测试
    def test_tool_uses_default_argument(self):
        manager = ToolManager()
        manager.register_tool("greet", tools.greet)
        result = manager.execute_tool("greet", {"name": "zhang"})
        self.assertEqual(result, "Hello, zhang")
    def test_text_tool_uses_default_argument(self):
        manager = ToolManager()
        manager.register_tool("label", tools.label)
        result = manager.execute_tool("label", {"text": "小琪琪"})
        self.assertEqual(result, "工单: 小琪琪!")
    #调用未注册工具测试
    def test_unknown_tool(self):
        manager = ToolManager()
        manager.register_tool("add", tools.add)       
        result = manager.execute_tool("hello", {"a": 3, "b" : 6})
        self.assertEqual(result, "未知工具")
        

if __name__=="__main__":
    unittest.main()