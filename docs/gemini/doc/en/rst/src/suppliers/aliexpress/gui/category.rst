Category Editor
==============

.. module:: hypotez.src.suppliers.aliexpress.gui.category
    :platform: Windows, Unix
    :synopsis: This module provides a GUI for editing categories in AliExpress advertising campaigns.


.. automodule:: hypotez.src.suppliers.aliexpress.gui.category
    :members:
    :undoc-members:
    :show-inheritance:


Classes
-------

.. autoclass:: CategoryEditor
    :members:
    :special-members: __init__
    :show-inheritance:
    
    :method:`__init__`
    ^^^^^^^^^^^^^^^^^^

    Initializes the `CategoryEditor` window.

    :param parent: The parent widget (optional).
    :type parent: Optional[QWidget]
    :param main_app: The main application object.
    :type main_app: MainApp
    
    :method:`setup_ui`
    ^^^^^^^^^^^^^^^^^^

    Sets up the user interface elements.

    :returns: None
    :rtype: None
    
    :method:`setup_connections`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Sets up signal-slot connections.

    :returns: None
    :rtype: None

    :method:`open_file`
    ^^^^^^^^^^^^^^^^^^^^

    Opens a file dialog to select a JSON file. Loads the file content into the editor.

    :returns: None
    :rtype: None

    :method:`load_file`
    ^^^^^^^^^^^^^^^^^^^^

    Loads a JSON file.

    :param campaign_file: The path to the JSON file.
    :type campaign_file: str
    :returns: None
    :raises Exception: If the file cannot be loaded or parsed.
    :rtype: None


    :method:`create_widgets`
    ^^^^^^^^^^^^^^^^^^^^^^^^

    Creates widgets based on the data loaded from the JSON file, dynamically updating the UI.


    :param data: Data loaded from the JSON file.
    :type data: SimpleNamespace
    :returns: None
    :rtype: None


    :method:`prepare_all_categories_async`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Asynchronously prepares all categories in the campaign.

    :returns: None
    :rtype: None

    :raises Exception: If any error occurs during the preparation process.

    :method:`prepare_category_async`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Asynchronously prepares a specific category.

    :param campaign_name: The name of the campaign.
    :type campaign_name: str
    :returns: None
    :rtype: None
    :raises Exception: If any error occurs during the preparation process.