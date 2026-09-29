import os

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .gemini_flash import generate_outline
from .gemini_pro import generate_story
from .image_generator import generate_image
from .layout_builder import build_comic_layout
from .exporters import save_pdf


router = APIRouter()

templates = Jinja2Templates(
    directory="templates"
)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@router.post("/generate", response_class=HTMLResponse)
async def create_comic(
    request: Request,
    prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    outline = generate_outline(
        prompt=prompt,
        character_name=character_name,
        setting=setting,
        tone=tone,
        art_style=art_style
    )

    story = generate_story(outline)

    images = []

    for panel in outline:
        image_path = generate_image(
            panel["image_prompt"],
            panel["panel"]
        )

        images.append(image_path)

    layout = build_comic_layout(
        outline,
        images,
        story
    )

    pdf_path = save_pdf(layout)

    return templates.TemplateResponse(
        "comic_preview.html",
        {
            "request": request,
            "layout": layout,
            "pdf_path": pdf_path
        }
    )


@router.post("/generate-comic/json")
async def generate_comic_json(
    prompt: str,
    character_name: str,
    setting: str,
    tone: str,
    art_style: str
):

    outline = generate_outline(
        prompt=prompt,
        character_name=character_name,
        setting=setting,
        tone=tone,
        art_style=art_style
    )

    story = generate_story(outline)

    return {
        "outline": outline,
        "story": story
    }


@router.get("/test-image")
async def test_image():

    image_path = generate_image(
        "A superhero standing in a futuristic city",
        1
    )

    return {
        "message": "Image generated successfully",
        "image": image_path
    }


@router.get("/export-success", response_class=HTMLResponse)
async def export_success(request: Request):

    return templates.TemplateResponse(
        "export_success.html",
        {
            "request": request
        }
    )