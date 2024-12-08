rst
How to use the file utility functions
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/utils/file.py`) provides functions for various file operations, including saving data to text files, reading file content (including directory contents), getting filenames, recursively yielding/getting file paths, reading files recursively, removing BOM characters from files, and traversing directories to clean Python files.  It includes error handling and logging using a custom logger.  Crucially, it handles different data types (strings, lists, dictionaries) when saving to files and provides options for reading files as lines or whole content.  It also allows filtering files by extensions within directories.


Execution steps
-------------------------
1. **Import the module:**  Import the `file` module into your script.
   ```python
   from hypotez.src.utils.file import save_text_file, read_text_file, get_filenames, recursively_read_text_files, remove_bom, traverse_and_clean
   ```

2. **Choose the operation:** Select the desired file operation function (e.g., `save_text_file`, `read_text_file`).

3. **Define Input Parameters:**  Provide the necessary arguments to the function, such as the file path, data to save, and options like `as_list` for reading files. For example:
   ```python
   data_to_save = {"key": "value"}
   file_path = "my_file.txt"
   ```

4. **Call the function:** Execute the chosen function with the input parameters:
   ```python
   save_result = save_text_file(data_to_save, file_path)
   ```

5. **Handle return value (if any):** Check the return value of the function.  Some functions return `True` for success and `False` for failure. `read_text_file`, if reading from a directory, returns a list of file content or `None` if an error occurs. 

   ```python
   if save_result:
       print("File saved successfully.")
   else:
       print("Error saving file.")
   ```


Usage example
-------------------------
.. code-block:: python

   from hypotez.src.utils.file import save_text_file, read_text_file, recursively_read_text_files
   import os

   def example_usage():
       # Example 1: Saving data to a file
       data = ["This is line 1.", "This is line 2."]
       file_path = "my_file.txt"
       success = save_text_file(data, file_path)
       if success:
           print(f"File '{file_path}' created successfully.")

       # Example 2: Reading file content as a string
       file_path = "my_file.txt"
       content = read_text_file(file_path)
       if content:
           print(f"Content of '{file_path}':\n{content}")

       # Example 3: Reading multiple files in a directory
       root_dir = os.path.join(os.getcwd(), "my_directory")  # Replace with your directory
       files_content = recursively_read_text_files(root_dir, ["*.txt"])
       if files_content:
           for line in files_content:
               print(line, end="")


   if __name__ == "__main__":
       example_usage()