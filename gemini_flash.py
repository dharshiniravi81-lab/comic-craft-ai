import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_outline(
    prompt: str,
    character_name: str,
    setting: str,
    tone: str,
    art_style: str
):
    model = genai.GenerativeModel(
        "models/gemini-1.5-flash"
    )

    instruction = f"""
Create a 5-panel comic outline.

Story prompt:
{prompt}

Main character:
{character_name}

Setting:
{setting}

Tone:
{tone}

Art style:
{art_style}

Return ONLY valid JSON.

Use exactly this format:

[
  {{
    "panel": 1,
    "title": "Panel title",
    "scene_description": "Scene description",
    "image_prompt": "Detailed image generation prompt"
  }}
]

Create exactly 5 panels.
"""

    response = model.generate_content(instruction)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text[7:]

    if text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return json.loads(text.strip())