## \file hypotez/src/webdriver/edge/_experiments/edge.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.webdriver.edge._experiments 
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
  
""" module: src.webdriver.edge._experiments """


from pathlib import Path
import os
import json
from selenium.webdriver import Edge as WebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
from src import gs
from src.utils.printer import pprint,  j_loads
from src.logger import logger
from src.logger.exceptions import WebDriverException 



class Edge(WebDriver):
    """
    Subclass of `selenium.webdriver.Edge` that provides additional functionality.

    @param actions (ActionChains): A `selenium.webdriver.common.action_chains.ActionChains` object that can be used to perform advanced interactions with the Edge webdriver.
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """Initializes the Edge webdriver with the specified launch options and profile."""
        self.payload_Edge(*args, **kwargs)

    def payload_Edge(self, *args, **kwargs):
        """Loads the launch parameters for `Edge`.

        @param args `*args`: Additional arguments.
        @param kwargs `**kwargs`: Additional named arguments.
        """
        # Load Edge settings from a JSON file or any other configuration method
        edge_settings: dict = json.loads(Path(gs.path.src, 'webdriver', 'edge', 'edge.json'))

        edgedriver_path: str = rf"C:\Users\user\Documents\repos\hypotez\bin\msedgedriver_124.exe"

        options: EdgeOptions = self.set_options(edge_settings.get('options'))

        profile_path: str = edge_settings['profile']['profile_path']['os']

        try:
            service = EdgeService(str(Path(gs.path.bin, edgedriver_path)))
            super().__init__(options, service, True)
        except WebDriverException as e:
            logger.critical(f""" """, e)
            """ @todo Implement driver restart"""
            return
        except Exception as e:
            logger.critical(f' Edge webdriver crashed. General error:  ', e)
            """ @todo Implement program restart"""
            return

    def set_options(self, opts=None) -> EdgeOptions:
        """Launch options for the Edge webdriver."""
        options = EdgeOptions()
        if opts:
            for opt in opts:
                # Set options as needed for Edge
                options.add_argument(opt)
        return options


