# Улучшенный код

```python
"""
Модуль для управления категориями AliExpress.
=========================================================================================

Этот модуль предоставляет функциональность для управления категориями на AliExpress. Он позволяет извлекать URL-адреса товаров, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

Основные характеристики:
- **Извлечение URL-адресов товаров**: Собирает URL-адреса товаров со страниц категорий.
- **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.

Пример использования:

.. code-block:: python

    from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

    # Пример использования
    supplier_instance = Supplier()
    category_urls = get_list_products_in_category(supplier_instance)
    update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
"""
import json
from typing import Any

import requests

from src.db.manager_categories.suppliers_categories import (
    AliexpressCategory,
    DBAdaptor as DBCategories,
)
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns


def get_list_products_in_category(s: Any) -> list[str]:
    """
    Извлекает список URL-адресов товаров со страницы категории, включая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :return: Список URL-адресов товаров со страницы категории.
    :rtype: list[str]
    """
    try:
        # Вызов функции для извлечения URL-адресов товаров с пагинацией.
        products_urls = get_prod_urls_from_pagination(s)
        return products_urls
    except Exception as e:
        logger.error(f'Ошибка при извлечении списка товаров из категории: {e}', exc_info=True)
        return []


def get_prod_urls_from_pagination(s: Any) -> list[str]:
    """
    Извлекает URL-адреса товаров со страниц категорий, обрабатывая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :return: Список URL-адресов товаров.
    :rtype: list[str]
    """
    products_urls = []
    try:
        # Код выполняет получение локатора для списка товаров
        products_locator = s.locator.products_list
        # Код выполняет получение списка элементов товаров
        products_elements = s.driver.get_elements(products_locator)
    except Exception as ex:
        logger.error(f'Не удалось получить список элементов: {ex}', exc_info=True)
        return products_urls

    for product_element in products_elements:
        try:
            # Код выполняет получение атрибута href из элемента товара
            product_url = product_element.get_attribute('href')
            if product_url:
                # Код добавляет URL товара в список
                products_urls.append(product_url)
        except Exception as ex:
            logger.error(f'Не удалось получить URL-адрес товара: {ex}', exc_info=True)

    try:
        # Код выполняет проверку наличия пагинации
        pagination_locator = s.locator.pagination
        if s.driver.is_element_present(pagination_locator):
            # Код выполняет получение списка элементов пагинации
            pagination_elements = s.driver.get_elements(pagination_locator)
        else:
            return products_urls
    except Exception as ex:
        logger.error(f'Не удалось получить элементы пагинации: {ex}', exc_info=True)
        return products_urls

    for el in pagination_elements:
        try:
            # Код выполняет клик по элементу пагинации
            el.click()
            # Код ждет загрузку страницы
            s.driver.wait_page_load()
            # Код выполняет получение нового списка элементов товаров на новой странице
            new_products_elements = s.driver.get_elements(products_locator)
            for product_element in new_products_elements:
                try:
                    # Код выполняет получение атрибута href из элемента товара
                    product_url = product_element.get_attribute('href')
                    if product_url:
                        # Код добавляет URL товара в список
                        products_urls.append(product_url)
                except Exception as ex:
                    logger.error(f'Не удалось получить URL-адрес товара: {ex}', exc_info=True)
        except Exception as ex:
            logger.error(f'Не удалось перейти на следующую страницу пагинации: {ex}', exc_info=True)

    return products_urls


def update_categories_in_scenario_file(s: Any, scenario_filename: str) -> bool:
    """
    Сравнивает категории на сайте с категориями в предоставленном файле сценария и обновляет файл любыми изменениями.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param scenario_filename: Имя файла сценария, который нужно обновить.
    :type scenario_filename: str
    :return: True, если категории были успешно обновлены, False в противном случае.
    :rtype: bool
    """
    try:
        # Код выполняет загрузку файла сценария
        with open(scenario_filename, 'r', encoding='utf-8') as f:
            scenario = j_loads(f)
    except Exception as e:
        logger.error(f'Не удалось загрузить файл сценария {scenario_filename}: {e}', exc_info=True)
        return False

    # Код выполняет получение списка категорий с сайта
    new_categories = get_list_categories_from_site(s, scenario)

    if not new_categories:
        logger.error('Не удалось получить список категорий с сайта')
        return False
    # Код выполняет сравнение категорий из файла и с сайта
    if scenario['categories'] != new_categories:
        scenario['categories'] = new_categories
        try:
            # Код выполняет запись обновленного файла сценария
            with open(scenario_filename, 'w', encoding='utf-8') as f:
                json.dump(scenario, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            logger.error(f'Не удалось обновить файл сценария {scenario_filename}: {e}', exc_info=True)
            return False

    return True


def get_list_categories_from_site(s: Any, scenario: dict, brand: str = '') -> list:
    """
    Извлекает список категорий с сайта AliExpress, на основе предоставленного файла сценария.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param scenario: Файл сценария, содержащий информацию о категориях.
    :type scenario: dict
    :param brand: Фильтр по бренду для категорий.
    :type brand: str, optional
    :return: Список категорий с сайта.
    :rtype: list
    """
    categories = []
    try:
        # Код выполняет получение списка URL-адресов категорий из сценария
        categories_urls = scenario.get('categories_urls', [])
        if not categories_urls:
            logger.error('В файле сценария отсутствуют URL-адреса категорий')
            return categories
    except Exception as ex:
        logger.error(f'Не удалось получить URL-адреса категорий из сценария {scenario}: {ex}', exc_info=True)
        return categories

    for url in categories_urls:
        try:
            # Код выполняет открытие URL-адреса категории в браузере
            s.driver.get(url)
            # Код выполняет ожидание загрузки страницы
            s.driver.wait_page_load()
            # Код выполняет получение локатора для элементов категорий
            category_elements_locator = s.locator.category_elements
        except Exception as ex:
            logger.error(f'Не удалось перейти по URL-адресу {url}: {ex}', exc_info=True)
            continue
        try:
            # Код выполняет получение элементов категорий
            category_elements = s.driver.get_elements(category_elements_locator)
            for category_element in category_elements:
                # Код выполняет извлечение текста из элемента категории
                category_name = category_element.text
                # Код добавляет имя категории в список
                categories.append(category_name)
        except Exception as ex:
            logger.error(f'Не удалось получить элементы категорий по локатору {category_elements_locator}: {ex}',
                         exc_info=True)
            continue

    return categories


class DBAdaptor:
    """
    Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции,
    такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` для записей `AliexpressCategory`.
    """

    def __init__(self, db):
        """
        Инициализирует адаптер базы данных.

        :param db: Экземпляр подключения к базе данных.
        :type db: Any
        """
        self.db = db
        self.db_categories = DBCategories(db)

    def select(self, **kwargs) -> list[AliexpressCategory]:
        """
        Извлекает записи из таблицы `AliexpressCategory`.

        :param kwargs: Критерии для фильтрации запроса.
        :type kwargs: dict
        :return: Список записей `AliexpressCategory`, соответствующих критериям запроса.
        :rtype: list[AliexpressCategory]
        """
        return self.db_categories.select(AliexpressCategory, **kwargs)

    def insert(self, data: dict) -> None:
        """
        Вставляет новую запись в таблицу `AliexpressCategory`.

        :param data: Данные для вставки новой записи.
        :type data: dict
        """
        self.db_categories.insert(AliexpressCategory, data)

    def update(self, data: dict, **kwargs) -> None:
        """
        Обновляет существующую запись в таблице `AliexpressCategory`.

        :param data: Данные для обновления записи.
        :type data: dict
        :param kwargs: Критерии для фильтрации записи, которую нужно обновить.
        :type kwargs: dict
        """
        self.db_categories.update(AliexpressCategory, data, **kwargs)

    def delete(self, **kwargs) -> None:
        """
        Удаляет запись из таблицы `AliexpressCategory`.

        :param kwargs: Критерии для фильтрации записи, которую нужно удалить.
        :type kwargs: dict
        """
        self.db_categories.delete(AliexpressCategory, **kwargs)
```

# Внесённые изменения

- Добавлены docstring к модулю, функциям и классу в формате reStructuredText (RST).
- Добавлены импорты `json` и `Any` для корректной работы.
- Изменены комментарии после `#` для подробного описания следующих за ними блоков кода.
- Добавлена обработка ошибок с использованием `logger.error` с `exc_info=True` для получения трассировки стека.
- Использованы `j_loads` и `j_loads_ns` из `src.utils.jjson` для чтения файлов.
- Добавлены проверки на наличие данных перед их обработкой, для избежания ошибок.
- Добавлена проверка на наличие пагинации перед ее обработкой.
- Удалены лишние `try-except` блоки для улучшения читаемости кода, обработка ошибок вынесена на более высокий уровень.

# Оптимизированный код

```python
"""
Модуль для управления категориями AliExpress.
=========================================================================================

Этот модуль предоставляет функциональность для управления категориями на AliExpress. Он позволяет извлекать URL-адреса товаров, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

Основные характеристики:
- **Извлечение URL-адресов товаров**: Собирает URL-адреса товаров со страниц категорий.
- **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.

Пример использования:

.. code-block:: python

    from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

    # Пример использования
    supplier_instance = Supplier()
    category_urls = get_list_products_in_category(supplier_instance)
    update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
"""
import json
from typing import Any

import requests

from src.db.manager_categories.suppliers_categories import (
    AliexpressCategory,
    DBAdaptor as DBCategories,
)
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns


def get_list_products_in_category(s: Any) -> list[str]:
    """
    Извлекает список URL-адресов товаров со страницы категории, включая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :return: Список URL-адресов товаров со страницы категории.
    :rtype: list[str]
    """
    try:
        # Вызов функции для извлечения URL-адресов товаров с пагинацией.
        products_urls = get_prod_urls_from_pagination(s)
        return products_urls
    except Exception as e:
        logger.error(f'Ошибка при извлечении списка товаров из категории: {e}', exc_info=True)
        return []


def get_prod_urls_from_pagination(s: Any) -> list[str]:
    """
    Извлекает URL-адреса товаров со страниц категорий, обрабатывая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :return: Список URL-адресов товаров.
    :rtype: list[str]
    """
    products_urls = []
    try:
        # Код выполняет получение локатора для списка товаров
        products_locator = s.locator.products_list
        # Код выполняет получение списка элементов товаров
        products_elements = s.driver.get_elements(products_locator)
    except Exception as ex:
        logger.error(f'Не удалось получить список элементов: {ex}', exc_info=True)
        return products_urls

    for product_element in products_elements:
        try:
            # Код выполняет получение атрибута href из элемента товара
            product_url = product_element.get_attribute('href')
            if product_url:
                # Код добавляет URL товара в список
                products_urls.append(product_url)
        except Exception as ex:
            logger.error(f'Не удалось получить URL-адрес товара: {ex}', exc_info=True)

    try:
        # Код выполняет проверку наличия пагинации
        pagination_locator = s.locator.pagination
        if s.driver.is_element_present(pagination_locator):
            # Код выполняет получение списка элементов пагинации
            pagination_elements = s.driver.get_elements(pagination_locator)
        else:
            return products_urls
    except Exception as ex:
        logger.error(f'Не удалось получить элементы пагинации: {ex}', exc_info=True)
        return products_urls

    for el in pagination_elements:
        try:
            # Код выполняет клик по элементу пагинации
            el.click()
            # Код ждет загрузку страницы
            s.driver.wait_page_load()
            # Код выполняет получение нового списка элементов товаров на новой странице
            new_products_elements = s.driver.get_elements(products_locator)
            for product_element in new_products_elements:
                try:
                    # Код выполняет получение атрибута href из элемента товара
                    product_url = product_element.get_attribute('href')
                    if product_url:
                        # Код добавляет URL товара в список
                        products_urls.append(product_url)
                except Exception as ex:
                    logger.error(f'Не удалось получить URL-адрес товара: {ex}', exc_info=True)
        except Exception as ex:
            logger.error(f'Не удалось перейти на следующую страницу пагинации: {ex}', exc_info=True)

    return products_urls


def update_categories_in_scenario_file(s: Any, scenario_filename: str) -> bool:
    """
    Сравнивает категории на сайте с категориями в предоставленном файле сценария и обновляет файл любыми изменениями.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param scenario_filename: Имя файла сценария, который нужно обновить.
    :type scenario_filename: str
    :return: True, если категории были успешно обновлены, False в противном случае.
    :rtype: bool
    """
    try:
        # Код выполняет загрузку файла сценария
        with open(scenario_filename, 'r', encoding='utf-8') as f:
            scenario = j_loads(f)
    except Exception as e:
        logger.error(f'Не удалось загрузить файл сценария {scenario_filename}: {e}', exc_info=True)
        return False

    # Код выполняет получение списка категорий с сайта
    new_categories = get_list_categories_from_site(s, scenario)

    if not new_categories:
        logger.error('Не удалось получить список категорий с сайта')
        return False
    # Код выполняет сравнение категорий из файла и с сайта
    if scenario['categories'] != new_categories:
        scenario['categories'] = new_categories
        try:
            # Код выполняет запись обновленного файла сценария
            with open(scenario_filename, 'w', encoding='utf-8') as f:
                json.dump(scenario, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            logger.error(f'Не удалось обновить файл сценария {scenario_filename}: {e}', exc_info=True)
            return False

    return True


def get_list_categories_from_site(s: Any, scenario: dict, brand: str = '') -> list:
    """
    Извлекает список категорий с сайта AliExpress, на основе предоставленного файла сценария.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: Any
    :param scenario: Файл сценария, содержащий информацию о категориях.
    :type scenario: dict
    :param brand: Фильтр по бренду для категорий.
    :type brand: str, optional
    :return: Список категорий с сайта.
    :rtype: list
    """
    categories = []
    try:
        # Код выполняет получение списка URL-адресов категорий из сценария
        categories_urls = scenario.get('categories_urls', [])
        if not categories_urls:
            logger.error('В файле сценария отсутствуют URL-адреса категорий')
            return categories
    except Exception as ex:
        logger.error(f'Не удалось получить URL-адреса категорий из сценария {scenario}: {ex}', exc_info=True)
        return categories

    for url in categories_urls:
        try:
            # Код выполняет открытие URL-адреса категории в браузере
            s.driver.get(url)
            # Код выполняет ожидание загрузки страницы
            s.driver.wait_page_load()
            # Код выполняет получение локатора для элементов категорий
            category_elements_locator = s.locator.category_elements
        except Exception as ex:
            logger.error(f'Не удалось перейти по URL-адресу {url}: {ex}', exc_info=True)
            continue
        try:
            # Код выполняет получение элементов категорий
            category_elements = s.driver.get_elements(category_elements_locator)
            for category_element in category_elements:
                # Код выполняет извлечение текста из элемента категории
                category_name = category_element.text
                # Код добавляет имя категории в список
                categories.append(category_name)
        except Exception as ex:
            logger.error(f'Не удалось получить элементы категорий по локатору {category_elements_locator}: {ex}',
                         exc_info=True)
            continue

    return categories


class DBAdaptor:
    """
    Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции,
    такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` для записей `AliexpressCategory`.
    """

    def __init__(self, db):
        """
        Инициализирует адаптер базы данных.

        :param db: Экземпляр подключения к базе данных.
        :type db: Any
        """
        self.db = db
        self.db_categories = DBCategories(db)

    def select(self, **kwargs) -> list[AliexpressCategory]:
        """
        Извлекает записи из таблицы `AliexpressCategory`.

        :param kwargs: Критерии для фильтрации запроса.
        :type kwargs: dict
        :return: Список записей `AliexpressCategory`, соответствующих критериям запроса.
        :rtype: list[AliexpressCategory]
        """
        return self.db_categories.select(AliexpressCategory, **kwargs)

    def insert(self, data: dict) -> None:
        """
        Вставляет новую запись в таблицу `AliexpressCategory`.

        :param data: Данные для вставки новой записи.
        :type data: dict
        """
        self.db_categories.insert(AliexpressCategory, data)

    def update(self, data: dict, **kwargs) -> None:
        """
        Обновляет существующую запись в таблице `AliexpressCategory`.

        :param data: Данные для обновления записи.
        :type data: dict
        :param kwargs: Критерии для фильтрации записи, которую нужно обновить.
        :type kwargs: dict
        """
        self.db_categories.update(AliexpressCategory, data, **kwargs)

    def delete(self, **kwargs) -> None:
        """
        Удаляет запись из таблицы `AliexpressCategory`.

        :param kwargs: Критерии для фильтрации записи, которую нужно удалить.
        :type kwargs: dict
        """
        self.db_categories.delete(AliexpressCategory, **kwargs)