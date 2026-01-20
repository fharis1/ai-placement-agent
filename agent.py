"""
AI Agent using Pydantic AI for generating placement preparation content.
"""

import os
from dotenv import load_dotenv

from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

if not os.getenv("OPENROUTER_API_KEY"):
    raise ValueError(
        "OPENROUTER_API_KEY not found in environment variables. "
        "Please set it in your .env file."
    )

# --------------------------------------------------
# Initialize AI Agent
# --------------------------------------------------
agent = Agent(
    model=OpenRouterModel(
        "qwen/qwen-2.5-7b-instruct"
    ),
    system_prompt=(
        "You are an expert career counselor and technical interview coach. "
        "You help students prepare for placements by generating personalized "
        "study plans, interview questions, and resume feedback. "
        "Respond in clear sections with headings."
    ),
)

# --------------------------------------------------
# Agent execution function
# --------------------------------------------------
async def generate_placement_plan(resume_text: str, target_role: str, weak_areas: str):
    return f"""
Placement Plan for {target_role}

Resume Summary:
{resume_text}

Weak Areas:
{weak_areas}

Plan:
1. Practice DSA daily (arrays, strings, trees)
2. Learn system design basics
3. Do mock interviews
4. Revise CS fundamentals
"""