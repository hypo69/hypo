```python
import pytest
import requests
import time
import hmac
import hashlib
import json
import logging
import os
from os.path import expanduser
import socket
import platform
from unittest.mock import patch, Mock

# Import the code to be tested
from hypotez.src.suppliers.aliexpress.api._examples.iop.base import (
    sign,
    mixStr,
    logApiError,
    IopRequest,
    IopResponse,
    IopClient,
    P_SDK_VERSION,
    P_APPKEY,
    P_ACCESS_TOKEN,
    P_TIMESTAMP,
    P_SIGN,
    P_SIGN_METHOD,
    P_PARTNER_ID,
    P_METHOD,
    P_DEBUG,
    P_SIMPLIFY,
    P_FORMAT,
    P_CODE,
    P_TYPE,
    P_MESSAGE,
    P_REQUEST_ID,
    P_LOG_LEVEL_DEBUG,
    P_LOG_LEVEL_INFO,
    P_LOG_LEVEL_ERROR,
)

# Fixture definitions
@pytest.fixture
def mock_logger():
    """Mocks the logger to avoid actual log file creation"""
    with patch('hypotez.src.suppliers.aliexpress.api._examples.iop.base.logger') as mock:
        yield mock

@pytest.fixture
def mock_requests_post():
    with patch('hypotez.src.suppliers.aliexpress.api._examples.iop.base.requests.post') as mock_post:
        yield mock_post
        
@pytest.fixture
def mock_requests_get():
    with patch('hypotez.src.suppliers.aliexpress.api._examples.iop.base.requests.get') as mock_get:
        yield mock_get


@pytest.fixture
def example_iop_client():
    """Provides an example IopClient instance"""
    return IopClient("https://example.com/api", "test_app_key", "test_app_secret")


@pytest.fixture
def example_iop_request():
    """Provides an example IopRequest instance"""
    return IopRequest("test.method")

@pytest.fixture
def example_api_params():
    """Provides example API parameters for tests."""
    return {"param1": "value1", "param2": "value2"}

@pytest.fixture
def example_file_params():
    """Provides example file parameters for tests."""
    return {"file1": "file_content"}

# Tests for sign function
def test_sign_valid_input():
    """Checks sign generation with valid input."""
    secret = "test_secret"
    api = "test.api"
    params = {"param1": "value1", "param2": "value2"}
    expected_signature = hmac.new(secret.encode(encoding="utf-8"), "param1value1param2value2".encode(encoding="utf-8"), digestmod=hashlib.sha256).hexdigest().upper()
    assert sign(secret, api, params) == expected_signature

def test_sign_api_with_slash():
    """Checks sign generation when API contains a slash."""
    secret = "test_secret"
    api = "/test/api"
    params = {"param1": "value1", "param2": "value2"}
    expected_signature = hmac.new(secret.encode(encoding="utf-8"), "/test/api"+"param1value1param2value2".encode(encoding="utf-8"), digestmod=hashlib.sha256).hexdigest().upper()
    assert sign(secret, api, params) == expected_signature

def test_sign_empty_params():
    """Checks sign generation with empty params."""
    secret = "test_secret"
    api = "test.api"
    params = {}
    expected_signature = hmac.new(secret.encode(encoding="utf-8"), "".encode(encoding="utf-8"), digestmod=hashlib.sha256).hexdigest().upper()
    assert sign(secret, api, params) == expected_signature

def test_sign_special_characters():
    """Checks sign generation with special characters in params."""
    secret = "test_secret"
    api = "test.api"
    params = {"param1": "value with spaces", "param2": "!@#$%^"}
    expected_signature = hmac.new(secret.encode(encoding="utf-8"), "param1value with spacesparam2!@#$%^".encode(encoding="utf-8"), digestmod=hashlib.sha256).hexdigest().upper()
    assert sign(secret, api, params) == expected_signature

# Tests for mixStr function
def test_mixStr_string():
    """Checks mixStr with a string input."""
    assert mixStr("test") == "test"

def test_mixStr_unicode():
    """Checks mixStr with a unicode input."""
    assert mixStr("test") == "test"

def test_mixStr_int():
    """Checks mixStr with an integer input."""
    assert mixStr(123) == "123"

def test_mixStr_float():
    """Checks mixStr with a float input."""
    assert mixStr(12.3) == "12.3"
    
# Tests for logApiError function
def test_logApiError(mock_logger):
    """Checks if logApiError logs correct message."""
    appkey = "test_appkey"
    sdkVersion = "test_sdk_version"
    requestUrl = "test_url"
    code = "test_code"
    message = "test_message"

    logApiError(appkey, sdkVersion, requestUrl, code, message)

    mock_logger.error.assert_called_once()
    logged_message = mock_logger.error.call_args[0][0]
    assert appkey in logged_message
    assert sdkVersion in logged_message
    assert requestUrl in logged_message
    assert code in logged_message
    assert message in logged_message
    

# Tests for IopRequest class
def test_iop_request_init():
    """Checks IopRequest initialization."""
    request = IopRequest("test.api", "GET")
    assert request._api_params == {}
    assert request._file_params == {}
    assert request._api_pame == "test.api"
    assert request._http_method == "GET"
    assert request._simplify == "false"
    assert request._format == "json"

def test_iop_request_add_api_param(example_iop_request,example_api_params):
    """Checks adding api parameters."""
    example_iop_request.add_api_param("param1", "value1")
    example_iop_request.add_api_param("param2", "value2")
    assert example_iop_request._api_params == example_api_params

def test_iop_request_add_file_param(example_iop_request,example_file_params):
    """Checks adding file parameters."""
    example_iop_request.add_file_param("file1", "file_content")
    assert example_iop_request._file_params == example_file_params

def test_iop_request_set_simplify(example_iop_request):
    """Checks setting simplify parameter."""
    example_iop_request.set_simplify()
    assert example_iop_request._simplify == "true"
    
def test_iop_request_set_format(example_iop_request):
    """Checks setting the format parameter."""
    example_iop_request.set_format("xml")
    assert example_iop_request._format == "xml"

# Tests for IopResponse class
def test_iop_response_init():
    """Checks IopResponse initialization."""
    response = IopResponse()
    assert response.type is None
    assert response.code is None
    assert response.message is None
    assert response.request_id is None
    assert response.body is None

def test_iop_response_str():
    """Checks IopResponse string representation."""
    response = IopResponse()
    response.type = "test_type"
    response.code = "123"
    response.message = "test_message"
    response.request_id = "test_id"
    
    expected_string = "type=test_type code=123 message=test_message requestId=test_id"
    assert str(response) == expected_string
    
def test_iop_response_str_with_none():
    """Checks IopResponse string representation when fields are None."""
    response = IopResponse()

    expected_string = "type=None code=None message=None requestId=None"
    assert str(response) == expected_string

# Tests for IopClient class
def test_iop_client_init():
    """Checks IopClient initialization."""
    client = IopClient("https://example.com/api", "test_app_key", "test_app_secret", 60)
    assert client._server_url == "https://example.com/api"
    assert client._app_key == "test_app_key"
    assert client._app_secret == "test_app_secret"
    assert client._timeout == 60

def test_iop_client_execute_get_request(example_iop_client, example_iop_request, mock_requests_get):
    """Checks the execution of a GET request."""
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    mock_requests_get.return_value = mock_response
    
    response = example_iop_client.execute(example_iop_request)
    
    mock_requests_get.assert_called_once()
    assert response.code == "0"
    assert response.type == "success"
    assert response.message == "OK"
    assert response.request_id == "test_request_id"
    assert response.body == {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}

def test_iop_client_execute_post_request(example_iop_client, example_iop_request, mock_requests_post):
    """Checks the execution of a POST request."""
    example_iop_request._http_method = "POST"
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    mock_requests_post.return_value = mock_response
    
    response = example_iop_client.execute(example_iop_request)
    
    mock_requests_post.assert_called_once()
    assert response.code == "0"
    assert response.type == "success"
    assert response.message == "OK"
    assert response.request_id == "test_request_id"
    assert response.body == {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    
def test_iop_client_execute_post_with_file_param(example_iop_client, example_iop_request,mock_requests_post,example_file_params):
    """Checks the execution of a POST request with file parameters."""
    example_iop_request._http_method = "POST"
    example_iop_request._file_params = example_file_params
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    mock_requests_post.return_value = mock_response
    
    response = example_iop_client.execute(example_iop_request)
    
    mock_requests_post.assert_called_once()
    assert response.code == "0"
    assert response.type == "success"
    assert response.message == "OK"
    assert response.request_id == "test_request_id"
    assert response.body == {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    
def test_iop_client_execute_with_access_token(example_iop_client, example_iop_request, mock_requests_get):
    """Checks the execution of a request with access token."""
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    mock_requests_get.return_value = mock_response
    
    access_token = "test_access_token"
    response = example_iop_client.execute(example_iop_request, access_token)
    
    mock_requests_get.assert_called_once()
    
    assert response.code == "0"
    assert response.type == "success"
    assert response.message == "OK"
    assert response.request_id == "test_request_id"
    assert response.body == {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    
def test_iop_client_execute_api_error(example_iop_client, example_iop_request, mock_requests_get, mock_logger):
    """Checks the behavior when API returns an error code."""
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "100", P_TYPE: "error", P_MESSAGE: "Test error", P_REQUEST_ID: "test_request_id"}
    mock_requests_get.return_value = mock_response

    response = example_iop_client.execute(example_iop_request)

    mock_logger.error.assert_called_once()
    assert response.code == "100"
    assert response.type == "error"
    assert response.message == "Test error"
    assert response.request_id == "test_request_id"

def test_iop_client_execute_http_error(example_iop_client, example_iop_request, mock_requests_get):
    """Checks the handling of HTTP errors during request execution."""
    mock_requests_get.side_effect = requests.exceptions.RequestException("HTTP Error")
    with pytest.raises(requests.exceptions.RequestException, match="HTTP Error"):
        example_iop_client.execute(example_iop_request)

def test_iop_client_execute_debug_log(example_iop_client, example_iop_request, mock_requests_get, mock_logger):
    """Checks if the log message is present when debug level is set."""
    example_iop_client.log_level = P_LOG_LEVEL_DEBUG
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    mock_requests_get.return_value = mock_response

    example_iop_client.execute(example_iop_request)

    mock_logger.error.assert_called_once()
    logged_message = mock_logger.error.call_args[0][0]
    assert "test_app_key" in logged_message
    assert "iop-sdk-python-20220609" in logged_message

def test_iop_client_execute_info_log(example_iop_client, example_iop_request, mock_requests_get, mock_logger):
    """Checks if the log message is present when info level is set."""
    example_iop_client.log_level = P_LOG_LEVEL_INFO
    mock_response = Mock()
    mock_response.json.return_value = {P_CODE: "0", P_TYPE: "success", P_MESSAGE: "OK", P_REQUEST_ID: "test_request_id"}
    mock_requests_get.return_value = mock_response

    example_iop_client.execute(example_iop_request)

    mock_logger.error.assert_called_once()
    logged_message = mock_logger.error.call_args[0][0]
    assert "test_app_key" in logged_message
    assert "iop-sdk-python-20220609" in logged_message
```