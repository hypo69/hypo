rst
How to use the AliRequests class
========================================================================================

Description
-------------------------
This code defines a class `AliRequests` for handling HTTP requests to AliExpress.  It's designed to manage cookies, specifically loading them from a pickle file, refreshing session cookies, and handling the JSESSIONID.  It provides a method (`make_get_request`) to perform GET requests with the loaded cookies and headers. Additionally, it offers a method (`short_affiliate_link`) to generate a short affiliate link.

Execution steps
-------------------------
1. **Initialization:** The `__init__` method initializes the `AliRequests` object, creating a `RequestsCookieJar` to store cookies, a default header with a random user agent, and a session object for managing requests.  Crucially, it loads cookies from a specified webdriver's cookie file using `_load_webdriver_cookies_file`.


2. **Cookie Loading (`_load_webdriver_cookies_file`):** This method attempts to load cookies from a pickle file (located in a specific directory structure) based on the provided `webdriver_for_cookies` parameter. The cookies are added to the `cookie_jar`. It logs success or failure accordingly.


3. **Session Cookie Refresh (`_refresh_session_cookies`):** This method makes a GET request to a specific AliExpress portal URL to refresh session cookies, specifically to obtain or update the JSESSIONID cookie.  This is crucial for maintaining a valid session on the site.  The response cookies are handled to ensure the JSESSIONID is properly updated.


4. **JSESSIONID Handling (`_handle_session_id`):** This method parses the response cookies to find the JSESSIONID. If found, it updates the internal `session_id` and updates the `cookies_jar` accordingly.


5. **Making a GET request (`make_get_request`):** This method performs a GET request to the specified `url` using the loaded `cookies_jar`. It ensures the session's cookies are updated and raises exceptions if the request fails. The function handles the case where `cookies` or `headers` are explicitly specified by the user.

6. **Short Affiliate Link (`short_affiliate_link`):**  This method builds a URL for generating a shortened affiliate link from a given `link_url`, appends it to a predefined base URL with the track ID, and then uses the `make_get_request` function to execute the request.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.alirequests import AliRequests
    from pathlib import Path

    # Replace with the actual path to the cookie file directory
    cookie_dir = Path("your_cookie_directory")

    # Initialize the AliRequests class
    aliexpress_requests = AliRequests()

    # Example usage for making a GET request
    url_to_fetch = "https://www.aliexpress.com/item/1234567890.html"
    response = aliexpress_requests.make_get_request(url_to_fetch)

    if response:
        # Process the response
        print(response.status_code)
        print(response.text)
    else:
        print("Request failed.")

    # Example usage for short affiliate link
    link_to_shorten = "https://www.example.com/product"
    shortened_link_response = aliexpress_requests.short_affiliate_link(link_to_shorten)

    if shortened_link_response:
        # Process the shortened link response
        print(shortened_link_response.text)
    else:
        print("Shortening link request failed.")