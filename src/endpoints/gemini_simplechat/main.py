

## \file main.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: gemini_simplechat.main
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

import header
from header import __root__
from src import gs
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

system_instruction:str = Path('instructions', 'system_instruction.md').read_text(encoding='UTF-8') 
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key = gs.credentials.gemini.api_key, 
                                               model_name = gs.credentials.gemini.model_name, 
                                               system_instruction = system_instruction)

# Root route
@app.get("/", response_class=HTMLResponse)
async def root():

    try:
        html_content = Path( __root__ / gs.fast_api.index_path).read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error reading templates:{str(ex)}" )


# Chat route
@app.post("/api/chat")
async def chat(request: ChatRequest):
    global model
    try:
        response = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: ",ex)
        raise HTTPException(status_code=500, detail=str(e))


    

# Local server execution
if __name__ == "__main__":

    uvicorn.run(app, host=gs.fast_api.host, port=int(gs.fast_api.port))
