# Usage Guide for `hypotez/src/utils/pdf.py`

This module provides functions for converting HTML content or files to PDF format using the `pdfkit` library, and also an alternative method using `fpdf`.

## Installation

Before using this module, ensure you have the necessary dependencies installed:

```bash
pip install pdfkit reportlab fpdf
```

Also, you need to install `wkhtmltopdf`.  This module assumes `wkhtmltopdf` is in a specific location within your project.  **You need to adjust the `wkhtmltopdf_exe` path if it's not in that location.**

## Usage

### Converting HTML to PDF (using `pdfkit`)

This method is the primary way to convert HTML to PDF.  It handles both string content and file paths.

```python
from hypotez.src.utils.pdf import PDFUtils
from pathlib import Path

# Example using HTML string
html_content = """
<h1>My HTML</h1>
<p>This is some HTML content.</p>
"""
output_pdf_path = Path("output.pdf")  # Path to the output PDF file

if PDFUtils.save_pdf(html_content, output_pdf_path):
    print("PDF saved successfully!")
else:
    print("Failed to save PDF.")

# Example using HTML file
html_file_path = Path("my_html_file.html")  # Replace with your file
output_pdf_path = Path("output2.pdf")

if PDFUtils.save_pdf(html_file_path, output_pdf_path):
    print("PDF saved successfully!")
else:
    print("Failed to save PDF.")

```

**Important Considerations:**

* **Error Handling:** The code includes robust error handling using `try...except` blocks.  This catches `pdfkit.PDFKitError`, `OSError`, and other exceptions to provide informative error messages.
* **`wkhtmltopdf` Location:** The code assumes that the `wkhtmltopdf.exe` binary is located in a specific directory (`__root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe`).  **If `wkhtmltopdf` is installed elsewhere, you must update this path.**
* **Project Root:** The `set_project_root` function is crucial for finding the project root directory.  It's crucial for correctly locating `wkhtmltopdf`.

### Converting Text to PDF (using `fpdf`)

This method provides an alternative way to convert text to PDF using the `fpdf` library.

```python
from hypotez.src.utils.pdf import PDFUtils
from pathlib import Path

text_content = "This is some text to be converted to PDF."
output_pdf_path = Path("text_output.pdf")

if PDFUtils.save_pdf_v2(text_content, output_pdf_path):
    print("PDF saved successfully!")
else:
    print("Failed to save PDF.")
```

**Important Considerations:**

* **Font:** The `fpdf` method needs a font file.  If you don't have a suitable font (`DejaVuSans.ttf`), the code will likely fail.


## Example Project Structure (Illustrative)

```
myproject/
├── bin/
│   └── wkhtmltopdf/
│       └── files/
│           └── bin/
│               └── wkhtmltopdf.exe
├── ... (other project files)
└── src/
    └── utils/
        └── pdf.py
```

This example shows the directory structure where wkhtmltopdf should reside.  **Update the paths in the code if needed.**


## Troubleshooting

* **`wkhtmltopdf` errors:** If you get errors related to `wkhtmltopdf`, double-check the installation and path to the binary.
* **Font errors (fpdf):** Ensure you have a compatible font file or specify an alternative font path.

This guide should help you use the `pdf.py` module effectively. Remember to adapt the paths to match your project structure. Remember to install required libraries!