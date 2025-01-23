## \file /src/endpoints/advertisement/facebook/facebook_fields.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.advertisement.facebook 
	:platform: Windows, Unix
	:synopsis:

"""



from pathlib import Path
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

class FacebookFields:
    """Поля для `объявлний` и `эвентов` """

    def __init__(self):
        """"""
        ...
        self._payload()

    def _payload(self):
        """"""
        ...
        data = j_loads (Path (gs.path.src, 'advertisement', 'facebok', 'facebook_feilds.json'))
        if not data:
            logger.debug(f"Ошибка загрузки полей из файла {gs.path.src}/advertisement/facebok/facebook_feilds.json")
            return 
        for name, value in data.items():
            setattr(self, f'{name}', value)
        return True
