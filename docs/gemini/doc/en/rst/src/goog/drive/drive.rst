Module src.goog.drive
=====================

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

Class Documentation
-------------------

.. autoclass:: hypotez.src.goog.drive.drive.GoogleDriveHandler
    :members:
    :show-inheritance:
    :undoc-members:

    
    .. automethod:: hypotez.src.goog.drive.drive.GoogleDriveHandler.__init__
        :noindex:

    .. automethod:: hypotez.src.goog.drive.drive.GoogleDriveHandler._create_credentials
        :noindex:

    .. automethod:: hypotez.src.goog.drive.drive.GoogleDriveHandler.upload_file
        :noindex:


Example Usage
------------

The following example demonstrates how to use the `GoogleDriveHandler` class to upload a file:

.. code-block:: python
    
    from pathlib import Path

    file_path = Path('/mnt/data/google_extracted/sample_file.txt')  # Replace with your actual file path
    folder_name = 'My Drive Folder'  # Replace with the target folder name in Google Drive

    google_drive_handler = GoogleDriveHandler(
        folder_name=folder_name,
    )
    google_drive_handler.upload_file(file_path)