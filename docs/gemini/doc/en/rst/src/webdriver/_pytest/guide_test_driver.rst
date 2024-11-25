Guide for Driver Testing
=========================

.. contents::

.. _guide_test_driver:

Introduction
------------

This document provides a guide for testing the `DriverBase` class using `pytest`. This guide details the steps for setting up the necessary tools, running tests, and interpreting test results.


Prerequisites
-------------

Before beginning the testing process, ensure you have the following components installed:

1. **Python 3.12:**
   Ensure that you have Python 3.12 installed. You can verify the current Python version using the command:
   ```bash
   python --version
   ```

2. **pytest:**
   Install `pytest` if it's not already installed:
   ```bash
   pip install pytest
   ```

3. **unittest.mock:**
   The `unittest.mock` library is part of the standard Python library starting with version 3.3.


Project Structure
----------------

The project has the following structure:

```
src/
|-- webdriver/
|   |-- driver.py
|   |-- javascript/
|   |-- executor/
|-- logger.py
|-- utils/
|   |-- jjson.py
tests/
|-- test_driver.py
```


Environment Setup
----------------

1. **Repository Cloning:**
   Clone the project repository to your local machine:
   ```bash
   git clone <URL_of_your_repository>
   cd <project_name>
   ```

2. **Virtual Environment Creation and Activation:**
   Create a virtual environment for installing dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Dependency Installation:**
   Install the necessary dependencies listed in `requirements.txt` (if available):
   ```bash
   pip install -r requirements.txt
   ```


Writing and Running Tests
-------------------------

1. **Writing Tests:**
   Tests for the `DriverBase` class are located in the `tests/test_driver.py` file. Test examples include testing the `driver_payload`, `scroll`, `locale` methods, and others.

2. **Running Tests:**
   To run the tests, execute the following command in the project root directory:
   ```bash
   pytest tests/test_driver.py
   ```

3. **Interpreting Test Results:**
   After running the tests, `pytest` will provide a report of the results. Example output:
   ```
   ============================== test session starts ===============================\n
   platform linux -- Python 3.12.0, pytest-7.0.0, pluggy-0.13.1\n
   rootdir: /path/to/your/project\n
   collected 9 items\n
\n
   tests/test_driver.py ........                                        [100%]\n
\n
   =============================== 9 passed in 1.23s ================================\n
   ```
   The output indicates the number of passed tests and the total execution time. If any test fails, `pytest` will provide error details.


Useful Commands
---------------

1. **Run all tests:**
   ```bash
   pytest
   ```

2. **Run tests with verbose output:**
   ```bash
   pytest -v
   ```

3. **Run tests with code coverage report:**
   Install `pytest-cov`:
   ```bash
   pip install pytest-cov
   ```
   Then run tests with coverage report:
   ```bash
   pytest --cov=src tests/
   ```

Conclusion
-----------

Testing is a crucial part of software development. Using `pytest` and following this guide, you can effectively test the functionality of the `DriverBase` class, ensuring its correct operation and preventing regressions.

.. automodule:: hypotez.src.webdriver._pytest.test_driver
   :members:
   :undoc-members:
   :show-inheritance: