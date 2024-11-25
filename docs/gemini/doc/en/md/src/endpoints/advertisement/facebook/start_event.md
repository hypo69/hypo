# hypotez/src/endpoints/advertisement/facebook/start_event.py

## Overview

This module defines the logic for sending events to Facebook groups. It utilizes the `FacebookPromoter` class to automate the process, fetching event data from JSON files, and posting to designated Facebook groups.  The script runs indefinitely, checking for new events at intervals of 2 hours.

## Modules

- `math`: Used for mathematical operations (likely logarithm).
- `header`:  Potentially for custom header functions (missing definition).
- `time`: For time-related functions.
- `src.utils.jjson`: For JSON handling (loading JSON data).
- `src.webdriver`: For web driver interaction (likely using Selenium).
- `src.endpoints.advertisement.facebook`: Contains the `FacebookPromoter` class.
- `src.logger`: For logging operations.


## Global Variables

- `MODE`:  String indicating the execution mode ('dev').
- `filenames`: List of JSON file paths containing group data.
- `excluded_filenames`: List of JSON file paths to exclude.
- `events_names`: List of event names to run.

## Classes

### `FacebookPromoter`

**Description**: A class for managing the advertisement and posting of events to Facebook groups.


**Methods (assumed, based on the usage):**

- `__init__`: Initializes the FacebookPromoter with a driver, a list of JSON files containing group data.
- `run_events`:  Executes events for the specified list of groups.


## Functions

(None explicitly defined)

## Code Structure and Execution Flow

The script initializes a web driver (`Driver`), retrieves group data from JSON files, and creates a `FacebookPromoter` object.  It then enters a loop, executing events using `promoter.run_events` and sleeps for 2 hours before repeating the process. The `try...except` block handles `KeyboardInterrupt`, gracefully stopping the campaign when the user interrupts the script.


## Error Handling

- `KeyboardInterrupt`: The script logs a message and exits gracefully when the user interrupts the program execution.


## Example Usage

```python
promoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
try:
    while True:
        logger.debug(f"waikig up {time.strftime(\'%H:%M:%S\')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"going to sleep at {time.strftime(\'%H:%M:%S\')}",None,False)
        time.sleep(7200)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```


## Further Considerations

- The code assumes the existence of `FacebookPromoter` and other classes/functions from the `src` package.
- The use of `logger` and `debug` messages suggests a logging framework is in place.
- The functionality and implementation details of `FacebookPromoter.run_events` are not shown, but implied.
- Understanding the structure of the JSON files (`filenames`) used for group data is crucial to fully comprehend the application logic.
- The file paths (`filenames`) are hardcoded.  Consider a more flexible configuration for these.
- More information about the `header` module and its purpose would be helpful.
- Adding type hints to functions in the `src` package would significantly improve readability and maintainability.