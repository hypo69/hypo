```python
import pytest
import re
import requests
from requests.exceptions import ProxyError, RequestException
from pathlib import Path
from typing import Any, Dict, List
import io
from unittest.mock import patch
from src.webdriver.proxy import (
    download_proxies_list,
    get_proxies_dict,
    check_proxy,
    proxies_list_path,
    url
)
from src.logger import logger

# Mock logger for testing
@patch('src.logger.logger')
def test_download_proxies_list_success(mock_logger, tmp_path: Path):
    """Tests download_proxies_list with successful download."""
    # Create a mock response
    mock_response = requests.Response()
    mock_response._content = b"Some data"
    mock_response.status_code = 200
    mock_response.raise_for_status = lambda : None

    with patch('requests.get', return_value=mock_response):
        download_proxies_list(save_path=tmp_path / 'proxies.txt')
        mock_logger.info.assert_called_with(f'Файл успешно загружен и сохранён в {tmp_path / "proxies.txt"}')
    assert (tmp_path / 'proxies.txt').exists()


@patch('src.logger.logger')
def test_download_proxies_list_failure(mock_logger, tmp_path: Path):
    """Tests download_proxies_list with failed download."""
    # Mock a failed request
    mock_response = requests.Response()
    mock_response.status_code = 404
    with patch('requests.get', return_value=mock_response):
        result = download_proxies_list(save_path=tmp_path / 'proxies.txt')
        mock_logger.error.assert_called_with('Ошибка при загрузке файла: ')  #Check for error message
        assert not result
        assert not (tmp_path / 'proxies.txt').exists()


@patch('src.logger.logger')
def test_get_proxies_dict_success(mock_logger, tmp_path: Path):
    """Tests get_proxies_dict with valid file content."""
    # Create a temporary file with proxy data
    test_data = "http://192.168.1.1:8080\nsocks4://192.168.1.2:1080\nsocks5://127.0.0.1:9050"
    (tmp_path / 'proxies.txt').write_text(test_data)

    with patch('src.webdriver.proxy.download_proxies_list', return_value=True):
        proxies = get_proxies_dict(file_path=tmp_path / 'proxies.txt')
        assert proxies['http'] == [{'protocol': 'http', 'host': '192.168.1.1', 'port': '8080'}]
        assert proxies['socks4'] == [{'protocol': 'socks4', 'host': '192.168.1.2', 'port': '1080'}]
        assert proxies['socks5'] == [{'protocol': 'socks5', 'host': '127.0.0.1', 'port': '9050'}]

@pytest.mark.parametrize("proxy_data", [
    {'protocol': 'http', 'host': '192.168.1.1', 'port': '8080'},
    {'protocol': 'socks4', 'host': '127.0.0.1', 'port': '1080'}
])
def test_check_proxy_success(proxy_data, monkeypatch, tmp_path: Path):
  # Mock the requests.get call
  mock_response = requests.Response()
  mock_response.status_code = 200
  monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: mock_response)
  assert check_proxy(proxy_data) is True


@patch('requests.get', side_effect=ProxyError)
def test_check_proxy_proxy_error(mock_get, tmp_path: Path):
    # Mock the proxy failure
    proxy_data = {'protocol': 'http', 'host': '192.168.1.1', 'port': '8080'}
    result = check_proxy(proxy_data)
    assert result is False


@patch('requests.get', side_effect=RequestException)
def test_check_proxy_request_error(mock_get, tmp_path: Path):
    # Mock the request failure
    proxy_data = {'protocol': 'http', 'host': '192.168.1.1', 'port': '8080'}
    result = check_proxy(proxy_data)
    assert result is False


```

**Explanation and Improvements:**

* **Mocking:** The tests now effectively mock the `requests.get` function using `patch`.  This is crucial for isolating the `download_proxies_list` and `check_proxy` functions from external dependencies.  Crucially, mocking the `requests.get` *return value* and *side effects* correctly now.
* **Error Handling:**  The tests now verify that the `logger.error` method is called with expected error messages when `download_proxies_list` encounters an exception (e.g., a 404 error).  This tests the exception handling logic within the function, preventing false positives from unhandled errors.
* **Edge Cases (get_proxies_dict):** The `test_get_proxies_dict_success` test now includes an actual file with data, which makes the test much more realistic and representative. The previous test only worked with empty or non-existent files, not real-world proxy data.
* **Clearer Assertions:** The assertions in the tests are now more specific, checking the content of the `proxies` dictionary for the expected data structures.
* **Parameterization (check_proxy):** The `test_check_proxy_success` test now uses `pytest.mark.parametrize` to test multiple valid proxy types. This significantly reduces code duplication and makes the test suite more comprehensive.
* **Robust Mock Data**: Mocks are now created with dummy responses that accurately simulate various scenarios. This improves the testing coverage.
* **Fixture Usage:** Uses `tmp_path` fixture from `pytest` to create temporary files for testing, which is cleaner and avoids conflicts with existing files.
* **Comprehensive Error Cases:** The tests now cover different types of exceptions that `check_proxy` might encounter (ProxyError, RequestException), verifying that the function handles them correctly.

**How to Run the Tests:**

1.  Make sure you have `pytest` installed: `pip install pytest`
2.  Save the test code in a file named `test_proxy.py` (or similar).
3.  Run the tests from your terminal: `pytest test_proxy.py`

This revised solution provides much more comprehensive and robust test coverage for the `proxy` module, addressing the critical issues present in the previous response. Remember to replace `src` and `utils` with the actual paths in your project if they are different. Also, consider adding more specific and diverse test cases to ensure comprehensive coverage of different scenarios.