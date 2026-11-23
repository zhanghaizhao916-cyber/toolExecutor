import inspect
import logging
import tools
from collections.abc import Callable
from typing import Any, get_type_hints


ToolFunc = Callable[..., Any]

logger = logging.getLogger(__name__)


class ToolManager:

    def __init__(self) -> None:
        self.tools: dict[str, list[Any]] = {}
    
    #注册函数{“函数名”：(函数，状态=True)}
    def register_tool(self, name: str, func: ToolFunc,  enabled: bool=True):
        self.tools[name] = [func, enabled]
    #查询函数
    def get_tool(self, name: str) -> ToolFunc | None:
        func = self.tools.get(name)
        if func is None:
            return None
        return func[0]
        
    #改变工具状态   
    def set_tool_enabled(
        self,
        name: str,
        enabled: bool
    ) -> str:
        if name not in self.tools:
            return "未知工具"
        self.tools[name][1] = enabled
        return f"工具状态已更改为{enabled}"

    def execute_tool(
        self,
        name: str,
        args: dict[str, Any]
    ) -> Any:
        # 1. 查询工具
        if self.get_tool(name) is None:
            return "未知工具"
        # 2. 检查启用状态
        if self.tools[name][1] == False:
            return "工具已禁用"
        # 3. 检查参数绑定
        func = self.get_tool(name)
        sig = inspect.signature(func)
        try:
            sig.bind(**args)
        except TypeError:
            return "参数错误"
        # 得到函数参数标注：name -> str
        
        #sig.parameters用来拿标注和默认值
        for param_name, param_obj in sig.parameters.items():
            #获取期望类型
            param_type = param_obj.annotation
            try:
                value = args[param_name]
            except KeyError:
                value = param_obj.default
            if type(value) == param_type:
                continue
            else:
                return f"参数类型错误: {value}"
        return func(**args)

