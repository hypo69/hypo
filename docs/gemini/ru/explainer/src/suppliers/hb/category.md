# <input code>

```python
## \file hypotez/src/suppliers/hb/category.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.hb 
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

""" module: src.suppliers.hb """


"""  Модуль сбора товаров со страницы категорий поставщика hb.co.il через вебдрайвер
У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категории `PrestaShop.categories <-> aliexpress.shop.categoies`
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

**Алгоритм `get_list_products_in_category`:**

1. **Получение драйвера и локаторов:** Извлекает веб-драйвер и локаторы из объекта `Supplier` (`s`).
2. **Ожидание и взаимодействие с сайтом:** Выполняет ожидание (`.wait(1)`) и действия, связанные с закрытием баннеров и прокруткой страницы (`.execute_locator`, `.scroll`).
3. **Получение списка ссылок на товары:** Используя локатор, получает список ссылок на товары с текущей страницы (`d.execute_locator(l['product_links'])`).
4. **Обработка пустого списка:** Если список пуст, выводит предупреждение и возвращает `None`.
5. **Обработка пагинации:** В цикле `while` проверяет, изменился ли текущий URL страницы по сравнению с предыдущим. Если URL изменился,  использует функцию `paginator` для получения следующей страницы и добавления ссылок в список.
6. **Преобразование результата:**  Проверяет тип результата, если это строка, то возвращает список, содержащий эту строку, иначе возвращает полученный список.
7. **Логирование:**  Выводит информацию о количестве найденных товаров в текущей категории.
8. **Возврат списка:** Возвращает список ссылок на товары.

**Алгоритм `paginator`:**

1. **Получение ответа:** Выполняет действие по нажатию на кнопку перехода на следующую страницу используя локатор (`locator['pagination']['<-']`).
2. **Проверка результата:** Проверяет, получен ли ответ и не пустой ли он. Если результат пустой, возвращает `None`.
3. **Возврат истинного значения:** Если все проверки пройдены, возвращает `True`.

**Пример перемещения данных:**
Функция `get_list_products_in_category` получает объект `Supplier`, содержащий веб-драйвер и локаторы.  Она использует веб-драйвер для получения списка ссылок на товары, а затем передает этот список в функции `paginator`.
Функция `paginator` проверяет и обрабатывает данные для навигации по страницам товаров и возвращает `True` или `False` для продолжения цикла.



# <mermaid>

```mermaid
graph TD
    A[get_list_products_in_category(Supplier)] --> B{Получение драйвера и локаторов};
    B --> C[Ожидание и взаимодействие с сайтом];
    C --> D{Получение списка ссылок на товары};
    D --Список не пуст --> E[Обработка пагинации];
    D --Список пуст --> F[Логирование и возврат None];
    E --> G{Изменился URL?};
    G --Да--> H[paginator(Driver, locator, list)];
    G --Нет--> I[Логирование и возврат списка];
    H --> J{Результат пуст?};
    J --Да--> K[Возврат None];
    J --Нет--> L[Добавление ссылок и возврат True];
    I --> M[Формирование списка, логирование];
    M --> N[Возврат списка];

    subgraph Функция paginator
        O[paginator(Driver, locator, list)] --> P{Получение ответа};
        P --> Q{Проверка результата};
        Q --Результат не пуст --> R[Возврат True];
        Q --Результат пуст --> S[Возврат None];
    end
```


# <explanation>

**Импорты:**

- `from typing import Dict, List`: Импортирует типы данных `Dict` и `List` для аннотаций типов в функциях.
- `from pathlib import Path`:  Импортирует класс `Path` для работы с путями к файлам (хотя в данном коде он не используется).
- `from src import gs`: Импортирует модуль `gs` из пакета `src`.  Предполагается, что `gs` содержит какие-то вспомогательные функции или данные. Непонятно, что именно делает этот модуль без дополнительной информации.
- `from src.logger import logger`: Импортирует объект логгера `logger` из модуля `logger` в пакете `src`.  Объект `logger` используется для вывода сообщений об ошибках, предупреждениях и информации. Это стандартный подход для ведения журналов операций.
- `from src.webdriver.driver import Driver`: Импортирует класс `Driver` из модуля `driver` пакета `src.webdriver`.  Предполагается, что `Driver` отвечает за взаимодействие с веб-драйвером (например, Selenium).
- `from src.suppliers import Supplier`: Импортирует класс `Supplier` из модуля `suppliers` пакета `src`. Этот класс, вероятно, представляет поставщика, предоставляя доступ к драйверу, локаторам и другим данным, необходимым для работы с конкретным поставщиком (в данном случае hb.co.il).

**Классы:**

- Никаких явных классов, кроме возможного импорта `Supplier` из `src.suppliers`, не видно в этом файле.


**Функции:**

- `get_list_products_in_category(s: Supplier) -> list[str, str, None]`: Получает список ссылок на товары со страницы категории поставщика.  Функция принимает объект `Supplier`, содержит логику получения списка, обработки пагинации, и возвращает список ссылок или `None`.  Важно, что она возвращает список строк — ссылок на страницы товаров.
- `paginator(d:Driver, locator: dict, list_products_in_category: list)`: Функция для обработки пагинации, перемещаясь к следующей странице, если она существует.  Она обрабатывает локаторы для навигации и возвращает `True`, если удалось перейти на следующую страницу или `False`, если это не удалось.
- `get_list_categories_from_site(s)`:  Функция для сбора списка категорий с сайта.  Пока не показан ее код, но предполагается, что она получает список категорий из веб-страницы и обрабатывает его.


**Переменные:**

- `MODE`: Строковая переменная, которая определяет режим работы (вероятно, для разработки или производства).
- `list_products_in_category`: Список ссылок на страницы товаров.
- `d`: Объект `Driver`, представляющий веб-драйвер для работы со страницей.
- `l`: Словарь, содержащий локаторы элементов веб-страницы для работы с категориями и товарами.
- `s`: Объект `Supplier`, содержащий информацию о поставщике и его свойства.

**Возможные ошибки и улучшения:**

- Отсутствует обработка исключений. Если веб-драйвер не может найти элементы или произойдет какая-то ошибка в процессе работы, необходимо добавить обработку исключений, чтобы предотвратить сбой программы.
- Непонятно, что содержит `s.locators['category']` и `s.locators['product']`.  Необходимо описать структуру данных в `s.locators`.
- `d.execute_locator` используется для получения различных типов данных. Необходимо более тщательно определять типы данных, которые ожидаются.
- `logger.warning('Нет ссылок на товары. Так бывает')` — следует добавить причину, почему не было найдено ссылок на товары (например, ошибка в локаторах, временная ошибка на сайте, или другие).


**Взаимосвязи с другими частями проекта:**

Функции в файле `category.py` взаимодействуют с классом `Supplier` из `src.suppliers`, классом `Driver` из `src.webdriver.driver`, и модулем `logger` из `src.logger`.  Они также, вероятно, используются модулями, которые обрабатывают конкретные товары (`Product`) или данные о категориях.  Функции `grab_product_page()` и класс `Product` используются для сбора и обработки информации о каждом товаре.