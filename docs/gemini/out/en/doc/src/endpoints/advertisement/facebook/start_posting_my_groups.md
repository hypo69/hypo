# hypotez/src/endpoints/advertisement/facebook/start_posting_my_groups.py

## Overview

This module handles the process of posting advertisements to Facebook groups. It utilizes the `FacebookPromoter` class to manage campaigns and posting within the specified groups.  The script aims to automate the posting process for various predefined campaigns.  It uses a `Chrome` webdriver instance.

## Table of Contents

* [Overview](#overview)
* [Global Variables](#global-variables)
* [Classes](#classes)
* [Functions](#functions)


## Global Variables

### `MODE`

```python
MODE = 'dev'
```

**Description**: A string variable defining the script's execution mode (e.g., 'dev', 'prod'). Defaults to 'dev'.

### `filenames`

```python
filenames: list = ['my_managed_groups.json',]
```

**Description**: A list of file names containing information about the Facebook groups. The script assumes a JSON structure for this data.


### `campaigns`

```python
campaigns: list = ['brands', 'mom_and_baby', 'pain', 'sport_and_activity', 'house', 'bags_backpacks_suitcases', 'man']
```

**Description**: A list of campaign names to be used for advertisement posting.

## Classes

### `FacebookPromoter`

**Description**: (See `src/endpoints/advertisement/facebook/promoter.py` for full implementation)
A class for handling the Facebook advertisement posting process within specified groups.


## Functions

This module does not contain user-defined functions; the script is primarily focused on the setup and automated execution of campaigns within the `FacebookPromoter` class.

## Executable Code


```python
import header
import copy
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['my_managed_groups.json',]

campaigns: list = ['brands', 'mom_and_baby', 'pain', 'sport_and_activity', 'house', 'bags_backpacks_suitcases', 'man']

promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = True)

try:
    while True:

        promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
        # ... (potentially other actions within the loop)

    excep KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")
```

**Description**: This code snippet initializes a `Driver` instance using the `Chrome` webdriver, fetches necessary data from files, creates a `FacebookPromoter` instance, and then runs the advertisement campaigns in a loop, continuously running until manually interrupted. Error handling is provided to manage `KeyboardInterrupt` for graceful termination.

**Note:** This section only documents the actual code execution and its logic.  It doesn't include detailed descriptions of the functions within `FacebookPromoter` and other modules, as those are expected to be documented in their respective files.