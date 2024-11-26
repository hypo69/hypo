## File: hypotez/src/endpoints/advertisement/facebook/start_event.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.advertisement.facebook 
	:platform: Windows, Unix
	:synopsis: Отправка мероприятий в группы фейсбук

"""
MODE = 'dev'

from math import log
import header
import time
from src.utils.jjson import j_loads
from src.webdriver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list[str] = [ "my_managed_groups.json",
                        "usa.json",
                        "he_il.json",
                        "ru_il.json",
                        "katia_homepage.json",
                        
                        "ru_usd.json",
                        "ger_en_eur.json",            
                        ]
excluded_filenames:list[str] = ["my_managed_groups.json",]

events_names:list = ["choice_day_01_10"]


promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)

try:
    while True:
        logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
        time.sleep(7200)
        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

```
<algorithm>
```
```mermaid
graph TD
    A[Initialize] --> B{Get Driver};
    B -- Driver(Chrome) & URL(Facebook.com) --> C[Create FacebookPromoter];
    C --> D{Loop Forever};
    D -- True --> E[Debug message (wake-up time)];
    E --> F[run_events(events_names, filenames)];
    F --> G[Debug message (sleep time)];
    G --> H[Sleep for 7200 seconds];
    H --> D;
    D -- KeyboardInterrupt --> I[Log Interrupt Message];
```
* **Initialize:** Initializes the necessary modules and variables, including `filenames`, `events_names`, and creates a FacebookPromoter object. 
* **Get Driver:** Uses `Driver(Chrome)` and `get_url()` to establish a connection with the Facebook website.
* **Create FacebookPromoter:** Creates an instance of the `FacebookPromoter` class, providing configuration data.
* **Loop Forever:** Enters an infinite loop for continuous campaign promotion.
* **Debug message (wake-up time):** Logs the current time.
* **run_events:** Calls the `run_events` method of the `FacebookPromoter` object. This method will likely handle tasks such as retrieving group data, preparing event postings, and posting the events to the Facebook groups defined in the files. (Example: `events_names` data for a specific event to be promoted).
* **Debug message (sleep time):** Logs the current time before the sleep period.
* **Sleep for 7200 seconds:** Pauses execution for 2 hours.
* **KeyboardInterrupt:** Exits the loop if a KeyboardInterrupt is caught.
* **Log Interrupt Message:** Logs a message indicating that the promotion campaign was interrupted.


```
<explanation>

**Imports:**

* `math`: Provides mathematical functions, specifically `log` in this case (though it isn't used).
* `header`:  Purpose unknown without further context.  It's likely a custom module included for specific tasks within the Facebook promotion process. This is a potential error as the `header` package is not part of the standard python packages, it must be explicitly defined in the `PYTHONPATH`.
* `time`: Used for time-related operations, like getting the current time and pausing execution (using `time.sleep`).
* `j_loads`: Likely a custom function (or class method) from `src.utils.jjson` for parsing JSON data from files.
* `Driver`, `Chrome`: Classes from `src.webdriver` for controlling a browser (likely ChromeDriver or similar).
* `FacebookPromoter`: A class from `src.endpoints.advertisement.facebook` specifically designed for promoting events on Facebook.
* `logger`: Likely a custom logging module from `src.logger` for managing log messages.

**Classes:**

* **Driver:** Handles interactions with the browser.  `Driver(Chrome)` creates a Chrome driver instance.
    * `get_url()`: Takes an URL as input and navigates the browser to it.

* **FacebookPromoter:** Likely has methods to manage Facebook group interactions. Attributes (not seen in the provided code snippet) likely include the browser driver, a list of group data files, potentially an event data file (data from `events_names`, a boolean for video preference (`no_video`), and a method `run_events`.
  * `run_events`:  This method is critical, but specifics are hidden within the `FacebookPromoter` class and require additional information to understand its logic.


**Functions:**

* `time.sleep()`: Pauses execution for a specified number of seconds. (argument `7200` pauses for 2 hours)

**Variables:**

* `MODE`: A string likely controlling the application's behavior (e.g., 'dev' for development mode or 'prod' for production).
* `filenames`, `excluded_filenames`: Lists of strings representing file paths to JSON configuration files containing Facebook group data. This is crucial data for targeted promotion.
* `events_names`: List of event names to promote.


**Potential Errors/Improvements:**

* **Error Handling:** While a `try...except` block handles `KeyboardInterrupt`, more robust error handling is needed for file I/O issues, Facebook API errors, network problems, or problems within `FacebookPromoter.run_events()`.
* **File Paths:** Hardcoding file paths like `"my_managed_groups.json"` is inflexible. Consider using a configuration file or environment variables for better maintainability and portability.
* **Concurrency:** The current design is potentially inefficient if promoting events takes a significant amount of time.  Consider using threads or asynchronous operations within `FacebookPromoter.run_events()` if many groups or events need to be processed.
* **Facebook API Limits:** The code should have checks for Facebook API limits, preventing exceeding the rate limits imposed by Facebook to prevent being blocked.
* **Data Validation:**  The code should validate the format of the JSON data to prevent unexpected behavior.  `j_loads()` should include error handling to gracefully manage issues if a file is corrupt, empty or improperly formatted.
* **Logging:** The use of `logger.debug` for wake-up/sleep messages might be excessive if not properly configured. Consider adjusting log levels or adding more context to the messages.
* **External Dependencies:** Ensure the dependencies for the `header` module are correctly installed and in the `PYTHONPATH`.


**Relationships with other parts of the project:**

The code relies heavily on other modules in the `src` package, namely `src.utils.jjson`, `src.webdriver`, `src.endpoints.advertisement.facebook` and `src.logger`. This indicates a modular design, where different components handle various aspects of the Facebook promotion task.