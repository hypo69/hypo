Facebook Groups Widget
=======================

.. module:: hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets
    :platform: Windows, Unix
    :synopsis: Expanding menu for selecting groups for ad placement

.. automodule:: hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets
    :members:
    :undoc-members:
    :show-inheritance:

Classes
-------

.. autoclass:: FacebookGroupsWidget
    :members:
    :undoc-members:
    :show-inheritance:

    .. automethod:: __init__
        :noindex:
        :show-inheritance:

        Args:
            json_file_path (Path): Path to the JSON file containing information about Facebook groups.

    .. automethod:: create_dropdown
        :noindex:
        :show-inheritance:

        Returns:
            Dropdown: A dropdown widget with Facebook group URLs.

    .. automethod:: display_widget
        :noindex:
        :show-inheritance: