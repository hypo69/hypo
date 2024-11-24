hypotez/src/endpoints/hypo69/code_assistant/main.py
====================================================

.. module:: src.endpoints.hypo69.code_assistant
   :platform: Windows, Unix
   :synopsis: Code assistant command-line interface.

This module provides a command-line interface for a code assistant.  It allows users to run the assistant with various configurations, including settings from a JSON file, roles, languages, models, and start directories.


Examples of Usage:
-------------------

1. Running with predefined settings:
   ```bash
   python main.py --settings settings.json
   ```

2. Running with 'doc_writer' role, 'ru' language, 'gemini' and 'openai' models, and specified start directories:
   ```bash
   python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
   ```

3. Running with 'code_checker' role, 'en' language, and only 'gemini' model, along with a start directory:
   ```bash
   python main.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
   ```

4. Running with 'doc_writer' role, 'en' language, and only 'openai' model:
   ```bash
   python main.py --role doc_writer --lang en --models openai
   ```


Functions
---------

.. autofunction:: parse_args
.. autofunction:: main