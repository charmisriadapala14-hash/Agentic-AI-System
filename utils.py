import re
from datetime import datetime


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def validate_input(text):
    if not text or not text.strip():
        return False

    return True


def format_response(response):
    if response is None:
        return "No response generated."

    return str(response).strip()


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def split_task(task):
    tasks = re.split(r'[,;]|\band\b', task)

    return [
        item.strip()
        for item in tasks
        if item.strip()
    ]
