## Анализ кода модуля `ali_promo_campaign.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Хорошая структурированность кода с разделением на методы для выполнения различных задач.
  - Использование `SimpleNamespace` для хранения данных конфигурации и кампании.
  - Документация присутствует, но требует доработки.
- **Минусы**:
  - Не везде соблюдены стандарты PEP8, особенно в части форматирования строк и пробелов.
  - В некоторых местах отсутствует документация или она неполная.
  - Не все переменные аннотированы типами.

**Рекомендации по улучшению:**

1. **Форматирование и стиль кода**:
   - Привести код в соответствие со стандартами PEP8.
   - Использовать black formater

2. **Документация**:
   - Дополнить документацию для всех методов и классов, используя указанный формат.
   - Уточнить описания аргументов и возвращаемых значений, добавить примеры использования.

3. **Использование `j_loads` и `j_dumps`**:
   - Убедиться, что все операции чтения и записи JSON-файлов используют `j_loads` и `j_dumps` из `src.utils.jjson`.
   - Проверить обработку ошибок при чтении JSON-файлов.

4. **Логирование**:
   - Использовать `logger` для записи информации, предупреждений и ошибок.
   - Добавить логирование в ключевых местах кода для облегчения отладки и мониторинга.

5. **Обработка ошибок**:
   - Проверить и улучшить обработку ошибок, особенно при работе с внешними API и файлами.
   - Использовать `try-except` блоки для обработки возможных исключений.

6. **Типизация**:
   - Добавить аннотации типов для всех переменных и параметров функций.
   - Использовать `Optional` и `Union` (через `|`) для указания возможных типов значений.

7. **Рефакторинг**:
   - Разбить сложные методы на более мелкие и простые для понимания.
   - Избавиться от дублирования кода.

**Оптимизированный код:**

```python
## \file /src/suppliers/aliexpress/campaign/ali_promo_campaign.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для управления рекламными кампаниями на платформе AliExpress.
====================================================================

Модуль содержит класс :class:`AliPromoCampaign`, который позволяет загружать и обрабатывать данные
рекламных кампаний, управлять категориями и товарами, а также использовать ИИ для генерации описаний и других данных.

Пример использования:
----------------------

>>> campaign = AliPromoCampaign(campaign_name='new_campaign', language='EN', currency='USD')
>>> campaign.process_campaign()
"""

import asyncio
import copy
import html
import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

from src import gs
from src.ai.gemini import GoogleGenerativeAI
#from src.ai.openai import OpenAIModel
from src.logger.logger import logger
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.campaign.html_generators import (
    CampaignHTMLGenerator,
    CategoryHTMLGenerator,
    ProductHTMLGenerator,
)
from src.suppliers.aliexpress.utils import locales
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.utils.convertors.csv import csv2dict
from src.utils.file import (
    get_directory_names,
    get_filenames,
    read_text_file,
    save_text_file,
)
from src.utils.jjson import j_dumps, j_loads_ns
from src.utils.printer import pprint


class AliPromoCampaign:
    """Управление рекламной кампанией."""

    language: str = None
    currency: str = None
    base_path: Path = None
    campaign_name: str = None
    campaign: SimpleNamespace = None
    campaign_ai: SimpleNamespace = None
    gemini: GoogleGenerativeAI = None
    #openai: OpenAIModel = None

    def __init__(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
        model: str = 'openai',
    ) -> None:
        """Инициализация объекта AliPromoCampaign для рекламной кампании.

        Args:
            campaign_name (str): Название кампании.
            language (Optional[str]): Язык, используемый в кампании. Defaults to None.
            currency (Optional[str]): Валюта, используемая в кампании. Defaults to None.
            model (str): Модель для генерации AI данных. Defaults to 'openai'.

        Example:
            >>> campaign = AliPromoCampaign(campaign_name='SummerSale', language='EN', currency='USD')
            >>> print(campaign.campaign_name)
            SummerSale
        """
        self.campaign_name = campaign_name
        self.base_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name
        campaign_file_path = self.base_path / f'{language}_{currency}.json'
        self.campaign = j_loads_ns(
            campaign_file_path, exc_info=False
        )  # <- файла может не быть, если я создаю новую рекламную камапнию - файл будет создан ИИ
        if not self.campaign:
            logger.warning(
                f'Campaign file not found at {campaign_file_path=}\\nStart as new \\n (Start build JSON file, categories, products etc.)'
            )
            # Если в корне рекламной кампании нет файла JSON -> запускается процесс создания новой реклмной кампании
            # создадутся категории из названий директорий ц директории `catergorry`,
            # соберутся affiliated товары в файлы <product_id>.JSON
            # сгенеририуется ai параметры
            self.process_new_campaign(
                campaign_name=campaign_name, language=language, currency=currency
            )  # <- создание новой рекламной кампании
            return

        if self.campaign.language and self.campaign.currency:
            self.language, self.currency = (
                self.campaign.language,
                self.campaign.currency,
            )
        else:
            self.language, self.currency = language, currency

        # self.campaign_ai = copy.copy(self.campaign)
        self._models_payload()

    def _models_payload(self) -> None:
        """Инициализация моделей AI."""
        # self.campaign_ai_file_name = f"{self.language}_{self.currency}_{model}_{gs.now}.json"
        system_instruction_path = gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'
        system_instruction: str = read_text_file(system_instruction_path)
        # self.model = OpenAIModel(system_instruction=system_instruction,
        #                         assistant_id = gs.credentials.openai.assistant.category_descriptions)
        self.gemini = GoogleGenerativeAI(system_instruction=system_instruction)
        assistant_id = 'asst_dr5AgQnhhhnef5OSMzQ9zdk9'  # <-  задача asst_dr5AgQnhhhnef5OSMzQ9zdk9 создание категорий и описаний на основе списка названий товаров
        # self.openai = OpenAIModel(system_instruction = system_instruction, assistant_id = assistant_id)

    def process_campaign(self) -> None:
        """Итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

        Example:
            >>> campaign.process_campaign()
        """
        categories_names_list = get_directory_names(self.base_path / 'category')  # читаю название папок категорий
        for category_name in categories_names_list:
            logger.info(f'Starting {category_name=}')
            self.process_category_products(category_name)
            logger.info('Starting AI category')
            self.process_ai_category(category_name)
            ...

    def process_campaign_category(self, category_name: str) -> Optional[List[SimpleNamespace]]:
        """Обрабатывает конкретную категорию в кампании для всех языков и валют.

        Args:
            category_name (str): Категория для кампании.

        Returns:
            Optional[List[SimpleNamespace]]: Список названий продуктов в категории.
        """
        # Process category products and get the list of products
        self.process_category_products(category_name=category_name)
        self.process_ai_category(category_name=category_name)
        return None

    def process_new_campaign(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
    ) -> None:
        """Создание новой рекламной кампании.

        Условия для создания кампании:
        - директория кампании с питоник названием
        - вложенная директория `campaign`, в ней директории с питоник названиями категорий
        - файл sources.txt и/или директория `sources` с файлами `<product)id>.html`

        Args:
            campaign_name (str): Название рекламной кампании.
            language (Optional[str]): Язык для кампании (необязательно).
            currency (Optional[str]): Валюта для кампании (необязательно).

        Flowchart:
        ┌──────────────────────────────────────────────┐
        │ Start                                        │
        └──────────────────────────────────────────────┘
                          │
                          ▼
        ┌───────────────────────────────────────────────┐
        │ Check if `self.language` and `self.currency`  │
        │ are set                                       │
        └───────────────────────────────────────────────┘
                          │
                ┌─────────┴──────────────────────────┐
                │                                    │
                ▼                                    ▼
        ┌─────────────────────────────┐   ┌──────────────────────────────────────┐
        │Yes: `locale` = `{language:  │   │No: `locale` = {                      │
        │currency}`                   │   │     'EN': 'USD',                     │
        │                             │   │     'HE': 'ILS',                     │
        │                             │   │     'RU': 'ILS'                      │
        │                             │   │    }                                 │
        └─────────────────────────────┘   └──────────────────────────────────────┘
                         │                         │
                         ▼                         ▼
        ┌───────────────────────────────────────────────┐
        │ For each `language`, `currency` in `locale`:  │
        │ - Set `self.language`, `self.currency`        │
        │ - Initialize `self.campaign`                  │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────────┐
        │ Call `self.set_categories_from_directories()` │
        │ to populate categories                        │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────────┐
        │ Copy `self.campaign` to `self.campaign_ai`    │
        │ and set `self.campaign_ai_file_name`          │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────────┐
        │ For each `category_name` in campaign:         │
        │ - Call `self.process_category_products`       │
        │ - Call `self.process_ai_category`             │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌──────────────────────────────────────────────┐
        │ End                                          │
        └──────────────────────────────────────────────┘
        """
        if not language and not currency:
            # Process all locales if language or currency is not provided
            _l = [(lang, curr) for locale in locales for lang, curr in locale.items()]
        else:
            _l = [(language, currency)]

        for language, currency in _l:
            self.language, self.currency = language, currency
            self.campaign = SimpleNamespace(
                **{
                    'campaign_name': campaign_name,
                    'title': '',
                    'language': language,
                    'currency': currency,
                    'description': '',
                    'category': SimpleNamespace(),
                }
            )

            self.set_categories_from_directories()
            self.campaign_ai = copy.copy(
                self.campaign
            )  # <- паралельно создаю ai кампанию
            self.campaign_ai_file_name = f'{language}_{currency}_AI_{gs.now}.json'
            for category_name in self.campaign.category.__dict__:
                self.process_category_products(category_name)

                self.process_ai_category(category_name)
                j_dumps(
                    self.campaign_ai,
                    self.base_path / f'{self.language}_{self.currency}.json',
                )  # <- в вновь созданный файл категорий

    def process_ai_category(self, category_name: Optional[str] = None) -> None:
        """Обрабатывает AI данные для указанной категории или всех категорий.

        Args:
            category_name (Optional[str]): Название категории для обработки. Если не указано, обрабатываются все категории.

        Flowchart:
            ┌──────────────────────────────────────────────┐
            │ Start                                        │
            └──────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Load system instructions from JSON file       │
            └───────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Initialize AI model with system instructions  │
            └───────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Check if `category_name` is provided          │
            └───────────────────────────────────────────────┘
                                │
                ┌─────────────────┴───────────────────┐
                │                                     │
                ▼                                     ▼
        ┌─────────────────────────────────────┐   ┌────────────────────────────────────┐
        │ Process specified category          │   │ Iterate over all categories        │
        │ - Load product titles               │   │ - Call `_process_category`         │
        │ - Generate prompt                   │   │   for each category                │
        │ - Get response from AI model        │   └────────────────────────────────────┘
        │ - Update or add category            │
        └─────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Save updated campaign data to file            │
            └───────────────────────────────────────────────┘
                                │
                                ▼
            ┌──────────────────────────────────────────────┐
            │ End                                          │
            └──────────────────────────────────────────────┘
        """
        campaign_ai = copy.copy(self.campaign)

        def _process_category(category_name: str) -> None:
            """Обрабатывает AI данные категории и обновляет кампанию."""
            titles_path: Path = (
                self.base_path
                / 'category'
                / category_name
                / f'{campaign_ai.language}_{campaign_ai.currency}'
                / 'product_titles.txt'
            )
            product_titles = read_text_file(titles_path, as_list=True)
            prompt = f'language={campaign_ai.language}\\n{category_name=}\\n{product_titles=}'

            if not self.gemini:# or not self.openai:
                self._models_payload()

            def get_response(_attempts: int = 5) -> str:
                """Получает ответ от AI модели."""
                # return [self.gemini.ask(prompt), self.openai.ask(prompt)]
                # gemini_response, openai_response = self.gemini.ask(prompt), self.openai.ask(prompt)
                return self.gemini.ask(prompt)
                ...

            response = get_response()
            if not response:
                return

            try:
                res_ns: SimpleNamespace = j_loads_ns(response)  # <- превращаю ответ машины в объект SimpleNamespace
                if hasattr(campaign_ai.category, category_name):
                    current_category = getattr(campaign_ai.category, category_name)
                    nested_category_ns = getattr(res_ns, category_name)
                    for key, value in vars(nested_category_ns).items():
                        setattr(current_category, key, value)
                    logger.debug(f'Category {category_name=} updated')
                else:
                    setattr(campaign_ai.category, category_name, res_ns)
                    logger.debug(f'Category {category_name=} created')
            except Exception as ex:
                logger.error(f'Error updating campaign for {category_name=}: {ex}', exc_info=True)
                ...

        # if category_name:
        #     if not _process_category(category_name):
        #         return
        # else:
        #     for category_name in vars(campaign_ai.category).keys():
        #         _process_category(category_name)

        for category_name in vars(campaign_ai.category).keys():
            _process_category(category_name)

        j_dumps(campaign_ai, self.base_path / 'ai' / f'gemini_{gs.now}_{self.language}_{self.currency}.json')
        return

    def process_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Обрабатывает продукты в указанной категории.

        Args:
            category_name (str): Название категории.

        Returns:
            Optional[List[SimpleNamespace]]: Список объектов `SimpleNamespace`, представляющих продукты.
                                            Возвращает `None`, если продукты не найдены.

        Notes:
            Функция пытается прочитать ID продуктов из HTML файлов и текстовых файлов в директории `sources` указанной категории.
            Если ID продуктов не найдены, регистрируется ошибка и функция возвращает `None`.
            Если партнерские продукты найдены, они возвращаются; иначе регистрируется ошибка и функция возвращает `None`.

        Flowchart:
        ┌───────────────────────────────────────────────────────────┐
        │ Start                                                     │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ Call `read_sources(category_name)` to get product IDs     │
        │ - Searches for product IDs in HTML files and sources.txt  │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ Check if `prod_ids` is empty                              │
        │ - If empty, log an error and return `None`                │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ Initialize `AliAffiliatedProducts` with `language`        │
        │ and `currency`                                            │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ Call `process_affiliate_products`                         │
        │ - Pass `campaign`, `category_name`, and `prod_ids`        │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ Check if `affiliated_products` is empty                   │
        │ - If empty, log an error and return `None`                │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ Return `affiliated_products`                              │
        └───────────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────────────────────────────────┐
        │ End                                                       │
        └───────────────────────────────────────────────────────────┘
        """

        def read_sources(category_name: str) -> Optional[List[str]]:
            """Читает источники продуктов и извлекает ID продуктов.

            Args:
                category_name (str): Название категории.

            Returns:
                Optional[List[str]]: Список ID продуктов, если найдены; иначе `None`.

            Notes:
                Эта функция ищет ID продуктов в HTML файлах и файле `sources.txt`, расположенных
                в директории `sources` категории. Если ID продуктов не найдены, возвращает `None`.
            """
            product_ids = []
            html_files = get_filenames(
                self.base_path / 'category' / category_name / 'sources',
                extensions='.html',
                exc_info=False,
            )
            if html_files:
                product_ids.extend(extract_prod_ids(html_files))
            product_urls = read_text_file(
                self.base_path / 'category' / category_name / 'sources.txt',
                as_list=True,
                exc_info=False,
            )

            if product_urls:
                _ = extract_prod_ids(product_urls)
                product_ids.extend(_)
            if not product_ids:
                return

            return product_ids

        prod_ids = read_sources(category_name)

        if not prod_ids:
            logger.error(
                f'No products found in category {category_name}/{self.language}_{self.currency}.',
                exc_info=False,
            )
            ...
            return

        promo_generator = AliAffiliatedProducts(language=self.language, currency=self.currency)

        return asyncio.run(
            promo_generator.process_affiliate_products(
                prod_ids=prod_ids,
                category_root=self.base_path / 'category' / category_name,
            )
        )

    def dump_category_products_files(
        self, category_name: str, products: List[SimpleNamespace]
    ) -> None:
        """Сохраняет данные о товарах в JSON файлы.

        Args:
            category_name (str): Имя категории.
            products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.
        """
        if not products:
            logger.warning('No products to save.')
            return

        category_path = Path(self.base_path / 'category' / category_name)
        for product in products:
            product_id = getattr(product, 'product_id', None)
            if not product_id:
                logger.warning(f'Skipping product without product_id: {product}')
                continue
            j_dumps(product, category_path / f'{product_id}.json')

    def set_categories_from_directories(self) -> None:
        """Устанавливает категории рекламной кампании из названий директорий в `category`.

        Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
        `category_name`, `title` и `description`.
        """
        category_dirs = self.base_path / 'category'
        categories = get_directory_names(category_dirs)

        # Ensure that self.campaign.category is an object of SimpleNamespace
        if not hasattr(self.campaign, 'category'):
            self.campaign.category = SimpleNamespace()

        # Add each category as an attribute to the campaign's category SimpleNamespace
        for category_name in categories:
            setattr(
                self.campaign.category,
                category_name,
                SimpleNamespace(category_name=category_name, title='', description=''),
            )

    async def generate_output(
        self,
        campaign_name: str,
        category_path: str | Path,
        products_list: list[SimpleNamespace] | SimpleNamespace,
    ) -> None:
        """Сохраняет данные о товарах в различных форматах.

        - `<product_id>.json`: Содержит все параметры продукта, один файл на продукт.
        - `ai_{timestamp}.json`: Общий файл для всех продуктов с определенными ключами.
        - `promotion_links.txt`: Список ссылок на продукты, создается в функции `save_promotion_links()`.
        - `category_products_titles.json`: Файл, содержащий заголовок, `product_id`, `first_category_name` и `second_category_name` каждого продукта в категории.
        """
        timestamp = time.strftime('%Y-%m-%d %H%M%S')
        products_list = products_list if isinstance(products_list, list) else [products_list]
        _data_for_openai: dict = {}
        _promotion_links_list: list = []
        _product_titles: list = []

        for product in products_list:
            # Adding the categories_convertor dictionary
            categories_convertor = {
                str(product.first_level_category_id): {
                    'ali_category_name': product.first_level_category_name,
                    'ali_parent': '',
                    'PrestaShop_categories': [],
                    'PrestaShop_main_category': '',
                },
                str(product.second_level_category_id): {
                    'ali_category_name': product.second_level_category_name,
                    'ali_parent': str(product.first_level_category_id),
                    'PrestaShop_categories': [],
                    'PrestaShop_main_category': '',
                },
            }
            product.categories_convertor = categories_convertor

            # Save individual product JSON
            j_dumps(
                product,
                Path(category_path / f'{self.language}_{self.currency}' / f'{product.product_id}.json'),
                exc_info=False,
            )
            _product_titles.append(product.product_title)
            _promotion_links_list.append(product.promotion_link)

        await self.save_product_titles(product_titles=_product_titles, category_path=category_path)
        await self.save_promotion_links(
            promotion_links=_promotion_links_list, category_path=category_path
        )
        await self.generate_html(
            campaign_name=campaign_name, category_path=category_path, products_list=products_list
        )

    async def generate_html(
        self,
        campaign_name: str,
        category_path: str | Path,
        products_list: list[SimpleNamespace] | SimpleNamespace,
    ) -> None:
        """Создает HTML файл для категории и корневой индексный файл.

        Args:
            products_list: Список продуктов для включения в HTML.
            category_path: Путь для сохранения HTML файла.
        """
        products_list = products_list if isinstance(products_list, list) else [products_list]

        category_name = Path(category_path).name
        category_html_path: Path = Path(category_path) / f'{self.language}_{self.currency}' / f'{category_name}.html'

        # Initialize the category dictionary to store product titles
        category = {'products_titles': []}

        html_content = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{category_name} Products</title>
        <link rel="stylesheet" href="styles.css">
        </head>
        <body>
        <h1>{category_name} Products</h1>
        <div class="product-grid">
        """

        for product in products_list:
            # Add the product's details to the category's products_titles
            category['products_titles'].append(
                {
                    'title': product.product_title,
                    'product_id': product.product_id,
                    'first_category_name': product.first_level_category_name,
                    'second_category_name': product.second_level_category_name,
                }
            )

            html_content += f"""
            <div class="product-card">
            <img src="{product.local_image_path}" alt="{html.escape(product.product_title)}" class="product-image">
            <div class="product-info">
            <h2 class="product-title">{html.escape(product.product_title)}</h2>
            <p class="product-price">{product.target_sale_price} {product.target_sale_price_currency}</p>
            <p class="product-original-price">{product.target_original_price} {product.target_original_price_currency}</p>
            <p class="product-category">Category: {product.second_level_category_name}</p>
            <a href="{product.promotion_link}" class="product-link">Buy Now</a>
            </div>
            </div>
            """

        html_content += """
        </div>
        </body>
        </html>
        """

        # Save the HTML content
        save_text_file(html_content, category_html_path)

        ...
        # Generate the main index.html file
        campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name
        campaign_path.mkdir(parents=True, exist_ok=True)
        index_html_path = campaign_path / 'index.html'

        # Collect all category links
        category_links = []
        categories = get_directory_names(campaign_path / 'category')
        for _category_path in categories:
            category_name = Path(_category_path).name
            category_link = f'{category_name}/{category_name}.html'
            category_links.append(f"<li><a href='{category_link}'>{html.escape(category_name)}</a></li>")

        index_html_content = fr"""<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Categories</title>
        <link rel="stylesheet" href="styles.css">
        </head>
        <body>
        <h1>Product Categories</h1>
        <ul>
        { "".join(category_links) }
        </ul>
        </body>
        </html>
        """

        save_text_file(index_html_content, index_html_path)

    def generate_html_for_campaign(self, campaign_name: str) -> None:
        """Генерирует HTML страницы для рекламной кампании.

        Args:
            campaign_name (str): Имя рекламной кампании.
        """
        campaign_root = Path(gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name)
        categories = get_filenames(campaign_root / 'category', extensions='')

        # Генерация HTML страниц для каждой категории
        for category_name in categories:
            category_path = campaign_root / 'category' / category_name
            products = self.get_category_products(category_name=category_name)

            if products:
                # Генерация страниц для каждого товара
                for product in products:
                    ProductHTMLGenerator.set_product_html(product, category_path)

                # Генерация страницы категории
                CategoryHTMLGenerator.set_category_html(products, category_path)
            else:
                logger.warning(f'No products found for category {category_name}.')

        # Генерация страницы рекламной кампании
        CampaignHTMLGenerator.set_campaign_html(categories, campaign_root)