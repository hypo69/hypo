# Анализ кода модуля `category`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Хорошая документация в формате Markdown, описывающая функциональность модуля, классов и методов.
    - Четкое разделение на функции и классы с понятными целями.
    - Описание зависимостей модуля.
- **Минусы**:
    - Отсутствуют docstrings в формате RST для функций и классов.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Импорт `logger` не соответствует `from src.logger import logger`.
    - Отсутствует обработка ошибок с помощью `logger.error`.
    - Нет примеров кода для функций в RST формате.
    - Присутствуют общие фразы в описании функций.

## Рекомендации по улучшению:
- Добавить docstrings в формате RST для всех функций, классов и методов.
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для работы с JSON.
- Исправить импорт `logger` на `from src.logger import logger`.
- Добавить обработку ошибок через `logger.error` для отслеживания проблем.
- Избегать общих фраз в описании, заменять их точными описаниями действий (например, «проверяет», «отправляет», «выполняет»).
- Добавить примеры использования функций в docstrings.

## Оптимизированный код:
```python
"""
Модуль для управления категориями на AliExpress
===================================================

Модуль предоставляет функциональность для управления категориями на AliExpress.
Он позволяет получать URL продуктов, обновлять списки категорий и взаимодействовать с платформой
AliExpress для синхронизации категорий.

Основные возможности:
- **Получение URL продуктов**: Сбор URL продуктов со страниц категорий.
- **Синхронизация категорий**: Сравнение и обновление категорий на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предоставляет операции для управления категориями в базе данных.

Пример использования:
----------------------
.. code-block:: python

    from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file
    # Пример использования
    supplier_instance = Supplier()
    category_urls = get_list_products_in_category(supplier_instance)
    update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
"""
from src.db.manager_categories.suppliers_categories import AliexpressCategory  # импорт для работы с категориями в бд
from src.utils.jjson import j_loads, j_loads_ns # импорт для работы с JSON
from src.logger import logger # импорт logger
# from requests import get # импорт для запросов
from pathlib import Path # импорт для работы с путями
from typing import List, Dict, Any # импорт для типов
# from src.suppliers.supplier import Supplier #  импорт класса Supplier


def get_list_products_in_category(s: object) -> List[str]:
    """
    Извлекает список URL-адресов продуктов со страницы категории, включая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: object
    :return: Список URL-адресов продуктов со страницы категории.
    :rtype: list[str]

    Пример:
    --------
    .. code-block:: python

        supplier_instance = Supplier()
        product_urls = get_list_products_in_category(supplier_instance)
        print(product_urls)
    """
    product_urls = [] # инициализация списка для хранения url товаров
    try:
        product_urls.extend(get_prod_urls_from_pagination(s)) # получаем url товаров со страниц пагинации
    except Exception as e: # ловим ошибку
        logger.error(f"Error in get_list_products_in_category: {e}") # логируем ошибку
    return product_urls # возвращаем список url товаров


def get_prod_urls_from_pagination(s: object) -> List[str]:
    """
    Извлекает URL-адреса продуктов со страниц категории, обрабатывая пагинацию.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: object
    :return: Список URL-адресов продуктов.
    :rtype: list[str]

    Пример:
    --------
    .. code-block:: python

        supplier_instance = Supplier()
        product_urls = get_prod_urls_from_pagination(supplier_instance)
        print(product_urls)
    """
    prod_urls = [] # инициализация списка для хранения url товаров
    try:
        s.driver.get(s.url)  # получаем url категории
        while True:
            prod_urls.extend([item.get_attribute('href') for item in s.driver.find_elements(*s.locators['product_item'])]) # добавляем в список url товаров с текущей страницы
            next_button = s.driver.find_elements(*s.locators['next_page_button'])  # проверяем наличие кнопки далее
            if not next_button: # если нет кнопки далее, то выходим из цикла
                break
            next_button[0].click()  # кликаем на кнопку далее
    except Exception as e:
          logger.error(f"Error in get_prod_urls_from_pagination: {e}") # логируем ошибку
    return prod_urls  # возвращаем список url товаров


def update_categories_in_scenario_file(s: object, scenario_filename: str) -> bool:
    """
    Сравнивает категории на сайте с категориями в предоставленном файле сценария и
    обновляет файл любыми изменениями.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: object
    :param scenario_filename: Имя файла сценария для обновления.
    :type scenario_filename: str
    :return: True, если категории были успешно обновлены, False в противном случае.
    :rtype: bool

     Пример:
    --------
    .. code-block:: python

        supplier_instance = Supplier()
        file_updated = update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
        print(file_updated)
    """
    try:
        scenario_file_path = Path(scenario_filename)  # путь к файлу сценария
        with open(scenario_file_path, 'r') as f:  # открываем файл на чтение
            scenario_data = j_loads(f.read())  # загружаем json данные из файла
        site_categories = get_list_categories_from_site(s, scenario_filename) # получаем список категорий с сайта
        if not site_categories: # проверяем, получили ли категории с сайта
             logger.error("Failed to get categories from site.") # если нет, логируем ошибку
             return False
        scenario_data['categories'] = site_categories  # обновляем данные в файле
        with open(scenario_file_path, 'w') as f:  # открываем файл на запись
            json.dump(scenario_data, f, indent=4)  # записываем обновленные данные в файл
        return True  # если все ок, то возвращаем True
    except Exception as e:  # ловим все ошибки
        logger.error(f"Error in update_categories_in_scenario_file: {e}")  # логируем ошибку
        return False  # в случае ошибки возвращаем False


def get_list_categories_from_site(s: object, scenario_file: str, brand: str = '') -> list:
    """
    Извлекает список категорий с сайта AliExpress, основываясь на предоставленном файле сценария.

    :param s: Экземпляр поставщика с драйвером браузера и локаторами.
    :type s: object
    :param scenario_file: Файл сценария, содержащий информацию о категориях.
    :type scenario_file: str
    :param brand: Фильтр бренда для категорий.
    :type brand: str, optional
    :return: Список категорий с сайта.
    :rtype: list

    Пример:
    --------
    .. code-block:: python

        supplier_instance = Supplier()
        categories = get_list_categories_from_site(supplier_instance, 'example_scenario.json', brand='Example Brand')
        print(categories)
    """
    categories = []  # инициализация списка для хранения категорий
    try:
        with open(scenario_file, 'r') as f:  # открываем файл на чтение
            scenario_data = j_loads(f.read())  # загружаем json данные из файла
        for category_data in scenario_data['categories']:  # проходимся по всем категориям
            url = category_data.get('url')  # получаем url категории
            if not url:  # проверяем, есть ли url
                logger.error(f"URL not found in category data: {category_data}")  # логируем ошибку если url нет
                continue # переходим к следующей итерации
            s.driver.get(url) # переходим по url
            category_name = s.driver.find_element(*s.locators['category_name']).text # получаем имя категории
            categories.append({
                'name': category_name,  # добавляем имя категории
                'url': url,  # добавляем url
                'brand': brand  # добавляем бренд
            })  # добавляем категорию в список
    except Exception as e:  # ловим все ошибки
        logger.error(f"Error in get_list_categories_from_site: {e}")  # логируем ошибку
    return categories  # возвращаем список категорий


class DBAdaptor:
    """
    Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные
    операции, такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` для записей `AliexpressCategory`.
    """
    def __init__(self, db):
        """
        Инициализация адаптера базы данных.
        :param db: Экземпляр базы данных.
        :type db: object
        """
        self.db = db  # получаем объект базы данных

    def select(self, **kwargs) -> List[AliexpressCategory]:
        """
        Извлекает записи из таблицы `AliexpressCategory`.

        :param kwargs: Критерии выбора.
        :type kwargs: dict
        :return: Список записей из таблицы `AliexpressCategory`.
        :rtype: list[AliexpressCategory]

        Пример:
        --------
        .. code-block:: python

            db_adaptor = DBAdaptor(db_instance)
            categories = db_adaptor.select(name='Example Category')
            print(categories)
        """
        try:
            return self.db.query(AliexpressCategory).filter_by(**kwargs).all()  # делаем запрос в бд
        except Exception as e:
            logger.error(f"Error in DBAdaptor select: {e}")
            return []

    def insert(self, data: Dict[str, Any]) -> bool:
        """
        Вставляет новую запись в таблицу `AliexpressCategory`.

        :param data: Данные для вставки.
        :type data: dict
        :return: True, если запись была успешно вставлена, False в противном случае.
        :rtype: bool

        Пример:
        --------
        .. code-block:: python

            db_adaptor = DBAdaptor(db_instance)
            new_category = {'name': 'New Category', 'url': 'http://example.com'}
            success = db_adaptor.insert(new_category)
            print(success)
        """
        try:
            new_record = AliexpressCategory(**data)  # создаем новый объект для бд
            self.db.add(new_record)  # добавляем объект в сессию
            self.db.commit() # коммитим изменения в бд
            return True # возвращаем True в случае успеха
        except Exception as e:  # ловим ошибки
            logger.error(f"Error in DBAdaptor insert: {e}")  # логируем ошибку
            self.db.rollback()  # откатываем изменения
            return False  # возвращаем False в случае неудачи

    def update(self, category_id: int, data: Dict[str, Any]) -> bool:
        """
        Обновляет существующую запись в таблице `AliexpressCategory`.

        :param category_id: ID записи для обновления.
        :type category_id: int
        :param data: Данные для обновления.
        :type data: dict
        :return: True, если запись была успешно обновлена, False в противном случае.
        :rtype: bool

         Пример:
        --------
        .. code-block:: python

            db_adaptor = DBAdaptor(db_instance)
            updated_category = {'name': 'Updated Category', 'url': 'http://updated.com'}
            success = db_adaptor.update(1, updated_category)
            print(success)
        """
        try:
            record = self.db.query(AliexpressCategory).filter(AliexpressCategory.id == category_id).first()  # делаем запрос к бд
            if record: # проверяем, нашли ли запись
                for key, value in data.items():  # проходимся по всем ключам и значениям
                    setattr(record, key, value) # обновляем значения
                self.db.commit()  # коммитим изменения в бд
                return True  # возвращаем True
            else:
                logger.error(f"Record with id {category_id} not found for update.") # логируем ошибку если запись не найдена
                return False  # возвращаем False если запись не найдена
        except Exception as e:  # ловим ошибки
            logger.error(f"Error in DBAdaptor update: {e}")  # логируем ошибку
            self.db.rollback()  # откатываем изменения
            return False  # возвращаем False в случае ошибки

    def delete(self, category_id: int) -> bool:
        """
        Удаляет запись из таблицы `AliexpressCategory`.

        :param category_id: ID записи для удаления.
        :type category_id: int
        :return: True, если запись была успешно удалена, False в противном случае.
        :rtype: bool

         Пример:
        --------
        .. code-block:: python

            db_adaptor = DBAdaptor(db_instance)
            success = db_adaptor.delete(1)
            print(success)
        """
        try:
            record = self.db.query(AliexpressCategory).filter(AliexpressCategory.id == category_id).first()  # делаем запрос к бд
            if record:  # проверяем, есть ли такая запись
                self.db.delete(record)  # удаляем запись
                self.db.commit()  # коммитим изменения
                return True  # возвращаем True
            else:
                logger.error(f"Record with id {category_id} not found for delete.") # логируем ошибку если запись не найдена
                return False  # возвращаем False
        except Exception as e:  # ловим ошибки
            logger.error(f"Error in DBAdaptor delete: {e}")  # логируем ошибку
            self.db.rollback()  # откатываем изменения
            return False  # возвращаем False
```