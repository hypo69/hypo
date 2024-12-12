# Анализ кода модуля `categories.py`

**Качество кода**
7
-  Плюсы
    - Код выполняет фильтрацию категорий на основе их родительских связей.
    - Функции `filter_parent_categories` и `filter_child_categories` достаточно ясны по своей логике.
    -  Присутствует проверка типов входных данных, что делает функции более устойчивыми к ошибкам.
-  Минусы
    - Отсутствует docstring модуля.
    - Нет обработки ошибок и логирования.
    -  Не используются `j_loads` или `j_loads_ns`.
    -  В коде есть импорт, который закомментирован.
    -  В функциях нет проверки на `None` для входных данных.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля с описанием его назначения и содержания.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Удалить закомментированный импорт.
4.  Добавить валидацию входящих параметров, например проверку на `None`.
5.  Переписать docstring функций в формате reStructuredText (RST).
6.  Добавить обработку ошибок с помощью `logger.error`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~
"""
Модуль для фильтрации категорий и подкатегорий API Aliexpress.
==============================================================

Этот модуль предоставляет функции для фильтрации категорий и подкатегорий на основе их родительских связей.
Функции позволяют выделить главные категории, не имеющие родительских категорий,
а также подкатегории, принадлежащие определенной родительской категории.
"""
from typing import List, Union
from .. import models
from src.logger.logger import logger  # Добавлен импорт логгера


def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Фильтрует и возвращает список категорий, не имеющих родительской категории.

    :param categories: Список объектов категорий или дочерних категорий.
    :type categories: List[models.Category | models.ChildCategory]
    :raises TypeError: Если входные данные являются `None`.
    :return: Список объектов категорий без родительской категории.
    :rtype: List[models.Category]
    """
    #  Проверка на None для входных данных
    if categories is None:
        logger.error('Входные данные не должны быть None')
        return []

    filtered_categories = []

    # Преобразует в список, если передан одиночный элемент
    if isinstance(categories, (str, int, float)):
        categories = [categories]

    for category in categories:
        #  Проверка наличия атрибута parent_category_id
        if not hasattr(category, 'parent_category_id'):
            filtered_categories.append(category)

    return filtered_categories


def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Фильтрует и возвращает список дочерних категорий, принадлежащих указанной родительской категории.

    :param categories: Список объектов категорий или дочерних категорий.
    :type categories: List[models.Category | models.ChildCategory]
    :param parent_category_id: Идентификатор родительской категории, по которому фильтруются дочерние категории.
    :type parent_category_id: int
    :raises TypeError: Если входные данные являются `None`.
    :return: Список объектов дочерних категорий с указанным идентификатором родительской категории.
    :rtype: List[models.ChildCategory]
    """
    #  Проверка на None для входных данных
    if categories is None:
        logger.error('Входные данные не должны быть None')
        return []

    filtered_categories = []
    # Преобразует в список, если передан одиночный элемент
    if isinstance(categories, (str, int, float)):
        categories = [categories]

    for category in categories:
        #  Проверка наличия атрибута parent_category_id и совпадение ID
        if hasattr(category, 'parent_category_id') and category.parent_category_id == parent_category_id:
            filtered_categories.append(category)

    return filtered_categories
```