cdata Login Module
===================

.. module:: hypotez.src.suppliers.cdata.login
    :platform: Windows, Unix
    :synopsis: Login module for c-data web driver.

Module Description
------------------

This module contains the `login` function, which handles the login process for the c-data website using a web driver.  It utilizes locators to interact with the web page elements.  The login process gathers credentials from the `self.locators` object and then submits them to the login form.  Successful login results in a log message and a return value of `True`.


Functions
---------

.. autofunction:: hypotez.src.suppliers.cdata.login.login
    :noindex: