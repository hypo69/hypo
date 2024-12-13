```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from src.endpoints.kazarinov.pricelist_generator.pricelist_generator import ReportGenerator, main
from src.utils.pdf import PDFUtils
import asyncio
from src import gs


@pytest.fixture
def mock_env():
    """Mocks the Jinja2 Environment for testing."""
    with patch('src.endpoints.kazarinov.pricelist_generator.pricelist_generator.Environment') as mock:
        yield mock

@pytest.fixture
def mock_pdf_utils():
    """Mocks the PDFUtils class for testing."""
    with patch('src.endpoints.kazarinov.pricelist_generator.pricelist_generator.PDFUtils') as mock:
        yield mock


@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return {
        'ru': {
            'products': [
                {'product_title': 'Product 1', 'specification': 'Spec 1'},
                {'product_title': 'Product 2', 'specification': 'Spec 2'}
            ]
        },
        'he': {
            'products': [
                {'product_title': 'מוצר 1', 'specification': 'מפרט 1'},
                {'product_title': 'מוצר 2', 'specification': 'מפרט 2'}
            ]
        }
    }

@pytest.fixture
def mock_j_loads():
    """Mocks j_loads function."""
    with patch('src.endpoints.kazarinov.pricelist_generator.pricelist_generator.j_loads') as mock:
        yield mock

@pytest.fixture
def mock_random_image():
    """Mocks random_image function."""
    with patch('src.endpoints.kazarinov.pricelist_generator.pricelist_generator.random_image') as mock:
        mock.return_value = 'mocked_image_path'
        yield mock


@pytest.mark.asyncio
async def test_generate_html_ru(mock_env, sample_data):
    """Checks correct HTML generation for Russian language."""
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (ru)</h1>"

    generator = ReportGenerator()
    html_content = await generator.generate_html(sample_data['ru'], 'ru')

    mock_env.return_value.from_string.assert_called()
    mock_template.render.assert_called_with(**sample_data['ru'])
    assert html_content == "<h1>Test HTML (ru)</h1>"

@pytest.mark.asyncio
async def test_generate_html_he(mock_env, sample_data):
    """Checks correct HTML generation for Hebrew language."""
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (he)</h1>"

    generator = ReportGenerator()
    html_content = await generator.generate_html(sample_data['he'], 'he')

    mock_env.return_value.from_string.assert_called()
    mock_template.render.assert_called_with(**sample_data['he'])
    assert html_content == "<h1>Test HTML (he)</h1>"



@pytest.mark.asyncio
async def test_create_report_success_ru(mock_env, mock_pdf_utils, sample_data, mock_random_image):
    """Checks successful report creation in Russian."""
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (ru)</h1>"
    mock_pdf_utils_instance = mock_pdf_utils.return_value
    mock_pdf_utils_instance.save_pdf_pdfkit.return_value = True

    generator = ReportGenerator()
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")
    
    with patch("builtins.open", mock_open()) as mocked_file:
        result = await generator.create_report(sample_data, 'ru', html_file, pdf_file)
    
        assert result is True
        mocked_file.assert_called_once_with(html_file, "w", encoding='UTF-8')
    
    mock_pdf_utils_instance.save_pdf_pdfkit.assert_called_once_with("<h1>Test HTML (ru)</h1>", pdf_file)


@pytest.mark.asyncio
async def test_create_report_pdf_fail_ru(mock_env, mock_pdf_utils, sample_data, mock_random_image):
    """Checks report creation failure when PDF generation fails in Russian."""
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (ru)</h1>"
    mock_pdf_utils_instance = mock_pdf_utils.return_value
    mock_pdf_utils_instance.save_pdf_pdfkit.return_value = False
    
    generator = ReportGenerator()
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")
    
    with patch("builtins.open", mock_open()) as mocked_file:
         result = await generator.create_report(sample_data, 'ru', html_file, pdf_file)
         assert result is False
    mock_pdf_utils_instance.save_pdf_pdfkit.assert_called_once()



@pytest.mark.asyncio
async def test_create_report_success_he(mock_env, mock_pdf_utils, sample_data, mock_random_image):
    """Checks successful report creation in Hebrew."""
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (he)</h1>"
    mock_pdf_utils_instance = mock_pdf_utils.return_value
    mock_pdf_utils_instance.save_pdf_pdfkit.return_value = True
    
    generator = ReportGenerator()
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")
    
    with patch("builtins.open", mock_open()) as mocked_file:
         result = await generator.create_report(sample_data, 'he', html_file, pdf_file)
         assert result is True
    mock_pdf_utils_instance.save_pdf_pdfkit.assert_called_once_with("<h1>Test HTML (he)</h1>", pdf_file)


@pytest.mark.asyncio
async def test_create_report_pdf_fail_he(mock_env, mock_pdf_utils, sample_data, mock_random_image):
    """Checks report creation failure when PDF generation fails in Hebrew."""
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (he)</h1>"
    mock_pdf_utils_instance = mock_pdf_utils.return_value
    mock_pdf_utils_instance.save_pdf_pdfkit.return_value = False
    
    generator = ReportGenerator()
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")
    
    with patch("builtins.open", mock_open()) as mocked_file:
         result = await generator.create_report(sample_data, 'he', html_file, pdf_file)
         assert result is False
    mock_pdf_utils_instance.save_pdf_pdfkit.assert_called_once()


def test_main_success(mock_j_loads, mock_random_image, mock_pdf_utils, mock_env):
    """Tests the main function with mocked dependencies."""
    mock_j_loads.return_value = {'ru': {'products': []}, 'he': {'products': []}}
    mock_pdf_utils_instance = mock_pdf_utils.return_value
    mock_pdf_utils_instance.save_pdf_pdfkit.return_value = True
    mock_template = mock_env.return_value.from_string.return_value
    mock_template.render.return_value = "<h1>Test HTML (ru)</h1>"

    mexiron = 'test_mexiron'
    lang = 'ru'

    with patch('src.endpoints.kazarinov.pricelist_generator.pricelist_generator.asyncio.run') as mock_asyncio_run, \
            patch('builtins.open', mock_open()) as mocked_file:
        result = main(mexiron, lang)

    assert result is None
    mock_j_loads.assert_called_once()
    mock_asyncio_run.assert_called_once()
    mocked_file.assert_called()

def test_main_pdf_fail(mock_j_loads, mock_random_image, mock_pdf_utils, mock_env):
    """Tests the main function when PDF generation fails."""
    mock_j_loads.return_value = {'ru': {'products': []}, 'he': {'products': []}}
    mock_pdf_utils_instance = mock_pdf_utils.return_value
    mock_pdf_utils_instance.save_pdf_pdfkit.return_value = False

    mexiron = 'test_mexiron'
    lang = 'ru'

    with patch('src.endpoints.kazarinov.pricelist_generator.pricelist_generator.asyncio.run') as mock_asyncio_run, \
            patch('builtins.open', mock_open()) as mocked_file:
        result = main(mexiron, lang)
    
    assert result is None
    mock_j_loads.assert_called_once()
    mock_asyncio_run.assert_called_once()
    mocked_file.assert_called()
```