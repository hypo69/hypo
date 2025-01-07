# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/category.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress 
	:platform: Windows, Unix
	:synopsis:  управление категориями aliexpress

"""


from typing import Union
from pathlib import Path

from src import gs
from src.utils.jjson import j_dumps, j_loads
from src.logger import logger

# Импорт класса CategoryManager и модели AliexpressCategory
# Зачем?  CategoryManager занимается переводами
from src.db.manager_categories.suppliers_categories import CategoryManager, AliexpressCategory

credentials = gs.db_translations_credentials
# Создание экземпляра класса CategoryManager
manager = CategoryManager()


def get_list_products_in_category(s) -> list[str, str]:
    """  
     Считывает URL товаров со страницы категории.

    @details Если есть несколько страниц с товарами в одной категории - листает все.
    Важно понимать, что к этому моменту вебдрайвер уже открыл страницу категорий.

    @param s `Supplier` - экземпляр поставщика
    @param run_async `bool` - устанавливает синхронность/асинхронность исполнения функции `async_get_list_products_in_category()`

    @returns list_products_in_category `list` - список собранных URL. Может быть пустым, если в исследуемой категории нет товаров.
    """
    
    return get_prod_urls_from_pagination (s)
        

def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    @param s `Supplier` 
    @returns list_products_in_category `list` :  Список ссылок, собранных со страницы категории"""
    
    _d = s.driver
    _l: dict = s.locators['category']['product_links']
    
    list_products_in_category: list = _d.execute_locator(_l)
    
    if not list_products_in_category:
        """ В категории нет товаров. Это нормально """
        return []

    while True:
        """ @todo Опасная ситуация здесь/ Могу уйти в бесконечный цикл """
        if not _d.execute_locator (s.locators ['category']['pagination']['->'] ):
            """  _rem Если больше некуда нажимать - выходим из цикла """
            break
        list_products_in_category.extend(_d.execute_locator(_l ))
   
    return list_products_in_category if isinstance(list_products_in_category, list) else [list_products_in_category]


# Сверяю файл сценария и текущее состояние списка категорий на сайте 
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте 
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен !!!! """
    
    scenario_json = j_loads(Path(gs.dir_scenarios, f'{scenario_filename}'))
    scenarios_in_file = scenario_json['scenarios']
    categoris_on_site = get_list_categories_from_site()

    all_ids_in_file:list=[]
    def _update_all_ids_in_file():
        for _category in scenario_json['scenarios'].items():
            if _category[1]['category ID on site'] > 0:
                all_ids_in_file.append(_category[1]['category ID on site'])
            else:
                url = _category[1]['url']
                cat = url[url.rfind('/')+1:url.rfind('.html'):].split('_')[1]
                _category[1]['category ID on site']:int = int(cat)
                all_ids_in_file.append(cat)
        #json_dump(scenario_json,Path(gs.dir_scenarios, f'{scenario_filename}'))

    _update_all_ids_in_file()
    # ... (остальной код функции)
```

# <algorithm>

**Алгоритм работы функции `update_categories_in_scenario_file`:**

1. **Чтение файла сценария:** Функция загружает JSON-данные из файла сценария.
2. **Получение категорий с сайта:** Вызывается функция `get_list_categories_from_site()`, которая, скорее всего, получает список категорий с сайта в формате JSON.
3. **Получение идентификаторов категорий из файла:** Извлекает список идентификаторов категорий из загруженного файла сценария. Обрабатывает случаи, где идентификатор отсутствует.
4. **Получение идентификаторов категорий с сайта:** Получает список идентификаторов категорий с сайта.
5. **Сравнение списков:** Сравнивает списки идентификаторов, находящиеся в файле и полученные с сайта, и выявляет добавленные и удаленные категории.
6. **Обновление файла сценария:**
    * Добавляет новые категории в файл сценария, если они найдены на сайте.
    * Отключает (меняет активность) те категории, которых нет на сайте.
7. **Сохранение изменений:** Сохраняет обновлённый файл сценария.
8. **Отправка уведомлений:** Отправляет уведомления о добавлении/удалении категорий.

**Пример:**

Если на сайте появились новые категории, функция `update_categories_in_scenario_file` найдёт их, добавит их в файл сценария и отправит уведомление. Если с сайта исчезли некоторые категории, функция обнаружит их отсутствие, пометит эти категории в файле сценария как неактивные и также отправит уведомление.


# <mermaid>

```mermaid
graph TD
    A[update_categories_in_scenario_file] --> B{Чтение файла сценария};
    B --> C[Получение категорий с сайта];
    C --> D{Получение идентификаторов категорий из файла};
    D --> E[Получение идентификаторов категорий с сайта];
    E --> F{Сравнение списков};
    F -- Добавлено -> G[Обновление файла сценария (Добавление)];
    F -- Удалено -> H[Обновление файла сценария (Удаление)];
    G --> I[Сохранение изменений];
    H --> I;
    I --> J[Отправка уведомлений];
```


# <explanation>

**Импорты:**

* `from typing import Union`: используется для указания типов переменных.
* `from pathlib import Path`: используется для работы с путями к файлам.
* `from src import gs`: импортирует модуль `gs`, скорее всего, содержащий глобальные константы или настройки.
* `from src.utils.jjson import j_dumps, j_loads`: импортирует функции для работы с JSON (сериализация/десериализация).
* `from src.logger import logger`: импортирует объект `logger` для записи сообщений об ошибках или других событий.
* `from src.db.manager_categories.suppliers_categories import CategoryManager, AliexpressCategory`: импортирует классы `CategoryManager` и `AliexpressCategory`, необходимые для работы с базой данных.  Это говорит о том, что код интегрирован в систему управления категориями и базами данных.

**Классы:**

* `CategoryManager`: класс для работы с категориями в базе данных. Методы `select_record`, `insert_record`, `update_record`, `delete_record`  свидетельствуют о его возможностях для взаимодействия с БД.
* `AliexpressCategory`: Модель данных для категорий Aliexpress.
* `DBAdaptor`: Класс предоставляет интерфейс для работы с базой данных (select, insert, update, delete). Этот класс необходим для абстрагирования доступа к базе данных, а не для непосредственной работы с ней.

**Функции:**

* `get_list_products_in_category`: Функция для получения списка URL товаров в категории. Принимает на вход экземпляр поставщика и флаг асинхронности. Возвращает список URL или пустой список, если товаров нет.
* `get_prod_urls_from_pagination`: Функция для получения ссылок на товары со страницы, включая перелистывание страниц.
* `update_categories_in_scenario_file`: Функция для обновления файла сценария. Сравнивает категории из файла сценария с категориями на сайте, добавляет и удаляет их.  Важно: функция не проверяется (`@todo не проверен !!!!`).


**Переменные:**

* `MODE`:  Глобальная переменная, определяющая режим работы (например, `dev` или `prod`).
* `credentials`:  Переменная для хранения данных аутентификации, вероятно, для доступа к базе данных.
* `manager`: Экземпляр класса `CategoryManager`, используемый для взаимодействия с базой данных.
* `scenario_filename`: Имя файла сценария.
* `scenario_json`: Загруженные данные из файла сценария.

**Возможные ошибки и улучшения:**

* **Непроверенная функция `update_categories_in_scenario_file`:** Функция содержит `@todo` и не проверяется.  Необходимо проверить правильность работы сравнения категорий, обновление файла сценария и обработки ошибок.
* **Возможные ошибки в get_list_categories_from_site():** Необходимо проверить работу этой функции.  Проблема с отсутствием аргумента `s` в функции.


**Цепочка взаимосвязей:**

Код взаимодействует с модулем `gs`, `utils.jjson`, `logger`,  `db.manager_categories`.  Вероятно,  он интегрирован в систему сбора данных, использующую веб-драйвер (`s.driver`).  Функции `get_list_products_in_category` и `update_categories_in_scenario_file`  обращаются к внешним ресурсам (веб-сайт и база данных).