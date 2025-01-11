# Анализ кода модуля `executor`

**Качество кода**
8
-   Плюсы
    - Код содержит примеры использования функций модуля `executor`.
    - Примеры охватывают основные функции модуля, включая запуск сценариев, обработку файлов сценариев и взаимодействие с PrestaShop API.
    - Присутствуют пояснения к примерам, что облегчает понимание их назначения.
    -  Используются `Path` для работы с путями к файлам, что является хорошей практикой.
-   Минусы
    -   Отсутствует документация в формате RST для функций и классов.
    -   Некоторые части кода используют `print` для вывода информации, что не подходит для production.
    -   Не используется `logger` для отслеживания ошибок и событий.
    -   Присутствуют заглушки (Mock) для Supplier, RelatedModules и Driver, что усложняет понимание реальной работы кода.
    -   Не хватает обработки исключений в примерах.
    -   Не хватает проверки на корректность входных данных.
    -   Импорты не полные и не соответствуют стандартам.

**Рекомендации по улучшению**

1.  **Добавить документацию в формате RST:**
    -   Добавить docstring в начале файла с описанием модуля.
    -   Добавить docstring для каждой функции, описывая ее назначение, аргументы и возвращаемые значения.
2.  **Заменить `print` на `logger`:**
    -   Использовать `logger.info` для информационных сообщений и `logger.error` для сообщений об ошибках.
3.  **Добавить обработку исключений:**
    -   Обернуть вызовы функций, которые могут вызывать ошибки, в блоки `try-except` и логировать ошибки с помощью `logger.error`.
4.  **Улучшить примеры:**
    -   Добавить проверку на корректность входных данных перед их использованием.
    -   Удалить заглушки (Mock) классов и добавить более реалистичные примеры.
5.  **Добавить импорты:**
    -   Добавить необходимые импорты для модуля asyncio.
    -   Указать импорт для logger.

**Оптимизированный код**

```python
"""
Примеры для модуля `executor` из `src.scenario.executor`.
=========================================================================================

Этот файл содержит примеры использования функций, предоставляемых в модуле `executor`.
Примеры демонстрируют, как запускать сценарии, обрабатывать файлы сценариев и взаимодействовать с PrestaShop API.

Подробности
----------
- `Example 1` показывает, как запустить список файлов сценариев.
- `Example 2` демонстрирует, как запустить один файл сценария.
- `Example 3` иллюстрирует, как запустить один сценарий.
- `Example 4` предоставляет пример выполнения сценария страницы продукта.
- `Example 5` показывает, как добавить купон с помощью PrestaShop API.

Изображение
----------
.. image:: html executor.png

"""
import asyncio
from pathlib import Path
from typing import List, Dict, Any
# Импортируем logger
from src.logger.logger import logger
# Импортируем необходимые функции из executor
from src.scenario.executor import run_scenario_files, run_scenario_file, run_scenarios, run_scenario, insert_grabbed_data, execute_PrestaShop_insert, execute_PrestaShop_insert_async, add_coupon
# Импортируем j_loads_ns для загрузки json файлов
from src.utils.jjson import j_loads_ns
# Импортируем ProductFields для работы с полями продуктов
from src.endpoints.prestashop.product_fields import ProductFields
# Импортируем PrestaShop для взаимодействия с API PrestaShop
from src.endpoints.PrestaShop import PrestaShop


#  Предполагаем, что класс `Supplier` доступен и имеет необходимые методы и атрибуты
class MockSupplier:
    """
    Мок класс для имитации поставщика.
    """
    def __init__(self):
        """
        Инициализация мок объекта Supplier.
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
    """
    def get_list_products_in_category(self, s) -> List[str]:
        """
        Мок метод для получения списка URL продуктов в категории.

        Args:
            s (Any):  Не используется в мок-реализации.

        Returns:
            list[str]:  Список URL продуктов.
        """
        return ['http://example.com/product1', 'http://example.com/product2']

    def grab_product_page(self, s) -> ProductFields:
        """
        Мок метод для имитации сбора данных со страницы продукта.

        Args:
            s (Any): Не используется в мок-реализации.

        Returns:
            ProductFields: Мок объект ProductFields с данными продукта.
        """
        return ProductFields(
            presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
            assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
        )

    async def grab_page(self, s) -> ProductFields:
        """
        Асинхронный мок метод для имитации сбора данных со страницы продукта.

        Args:
             s (Any): Не используется в мок-реализации.

        Returns:
             ProductFields: Мок объект ProductFields с данными продукта.
        """
        return self.grab_product_page(s)


class MockDriver:
    """
    Мок класс для имитации драйвера браузера.
    """
    def get_url(self, url) -> bool:
        """
        Мок метод для имитации перехода по URL.

        Args:
            url (str): URL для перехода.

        Returns:
            bool: True, если переход выполнен.
        """
        return True


# Example 1: Run a list of scenario files
def example_run_scenario_files():
    """
    Пример запуска списка файлов сценариев.
    """
    supplier = MockSupplier()
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    try: #  Обрабатываем возможные ошибки при выполнении сценариев
        result = run_scenario_files(supplier, scenario_files)
        if result:
            logger.info("Все сценарии выполнены успешно.")
        else:
            logger.error("Некоторые сценарии не выполнены.")
    except Exception as ex: #  Логируем любые возникшие исключения
        logger.error(f"Ошибка при выполнении сценариев: {ex}")


# Example 2: Run a single scenario file
def example_run_scenario_file():
    """
    Пример запуска одного файла сценария.
    """
    supplier = MockSupplier()
    scenario_file = Path('scenarios/scenario1.json')
    try: #  Обрабатываем возможные ошибки при выполнении сценария
        result = run_scenario_file(supplier, scenario_file)
        if result:
            logger.info("Файл сценария выполнен успешно.")
        else:
            logger.error("Не удалось выполнить файл сценария.")
    except Exception as ex: #  Логируем любые возникшие исключения
        logger.error(f"Ошибка при выполнении файла сценария: {ex}")

# Example 3: Run a single scenario
def example_run_scenario():
    """
    Пример запуска одного сценария.
    """
    supplier = MockSupplier()
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    try: #  Обрабатываем возможные ошибки при выполнении сценария
        result = run_scenario(supplier, scenario)
        if result:
            logger.info("Сценарий выполнен успешно.")
        else:
            logger.error("Не удалось выполнить сценарий.")
    except Exception as ex: #  Логируем любые возникшие исключения
        logger.error(f"Ошибка при выполнении сценария: {ex}")

# Example 4: Insert grabbed product data into PrestaShop
def example_insert_grabbed_data():
    """
    Пример вставки полученных данных о продукте в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try: #  Обрабатываем возможные ошибки при вставке данных
        insert_grabbed_data(product_fields)
        logger.info("Данные о продукте вставлены в PrestaShop.")
    except Exception as ex: #  Логируем любые возникшие исключения
        logger.error(f"Ошибка при вставке данных о продукте: {ex}")

# Example 5: Add a coupon using PrestaShop API
def example_add_coupon():
    """
    Пример добавления купона с использованием PrestaShop API.
    """
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    try: #  Обрабатываем возможные ошибки при добавлении купона
        add_coupon(credentials, reference, coupon_code, start_date, end_date)
        logger.info("Купон успешно добавлен.")
    except Exception as ex: #  Логируем любые возникшие исключения
         logger.error(f"Ошибка при добавлении купона: {ex}")


# Example 6: Execute PrestaShop insert asynchronously
async def example_execute_PrestaShop_insert_async():
    """
    Пример асинхронного выполнения вставки данных о продукте в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try: #  Обрабатываем возможные ошибки при асинхронной вставке данных
        await execute_PrestaShop_insert_async(product_fields)
        logger.info("Данные о продукте асинхронно вставлены в PrestaShop.")
    except Exception as ex: #  Логируем любые возникшие исключения
        logger.error(f"Ошибка при асинхронной вставке данных о продукте: {ex}")


# Example 7: Execute PrestaShop insert synchronously
def example_execute_PrestaShop_insert():
    """
    Пример синхронного выполнения вставки данных о продукте в PrestaShop.
    """
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    try: #  Обрабатываем возможные ошибки при синхронной вставке данных
        result = execute_PrestaShop_insert(product_fields)
        if result:
            logger.info("Данные о продукте вставлены в PrestaShop.")
        else:
            logger.error("Не удалось вставить данные о продукте в PrestaShop.")
    except Exception as ex: #  Логируем любые возникшие исключения
        logger.error(f"Ошибка при синхронной вставке данных о продукте: {ex}")


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