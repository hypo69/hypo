Facebook Advertisement Posting
=============================

.. module:: hypotez.src.endpoints.advertisement.facebook.start_posting
    :platform: Windows, Unix
    :synopsis: Sending advertisement posts to Facebook groups.


Module Description
------------------

This module handles the process of posting advertisements to Facebook groups. It utilizes the FacebookPromoter class to manage the campaign execution, providing functionality for sending posts to various target groups.


Functions
---------

.. autofunction:: hypotez.src.endpoints.advertisement.facebook.start_posting.MODE
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.start_posting.filenames
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.start_posting.excluded_filenames
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.start_posting.campaigns
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.start_posting.promoter


Classes
-------

.. autoclass:: hypotez.src.webdriver.Driver
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: hypotez.src.webdriver.Chrome
    :members:
    :undoc-members:
    :show-inheritance:


.. autoclass:: hypotez.src.endpoints.advertisement.facebook.FacebookPromoter
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: hypotez.src.logger
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: math
    :members:
    :undoc-members:
    :show-inheritance:


.. automodule:: time
    :members:
    :undoc-members:
    :show-inheritance:
.. automodule:: copy
    :members:
    :undoc-members:
    :show-inheritance:

Module Contents
---------------

.. literalinclude:: hypotez/src/endpoints/advertisement/facebook/start_posting.py
    :language: python
    :linenos:
    :lines: 12-

Example Usage
-------------

.. code-block:: python

    # ... (Import necessary modules)
    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")
    # ... (Define filenames, excluded_filenames, campaigns)

    promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)

    try:
        while True:
            promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
            print(f"Going sleep {time.localtime()}")
            time.sleep(180)
            # ... (Additional logic as needed)
    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")