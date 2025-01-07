# <input code>

```python
## \file hypotez/src/suppliers/hb/category.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.hb 
	:platform: Windows, Unix
	:synopsis:

"""



"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.suppliers.hb """


"""  Модуль сбора товаров со страницы категорий поставщика hb.co.il через вебдрайвер
У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категорий `PrestaShop.categories <-> aliexpress.shop.categoies`
- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Итерируясь по списку передает управление в `grab_product_page()` отсылая функции текущий url страницы  
`grab_product_page()` обрабатывает поля товара и передает управление классу `Product` 

"""
...

from typing import Dict, List
from pathlib import Path

from src import gs
from src.logger import logger
from src.webdriver.driver import Driver
from src.suppliers import Supplier


def get_list_products_in_category (s: Supplier) -> list[str, str, None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
    ...
    d:Driver = s.driver
    l: dict = s.locators['category']
    ...
    d.wait(1)
    d.execute_locator (s.locators ['product']['close_banner'] )
    d.scroll()
    ...

    list_products_in_category: List = d.execute_locator(l['product_links'])

    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        ...
        return
    ...
    while d.current_url != d.previous_url:
        if paginator(d,l,list_products_in_category):
            list_products_in_category.append(d.execute_locator(l['product_links']))
        else:
            break
        
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category

    logger.debug(f""" Found {len(list_products_in_category)} items in category {s.current_scenario['name']} """)
    
    return list_products_in_category

def paginator(d:Driver, locator: dict, list_products_in_category: list):
    """ Листалка """
    response = d.execute_locator(locator['pagination']['<-'])
    if not response or (isinstance(response, list) and len(response) == 0): 
        ...
        return
    return True

def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...

```

# <algorithm>

**Шаг 1:** Функция `get_list_products_in_category` получает объект `Supplier` как аргумент.
**Шаг 2:** Извлекает драйвер (`Driver`) и локаторы (`locators`) из объекта `Supplier`.
**Шаг 3:** Выполняет ожидание (wait) и действия с драйвером (например, закрытие баннера и прокрутка страницы).
**Шаг 4:** Ищет ссылки на товары (`product_links`) на странице категории.
**Шаг 5:** Если ссылок нет, записывает предупреждение в лог и возвращает `None`.
**Шаг 6:** В цикле проверяет, изменился ли текущий URL.
**Шаг 7:** Если URL изменился, вызывает функцию `paginator`, чтобы получить ссылки с новой страницы, добавляет их в список.
**Шаг 8:** Если URL не изменился, цикл завершается.
**Шаг 9:** Преобразует список ссылок в единичный список, если он был строкой.
**Шаг 10:** Выводит сообщение в лог о количестве найденных товаров.
**Шаг 11:** Возвращает список ссылок.

**Функция `paginator`:**
**Шаг 1:** Ищет на странице элемент пагинации (следующая страница).
**Шаг 2:** Если элемент пагинации найден, возвращает `True`. В противном случае - `False`.

**Пример данных:**

`s`: Объект `Supplier` содержащий драйвер и локаторы для вебдрайвера.
`l`: Словарь локаторов для текущей категории.
`list_products_in_category`: Список URL адресов товаров.
`d.current_url`, `d.previous_url`:  Текущий и предыдущий URL страницы.


# <mermaid>

```mermaid
graph TD
    A[get_list_products_in_category(s)] --> B{Получить драйвер и локаторы};
    B -- s.driver, s.locators -> C[Выполнение действий с драйвером];
    C --> D{Поиск ссылок на товары};
    D -- ссылки -> E[Проверка наличия ссылок];
    E -- Нет ссылок -> F[Лог предупреждения и возврат None];
    E -- Есть ссылки -> G{Проверка изменения URL};
    G -- URL не изменился -> H[Возврат списка ссылок];
    G -- URL изменился -> I[paginator(d, l, list_products_in_category)];
    I --> J[Добавление ссылок в list_products_in_category];
    J --> G;
    H --> K[Лог количества товаров];
    K --> H;
    I --> K;

    subgraph "paginator(d, l, list_products_in_category)"
        I1[Поиск элемента пагинации] --> I2{Проверка наличия элемента};
        I2 -- Наличие элемента -> I3[Возврат True];
        I2 -- Отсутствие элемента -> I4[Возврат False];
    end
```

**Подключаемые зависимости:**

* `gs`: Вероятно, модуль для работы с Google Sheets или другим хранилищем данных.
* `logger`: Модуль для логирования, вероятно, из `src.logger`.
* `Driver`: Класс для взаимодействия с веб-драйвером, из `src.webdriver.driver`.
* `Supplier`: Базовый класс поставщика, из `src.suppliers`.


# <explanation>

* **Импорты:**
    * `from typing import Dict, List`: необходимы для указания типов данных.
    * `from pathlib import Path`: используется для работы с файлами, но в данном коде не используется напрямую.
    * `from src import gs`: импортирует модуль для работы с Google Sheets.
    * `from src.logger import logger`: импортирует класс для логирования.
    * `from src.webdriver.driver import Driver`: импортирует класс для взаимодействия с веб-драйвером.
    * `from src.suppliers import Supplier`: импортирует класс для работы с поставщиками.

Связь с пакетами `src` (иерархическая):  Код организован иерархически. Модули `gs`, `logger`, `Driver` и `Supplier` находятся в подпакетах пакета `src`. Это позволяет организовать проект в виде модулей, которые можно использовать в других частях программы.

* **Классы:**
    * `Supplier`: Вероятно, базовый класс, содержащий общие методы для работы с разными поставщиками.
    * `Driver`: Класс, предоставляющий методы для управления веб-драйвером (например, `wait`, `execute_locator`, `scroll`).
* **Функции:**
    * `get_list_products_in_category`: собирает ссылки на товары из категории.
    * `paginator`: функция для обработки пагинации (если есть страницы с товарами, переходя на следующие).
    * `get_list_categories_from_site`: функция для сбора списка категорий.
* **Переменные:**
    * `MODE`: переменная, которая указывает режим работы (например, 'dev' или 'prod').
    * `s`: Объект `Supplier`, содержащий данные о текущем поставщике (драйвер, локаторы).
    * `l`: Словарь локаторов для вебэлементов на странице категории.
    * `list_products_in_category`: Список URL адресов товаров на странице категории.

* **Возможные ошибки и улучшения:**
    * Отсутствует обработка исключений: код не обрабатывает потенциальные ошибки при работе с веб-драйвером (например, если элемент не найден).
    * Неясно, как определяется `s.locators`. Необходимо определить, как `Supplier` получает локаторы и как они хранятся.
    * Не хватает проверок на корректность входящих данных (например, тип объекта `s`).
    * Нет явного использования пагинации.  Возможно, страница имеет несколько страниц, содержащих товары.

**Цепочка взаимосвязей:**

Функция `get_list_products_in_category` использует класс `Driver` и локаторы `locators`. `Supplier` предоставляет экземпляр `Driver` и данные `locators` для работы. `Supplier` взаимодействует с другими частями проекта через интерфейсы.  Возможно, `Supplier` получает данные о текущем сценарии (название категории), необходимые для вывода логов.  `get_list_products_in_category`  работает с текущим сценарием через атрибут `s.current_scenario['name']`.