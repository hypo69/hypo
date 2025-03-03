
## \file /src/endpoints/advertisement/facebook/facebook.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.advertisement.facebook 
    :platform: Windows, Unix
    :synopsis: Модуль рекламы на фейсбук

 сценарии:
    - login: логин на фейсбук
    - post_message: отправка текствого сообщения в форму 
    - upload_media: Загрузка файла или списка файлов

"""


import os, sys
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List

from src import gs
from src.utils.jjson import j_loads, j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger
from .scenarios.login import login
from .scenarios import  switch_account, promote_post,  post_title, upload_media, update_images_captions


class Facebook():
    """  Класс общается с фейбуком через вебдрайвер """
    d: 'Driver'  # Строковая аннотация типа для откладывания импорта
    start_page: str = r'https://www.facebook.com/hypotez.promocodes'
    promoter: str

    def __init__(self, driver: 'Driver', promoter: str, group_file_paths: list[str], *args, **kwards):
        """ Я могу передать уже запущенный инстанс драйвера. Например, из алиэкспресс
        @todo:
            - Добавить проверку на какой странице открылся фейсбук. Если открылась страница логина - выполнитл сценарий логина
        """
        self.d = driver
        self.promoter = promoter
        ...
        
        #self.driver.get_url (self.start_page)
        #switch_account(self.driver) # <- переключение профиля, если не на своей странице

    def login(self) -> bool:
        return login(self)

    def promote_post(self, item: SimpleNamespace) -> bool:
        """ Функция отправляет текст в форму сообщения 
        @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
        @returns `True`, если успешно, иначе `False`
        """
        ...
        return promote_post(self.d, item)
    
    def promote_event(self, event: SimpleNamespace):
        """ Пример функции для продвижения события """
        ...
