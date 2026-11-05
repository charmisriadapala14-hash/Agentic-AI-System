import json
import os
from datetime import datetime

MEMORY_FILE = "agent_memory.json"


class AgentMemory:

    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                return []

        return []

    def save_memory(self):
        with open(MEMORY_FILE, "w") as file:
            json.dump(self.memory, file, indent=4)

    def add_memory(self, task, result):
        entry = {
            "task": task,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(entry)
        self.save_memory()

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = []
        self.save_memory()

    def search_memory(self, keyword):
        return [
            item for item in self.memory
            if keyword.lower() in item["task"].lower()
            or keyword.lower() in item["result"].lower()
        ]


agent_memory = AgentMemory()
