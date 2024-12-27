# Анализ кода модуля `category.md`

**Качество кода**
9
- Плюсы
    -   Документация модуля в формате markdown, что соответствует заданию.
    -   Предоставлено подробное описание основных функций и классов модуля.
    -   Присутствует описание параметров, возвращаемых значений и исключений для каждой функции.
    -   Присутствуют разделы обзора, ключевых функций, функций, классов, зависимостей и примера использования.
    -   Включен раздел лицензирования.
- Минусы
    -   Необходимо переработать документацию в reStructuredText (RST).
    -   Необходимо добавить импорты, которые используются в коде модуля.
    -   Отсутствует логирование ошибок.
    -   Нет примеров кода с использованием  `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**

1.  Переписать документацию в формате reStructuredText (RST) для соответствия требованиям.
2.  Добавить необходимые импорты, такие как `from src.db.manager_categories.suppliers_categories import DBAdaptor`, `from src.utils.jjson import j_loads`,  `from src.logger.logger import logger`, `from typing import Any`, `from src.suppliers.supplier import Supplier`, `requests`,  `json`,  `os`.
3.  Добавить логирование ошибок с использованием `logger.error`.
4.  Использовать `j_loads` или `j_loads_ns` для работы с JSON файлами.
5.  Добавить docstrings в формате RST ко всем функциям, методам и классам.
6.  Избегать избыточного использования try-except, использовать `logger.error` для обработки ошибок.
7.  Добавить комментарии к коду для пояснения его работы.

**Оптимизированный код**
```python
"""
Модуль для управления категориями AliExpress.
===================================================
Этот модуль предоставляет функциональность для управления категориями на AliExpress.
Он позволяет извлекать URL-адреса товаров, обновлять списки категорий и взаимодействовать с
платформой AliExpress для синхронизации категорий.

Модуль содержит различные функции и методы для взаимодействия с категориями товаров на AliExpress,
включая получение URL-адресов товаров, обновление категорий в файлах сценариев и управление данными
категорий в базе данных.

Основные возможности:
- **Извлечение URL-адресов товаров**: Сбор URL-адресов товаров со страниц категорий.
- **Синхронизация категорий**: Сравнение и обновление категорий на сайте с теми, что находятся в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предоставление операций базы данных для управления категориями.

Пример использования:
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file
    from src.suppliers.supplier import Supplier

    # Пример использования
    supplier_instance = Supplier()
    category_urls = get_list_products_in_category(supplier_instance)
    update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
"""
import os
import json
from typing import Any, List
import requests

from src.db.manager_categories.suppliers_categories import DBAdaptor
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger
from src.suppliers.supplier import Supplier


def get_list_products_in_category(s: Supplier) -> List[str]:
    """
    Извлекает список URL-адресов товаров со страницы категории, включая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Supplier
    :return: Список URL-адресов товаров со страницы категории.
    :rtype: List[str]
    """
    try:
        # Код исполняет получение списка URL товаров с пагинации
        urls = _get_prod_urls_from_pagination(s)
        return urls
    except Exception as e:
        logger.error(f'Ошибка при получении списка товаров в категории: {e}')
        return []


def _get_prod_urls_from_pagination(s: Supplier) -> List[str]:
    """
    Извлекает URL-адреса товаров со страниц категории, обрабатывая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Supplier
    :return: Список URL-адресов товаров.
    :rtype: List[str]
    """
    urls = []
    try:
        # Код исполняет получение всех ссылок на товары на странице
        product_elements = s.driver.execute_locator(s.locator.products)
        for element in product_elements:
            try:
                # Код исполняет получение ссылки из элемента
                url = element.get_attribute('href')
                if url:
                    urls.append(url)
            except Exception as e:
                logger.error(f'Ошибка при извлечении URL товара: {e}')
        # Код исполняет поиск кнопки следующей страницы
        next_page_button = s.driver.execute_locator(s.locator.next_page)
        if next_page_button:
            # Код исполняет переход на следующую страницу и рекурсивное получение ссылок
            s.driver.execute_locator(s.locator.next_page, 'click')
            urls.extend(_get_prod_urls_from_pagination(s))
    except Exception as e:
        logger.error(f'Ошибка при получении URL-адресов товаров с пагинации: {e}')
    return urls


def update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool:
    """
    Сравнивает категории на сайте с категориями в предоставленном файле сценария и обновляет файл
    при наличии изменений.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Supplier
    :param scenario_filename: Имя файла сценария, который необходимо обновить.
    :type scenario_filename: str
    :return: True, если категории были успешно обновлены, False в противном случае.
    :rtype: bool
    """
    try:
        # Код исполняет получение списка категорий с сайта
        site_categories = get_list_categories_from_site(s, scenario_filename)
        if not site_categories:
            logger.error(f'Не удалось получить категории с сайта.')
            return False

        # Код исполняет чтение категорий из файла сценария
        if not os.path.exists(scenario_filename):
            logger.error(f'Файл сценария не найден: {scenario_filename}')
            return False
        with open(scenario_filename, 'r', encoding='utf-8') as f:
            try:
                scenario_data = j_loads(f)
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка при чтении файла сценария {scenario_filename}: {e}")
                return False
            scenario_categories = scenario_data.get('categories', [])

        # Код исполняет сравнение категорий сайта и файла
        if site_categories != scenario_categories:
            # Код исполняет обновление категорий в файле сценария
            scenario_data['categories'] = site_categories
            with open(scenario_filename, 'w', encoding='utf-8') as f:
                json.dump(scenario_data, f, indent=4, ensure_ascii=False)
            logger.info(f'Категории в файле {scenario_filename} обновлены.')
        else:
            logger.info(f'Категории в файле {scenario_filename} не требуют обновления.')
        return True
    except Exception as e:
        logger.error(f'Ошибка при обновлении категорий в файле сценария: {e}')
        return False


def get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> List[str]:
    """
    Извлекает список категорий с сайта AliExpress на основе предоставленного файла сценария.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Supplier
    :param scenario_file: Файл сценария, содержащий информацию о категориях.
    :type scenario_file: str
    :param brand: Фильтр бренда для категорий.
    :type brand: str
    :return: Список категорий с сайта.
    :rtype: List[str]
    """
    try:
        # Код исполняет чтение файла сценария
        if not os.path.exists(scenario_file):
            logger.error(f'Файл сценария не найден: {scenario_file}')
            return []
        with open(scenario_file, 'r', encoding='utf-8') as f:
            try:
                scenario_data = j_loads(f)
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка при чтении файла сценария {scenario_file}: {e}")
                return []
            start_urls = scenario_data.get('start_urls', [])

        categories = []
        for url_data in start_urls:
            try:
                # Код исполняет формирование URL с учетом бренда
                if brand:
                    url = url_data.get('url', '').format(brand=brand)
                else:
                    url = url_data.get('url', '')
                if not url:
                    logger.warning(f'Пустой URL для категории в {url_data=}')
                    continue
                # Код исполняет запрос к странице категории
                response = requests.get(url)
                response.raise_for_status()
                # Код исполняет загрузку и анализ HTML-кода страницы
                s.driver.get(url)
                category_elements = s.driver.execute_locator(s.locator.category_item)
                if not category_elements:
                    logger.warning(f'Нет элементов категорий по локатору {s.locator.category_item}')
                    continue
                for element in category_elements:
                    try:
                         # Код исполняет получение текста категории и добавление в список
                        category_name = element.text
                        if category_name:
                            categories.append(category_name)
                    except Exception as e:
                        logger.error(f'Ошибка при извлечении категории: {e}')
            except Exception as e:
                logger.error(f'Ошибка при обработке URL: {url_data=}, {e}')
        return categories
    except Exception as e:
        logger.error(f'Ошибка при получении списка категорий с сайта: {e}')
        return []


class DBAdaptor:
    """
    Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные
    операции, такие как SELECT, INSERT, UPDATE и DELETE с записями AliexpressCategory.
    """
    def __init__(self, table_name: str = "AliexpressCategory"):
        """
        Инициализирует адаптер базы данных для таблицы `AliexpressCategory`.

        :param table_name: Имя таблицы, с которой будет работать адаптер.
        :type table_name: str
        """
        self.table_name = table_name
        self.db = DBAdaptor() # TODO :  возможно, тут не правильная логика
        
    def select(self, where: str = None, **kwargs: Any) -> list[dict]:
        """
        Извлекает записи из таблицы `AliexpressCategory`.

        :param where: Условие WHERE для запроса.
        :type where: str
        :param kwargs: Дополнительные параметры для запроса.
        :type kwargs: Any
        :return: Список записей, соответствующих условию.
        :rtype: list[dict]
        """
        # Код исполняет запрос на выборку данных из базы данных
        return self.db.select(self.table_name, where, **kwargs)

    def insert(self, values: dict) -> None:
        """
        Вставляет новую запись в таблицу `AliexpressCategory`.

        :param values: Словарь значений для вставки.
        :type values: dict
        """
        # Код исполняет вставку данных в базу данных
        self.db.insert(self.table_name, values)

    def update(self, where: str, values: dict) -> None:
         """
        Обновляет существующую запись в таблице `AliexpressCategory`.

        :param where: Условие WHERE для обновления записи.
        :type where: str
        :param values: Словарь новых значений для обновления.
        :type values: dict
        """
        # Код исполняет обновление данных в базе данных
        self.db.update(self.table_name, where, values)

    def delete(self, where: str) -> None:
        """
        Удаляет запись из таблицы `AliexpressCategory`.

        :param where: Условие WHERE для удаления записи.
        :type where: str
        """
        # Код исполняет удаление данных из базы данных
        self.db.delete(self.table_name, where)
```