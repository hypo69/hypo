```rst
Presta Category Endpoint
=========================

.. module:: hypotez.src.endpoints.prestashop.category
    :platform: Windows, Unix
    :synopsis: PrestaCategory layer between client categories (PrestaShop) and suppliers.  Provides methods for adding, deleting, updating categories, and retrieving parent categories.  Clients can have unique category trees.

locator_description
-------------------
Clients can each have their own unique category tree, which is only understandable to them. Product binding to category is described in supplier scenarios


.. image:: categories_tree.png
   :alt: Category Tree Diagram


.. automodule:: hypotez.src.endpoints.prestashop.category
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.endpoints.prestashop.category.PrestaCategory.__init__
.. autofunction:: hypotez.src.endpoints.prestashop.category.PrestaCategory.get_parent_categories_list

Class Documentation
-------------------

.. autoclass:: hypotez.src.endpoints.prestashop.category.PrestaCategory
    :members:
    :undoc-members:
    :show-inheritance:


Example Usage (PrestaCategory)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
    prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
    prestacategory.delete_category_PrestaShop(3)
    prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
    print(prestacategory.get_parent_categories_list_PrestaShop(5))

```
