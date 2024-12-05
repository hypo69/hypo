# PrestaShop Website Endpoints

## Overview

This document details the structure and usage of PrestaShop websites, including API key storage and example API calls.

## Table of Contents

* [Websites](#websites)
* [Storing API Keys](#storing-api-keys)
* [Example API Usage](#example-api-usage)
    * [API Request Example](#api-request-example)
    * [Example API Call](#example-api-call)
* [Security Recommendations](#security-recommendations)
* [Additional Resources](#additional-resources)

## Websites

Your PrestaShop websites are:

1. [e-cat.co.il](https://e-cat.co.il)
2. [emil-design.com](https://emil-design.com)
3. [sergey.mymaster.co.il](https://sergey.mymaster.co.il)

Each website utilizes APIs to interact with various parameters and functions.

## Storing API Keys

API keys for each website are stored in the `credentials.kdbx` file.  This is a secure password database.  It contains the following data for each website:

* Website URL
* API Key
* Additional metadata (if necessary)

Use a password manager supporting the `.kdbx` format, such as [KeePass](https://keepass.info/) or [KeePassXC](https://keepassxc.org/), to work with the keys.

## Example API Usage

To connect to a PrestaShop website's API, follow the template below.

### API Request Example

**API Request Template:**

```bash
curl -X GET 'https://<SITE_URL>/api/<endpoint>' \
-H 'Authorization: Basic <base64(API_KEY)>'
```

**Parameter Explanation:**

* `<SITE_URL>`: The website address (e.g., `e-cat.co.il`).
* `<endpoint>`: The API endpoint (e.g., `products`, `customers`).
* `<API_KEY>`: The API key, encoded in Base64.

### Example API Call

To fetch a list of products from `e-cat.co.il`:

```bash
curl -X GET 'https://e-cat.co.il/api/products' \
-H 'Authorization: Basic <base64(API_KEY)>'
```


## Security Recommendations

* Never share the `credentials.kdbx` file.
* Store the file securely, accessible only to you.
* Regularly update your API keys and database passwords.


## Additional Resources

For further information on available endpoints and API interaction, refer to the official [PrestaShop API documentation](https://devdocs.prestashop.com/).