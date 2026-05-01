from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from datetime import datetime


def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together and returns the result."""
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers together and returns the result."""
    return a * b


def get_current_time() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_day_of_week() -> str:
    """Returns the current day of the week."""
    return datetime.now().strftime("%A")


root_agent = LlmAgent(
    name="my_first_agent",
    model=LiteLlm(model="ollama/llama3.2", api_base="http://localhost:11434"),
    description="A helpful assistant that can do math and tell the time.",
    instruction="You are a friendly assistant. Use tools when needed to answer accurately.",
    tools=[add_numbers, multiply_numbers, get_current_time, get_day_of_week],
)
