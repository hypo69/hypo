```rst
hypotez.endpoints.hypo69.code_assistant
=====================================

This module provides a code assistant CLI application.  It allows for various tasks such as code checking, analysis, documentation generation, and test creation.  The application supports multiple language models (e.g., gemini, openai) and configuration via a JSON settings file.


.. automodule:: hypotez.src.endpoints.hypo69.code_assistant.main
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.endpoints.hypo69.code_assistant.main.parse_args
   :noindex:

.. autofunction:: hypotez.src.endpoints.hypo69.code_assistant.main.main
   :noindex:

Usage Examples
-------------

1. Running with default settings:
   ```bash
   python main.py --settings settings.json
   ```

2. Running with specific role, language, models, and start directories:
   ```bash
   python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
   ```

3. Running with code checking role, language, and model:
   ```bash
   python main.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
   ```

4. Running with documentation writing role, language, and model:
   ```bash
   python main.py --role doc_writer --lang en --models openai
   ```


.. note::

    Replace `/path/to/dir` and other paths with your actual directories.
    A `settings.json` file must be provided with the correct format for option 1.

```
