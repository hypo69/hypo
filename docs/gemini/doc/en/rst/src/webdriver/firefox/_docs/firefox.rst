Firefox WebDriver
=================

.. automodule:: hypotez.src.webdriver.firefox.firefox
    :members:
    :undoc-members:
    :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.webdriver.firefox.firefox.Firefox.__init__
.. autofunction:: hypotez.src.webdriver.firefox.firefox.Firefox._set_options
.. autofunction:: hypotez.src.webdriver.firefox.firefox.Firefox._set_profile


Usage
-----

Creating a Profile with User Agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    profile = FirefoxProfile()
    profile.set_preference("general.useragent.override", "user-agent-string")


Disabling Images
~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    profile = FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)


Blocking Pop-up Windows
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    profile = FirefoxProfile()
    profile.set_preference("dom.disable_open_during_load", False)


Setting File Download Path
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    profile = FirefoxProfile()
    profile.set_preference("browser.download.dir", "/path/to/download/folder")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")


Disabling Browser Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    profile = FirefoxProfile()
    profile.set_preference("dom.webnotifications.enabled", False)


Options Examples
---------------

Launching in Headless Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    options = Options()
    options.headless = True


Setting Browser Language
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    options = Options()
    options.add_argument('-lang=es')


Custom Command Line Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    options = Options()
    options.add_argument('--some-option=value')


Managing Debug Messages
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    options = Options()
    options.add_argument('-vv')


Launching in Fullscreen Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    options = Options()
    options.add_argument('--kiosk')


Links
-----

- `Documentation on Firefox Profile Settings <https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile>`_
- `Documentation on Firefox Options <https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html>`_