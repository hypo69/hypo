# Анализ кода модуля `src.endpoints.prestashop.category`

**Качество кода**
7
-  Плюсы
    - Код структурирован и разбит на функции.
    - Присутствует базовая обработка ошибок.
    - Используются type hints для большей читаемости.
    - Присутствует docstring для класса `PrestaCategory`.
-  Минусы
    - Не все функции имеют docstring.
    - Отсутствует подробная документация в формате reStructuredText (RST) для всех функций.
    - Использование `try-except` блоков в коде не оптимально, предпочитается `logger.error`.
    - Комментарии после `#` требуют более подробного объяснения следующего блока кода.
    - Не используется `j_loads` для чтения данных из файлов.
    - Некоторые переменные именованы не достаточно явно (`_parent_category`).
    - Отсутствуют проверки на наличие ключей в словаре `category`.
    - Не обработана ситуация, когда `category` является `None`.

**Рекомендации по улучшению**
1.  Добавить docstring в формате reStructuredText (RST) для всех функций и методов.
2.  Использовать `j_loads` или `j_loads_ns` для чтения конфигурационных файлов.
3.  Заменить стандартные `try-except` на логирование ошибок через `logger.error` где это возможно.
4.  Добавить проверки на наличие ключей в словаре `category` перед их использованием.
5.  Добавить обработку случая когда `category` является `None`.
6.  Улучшить именование переменных для повышения читаемости.
7.  Добавить подробные комментарии `#` с пояснением, что делает код.
8.  Убрать избыточные комментарии и `...` если они не являются точкой остановки.

**Оптимизиробанный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с категориями PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`PrestaCategory`, который используется для взаимодействия с категориями PrestaShop через API.

Он предоставляет методы для добавления, удаления, обновления категорий, а также для получения списка родительских категорий.

.. image:: html categories_tree.png
   :alt: Дерево категорий PrestaShop

.. note::
    Клиенты могут иметь свои уникальные деревья категорий, которые понятны только им.
    Связывание продуктов с категориями описывается в сценариях поставщиков.
"""
MODE = 'dev'

import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict
from types import SimpleNamespace
from typing import Optional
from src import gs
from src.utils.jjson import j_loads
from src.logger.logger import logger
from .api import PrestaShop

class PrestaCategory(PrestaShop):
    """
    Класс для работы с категориями в PrestaShop.

    :param credentials: (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
    :param api_domain: (Optional[str], optional): Домен API. Defaults to None.
    :param api_key: (Optional[str], optional): Ключ API. Defaults to None.

    :raises ValueError: Если не указаны оба параметра api_domain и api_key.

    Пример использования класса::

        prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
        prestacategory.delete_category_PrestaShop(3)
        prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
        print(prestacategory.get_parent_categories_list_PrestaShop(5))
    """
    def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
        """
        Инициализация категории PrestaShop.

        :param credentials: Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`.
        :param api_domain: Домен API.
        :param api_key: Ключ API.
        :raises ValueError: Если не указаны оба параметра `api_domain` и `api_key`.
        """
        # Если переданы учетные данные через credentials, извлекаем из них api_domain и api_key.
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        # Проверяем, что оба параметра api_domain и api_key были переданы.
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')

        # Инициализируем родительский класс PrestaShop.
        super().__init__(api_domain, api_key, *args, **kwards)

    def get_parent_categories_list(self, id_category: str | int,  parent_categories_list: List[int] = []) -> list:
        """
        Получает список родительских категорий для заданной категории.

        :param id_category: ID категории, для которой нужно получить родительские категории.
        :type id_category: str | int
        :param parent_categories_list: Список для хранения родительских категорий (используется в рекурсии).
        :type parent_categories_list: List[int]
        :return: Список родительских категорий.
        :rtype: list

        :raises ValueError: Если `id_category` не предоставлен.

        .. todo::
            Обработать ситуацию, когда у клиента нет такой категории.
            Например, в магазине мебели не должно быть категории `motherboards`.
        """
        # Проверяем, что id_category был передан.
        if not id_category:
            logger.error(f"""Нет id категории!!!
                         {parent_categories_list}
                    Если отправить запрос без id вернется словарь со всеми категориями""")
            return parent_categories_list

        # Получаем данные о категории из API PrestaShop.
        category = super().get('categories', resource_id = id_category, display='full', io_format='JSON')
        """
         возвращает словарь
         пример::
             {
                 'category': {
                     'id': 11259,
                     'id_parent': '11248',
                     'level_depth': '5',
                     'nb_products_recursive': -1,
                     'active': '1',
                     'id_shop_default': '1',
                     'is_root_category': '0',
                     'position': '0',
                     'date_add': '2023-07-25 11:58:08',
                     ...
                  }
             }
        """
        # Проверяем, что категория была найдена.
        if not category:
            logger.error(f'Не удалось получить данные категории с ID: {id_category}')
            return parent_categories_list

        # Проверяем наличие ключей в словаре `category`
        if 'category' not in category or 'id_parent' not in category['category']:
             logger.error(f'В ответе от API отсутствуют необходимые ключи "category" или "id_parent" для категории с ID: {id_category}. Ответ: {category}')
             return parent_categories_list

        # Извлекаем id родительской категории из ответа API.
        try:
            _parent_category: int = int(category['category']['id_parent'])
        except (KeyError, ValueError) as e:
            logger.error(f'Ошибка при извлечении id родительской категории из ответа API. {e}', exc_info=True)
            return parent_categories_list

        # Добавляем id родительской категории в список.
        parent_categories_list.append(_parent_category)

        # Если родительская категория является корневой (<= 2), возвращаем список.
        if _parent_category <= 2:
            return parent_categories_list
        # Иначе, рекурсивно вызываем функцию для получения родительских категорий.
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)

```