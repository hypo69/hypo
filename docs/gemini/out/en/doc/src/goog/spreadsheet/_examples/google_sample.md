# google_sample.py

## Overview

This script demonStartes a basic usage of the Google Sheets API. It retrieves data from a specified spreadsheet and prints the values of the first and last columns.  It handles authentication using OAuth 2.0 and manages credentials for future use.


## Table of Contents

* [Authentication](#authentication)
* [Error Handling](#error-handling)
* [Main Function (`main`)](#main-function-main)
* [API Calls](#api-calls)
* [Output](#output)


## Authentication

### `main`
**Description**: The main function handles authentication with the Google Sheets API.

**Functionality**:
* Checks if a `token.json` file exists. If it does, it loads the credentials from this file.
* If no credentials are found or if the existing credentials are invalid or expired, it prompts the user to authenticate and then saves the credentials to `token.json` for later use.

### Credentials handling
**Description**: This section details the credential handling aspects within the script.

**Functionality**:
* It uses `Credentials.from_authorized_user_file` to read credentials from the `token.json` file.
* If no valid credentials exist, or if the credentials are expired, a new authorization flow is initiated. This involves obtaining client secrets (e.g., from a `credentials.json` file), setting up an `InstalledAppFlow`, and running a local server for user authorization.
* The obtained credentials are then saved in the `token.json` file.


## Error Handling

### `try...except` Block
**Description**: This section explains the error handling mechanism in place.

**Functionality**: The `try...except` block catches potential `HttpError` exceptions that might occur during API calls. If such an error occurs, it prints the error message to the console, which helps in debugging.

## Main Function (`main`)

### `main`
**Description**: This function is the entry point of the script and orcheStartes the data retrieval and printing process.

**Functionality**:
* Initializes credentials.
* Builds a Sheets API service instance.
* Executes an API call to retrieve data from the specified spreadsheet.
* Handles potential exceptions during the API call, including printing appropriate error messages if any occur.
* Processes the retrieved data. If no data is found, it prints a message and exits.
* Prints the desired values.


## API Calls

### `service.spreadsheets().values().get()`
**Description**: This method retrieves the values from a specified range in a spreadsheet.

**Parameters**:
* `spreadsheetId` (str): The ID of the spreadsheet.
* `range` (str): The range of cells to retrieve.

**Returns**:
* `result` (dict): A dictionary containing the retrieved data.

**Raises**:
* `HttpError`: If there is an error during the API call.


## Output

**Description**: This section describes the output format.

**Functionality**: The script prints the values from the specified columns (column A and column E) of the spreadsheet to the console in a comma-separated format.


## Example Usage


```
Name, Major:
John Doe,Computer Science
Jane Smith,Math
...
```


```
```
```


```
```
```

```