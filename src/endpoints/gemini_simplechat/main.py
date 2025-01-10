from __future__ import annotations

## \file vercel_gemini_chat/main.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
.. module:: vercel_gemini_chat.main
    :platform: Windows, Unix
    :synopsis: Простой gemini чат
"""
import sys, os

from pathlib import Path
from types import SimpleNamespace
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn


from src.ai import GoogleGenerativeAI
from src.utils.jjson import j_loads_ns
from src.logger import logger


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (for testing purposes)
    allow_credentials=True,
    allow_methods=["*"],  # Allowed methods (GET, POST, etc.)
    allow_headers=["*"],  # Allowed headers
)

# Chat request model
class ChatRequest(BaseModel):
    message: str


model: GoogleGenerativeAI = None
api_key:str
system_instruction:str

config:SimpleNamespace = j_loads_ns(Path('config.json'))
gs = config

# Root route
@app.get("/", response_class=HTMLResponse)
async def root():
    if config and hasattr(config, 'templates_path') and isinstance(config.templates_path, Path):
        try:
            html_content = config.templates_path.read_text(encoding="utf-8")
            return HTMLResponse(content=html_content)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading templates: {str(e)}")
    else:
        raise HTTPException(status_code=500, detail="Configuration error: templates_path is not defined")

# Chat route
@app.post("/api/chat")
async def chat(request: ChatRequest):
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=gs.credentials.gemini.games, model_name='gemini-2.0-flash-exp')
        response = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: ",ex)
        raise HTTPException(status_code=500, detail=str(e))

# Serverless handler for Vercel
def vercel_handler(request):
    from .header import __root__
    global config, api_key
    
    config.templates_path = __root__ / 'templates' / 'index.html'

    # Load API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error(f"Не найден ключ от машины")
        sys.exit(1)

    async def app_wrapper(scope, receive, send):
        await app(scope, receive, send)
    return app_wrapper(request.scope, request.receive, request.send)

# Local initialization
def initialize_local():
    """Initializes `config` and `model` for local execution."""
    global config, api
    
    api = gs.credentials.gemini.games
    config.templates_path = Path(gs.path.endpoints, 'templates', 'index.html')
    

# Local server execution
if __name__ == "__main__":
    from src import gs
    initialize_local()
    uvicorn.run(app, host="127.0.0.1", port=8000)
