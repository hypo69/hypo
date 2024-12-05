rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines an interactive menu for running predefined scripts (script1 and script2).  The user can select which script to execute through the menu.  It includes handling for the `--help` argument, which displays the available commands.  The code uses the `argparse` module for command-line argument parsing. It also imports a `logger` for error handling (though the `logger` object isn't used in the provided example).

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `argparse` module for command-line argument handling, `jjson` functions for potential JSON handling (though not used in the present example) and the `logger` for error handling.

2. **Define script functions:** Functions `script1()` and `script2()` are defined to execute the respective scripts.  Currently, they only print messages indicating script start.  Actual script logic should be added within these functions.

3. **Define help function:** The `show_help()` function displays a list of available commands, aiding users in navigating the menu.

4. **Define interactive menu function:** The `interactive_menu()` function presents a command prompt.  It prompts the user to enter a command number (1, 2, or 3 for help or 4 to exit), and executes the corresponding script or function based on the choice. Error handling is included for invalid inputs.

5. **Define main function:** The `main()` function is the entry point. It initializes an `argparse` parser and handles the `--help` argument.  If `--help` is provided, it displays the help message; otherwise, it starts the interactive menu.


6. **Run the script:** When executed, the code proceeds to handle the provided command-line arguments. If `--help` is used, the help is displayed. Otherwise, the interactive menu is initiated, allowing user interaction with the program.


Usage example
-------------------------
.. code-block:: bash

    python main.py  # Starts the interactive menu

.. code-block:: python

    python main.py --help  # Displays the help menu

.. code-block::
    
    Welcome! Choose one of the commands:

    1. Run script 1
    2. Run script 2
    3. --help - Show command list.
    4. exit - Exit the program.

    Enter command number: 1
    Script 1 started

    Enter command number: 3
    
    Available commands:
    1. Run script 1 - Executes script 1.
    2. Run script 2 - Executes script 2.
    3. --help - Displays this help menu.
    4. exit - Exits the program.