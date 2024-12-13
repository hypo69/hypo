```python
import pytest
import os

# Mock IopClient and IopRequest classes for testing purposes
class MockIopClient:
    def __init__(self, url, appkey, appSecret):
        self.url = url
        self.appkey = appkey
        self.appSecret = appSecret

    def execute(self, request):
        # Simulate API response
        response = MockIopResponse()
        if request.params.get('file_name') == 'pom.xml':
            response.type = 'nil'
            response.code = 0
            response.message = 'success'
            response.body = '{"status": "success", "file_name": "pom.xml"}'
        elif request.params.get('file_name') == None:
            response.type = 'ISV'
            response.code = 400
            response.message = 'file_name is required'
            response.body = '{"error": "file_name is required"}'
        elif request.params.get('file_name') == 'invalid_file_name':
            response.type = 'ISV'
            response.code = 400
            response.message = 'invalid file_name'
            response.body = '{"error": "invalid file_name"}'
        elif request.params.get('file_bytes') == None:
            response.type = 'ISV'
            response.code = 400
            response.message = 'file_bytes is required'
            response.body = '{"error": "file_bytes is required"}'
        else:
             response.type = 'SYSTEM'
             response.code = 500
             response.message = 'server error'
             response.body = '{"error": "server error"}'
        return response


class MockIopRequest:
    def __init__(self, api_path):
        self.api_path = api_path
        self.params = {}
        self.file_params = {}

    def add_api_param(self, key, value):
        self.params[key] = value

    def add_file_param(self, key, value):
        self.file_params[key] = value

class MockIopResponse:
    def __init__(self):
        self.type = None
        self.code = None
        self.message = None
        self.request_id = 'test_request_id'
        self.body = None

@pytest.fixture
def mock_iop_client():
    """Provides a mock IopClient instance."""
    return MockIopClient('https://api.taobao.tw/rest', 'test_appKey', 'test_appSecret')

@pytest.fixture
def mock_pom_file():
   """Provides a mock pom.xml file for testing"""
   with open('mock_pom.xml', 'w') as f:
        f.write("<project></project>")
   yield 'mock_pom.xml'
   os.remove('mock_pom.xml')

def test_upload_valid_file(mock_iop_client, mock_pom_file):
    """Tests successful file upload with valid file name and content."""
    request = MockIopRequest('/xiaoxuan/mockfileupload')
    request.add_api_param('file_name', 'pom.xml')
    
    with open(mock_pom_file, 'r') as f:
        file_content = f.read()
    request.add_file_param('file_bytes', file_content)
    
    response = mock_iop_client.execute(request)
    
    assert response.type == 'nil'
    assert response.code == 0
    assert response.message == 'success'
    assert 'status' in response.body
    assert 'file_name' in response.body

def test_upload_missing_file_name(mock_iop_client, mock_pom_file):
    """Tests file upload with missing file name, should return error."""
    request = MockIopRequest('/xiaoxuan/mockfileupload')
    with open(mock_pom_file, 'r') as f:
        file_content = f.read()
    request.add_file_param('file_bytes', file_content)
    response = mock_iop_client.execute(request)
    assert response.type == 'ISV'
    assert response.code == 400
    assert response.message == 'file_name is required'

def test_upload_missing_file_content(mock_iop_client):
    """Tests file upload with missing file content, should return error."""
    request = MockIopRequest('/xiaoxuan/mockfileupload')
    request.add_api_param('file_name', 'pom.xml')
    response = mock_iop_client.execute(request)
    assert response.type == 'ISV'
    assert response.code == 400
    assert response.message == 'file_bytes is required'


def test_upload_invalid_file_name(mock_iop_client, mock_pom_file):
    """Tests file upload with invalid file name, should return error."""
    request = MockIopRequest('/xiaoxuan/mockfileupload')
    request.add_api_param('file_name', 'invalid_file_name')
    with open(mock_pom_file, 'r') as f:
        file_content = f.read()
    request.add_file_param('file_bytes', file_content)
    response = mock_iop_client.execute(request)
    assert response.type == 'ISV'
    assert response.code == 400
    assert response.message == 'invalid file_name'

def test_upload_server_error(mock_iop_client):
    """Tests file upload with unexpected condition, should return server error."""
    request = MockIopRequest('/xiaoxuan/mockfileupload')
    request.add_api_param('file_name', 'test_file')
    request.add_file_param('file_bytes', 'test_content')
    response = mock_iop_client.execute(request)
    assert response.type == 'SYSTEM'
    assert response.code == 500
    assert response.message == 'server error'
```