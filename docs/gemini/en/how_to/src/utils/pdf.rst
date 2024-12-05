rst
How to use the PDFUtils class
========================================================================================

Description
-------------------------
This Python code defines the `PDFUtils` class, which provides static methods for converting HTML content or files to PDF format using various libraries like `pdfkit`, `FPDF`, `WeasyPrint`, and `xhtml2pdf`.  It also includes a function `set_project_root` to find the project root directory and add it to the system path if needed.  Critically, it handles potential errors robustly, logging them and returning `False` in case of failure.


Execution steps
-------------------------
1. **Project Root Detection:** The code first determines the root directory of the project. It does this by searching up from the current file's location for directories containing specific marker files (like `pyproject.toml` or `.git`). The location of the project root is then stored in a variable called `__root__`. The `set_project_root` function modifies `sys.path` to include the root directory for easier module import.

2. **Wkhtmltopdf Path Validation:** It tries to find the `wkhtmltopdf.exe` file in a specific path relative to the project root. If the file isn't found, it raises a `FileNotFoundError`, alerting the user and preventing further execution.

3. **PDF Generation (PDFKit):** The `save_pdf_pdfkit` method takes HTML content (as a string or a file path) and a PDF output file path as input. It uses `pdfkit` to convert the HTML to PDF, handling different input types (string or file). A critical step is setting up `pdfkit.configuration` with the `wkhtmltopdf` executable, ensuring that the correct `wkhtmltopdf` is used.  It also employs error handling using `try...except` blocks, logging errors and returning `False`.

4. **PDF Generation (FPDF):** The `save_pdf_fpdf` method takes HTML text and a PDF output file path. It generates a PDF using the `FPDF` library to output simple text content.  The code uses a `fonts.json` file to manage fonts, ensuring proper rendering. It's crucial that the `fonts.json` file exists in a specified location and that the corresponding font files are available at the specified paths.

5. **PDF Generation (WeasyPrint):** The `save_pdf_weasyprint` method takes HTML content (string or file path) and a PDF output file path. It uses `WeasyPrint` to generate the PDF, again handling errors effectively.

6. **PDF Generation (xhtml2pdf):** The `save_pdf_xhtml2pdf` method takes HTML content (string or file path) and a PDF output file path.  It uses `xhtml2pdf` to generate the PDF. The code addresses a potential encoding issue by converting input strings to UTF-8 if necessary.

7. **Error Handling:** Throughout the code, `try...except` blocks are implemented to handle potential errors during PDF generation and file operations (e.g., `pdfkit.PDFKitError`, `OSError`, missing files).  Errors are logged using the `logger` object to provide informative feedback to the user and prevent unexpected crashes.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.utils.pdf import PDFUtils
    from pathlib import Path

    html_content = """
    <h1>My HTML content</h1>
    <p>This is some sample text.</p>
    """

    pdf_output_file = Path("output.pdf")

    success = PDFUtils.save_pdf_pdfkit(html_content, pdf_output_file)

    if success:
        print("PDF generated successfully!")
    else:
        print("Failed to generate PDF.")