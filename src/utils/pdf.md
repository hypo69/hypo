```rst
.. module:: src.utils.pdf
```
<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> / 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/utils/README.MD'>utils</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/utils/pdf/pdf.ru.md'>Русский</A>
</TD>
</TR>
</TABLE>

# PDF File Handling Module

## Description

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This module is designed for working with PDF files. It provides functions for converting HTML content or files into PDF, as well as converting PDF files into HTML. The module utilizes several libraries to accomplish these tasks, including `pdfkit`, `FPDF`, `WeasyPrint`, `xhtml2pdf`, and `pdfminer.six`.

## Key Features

1. **HTML to PDF Conversion**:
   - Uses the `pdfkit` library to convert HTML content or files into PDF.
   - Supports both HTML strings and files.

2. **Text to PDF Creation**:
   - Uses the `FPDF` library to create PDF files from text.
   - Supports adding custom fonts via the `fonts.json` file.

3. **HTML to PDF Conversion Using WeasyPrint**:
   - Uses the `WeasyPrint` library to create PDF files from HTML content or files.

4. **HTML to PDF Conversion Using xhtml2pdf**:
   - Uses the `xhtml2pdf` library to create PDF files from HTML content or files.

5. **PDF to HTML Conversion**:
   - Uses the `pdfminer.six` library to extract text from PDF files and create HTML files.

## Module Structure

### Imports

The module uses the following libraries:

- `pdfkit`: For converting HTML to PDF.
- `FPDF`: For creating PDF files from text.
- `WeasyPrint`: For converting HTML to PDF while preserving styles.
- `xhtml2pdf`: An alternative for converting HTML to PDF.
- `pdfminer.six`: For extracting text from PDF files.
- `pathlib`: For handling file paths.
- `json`: For loading font configuration.
- `src.logger.logger`: Custom logger for logging messages.
- `src.utils.printer`: Custom module for printing information.

### Function `set_project_root`

This function determines the project's root directory based on the presence of marker files such as `pyproject.toml`, `requirements.txt`, or `.git`. This allows the module to function independently of the current file location.

### Class `PDFUtils`

The `PDFUtils` class contains static methods for working with PDF files:

#### Methods for Creating PDF:

- **`save_pdf_pdfkit`**: Converts HTML content or files into PDF using the `pdfkit` library.
- **`save_pdf_fpdf`**: Creates a PDF file from text using the `FPDF` library. Supports adding custom fonts.
- **`save_pdf_weasyprint`**: Converts HTML content or files into PDF using the `WeasyPrint` library.
- **`save_pdf_xhtml2pdf`**: Converts HTML content or files into PDF using the `xhtml2pdf` library.

#### Methods for Converting PDF:

- **`pdf_to_html`**: Converts a PDF file into an HTML file by extracting text using the `pdfminer.six` library.

## Usage Examples

### Converting HTML to PDF

```python
from src.utils.pdf import PDFUtils

html_content = "<h1>Example HTML</h1><p>This is text.</p>"
pdf_file = "output.pdf"

success = PDFUtils.save_pdf_pdfkit(html_content, pdf_file)
if success:
    print("PDF successfully created.")
else:
    print("Error creating PDF.")
```

### Converting PDF to HTML

```python
from src.utils.pdf import PDFUtils

pdf_file = "example.pdf"
html_file = "example.html"

success = PDFUtils.pdf_to_html(pdf_file, html_file)
if success:
    print("HTML successfully created.")
else:
    print("Error converting PDF to HTML.")
```

## Dependencies

To use this module, you need to install the following libraries:

- `pdfkit`
- `FPDF`
- `WeasyPrint`
- `xhtml2pdf`
- `pdfminer.six`

Install via `pip`:

```bash
pip install pdfkit fpdf weasyprint xhtml2pdf pdfminer.six
```

## Notes

- The `pdfkit` library requires the `wkhtmltopdf` tool to be installed. The path to the executable is specified in the `wkhtmltopdf_exe` variable.
- When using `FPDF`, the `fonts.json` file must be present in the `assets/fonts` directory, containing font information.

## References

- [pdfkit Documentation](https://pypi.org/project/pdfkit/)
- [FPDF Documentation](https://pyfpdf.github.io/fpdf2/)
- [WeasyPrint Documentation](https://weasyprint.org/)
- [xhtml2pdf Documentation](https://xhtml2pdf.readthedocs.io/)
- [pdfminer.six Documentation](https://pdfminersix.readthedocs.io/)

## Author

Module author: [Your Name]

## License

This module is distributed under the [specify license, if any].