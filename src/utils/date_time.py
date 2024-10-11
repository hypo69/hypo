## \file ../src/utils/date_time.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! This module contains a function to check if the current time is within a specified interval.

The `interval` function allows for determining whether the current time falls within the 
given time frame, which is useful for running operations that should only occur during 
specific periods (e.g., late-night maintenance). The default time interval is from 23:00 
to 06:00, and the function can handle intervals that span midnight.
"""

from datetime import datetime, time

def interval(start: time = time(23, 0), end: time = time(6, 0)) -> bool:
    """! Check if the current time is within the specified interval.
    
    Args:
        start (time): Start of the interval (default is 23:00).
        end (time): End of the interval (default is 06:00).

    Returns:
        bool: True if the current time is within the interval, False otherwise.
    """
    current_time = datetime.now().time()

    if start < end:
        # Interval within the same day (e.g., 08:00 to 17:00)
        return start <= current_time <= end
    else:
        # Interval spanning midnight (e.g., 23:00 to 06:00)
        return current_time >= start or current_time <= end

if __name__ == 'main':
    # Example usage
    if interval():
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval.")
