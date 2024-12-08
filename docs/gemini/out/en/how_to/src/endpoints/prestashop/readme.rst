rst
How to Access and Use PrestaShop Website APIs
========================================================================================

Description
-------------------------
This document outlines how to access and utilize the APIs for your PrestaShop websites.  It details the location of API keys, providing a template and example for making API requests.

Execution steps
-------------------------
1. **Identify the target website:** Determine which PrestaShop website's API you need to interact with (e.g., `e-cat.co.il`).

2. **Retrieve the API key:** Locate the API key for the chosen website within the `credentials.kdbx` file.  Use a password manager (e.g., KeePass, KeePassXC) that supports this format to securely access and handle this file.  The file contains the website URL, API key, and potential additional metadata.

3. **Encode the API key:** Convert the retrieved API key into Base64 format.  This is a crucial step for secure API communication.

4. **Construct the API request:** Utilize the provided template to assemble the complete API request.  Substitute the placeholder values (`<SITE_URL>`, `<endpoint>`) with the appropriate values for your target website and API endpoint. Replace `<base64(API_KEY)>` with the Base64-encoded API key you generated in step 3.

5. **Execute the API request:** Use the `curl` command-line tool to send the constructed API request to the target website.

6. **Interpret the response:** Analyze the response received from the API.  Refer to the PrestaShop API documentation for details on the expected format and content of the response.


Usage example
-------------------------
.. code-block:: bash

    curl -X GET 'https://e-cat.co.il/api/products' \
    -H 'Authorization: Basic <YOUR_BASE64_ENCODED_API_KEY>'