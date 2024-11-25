How to Install Chrome for Testing
=================================

This document describes the steps to install Chrome for automated testing using the Hypotez webdriver.

.. toctree::
   :maxdepth: 2

   webdriver_installation


Installation Steps
------------------

^ Step 1: Download the ChromeDriver executable.  Go to the ChromeDriver download page and download the appropriate version for your Chrome browser and operating system.

^ Step 2: Set the PATH Environment Variable. This allows your system to find the ChromeDriver executable.  Locate the downloaded ChromeDriver executable.  Add the directory containing this executable to your system's PATH environment variable.


^ Step 3: Verification.  Open a new terminal or command prompt.  Enter the following command:

   ```bash
   chromedriver --version
   ```

   If ChromeDriver is installed correctly, the version number should be displayed.  If not, verify the PATH environment variable has been set correctly.

^ Step 4:  Verify the Setup. Run your test scripts and ensure that they are using the correct ChromeDriver path.  If you encounter errors, check the downloaded ChromeDriver executable for any incompatibility issues.  Adjust file paths if necessary.


.. automodule:: hypotez.src.webdriver._docs.how_to_istall_chrome_for_testing
   :members:
   :undoc-members:
   :show-inheritance: