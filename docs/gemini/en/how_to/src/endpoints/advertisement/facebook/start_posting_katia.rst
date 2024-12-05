rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a script for posting advertisements to Facebook groups.  It utilizes a Facebook-specific `FacebookPromoter` class to manage the campaign process. The script fetches the necessary data (likely campaign details and group information) from JSON files, then automates the posting process using a WebDriver (likely Chrome). The script includes error handling to gracefully exit on user interruption.

Execution steps
-------------------------
1. **Import necessary libraries:** The script starts by importing required modules: `header`, `Driver`, `Chrome` from the `src.webdriver.driver` module, `FacebookPromoter` from `src.endpoints.advertisement.facebook.promoter`, and `logger` from `src.logger`.

2. **Initialize WebDriver:** It initializes a Chrome WebDriver instance using the `Driver` class.

3. **Navigate to Facebook:**  The WebDriver navigates to the Facebook homepage (`https://facebook.com`).

4. **Define campaign data:** The script defines a list of filenames (`filenames`) and campaign names (`campaigns`) which specify the advertisement details and groups to target.

5. **Create a FacebookPromoter instance:** An instance of `FacebookPromoter` is created, passing the WebDriver (`d`), a list of JSON file paths for group information, and a flag (`no_video`) which controls the inclusion of videos in the ads.

6. **Run campaigns:** The `run_campaigns` method of the `FacebookPromoter` is called to execute the ad posting for the defined campaigns.

7. **Error handling:** A `try...except` block is implemented to catch `KeyboardInterrupt` exceptions. If the user interrupts the script, a log message is printed indicating the campaign promotion was interrupted.


Usage example
-------------------------
.. code-block:: python

    # Assuming the necessary modules are installed and paths are correct
    import header
    from src.webdriver.driver import Driver, Chrome
    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.logger import logger
    
    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")
    
    filenames:list = ['katia_homepage.json']
    campaigns:list = ['sport_and_activity', 'bags_backpacks_suitcases']
    promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)

    try:
        promoter.run_campaigns(campaigns)
    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")