## \file ./src/endpoints/advertisement/facebook/__init__.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .facebook import Facebook
from .facebook_fields import FacebookFields
from .promoter import FacebookPromoter, get_event_url