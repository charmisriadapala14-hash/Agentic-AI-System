import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "openai/gpt-4o-mini"

APP_NAME = "Agentic AI System"

APP_VERSION = "1.0.0"

MAX_ITERATIONS = 5

TEMPERATURE = 0.7
