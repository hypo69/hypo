# src.endpoints.advertisement.facebook.start_posting_katia.py

## Overview

This module contains the logic for posting advertisements to Facebook groups (Katia?). It utilizes the `FacebookPromoter` class to manage the campaign workflow.


## Modules

* `header`
* `src.webdriver.driver`
* `src.endpoints.advertisement.facebook.promoter`
* `src.logger`


## Variables

### `MODE`

**Description:**  A string variable, currently set to 'dev', presumably controlling the execution mode.


### `filenames`

**Description:**  A list of filenames containing data relevant to the Facebook groups.


### `campaigns`

**Description:** A list of strings representing the advertisement campaign names.


## Classes

### `Driver`

**Description**:  This class handles web driver initialization and interaction.

### `Chrome`

**Description**:  This class likely represents a specific webdriver implementation (e.g., Chrome).

### `FacebookPromoter`

**Description**: A class that manages the process of sending advertisements to Facebook groups.


## Functions

### `run_campaigns`

**Description**:  Executes the advertisement campaigns.

**Parameters**:
- `campaigns` (list): A list of strings, each representing a campaign name.

**Returns**:
- `None`: The function is executed to run the campaigns and does not return a value.

**Raises**:
- `KeyboardInterrupt`: If the campaign execution is interrupted by the user.


## Code Example

```python
MODE = 'dev'

import header
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['katia_homepage.json',]
campaigns: list = ['sport_and_activity',
                  'bags_backpacks_suitcases',
                    'pain',
                    'brands',
                    'mom_and_baby',
                    'house',
                ]
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)

try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```


## Notes

- The code initializes a webdriver (`Driver`) and sets the URL to facebook.com.
- It then creates a `FacebookPromoter` instance, passing the webdriver and filenames to define the target groups.
- The `run_campaigns` method is called to run the campaigns.
- The `try...except` block handles `KeyboardInterrupt` to gracefully exit.
- The code is likely part of a larger system for advertisement automation.