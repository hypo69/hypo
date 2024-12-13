```python
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from types import SimpleNamespace
import asyncio
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.product.product_fields import ProductFields
from src import gs

@pytest.fixture
def mock_driver():
    """Mocks the Driver class."""
    driver = MagicMock()
    driver.get_url = MagicMock()
    driver.wait = MagicMock()
    return driver

@pytest.fixture
def mock_google_generative_ai():
    """Mocks the GoogleGenerativeAI class."""
    model = MagicMock()
    model.ask = AsyncMock(return_value='{"he": {"test": "test_he"}, "ru": {"test": "test_ru"}}')
    return model

@pytest.fixture
def mock_report_generator():
    """Mocks the ReportGenerator class."""
    generator = MagicMock()
    generator.create_report = AsyncMock(return_value=True)
    return generator

@pytest.fixture
def mock_update():
    """Mocks the telegram Update class."""
    update = MagicMock()
    update.message.reply_text = AsyncMock()
    update.message.reply_document = AsyncMock()
    return update

@pytest.fixture
def mock_context():
     """Mocks the telegram CallbackContext class."""
     return MagicMock()

@pytest.fixture
def mexiron_builder(mock_driver, mock_google_generative_ai):
    """Creates an instance of MexironBuilder with mocked dependencies."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.GoogleGenerativeAI', return_value=mock_google_generative_ai):
        with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_loads_ns', return_value=SimpleNamespace(storage='data')):
            builder = MexironBuilder(mock_driver, "test_mexiron")
            builder.model = mock_google_generative_ai
            return builder

@pytest.fixture
def mock_product_fields():
    """Mocks a ProductFields object."""
    product_fields = MagicMock(spec=ProductFields)
    product_fields.id_product = "12345"
    product_fields.name = {'language': [{'value': 'Test Product'}]}
    product_fields.description_short = {'language': [{'value': 'Short description'}]}
    product_fields.description = {'language': [{'value': 'Full description'}]}
    product_fields.specification = {'language': [{'value': 'Specification details'}]}
    product_fields.local_saved_image = Path("test_image.png")
    return product_fields

@pytest.fixture
def mock_j_dumps():
    """Mocks the j_dumps function."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_dumps', return_value=True) as mock:
        yield mock

@pytest.fixture
def mock_j_loads():
    """Mocks the j_loads function."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_loads', return_value={"he": {"test": "test_he"}, "ru": {"test": "test_ru"}}) as mock:
        yield mock

@pytest.fixture
def mock_read_text_file():
    """Mocks the read_text_file function."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.Path.read_text', return_value="command_instruction_mexiron_he") as mock:
        yield mock


@pytest.mark.asyncio
async def test_mexironbuilder_init_success(mock_driver):
    """Test successful initialization of MexironBuilder."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_loads_ns', return_value=SimpleNamespace(storage='data')):
         with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.GoogleGenerativeAI'):
            builder = MexironBuilder(mock_driver, "test_mexiron")
            assert builder.driver == mock_driver
            assert builder.mexiron_name == "test_mexiron"
            assert builder.export_path == gs.path.data / 'kazarinov' / 'mexironim' / 'test_mexiron'
            assert builder.model is not None


@pytest.mark.asyncio
async def test_mexironbuilder_init_config_load_error(mock_driver, caplog):
    """Test error handling when config file fails to load."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_loads_ns', side_effect=Exception("Failed to load")):
         builder = MexironBuilder(mock_driver, "test_mexiron")
         assert builder.config is None
         assert "Error loading configuration" in caplog.text

@pytest.mark.asyncio
async def test_mexironbuilder_init_export_path_error(mock_driver, caplog):
    """Test error handling when export path cannot be constructed."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_loads_ns', return_value=SimpleNamespace(storage='invalid_storage')):
        builder = MexironBuilder(mock_driver, "test_mexiron")
        assert builder.export_path is None
        assert "Error constructing export path" in caplog.text

@pytest.mark.asyncio
async def test_mexironbuilder_init_instruction_load_error(mock_driver, caplog):
    """Test error handling when instructions or api key fails to load."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.j_loads_ns', return_value=SimpleNamespace(storage='data')):
        with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.Path.read_text', side_effect=Exception("Failed to load")):
            builder = MexironBuilder(mock_driver, "test_mexiron")
            assert builder.model is None
            assert "Error loading instructions or API key" in caplog.text


@pytest.mark.asyncio
async def test_run_scenario_success(mexiron_builder, mock_driver, mock_update, mock_context, mock_product_fields, mock_j_dumps, mock_j_loads, mock_read_text_file):
    """Test successful execution of the run_scenario method."""
    mock_graber = MagicMock()
    mock_graber.grab_page = AsyncMock(return_value=mock_product_fields)
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.ReportGenerator', return_value=mock_report_generator()):
       result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"], price="100")
       assert result is True
       mock_driver.get_url.assert_called()
       mock_graber.grab_page.assert_called()
       assert mock_update.message.reply_text.call_count == 5
       assert mock_j_dumps.call_count == 2
       assert mock_update.message.reply_document.call_count == 2
       assert mock_j_loads.call_count == 2

@pytest.mark.asyncio
async def test_run_scenario_no_graber(mexiron_builder, mock_update, mock_context, caplog):
    """Test scenario where no graber is found for a URL."""
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=None)
    result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"])
    assert result is True
    assert "Нет грабера для: https://test.com" in caplog.text

@pytest.mark.asyncio
async def test_run_scenario_grab_page_error(mexiron_builder, mock_driver, mock_update, mock_context, caplog):
    """Test scenario where grabbing product fields fails."""
    mock_graber = MagicMock()
    mock_graber.grab_page = AsyncMock(side_effect=Exception("Grab error"))
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)
    result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"])
    assert result is True
    assert "Ошибка получения полей товара" in caplog.text

@pytest.mark.asyncio
async def test_run_scenario_no_product_fields(mexiron_builder, mock_driver, mock_update, mock_context, mock_product_fields, caplog):
    """Test scenario where product fields are not parsed."""
    mock_graber = MagicMock()
    mock_graber.grab_page = AsyncMock(return_value=None)
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)

    result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"])

    assert result is True
    assert "Failed to parse product fields for URL: https://test.com" in caplog.text


@pytest.mark.asyncio
async def test_run_scenario_convert_product_fields_error(mexiron_builder, mock_driver, mock_update, mock_context, mock_product_fields, caplog):
    """Test scenario where product fields conversion fails."""
    mock_graber = MagicMock()
    mock_graber.grab_page = AsyncMock(return_value=mock_product_fields)
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)
    mexiron_builder.convert_product_fields = AsyncMock(return_value=None)

    result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"])
    assert result is True
    assert "Failed to convert product fields: None" in caplog.text

@pytest.mark.asyncio
async def test_run_scenario_save_product_data_error(mexiron_builder, mock_driver, mock_update, mock_context, mock_product_fields, caplog):
    """Test scenario where saving product data fails."""
    mock_graber = MagicMock()
    mock_graber.grab_page = AsyncMock(return_value=mock_product_fields)
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)
    mexiron_builder.save_product_data = AsyncMock(return_value=False)
    result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"], price="100")
    assert result is True
    assert "Data not saved!" in caplog.text

@pytest.mark.asyncio
async def test_run_scenario_pdf_creation_error(mexiron_builder, mock_driver, mock_update, mock_context, mock_product_fields, mock_j_dumps, mock_j_loads, mock_read_text_file):
     """Test scenario where pdf creation fails."""
     mock_graber = MagicMock()
     mock_graber.grab_page = AsyncMock(return_value=mock_product_fields)
     mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)
     with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.ReportGenerator', return_value=mock_report_generator()) as mock_generator:
         mock_generator.return_value.create_report = AsyncMock(return_value=False)
         result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"], price="100")
         assert result is True
         assert "Ошибка создания PDF: test_mexiron_he.pdf" in mock_update.message.reply_text.call_args_list[-1].args[0]

@pytest.mark.asyncio
async def test_run_scenario_pdf_not_found(mexiron_builder, mock_driver, mock_update, mock_context, mock_product_fields, mock_j_dumps, mock_j_loads, mock_read_text_file):
    """Test scenario where pdf creation is successful, but file not found."""
    mock_graber = MagicMock()
    mock_graber.grab_page = AsyncMock(return_value=mock_product_fields)
    mexiron_builder.get_graber_by_supplier_url = MagicMock(return_value=mock_graber)
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.ReportGenerator', return_value=mock_report_generator()):
      with patch("src.endpoints.kazarinov.scenarios.scenario_pricelist.Path.exists", return_value=False):
           result = await mexiron_builder.run_scenario(mock_update, mock_context, urls=["https://test.com"], price="100")
           assert result is True
           assert "PDF файл не найден или не является файлом" in mock_update.message.reply_text.call_args_list[-1].args[0]

@pytest.mark.asyncio
async def test_get_graber_by_supplier_url_morlevi(mexiron_builder, mock_driver):
    """Test get_graber_by_supplier_url method with Morlevi URL."""
    url = "https://morlevi.co.il/test"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    assert graber is not None
    assert graber.__class__.__name__ == "Graber"

@pytest.mark.asyncio
async def test_get_graber_by_supplier_url_ksp(mexiron_builder, mock_driver):
    """Test get_graber_by_supplier_url method with Ksp URL."""
    url = "https://ksp.co.il/test"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    assert graber is not None
    assert graber.__class__.__name__ == "Graber"

@pytest.mark.asyncio
async def test_get_graber_by_supplier_url_grandadvance(mexiron_builder, mock_driver):
    """Test get_graber_by_supplier_url method with Grandadvance URL."""
    url = "https://grandadvance.co.il/test"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    assert graber is not None
    assert graber.__class__.__name__ == "Graber"

@pytest.mark.asyncio
async def test_get_graber_by_supplier_url_ivory(mexiron_builder, mock_driver):
    """Test get_graber_by_supplier_url method with Ivory URL."""
    url = "https://ivory.co.il/test"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    assert graber is not None
    assert graber.__class__.__name__ == "Graber"


@pytest.mark.asyncio
async def test_get_graber_by_supplier_url_not_found(mexiron_builder, mock_driver, caplog):
    """Test get_graber_by_supplier_url method with an unknown URL."""
    url = "https://unknown.com/test"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    assert graber is None
    assert f"No graber found for URL: {url}" in caplog.text


@pytest.mark.asyncio
async def test_convert_product_fields_success(mexiron_builder, mock_product_fields):
    """Test successful conversion of ProductFields to a dictionary."""
    converted_data = await mexiron_builder.convert_product_fields(mock_product_fields)
    assert converted_data['product_title'] == 'Test Product'
    assert converted_data['product_id'] == '12345'
    assert converted_data['description_short'] == 'Short description'
    assert converted_data['description'] == 'Full description'
    assert converted_data['specification'] == 'Specification details'
    assert str(converted_data['local_saved_image']) == 'test_image.png'

@pytest.mark.asyncio
async def test_convert_product_fields_no_id(mexiron_builder, mock_product_fields):
    """Test conversion with missing id_product."""
    mock_product_fields.id_product = None
    converted_data = await mexiron_builder.convert_product_fields(mock_product_fields)
    assert converted_data == {}

@pytest.mark.asyncio
async def test_save_product_data_success(mexiron_builder, mock_j_dumps):
    """Test successful saving of product data."""
    product_data = {"product_id": "123", "name": "Test Product"}
    result = await mexiron_builder.save_product_data(product_data)
    assert result is True
    mock_j_dumps.assert_called()

@pytest.mark.asyncio
async def test_save_product_data_error(mexiron_builder, mock_j_dumps, caplog):
    """Test failed saving of product data."""
    mock_j_dumps.return_value = False
    product_data = {"product_id": "123", "name": "Test Product"}
    result = await mexiron_builder.save_product_data(product_data)
    assert result is None
    assert "Ошибка сохранения словаря" in caplog.text

@pytest.mark.asyncio
async def test_process_ai_success(mexiron_builder, mock_j_loads, mock_read_text_file):
    """Test successful AI processing."""
    products_list = ["product1", "product2"]
    result = await mexiron_builder.process_ai(products_list, 'he')
    assert result == {'he': {'test': 'test_he'}, 'ru': {'test': 'test_ru'}}

@pytest.mark.asyncio
async def test_process_ai_no_response(mexiron_builder, mock_google_generative_ai, mock_read_text_file, caplog):
    """Test AI processing with no response from the model."""
    mock_google_generative_ai.ask = AsyncMock(return_value=None)
    products_list = ["product1", "product2"]
    result = await mexiron_builder.process_ai(products_list, 'he')
    assert result == {}
    assert "Нет ответа от модели" in caplog.text


@pytest.mark.asyncio
async def test_process_ai_invalid_response(mexiron_builder, mock_google_generative_ai, mock_j_loads, mock_read_text_file, caplog):
    """Test AI processing with an invalid response from the model."""
    mock_j_loads.return_value = None
    products_list = ["product1", "product2"]
    result = await mexiron_builder.process_ai(products_list, 'he', attempts=1)
    assert result == {}
    assert "Ошибка парсинга ответа модели" in caplog.text

@pytest.mark.asyncio
async def test_process_ai_max_attempts_reached(mexiron_builder, mock_google_generative_ai, mock_j_loads, mock_read_text_file, caplog):
    """Test AI processing with max attempts reached."""
    mock_j_loads.return_value = None
    products_list = ["product1", "product2"]
    result = await mexiron_builder.process_ai(products_list, 'he', attempts=0)
    assert result == {}

@pytest.mark.asyncio
async def test_post_facebook_success(mexiron_builder, mock_driver):
    """Test successful facebook post."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.post_message_title', return_value = True):
        with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.upload_post_media', return_value = True):
            with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.message_publish', return_value = True):
                mexiron = SimpleNamespace(title='test_title', description='test_description', price='100', products=['test_image.png'])
                result = await mexiron_builder.post_facebook(mexiron)
                assert result is True

@pytest.mark.asyncio
async def test_post_facebook_title_fail(mexiron_builder, mock_driver, caplog):
        """Test failed facebook post, when title posting failed."""
        with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.post_message_title', return_value = False):
            with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.upload_post_media', return_value = True):
                with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.message_publish', return_value = True):
                    mexiron = SimpleNamespace(title='test_title', description='test_description', price='100', products=['test_image.png'])
                    result = await mexiron_builder.post_facebook(mexiron)
                    assert result is None
                    assert 'Не получилось отправить название мехирона' in caplog.text

@pytest.mark.asyncio
async def test_post_facebook_media_fail(mexiron_builder, mock_driver, caplog):
    """Test failed facebook post, when media posting failed."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.post_message_title', return_value = True):
        with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.upload_post_media', return_value = False):
            with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.message_publish', return_value = True):
                mexiron = SimpleNamespace(title='test_title', description='test_description', price='100', products=['test_image.png'])
                result = await mexiron_builder.post_facebook(mexiron)
                assert result is None
                assert 'Не получилось отправить media' in caplog.text

@pytest.mark.asyncio
async def test_post_facebook_publish_fail(mexiron_builder, mock_driver, caplog):
    """Test failed facebook post, when publish posting failed."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.post_message_title', return_value = True):
        with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.upload_post_media', return_value = True):
            with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.message_publish', return_value = False):
                mexiron = SimpleNamespace(title='test_title', description='test_description', price='100', products=['test_image.png'])
                result = await mexiron_builder.post_facebook(mexiron)
                assert result is None
                assert 'Не получилось отправить media' in caplog.text

@pytest.mark.asyncio
async def test_create_report_success(mexiron_builder, mock_report_generator, mock_update):
    """Test successful creation of a report."""
    data = {"test": "data"}
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")
    await mexiron_builder.create_report(data, html_file, pdf_file)
    mock_report_generator.create_report.assert_called()
    assert mock_update.message.reply_document.call_count == 2


@pytest.mark.asyncio
async def test_create_report_pdf_not_found(mexiron_builder, mock_report_generator, mock_update, caplog):
    """Test report creation fail, file not found."""
    data = {"test": "data"}
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")
    with patch("src.endpoints.kazarinov.scenarios.scenario_pricelist.Path.exists", return_value=False):
        await mexiron_builder.create_report(data, html_file, pdf_file)
        assert "PDF файл не найден или не является файлом" in caplog.text
```