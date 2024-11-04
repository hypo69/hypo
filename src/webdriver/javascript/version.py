## \file src/webdriver/version.py
## \file src/webdriver/javascript/version.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
__name__ = '' 
__version__="3.12.0.0.0.4"
__doc__ = ''
__details__="Added support for Edge and Chrome drivers."
__annotations__ = ''
__examples__ = f"""
from src.webdriver.firefox.firefox import Firefox
from src.driver import Driver

def main():
    d = Driver(Firefox)
    content = d.get_url("https://www.example.com")
    if content:
        print("Page content fetched successfully")
    else:
        print("Failed to fetch page content")

if __name__ == "__main__":
    main()
    """
__author__='hypotez '

