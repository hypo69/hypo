```python
import pytest
from unittest.mock import MagicMock, patch
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError
import requests

from src.endpoints.prestashop.api.api import PrestaShop, Format
from src.logger.exceptions import PrestaShopException, PrestaShopAuthenticationError


@pytest.fixture
def prestashop_instance():
    """Provides a basic PrestaShop instance for testing."""
    with patch('src.endpoints.prestashop.api.api.gs.credentials', new_callable=MagicMock) as mock_gs_cred:
        mock_gs_cred.presta.client.api_key = "https://test.prestashop.com/api/"
        instance = PrestaShop(data_format='JSON', default_lang=1, debug=True)
    return instance


@pytest.fixture
def mock_response():
    """Provides a mock response object."""
    mock = MagicMock()
    mock.status_code = 200
    mock.headers = {'psws-version': '1.7.8'}
    mock.json.return_value = {'test': 'data'}
    mock.text = '<xml><test>data</test></xml>'
    mock.request = MagicMock()
    mock.request.url = "https://test.prestashop.com/api/test_resource"
    return mock

def test_prestashop_init(prestashop_instance):
    """Test the initialization of the PrestaShop class."""
    assert prestashop_instance.API_DOMAIN == "https://test.prestashop.com/api/api/"
    assert prestashop_instance.API_KEY == "https://test.prestashop.com/api/"
    assert prestashop_instance.debug is True
    assert prestashop_instance.language == 1
    assert prestashop_instance.data_format == 'JSON'
    assert prestashop_instance.ps_version == '1.7.8'
    assert prestashop_instance.client.auth == ("https://test.prestashop.com/api/", '')


def test_ping_success(prestashop_instance, mock_response):
    """Test successful ping to the API."""
    prestashop_instance.client.request = MagicMock(return_value=mock_response)
    assert prestashop_instance.ping() is True
    prestashop_instance.client.request.assert_called_once_with(method='HEAD', url=prestashop_instance.API_DOMAIN)

def test_ping_failure(prestashop_instance):
    """Test failed ping to the API with non-200 status code."""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.text = "Error message"
    prestashop_instance.client.request = MagicMock(return_value=mock_response)
    with patch.object(prestashop_instance, '_parse_response_error') as mock_parse_error:
        assert prestashop_instance.ping() is False
        mock_parse_error.assert_called_once()


def test_check_response_success(prestashop_instance, mock_response):
    """Test _check_response method with a successful status code."""
    assert prestashop_instance._check_response(200, mock_response) is True
    assert prestashop_instance._check_response(201, mock_response) is True


def test_check_response_failure(prestashop_instance, mock_response):
    """Test _check_response method with a failed status code."""
    with patch.object(prestashop_instance, '_parse_response_error') as mock_parse_error:
      assert prestashop_instance._check_response(404, mock_response) is False
      mock_parse_error.assert_called_once()

def test_parse_response_error_json(prestashop_instance, mock_response):
    """Test _parse_response_error method with JSON format."""
    mock_response.status_code = 404
    mock_response.text = '{"error": "test error"}'
    result = prestashop_instance._parse_response_error(mock_response)
    assert result == mock_response

def test_parse_response_error_xml_dict(prestashop_instance, mock_response):
    """Test _parse_response_error method with XML format."""
    prestashop_instance.data_format = 'XML'
    mock_response.text = '''<prestashop><errors><error><code>123</code><message>Test Error</message></error></errors></prestashop>'''
    with patch.object(prestashop_instance, '_parse', return_value={'PrestaShop': {'errors': {'error': {'code': '123', 'message': 'Test Error'}}}}):
        code, message = prestashop_instance._parse_response_error(mock_response)
        assert code == '123'
        assert message == 'Test Error'
def test_parse_response_error_xml_list(prestashop_instance, mock_response):
    """Test _parse_response_error method with XML format and a list of errors."""
    prestashop_instance.data_format = 'XML'
    mock_response.text = '''<prestashop><errors><error><code>123</code><message>Test Error</message></error><error><code>124</code><message>Test Error 2</message></error></errors></prestashop>'''
    with patch.object(prestashop_instance, '_parse', return_value={'PrestaShop': {'errors': {'error': [{'code': '123', 'message': 'Test Error'},{'code': '124', 'message': 'Test Error 2'}]}}}}):
        code, message = prestashop_instance._parse_response_error(mock_response)
        assert code == '123'
        assert message == 'Test Error'

def test_parse_response_error_xml_element(prestashop_instance, mock_response):
    """Test _parse_response_error method with XML format."""
    prestashop_instance.data_format = 'XML'
    xml_text = '<errors><error><code>123</code><message>Test Error</message></error></errors>'
    element = ElementTree.fromstring(xml_text)
    with patch.object(prestashop_instance, '_parse', return_value=element):
        code, message = prestashop_instance._parse_response_error(mock_response)
        assert code == '123'
        assert message == 'Test Error'

def test_prepare(prestashop_instance):
    """Test the _prepare method."""
    url = "https://test.prestashop.com/api/products"
    params = {"filter": "[id]=5", "display": "full"}
    expected_url = "https://test.prestashop.com/api/products?filter=%5Bid%5D=5&display=full"
    assert prestashop_instance._prepare(url, params) == expected_url

@patch('src.endpoints.prestashop.api.api.sys')
@patch('src.endpoints.prestashop.api.api.open', new_callable=MagicMock)
def test_exec_success_json(mock_open, mock_sys, prestashop_instance, mock_response):
    """Test successful execution of an API request with JSON format."""
    prestashop_instance.client.request = MagicMock(return_value=mock_response)
    result = prestashop_instance._exec(resource='products', method='GET', io_format='JSON')
    assert result == {'test': 'data'}
    prestashop_instance.client.request.assert_called_once()


@patch('src.endpoints.prestashop.api.api.sys')
@patch('src.endpoints.prestashop.api.api.open', new_callable=MagicMock)
def test_exec_success_xml(mock_open, mock_sys, prestashop_instance, mock_response):
    """Test successful execution of an API request with XML format."""
    prestashop_instance.client.request = MagicMock(return_value=mock_response)
    prestashop_instance.data_format = 'XML'
    with patch.object(prestashop_instance, '_parse', return_value={'test': 'data'}):
      result = prestashop_instance._exec(resource='products', method='GET', io_format='XML')
      assert result == {'test': 'data'}
    prestashop_instance.client.request.assert_called_once()

@patch('src.endpoints.prestashop.api.api.sys')
@patch('src.endpoints.prestashop.api.api.open', new_callable=MagicMock)
def test_exec_failure(mock_open, mock_sys, prestashop_instance, mock_response):
    """Test failed execution of an API request."""
    mock_response.status_code = 404
    prestashop_instance.client.request = MagicMock(return_value=mock_response)
    assert prestashop_instance._exec(resource='products', method='GET', io_format='JSON') is False

def test_parse_json_success(prestashop_instance, mock_response):
    """Test successful parsing of a JSON response."""
    with patch('src.endpoints.prestashop.api.api.requests.Response.json', return_value={'PrestaShop': {'test': 'data'}}):
        result = prestashop_instance._parse(mock_response.text)
        assert result == {'test': 'data'}

def test_parse_json_no_prestashop(prestashop_instance, mock_response):
    """Test successful parsing of a JSON response."""
    with patch('src.endpoints.prestashop.api.api.requests.Response.json', return_value={'test': 'data'}):
        result = prestashop_instance._parse(mock_response.text)
        assert result == {'test': 'data'}

def test_parse_xml_success(prestashop_instance, mock_response):
    """Test successful parsing of an XML response."""
    prestashop_instance.data_format = 'XML'
    result = prestashop_instance._parse(mock_response.text)
    assert isinstance(result, ElementTree.Element)

def test_parse_xml_error(prestashop_instance):
    """Test XML parsing with invalid XML format."""
    prestashop_instance.data_format = 'XML'
    with patch('src.endpoints.prestashop.api.api.ElementTree.fromstring', side_effect=ExpatError('Invalid XML', None, None)) as mock_fromstring:
        assert prestashop_instance._parse('invalid xml') is False
        mock_fromstring.assert_called_once()


def test_create(prestashop_instance):
    """Test the create method."""
    with patch.object(prestashop_instance, '_exec', return_value={'test': 'data'}) as mock_exec:
        data = {'name': 'Test Product'}
        result = prestashop_instance.create(resource='products', data=data)
        assert result == {'test': 'data'}
        mock_exec.assert_called_once_with(resource='products', method='POST', data=data, io_format='JSON')


def test_read(prestashop_instance):
    """Test the read method."""
    with patch.object(prestashop_instance, '_exec', return_value={'test': 'data'}) as mock_exec:
      result = prestashop_instance.read(resource='products', resource_id=1)
      assert result == {'test': 'data'}
      mock_exec.assert_called_once_with(resource='products', resource_id=1, method='GET', io_format='JSON')

def test_write(prestashop_instance):
    """Test the write method."""
    with patch.object(prestashop_instance, '_exec', return_value={'test': 'data'}) as mock_exec:
        data = {'id': 1, 'name': 'Updated Product'}
        result = prestashop_instance.write(resource='products', data=data)
        assert result == {'test': 'data'}
        mock_exec.assert_called_once_with(resource='products', resource_id=1, method='PUT', data=data, io_format='JSON')


def test_unlink(prestashop_instance):
    """Test the unlink method."""
    with patch.object(prestashop_instance, '_exec', return_value=True) as mock_exec:
        result = prestashop_instance.unlink(resource='products', resource_id=1)
        assert result is True
        mock_exec.assert_called_once_with(resource='products', resource_id=1, method='DELETE', io_format='JSON')


def test_search(prestashop_instance):
    """Test the search method."""
    with patch.object(prestashop_instance, '_exec', return_value=[{'id': 1, 'name': 'Test Product'}]) as mock_exec:
        result = prestashop_instance.search(resource='products', filter='[name]=%test%')
        assert result == [{'id': 1, 'name': 'Test Product'}]
        mock_exec.assert_called_once_with(resource='products', search_filter='[name]=%test%', method='GET', io_format='JSON')


@patch('src.endpoints.prestashop.api.api.open', new_callable=MagicMock)
def test_create_binary(mock_open, prestashop_instance, mock_response):
    """Test the create_binary method."""
    mock_open.return_value.__enter__.return_value.read.return_value = b"test_data"
    prestashop_instance.client.post = MagicMock(return_value=mock_response)
    result = prestashop_instance.create_binary(resource='images/products/22', file_path='test.jpeg', file_name='image')
    assert result == {'test': 'data'}
    prestashop_instance.client.post.assert_called_once()


@patch('src.endpoints.prestashop.api.api.save_text_file')
def test_save(mock_save_text_file, prestashop_instance):
    """Test the _save method."""
    data = {'test': 'data'}
    prestashop_instance._save('test.json', data)
    mock_save_text_file.assert_called_once()


def test_get_data_success(prestashop_instance):
    """Test successful data fetching with get_data."""
    with patch.object(prestashop_instance, '_exec', return_value={'test': 'data'}) as mock_exec:
        with patch.object(prestashop_instance, '_save') as mock_save:
            result = prestashop_instance.get_data(resource='products')
            assert result == {'test': 'data'}
            mock_exec.assert_called_once_with(resource='products', method='GET', io_format='JSON')
            mock_save.assert_called_once()

def test_get_data_failure(prestashop_instance):
    """Test failed data fetching with get_data."""
    with patch.object(prestashop_instance, '_exec', return_value=False):
        assert prestashop_instance.get_data(resource='products') is False

@patch('src.endpoints.prestashop.api.api.os.remove')
def test_remove_file_success(mock_remove, prestashop_instance):
    """Test successful file removal."""
    prestashop_instance.remove_file('test.txt')
    mock_remove.assert_called_once_with('test.txt')


@patch('src.endpoints.prestashop.api.api.os.remove', side_effect=Exception("Test exception"))
def test_remove_file_exception(mock_remove, prestashop_instance):
    """Test file removal with an exception."""
    with patch('src.endpoints.prestashop.api.api.logger.error') as mock_logger_error:
      prestashop_instance.remove_file('test.txt')
      mock_logger_error.assert_called_once()

def test_get_apis(prestashop_instance):
    """Test getting a list of all available APIs."""
    with patch.object(prestashop_instance, '_exec', return_value={'apis': ['products', 'categories']}) as mock_exec:
        result = prestashop_instance.get_apis()
        assert result == {'apis': ['products', 'categories']}
        mock_exec.assert_called_once_with('apis', method='GET', io_format='JSON')


def test_get_languages_schema_success(prestashop_instance):
    """Test successful fetching of the language schema."""
    with patch.object(prestashop_instance, '_exec', return_value={'languages': {'language': [{'id': 1, 'name': 'English'}]}}) as mock_exec:
        result = prestashop_instance.get_languages_schema()
        assert result == {'languages': {'language': [{'id': 1, 'name': 'English'}]}}
        mock_exec.assert_called_once_with('languages', display='full', io_format='JSON')


def test_get_languages_schema_failure(prestashop_instance):
    """Test failed fetching of the language schema."""
    with patch.object(prestashop_instance, '_exec', side_effect=Exception("Test Exception")) as mock_exec:
        with patch('src.endpoints.prestashop.api.api.logger.error') as mock_logger_error:
          result = prestashop_instance.get_languages_schema()
          assert result is None
          mock_logger_error.assert_called_once()

@patch('src.endpoints.prestashop.api.api.save_png_from_url', return_value='test.png')
@patch('src.endpoints.prestashop.api.api.PrestaShop.create_binary', return_value={'test': 'data'})
@patch('src.endpoints.prestashop.api.api.PrestaShop.remove_file')
def test_upload_image_async(mock_remove_file, mock_create_binary, mock_save_png, prestashop_instance):
  """Test the upload_image_async method."""
  result = prestashop_instance.upload_image_async(resource='images/products/22', resource_id=22, img_url='test.jpg', img_name='test')
  assert result == {'test': 'data'}
  mock_save_png.assert_called_once()
  mock_create_binary.assert_called_once()
  mock_remove_file.assert_called_once()

@patch('src.endpoints.prestashop.api.api.save_png_from_url', return_value='test.png')
@patch('src.endpoints.prestashop.api.api.PrestaShop.create_binary', return_value={'test': 'data'})
@patch('src.endpoints.prestashop.api.api.PrestaShop.remove_file')
def test_upload_image(mock_remove_file, mock_create_binary, mock_save_png, prestashop_instance):
  """Test the upload_image method."""
  result = prestashop_instance.upload_image(resource='images/products/22', resource_id=22, img_url='test.jpg', img_name='test')
  assert result == {'test': 'data'}
  mock_save_png.assert_called_once()
  mock_create_binary.assert_called_once()
  mock_remove_file.assert_called_once()


def test_get_product_images(prestashop_instance):
    """Test getting product images."""
    with patch.object(prestashop_instance, '_exec', return_value={'images': [{'id': 1}, {'id': 2}]}) as mock_exec:
        result = prestashop_instance.get_product_images(product_id=1)
        assert result == {'images': [{'id': 1}, {'id': 2}]}
        mock_exec.assert_called_once_with('products/1/images', method='GET', io_format='JSON')

```