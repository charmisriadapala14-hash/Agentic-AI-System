import math
from datetime import datetime


def calculator(expression):
    try:
        allowed_names = {
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "sqrt": math.sqrt,
            "pow": pow
        }

        result = eval(
            expression,
            {"__builtins__": {}},
            allowed_names
        )

        return str(result)

    except Exception as e:
        return f"Calculation Error: {str(e)}"


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def text_summarizer(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:3])
    return summary.strip()


def word_counter(text):
    return len(text.split())


def get_available_tools():
    return {
        "calculator": calculator,
        "current_time": get_current_time,
        "summarizer": text_summarizer,
        "word_counter": word_counter
    }


def execute_tool(tool_name, input_data):

    tools = get_available_tools()

    if tool_name not in tools:
        return "Tool not found."

    if tool_name == "current_time":
        return tools[tool_name]()

    return tools[tool_name](input_data)
