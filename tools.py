def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b

def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix}, {name}"

def divide(a: int, b: int) -> float:
    return a / b

def label(text: str, prefix: str = "工单", suffix: str = "!") -> str:
    return f"{prefix}: {text}{suffix}"