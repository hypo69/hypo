## \file /src/logger/__init__.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.logger 
	:platform: Windows, Unix
	:synopsis:

"""


from .logger import logger
#from .beeper import Beeper
from .exceptions import ( ExecuteLocatorException, 
                         DefaultSettingsException, 
                         CredentialsError, 
                         PrestaShopException, 
                         PayloadChecksumError
                        )