""" вебдрайвер Firefox

This code defines a subclass of webdriver.Firefox called Firefox. 
It provides additional functionality such as the ability to launch Firefox 
in kiosk mode and the ability to set up a Firefox profile for the webdriver.

@image html class_firefox.png
"""
## \file src/webdriver/firefox/_experiments/start_driver.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional
import subprocess

import header
from header import __root__
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from src.webdriver import Driver, Firefox, Chrome
from src.utils import j_loads_ns
from src.logger import logger

__bin__ = Path(__root__, 'bin')
__src__ = Path(__root__, 'src')

# Set logging preferences
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['loggingPrefs'] = {'browser': 'ALL'}

# Initialize the Firefox driver with logging capabilities
d:Driver = Driver(Firefox, desired_capabilities=capabilities)

def driver_data(d):
    # Print browser and profile information
    version = d.execute_script("return navigator.userAgent;")
    print(f"Browser version (from user agent): {version}")

    capabilities = d.capabilities
    browser_version = capabilities.get('browserVersion')
    print(f"Browser version (from capabilities): {browser_version}")

    profile_path = capabilities.get('moz:profile')
    print(f"Profile information: {profile_path}")

    def get_profile_entry():
        # Print profile contents
        if profile_path:
            profile_dir = Path(profile_path)
            for root, dirs, files in os.walk(profile_dir):
                for name in files:
                    print(os.path.join(root, name))
                    
    def get_executable_path():
        # Get Firefox executable path
        process_name = "firefox.exe"
        try:
            result = subprocess.run(
                ["wmic", "process", "where", f"name='{process_name}'", "get", "ExecutablePath"],
                capture_output=True,
                text=True,
                check=True
            )
            executable_path = result.stdout.strip().split('\n')[-1]
            print(f"Firefox executable path: {executable_path}")
        except subprocess.CalledProcessError as ex:
            logger.error("Failed to get executable path for Firefox", ex)

    # Print browser logs
    try:
        logs = d.get_log('browser')
        for log in logs:
            print(log)
    except Exception as ex:
        logger.error("Failed to retrieve browser logs", ex)

driver_data(d)


