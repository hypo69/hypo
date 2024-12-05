# check_release.py

## Overview

This module provides a function to check the latest release version of a GitHub repository.  It utilizes the GitHub API to fetch release information.


## Table of Contents

- [check_latest_release](#check_latest_release)


## Functions

### `check_latest_release`

**Description**: This function retrieves the latest release tag name from a GitHub repository.

**Parameters**:

- `owner` (str): The owner of the GitHub repository.
- `repo` (str): The name of the GitHub repository.


**Returns**:

- `str`: The latest release tag name as a string, or `None` if no release is found or if there's an error contacting the GitHub API.


**Raises**:

- `requests.exceptions.RequestException`:  An error occurred during the HTTP request (e.g., network issues, invalid API key).