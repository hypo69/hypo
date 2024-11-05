#! /usr/bin/python
﻿## \file src/logger/__init__.py
## \file /src/logger/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Logger """
...
from packaging.version import Version
from .version import __version__, __doc__, __details__       

from .logger import logger
#from .beeper import Beeper
from .exceptions import ExecuteLocatorException, DefaultSettingsException, CredentialsError, PrestaShopException, PayloadChecksumError