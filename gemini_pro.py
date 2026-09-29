import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_story(outline):
    model = genai.GenerativeModel(
        "models/gemini-1.5-pro"
    )

    prompt = f"""
You are a professional comic book writer.

Create detailed narration and dialogue
for the following comic outline.

OUTLINE:

{outline}

For every panel provide:

Panel number
Narration
Caption
Dialogue

Use this format:

PANEL 1
Narration: ...
Caption: ...
Dialogue: ...

PANEL 2
Narration: ...
Caption: ...
Dialogue: ...

Continue until PANEL 5.
"""

    response = model.generate_content(prompt)

    return response.text