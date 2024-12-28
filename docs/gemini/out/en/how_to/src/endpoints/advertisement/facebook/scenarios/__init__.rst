rst
How to use the hypotez/src/endpoints/advertisement/facebook/scenarios/__init__.py module
=============================================================================================

Description
-------------------------
This Python module provides functions for interacting with Facebook's advertising API within the Hypotez platform. It handles various scenarios such as logging in, posting messages, switching accounts, posting events, and posting ads.  The code imports necessary functions from submodules, organizing them for better management and clarity. It also defines a constant `MODE` set to 'dev'.

Execution steps
-------------------------
1. **Import necessary functions:** The `__init__.py` file imports functions from submodules like `login`, `post_message`, `switch_account`, `post_event`, and `post_ad`. This allows you to call these functions later in your application.

2. **Define a mode:** The `` line sets a mode variable, presumably used for different operational configurations (development, testing, or production).

3. **Organize function access:** This module imports and organizes various functions for Facebook advertisement operations.  This ensures you can call specific posting functions like `post_message_title`, `upload_post_media`, and `message_publish` without having to navigate through multiple files. The same structure is applied for `post_event` scenarios.

4. **Utilize specific functions:** To perform a Facebook action, use functions within the imported sub-modules. For example, use `login()` to log into Facebook. Then, for posting a message use functions like `post_message()`, `post_message_title()`, `upload_post_media()`, and others from the `post_message` submodule. Similarly, functions from `post_event` and `post_ad` are called to create events and ads, respectively.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.advertisement.facebook.scenarios import login, post_message, post_event
    from datetime import datetime


    # Example usage - Login
    login("username", "password")


    # Example usage - Post a message
    post_message(title="Hello Facebook!", body="This is my first post.")


    # Example usage - Post an event
    post_event_title = "My Awesome Event"
    post_event_description = "This is a great event!"
    event_date = datetime(2024, 10, 26)
    event_time = datetime(2024, 10, 26, 14, 00)
    post_event(post_event_title, post_event_description, event_date, event_time)