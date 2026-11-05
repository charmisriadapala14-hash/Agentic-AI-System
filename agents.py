from openai import OpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME, TEMPERATURE

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


class AIAgent:

    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal

    def execute(self, task):

        prompt = f"""
        You are {self.name}.
        Role: {self.role}
        Goal: {self.goal}

        Complete the following task:
        {task}
        """

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": self.role},
                    {"role": "user", "content": prompt}
                ],
                temperature=TEMPERATURE
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Agent Error: {str(e)}"


# Research Agent
research_agent = AIAgent(
    name="Research Agent",
    role="You are an expert research assistant.",
    goal="Research topics and provide accurate information."
)


# Planning Agent
planning_agent
