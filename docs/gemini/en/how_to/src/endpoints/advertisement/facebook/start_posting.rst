rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a script for posting advertisements to Facebook groups. It initializes a web driver (using Chrome), loads advertisement data from JSON files, and runs campaigns to post advertisements to specified Facebook groups. The script employs a loop to repeatedly execute campaign posting, pausing for 180 seconds between iterations.

Execution steps
-------------------------
1. **Initialization:** The code initializes a web driver (`Driver` object with Chrome) and navigates to the Facebook website.

2. **Data Loading:** A list of JSON file names (`filenames`) for advertisement data and a list of JSON file names to exclude (`excluded_filenames`) are defined. Campaign types (`campaigns`) are also defined.

3. **Object Creation:** An instance of `FacebookPromoter` class is created, providing the initialized driver and the list of relevant JSON file paths. Optionally, specifies if video posting should be skipped (`no_video = True`).

4. **Campaign Execution Loop:** Enters a `while True` loop, which continuously executes the `run_campaigns` method of the `FacebookPromoter` object. The `run_campaigns` method uses a copy of the defined `campaigns` list for each iteration to prevent modification of the original list. It also passes in the `filenames` list to the `FacebookPromoter`.

5. **Pause and Logging:** After each campaign execution, the code prints a message indicating the current time, and then uses `time.sleep(180)` to pause the execution for 180 seconds.

6. **Error Handling:** A `try...except KeyboardInterrupt` block handles potential interruptions (e.g., Ctrl+C). If an interruption occurs, a logging message is printed to indicate the interruption.

7. **Continuous Running:** The `while True` loop ensures that the advertisement posting continues indefinitely, or until interrupted.


Usage example
-------------------------
.. code-block:: python

    # Assuming the necessary libraries (header, etc.) are installed.
    # And the `src` directory is structured correctly to import the modules.

    import time
    import copy
    from src.webdriver.driver import Driver, Chrome
    from src.endpoints.advertisement.facebook import FacebookPromoter
    from src.logger import logger #Import logger

    # ... (other necessary imports and definitions)

    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")


    # ... (Define your filenames, excluded_filenames, and campaigns as needed)


    promoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)


    try:
        while True:

            promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
            print(f"Going sleep {time.localtime()}")
            time.sleep(180)


    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")