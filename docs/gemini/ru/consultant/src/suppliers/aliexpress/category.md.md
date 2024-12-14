# Анализ кода модуля `category.md`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и документирован в формате Markdown.
    - Описание функций, классов и их параметров довольно подробное.
    - Есть примеры использования и указания на зависимости.
    -  Присутствует описание лицензии.
- Минусы
    - Документация написана в формате Markdown, а не reStructuredText (RST) как требуется.
    - Нет примеров кода в формате RST.
    - Не указаны импорты используемых модулей и классов, которые необходимы для работы кода.

**Рекомендации по улучшению**
1.  **Переформатировать документацию в reStructuredText (RST)**: Заменить Markdown на RST для всех комментариев и docstring.
2.  **Добавить импорты**: Указать необходимые импорты для работы модуля.
3.  **Использовать docstring**: Добавить docstring в формате RST к функциям, классам и методам.
4.  **Логирование ошибок**: Использовать `logger.error` для обработки ошибок, вместо `try-except`.
5.  **Улучшить описание параметров**: Добавить более детальное описание параметров функций и методов.

**Оптимизированный код**

```python
"""
Модуль для управления категориями AliExpress
=========================================================================================

Этот модуль предоставляет функциональность для управления категориями на AliExpress.
Он включает извлечение URL продуктов, обновление списков категорий и взаимодействие
с платформой AliExpress для синхронизации категорий.

Основные возможности:
---------------------

- **Извлечение URL продуктов**: Сбор URL продуктов со страниц категорий.
- **Синхронизация категорий**: Сравнение и обновление категорий на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Операции с базой данных для управления категориями.

Зависимости:
------------
    - `src.db.manager_categories.suppliers_categories`: Для управления категориями в базе данных.
    - `src.utils.jjson`: Для работы с данными JSON.
    - `src.logger`: Для логирования ошибок и сообщений.
    - `requests`: Для выполнения HTTP-запросов к сайту AliExpress.

Пример использования:
---------------------
.. code-block:: python

    from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

    # Пример использования
    supplier_instance = Supplier()
    category_urls = get_list_products_in_category(supplier_instance)
    update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')

"""
from typing import Any, List
from src.db.manager_categories.suppliers_categories import AliexpressCategory  # Добавлен импорт класса AliexpressCategory
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger
# from src.suppliers.supplier import Supplier # TODO  может не использоваться
import requests

def get_list_products_in_category(s: Any) -> list[str]:
    """
    Извлекает список URL продуктов со страницы категории, включая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :return: Список URL продуктов со страницы категории.
    :rtype: list[str]
    """
    prod_urls = []
    try:
        #  код исполняет получение списка URL из пагинации
        prod_urls = get_prod_urls_from_pagination(s)
    except Exception as ex:
        logger.error(f'Ошибка получения списка продуктов из категории {ex}')
    return prod_urls


def get_prod_urls_from_pagination(s: Any) -> list[str]:
    """
    Извлекает URL продуктов со страниц категорий, обрабатывая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :return: Список URL продуктов.
    :rtype: list[str]
    """
    urls = []
    try:
        # код исполняет проверку наличия локатора пагинации
        if not s.locator.pagination:
            # код исполняет получение списка продуктов
            return get_list_products(s)

        # код исполняет получение количества страниц
        count_page = s.driver.get_count_elements(s.locator.pagination)
        # код исполняет итерирование по страницам
        for page in range(1, count_page + 1):
            # код исполняет получение продуктов на текущей странице
            urls.extend(get_list_products(s, page))
            # код исполняет переход на следующую страницу
            s.driver.execute_locator(s.locator.next_page)
    except Exception as ex:
         logger.error(f'Ошибка получения списка продуктов с пагинацией {ex}')
    return urls

def get_list_products(s: Any, page: int = None) -> list[str]:
    """
    Извлекает список URL продуктов с текущей страницы.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param page: Номер страницы (необязательно).
    :type page: int, optional
    :return: Список URL продуктов.
    :rtype: list[str]
    """
    urls = []
    try:
        #  код исполняет получение списка элементов по локатору продуктов
        elements = s.driver.get_elements(s.locator.product)
        #  код исполняет итерацию по элементам и извлечение ссылок
        for el in elements:
             urls.append(el.get_attribute('href'))
    except Exception as ex:
        logger.error(f'Ошибка получения списка продуктов {ex}')
    return urls

def update_categories_in_scenario_file(s: Any, scenario_filename: str) -> bool:
    """
    Сравнивает категории на сайте с категориями в файле сценария и обновляет файл
    изменениями.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param scenario_filename: Имя файла сценария для обновления.
    :type scenario_filename: str
    :return: True, если категории успешно обновлены, иначе False.
    :rtype: bool
    """
    try:
        # код исполняет загрузку данных из файла сценария
        scenario_data = j_loads(scenario_filename)
        # код исполняет получение списка категорий с сайта
        site_categories = get_list_categories_from_site(s, scenario_filename)

        if not site_categories:
            logger.error(f'Не удалось получить категории с сайта')
            return False

        # код исполняет обновление списка категорий в файле сценария
        for category in site_categories:
            for item in scenario_data['categories']:
                 if item['name'] == category['name']:
                    item['url'] = category['url']
                    break

        # код исполняет запись обновлённых данных в файл сценария
        with open(scenario_filename, 'w', encoding='utf-8') as file:
            import json # TODO использовать src.utils.jjson.j_dumps для сохранения
            json.dump(scenario_data, file, indent=4, ensure_ascii=False)

        return True
    except Exception as ex:
        logger.error(f'Ошибка обновления категорий в файле сценария {ex}')
        return False

def get_list_categories_from_site(s: Any, scenario_file: str, brand: str = '') -> list:
    """
    Извлекает список категорий с сайта AliExpress, основываясь на файле сценария.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param scenario_file: Файл сценария, содержащий информацию о категориях.
    :type scenario_file: str
    :param brand: Фильтр бренда для категорий (необязательно).
    :type brand: str, optional
    :return: Список категорий с сайта.
    :rtype: list
    """
    categories = []
    try:
        # код исполняет загрузку данных из файла сценария
        scenario_data = j_loads(scenario_file)
        # код исполняет итерацию по категориям в файле сценария
        for category in scenario_data.get('categories', []):
            # код исполняет открытие страницы категории
            s.driver.get_page(category['url'])
             # код исполняет ожидание загрузки контента
            s.driver.wait_for_element(s.locator.category_card)
             # код исполняет добавление категории в список
            categories.append({
                'name': category['name'],
                'url': s.driver.current_url,
            })
    except Exception as ex:
        logger.error(f'Ошибка получения списка категорий с сайта {ex}')
    return categories


class DBAdaptor:
    """
    Предоставляет методы для взаимодействия с базой данных,
    позволяя выполнять стандартные операции `SELECT`, `INSERT`, `UPDATE` и `DELETE`
    с записями `AliexpressCategory`.
    """
    def select(self, where: str = None, limit: int = None) -> List[AliexpressCategory]:
        """
        Извлекает записи из таблицы `AliexpressCategory`.

        :param where: Условие `WHERE` для запроса (необязательно).
        :type where: str, optional
        :param limit: Ограничение количества возвращаемых записей (необязательно).
        :type limit: int, optional
        :return: Список записей `AliexpressCategory`.
        :rtype: List[AliexpressCategory]
        """
        try:
            # код исполняет формирование запроса к БД
            query = f'SELECT * FROM aliexpress_category'
            if where:
                query += f' WHERE {where}'
            if limit:
                query += f' LIMIT {limit}'
            # код исполняет выполнение запроса к БД
            result = AliexpressCategory.raw(query)
            return result
        except Exception as ex:
            logger.error(f'Ошибка запроса SELECT к БД {ex}')
            return []

    def insert(self, data: dict) -> bool:
        """
        Вставляет новую запись в таблицу `AliexpressCategory`.

        :param data: Данные для вставки.
        :type data: dict
        :return: `True`, если запись успешно вставлена, `False` в противном случае.
        :rtype: bool
        """
        try:
            # код исполняет создание записи в БД
            AliexpressCategory.create(**data)
            return True
        except Exception as ex:
            logger.error(f'Ошибка запроса INSERT в БД {ex}')
            return False

    def update(self, data: dict, where: str) -> bool:
        """
        Обновляет существующую запись в таблице `AliexpressCategory`.

        :param data: Данные для обновления.
        :type data: dict
        :param where: Условие `WHERE` для обновления.
        :type where: str
        :return: `True`, если запись успешно обновлена, `False` в противном случае.
        :rtype: bool
        """
        try:
             # код исполняет обновление записи в БД
            AliexpressCategory.update(**data).where(where).execute()
            return True
        except Exception as ex:
            logger.error(f'Ошибка запроса UPDATE в БД {ex}')
            return False

    def delete(self, where: str) -> bool:
        """
        Удаляет запись из таблицы `AliexpressCategory`.

        :param where: Условие `WHERE` для удаления.
        :type where: str
        :return: `True`, если запись успешно удалена, `False` в противном случае.
        :rtype: bool
        """
        try:
             # код исполняет удаление записи из БД
            AliexpressCategory.delete().where(where).execute()
            return True
        except Exception as ex:
            logger.error(f'Ошибка запроса DELETE в БД {ex}')
            return False
```