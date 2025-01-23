## \file /src/_experiments/test_file_operations.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src._experiments """


import os

def test_file_operations():
    """Test for basic file operations: create, read, write, and delete."""

    # Step 1: Define the file path
    filename = "test_file.txt"

    try:
        # Step 2: Create and write to the file
        with open(filename, "w") as f:
            f.write("Hello, World!")

        # Step 3: Read the content from the file
        with open(filename, "r") as f:
            content = f.read()
            assert content == "Hello, World!", f"Unexpected content: {content}"

        # Step 4: Append new content to the file
        with open(filename, "a") as f:
            f.write("\nAppended Line")

        # Step 5: Verify the appended content
        with open(filename, "r") as f:
            lines = f.readlines()
            assert lines[1].strip() == "Appended Line", f"Unexpected line: {lines[1].strip()}"

        print("All tests passed!")

    except AssertionError as e:
        print(f"Test failed: {e}")

    finally:
        # Step 6: Delete the file
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' not found for deletion.")

# Run the test
test_file_operations()
...
