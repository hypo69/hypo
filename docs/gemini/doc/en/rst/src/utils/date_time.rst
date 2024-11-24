hypotez/src/utils/date_time.py
==========================

.. module:: hypotez.src.utils.date_time
    :platform: Windows, Unix
    :synopsis: Function to check if the current time is within a specified interval with an optional timeout.

This module contains a function to check if the current time is within a specified interval with an optional timeout.

The `interval` function allows for determining whether the current time falls within the
given time frame, which is useful for running operations that should only occur during
specific periods (e.g., late-night maintenance). The default time interval is from 23:00
to 06:00, and the function can handle intervals that span midnight.

Additionally, it provides functionality to wait for a response with a timeout.


Classes
-------

.. autoclass:: TimeoutCheck
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: TimeoutCheck.interval
.. autofunction:: TimeoutCheck.interval_with_timeout
.. autofunction:: TimeoutCheck.get_input
.. autofunction:: TimeoutCheck.input_with_timeout


Example Usage (in ``__main__`` block)
-------------------------------------

The example demonstrates how to use the functions within the module.  It creates a `TimeoutCheck` object and calls `interval_with_timeout` with a 5-second timeout.  The output indicates whether the current time falls within the specified interval or if the timeout was reached.

```
```
```python
if __name__ == '__main__':
    # Example usage
    timeout_check = TimeoutCheck()

    # Check interval with a timeout of 5 seconds
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")
```