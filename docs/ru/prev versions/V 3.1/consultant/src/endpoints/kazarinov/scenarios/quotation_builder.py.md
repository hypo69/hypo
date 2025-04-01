## Анализ кода модуля `quotation_builder`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован и содержит docstring для большинства функций.
    - Используются `logger` для логирования ошибок.
    - Присутствует обработка исключений.
    - Использование `j_loads` и `j_loads_ns` для загрузки JSON-данных.
- **Минусы**:
    - Не везде соблюдены PEP8 (например, пробелы вокруг операторов).
    - Некоторые docstring требуют доработки и уточнения.
    - Не все переменные аннотированы типами.
    - Встречаются `...`, которые необходимо заменить на конкретную реализацию или `pass`.
    - Есть дублирование кода (например, в `process_ai` и `process_ai_async`).
    - Не все функции имеют docstring.

**Рекомендации по улучшению:**

1.  **Форматирование и PEP8**:
    - Добавить пробелы вокруг операторов присваивания и других операторов для улучшения читаемости.
    - Исправить отступы в соответствии с PEP8.

2.  **Документация**:
    - Дополнить docstring для всех функций, методов и классов, включая описание аргументов, возвращаемых значений и возможных исключений.
    - Привести примеры использования в docstring.
    - Уточнить и конкретизировать существующие docstring.

3.  **Типизация**:
    - Добавить аннотации типов для всех переменных, аргументов функций и возвращаемых значений, где это еще не сделано.

4.  **Обработка `...`**:
    - Заменить все `...` конкретной реализацией или `pass`, если код еще не реализован.

5.  **Удаление дублирования кода**:
    - Вынести общую логику из `process_ai` и `process_ai_async` в отдельную функцию и использовать ее в обеих функциях.

6.  **Использовать одинарные кавычки**:
    - Заменить двойные кавычки на одинарные, если это возможно.

7.  **Логирование**:
    - Всегда передавай `exc_info=True` в `logger.error`, чтобы получить traceback.

8. **Проверка наличия ключей в словарях**:
    - При обращении к ключам словарей (`product_data['product_id']`) следует проверять их наличие, чтобы избежать `KeyError`.

9. **Обработка ошибок**:
    - В блоках `try...except` всегда явно указывайте тип перехватываемого исключения (например, `except KeyError as e:`).

**Оптимизированный код:**

```python
## \file /src/endpoints/kazarinov/scenarios/quotation_builder.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
The module handles data preparation, AI processing, and integration with Facebook for product posting.
==================================================================

```rst
.. module:: src.endpoints.kazarinov.scenarios.quotation_builder
    :platform: Windows, Unix
    :synopsis: Provides functionality for extracting, parsing, and processing product data from
various suppliers. The module handles data preparation, AI processing,
and integration with Facebook for product posting.
```

"""
import re
import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List, Any, Tuple, Dict
from types import SimpleNamespace
from dataclasses import field

import telebot
import requests
from bs4 import BeautifulSoup
from jinja2.utils import F
from pydantic.type_adapter import P

import header
from header import __root__
from src import gs
from src.endpoints.prestashop.product_fields import ProductFields

from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.webdriver.playwright import Playwrid

from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
)
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.endpoints.kazarinov.report_generator import ReportGenerator

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_image_from_url_async, save_image
from src.utils.printer import pprint as print
from src.logger.logger import logger

##############################################################

ENDPOINT = 'kazarinov'

#############################################################

class QuotationBuilder:
    """
    Processes the extraction, parsing, and saving of supplier product data.

    Attributes:
        driver (Driver): Selenium WebDriver instance.
        export_path (Path): Path for exporting data.
        products_list (List[dict]): List of processed product data.
    """

    base_path: Path = __root__ / 'src' / 'endpoints' / ENDPOINT

    try:
        config: SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')
    except Exception as ex:
        logger.error('Error loading configuration', ex, exc_info=True)

    html_path: str | Path
    pdf_path: str | Path
    docx_path: str | Path

    driver: 'Driver'
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: 'GoogleGenerativeAI'
    translations: 'SimpleNamespace' = j_loads_ns(base_path / 'translations' / 'mexiron.json')

    # Not all product fields need to be filled. Here is a tuple of required fields:
    required_fields: tuple = (
        'id_product',
        'name',
        'description_short',
        'description',
        'specification',
        'local_image_path'
    )


    def __init__(
        self,
        mexiron_name: Optional[str] = gs.now,
        driver: Optional[Firefox | Playwrid | str] = None,
        **kwards
    ) -> None:
        """
        Initializes the QuotationBuilder class with required components.

        Args:
            mexiron_name (Optional[str]): Custom name for the Mexiron process. Defaults to current timestamp.
            driver (Optional[Firefox | Playwrid | str]): WebDriver instance or name ('firefox', 'playwright'). Defaults to Firefox.
            **kwards: Additional keyword arguments to pass to the WebDriver initialization.
        """
        self.mexiron_name = mexiron_name
        try:
            self.export_path = gs.path.external_storage / ENDPOINT / 'mexironim' / self.mexiron_name
        except Exception as ex:
            logger.error('Error constructing export path:', ex, exc_info=True)
            return

        # 1. Initialize webdriver
        if driver:
            if isinstance(driver, Driver):
                self.driver = driver
            elif isinstance(driver, (Firefox, Playwrid)):  # Chrome, Edge
                self.driver = Driver(driver, **kwards)
            elif isinstance(driver, str):
                if driver.lower() == 'firefox':
                    self.driver = Driver(Firefox, **kwards)
                elif driver.lower() == 'playwright':
                    self.driver = Driver(Playwrid, **kwards)
        else:
            self.driver = Driver(Firefox, **kwards)

        # 2. Initialize Gemini model
        try:
            system_instruction: str = (gs.path.endpoints / ENDPOINT / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            api_key: str = gs.credentials.gemini.kazarinov
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error('Error loading model, or instructions or API key:', ex, exc_info=True)


    def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Converts product fields from a ProductFields object into a dictionary.

        Args:
            f (ProductFields): Object containing parsed product data.

        Returns:
            dict: Formatted product data dictionary. Returns an empty dictionary if product ID is missing.

        Note:
            The rules for constructing fields are defined in `ProductFields`.
        """
        if not f.id_product:
            logger.error('Failed to retrieve product fields.')
            return {}  # Failure to retrieve product fields. This can happen if a category page is encountered instead of a product page

        def escape_and_strip(text: str) -> str:
            """
            Cleans and escapes a string by replacing '"' and '"' with '\\"' and '\\"',
            and removing leading/trailing spaces.
            """
            if not text:
                return ''
            # Escape '"' and '"', replace ";" with "<br>", remove extra spaces
            escaped_text = re.sub(r"['\"]", lambda match: '\\' + match.group(0), text.strip()).replace(';', '<br>')
            return escaped_text

        product_name = escape_and_strip(f.name['language'][0]['value']) if f.name and f.name['language'] and len(f.name['language']) > 0 and 'value' in f.name['language'][0] else ''
        description = escape_and_strip(f.description['language'][0]['value']) if f.description and f.description['language'] and len(f.description['language']) > 0 and 'value' in f.description['language'][0] else ''
        description_short = escape_and_strip(f.description_short['language'][0]['value']) if f.description_short and f.description_short['language'] and len(f.description_short['language']) > 0 and 'value' in f.description_short['language'][0] else ''
        specification = escape_and_strip(f.specification['language'][0]['value']) if f.specification and f.specification['language'] and len(f.specification['language']) > 0 and 'value' in f.specification['language'][0] else ''

        if not product_name:
            return {}

        return {
            'product_name': product_name,
            'product_id': f.id_product,
            'description_short': description_short,
            'description': description,
            'specification': specification,
            'local_image_path': str(f.local_image_path),
        }

    def _process_ai(self, products_list: List[str], lang: str, attempts: int = 3, async_mode: bool = False) -> dict:
        """
        Processes the product list through the AI model.

        Args:
            products_list (str): List of product data dictionaries as a string.
            lang (str): Language of the model command ('ru' or 'he').
            attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.
            async_mode (bool, optional): Whether to use asynchronous mode. Defaults to False.

        Returns:
            dict: Processed response from the AI model.
            dict: Empty dict if unable to get a valid response after retries.

        Note:
            The model may return an invalid result. In such cases, the model is re-queried a reasonable number of times.
        """
        if attempts < 1:
            logger.error('No attempts left to process AI.')
            return {}  # return early if no attempts are left

        try:
            model_command = Path(gs.path.endpoints / ENDPOINT / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
            # Request response from the AI model
            q = model_command + '\n' + str(products_list)
            if async_mode:
                response = await self.model.ask_async(q)
            else:
                response = self.model.ask(q)
        except Exception as ex:
            logger.error('Error while processing AI request', ex, exc_info=True)
            return {}

        if not response:
            logger.error('No response from the model')
            return {}

        try:
            response_dict: dict = j_loads(response)  # <- вернет пустой словарь, если будет ошибка
        except Exception as ex:
            logger.error('Error parsing model response', ex, exc_info=True)
            return {}

        if not response_dict:
            logger.error(f'Attempt {attempts} failed to parse model response')
            if attempts > 1:
                return self._process_ai(products_list, lang, attempts - 1, async_mode)
            return {}
        return response_dict

    def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> dict:
        """
        Processes the product list through the AI model synchronously.

        Args:
            products_list (str): List of product data dictionaries as a string.
            lang (str): Language of the model command ('ru' or 'he').
            attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

        Returns:
            dict: Processed response from the AI model.
            dict: Empty dict if unable to get a valid response after retries.

        Note:
            The model may return an invalid result. In such cases, the model is re-queried a reasonable number of times.
        """
        return self._process_ai(products_list, lang, attempts)

    async def process_ai_async(self, products_list: List[str], lang: str, attempts: int = 3) -> dict:
        """
        Processes the product list through the AI model asynchronously.

        Args:
            products_list (str): List of product data dictionaries as a string.
            lang (str): Language of the model command ('ru' or 'he').
            attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

        Returns:
            dict: Processed response from the AI model.
            dict: Empty dict if unable to get a valid response after retries.

        Note:
            The model may return an invalid result. In such cases, the model is re-queried a reasonable number of times.
        """
        return await self._process_ai(products_list, lang, attempts, async_mode=True)


    async def save_product_data(self, product_data: dict) -> bool:
        """
        Saves individual product data to a file.

        Args:
            product_data (dict): Formatted product data.

        Returns:
            bool: True if the data was successfully saved, False otherwise.
        """
        file_path = self.export_path / 'products' / f"{product_data.get('product_id', 'undefined')}.json" # проверка наличия ключа
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Error saving dictionary {print(product_data)}\n Path: {file_path}')
            return False
        return True


    async def post_facebook_async(self, mexiron: SimpleNamespace) -> bool:
        """Executes the scenario of the `facebook` advertising module."""
        # self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
        currency = "ש''ח"
        title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
        if not post_message_title(self.driver, title):
            logger.warning('Failed to send mexiron title')
            return False

        if not upload_post_media(self.driver, media=mexiron.products):
            logger.warning('Failed to send media')
            return False

        if not message_publish(self.driver):
            logger.warning('Failed to publish message')
            return False

        return True


def main():
    """Main function to execute the quotation builder."""
    lang: str = 'he'

    mexiron_name: str = '250203025325520'
    base_path: Path = Path(gs.path.external_storage)
    export_path = base_path / ENDPOINT / 'mexironim' / mexiron_name
    html_path: Path = export_path / f'{mexiron_name}_{lang}.html'
    pdf_path: Path = export_path / f'{mexiron_name}_{lang}.pdf'
    docx_path: Path = export_path / f'{mexiron_name}_{lang}.doc'
    data = j_loads(export_path / f'{mexiron_name}_{lang}.json')

    quotation = QuotationBuilder(mexiron_name)
    # asyncio.run(quotation.create_reports(data[lang], mexiron_name, lang, html_path, pdf_path, docx_path))
    #TODO quotation.create_reports не реализован
    ...


if __name__ == '__main__':
    main()