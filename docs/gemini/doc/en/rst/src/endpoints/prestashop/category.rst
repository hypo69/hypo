Module hypotez.src.endpoints.prestashop.category
============================================

.. module:: hypotez.src.endpoints.prestashop.category
   :platform: Windows, Unix
   :synopsis: PrestaCategory layer between client categories (PrestaShop) and suppliers.

This module provides a class for interacting with PrestaShop categories, offering methods for adding, deleting, updating categories, and retrieving parent categories.  It handles the communication layer between client-specific category structures and the underlying PrestaShop API.

.. note::
    Client category trees are unique to each client and are not readily shared with suppliers.  Product association with categories is managed separately within supplier contexts.

.. image:: categories_tree.png
   :alt: Category Tree Diagram
   :width: 50%


Classes
-------

.. autoclass:: PrestaCategory
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

Methods
-------

.. automethod:: PrestaCategory.__init__
.. automethod:: PrestaCategory.get_parent_categories_list