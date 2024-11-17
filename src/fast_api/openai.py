## \file hypotez/src/fast_api/openai.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.fast_api """
MODE = 'development'



"""
This module provides a FastAPI application for interacting with the OpenAI model.
It includes API endpoints for querying the model and training it based on provided data.
"""

import header

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path
import uvicorn

from src import gs
from src.utils import j_loads
from src.logger import logger  # Используем ваш класс логгирования

# Импортируем класс OpenAIModel из существующего кода
from src.ai.openai.model.training import OpenAIModel
from src.gui.openai_trаigner import AssistantMainWindow

app = FastAPI()

# Указываем полный путь к директории с файлами
app.mount("/static", StaticFiles(directory=gs.path.src / 'fast_api' / 'html' / 'openai_training'), name="static")

app.add_middleware(                 # <- это для браузерных раширений 
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

model = OpenAIModel()

class AskRequest(BaseModel):
    """ Data model for the `/ask` endpoint request."""
    message: str
    system_instruction: str = None

@app.get("/", response_class=HTMLResponse)
async def root():
    """ Serve the `index.html` file at the root URL. """
    try:
        return HTMLResponse(open("html/openai/index.html").read())
    except Exception as ex:
        logger.error(f"Error during request: {str(ex)}")
        raise HTTPException(status_code=500, detail=f"Error processing the request\n{ex}")

@app.post("/ask")
async def ask_model(request: AskRequest):
    """ Processes the user's request and returns the response from the model. """
    try:
        response = model.ask(request.message, request.system_instruction)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error during request: {str(ex)}")
        raise HTTPException(status_code=500, detail=f"Error processing the request\n{ex}")

# Остальные эндпоинты...

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
