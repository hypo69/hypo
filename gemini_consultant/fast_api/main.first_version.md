```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
""" module: src.fast_api """


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


# Endpoint to process data from HTML form
@app.post("/process_data")
async def process_data(request: Request, first_name: str = Form(...), last_name: str = Form(...)):
    # Check if first name and last name are provided
    if not first_name or not last_name:
        return HTTPException(status_code=400, detail="First name and last name must be provided")  # Return directly
    
    input_data = f"{first_name} {last_name}"
    
    script_path = Path(__file__).resolve().parent.parent / 'script.py'
    
    try:
        process = Popen(['python', str(script_path)], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True) # Crucial: text=True
        stdout, stderr = process.communicate(input=input_data)
        
        if process.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Error executing the script: {stderr}")
        
        return {"output": stdout}  # Return as a dict

    except FileNotFoundError:
        return HTTPException(status_code=500, detail=f"Script file 'script.py' not found.")
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")


# Endpoint to open index.html (not needed, handled by StaticFiles)
@app.get("/")
async def root():
    return {"message": "Welcome to the application!"}


```

**Explanation of Changes and Improvements:**

* **Error Handling:**
    * The `try...except` block now catches `FileNotFoundError`. This is vital; if `script.py` isn't found, the program crashes.  The `except Exception` now has proper error handling.
    * More specific error messages are returned in case of issues, making debugging easier.
    * The `HTTPException` is returned directly from the `if not first_name` check, avoiding unnecessary code.

* **`text=True` in `Popen`:** This is **critical**.  Without `text=True`, the `communicate` method will try to interpret the input and output as bytes, potentially causing encoding errors or issues with the script's expected input format.
* **Return Type:** The function now returns a dictionary `{"output": stdout}` which is the expected format from FastAPI's response.
* **Removed Unnecessary Endpoint:** The `@app.get("/")` endpoint now returns a message, which is a more appropriate response for a GET request to the root path.  The other `@app.get` endpoint for opening `index.html` is now entirely unnecessary as the static file server will handle that automatically.
* **Clearer Error Messages:** More informative error messages for better debugging.

**How to Run:**

1.  **Ensure `script.py` exists:**  Make sure you have a Python script named `script.py` in the same directory as `main.first_version.py`'s parent directory that can accept text input and produce text output.


2.  **Run FastAPI:**
    ```bash
    uvicorn main:app --reload
    ```

3.  **Open the HTML page in a browser:** Open `http://localhost:8000/html/index.html` in your web browser.


This improved code is more robust, handles errors gracefully, and adheres to best practices.  Make sure your `script.py` can handle the string input.  If the issue still persists, please provide your `script.py` code.