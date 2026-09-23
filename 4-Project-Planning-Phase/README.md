# 4. Project Planning Phase
**Project:** ComicCraft - AI Comic Story Creator using Gemini Models

## Project Workflow and Milestones
Here is how we planned and divided our work:

* **Milestone 1: Planning & Setup**
  - Selected the best AI models for the job (Gemini for text, Stable Diffusion for images).
  - Planned the overall architecture (how frontend talks to backend).
  - Created a virtual environment and installed all required Python libraries.

* **Milestone 2: Core Development**
  - Wrote the main Python scripts to generate stories using Gemini API.
  - Connected the Hugging Face API to generate images.
  - Added the code to combine the text and images into a single PDF file.

* **Milestone 3: Setting up the Server**
  - Built the FastAPI backend.
  - Created routes (like `/generate` and `/export-success`) so the frontend forms can send data to our Python code.

* **Milestone 4: Frontend Web Design**
  - Designed the web pages using HTML, CSS, and Jinja2.
  - Made sure the form looks good and the comic panels are displayed neatly one by one.

* **Milestone 5: Testing & Local Run**
  - Ran the server locally using Uvicorn.
  - Tested all inputs to make sure the AI generates the right comic and the PDF download works properly.
  - 
