# hypotez/src/endpoints/advertisement/facebook/scenarios/post_event.py

## Overview

This module provides functions for posting event details on Facebook groups. It utilizes Selenium WebDriver (`Driver`) for interaction with the webpage and handles various aspects of the event posting process, such as inputting the title, date, time, description, and triggering the posting action.  The module leverages a JSON file (`post_event.json`) containing locators for interacting with the Facebook page elements.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`post_title`](#post_title)
    * [`post_date`](#post_date)
    * [`post_time`](#post_time)
    * [`post_description`](#post_description)
    * [`post_event`](#post_event)


## Functions

### `post_title`

**Description**: This function handles the input of the event title on the Facebook page.

**Parameters**:

* `d` (Driver): The driver instance used for interacting with the webpage.
* `title` (str): The title of the event to be posted.

**Returns**:

* `bool`: `True` if the title was sent successfully, `None` otherwise.  The function uses the error logger if it fails to send the title.

**Raises**:
* `Exception`:  (Caught by the logger)  Any exception during the WebDriver interaction.


### `post_date`

**Description**: This function handles the input of the event date on the Facebook page.

**Parameters**:

* `d` (Driver): The driver instance used for interacting with the webpage.
* `date` (str): The date of the event to be posted.

**Returns**:

* `bool`: `True` if the date was sent successfully, `None` otherwise. The function uses the error logger if it fails to send the date.

**Raises**:
* `Exception`: (Caught by the logger) Any exception during the WebDriver interaction.

### `post_time`

**Description**: This function handles the input of the event time on the Facebook page.

**Parameters**:

* `d` (Driver): The driver instance used for interacting with the webpage.
* `time` (str): The time of the event to be posted.

**Returns**:

* `bool`: `True` if the time was sent successfully, `None` otherwise. The function uses the error logger if it fails to send the time.

**Raises**:
* `Exception`: (Caught by the logger) Any exception during the WebDriver interaction.

### `post_description`

**Description**: This function handles the input of the event description on the Facebook page.

**Parameters**:

* `d` (Driver): The driver instance used for interacting with the webpage.
* `description` (str): The description of the event to be posted.

**Returns**:

* `bool`: `True` if the description was sent successfully, `None` otherwise. The function uses the error logger if it fails to send the description.


**Raises**:
* `Exception`: (Caught by the logger) Any exception during the WebDriver interaction.

### `post_event`

**Description**: This function orchestrates the entire event posting process.

**Parameters**:

* `d` (Driver): The driver instance used for interacting with the webpage.
* `event` (SimpleNamespace): An object containing the event details (title, date, time, description, and potential promotional link).

**Returns**:

* `bool`: `True` if the event was posted successfully, `None` otherwise.  The function attempts each step of the posting process and returns early if any step fails.


**Raises**:
* `Exception`: (Caught by the logger) Any exception during the WebDriver interaction.