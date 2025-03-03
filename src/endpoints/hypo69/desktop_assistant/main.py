# main.py

import sys
from pathlib import Path
from types import SimpleNamespace
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import json

import header
from src import gs
from src.logger import logger
from src.ai import GoogleGenerativeAI

base_path: Path = gs.path.endpoints / 'hypo69' / 'desktop_assistant'
templates_path : Path = base_path / 'templates'
locales_path: Path = base_path / 'translations'

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
api_key:str = gs.credentials.gemini.games
system_instruction:str = ""


app.mount("/templates", StaticFiles(directory=templates_path), name="static") # Ensuring mounting at root


# Root route
@app.get("/", response_class=HTMLResponse)
async def root():
    try:
        index_file =  templates_path /  'index.html'
        if not index_file.exists():
            raise FileNotFoundError(f"Could not find index.html at path: {index_file}")
        html_content = index_file.read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)
    except Exception as e:
        logger.error(f"Error in root: {e}")
        raise HTTPException(status_code=500, detail=f"Error reading templates: {str(e)}")

# Chat route
@app.post("/api/chat")
async def chat(request: ChatRequest):
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=api_key, model_name='gemini-2.0-flash-exp')
        response = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))


def get_locale_file(lang: str):
    locale_file = locales_path / f'{lang}.json'
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as ex:
        logger.error(f"Error reading locale: {ex}")
        raise HTTPException(status_code=404, detail="Locale not found")
    except json.JSONDecodeError as ex:
        logger.error(f"Error decoding json: {ex}")
        raise HTTPException(status_code=500, detail="Invalid locale file")
    except Exception as ex:
        logger.error(f"Error reading locale: {ex}")
        raise HTTPException(status_code=500, detail="Error reading locales")


@app.get("/locales/{lang}.json")
async def locales(lang:str):
    return get_locale_file(lang)


# Local server execution
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)