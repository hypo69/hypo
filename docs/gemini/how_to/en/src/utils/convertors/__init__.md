## Usage Guide for `hypotez/src/utils/convertors/__init__.py`

This module provides a collection of functions for converting between various data formats, including CSV, JSON, XML, HTML, dictionaries, and more.  It's part of the `hypotez` project's utility library.


### Supported Conversions

The module exports functions for converting between the following formats:

* **CSV:** `csv2dict`, `csv2ns`, `dict2csv`, `ns2csv`, `json2csv`
* **Dictionaries:** `dict2ns`, `dict2xls`, `dict2xml`, `dict2csv`, `dict2html`, `md2dict`, `xls2dict`, `xml2dict`
* **JSON:** `json2csv`, `json2ns`, `json2xls`, `json2xml`, `ns2json`
* **XML:** `dict2xml`, `ns2xml`, `xml2dict`, `json2xml`
* **HTML:** `html2escape`, `html2ns`, `html2dict`, `escape2html`, `html2text`, `html2text_file`  (includes text extraction)
* **Namespaces (NS):**  `csv2ns`, `dict2ns`, `json2ns`, `ns2csv`, `ns2dict`, `ns2json`, `ns2xls`, `ns2xml`
* **Excel (XLS):** `dict2xls`, `ns2xls`, `json2xls`, `xls2dict`
* **Markdown (MD):** `md2dict`
* **Base64:** `base64_to_tmpfile`, `base64encode`
* **PNG/WebP:** `webp2png`, `TextToImageGenerator` (for text-to-image generation)
* **Speech (Text-to-Speech/Speech Recognition):** `text2speech`, `speech_recognizer`
* **DOT (GraphViz):** `dot2png`


### Example Usage (CSV to Dictionary)

```python
import os
from hypotez.src.utils.convertors import csv2dict

# Replace with your CSV file path
csv_file_path = os.path.join("data", "mydata.csv")

try:
    data_dict = csv2dict(csv_file_path)
    print(data_dict)  # Output the dictionary
except Exception as e:
    print(f"Error during conversion: {e}")
```

**Important Notes:**


* **Error Handling:**  The examples above demonstrate basic error handling.  In production code, you should always include comprehensive error handling to catch potential issues (e.g., file not found, invalid data format).
* **Input Validation:**  Consider adding input validation to your functions to ensure data integrity.  This could include checking file types, validating required columns in CSV, or verifying the structure of dictionaries.  Robust input validation is crucial for preventing unexpected behavior and ensuring data reliability.
* **File Paths:**  Always use absolute or relative paths correctly when dealing with files.


### Modules Within `convertors`

The `__init__.py` file imports functions from various submodules (`csv`, `dict`, `html`, `html2text`, `json`, `ns`, `md2dict`, `xls`, `xml2dict`, `base64`, `png`, `tts`, `dot`). Each of these submodules likely contains more specific conversions or related utilities.  You should refer to their individual documentation (if available) for detailed information about specific functions.

### Installation (For External Users)

This module is likely part of a larger project. To use it, you need to install the project containing this code.  The typical installation would be from a `requirements.txt` file, if it exists:

```bash
pip install -r requirements.txt
```

This will install the entire project, including `convertors`.  Be sure you've appropriately installed `venv` or the equivalent environment management solution.