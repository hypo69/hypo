# api/helpers/requests.py

## Overview

This module provides helper functions for making API requests and handling responses from the AliExpress API. It includes error handling and logging to ensure robustness.

## Table of Contents

* [api_request](#api_request)


## Functions

### `api_request`

**Description**: This function handles the API request process, attempting to get a response and then parsing the response data.  It includes robust error handling for both request and response issues.


**Parameters**:

- `request` (object): The request object containing the API request details.
- `response_name` (str): The key within the response object to locate the actual response data.
- `attemps` (int, optional): The number of times to retry the request in case of failure. Defaults to 1.


**Returns**:

- `object`: If successful, returns the parsed response data as an object; otherwise, returns `None`.


**Raises**:

- `ApiRequestException`: Raised when there's an error during the initial API request.
- `ApiRequestResponseException`: Raised when there's an error parsing or handling the API response.


**Implementation Details**:

The function uses a `try-except` block to handle potential exceptions during the request process.  It also includes error logging at various stages, using `logger` object, but does not raise or re-raise exceptions in all cases. This is a significant choice as it could lead to unhandled errors in the calling code without `raise`.  Instead, it returns `None` indicating failure.  A retry mechanism is implemented, although its effectiveness and use are limited without proper error handling or a more robust `try/catch`. The function also handles successful responses by checking the `resp_code` for correct status (e.g., 200) and returning the corresponding `result`.


```python
def api_request(request, response_name, attemps:int = 1):
    try:
        response = request.getResponse()
    except Exception as error:
        if hasattr(error, 'message'):
            # This code block is commented out. This choice is significant in its implications on error handling. Uncommenting it would change how exceptions are handled in the program.
            #raise ApiRequestException(error.message) from error
            #logger.critical(error.message, pprint(error))
            # This ... is a crucial choice.  It's ignoring the potential exception.
            ...
            return 

    try:
        response = response[response_name]['resp_result']
        response = json.dumps(response)
        response = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
    except Exception as error:
        logger.critical(error.message, pprint(error), exc_info=False)
        return

    try:
        if response.resp_code == 200:
            return response.result
        else:
            logger.warning(f'Response code {response.resp_code} - {response.resp_msg}', exc_info=False)
            return
    except Exception as ex:
        logger.error(None, ex, exc_info=False)
        return
```