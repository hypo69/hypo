
# FastAPI Server Manager

This project provides tools for managing FastAPI servers, including:

- An interactive CLI tool in Python for managing servers.
- An interactive PowerShell script for managing servers.

## Features

-   **Singleton Pattern:** Ensures that only one instance of the FastAPI server is managed through the CLI.
-   **Interactive Management:** Starts the server once, then manages its state (start, stop, view status) through commands.
-   **Customizable Options:** Ability to specify the port and host for starting servers.
-   **Asynchronous Management:** Uses `asyncio` for asynchronous server start and stop operations (in Python CLI).
-   **Status Tracking:** Ability to view the status of the server and all its running ports.
-   **Collision Prevention:** Uses a mutex (in the PowerShell script) to ensure that only one instance of the script can be run at a time.
-   **Interactive Menu:** Provides a user-friendly command-line interface through PowerShell.
-   **Port Checking:** Checks the availability of ports before starting servers (in the PowerShell script).
-   **Error Handling:** Logs errors during script execution.

## Requirements

-   Python 3.7+
-   Windows (for the PowerShell script)
-   PowerShell 5.1 or higher (for the PowerShell script)
-   Installed dependencies (for Python CLI):
    -   `typer`
    -   `uvicorn`
    -   `fastapi`
    -   `pydantic`
    -   `loguru` (or a similar logging module)

## Installation

1.  Clone the repository (if applicable) or copy the files.
2.  **For Python CLI (main.py):**
    *   It is recommended to create a virtual environment.
    *   Install the necessary dependencies, for example, via: `pip install -r requirements.txt`, or manually (if `requirements.txt` is missing) `pip install typer uvicorn fastapi pydantic loguru`.
3.  **For the PowerShell script (server_manager.ps1):**
    *   Ensure that `python.exe` is installed and accessible through the `PATH` environment variable.

## Usage

### Python CLI

1.  Make sure the `main.py` (Python CLI) file is in your working directory.
2.  Run the CLI using Python:

    ```bash
    python main.py <command> [options]
    ```

#### Commands

-   **`start`:** Initializes and starts the FastAPI server.
    -   `--port`: (Optional) The port to start the server on (default: 8000).
    -   `--host`: (Optional) The host address for the server (default: 0.0.0.0).

    Example:

    ```bash
    python main.py start --port 8080
    python main.py start --port 8081 --host 127.0.0.1
    ```

    *Note:* If the server is already initialized, a message will be displayed, and the server cannot be reinitialized.
-   **`stop`:** Stops the FastAPI server on the specified port.
    -   `--port`: (Required) The port of the server to stop.

    Example:

    ```bash
    python main.py stop --port 8080
    ```

    *Note:* You cannot stop the server if it has not been started.
-   **`stop-all`:** Stops all running FastAPI servers.

    Example:

    ```bash
    python main.py stop-all
    ```

    *Note:* You cannot stop the server if it has not been started.
-   **`status`:** Displays the status of the server and all its running ports.

    Example:

    ```bash
    python main.py status
    ```

    *Note:* This will only display information if the server has been started.
-   **`--help`:** Displays help information for the commands.

    Example:

    ```bash
    python main.py --help
    python main.py start --help
    ```

#### Example Usage of Python CLI

1.  **Start Server:** Start the server on port 8000:

    ```bash
    python main.py start --port 8000
    ```

2.  **View Status:** View the status of the server and its running ports:

    ```bash
    python main.py status
    ```

3.  **Attempt to Restart:** Attempt to start the server on a different port (e.g., 8081):

    ```bash
    python main.py start --port 8081
    ```

    A message will be displayed in the console indicating that the server has already been started.

4.  **Stop Server on port 8000:** Stop the server on port 8000:

    ```bash
    python main.py stop --port 8000
    ```

5.  **View Status after Stop:** View the status of the server:

    ```bash
    python main.py status
    ```

    A message will be displayed indicating that the server is not running on port 8000.
6.  **Stop All Servers:**

    ```bash
    python main.py stop-all
    ```

7.  **View Status after Stopping All Servers:**

    ```bash
    python main.py status
    ```

    A message will be displayed in the console indicating that the server has not been initialized.

### PowerShell Script

1.  Make sure the `server_manager.ps1` (PowerShell Script) and `main.py` (Python CLI) files are in the same directory or specify the correct path to `main.py` in the `$pythonScriptPath` variable.
2.  Run PowerShell as an administrator.
3.  Navigate to the directory where the `server_manager.ps1` file is located.
4.  Execute the script:

    ```powershell
    .\server_manager.ps1
    ```

#### Menu

After starting the script, you will see the menu:

```
FastAPI Server Manager
----------------------
1. Start Server
2. Stop Server
3. Stop All Servers
4. Get Server Status
5. Exit
```

Select an option by entering the corresponding number (1-5) and press Enter.

#### Menu Commands

-   **`1. Start Server`:**
    -   Prompts for a port (default: 8000).
    -   Prompts for a host (default: 0.0.0.0).
        - You can skip entering the host or port, in which case the default values ​​will be used.
    -   Checks if the port is available.
    -   Calls the Python CLI `main.py` to start the FastAPI server.

-   **`2. Stop Server`:**
    -   Prompts for the port of the server to stop.
    -   Calls the Python CLI `main.py` to stop the FastAPI server on the specified port.

-   **`3. Stop All Servers`:**
    -   Calls the Python CLI `main.py` to stop all running FastAPI servers.

-   **`4. Get Server Status`:**
    -   Calls the Python CLI `main.py` to display the status of all running FastAPI servers.

-   **`5. Exit`:**
    -   Exits the script.

#### Example Usage of PowerShell Script

1.  **Start Server:**
    -   Select `1`.
    -   Enter a port, e.g., `8080` (or leave it blank to use the default port `8000`).
    -   Enter a host, e.g., `127.0.0.1` (or leave it blank to use the default host `0.0.0.0`).
2.  **Stop Server:**
    -   Select `2`.
    -   Enter the port, e.g., `8080`.
3.  **Stop All Servers**
    -   Select `3`.
4.  **View Status:**
    -  Select `4`.
5.  **Exit**
    -  Select `5`.

#### PowerShell Script Protection against Simultaneous Launch
The script uses a mutex to ensure that only one instance of the script can be run at any time. If you try to run a second instance, it will exit with an error.

## Architecture

-   `FastApiServer`: Singleton class representing the FastAPI application and managing server startup (in `main.py`).
-   `main.py`: Contains the CLI commands and logic for interactive server management in Python.
-   `server_manager.ps1`: PowerShell script providing an interactive interface for managing the FastAPI server through the Python CLI.
-   `typer`: Library used for creating the command-line interface (in `main.py`).
-   `uvicorn`: ASGI web server for running the FastAPI application (in `main.py`).
-   `Test-NetConnection`: PowerShell cmdlet for checking ports (in `server_manager.ps1`).
-   `System.Threading.Mutex`: .NET class for implementing a mutex (in `server_manager.ps1`).
-   `python.exe`: Invokes Python to run CLI commands in `main.py` (in `server_manager.ps1`).

## Dependencies

-   `python.exe`: Must be installed on the system and accessible via the `PATH` environment variable (for PowerShell).
-   `fastapi`: Web framework for creating APIs (in Python).
-   `typer`: Library for creating command-line interfaces (in Python).
-   `uvicorn`: ASGI web server (in Python).
-   `pydantic`: Library for data validation (in Python).
-   `loguru`: Library for logging (in Python).

## License

[LICENCE]
