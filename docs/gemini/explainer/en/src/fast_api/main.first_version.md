## File hypotez/src/fast_api/main.first_version.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.fast_api
	:platform: Windows, Unix
	:synopsis:
"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis:
"""


"""
	:platform: Windows, Unix
	:synopsis:
"""


"""
  :platform: Windows, Unix
"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'

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
    process = Popen([ 'python', str(script_path)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
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
```

```
<algorithm>
```

```mermaid
graph TD
    A[Request Received] --> B{Validate Input};
    B -- Valid Input --> C[Formulate Input];
    B -- Invalid Input --> D[Error Response (400)];
    C --> E[Execute Script];
    E --> F{Check Script Return Code};
    F -- Success --> G[Return Output];
    F -- Failure --> H[Error Response (500)];
    G --> I[Response Sent];
    H --> I;
    
    subgraph Script Execution
        E --> J[Python Process];
        J --> K[Script.py];
        K --> L[Script Output];
        L --> M[Python Process];
        M --> E;
    end
    
    subgraph Documentation & Static
       A --> O[Mount Static Files]
       O --> P[Serve HTML]
       A --> Q[Open Browser]
       
    end

```

```
<explanation>
```

**Imports:**

- `os`: Provides functions for interacting with the operating system (e.g., file paths). Not heavily used here.
- `subprocess`: Used to execute external commands (like running the Python script). Crucial for inter-process communication.
- `webbrowser`: Opens web pages in a default browser.
- `pathlib`: Provides object-oriented way of working with file paths, offering more clarity and safety than string manipulations.
- `fastapi`: Core FastAPI library.  Necessary for building the API endpoints.
- `Form`, `Request`, `HTTPException`: FastAPI classes for handling form data, requests, and HTTP errors.
- `Popen`, `PIPE`: from `subprocess`, used for creating and communicating with the subprocess.
- `StaticFiles`: from `fastapi.staticfiles`, crucial for serving static files (HTML).


**Classes:**

- `FastAPI`: The main FastAPI application.  Handles routing, middleware, and startup/shutdown.
- `Request`: Represents an incoming request to the API. Used for accessing request details and headers.
-  `Path`: Provides an object-oriented way to work with file paths.

**Functions:**

- `process_data(request: Request, first_name: str = Form(...), last_name: str = Form(...)`): This function takes a request object and form data. It validates the input, constructs the input for the external script, executes the script using `subprocess.Popen()`, and returns the script output.  It's crucial for handling user input and interacting with the external script.  Error handling is good for preventing unexpected behavior.
- `open_index()`: A simple GET endpoint that sends a message to the client, currently functioning as a redirect to the static HTML page.
- (commented out) `open_index_html()`:  This function is commented out, which is a good practice when not in use.


**Variables:**

- `app = FastAPI()`: Creates a FastAPI application instance.
- `input_data`: Holds the formatted input string to be passed to the external script.


**Error Handling:**

- The code includes `HTTPException` to return appropriate error responses (400 for bad input, 500 for script errors).  This is best practice for a web API and provides meaningful error messages to the client.


**Potential Errors/Improvements:**

- The commented-out `open_index_html()` function likely won't be necessary because the static HTML is now being served directly from the path.
- Consider adding input validation to ensure first_name and last_name are not excessively long (or contain invalid characters) to enhance security.
- Error handling could be more robust.  Adding logging to capture more specific error details when communicating with the external script is recommended.


**Relationships:**

The `main.first_version.py` file is in the `fast_api` folder, likely part of a larger project (`hypotez`). It relies on `script.py` (not in the provided code), an external script, which it calls to perform its processing. The `html` directory is a static asset referenced by the `FastAPI` app. The application communicates with the script to generate results, demonstrating a clear relationship between backend API logic and external processing.