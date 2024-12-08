rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python script `start_sergey.py` manages the launch of Facebook advertisement campaigns. It defines functions for running campaigns, handling different languages and currencies, and orchestrates the process through a loop.  The script interacts with a Facebook driver, fetches advertisement data from JSON files, and automatically sends ads to specified Facebook groups.

Execution steps
-------------------------
1. **Initialization:** The script imports necessary libraries like `header`, `random`, `time`, `copy`, `pathlib`, and classes for webdriver interaction, file handling, and logging.  It sets up variables for campaign modes, paths to JSON files containing ad and group information, and categories for targeting.


2. **`run_campaign` function:** This function takes a Facebook driver, advertiser name, campaign names, group file paths, language, and currency as input.  It initializes a `FacebookPromoter` object using the provided driver and advertiser name. It then uses this object to execute the specified campaigns using the provided data.


3. **`campaign_cycle` function:** This function orchestrates the campaign launch process. It copies and extends lists of file paths based on the language (Russian or Hebrew) for groups and advertisements. It defines language-currency pairs to be used in the campaign.  Iterates through each language-currency pair.  For each language, it chooses appropriate group file paths. It chooses campaigns based on the selected language. It calls the `run_campaign` function for each campaign with the corresponding data.


4. **`main` function:** The `main` function is the entry point of the script. It initializes a Facebook driver, sets a flag for an AliExpress advertising campaign, and enters an infinite loop.  Inside the loop, it checks if a certain interval has passed, calls the `campaign_cycle` function to manage advertisement campaigns, logs the activity using logger, and introduces random delays to avoid overloading the Facebook system. The script continuously runs until interrupted by a keyboard interrupt.


5. **Error Handling:** The `try...except KeyboardInterrupt` block ensures the script can gracefully exit if interrupted, logging a message to indicate the termination.

Usage example
-------------------------
.. code-block:: python

    # Assuming you have the necessary imports and driver initialization
    from hypotez.src.endpoints.advertisement.facebook import start_sergey
    from hypotez.src.webdriver.driver import Chrome


    driver = Chrome()  # Initialize a Chrome driver

    #Example run of the campaign cycle
    try:
        success = start_sergey.campaign_cycle(driver)
        if success:
           print("Advertisement campaign successfully initiated.")

    except Exception as e:
       print(f"An error occurred: {e}")


    driver.quit()  # Crucial: close the driver