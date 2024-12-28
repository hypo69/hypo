# <input code>

```python
## \file hypotez/src/endpoints/prestashop/category.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.prestashop 
	:platform: Windows, Unix
	:synopsis: `PrestaCategory` layer between client categories (PrestaShop, in my case) and suppliers
The class provides methods for adding, deleting, updating categories, 
as well as obtaining a list of parent categories from a given one.

locator_description Clients can each have their own unique category tree, which is only understandable to them. 
Product binding to category is described in supplier scenarios

@image html categories_tree.png 
"""
...



import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict, Optional
from types import SimpleNamespace

import header
from src import gs
from src.utils.jjson import j_loads
from .api import PrestaShop
from src.logger import logger


class PrestaCategory(PrestaShop):
    """    
    Класс для работы с категориями в PrestaShop.

    Пример использования класса:

    .. code-block:: python

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
        """Инициализация категории PrestaShop.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
            api_domain (Optional[str], optional): Домен API. Defaults to None.
            api_key (Optional[str], optional): Ключ API. Defaults to None.
        """
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)
        
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        
        super().__init__(api_domain, api_key, *args, **kwards)


    def get_parent_categories_list(self, id_category: str | int,  parent_categories_list:List[int] = []) -> list:
        """  Вытаскивет из базы данных PrestaShop родительские категории от заданной 
        @details функция через API получает список категорий

        @param id_category `int`  категория для которой надо вытащить родителя
        @param dept `int = 0` : глубина рекурсии. Если 0, глубина не ограчинена
        @returns `list`  Список родительских категорий
        @todo обработать ситуацию, кода у клиента нет такой категории. 
        Напимер в магазине мебели не должно быть категории `motherboards`
        """
        if not id_category:
            logger.error(f"""Нет id категории!!!
                         {parent_categories_list}
                    Если отправить запрос без id вернется словарь со всми категориями""")
            return parent_categories_list
        category = super().get('categories', resource_id = id_category, display='full', io_format='JSON')
        if not category:
            logger.error(f'Что-то не так с категориями')
            return

        _parent_category = int(category['id_parent'])
        parent_categories_list.append(_parent_category)
        if _parent_category <= 2:
            return parent_categories_list
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)
```

# <algorithm>

**Шаг 1:** Функция `get_parent_categories_list` получает `id_category` и `parent_categories_list` (инициализированный как пустой список).

**Шаг 2:** Проверяет, что `id_category` определен. Если нет, выводит лог об ошибке и возвращает исходный список.

**Шаг 3:** Вызывает базовый метод `get` класса `PrestaShop` для получения данных категории по `id_category`.  Аргументы `display='full'` и `io_format='JSON'` указывают на то, что требуется полная информация в формате JSON.

**Шаг 4:** Проверяет, что ответ от API не пуст. Если пусто, то выводит сообщение об ошибке и возвращает None.

**Шаг 5:** Извлекает `id_parent` из полученного словаря `category`.

**Шаг 6:** Добавляет `id_parent` в список `parent_categories_list`.

**Шаг 7:** Проверяет, является ли `id_parent` корневой категорией (значение меньше или равно 2). Если да, возвращает `parent_categories_list`.

**Шаг 8:** Если `id_parent` не является корневой категорией, рекурсивно вызывает функцию `get_parent_categories_list` с `id_parent` и текущим списком `parent_categories_list`.


**Пример:**

Если `id_category` = 10,  алгоритм будет искать родителя категории 10, добавляя его в список и повторяя процесс для родителя, пока не дойдет до корневой категории или у него не окажется родителя.


# <mermaid>

```mermaid
graph TD
    A[PrestaCategory.get_parent_categories_list] --> B{id_category is valid?};
    B -- Yes --> C[API Call];
    B -- No --> D[Error Log & Return parent_categories_list];
    C --> E{category data empty?};
    E -- Yes --> F[Error Log & Return];
    E -- No --> G[Extract id_parent];
    G --> H[Append id_parent to parent_categories_list];
    H --> I{id_parent <= 2?};
    I -- Yes --> J[Return parent_categories_list];
    I -- No --> K[PrestaCategory.get_parent_categories_list(id_parent)];
    K --> H;
```

**Описание диаграммы:**

Диаграмма иллюстрирует поток данных и вызовов.  Главная функция `PrestaCategory.get_parent_categories_list` вызывает функцию `get` в базовом классе `PrestaShop` для получения данных.  В случае успешного получения данных, извлекается `id_parent`, и функция рекурсивно вызывает себя для получения родительских категорий. Если `id_parent` равен или меньше 2 (корень), то возвращается список родительских категорий.


# <explanation>

**Импорты:**

- `requests`:  Библиотека для работы с HTTP-запросами, используется для взаимодействия с API PrestaShop.
- `attr`: Модуль для аннотаций атрибутов, используется для улучшения описания и обработки данных, но в данном случае не используется явно.
- `pathlib`: Модуль для работы с путями к файлам и каталогам (не используется непосредственно в данном коде).
- `typing`: Модуль для типов данных.  `List`, `Dict`, `Optional`  используются для явного указания типов данных, что делает код более понятным и помогает избежать ошибок.
- `types`: Модуль для встроенных типов данных.  `SimpleNamespace`  используется для хранения параметров API.
- `header`: Непонятно, что это, возможно, содержит вспомогательные функции или константы. Нужно посмотреть файл `header.py`
- `src`: Входная точка проекта.  `gs`, `src.utils.jjson`, `src.logger` — части внутренней структуры проекта.  Импорты показывают иерархию пакетов.
- `.api`: Подпапка, содержащая класс `PrestaShop`, который определяет общие методы для работы с API PrestaShop.
- `PrestaShop`: Этот класс содержит методы для работы с API PrestaShop, которые могут быть повторно использованы другими частями приложения.

**Классы:**

- `PrestaCategory`: Этот класс наследует от класса `PrestaShop`. Он предоставляет методы для работы с категориями в PrestaShop, такие как получение списка родительских категорий.  Инициализация требует `api_domain` и `api_key`. `credentials` — необязательный аргумент для передачи этих данных в виде словаря или `SimpleNamespace`.

**Функции:**

- `get_parent_categories_list`: Функция рекурсивно получает список родительских категорий для заданной категории. Она принимает `id_category`, и  `parent_categories_list` — список родительских категорий,  возвращает список ID родительских категорий.

**Переменные:**

- `MODE`: Вероятно, константа для определения режима работы приложения (например, "dev" или "prod").
- `credentials`: Словарь или `SimpleNamespace`, содержащий учетные данные для доступа к API Престашоп.
- `id_category`: Целое число, представляющее идентификатор категории.
- `parent_categories_list`: Список идентификаторов родительских категорий.

**Возможные ошибки и улучшения:**

- **Обработка ошибок:**  Код обрабатывает пустой ответ API, но не обрабатывает другие возможные исключения (например, проблемы с соединением или некорректный формат данных).
- **Проверка входных данных:** Добавление проверки `id_category` на корректный тип данных.
- **Обработка не найденных категорий:**  Необходимо предусмотреть обработку ситуации, когда категория с заданным `id_category` не найдена.  (Сейчас возвращается `None`, что может привести к ошибке).
- **Повторные запросы API:**  В рекурсивном вызове `get_parent_categories_list` есть возможность повтора запроса API. Лучше добавить проверку в список уже полученных `id`-категорий.
- **Глубина рекурсии:**  Рекурсия может привести к проблемам, если дерево категорий слишком глубокое. Нужно ограничить глубину рекурсии, чтобы избежать `RecursionError`.
- **Проверка на циклы в дереве:** Необходимо убедиться, что дерево категорий не содержит циклов.

**Взаимосвязь с другими частями проекта:**

Код использует классы и функции из других модулей проекта, таких как `PrestaShop`, `logger`, `j_loads`, что предполагает наличие соответствующих импортов и определений в этих модулях. `header.py` также участвует в проекте.  Необходимо проанализировать его содержимое, чтобы понять его функциональность.