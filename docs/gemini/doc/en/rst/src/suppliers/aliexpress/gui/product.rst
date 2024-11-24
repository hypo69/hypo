Product Editor
=============

.. module:: hypotez.src.suppliers.aliexpress.gui.product
    :platform: Windows, Unix
    :synopsis: This module provides a graphical user interface (GUI) for editing product data.


ProductEditor Class
-------------------

.. autoclass:: hypotez.src.suppliers.aliexpress.gui.product.ProductEditor
    :members:
    :undoc-members:
    :show-inheritance:

    
    .. automethod:: __init__
        :noindex:
        :show-inheritance:

        :param parent: Parent widget.
        :type parent: Optional[QtWidgets.QWidget]
        :param main_app: Main application instance.
        :type main_app: Optional[QtWidgets.QApplication]

    .. automethod:: setup_ui
        :noindex:
        :show-inheritance:
        
        :Description: Sets up the user interface, adding buttons and labels.
        

    .. automethod:: setup_connections
        :noindex:
        :show-inheritance:

        :Description: Sets up signal-slot connections (currently empty).

    .. automethod:: open_file
        :noindex:
        :show-inheritance:
        
        :Description: Opens a file dialog to select a JSON file.
        
    .. automethod:: load_file
        :noindex:
        :show-inheritance:
        :param file_path: Path to the JSON file.
        :type file_path: str
        :raises Exception: If there's an error loading the JSON file.
        :returns: Loads the JSON file and displays its content.

    .. automethod:: create_widgets
        :noindex:
        :show-inheritance:
        :param data: Data loaded from the JSON file.
        :type data: SimpleNamespace

        :Description: Creates UI widgets based on the data from the JSON file. Removes previous widgets.


    .. automethod:: prepare_product_async
        :noindex:
        :show-inheritance:
        :raises Exception: If there's an error preparing the product.
        
        :Description: Asynchronously prepares the product using the `AliCampaignEditor` object. Displays success or error messages using QMessageBox.