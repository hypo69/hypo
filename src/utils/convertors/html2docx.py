import subprocess
from pathlib import Path
from src.logger import logger
import os


def html_to_docx(html_file: str, output_docx: Path | str) -> bool:
    """Converts an HTML file to a Word document using LibreOffice.

    Args:
        html_file (str): Path to the input HTML file as a string.
        output_docx (Path | str): Path to the output DOCX file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        # Ensure the html_file exists
        if not os.path.exists(html_file):
            logger.error(f"HTML file not found: {html_file}")
            return False

        # Ensure output directory exists
        output_dir = Path(output_docx).parent
        if not output_dir.exists():
            os.makedirs(output_dir)

        # Construct the command for LibreOffice
        command = [
            "soffice",
            "--headless",  # Run LibreOffice in headless mode
            "--convert-to",
            "docx:HTML", # Specify that input is HTML
            html_file, # use html_file as is
            "--outdir",
            str(output_dir)
        ]

        # Execute the LibreOffice command
        process = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )

        # Check for any errors outputted in the process output
        if process.stderr:
           logger.error(f"LibreOffice conversion errors: {process.stderr}")

        return True

    except subprocess.CalledProcessError as ex:
        logger.error(f"LibreOffice failed to convert HTML file: {html_file} to DOCX file: {output_docx}. Error: {ex.stderr}", exc_info=True)
        return False
    except FileNotFoundError:
        logger.error(f"LibreOffice executable (soffice) not found. Ensure it is installed and in your system's PATH.", exc_info=True)
        return False
    except Exception as ex:
        logger.error(f"An unexpected error occurred during conversion. Error: {ex}", exc_info=True)
        return False


if __name__ == '__main__':
    # Example usage
    html_file = "template.html"  # Replace with your HTML file (as string)
    output_docx = Path("output_libreoffice.docx")  # Replace with your desired output file

    if html_to_docx(html_file, output_docx):
        print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
    else:
        print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")