```rst
hypotez/src/goog/drive/drive.rst
===========================

Minimal library for working with Google Drive.

.. automodule:: hypotez.src.goog.drive.drive
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.goog.drive.drive.GoogleDriveHandler
.. autofunction:: hypotez.src.goog.drive.drive.GoogleDriveHandler.__init__
   :noindex:


.. autofunction:: hypotez.src.goog.drive.drive.GoogleDriveHandler._create_credentials
    :noindex:

.. autofunction:: hypotez.src.goog.drive.drive.GoogleDriveHandler.upload_file
   :noindex:

.. autofunction:: hypotez.src.goog.drive.drive.main
   :noindex:

Example Usage
------------

This example demonstrates how to use the `GoogleDriveHandler` class to upload a file to Google Drive.

.. code-block:: python
    :linenos:
    
    if __name__ == "__main__":
        from pathlib import Path
    
        file_path = Path('/mnt/data/google_extracted/sample_file.txt')  # Replace with your actual file path
        folder_name = 'My Drive Folder'  # Replace with the target folder name in Google Drive
    
        google_drive_handler = GoogleDriveHandler(
            folder_name=folder_name,
        )
        google_drive_handler.upload_file(file_path)

.. note::  Remember to replace `/mnt/data/google_extracted/sample_file.txt` and 'My Drive Folder' with your actual file path and folder name.  Also, ensure the necessary Google API credentials and environment setup are in place.


Class Details
------------

.. autoclass:: hypotez.src.goog.drive.drive.GoogleDriveHandler
    :members:
    :show-inheritance:

.. rubric:: Google Drive Handler Class
   
.. automethod:: hypotez.src.goog.drive.drive.GoogleDriveHandler.__init__
   :noindex:

.. automethod:: hypotez.src.goog.drive.drive.GoogleDriveHandler._create_credentials
    :noindex:
    
.. automethod:: hypotez.src.goog.drive.drive.GoogleDriveHandler.upload_file
    :noindex:


Module Contents
--------------


.. rubric:: Main Function

.. autofunction:: hypotez.src.goog.drive.drive.main
   :noindex:

```
