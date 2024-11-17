## \file hypotez/src/fast_api/main.first_version.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.fast_api """
MODE = 'development'




""" Start FastAPI 
uvicorn main:app --reload
"""

import os
import subprocess
import webbrowser
from pathlib import Path
from fastapi import FastAPI, Form, Request, HTTPException
from subprocess import Popen, PIPE
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the 'html' folder as static files
app.mount("/", StaticFiles(directory="html"), name="html")

webbrowser.open("http://localhost:8000/html/index.html")

# Endpoint to process data from HTML form
@app.post("/process_data")
async def process_data(request: Request, first_name: str = Form(...), last_name: str = Form(...)):
    # Check if first name and last name are provided
    if not first_name or not last_name:
        raise HTTPException(status_code=400, detail="First name and last name must be provided")
    
    # Formulate the input data string
    input_data = f"{first_name} {last_name}"
    
    # Execute the script with the input data and get the result
    script_path = Path(__file__).resolve().parent.parent / 'script.py'
    process = Popen(['python', str(script_path)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate(input=input_data.encode())
    
    # Check for errors during script execution
    if process.returncode != 0:
        raise HTTPException(status_code=500, detail=f"Error executing the script: {stderr.decode()}")
    
    return {"output": stdout.decode()}

# Endpoint to open index.html in the browser
@app.get("/")
async def open_index():
    # Redirect to index.html
    return {"message": "Redirecting to index.html..."}

# @app.get("/index.html")
# async def open_index_html():
#     # Open index.html in the browser
#     try:
#         webbrowser.open("http://localhost:8000/index.html")
#     except Exception as e:
#         return {"error": f"Error opening file: {e}"}
#     return {"message": "Opening index.html in the browser..."}}