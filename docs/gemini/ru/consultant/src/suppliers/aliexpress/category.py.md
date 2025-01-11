# Анализ кода модуля `category.py`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для функций.
    - Используется `logger` для логирования ошибок.
    - Код структурирован и разделен на функции.
-  Минусы
    -  Не везде используется `j_loads` и `j_dumps`.
    -  Есть потенциально опасные места с бесконечными циклами.
    -  Не все функции имеют полные docstring.
    -  Смешаны одинарные и двойные кавычки.
    -  Сложная логика сравнения категорий.
    -  Отсутствует обработка ошибок в некоторых местах.
    -  Используются магические значения для ключей.
**Рекомендации по улучшению**

1.  **Форматирование и кавычки**:
    -   Использовать одинарные кавычки для строк в коде, двойные кавычки только для вывода.
2.  **Импорты**:
    -   Добавить недостающие импорты.
    -   Убедиться, что все импорты соответствуют стилю проекта.
3.  **JSON**:
    -   Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для работы с JSON.
4.  **Логирование**:
    -   Улучшить логирование ошибок, добавив больше контекста.
    -   Избегать использования `try-except` там, где достаточно `logger.error`.
5.  **Бесконечные циклы**:
    -   Добавить проверку на максимальное количество итераций в циклах `while True`.
6.  **Документация**:
    -   Добавить более подробные docstring для всех функций и методов, включая описание параметров и возвращаемых значений.
    -   Использовать RST формат для docstring.
7. **Обновление категорий:**
    -  Упростить логику сравнения категорий на сайте и в файле.
    -  Использовать более понятные переменные.
8. **DBAdaptor**:
    -  Реализовать полноценные методы `DBAdaptor` с корректными параметрами.
9.  **Обработка ошибок**:
    -   Добавить обработку ошибок для всех операций, которые могут вызвать исключения.
10. **Магические значения**:
    -   Использовать константы для магических значений.
11. **Комментарии**:
     -  Дополнить комментарии в коде для лучшего понимания.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с категориями Aliexpress.
===========================================

Этот модуль содержит функции для извлечения списка товаров из категорий Aliexpress,
обновления категорий в файлах сценариев, а также для взаимодействия с базой данных.

Пример использования:
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

    # Пример использования функций
    # ...
"""
from typing import Union, Any
from pathlib import Path
import requests
from src import gs
from src.utils.jjson import j_dumps, j_loads
from src.logger.logger import logger
from src.db.manager_categories.suppliers_categories import CategoryManager, AliexpressCategory
from src.notifier.send import send


credentials = gs.db_translations_credentials
manager = CategoryManager()

def get_list_products_in_category(s) -> list[str]:
    """
    Извлекает URL товаров со страницы категории.

    Функция переходит по всем страницам категории, если таковые имеются.

    Args:
        s: Экземпляр поставщика (Supplier).

    Returns:
        Список URL товаров. Может быть пустым, если в категории нет товаров.
    """
    return get_prod_urls_from_pagination(s)


def get_prod_urls_from_pagination(s) -> list[str]:
    """
    Собирает URL товаров со страниц категории с пагинацией.

    Args:
        s: Экземпляр поставщика (Supplier).

    Returns:
        Список URL товаров.
    """
    _driver = s.driver
    _locator: dict = s.locators['category']['product_links']

    list_products_in_category: list = _driver.execute_locator(_locator)
    if not list_products_in_category:
        # Если в категории нет товаров, возвращаем пустой список.
        return []

    max_iterations = 100  # Максимальное количество итераций, чтобы избежать бесконечного цикла.
    iteration = 0
    while True:
        # Проверка, есть ли следующая страница пагинации.
        next_page_locator = s.locators['category']['pagination']['->']
        if not _driver.execute_locator(next_page_locator):
            # Если больше нет страниц, выходим из цикла.
            break

        # Добавляем URL товаров со следующей страницы.
        list_products_in_category.extend(_driver.execute_locator(_locator))

        iteration += 1
        if iteration > max_iterations:
            logger.error('Достигнуто максимальное количество итераций при сборе товаров с категории, возможно, бесконечный цикл')
            break

    return list_products_in_category if isinstance(list_products_in_category, list) else [list_products_in_category]


def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """
    Обновляет категории в файле сценария, сравнивая их с категориями на сайте.

    Args:
        s: Экземпляр поставщика (Supplier).
        scenario_filename: Имя файла сценария.

    Returns:
        `True`, если обновление прошло успешно.
    """
    try:
        scenario_path = Path(gs.dir_scenarios, scenario_filename)
        scenario_json = j_loads(scenario_path)
        scenarios_in_file = scenario_json['scenarios']
        # Извлечение списка категорий с сайта
        categories_from_site = get_list_categories_from_site(s,scenario_filename)

        all_ids_in_file: list = []
        def _update_all_ids_in_file():
             """
             Обновляет список всех ID категорий из файла сценария.
             """
             for _category in scenario_json['scenarios'].items():
                 if _category[1].get('category ID on site', 0) > 0:
                     # Если ID категории определен в файле - добавляем его в список.
                     all_ids_in_file.append(_category[1]['category ID on site'])
                 else:
                    #  Если ID категории не определен в файле, извлекаем его из URL.
                    url = _category[1]['url']
                    cat = url[url.rfind('/') + 1:url.rfind('.html')].split('_')[1]
                    _category[1]['category ID on site'] = int(cat)
                    all_ids_in_file.append(cat)

        _update_all_ids_in_file()

        shop_categories_json_url = scenario_json['store']['shop categories json file']
        try:
            response = requests.get(shop_categories_json_url)
            response.raise_for_status() #  Проверка на статус код 200
            categories_from_aliexpress_shop_json = response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'Ошибка чтения JSON файла: {shop_categories_json_url}. Ошибка: {e}')
            return False

        groups = categories_from_aliexpress_shop_json['groups']
        all_ids_on_site: list = []
        all_categories_on_site: list = []
        for group in groups:
            if not group['subGroupList']:
                all_ids_on_site.append(str(group['groupId']))
                all_categories_on_site.append(group)
            else:
                for subgroup in group['subGroupList']:
                    all_ids_on_site.append(str(subgroup['groupId']))
                    all_categories_on_site.append(subgroup)

        removed_categories = [str(x) for x in all_ids_in_file if str(x) not in set(all_ids_on_site)]
        added_categories = [x for x in all_ids_on_site if x not in set(map(str,all_ids_in_file))]
        
        categories_in_file = scenario_json['scenarios']

        if added_categories:
            for category_id in added_categories:
                category = [c for c in all_categories_on_site if str(c['groupId']) == category_id]
                if not category:
                    logger.error(f'Не найдена категория с ID {category_id} на сайте')
                    continue
                category_name = category[0]['name']
                category_url = category[0]['url']
                categories_in_file.update({category_name: {
                    'category ID on site': int(category_id),
                    'brand': '',
                    'active': True,
                    'url': category_url,
                    'condition': '',
                    'PrestaShop_categories': ''
                }})
            scenario_json['scenarios'] = categories_in_file
            j_dumps(scenario_json, scenario_path)
            post_subject = f'Добавлены новые категории в файл {scenario_filename}'
            post_message = f'\nВ файл {scenario_filename} были добавлены новые категории:\n{added_categories}\n'
            send(post_subject, post_message)

        if removed_categories:
            for category_id in removed_categories:
               # category = [v for k, v in categories_in_file.items() if str(v.get('category ID on site')) == category_id]
                category = [v for k, v in categories_in_file.items() if str(v.get('category ID on site')) == str(category_id)]
                if not category:
                    logger.warning(f'Категория c ID {category_id} не найдена в файле {scenario_filename}')
                    continue
                category[0]['active'] = False

            scenario_json['scenarios'] = categories_in_file
            j_dumps(scenario_json, scenario_path)
            post_subject = f'Отключены категории в файле {scenario_filename}'
            post_message = f'\nВ файл {scenario_filename} были отключены категории:\n{removed_categories}\n'
            send(post_subject, post_message)

        return True
    except Exception as ex:
        logger.error(f'Ошибка при обновлении категорий в файле {scenario_filename}: {ex}')
        return False

def get_list_categories_from_site(s,scenario_file,brand=''):
    """
    Получает список категорий с сайта.

    Args:
        s: Экземпляр поставщика (Supplier).
        scenario_file: Имя файла сценария.
        brand: Бренд.

    Returns:
        Список категорий с сайта.
    """
    _driver = s.driver
    scenario_json = j_loads(Path(gs.dir_scenarios, scenario_file))
    _driver.get_url(scenario_json['store']['shop categories page'])
    ...


class DBAdaptor:
    """
    Адаптер для взаимодействия с базой данных категорий Aliexpress.
    """
    @staticmethod
    def select(cat_id: int = None, parent_id: int = None, project_cat_id: int = None) -> list[AliexpressCategory]:
         """
         Получает записи из таблицы AliexpressCategory по заданным параметрам.

         Args:
            cat_id: ID категории.
            parent_id: ID родительской категории.
            project_cat_id: ID категории проекта.

         Returns:
            Список записей из БД.
         """
         query_params = {}
         if parent_id:
            query_params['parent_category_id'] = parent_id
         if cat_id:
             query_params['category_id'] = cat_id
         if project_cat_id:
             query_params['hypotez_category_id'] = project_cat_id
         # Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен `parent_id`
         records = manager.select_record(AliexpressCategory, **query_params)
         return records
    @staticmethod
    def insert(fields: dict) -> None:
        """
        Вставляет новую запись в таблицу AliexpressCategory.

        Args:
            fields: Словарь с данными для вставки.
        """
        try:
           manager.insert_record(AliexpressCategory, fields)
        except Exception as ex:
             logger.error(f'Ошибка при вставке записи в базу данных: {ex}')
    @staticmethod
    def update(hypotez_id_value: Any, **kwargs) -> None:
        """
        Обновляет запись в таблице AliexpressCategory.

        Args:
            hypotez_id_value: ID для обновления.
            kwargs: Параметры для обновления.
        """
        try:
           manager.update_record(AliexpressCategory, hypotez_id_value, **kwargs)
        except Exception as ex:
             logger.error(f'Ошибка при обновлении записи в базе данных: {ex}')

    @staticmethod
    def delete(hypotez_id_value: Any) -> None:
        """
         Удаляет запись из таблицы AliexpressCategory.

        Args:
             hypotez_id_value: ID для удаления.
        """
        try:
            manager.delete_record(AliexpressCategory, hypotez_id_value)
        except Exception as ex:
            logger.error(f'Ошибка при удалении записи из базы данных: {ex}')