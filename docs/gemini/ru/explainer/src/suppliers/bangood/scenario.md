# <input code>

```python
## \file hypotez/src/suppliers/bangood/scenario.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.bangood 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


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
"""MODE = 'dev'
  
""" module: src.suppliers.bangood """


"""  Модуль сбора товаров со страницы категорий поставщика bangood.co.il через вебдрайвер
У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категорий `PrestaShop.categories <-> aliexpress.shop.categoies`
- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Итерируясь по списку передает управление в `grab_product_page()` отсылая функции текущий url страницы  
`grab_product_page()` обрабатывает поля товара и передает управление классу `Product` 

"""


from typing import Union
from pathlib import Path

from src import gs
from src.logger import logger

def get_list_products_in_category (s) -> list[str, str, None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
    d = s.driver
    

    l: dict = s.locators['category']
    
    d.execute_locator (s.locators ['product']['close_banner'] )
    
    if not l:
        """ Много проверок, потому, что код можно запускать от лица разных ихполнителей: Supplier, Product, Scenario """
        logger.error(f"А где локаторы? {l}")
        return
    d.scroll()

    #TODO: Нет листалки

    list_products_in_category = d.execute_locator(l['product_links'])
    """ Собирал ссылки на товары.  """
    
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        return
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category

    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    

    return list_products_in_category


def get_list_categories_from_site(s):
    ...
```

# <algorithm>

**Алгоритм работы функции `get_list_products_in_category`:**

1. **Принимает на вход объект `s`:**  Предполагается, что это объект `Supplier`, содержащий информацию о поставщике, включая драйвер `s.driver` и локаторы `s.locators`.
2. **Получает локаторы:**  Извлекает локаторы для элементов страницы категории из `s.locators['category']`.
3. **Закрывает баннер:**  Выполняет действие `d.execute_locator (s.locators ['product']['close_banner'] )`, предположительно закрывающее рекламный баннер.
4. **Проверка локаторов:** Проверяет, не пуст ли словарь локаторов (`l`). Если пуст, выводит ошибку и возвращает `None`.
5. **Прокрутка страницы:** Вызывает метод `d.scroll()`,  чтобы загрузить все элементы страницы. (Предполагается, что страница с товарами может быть длинной.)
6. **Получение ссылок на товары:**  Используя `d.execute_locator(l['product_links'])` получает список ссылок на товары.  
7. **Обработка результата:** Проверяет тип результата. Если это строка, преобразует её в список, содержащий только эту строку.
8. **Логирование:** Выводит информацию о количестве найденных товаров.
9. **Возвращает список ссылок:** Возвращает список ссылок на товары.


**Пример:**

Если `s.driver` представляет собой объект вебдрайвера, а `s.locators['category']['product_links']` содержит xpath выражение к элементу, содержащему ссылки на товары, то алгоритм получит список ссылок и вернет его.

# <mermaid>

```mermaid
graph TD
    A[get_list_products_in_category(s)] --> B{Проверка локаторов};
    B -- Локаторы существуют --> C[d.execute_locator (s.locators ['product']['close_banner'])];
    B -- Локаторы отсутствуют --> D[logger.error];
    C --> E[d.scroll()];
    E --> F[d.execute_locator(l['product_links'])];
    F -- Возвращает список --> G[Обработка результата];
    F -- Возвращает None --> H[logger.warning, Возврат None];
    G --> I[logger.info, вывод кол-ва товаров];
    G --> J[Возврат списка];
    D --> J;

    subgraph Supplier
        s[Supplier Object]
    end

    subgraph WebDriver
        d[Webdriver Object]
    end


    subgraph Locators
        l[Локаторы]
        s.locators['category'] --> l
    end

```

# <explanation>

**Импорты:**

- `from typing import Union`:  Импортирует тип `Union`, который используется для определения возможных возвращаемых типов функций.  Этот импорт  не используется непосредственно, но обеспечивает возможность указывать возможные возвращаемые значения типов (строка, список и т.д.).
- `from pathlib import Path`: Импортирует класс `Path` для работы с путями к файлам. Не используется в данном фрагменте, но важен для работы с файлами в целом.
- `from src import gs`: Импортирует модуль `gs` из пакета `src`.  Непонятно, что он делает, но импорт предполагает использование его функций или данных.
- `from src.logger import logger`: Импортирует логгер `logger` из модуля `logger` в пакете `src`.  Предполагается, что это логгер, который используется для вывода сообщений об ошибках, предупреждениях и информации в ходе выполнения программы.

**Классы:**

- `Supplier`: Объект класса, содержащий данные о поставщике.
- `WebDriver`:  Предполагается, что это класс для работы с веб-драйвером.
- `Product`:  Класс для обработки информации о товаре. Указанный фрагмент кода не содержит информации об этих классах.


**Функции:**

- `get_list_products_in_category(s)`: Получает список ссылок на товары со страницы категории.
    - Принимает на вход объект `Supplier` (`s`).
    - Возвращает список ссылок (`list[str]`) или `None` в случае ошибки.
- `get_list_categories_from_site(s)`:  Не определена в представленном фрагменте кода. Предполагается, что она получает список категорий от поставщика.

**Переменные:**

- `MODE`:  Строковая переменная, вероятно, определяющая режим работы (например, `dev`, `prod`).
- `s`: Объект класса `Supplier` (или подобный).
- `d`: Веб-драйвер (объект).
- `l`: Словарь локаторов для элементов на странице.
- `list_products_in_category`: Список URL адресов товаров.


**Возможные ошибки и улучшения:**

- **Отсутствие проверки типов:** Функция `get_list_products_in_category` не проверяет, что в `s` действительно есть `s.driver` и `s.locators`.  Добавление проверки типов (например, через `isinstance`) повысит надежность.
- **Недостаточная обработка ошибок:**  Если функция `d.execute_locator` возвращает ошибку, это может привести к сбою. Необходимо добавить обработку таких ситуаций.
- **Проверка на наличие страницы:**  В коде нет проверки, загрузилась ли страница, прежде чем пытаться получить локаторы, что потенциально может привести к ошибкам.
- **`get_list_categories_from_site`:** Функция не реализована.
- **`TODO`:** Заметки о `TODO` должны быть реализованы.


**Взаимосвязи с другими частями проекта:**

Функция `get_list_products_in_category` использует объекты `Supplier` (для получения драйвера и локаторов) и `WebDriver` (для взаимодействия с веб-страницей).  Она использует логгер `logger` из модуля `src.logger`.  Функция предполагает наличие  `Product` (для обработки информации о товаре), но в предоставленном фрагменте кода этот класс не определен.