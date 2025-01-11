# Анализ кода модуля `from_supplier_to_prestashop`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код содержит docstring для модуля и функций.
    *   Используется `logger` для логирования ошибок.
    *   Применяются асинхронные операции.
    *   Используется `j_loads_ns`, `j_dumps`, `j_loads`.
-   **Минусы:**
    *   Не все функции имеют полные docstring (например, отсутствуют примеры использования).
    *   Много `...` в коде, что затрудняет понимание.
    *   Присутствует избыточное использование `try-except`, когда можно использовать `logger.error`.
    *   Некоторые логи `logger.debug` не информативны.
    *   Импорты не все в начале файла, есть локальные импорты (например, `header`).
    *   Используется `self.d` вместо `self.driver` в методе `post_facebook`.
    *   Не хватает проверок на None значения, когда работаешь с `ProductFields`

**Рекомендации по улучшению**

1.  **Импорты:**
    *   Перенести все импорты в начало файла, включая `header`.
2.  **Документация:**
    *   Добавить примеры использования в docstring для функций `save_text_file`, `convert_product_fields`, `save_product_data`, `process_ai`.
    *   Уточнить docstring для класса `SupplierToPrestashopProvider`.
    *   Заменить docstring в функции `run_scenario` на более подробное описание.
3.  **Логирование:**
    *   Заменить `...` на более информативные логи, когда это необходимо.
    *   Уточнить сообщения об ошибках, делая их более конкретными.
    *   Использовать `logger.error` для обработки ошибок вместо `try-except` там, где это возможно.
4.  **Обработка данных:**
    *   Проверять на `None` переменные при работе с данными от `ProductFields`
    *   Убрать `...` и добавить логирование.
5.  **Код:**
    *   Переименовать `self.d` на `self.driver` в методе `post_facebook`.
    *   Уточнить тип `products_list: List = field(default_factory=list)` добавить тип данных.
    *   В методе `run_scenario` вынести проверку существования `graber` в отдельную функцию и описать в docstring.

**Оптимизированный код**

```python
"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

```rst
.. module:: src.endpoints.emil.scenarios.from_supplier_to_prestashop
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from
various suppliers. The module handles data preparation, AI processing,
and integration with Prestashop for product posting.
```

"""

from __future__ import annotations

import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from types import SimpleNamespace
from dataclasses import field

from telegram import Update
from telegram.ext import CallbackContext

from src import gs
from src.endpoints.prestashop.product_fields import ProductFields
from src.webdriver.driver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
)
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_image_from_url, save_image
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger.logger import logger
from src.endpoints.emil.report_generator import ReportGenerator
from src.suppliers import aliexpress
import header # <-  импорт в начале файла

class SupplierToPrestashopProvider:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

    Attributes:
        driver (Driver): Экземпляр Selenium WebDriver.
        export_path (Path): Путь для экспорта данных.
        products_list (List[dict]): Список обработанных данных о продуктах.
        mexiron_name (str): Название мехирона.
        price (float): Цена продукта.
        timestamp (str): Временная метка.
        model (GoogleGenerativeAI): Экземпляр модели Google Gemini AI.
        config (SimpleNamespace): Конфигурация из файла `emil.json`.
        update (Update): Объект Telegram Update.
        context (CallbackContext): Объект Telegram CallbackContext.
    """

    driver: 'Driver'
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List[dict] = field(default_factory=list) # <- добавил тип данных
    model: 'GoogleGenerativeAI'
    config: SimpleNamespace
    update: 'Update'
    context: 'CallbackContext'

    def __init__(self, driver: Driver):
        """
        Инициализирует класс `SupplierToPrestashopProvider` необходимыми компонентами.

        Args:
            driver (Driver): Экземпляр Selenium WebDriver.
        """
        try:
            self.config = j_loads_ns(gs.path.endpoints / 'emil' / 'emil.json')
        except Exception as ex:
            logger.error(f"Ошибка загрузки конфигурации: {ex}")
            return  # или вызвать исключение, в зависимости от стратегии обработки ошибок

        self.timestamp = gs.now
        self.driver = driver

        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'emil'
        except Exception as ex:
            logger.error(f"Ошибка при создании пути экспорта: {ex}")
            return


        try:
            system_instruction = (gs.path.endpoints / 'emil' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')

            api_key = gs.credentials.gemini.emil
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error(f"Ошибка загрузки инструкций или API ключа: {ex}")
            return


    async def run_scenario(
        self,
        update: Update,
        context: CallbackContext,
        urls: list[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = '',

    ) -> bool:
        """
        Выполняет сценарий: извлекает, обрабатывает данные о продуктах, сохраняет их.

        Args:
            update (Update): Объект Telegram Update.
            context (CallbackContext): Объект Telegram CallbackContext.
            urls (list[str]): Список URL-адресов страниц товаров.
            price (Optional[str]): Цена для обработки.
            mexiron_name (Optional[str]): Пользовательское название мехирона.

        Returns:
            bool: True, если сценарий выполнен успешно, иначе False.

        .. todo::
           Сделать логер перед отрицательным выходом из функции.
           Важно! Модель ошибается.
        """
        self.update = update
        self.context = context

        # Не все поля товара надо заполнять. Вот кортеж необходимых полей:
        required_fields: tuple = (
            'id_product',
            'name',
            'description_short',
            'description',
            'specification',
            'local_image_path'
        )
        products_list = []

        # 1. Сбор товаров
        for url in urls:

            graber = self.get_graber_by_supplier_url(url)

            if not graber:
                logger.debug(f"Нет грабера для: {url}")
                continue

            try:
                await update.message.reply_text(f"Process: \n{url}")
                f = await graber.grab_page(*required_fields)

                if gs.host_name == 'Vostro-3888':
                    pass
                    #self.driver.wait(5)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара", ex)
                continue

            if not f:
                logger.debug(f'Не удалось разобрать поля товара для URL: {url}')
                continue

            product_data = await self.convert_product_fields(f)
            if not product_data:
                logger.debug(f'Не удалось преобразовать поля товара: {product_data}')
                continue

            if not await self.save_product_data(product_data):
                logger.error(f"Данные не сохранены! {pprint(product_data)}")
                continue
            products_list.append(product_data)


    def get_graber_by_supplier_url(self, url:str) -> aliexpress.AliExpress | None:
        """
        Определяет грабер в зависимости от URL поставщика.

        Args:
            url (str): URL-адрес страницы товара.

        Returns:
            Union[aliexpress.AliExpress, None]: Экземпляр грабера, если найден, иначе None.
        """
        if 'aliexpress' in url:
            return aliexpress.AliExpress(driver=self.driver)
        logger.error(f"Неизвестный URL: {url}")
        return None

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Преобразует поля товара из объекта `ProductFields` в словарь.

        Args:
            f (ProductFields): Объект, содержащий данные о товаре.

        Returns:
            dict: Словарь с преобразованными данными о товаре.

        .. note:: Правила построения полей определяются в `ProductFields`

        Example:
        ```python
            product_fields = ProductFields(
                id_product='123',
                name=[{'language':[{'value':'Test product'}]}],
                description_short=[{'language':[{'value':'Short description'}]}],
                description=[{'language':[{'value':'Long description'}]}],
                specification=[{'language':[{'value':'Specification'}]}],
                local_image_path=Path('/path/to/image.jpg')
            )
            result = await convert_product_fields(product_fields)
            print(result)
            # Expected output:
            # {
            #   'product_title': 'Test product',
            #   'product_id': '123',
            #   'description_short': 'Short description',
            #   'description': 'Long description',
            #   'specification': 'Specification',
            #   'local_image_path': '/path/to/image.jpg'
            # }
        ```
        """
        if not f.id_product:
            return {} # <- сбой при получении полей товара. Такое может произойти если вместо страницы товара попалась страница категории, при невнимательном составлении мехирона из комплектующих
        if not f.name or not f.description_short or not f.description or not f.specification: # <- проверка на None
            logger.error(f"Отсутствуют необходимые поля в f: {f}")
            return {}

        return {
            'product_title': f.name['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
            'description': f.description['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
            'specification': f.specification['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
            'local_image_path': str(f.local_image_path),
        }

    async def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные о товаре в файл.

        Args:
            product_data (dict): Словарь с данными о товаре.

        Returns:
            bool: True, если данные успешно сохранены, иначе False.

        Example:
            ```python
            product_data = {'product_id': '123', 'product_title': 'Test product'}
            result = await save_product_data(product_data)
            print(result)
            # Expected output: True or False (if save failed)
            ```
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {pprint(product_data)}\\n Путь: {file_path}')
            return False
        return True

    async def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> dict | bool:
        """
        Обрабатывает список товаров с помощью AI модели.

        Args:
            products_list (List[str]): Список словарей с данными о товарах в виде строки.
            lang (str): Язык ответа.
            attempts (int, optional): Количество попыток запроса к модели в случае неудачи. Defaults to 3.

        Returns:
            dict: Обработанные данные в форматах `ru` и `he`.
            bool: False, если не удалось получить валидный ответ после нескольких попыток.

        .. note::
            Модель может возвращать невалидный результат.
            В таком случае я переспрашиваю модель разумное количество раз.

        Example:
        ```python
            products = [{'product_id': '123', 'product_title': 'Test product'}]
            lang = 'ru'
            result = await process_ai(str(products), lang)
            print(result)
            # Expected output: dict
        ```
        """
        if attempts < 1:
             logger.error(f"Нет попыток")
             return {}  # return early if no attempts are left

        model_command = Path(gs.path.endpoints / 'emil' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
        # Request response from the AI model
        q = model_command + '\n' + str(products_list)
        response = await self.model.ask(q)
        if not response:
            logger.error("Нет ответа от модели")
            return {}

        try:
            response_dict: dict = j_loads(response)
        except Exception as ex:
             logger.error(f"Ошибка парсинга ответа модели: {ex}")
             if attempts > 1:
                 return await self.process_ai(products_list, lang, attempts - 1)
             return {}

        if not response_dict:
             logger.error("Ошибка парсинга ответа модели")
             if attempts > 1:
                 return await self.process_ai(products_list, lang, attempts - 1)
             return {}
        return response_dict


    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """Функция исполняет сценарий рекламного модуля `facvebook`."""
        self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
        currency = "ש''ח"
        title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
        if not post_message_title(self.driver, title): # <- self.d -> self.driver
            logger.warning(f'Не получилось отправить название мехирона')
            return False

        if not upload_post_media(self.driver, media=mexiron.products):  # <- self.d -> self.driver
            logger.warning(f'Не получилось отправить media')
            return False

        if not message_publish(self.driver): # <- self.d -> self.driver
            logger.warning(f'Не получилось отправить media')
            return False

        return True

    async def create_report(self, data: dict, lang: str, html_file: Path, pdf_file: Path) -> bool:
        """Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
        Если мехорон в pdf создался (`generator.create_report()` вернул True) -
        отправить его боту
        """

        generator = ReportGenerator()

        if await generator.create_report(data, lang, html_file, pdf_file):
            # Проверка, существует ли файл и является ли он файлом
            if pdf_file.exists() and pdf_file.is_file():
                # Отправка боту PDF-файл через reply_document()
                await self.update.message.reply_document(document=pdf_file)
                return True
            else:
                logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
                return False
```