rst
How to initialize the TinyTroupe application
========================================================================================

Description
-------------------------
This code initializes the TinyTroupe application by setting up necessary modules, handling configuration, and printing disclaimers about the use of AI models. It prepares the environment for running TinyTroupe by importing required libraries, adding the current directory to the system path, loading the configuration, and configuring logging.  Crucially, it addresses a potential display issue within Jupyter notebooks by modifying the `rich` library's HTML formatting.

Execution steps
-------------------------
1. **Import necessary modules:** The script imports `os`, `logging`, `configparser`, `rich`, `rich.jupyter`, and the `utils` module from the `tinytroupe` package. It also imports `sys` for modifying the system path.
2. **Add current directory to system path:** The code adds the current directory to the `sys.path` to enable importing modules from the local `tinytroupe` package.
3. **Display AI disclaimer:** A message providing a disclaimer about the reliance on AI models and the potential for inaccuracies is printed to the console.  This is a critical step to inform users of limitations.
4. **Read configuration file:** The function `utils.read_config_file()` is called to load configuration settings from a specified file.
5. **Print formatted configuration:** The `utils.pretty_print_config(config)` function displays the configuration details in a user-friendly, formatted way.
6. **Configure logging:** The `utils.start_logger(config)` function configures logging based on the loaded configuration, setting up how the application will record events and errors.
7. **Fix rich library issue (Jupyter notebooks):** The code addresses an issue with `rich` library display in Jupyter notebooks by modifying the `JUPYTER_HTML_FORMAT` variable, removing margins to prevent display errors.


Usage example
-------------------------
.. code-block:: python

    import os
    import sys
    # ... (place imports for configparser, logging, rich etc.) ...
    from tinytroupe import utils


    # Create a sample config file (e.g., 'config.ini')
    with open('config.ini', 'w') as configfile:
        configfile.write('[logging]\nlevel=INFO')
    # Ensure that tinytroupe/utils.py exists


    # ... (Place the rest of your code to initialize the TinyTroupe application) ...


    # Initialize the application
    try:
        # Modify this to reflect your actual path to utils.py (if necessary)
        sys.path.append(os.path.abspath(os.path.join('..', 'tinytroupe')))
        from tinytroupe import __init__ as tinytroupe_init
        tinytroupe_init.init()
    except ImportError as e:
        print(f"Error initializing TinyTroupe: {e}")