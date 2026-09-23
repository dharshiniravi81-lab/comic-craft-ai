# 3. Project Design Phase
**Project:** ComicCraft - AI Comic Story Creator using Gemini Models

## How we designed the app
We split the project into 3 main parts: Frontend, Backend, and AI Models.

### 1. Frontend (User Interface)
* We used HTML and CSS for the design, and Jinja2 for connecting it with Python.
* The main page takes user inputs like the story idea, character name, and art style.
* We created separate pages to get the input, preview the comic, and show the download success message.

### 2. Backend (FastAPI)
* The backend is built using FastAPI.
* It acts as a bridge between the user interface and the AI models.
* It handles all the form data, builds the comic layout, and finally converts everything into a PDF file.

### 3. AI Models Used
* **Gemini Flash:** We use this to quickly create the story outline and panel descriptions.
* **Gemini Pro:** This generates the actual dialogues and character narration.
* **Stable Diffusion:** This generates the comic images based on the scene descriptions.
