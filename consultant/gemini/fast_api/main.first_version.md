## \file hypotez/consultant/gemini/fast_api/main.first_version.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.fast_api """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
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
        return {"error": "First name and last name are required."}, 400  # Return JSON error

    # Formulate the input data string
    input_data = f"{first_name} {last_name}"
    
    script_path = Path(__file__).resolve().parent.parent / "script.py"

    if not script_path.exists():
        return {"error": "script.py not found"}, 404

    try:
        process = Popen(['python', str(script_path)], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate(input=input_data, timeout=10)  # Add timeout

        if process.returncode != 0:
            return {"error": f"Error executing script: {stderr}"}, 500
        
        return {"output": stdout}
    except subprocess.TimeoutExpired:
        return {"error": "Script execution timed out"}, 500
    except FileNotFoundError:
        return {"error": "Python interpreter not found"}, 500


# Endpoint to open index.html (No longer needed; handled by client-side redirect)
@app.get("/")
async def open_index():
    return {"message": "Redirecting to index.html..."} # No redirect needed
```

**Explanation of Changes and Improvements:**

* **Error Handling:**
    * The code now returns a proper JSON response with an "error" key for various errors, and appropriate HTTP status codes (400 for bad request, 404 for file not found, 500 for internal server errors). This is crucial for client-side error handling.
    * **FileNotFoundError**: Added error handling if `script.py` doesn't exist.
    * **Python Interpreter Not Found**: Checks for this common problem.
    * **Timeout**: Added a timeout (10 seconds) to `process.communicate()`.  This prevents the server from hanging indefinitely if the script takes too long. Critically important for preventing denial-of-service attacks.

* **Simplified `open_index`:** The `@app.get("/")` endpoint is now simplified to just return a message.  The client (the HTML) now handles the redirect.  This is much more elegant.


* **Clearer Error Messages:**  The error messages are more informative, helping in debugging.

* **Security Considerations (Crucial):**
    * **Input Validation:** Although not demonstrated here, input sanitization is crucial to prevent vulnerabilities like command injection.  If the script in `script.py` executes commands based on user input, you need to prevent malicious input.
    * **Timeout**: The timeout is vital.  A script that takes forever or is intended to be malicious could hold up the server.

**How to Run:**

1.  Make sure your `script.py` file exists in the correct location (`hypotez/src/script.py`).
2.  Run `uvicorn main:app --reload` from your terminal.
3.  Open your `index.html` file in a web browser.  You should see the form and be able to submit data.

**Important Considerations for `script.py`:**

Your `script.py` should be designed to handle the input data appropriately and return the processed data.  For instance:

```python
# script.py
import sys

def process_data(input_data):
    # Process the input data
    print(input_data)
    result = input_data.upper()
    return result


if __name__ == "__main__":
    input_data = sys.stdin.buffer.read().decode('utf-8').strip()
    result = process_data(input_data)
    print(result, file=sys.stdout)  #Crucial! Otherwise, stdout is empty.
```

Remember to handle potential errors within `script.py` as well.