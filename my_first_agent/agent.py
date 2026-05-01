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


GROQ_MODEL = LiteLlm(model="ollama/llama3.2", api_base="http://localhost:11434")

math_agent = LlmAgent(
    name="math_agent",
    model=GROQ_MODEL,
    description="Specialist for math calculations like addition and multiplication.",
    instruction="You are a math specialist. Only answer math-related questions using your tools.",
    tools=[add_numbers, multiply_numbers],
)

time_agent = LlmAgent(
    name="time_agent",
    model=GROQ_MODEL,
    description="Specialist for time and date questions.",
    instruction="You are a time specialist. Only answer questions about time and dates using your tools.",
    tools=[get_current_time, get_day_of_week],
)

root_agent = LlmAgent(
    name="coordinator",
    model=GROQ_MODEL,
    description="Coordinator that routes questions to the right specialist agent.",
    instruction=(
        "You are a coordinator. Route the user's question to the right specialist:\n"
        "- Math questions → math_agent\n"
        "- Time/date questions → time_agent\n"
        "- General questions → answer yourself"
    ),
    sub_agents=[math_agent, time_agent],
)
