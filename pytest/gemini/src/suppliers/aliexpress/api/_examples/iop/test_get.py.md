```python
import pytest
import iop  # Assuming iop is installed or in the PYTHONPATH

# Fixture for creating a client for testing
@pytest.fixture
def iop_client():
    """Provides an iop client for testing."""
    return iop.IopClient('https://api-pre.aliexpress.com/sync', '33505222', 'e1fed6b34feb26aabc391d187732af93')

# Fixture for creating a request object
@pytest.fixture
def iop_request():
    """Provides an iop request object for testing."""
    request = iop.IopRequest('aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST')
    request.set_simplify()
    request.add_api_param('seller_address_query','pickup')
    return request

def test_iop_client_creation(iop_client):
    """Checks if an IopClient can be created successfully."""
    assert isinstance(iop_client, iop.IopClient)
    assert iop_client.gateway_url == 'https://api-pre.aliexpress.com/sync'
    assert iop_client.appkey == '33505222'
    assert iop_client.appSecret == 'e1fed6b34feb26aabc391d187732af93'
    
def test_iop_request_creation(iop_request):
    """Checks if an IopRequest can be created and configured."""
    assert isinstance(iop_request, iop.IopRequest)
    assert iop_request.api_name == 'aliexpress.logistics.redefining.getlogisticsselleraddresses'
    assert iop_request.http_method == 'POST'
    assert iop_request.simplify == True
    assert 'seller_address_query' in iop_request.api_params
    assert iop_request.api_params['seller_address_query'] == 'pickup'

def test_iop_execute_valid_request(iop_client, iop_request):
    """Checks the execution of a valid request and the response."""
    # This test assumes that the client.execute method will return an iop.IopResponse object
    # with valid data.
    response = iop_client.execute(iop_request,"50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL")
    assert isinstance(response, iop.IopResponse)
    # Assertions on type, code, message, request_id, body are not feasible without knowing
    # the exact expected data from the API, however we can check that the attributes exist
    assert hasattr(response, 'type')
    assert hasattr(response, 'code')
    assert hasattr(response, 'message')
    assert hasattr(response, 'request_id')
    assert hasattr(response, 'body')

def test_iop_execute_invalid_token(iop_client, iop_request):
     """Checks the execution with invalid token"""
     response = iop_client.execute(iop_request,"invalid_token")
     assert isinstance(response, iop.IopResponse)
     #  we expect the API to return an error when an invalid token is passed
     assert response.code != 0
     assert response.type != "nil"


def test_iop_request_missing_param(iop_client):
    """Checks the execution when a required parameter is missing."""
    request = iop.IopRequest('aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST')
    request.set_simplify()
    with pytest.raises(Exception) as excinfo: # Assuming the missing parameter raises an error during execution
         iop_client.execute(request,"50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL") # Here a parameter is missing so we expect an exception
    assert "api_params" in str(excinfo.value) # Ensure the error is related to missing parameter
    
def test_iop_client_invalid_url():
    """Checks exception when creating an iop client with invalid URL"""
    with pytest.raises(ValueError) as excinfo:
         iop.IopClient("invalid url","test_key", "test_secret") 
    assert "Invalid URL format" in str(excinfo.value)
```