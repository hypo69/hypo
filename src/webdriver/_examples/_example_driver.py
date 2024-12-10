## \file hypotez/src/webdriver/_examples/_example_driver.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.webdriver._examples 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.webdriver._examples """


# example.py

from src.webdriver.driver import Driver, Chrome, Firefox, Edge

def main():
    """ Main function to demonstrate how to use the Driver class with different web browsers."""

    # Create an instance of the Driver class with the Chrome webdriver
    print("Creating a Chrome browser instance...")
    chrome_driver = Driver(Chrome)

    try:
        # Navigate to a URL and check if successful
        url = "https://www.example.com"
        if chrome_driver.get_url(url):
            print(f"Successfully navigated to {url}")
        else:
            print(f"Failed to navigate to {url}")

        # Extract the domain from the URL
        domain = chrome_driver.extract_domain(url)
        print(f"Extracted domain: {domain}")

        # Scroll down the page
        if chrome_driver.scroll(scrolls=3, direction='forward'):
            print("Successfully scrolled down the page")
        else:
            print("Failed to scroll down the page")

        # Save cookies to a file
        if chrome_driver._save_cookies_localy(to_file='cookies_chrome.pkl'):
            print("Cookies saved successfully")
        else:
            print("Failed to save cookies")

    finally:
        # Ensure that the driver is closed
        chrome_driver.quit()
        print("Chrome browser closed.")

    # Create an instance of the Driver class with the Firefox webdriver
    print("Creating a Firefox browser instance...")
    firefox_driver = Driver(Firefox)

    try:
        # Navigate to a URL and check if successful
        url = "https://www.example.com"
        if firefox_driver.get_url(url):
            print(f"Successfully navigated to {url}")
        else:
            print(f"Failed to navigate to {url}")

        # Extract the domain from the URL
        domain = firefox_driver.extract_domain(url)
        print(f"Extracted domain: {domain}")

        # Scroll up the page
        if firefox_driver.scroll(scrolls=2, direction='backward'):
            print("Successfully scrolled up the page")
        else:
            print("Failed to scroll up the page")

        # Save cookies to a file
        if firefox_driver._save_cookies_localy(to_file='cookies_firefox.pkl'):
            print("Cookies saved successfully")
        else:
            print("Failed to save cookies")

    finally:
        # Ensure that the driver is closed
        firefox_driver.quit()
        print("Firefox browser closed.")

    # Create an instance of the Driver class with the Edge webdriver
    print("Creating an Edge browser instance...")
    edge_driver = Driver(Edge)

    try:
        # Navigate to a URL and check if successful
        url = "https://www.example.com"
        if edge_driver.get_url(url):
            print(f"Successfully navigated to {url}")
        else:
            print(f"Failed to navigate to {url}")

        # Extract the domain from the URL
        domain = edge_driver.extract_domain(url)
        print(f"Extracted domain: {domain}")

        # Scroll the page in both directions
        if edge_driver.scroll(scrolls=2, direction='both'):
            print("Successfully scrolled the page in both directions")
        else:
            print("Failed to scroll the page in both directions")

        # Save cookies to a file
        if edge_driver._save_cookies_localy(to_file='cookies_edge.pkl'):
            print("Cookies saved successfully")
        else:
            print("Failed to save cookies")

    finally:
        # Ensure that the driver is closed
        edge_driver.quit()
        print("Edge browser closed.")

if __name__ == "__main__":
    main()

