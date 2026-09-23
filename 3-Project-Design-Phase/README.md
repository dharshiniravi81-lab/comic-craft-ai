# 3. Project Design Phase
**Project:** ComicCraft - AI Comic Story Creator using Gemini Models

## Architecture Overview
The architecture of ComicCraft is structured into three primary components:

### 1. Frontend (HTML, CSS, Jinja2)
* Provides a simple, user-friendly web interface.
* Captures user inputs: Story Prompt, Character Name, Setting, Story Tone, and Art Style.
* Key Templates: `index.html` (input collection), `comic_preview.html` (display generated comic), and `export_success.html` (success message).

### 2. Backend (FastAPI application)
* Manages server-side operations and route handling.
* Receives form data, calls AI models, organizes the comic layout, and exports to PDF.
* Key Routes: `/generate`, `/generate-comic/json`, `/test-image`, and `/export-success`.

### 3. AI Integration
* **Gemini Flash:** Generates the structured 5-panel comic outline based on the story prompt.
* **Gemini Pro:** Creates detailed narration and character dialogues.
* **Stable Diffusion:** Generates high-quality comic-style illustrations based on image prompts.
* 
