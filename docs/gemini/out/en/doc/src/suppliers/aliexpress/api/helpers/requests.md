# hypotez/src/suppliers/aliexpress/api/helpers/requests.py

## Overview

This module contains helper functions for making API requests to AliExpress, specifically focusing on handling potential errors and parsing responses. It includes the `api_request` function for managing requests, and uses the `logger` and `pprint` utilities for logging and debugging.


## Functions

### `api_request`

**Description**: This function handles making an API request, handling potential errors during the request and response processing.  It attempts to retrieve a response from the request object.  If successful, it parses the response, checks the response code, and returns the relevant result.

**Parameters**:

- `request`: (`object`): The request object.
- `response_name` (`str`): The name of the key in the response dictionary containing the result.
- `attemps` (`int`, optional): The number of times to retry the request. Defaults to 1.


**Returns**:

- `object | None`: Returns the parsed API result if the request and response processing are successful. If there are errors, returns `None`.  Returns the parsed result if the `resp_code` is 200. Logs an error if the `resp_code` is not 200.


**Raises**:

- `ApiRequestException`: Raised if an error occurs during the request.
- `ApiRequestResponseException`: Raised if an error occurs during response processing or if the response status code is not 200.


```
```python
def api_request(request, response_name, attemps:int = 1):
    try:
        response = request.getResponse()
    except Exception as error:
        logger.critical(f"Error during request: {error.message}", pprint(error), exc_info=False)
        return None

    try:
        response = response[response_name]['resp_result']
        response = json.dumps(response)
        response = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
    except Exception as error:
        logger.critical(f"Error parsing response: {error.message}", pprint(error), exc_info=False)
        return None

    try:
        if response.resp_code == 200:
            return response.result
        else:
            logger.warning(f"API request failed: Response code {response.resp_code} - {response.resp_msg}", exc_info=False)
            return None
    except Exception as ex:
        logger.error("Error processing response:", ex, exc_info=False)
        return None
```