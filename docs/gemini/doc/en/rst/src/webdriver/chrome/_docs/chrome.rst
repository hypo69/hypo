Chrome WebDriver
=================

.. automodule:: hypotez.src.webdriver.chrome.chrome
    :members:
    :undoc-members:
    :show-inheritance:

Summary
-------

This module provides a custom `Chrome` class extending `selenium.webdriver.Chrome`.  It facilitates the setup of a Chrome WebDriver instance with configurable options, including user agents,  custom profiles, and the ability to locate free ports.  The configuration is primarily managed by the `chrome.json` file.

Configuration (`chrome.json`)
----------------------------

The `chrome.json` file configures various aspects of the Chrome WebDriver, including paths to ChromeDriver, Chrome binary, and optional configuration headers.

.. code-block:: json
   :linenos:

   {
     "profiles": {
       "one.last.bit": {
         "os": "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default",
         "internal": "webdriver\\chrome\\profiles\\default",
         "testing": "%LOCALAPPDATA%\\Google\\Chrome for Testing\\User Data\\Default"
       },
       "@todo": "Organize management from a shared storage system `Keepass`"
     },
     "locator_description": "You can use profiles from different directories. Multiple profiles can be available on the system.",

     "driver": {
       "chromedriver": [ "webdrivers", "chrome", "125.0.6422.14", "chromedriver.exe" ],
       "chrome_binary": [ "webdrivers", "chrome", "125.0.6422.14", "win64-125.0.6422.14", "chrome-win64", "chrome.exe" ],
       "locator_description": "Different driver versions are in different folders. I work with a tested version of the browser. The system updates to the latest version in the background."
     },

     "headers": {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
       "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
       "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
       "Accept-Encoding": "none",
       "Accept-Language": "en-US,en;q=0.8",
       "Connection": "keep-alive"
     },
     "locator_description headers": "Adjustable for any agent. Details in `fake-useragent`."
   }

Classes
-------

.. autoclass:: hypotez.src.webdriver.chrome.chrome.Chrome
    :members:
    :undoc-members:
    :show-inheritance: