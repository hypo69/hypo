```rst
visualdg Graber Module
=======================

.. module:: hypotez.src.suppliers.visualdg.graber
    :platform: Windows, Unix
    :synopsis: This module contains the `Graber` class for grabbing product data from VisualDG.


Description
-----------

This module provides a class for grabbing product data from the VisualDG supplier. It utilizes a driver instance for interacting with the website and follows a specific data extraction strategy.  The `Graber` class inherits from `Grbr` (likely a base Graber class) and uses the `ProductFields` data structure for storing the extracted data.


Classes
-------

.. autoclass:: hypotez.src.suppliers.visualdg.graber.Graber
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.suppliers.visualdg.graber.close_popup
    :noindex:


Detailed Descriptions
---------------------


.. autofunction:: hypotez.src.suppliers.visualdg.graber.Graber.__init__
   :noindex:

.. autofunction:: hypotez.src.suppliers.visualdg.graber.Graber.grab_page
    :noindex:
    
```