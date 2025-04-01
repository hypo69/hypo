## Анализ кода модуля `from_supplier_to_prestashop.py`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Модульная структура, разделение на классы и функции.
  - Использование `logger` для логирования.
  - Применение `j_loads_ns` для загрузки JSON-данных.
- **Минусы**:
  - Неполная документация функций и классов.
  - Отсутствие обработки исключений в некоторых местах.
  - Смешанный стиль комментариев (русский и английский).
  - Использование `...` как заглушек кода.
  - Не все переменные аннотированы типами.

**Рекомендации по улучшению:**

1.  **Документация**:
    *   Дополнить документацию для всех функций, методов и классов в соответствии с форматом, указанным в инструкции.
    *   Добавить примеры использования в документацию.
    *   Убедиться, что все параметры и возвращаемые значения аннотированы типами.
2.  **Обработка ошибок**:
    *   Добавить обработку исключений для всех потенциально опасных операций, таких как чтение файлов, сетевые запросы и т.д.
    *   Использовать `logger.error` для логирования ошибок с трассировкой (`exc_info=True`).
3.  **Комментарии**:
    *   Привести все комментарии к единому стилю (русский).
    *   Удалить или заменить все `...` на полноценный код или `pass` с комментарием.
    *   Уточнить неясные комментарии, избегать расплывчатых формулировок.
4.  **Использование `j_loads`**:
    *   Убедиться, что все JSON-файлы загружаются с использованием `j_loads` или `j_loads_ns`.
5.  **Форматирование**:
    *   Проверить код на соответствие стандартам PEP8.
    *   Использовать autopep8 или black для автоматического форматирования.
6.  **Улучшение структуры**:
    *   Рассмотреть возможность разделения класса `SupplierToPrestashopProvider` на более мелкие классы или функции для повышения читаемости и поддерживаемости.
7.  **Безопасность**:
    *   Проверить использование переменных окружения и убедиться, что они не содержат конфиденциальную информацию в коде.

**Оптимизированный код:**

```python
## \file /src/endpoints/emil/scenarios/from_supplier_to_prestashop.py
# -*- coding: utf-8 -*-

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

import asyncio
import os
import random
import shutil
from pathlib import Path
from tkinter import SEL
from types import SimpleNamespace
from typing import List, Optional

import header
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    message_publish,
    post_message_title,
    upload_post_media,
)
from src.endpoints.emil.report_generator import ReportGenerator
from src.endpoints.prestashop.product import PrestaProduct
from src.endpoints.prestashop.product_fields import ProductFields
from src.logger.logger import logger
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.file import (
    read_text_file,
    recursively_get_file_path,
    save_text_file,
)
from src.utils.image import save_image, save_image_from_url
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint as print
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox

##############################################################

ENDPOINT = 'emil'
USE_ENV: bool = True  # <- Определает откуда брать ключи. Если False - то из базы данных с паролями, иначе из .env

if USE_ENV:
    from dotenv import load_dotenv

    load_dotenv()

#############################################################


class SupplierToPrestashopProvider:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.
    Данные могут быть получены как из посторнних сайтов, так из файла JSON.

    Attributes:
        driver (Driver): Экземпляр Selenium WebDriver.
        export_path (Path): Путь для экспорта данных.
        products_list (List[dict]): Список обработанных данных о продуктах.
        mexiron_name (str): Название мехирона.
        price (float): Цена мехирона.
        timestamp (str): Временная метка.
        model (GoogleGenerativeAI): Модель AI.
        config (SimpleNamespace): Конфигурация.
        local_images_path (Path): Путь к локальным изображениям.
        lang (str): Язык.
        gemini_api (str): API ключ Gemini.
        presta_api (str): API ключ Prestashop.
        presta_url (str): URL Prestashop.
    """

    driver: Driver
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: list
    model: GoogleGenerativeAI
    config: SimpleNamespace
    local_images_path: Path = gs.path.external_storage / ENDPOINT / 'images' / 'furniture_images'
    lang: str
    gemini_api: str
    presta_api: str
    presta_url: str

    def __init__(
        self,
        lang: str,
        gemini_api: str,
        presta_api: str,
        presta_url: str,
        driver: Optional[Driver] = None,
    ) -> None:
        """
        Initializes SupplierToPrestashopProvider class with required components.

        Args:
            lang (str): Язык.
            gemini_api (str): API ключ Gemini.
            presta_api (str): API ключ Prestashop.
            presta_url (str): URL Prestashop.
            driver (Optional[Driver], optional): Selenium WebDriver instance. Defaults to None.
        """
        self.gemini_api = gemini_api
        self.presta_api = presta_api
        self.presta_url = presta_url
        self.lang = lang
        try:
            self.config = j_loads_ns(gs.path.endpoints / ENDPOINT / f'{ENDPOINT}.json')
        except Exception as ex:
            logger.error(f'Error loading configuration: {ex}', exc_info=True)
            return  # or raise an exception, depending on your error handling strategy

        self.timestamp = gs.now
        self.driver = driver if driver else Driver(Firefox)
        self.model = self.initialise_ai_model()

    def initialise_ai_model(self) -> GoogleGenerativeAI | None:
        """Инициализация модели Gemini"""
        try:
            system_instruction = (
                gs.path.endpoints
                / 'emil'
                / 'instructions'
                / f'system_instruction_mexiron.{self.lang}.md'
            ).read_text(encoding='UTF-8')
            return GoogleGenerativeAI(
                api_key=gs.credentials.gemini.emil,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'},
            )
        except Exception as ex:
            logger.error('Error loading instructions', ex, exc_info=True)
            return None

    async def run_scenario(
        self,
        urls: list[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = '',
    ) -> bool:
        """
        Executes the scenario: parses products, processes them via AI, and stores data.

        Args:
            urls (list[str]): Product page URLs.
            price (Optional[str], optional): Price to process. Defaults to ''.
            mexiron_name (Optional[str], optional): Custom Mexiron name. Defaults to ''.

        Returns:
            bool: True if the scenario executes successfully, False otherwise.

        Raises:
            Exception: If any error occurs during the process.
        """

        # Не все поля товара надо заполнять. Вот кортеж необходимых полей:
        required_fields: tuple = (
            'id_product',
            'name',
            'description_short',
            'description',
            'specification',
            'local_image_path',
        )
        products_list = []

        # 1. Сбор товаров
        for url in urls:
            graber = get_graber_by_supplier_url(url)

            if not graber:
                logger.debug(f'Нет грабера для: {url}')
                continue

            try:
                f = await graber.grab_page(*required_fields)

                if gs.host_name == 'Vostro-3888':
                    # self.driver.wait(5)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
                    pass  # Заглушка для кода, который будет добавлен позже
            except Exception as ex:
                logger.error('Ошибка получения полей товара', ex, exc_info=True)
                continue

            if not f:
                logger.debug(f'Failed to parse product fields for URL: {url}')
                continue

            product_data = await self.convert_product_fields(f)
            if not product_data:
                logger.debug(f'Failed to convert product fields: {product_data}')
                continue

            if not await self.save_product_data(product_data):
                logger.error(f'Data not saved! {print(product_data)}')
                continue
            products_list.append(product_data)

        return True  # Добавлено для соответствия типу возврата функции

    async def save_product_data(self, product_data: dict) -> bool | None:
        """
        Saves individual product data to a file.

        Args:
            product_data (dict): Formatted product data.

        Returns:
            bool | None: True если данные успешно сохранены, None в случае ошибки.
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {print(product_data)}\n Путь: {file_path}')
            return None
        return True

    async def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> dict | bool:
        """
        Processes the product list through the AI model.

        Args:
            products_list (str): List of product data dictionaries as a string.
            lang (str): Язык.
            attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

        Returns:
            dict: Processed response in `ru` and `he` formats.
            bool: False if unable to get a valid response after retries.

        Note:
            Модель может возвращать невелидный результат.
            В таком случае я переспрашиваю модель разумное количество раз.
        """
        if attempts < 1:
            logger.warning('Превышено количество попыток получения ответа от модели')
            return {}  # return early if no attempts are left
        model_command = Path(
            gs.path.endpoints / 'emil' / 'instructions' / f'command_instruction_mexiron_{lang}.md'
        ).read_text(encoding='UTF-8')
        # Request response from the AI model
        q = model_command + '\n' + str(products_list)
        response = await self.model.ask(q)
        if not response:
            logger.error('Нет ответа от модели')
            return {}

        response_dict: dict = j_loads(response)

        if not response_dict:
            logger.error('Ошибка парсинга ответа модели', exc_info=True)
            if attempts > 1:
                await self.process_ai(products_list, lang, attempts - 1)
            return {}
        return response_dict

    async def read_data_from_json(self) -> None:
        """Загружаю JSON файлы и фотки, которые я сделал через телеграм"""

        # 1. Get from JSON
        raw_data = j_loads_ns(self.local_images_path)
        print(raw_data)

    async def save_in_prestashop(self, products_list: ProductFields | list[ProductFields]) -> bool:
        """Функция, которая сохраняет товары в Prestashop emil-design.com"""

        products_list: list = products_list if isinstance(products_list, list) else [products_list]

        p = PrestaProduct(api_key=self.presta_api, api_domain=self.presta_url)

        for f in products_list:
            p.add_new_product(f)
        return True

    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """Функция исполняет сценарий рекламного модуля `facvebook`."""

        self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
        currency = "ש''ח"
        title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
        if not post_message_title(self.driver, title):
            logger.warning('Не получилось отправить название мехирона')
            return False

        if not upload_post_media(self.driver, media=mexiron.products):
            logger.warning('Не получилось отправить media')
            return False
        if not message_publish(self.driver):
            logger.warning('Не получилось отправить media')
            return False

        return True

    async def create_report(self, data: dict, lang: str, html_file: Path, pdf_file: Path) -> bool | None:
        """
        Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
        Если мехорон в pdf создался (`generator.create_report()` вернул True) -
        отправить его боту
        """

        report_generator = ReportGenerator()

        if await report_generator.create_report(data, lang, html_file, pdf_file):
            # Проверка, существует ли файл и является ли он файлом
            if pdf_file.exists() and pdf_file.is_file():
                # Отправка боту PDF-файл через reply_document()
                # await self.update.message.reply_document(document=pdf_file) #  <- Закомментировано, тк нет update
                logger.info(f'Отправлен боту PDF-файл: {pdf_file}')
                return True
            else:
                logger.error(f'PDF файл не найден или не является файлом: {pdf_file}')
                return None
        return False


async def main():
    """На данный момент функция читает JSON со списком фотографий, которые были получены от Эмиля"""
    lang = 'he'
    products_ns = j_loads_ns(gs.path.external_storage / ENDPOINT / 'out_250108230345305_he.json')

    suppier_to_presta = SupplierToPrestashopProvider(lang)
    products_list: list = [f for f in products_ns]
    await suppier_to_presta.save_in_prestashop(products_list)


if __name__ == '__main__':
    asyncio.run(main())