## \file hypotez/src/endpoints/kazarinov/parser_onetab.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
""" module: src.endpoints.kazarinov """
"""Модуль для парсинга URL из страницы OneTab."""

MODE = 'debug'

import requests
from bs4 import BeautifulSoup
from typing import Optional, List, Tuple
from src.utils import pprint
from src.logger import logger
from src import gs


def prepare_one_tab(target_page_url: str) -> Tuple[int, str, List[str]] | bool:
    """Подготавливает данные для OneTab.

    Args:
        target_page_url (str): URL страницы OneTab.

    Returns:
        Tuple[int, str, List[str]] | bool: Кортеж из цены, имени и списка URL, 
        или `False`, если произошла ошибка.
    """
    return fetch_target_urls_onetab(target_page_url)


def fetch_target_urls_onetab(target_page_url: str) -> Tuple[int, str, List[str]] | bool:
    """Извлекает целевые URL с указанного URL OneTab.

    Выполняет GET-запрос к указанному URL, парсит HTML-контент
    и извлекает все ссылки из тегов 'a' с классом 'tabLink'.

    Args:
        target_page_url (str): URL страницы OneTab для извлечения целевых URL.

    Returns:
        Tuple[int, str, List[str]] | bool: Кортеж из цены, имени и списка URL 
        или `False`, если произошла ошибка.

    Raises:
        requests.exceptions.RequestException: При ошибке запроса.
    """
    try:
        response = requests.get(target_page_url, timeout=10)
        response.raise_for_status()

        if response.status_code != 200:
            logger.debug(f'Ошибка response\n{pprint(response)}')
            return False

        soup = BeautifulSoup(response.content, 'html.parser')

        # Извлечение ссылок
        urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

        # Извлечение данных из div с классом 'tabGroupLabel'
        element = soup.find('div', class_='tabGroupLabel')
        data = element.get_text() if element else None

        if not data:
            return False

        # Разбивка данных на цену и имя
        parts = data.split(maxsplit=1)
        try:
            price = int(parts[0])
        except ValueError as ex:
            logger.error(f'Ошибка при преобразовании цены: {ex}')
            return False

        mexiron_name = parts[1] if len(parts) > 1 else gs.now

        return price, mexiron_name, urls

    except requests.exceptions.RequestException as ex:
        logger.error(f'Ошибка при выполнении запроса: {ex}')
        return False
