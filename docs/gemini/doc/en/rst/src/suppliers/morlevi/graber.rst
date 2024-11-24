Module morlevi.graber
======================

.. module:: hypotez.src.suppliers.morlevi.graber
    :platform: Windows, Unix
    :synopsis: Graber for Morlevi supplier webpage


Module Description
------------------

This module provides functionality for grabbing product data from the Morlevi supplier's webpage. It utilizes web-driving capabilities and data extraction techniques to populate product fields.


Classes
-------

.. autoclass:: Graber
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: Graber.grab_page
.. autofunction:: Graber.local_saved_image


Attributes
----------

.. autoattribute:: Graber.supplier_prefix


Detailed Descriptions
--------------------


.. autoclass:: Graber
    :show-inheritance:

    .. automethod:: __init__
        :noindex:
    .. automethod:: grab_page
        :noindex:

        .. rubric:: Args
           :class: sphinx-arg

           driver (Driver): The driver instance to use for grabbing.

        .. rubric:: Returns
           :class: sphinx-arg

           ProductFields: The grabbed product fields.


.. autofunction:: Graber.local_saved_image
    :noindex:

    .. rubric:: Args
       :class: sphinx-arg

       value (Any):  This value can be passed in the kwargs dictionary via the key {local_saved_image = `value`}. If `value` was passed, its value will be used for ProductFields.local_saved_image.

    .. rubric:: Raises
       :class: sphinx-arg
       Exception: various exceptions during image fetching and saving.