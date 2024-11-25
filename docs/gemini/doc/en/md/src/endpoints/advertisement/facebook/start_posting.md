# hypotez/src/endpoints/advertisement/facebook/start_posting.py

## Overview

This module defines the logic for starting and running advertisement campaigns on Facebook. It utilizes the `FacebookPromoter` class to interact with the Facebook platform and manage the posting process.  The script handles loading advertisement data from JSON files, specifying campaigns, and incorporates error handling for graceful interruption.


## Modules

- `math`
- `header`
- `time`
- `copy`
- `src.webdriver`
- `src.endpoints.advertisement.facebook`
- `src.logger`


## Variables

### `MODE`

**Description**:  A string variable likely defining the execution mode (e.g., 'dev', 'prod').


### `filenames`

**Description**: A list of strings representing the paths to JSON files containing advertisement data for different target groups.


### `excluded_filenames`

**Description**: A list of filenames to exclude from the advertisement campaign process.


### `campaigns`

**Description**: A list of strings representing the different advertising campaigns to run.


### `promoter`

**Description**: An instance of the `FacebookPromoter` class, responsible for interacting with the Facebook API to run the advertisement campaigns.



## Classes

### `FacebookPromoter`

**Description**: (Placeholder, needs the actual class definition) A class handling the interaction with Facebook for advertisement campaigns.


## Functions

(No functions directly defined in this script.  The `run_campaigns` method of `FacebookPromoter` would be documented separately.)


## Usage Example

```python
filenames:list[str] = [...]
campaigns:list = [...]
# ... (other initialization)
try:
  while True:
    promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
    print(f"Going sleep {time.localtime}")
    time.sleep(180)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

## Error Handling

### `KeyboardInterrupt`

**Description**: The script includes a `try...except` block to handle `KeyboardInterrupt` exceptions, logging a message and exiting gracefully when the user interrupts the program.


## Notes

- This script requires initialization of the `FacebookPromoter` object and loading data from JSON files.


-  The `run_campaigns` function likely exists within the `FacebookPromoter` class and its documentation should detail the arguments and return values.

- The `time.sleep(180)` is a crucial component for preventing excessive requests to Facebook, respecting API limits and staying within acceptable usage practices.


- The script's logic relies on the `FacebookPromoter` object and associated methods. This example shows the general usage pattern. Complete documentation will require documentation of the `FacebookPromoter` class.