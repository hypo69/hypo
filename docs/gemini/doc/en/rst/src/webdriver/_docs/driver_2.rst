Driver Base Class
=================

.. automodule:: hypotez.src.webdriver.driver
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.webdriver.driver.DriverBase.driver_payload
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.scroll
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.locale
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.get_url
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.extract_domain
.. autofunction:: hypotez.src.webdriver.driver.DriverBase._save_cookies_locally
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.page_refresh
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.window_focus
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.wait
.. autofunction:: hypotez.src.webdriver.driver.DriverBase.delete_driver_logs


Metaclass
---------

.. autoclass:: hypotez.src.webdriver.driver.DriverMeta
    :members:
    :undoc-members:
    :show-inheritance:

Driver Class
------------

.. autoclass:: hypotez.src.webdriver.driver.Driver
    :members:
    :undoc-members:
    :show-inheritance:


Usage
-----

This code allows you to create WebDriver objects for different browsers using the following syntax:

.. code-block:: python

    from hypotez.src.webdriver import Driver, Chrome, Firefox, Edge

    # Create a Chrome driver object
    d = Driver(Chrome)

    # Access DriverBase methods through the 'd' object
    d.get_url("https://example.com")
    d.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)


Example Usage of Methods
------------------------

1. **Opening a Webpage and Checking Navigation Success**:

.. code-block:: python

    d.get_url("https://example.com")


2. **Scrolling the Page**:

.. code-block:: python

    d.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)


3. **Determining the Page Language**:

.. code-block:: python

    language = d.locale()


4. **Saving Cookies Locally**:

.. code-block:: python

    d._save_cookies_locally('cookies.pkl')


5. **Refreshing the Page**:

.. code-block:: python

    d.page_refresh()


Note:  The examples provided are illustrative.  The actual usage will depend on the specific WebDriver implementation (e.g., Chrome, Firefox) and its available methods.  Proper error handling is crucial in real-world applications.