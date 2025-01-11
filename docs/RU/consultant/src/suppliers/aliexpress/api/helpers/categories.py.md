# Анализ кода модуля `categories`

**Качество кода**
7
- Плюсы
    - Код выполняет фильтрацию категорий, как родительских, так и дочерних, по заданным критериям.
    - Присутствуют docstring для функций, описывающие их назначение, аргументы и возвращаемое значение.
    - Обрабатывается ситуация, когда на вход подаётся не список категорий.
- Минусы
    - Отсутствует импорт `logger` из `src.logger`.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`, поскольку файл не загружается, а функции работают со структурами данных.
    - Комментарии docstring не соответствуют стандарту reStructuredText (RST) и Sphinx.
    - Не хватает описания модуля в начале файла.
    - Нет обработки ошибок с использованием `logger.error`.
    -  Не все комментарии в коде являются пояснениями.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла, чтобы предоставить общее представление о его назначении.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Переписать комментарии docstring в формате RST.
4.  Убрать лишние комментарии и добавить пояснения к важным частям кода.
5.  Использовать явную проверку на тип для `categories`, а не `isinstance` с несколькими типами.
6.  В блоках `if` где происходит присвоение, добавить комментарий.
7.  Сделать проверку на наличие атрибута `parent_category_id` более читаемой.
8.  Добавить примеры использования функций в docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
# <- venv win
"""
Модуль для работы с категориями и подкатегориями API Aliexpress.
==============================================================

Этот модуль содержит функции для фильтрации категорий и подкатегорий,
возвращая списки категорий на основе заданных критериев.

Пример использования
--------------------
    
    from src.suppliers.aliexpress.api import models
    from src.suppliers.aliexpress.api.helpers import categories
    
    categories_data = [
        models.Category(id=1, name='Category 1'),
        models.ChildCategory(id=2, name='Child Category 1', parent_category_id=1),
        models.Category(id=3, name='Category 2'),
        models.ChildCategory(id=4, name='Child Category 2', parent_category_id=3),
    ]

    parent_categories = categories.filter_parent_categories(categories_data)
    child_categories = categories.filter_child_categories(categories_data, 1)

    print([c.name for c in parent_categories])
    print([c.name for c in child_categories])
"""
from typing import List, Union
from .. import models
from src.logger.logger import logger # Импортируем logger

def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Фильтрует и возвращает список категорий, не имеющих родительской категории.

    :param categories: Список объектов категорий или дочерних категорий.
    :type categories: List[models.Category | models.ChildCategory]
    :return: Список объектов категорий без родительской категории.
    :rtype: List[models.Category]

    Пример использования:
    
    .. code-block:: python

        from src.suppliers.aliexpress.api import models
        from src.suppliers.aliexpress.api.helpers import categories

        categories_data = [
            models.Category(id=1, name='Category 1'),
            models.ChildCategory(id=2, name='Child Category 1', parent_category_id=1),
            models.Category(id=3, name='Category 2'),
            models.ChildCategory(id=4, name='Child Category 2', parent_category_id=3),
        ]

        parent_categories = categories.filter_parent_categories(categories_data)
        print([c.name for c in parent_categories])
    """
    filtered_categories = []
    # Проверка, является ли categories списком. Если нет, создается список из одного элемента.
    if not isinstance(categories, list):
        categories = [categories]
    # Перебор элементов списка categories.
    for category in categories:
        # Проверка, что у категории нет атрибута 'parent_category_id'.
        if not hasattr(category, 'parent_category_id'):
            # Добавляем категорию в список.
            filtered_categories.append(category)
    # Возвращаем отфильтрованный список категорий.
    return filtered_categories

def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Фильтрует и возвращает список дочерних категорий, принадлежащих указанной родительской категории.

    :param categories: Список объектов категорий или дочерних категорий.
    :type categories: List[models.Category | models.ChildCategory]
    :param parent_category_id: ID родительской категории, по которой фильтруются дочерние категории.
    :type parent_category_id: int
    :return: Список объектов дочерних категорий с указанным ID родительской категории.
    :rtype: List[models.ChildCategory]

    Пример использования:
    
    .. code-block:: python

        from src.suppliers.aliexpress.api import models
        from src.suppliers.aliexpress.api.helpers import categories

        categories_data = [
            models.Category(id=1, name='Category 1'),
            models.ChildCategory(id=2, name='Child Category 1', parent_category_id=1),
            models.Category(id=3, name='Category 2'),
            models.ChildCategory(id=4, name='Child Category 2', parent_category_id=3),
        ]

        child_categories = categories.filter_child_categories(categories_data, 1)
        print([c.name for c in child_categories])
    """
    filtered_categories = []
    # Проверка, является ли categories списком. Если нет, создается список из одного элемента.
    if not isinstance(categories, list):
        categories = [categories]
    # Перебор элементов списка categories.
    for category in categories:
        # Проверка наличия атрибута 'parent_category_id' и соответствия его значения заданному 'parent_category_id'.
        if hasattr(category, 'parent_category_id') and getattr(category, 'parent_category_id') == parent_category_id:
            # Добавляем категорию в список.
            filtered_categories.append(category)
    # Возвращаем отфильтрованный список дочерних категорий.
    return filtered_categories
```