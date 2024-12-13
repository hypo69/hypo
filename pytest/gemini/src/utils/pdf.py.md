```python
import pytest
from pathlib import Path
import sys
import os
from unittest.mock import patch, mock_open
from hypotez.src.utils.pdf import PDFUtils, set_project_root

# Mock logger to avoid actual logging during tests
class MockLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(('info', message))
    
    def error(self, message, ex = None):
        self.messages.append(('error', message, ex))

@pytest.fixture(scope="function")
def mock_logger():
    with patch('hypotez.src.utils.pdf.logger', new_callable=MockLogger) as mock:
      yield mock

@pytest.fixture
def example_html_content():
    """Provides example HTML content for testing."""
    return "<html><body><h1>Test HTML Content</h1></body></html>"

@pytest.fixture
def example_text_content():
    """Provides example text content for testing."""
    return "This is a test text content."

@pytest.fixture
def example_html_file(tmp_path):
    """Creates a temporary HTML file for testing."""
    html_file = tmp_path / "test.html"
    html_file.write_text("<html><body><h1>Test HTML File</h1></body></html>")
    return html_file

@pytest.fixture
def example_pdf_file(tmp_path):
    """Provides a temporary file path for PDF output."""
    return tmp_path / "test.pdf"


def test_set_project_root_with_marker_file():
    """Test set_project_root function with a marker file."""
    # Create a dummy marker file in the current directory
    marker_file = "test_marker.txt"
    Path(marker_file).touch()
    
    try:
        project_root = set_project_root(marker_files=(marker_file,))
        assert project_root == Path(__file__).resolve().parent
    finally:
        # Clean up the dummy marker file
        Path(marker_file).unlink()
        
def test_set_project_root_no_marker_file():
    """Test set_project_root function with no marker file."""
    # Ensure no marker file exists in current or parent directories
    project_root = set_project_root(marker_files=('nonexistent_file.txt',))
    assert project_root == Path(__file__).resolve().parent


def test_save_pdf_pdfkit_valid_html_string(mock_logger, example_html_content, example_pdf_file):
    """Test saving PDF from HTML string using pdfkit with valid input."""
    result = PDFUtils.save_pdf_pdfkit(example_html_content, example_pdf_file)
    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()

def test_save_pdf_pdfkit_valid_html_file(mock_logger, example_html_file, example_pdf_file):
    """Test saving PDF from HTML file using pdfkit with valid input."""
    result = PDFUtils.save_pdf_pdfkit(example_html_file, example_pdf_file)
    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()

def test_save_pdf_pdfkit_invalid_data_type(mock_logger, example_pdf_file):
    """Test save_pdf_pdfkit with invalid data type."""
    result = PDFUtils.save_pdf_pdfkit(123, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Неожиданная ошибка: " in mock_logger.messages[-1][1]


@patch('hypotez.src.utils.pdf.pdfkit.from_string', side_effect=Exception("Test Exception"))
def test_save_pdf_pdfkit_pdfkit_error(mock_from_string, mock_logger, example_html_content, example_pdf_file):
    """Test handling of pdfkit.PDFKitError."""
    result = PDFUtils.save_pdf_pdfkit(example_html_content, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Неожиданная ошибка: " in mock_logger.messages[-1][1]
   

@patch('hypotez.src.utils.pdf.pdfkit.from_file', side_effect=Exception("Test Exception"))
def test_save_pdf_pdfkit_file_error(mock_from_file, mock_logger, example_html_file, example_pdf_file):
    """Test handling of OSError."""
    result = PDFUtils.save_pdf_pdfkit(example_html_file, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Неожиданная ошибка: " in mock_logger.messages[-1][1]


def test_save_pdf_fpdf_valid_text(mock_logger, example_text_content, example_pdf_file, tmp_path):
    """Test saving PDF from text using FPDF with valid input."""
    # Create a dummy fonts.json file
    fonts_file_path = tmp_path / "assets" / "fonts" / "fonts.json"
    fonts_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create a dummy font file
    font_file_path = tmp_path / "assets" / "fonts" / "dejavu-sans.book.ttf"
    font_file_path.parent.mkdir(parents=True, exist_ok=True)
    font_file_path.touch()
    
    fonts_json_content = """
{
    "dejavu-sans.book": {
        "family": "DejaVuSans",
        "path": "dejavu-sans.book.ttf",
        "style": "book",
        "uni": true
    }
}
"""
    fonts_file_path.write_text(fonts_json_content)
    
    with patch('hypotez.src.utils.pdf.__root__', tmp_path):
        result = PDFUtils.save_pdf_fpdf(example_text_content, example_pdf_file)

    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF отчет успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()


def test_save_pdf_fpdf_missing_fonts_json(mock_logger, example_text_content, example_pdf_file, tmp_path):
    """Test handling of missing fonts.json file."""
    with patch('hypotez.src.utils.pdf.__root__', tmp_path):
        result = PDFUtils.save_pdf_fpdf(example_text_content, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert f'JSON файл установки шрифтов не найден:' in mock_logger.messages[-1][1]
    assert not example_pdf_file.exists()

def test_save_pdf_fpdf_missing_font_file(mock_logger, example_text_content, example_pdf_file, tmp_path):
    """Test handling of missing font file."""
    fonts_file_path = tmp_path / "assets" / "fonts" / "fonts.json"
    fonts_file_path.parent.mkdir(parents=True, exist_ok=True)
    fonts_json_content = """
{
    "dejavu-sans.book": {
        "family": "DejaVuSans",
        "path": "dejavu-sans.book.ttf",
        "style": "book",
        "uni": true
    }
}
"""
    fonts_file_path.write_text(fonts_json_content)

    with patch('hypotez.src.utils.pdf.__root__', tmp_path):
        result = PDFUtils.save_pdf_fpdf(example_text_content, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert f'Файл шрифта не найден:' in mock_logger.messages[-1][1]
    assert not example_pdf_file.exists()

@patch('hypotez.src.utils.pdf.FPDF.output', side_effect=Exception("Test Exception"))
def test_save_pdf_fpdf_error(mock_output, mock_logger, example_text_content, example_pdf_file, tmp_path):
    """Test handling of FPDF exception during PDF creation."""
    fonts_file_path = tmp_path / "assets" / "fonts" / "fonts.json"
    fonts_file_path.parent.mkdir(parents=True, exist_ok=True)
    font_file_path = tmp_path / "assets" / "fonts" / "dejavu-sans.book.ttf"
    font_file_path.parent.mkdir(parents=True, exist_ok=True)
    font_file_path.touch()
    
    fonts_json_content = """
{
    "dejavu-sans.book": {
        "family": "DejaVuSans",
        "path": "dejavu-sans.book.ttf",
        "style": "book",
        "uni": true
    }
}
"""
    fonts_file_path.write_text(fonts_json_content)

    with patch('hypotez.src.utils.pdf.__root__', tmp_path):
        result = PDFUtils.save_pdf_fpdf(example_text_content, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Ошибка при сохранении PDF через FPDF: " in mock_logger.messages[-1][1]


def test_save_pdf_weasyprint_valid_html_string(mock_logger, example_html_content, example_pdf_file):
    """Test saving PDF from HTML string using WeasyPrint with valid input."""
    result = PDFUtils.save_pdf_weasyprint(example_html_content, example_pdf_file)
    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()

def test_save_pdf_weasyprint_valid_html_file(mock_logger, example_html_file, example_pdf_file):
    """Test saving PDF from HTML file using WeasyPrint with valid input."""
    result = PDFUtils.save_pdf_weasyprint(example_html_file, example_pdf_file)
    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()


@patch('hypotez.src.utils.pdf.HTML.write_pdf', side_effect=Exception("Test Exception"))
def test_save_pdf_weasyprint_error(mock_write_pdf, mock_logger, example_html_content, example_pdf_file):
    """Test handling of WeasyPrint exception."""
    result = PDFUtils.save_pdf_weasyprint(example_html_content, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Ошибка при сохранении PDF через WeasyPrint: " in mock_logger.messages[-1][1]


def test_save_pdf_xhtml2pdf_valid_html_string(mock_logger, example_html_content, example_pdf_file):
    """Test saving PDF from HTML string using xhtml2pdf with valid input."""
    result = PDFUtils.save_pdf_xhtml2pdf(example_html_content, example_pdf_file)
    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()

def test_save_pdf_xhtml2pdf_valid_html_file(mock_logger, example_html_file, example_pdf_file):
    """Test saving PDF from HTML file using xhtml2pdf with valid input."""
    result = PDFUtils.save_pdf_xhtml2pdf(example_html_file, example_pdf_file)
    assert result is True
    assert mock_logger.messages[-1][0] == 'info'
    assert f"PDF успешно сохранен: {example_pdf_file}" in mock_logger.messages[-1][1]
    assert example_pdf_file.exists()

@patch('hypotez.src.utils.pdf.pisa.CreatePDF', side_effect=Exception("Test Exception"))
def test_save_pdf_xhtml2pdf_error_string(mock_create_pdf, mock_logger, example_html_content, example_pdf_file):
    """Test handling of xhtml2pdf exception with string data."""
    result = PDFUtils.save_pdf_xhtml2pdf(example_html_content, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Ошибка при сохранении PDF через xhtml2pdf: " in mock_logger.messages[-1][1]

@patch('hypotez.src.utils.pdf.pisa.CreatePDF', side_effect=Exception("Test Exception"))
def test_save_pdf_xhtml2pdf_error_file(mock_create_pdf, mock_logger, example_html_file, example_pdf_file):
    """Test handling of xhtml2pdf exception with file data."""
    result = PDFUtils.save_pdf_xhtml2pdf(example_html_file, example_pdf_file)
    assert result is False
    assert mock_logger.messages[-1][0] == 'error'
    assert "Ошибка при сохранении PDF через xhtml2pdf: " in mock_logger.messages[-1][1]


def test_html2pdf_valid_input(mock_logger, example_html_content, example_pdf_file):
    """Test html2pdf with valid HTML string."""
    result = PDFUtils.html2pdf(example_html_content, example_pdf_file)
    assert result is True
    assert example_pdf_file.exists()


@patch('hypotez.src.utils.pdf.HTML.write_pdf', side_effect=Exception("Test Exception"))
def test_html2pdf_error(mock_write_pdf):
    """Test html2pdf with error during PDF creation."""
    result = PDFUtils.html2pdf("<html><body><h1>Test</h1></body></html>", "test.pdf")
    assert result is None
```