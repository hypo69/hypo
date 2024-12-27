# Анализ кода модуля `_example_executor.py`

**Качество кода**
7
-   Плюсы
    -   Код содержит примеры использования функций из `src.scenario.executor`.
    -   Присутствуют примеры синхронного и асинхронного выполнения.
    -   Используются mock-объекты для тестирования.
    -   Код структурирован и понятен.
-   Минусы
    -   Отсутствует reStructuredText (RST) документация для модуля, классов и функций.
    -   Используются прямые вызовы `print` вместо логирования через `src.logger.logger`.
    -   Присутствуют неиспользуемые импорты и переменные.
    -   Не стандартизировано именование переменных и функций.
    -   Присутствуют пустые docstring и комментарии.
    -   Не используется `j_loads_ns` для загрузки файлов.

**Рекомендации по улучшению**

1.  **Документация**: Добавить RST документацию для модуля, классов и функций.
2.  **Логирование**: Заменить `print` на `logger.info` или `logger.error` для логирования.
3.  **Импорты**: Удалить неиспользуемые импорты и привести в соответствие с ранее обработанными файлами.
4.  **Именование**: Привести имена функций и переменных к единому стилю (snake_case).
5.  **Обработка ошибок**: Использовать `logger.error` вместо `try-except` для обработки ошибок в `example_execute_PrestaShop_insert_async` и `example_execute_PrestaShop_insert`.
6.  **Загрузка файлов**: Использовать `j_loads_ns` для чтения json файлов.
7.  **Удалить лишние комментарии**: удалить пустые комментарии.
8.  **Расширить Mock**: Расширить функционал Mock классов для более полного покрытия.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль с примерами использования executor
=======================================================

Этот модуль содержит примеры использования функций из модуля `src.scenario.executor`.
Примеры демонстрируют запуск сценариев, обработку файлов сценариев и взаимодействие с PrestaShop API.

Примеры использования
--------------------

- `example_run_scenario_files`: показывает запуск списка файлов сценариев.
- `example_run_scenario_file`: показывает запуск одного файла сценария.
- `example_run_scenario`: показывает запуск одного сценария.
- `example_insert_grabbed_data`: показывает вставку полученных данных продукта в PrestaShop.
- `example_add_coupon`: показывает добавление купона с использованием PrestaShop API.
- `example_execute_PrestaShop_insert_async`: показывает асинхронную вставку данных продукта в PrestaShop.
- `example_execute_PrestaShop_insert`: показывает синхронную вставку данных продукта в PrestaShop.

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
from src.utils.jjson import j_loads_ns
from src.product.product_fields import ProductFields
from src.logger.logger import logger  # Добавлен импорт logger

# Mock класс для Supplier
class MockSupplier:
    """
    Mock класс для имитации поставщика.

    :ivar Path supplier_abs_path: Абсолютный путь к директории со сценариями.
    :ivar list scenario_files: Список путей к файлам сценариев.
    :ivar dict supplier_settings: Словарь настроек поставщика.
    :ivar MockRelatedModules related_modules: Mock объект для связанных модулей.
    :ivar MockDriver driver: Mock объект для драйвера.
    """
    def __init__(self):
        """
        Инициализирует MockSupplier.
        """
        self.supplier_abs_path = Path('/path/to/scenarios')
        self.scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
        self.current_scenario = None
        self.supplier_settings = {'runned_scenario': []}
        self.related_modules = MockRelatedModules()
        self.driver = MockDriver()

# Mock класс для связанных модулей
class MockRelatedModules:
    """
    Mock класс для имитации связанных модулей.
    """
    def get_list_products_in_category(self, s):
        """
        Имитирует получение списка продуктов в категории.

        :param s: Параметр (не используется в мок-классе).
        :return: Список URL-адресов продуктов.
        """
        return ['http://example.com/product1', 'http://example.com/product2']

    def grab_product_page(self, s):
        """
        Имитирует получение данных со страницы продукта.

        :param s: Параметр (не используется в мок-классе).
        :return: Объект ProductFields с mock данными.
        """
        return ProductFields(
            presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
            assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
        )

    async def grab_page(self, s):
        """
        Асинхронно имитирует получение данных со страницы продукта.

        :param s: Параметр (не используется в мок-классе).
        :return: Объект ProductFields с mock данными.
        """
        return self.grab_product_page(s)

# Mock класс для драйвера
class MockDriver:
    """
    Mock класс для имитации драйвера.
    """
    def get_url(self, url):
        """
        Имитирует получение URL-адреса.

        :param str url: URL-адрес для имитации получения.
        :return: True.
        """
        return True

# Example 1: Run a list of scenario files
def example_run_scenario_files():
    """
    Запускает список файлов сценариев.
    """
    supplier = MockSupplier()
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    result = run_scenario_files(supplier, scenario_files)
    if result:
        logger.info("All scenarios executed successfully.")
    else:
        logger.error("Some scenarios failed.")

# Example 2: Run a single scenario file
def example_run_scenario_file():
    """
    Запускает один файл сценария.
    """
    supplier = MockSupplier()
    scenario_file = Path('scenarios/scenario1.json')
    result = run_scenario_file(supplier, scenario_file)
    if result:
         logger.info("Scenario file executed successfully.")
    else:
        logger.error("Failed to execute scenario file.")

# Example 3: Run a single scenario
def example_run_scenario():
    """
    Запускает один сценарий.
    """
    supplier = MockSupplier()
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    result = run_scenario(supplier, scenario)
    if result:
        logger.info("Scenario executed successfully.")
    else:
        logger.error("Failed to execute the scenario.")

# Example 4: Insert grabbed product data into PrestaShop
def example_insert_grabbed_data():
    """
    Вставляет полученные данные продукта в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    insert_grabbed_data(product_fields)
    logger.info("Product data inserted into PrestaShop.")

# Example 5: Add a coupon using PrestaShop API
def example_add_coupon():
    """
    Добавляет купон с использованием PrestaShop API.
    """
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    add_coupon(credentials, reference, coupon_code, start_date, end_date)
    logger.info("Coupon added successfully.")

# Example 6: Execute PrestaShop insert asynchronously
async def example_execute_PrestaShop_insert_async():
    """
    Асинхронно вставляет данные продукта в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try:
        await execute_PrestaShop_insert_async(product_fields)
        logger.info("Product data inserted into PrestaShop asynchronously.")
    except Exception as e:
        logger.error("Failed to insert product data into PrestaShop asynchronously.", exc_info=e)


# Example 7: Execute PrestaShop insert synchronously
def example_execute_PrestaShop_insert():
    """
    Синхронно вставляет данные продукта в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    result = execute_PrestaShop_insert(product_fields)
    if result:
        logger.info("Product data inserted into PrestaShop.")
    else:
        logger.error("Failed to insert product data into PrestaShop.")

# Running the examples
if __name__ == "__main__":
    example_run_scenario_files()
    example_run_scenario_file()
    example_run_scenario()
    example_insert_grabbed_data()
    example_add_coupon()
    asyncio.run(example_execute_PrestaShop_insert_async())
    example_execute_PrestaShop_insert()
```