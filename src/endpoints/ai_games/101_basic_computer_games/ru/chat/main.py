# main.py
from __future__ import annotations

import json
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from typing import Any

import header
from src import gs
from src.logger import logger
from src.ai import GoogleGenerativeAI
from src.utils.file import recursively_get_file_path

base_path: Path = gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'chat'
locales_path: Path = base_path /  'html' / 'locales'
_html: Path = base_path / 'html'  # Path to Angular App


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Chat request model
class ChatRequest(BaseModel):
    message: str


model: GoogleGenerativeAI | None = None
api_key: str = gs.credentials.gemini.games
system_instruction: str = ""
rules_list: list[str] = recursively_get_file_path(
    gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'rules'
)

#app.mount("/", StaticFiles(directory=_html), name='html')  # Ensuring mounting at root


# Root route
@app.get("/", response_class=HTMLResponse)
async def root() -> HTMLResponse:
    """Serves the main index.html file for the application."""
    try:
        index_file: Path = _html / 'index.html'
        if not index_file.exists():
            raise FileNotFoundError(f"Could not find index.html at path: {index_file}")
        html_content: str = index_file.read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)
    except FileNotFoundError as e:
      logger.error(f"Error in root: File not found: {e}", exc_info=True)
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"index.html not found: {e}")
    except Exception as e:
        logger.error(f"Error in root: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error reading templates: {str(e)}")


# Chat route
@app.post("/api/chat")
async def chat(request: ChatRequest) -> dict[str, Any]:
    """Handles chat requests and returns a bot response."""
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=api_key, model_name='gemini-2.0-flash-exp')
        response: str = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))


@app.get("/api/rules")
async def rules() -> list[str]:
    """Returns the list of rules."""
    return rules_list


def get_locale_file(lang: str) -> dict[str, str]:
    """Reads a locale file based on the given language."""
    locale_file: Path = locales_path / f'{lang}.json'
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as ex:
        logger.error(f"Error reading locale: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Locale not found")
    except json.JSONDecodeError as ex:
        logger.error(f"Error decoding json: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalid locale file")
    except Exception as ex:
        logger.error(f"Error reading locale: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error reading locales")


@app.get("/locales/{lang}.json")
async def locales(lang: str) -> dict[str, str]:
    """Endpoint to retrieve locale files."""
    return get_locale_file(lang)


# Local server execution
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")