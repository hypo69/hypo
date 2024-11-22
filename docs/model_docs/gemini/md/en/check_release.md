# check_release.py

## Overview

This module contains a function to check the latest release version of a GitHub repository.


## Table of Contents

- [check_latest_release](#check_latest_release)


## Functions

### `check_latest_release`

**Description**: This function fetches the latest release version from a GitHub repository.

**Parameters**:
- `owner` (str): The owner of the GitHub repository.
- `repo` (str): The name of the GitHub repository.

**Returns**:
- `str`: The latest release tag name, or `None` if no release is found or there's an error.

**Raises**:
- `requests.exceptions.RequestException`: An error occurred during the HTTP request.


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
```
