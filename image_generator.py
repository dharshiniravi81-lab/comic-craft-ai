import os
import re
import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "runwayml/stable-diffusion-v1-5"

device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID
)

pipe = pipe.to(device)


def clean_filename(text):
    text = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        text
    )

    return text[:80]


def generate_image(
    prompt: str,
    panel_number: int
):
    os.makedirs(
        "static/panels",
        exist_ok=True
    )

    enhanced_prompt = f"""
Comic book illustration,
high quality,
detailed,
cinematic composition,
vibrant colors,
clear characters,
professional comic art.

{prompt}
"""

    image = pipe(
        enhanced_prompt,
        num_inference_steps=30
    ).images[0]

    filename = (
        f"panel_{panel_number}_"
        f"{clean_filename(prompt)}.png"
    )

    filepath = os.path.join(
        "static",
        "panels",
        filename
    )

    image.save(filepath)

    return filepath