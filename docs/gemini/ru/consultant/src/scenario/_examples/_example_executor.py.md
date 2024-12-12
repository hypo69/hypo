# Анализ кода модуля src.scenario._examples._example_executor

**Качество кода**
8
-  Плюсы
    -  Код хорошо структурирован, с примерами использования функций из модуля `executor`.
    -  Используются моки для имитации зависимостей, что позволяет запускать примеры без реальных данных.
    -  Присутствуют примеры как синхронного, так и асинхронного выполнения операций.
-  Минусы
    -  Отсутствует docstring для модуля в начале файла.
    -  Не все функции и классы имеют docstring в формате reStructuredText (RST).
    -  Используется `print` для вывода сообщений, вместо логирования через `logger`.
    -  Не все импорты используеются (например, `j_loads_ns`).
    -  Не везде используется асинхронное выполнение, где это возможно (например, `run_scenario_files`).
    -  Много неиспользуемых пустых строк и комментариев `#`

**Рекомендации по улучшению**
1.  Добавить docstring для модуля в формате RST.
2.  Добавить docstring в формате RST для всех функций, классов и методов.
3.  Заменить `print` на `logger.info` для вывода сообщений об успехе и `logger.error` для ошибок.
4.  Удалить неиспользуемые импорты и комментарии `#`.
5.  Использовать асинхронное выполнение там, где это возможно, например, при запуске нескольких файлов сценариев.
6.  Убрать лишние пустые строки.
7.  Обеспечить консистентность в использовании кавычек (использовать одинарные кавычки `''`).
8.  Добавить обработку ошибок с помощью `try-except` и `logger.error` для повышения надежности кода.

**Оптимизиробанный код**
```python
# -*- coding: utf-8 -*-
"""
Примеры использования модуля `executor` из `src.scenario.executor`.
==================================================================

Этот модуль содержит примеры использования функций, предоставляемых в модуле `executor`.
Примеры демонстрируют, как запускать сценарии, обрабатывать файлы сценариев и взаимодействовать с PrestaShop API.

Подробности
----------
- `Пример 1` показывает, как запустить список файлов сценариев.
- `Пример 2` демонстрирует, как запустить один файл сценария.
- `Пример 3` иллюстрирует, как запустить один сценарий.
- `Пример 4` предоставляет пример выполнения сценария страницы продукта.
- `Пример 5` показывает, как добавить купон с использованием PrestaShop API.

Изображение
----------
.. image:: executor.png
   :alt: executor.png
"""

import asyncio
from pathlib import Path

from src.scenario.executor import (
    run_scenario_files,
    run_scenario_file,
    run_scenarios,
    run_scenario,
    insert_grabbed_data,
    execute_PrestaShop_insert,
    execute_PrestaShop_insert_async,
    add_coupon,
)
# from src.utils.jjson import j_loads_ns # Удален неиспользуемый импорт
from src.product.product_fields import ProductFields
# from src.endpoints.PrestaShop import PrestaShop # Удален неиспользуемый импорт
from src.logger.logger import logger


class MockSupplier:
    """
    Мок класс для имитации поставщика.

    Этот класс предоставляет необходимые атрибуты и методы для имитации поставщика,
    включая путь к файлам сценариев, список файлов сценариев, текущий сценарий, настройки поставщика
    и связанные модули.
    """
    def __init__(self):
        """
        Инициализирует мок поставщика.
        """
        self.supplier_abs_path = Path('/path/to/scenarios')
        self.scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
        self.current_scenario = None
        self.supplier_settings = {'runned_scenario': []}
        self.related_modules = MockRelatedModules()
        self.driver = MockDriver()

class MockRelatedModules:
    """
    Мок класс для имитации связанных модулей.

    Этот класс имитирует работу связанных модулей, таких как получение списка продуктов в категории и
    сбор данных со страницы продукта.
    """
    def get_list_products_in_category(self, s):
        """
        Имитирует получение списка продуктов в категории.

        :param s: Параметр (не используется в моке).
        :return: Список URL продуктов.
        """
        return ['http://example.com/product1', 'http://example.com/product2']

    def grab_product_page(self, s):
        """
        Имитирует сбор данных со страницы продукта.

        :param s: Параметр (не используется в моке).
        :return: Объект ProductFields с моковыми данными.
        """
        return ProductFields(
            presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
            assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
        )

    async def grab_page(self, s):
        """
        Асинхронно имитирует сбор данных со страницы.

        :param s: Параметр (не используется в моке).
        :return: Объект ProductFields с моковыми данными.
        """
        return self.grab_product_page(s)

class MockDriver:
    """
    Мок класс для имитации драйвера.

    Этот класс имитирует работу драйвера, например, переход по URL.
    """
    def get_url(self, url):
        """
        Имитирует переход по URL.

        :param url: URL для перехода.
        :return: True, имитирует успешный переход.
        """
        return True

# Пример 1: Запуск списка файлов сценариев
def example_run_scenario_files():
    """
    Пример запуска списка файлов сценариев.

    Этот пример демонстрирует, как запустить несколько файлов сценариев.
    """
    supplier = MockSupplier()
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    try:
        result = run_scenario_files(supplier, scenario_files)
        if result:
            logger.info('Все сценарии успешно выполнены.')
        else:
            logger.error('Некоторые сценарии не выполнены.')
    except Exception as e:
        logger.error(f'Произошла ошибка при выполнении сценариев: {e}')

# Пример 2: Запуск одного файла сценария
def example_run_scenario_file():
    """
    Пример запуска одного файла сценария.

    Этот пример показывает, как запустить один файл сценария.
    """
    supplier = MockSupplier()
    scenario_file = Path('scenarios/scenario1.json')
    try:
        result = run_scenario_file(supplier, scenario_file)
        if result:
            logger.info('Файл сценария успешно выполнен.')
        else:
            logger.error('Не удалось выполнить файл сценария.')
    except Exception as e:
         logger.error(f'Произошла ошибка при выполнении файла сценария: {e}')

# Пример 3: Запуск одного сценария
def example_run_scenario():
    """
    Пример запуска одного сценария.

    Этот пример демонстрирует, как запустить один сценарий.
    """
    supplier = MockSupplier()
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    try:
        result = run_scenario(supplier, scenario)
        if result:
            logger.info('Сценарий успешно выполнен.')
        else:
            logger.error('Не удалось выполнить сценарий.')
    except Exception as e:
        logger.error(f'Произошла ошибка при выполнении сценария: {e}')

# Пример 4: Вставка собранных данных о продукте в PrestaShop
def example_insert_grabbed_data():
    """
    Пример вставки собранных данных о продукте в PrestaShop.

    Этот пример показывает, как вставить данные о продукте, полученные со страницы, в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try:
        insert_grabbed_data(product_fields)
        logger.info('Данные о продукте вставлены в PrestaShop.')
    except Exception as e:
         logger.error(f'Произошла ошибка при вставке данных о продукте: {e}')

# Пример 5: Добавление купона через PrestaShop API
def example_add_coupon():
    """
    Пример добавления купона через PrestaShop API.

    Этот пример демонстрирует, как добавить купон с использованием PrestaShop API.
    """
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    try:
        add_coupon(credentials, reference, coupon_code, start_date, end_date)
        logger.info('Купон успешно добавлен.')
    except Exception as e:
        logger.error(f'Произошла ошибка при добавлении купона: {e}')

# Пример 6: Асинхронное выполнение вставки данных о продукте в PrestaShop
async def example_execute_PrestaShop_insert_async():
    """
    Пример асинхронной вставки данных о продукте в PrestaShop.

    Этот пример показывает, как асинхронно вставить данные о продукте в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try:
        await execute_PrestaShop_insert_async(product_fields)
        logger.info('Данные о продукте вставлены в PrestaShop асинхронно.')
    except Exception as e:
        logger.error(f'Произошла ошибка при асинхронной вставке данных о продукте: {e}')


# Пример 7: Синхронное выполнение вставки данных о продукте в PrestaShop
def example_execute_PrestaShop_insert():
    """
    Пример синхронной вставки данных о продукте в PrestaShop.

    Этот пример демонстрирует, как синхронно вставить данные о продукте в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try:
        result = execute_PrestaShop_insert(product_fields)
        if result:
            logger.info('Данные о продукте вставлены в PrestaShop.')
        else:
            logger.error('Не удалось вставить данные о продукте в PrestaShop.')
    except Exception as e:
        logger.error(f'Произошла ошибка при вставке данных о продукте: {e}')

# Запуск примеров
if __name__ == '__main__':
    example_run_scenario_files()
    example_run_scenario_file()
    example_run_scenario()
    example_insert_grabbed_data()
    example_add_coupon()
    asyncio.run(example_execute_PrestaShop_insert_async())
    example_execute_PrestaShop_insert()