## \file src/utils/pdf.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""
This module provides functionality to convert HTML content or files into PDF using `pdfkit`.
https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
"""

import pdfkit
from pathlib import Path
import os
from reportlab.pdfgen import canvas
import header
#from src import gs  
from src.logger import logger  

# Configuration for wkhtmltopdf executable path
__root__ : Path = Path(os.getcwd() [:os.getcwd().rfind(r'hypotez')+7] )

configuration = pdfkit.configuration(
    wkhtmltopdf=str(__root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe')
)
options = {"enable-local-file-access": ""}




def save_pdf(data: str | Path, pdf_file: str | Path) -> bool | None:
    """
    Save provided HTML data or a file path as a PDF.

    Args:
        data (str | Path): HTML content or path to an HTML file.
        pdf_file (str | Path): Destination path for the generated PDF.

    Example:
        .. python::
            save_as_pdf("<h1>Hello World</h1>", "output.pdf")
            save_as_pdf(Path("example.html"), "example.pdf")
    """
    try:
        if isinstance(data, str):
            # HTML content to PDF
            pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
        else:
            # File path to PDF
            pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
        logger.info(f"PDF successfully saved: {pdf_file}")
        return True
    except (pdfkit.PDFKitError, OSError) as ex:
        # Log specific errors with exception info
        logger.error("Failed to generate PDF:", ex, exc_info=True)
    except Exception as ex:
        # Catch any unexpected exceptions and log them
        logger.error("An unexpected error occurred:", ex, exc_info=True)
