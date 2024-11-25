# check_release.py

## Overview

This module provides functions for checking the latest release version of a GitHub repository.  It uses the GitHub API to retrieve release information.


## Table of Contents

* [check_latest_release](#check_latest_release)


## Functions

### `check_latest_release`

**Description**: Checks the latest release version of a GitHub repository.

**Parameters**:
- `owner` (str): The owner of the repository.
- `repo` (str): The name of the repository.

**Returns**:
- `str`: The latest release version if available, else `None`.


**Raises**:
- `requests.exceptions.RequestException`: If there is an error during the API request.  (e.g., network issues, invalid API key).
- `Exception`: If there's an issue processing the API response.


```python
def check_latest_release(owner: str, repo: str):
    """Check the latest release version of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        str: The latest release version if available, else None.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    response = requests.get(url)

    if response.status_code == 200:
        latest_release = response.json()
        return latest_release['tag_name']
    else:
        #logger.error(f"Error fetching data: {response.status_code}")
        #TODO: Код не проверен
        return None