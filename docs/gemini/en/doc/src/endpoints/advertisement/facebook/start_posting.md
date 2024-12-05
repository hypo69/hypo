# hypotez/src/endpoints/advertisement/facebook/start_posting.py

## Overview

This module contains the logic for starting and running advertisement posting campaigns on Facebook groups. It uses the FacebookPromoter class to handle the actual posting process and manages campaign execution, including scheduled pauses.

## Table of Contents

* [Overview](#overview)
* [Variables](#variables)
* [Classes](#classes)
* [Functions](#functions)


## Variables

### `MODE`

**Description**:  A string variable, currently set to 'dev'.  This likely controls different execution modes (e.g., development vs. production).

### `filenames`

**Description**: A list of JSON file paths used to fetch groups for advertisement targeting.

### `excluded_filenames`

**Description**: A list of JSON file paths to exclude from advertisement targeting.

### `campaigns`

**Description**: A list of campaign names for advertisement posting.

### `promoter`

**Description**: An instance of the `FacebookPromoter` class initialized with webdriver instance `d` and JSON file paths for targeting.


## Classes

### `FacebookPromoter`

**Description**:  (Assumed class definition from `src.endpoints.advertisement.facebook`)  Responsible for handling the advertisement posting process on Facebook.


## Functions

(This section is likely incomplete without the actual `FacebookPromoter` class definition.  The following is a placeholder)


### `run_campaigns` (Within `FacebookPromoter`)

**Description**:  Performs the advertisement posting on Facebook groups.


**Parameters**:
- `campaigns` (list):  A list of campaign names for advertisements.
- `group_file_paths` (list):  A list of paths to JSON files containing group data.

**Returns**:
- `None`: The function likely does not explicitly return a value.

**Raises**:
- `Exception`:  Any exception that occurs during the campaign running.


## Main Execution Block

**Description**:
The provided code sets up a `Driver` object with a Chrome browser.  It initializes a `FacebookPromoter` instance with various inputs. Then, it enters a loop, running the campaigns within the `run_campaigns` method and pausing for 180 seconds.

**Code Explanation**:

The `while True` loop continuously runs `promoter.run_campaigns()` with a copy of the campaigns list. This ensures the campaigns run independently. The `time.sleep(180)` part introduces a delay for the specified duration (180 seconds). The `try...except` block handles `KeyboardInterrupt` to gracefully terminate the campaign promotion.