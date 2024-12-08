# hypotez/src/endpoints/advertisement/facebook/start_event.py

## Overview

This module contains the logic for scheduling and running Facebook advertisement events for various groups.  It utilizes the `FacebookPromoter` class to automate the posting of events to specified Facebook groups. The script manages a list of group data files and event names to control the advertisement campaigns. It utilizes `webdriver` for Facebook interaction and includes error handling and logging.

## Table of Contents

* [Overview](#overview)
* [Variables](#variables)
* [Classes](#classes)
* [Functions](#functions)


## Variables

### `MODE`

**Description**: A string variable holding the current mode of operation (e.g., 'dev', 'prod').

### `filenames`

**Description**: A list of strings representing JSON file paths containing data for Facebook groups.

### `excluded_filenames`

**Description**: A list of strings representing JSON file paths that should be excluded from the process.

### `events_names`

**Description**: A list of strings representing the names of the events to be advertised.

### `promoter`

**Description**: An instance of the `FacebookPromoter` class, responsible for interacting with Facebook and scheduling events.


## Classes

### `FacebookPromoter`

**Description**:  Not included in this file; presumably defined in a separate module.  This class handles the actual Facebook interaction.

**Methods (assumed):**

- `run_events`: Executes the scheduled advertisement events.


## Functions

### `(No functions directly defined in this script.)`



## Modules

### `header`

**Description**:  Not defined within this module, but it is imported. This module is assumed to contain helper functions or configurations.

### `time`

**Description**:  Python's built-in module for time-related functions.

### `math`

**Description**: Python's built-in module for mathematical functions, specifically using `log`.


## Script Execution

The script instantiates a `Driver` object with a `Chrome` web driver, navigates to Facebook.com. It then creates a `FacebookPromoter` object, using a list of JSON files (`filenames`) and flags, likely for configuration and target groups. In a `while True` loop, the script calls the `run_events` method of the promoter object to trigger the advertisement process for a set of events. It introduces delays of 7200 seconds (two hours) between runs, indicated by `time.sleep(7200)`. The `try...except` block handles `KeyboardInterrupt` signals to gracefully terminate the process and log a message. This provides a continuous cycle of event promotion, pausing for 2 hours between cycles.


## Exceptions

### `KeyboardInterrupt`

**Description**: The script catches a `KeyboardInterrupt` exception to terminate the program when the user presses Ctrl+C.
```