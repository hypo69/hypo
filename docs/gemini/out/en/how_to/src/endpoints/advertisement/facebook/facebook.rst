rst
How to use the Facebook class
========================================================================================

Description
-------------------------
This code defines a `Facebook` class for interacting with Facebook using a web driver.  It encapsulates various actions like logging in, posting messages, uploading media, and switching accounts.  It utilizes functions from sub-modules within the `facebook` directory.  The class requires a web driver instance (`driver`) to interact with the Facebook interface.


Execution steps
-------------------------
1. **Initialization:** Instantiate the `Facebook` class, providing the web driver, promoter name, and a list of file paths for media uploads. This sets up the necessary attributes (`d`, `promoter`) for subsequent interactions.

2. **Driver Initialization (if necessary):**  If the web driver isn't already running, this code establishes the connection to the web driver and navigates to the specified start page (`https://www.facebook.com/hypotez.promocodes`).  There is a placeholder for potential account switching logic (`switch_account`) if the login page is displayed.  This step handles setting up the web driver for interacting with Facebook.

3. **Login:** If needed, call the `login()` method to perform the Facebook login process.  This utilizes the `login` function from the `login` module within the `facebook` directory.

4. **Promoting Post or Event:**  Use methods like `promote_post` or `promote_event` to interact with Facebook posts and events.  The `promote_post` method takes a `SimpleNamespace` object (`item`) containing post data. The `promote_event` method is a placeholder and expects a `SimpleNamespace` object named `event` holding relevant event details.  These methods delegate the actual implementation to functions defined in sub-modules.


Usage example
-------------------------
.. code-block:: python

    from selenium import webdriver  # Import necessary library
    from hypotez.src.endpoints.advertisement.facebook.facebook import Facebook
    from types import SimpleNamespace

    # Assuming you have a web driver instance and other relevant data
    driver = webdriver.Chrome()
    promoter_name = "your_promoter"
    media_file_paths = ["path/to/image1.jpg", "path/to/image2.png"]

    # Create a SimpleNamespace object for post data
    post_item = SimpleNamespace(message="This is my post message!", media=media_file_paths)

    facebook_instance = Facebook(driver, promoter_name, media_file_paths)

    if facebook_instance.login():
        success = facebook_instance.promote_post(post_item)
        if success:
            print("Post promoted successfully!")
        else:
            print("Failed to promote post.")
    else:
        print("Login failed.")

    # Close the web driver after use
    driver.quit()