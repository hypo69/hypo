# Анализ кода модуля `ali_promo_campaign.py`

**Качество кода: 6/10**

-   **Плюсы:**
    *   Модульная структура: Код разбит на классы и функции, что облегчает понимание и поддержку.
    *   Использование `SimpleNamespace`: Удобно для представления данных.
    *   Применение `asyncio` для асинхронных операций: Потенциал для повышения производительности.
    *   Использование `logger`: Логирование событий, ошибок и отладочной информации.
    *   Наличие docstring для классов и методов: Понимание функциональности кода.
    *   Разделение на генерацию HTML, обработку AI и продуктов.
-   **Минусы:**
    *   Непоследовательное использование кавычек: В коде используются как двойные, так и одинарные кавычки.
    *   Избыточные импорты: Некоторые импорты повторяются или не используются.
    *   Отсутствие проверок типов: В некоторых функциях отсутствуют явные проверки типов, что может привести к ошибкам.
    *   Смешение логики: Некоторые функции выполняют несколько задач, что может усложнить понимание и тестирование.
    *   Неполное использование `try-except`: Предпочтительнее использовать `logger.error` для обработки ошибок.
    *   Дублирование кода: Например, в `process_ai_category` и в других местах.
    *   Не всегда ясные названия переменных и функций:  Некоторые названия можно сделать более выразительными.
    *   Непоследовательная документация: Присутствуют как подробные описания, так и недостаток документации.
    *   Смешение ответственности: Некоторые функции отвечают за несколько задач, что усложняет тестирование и поддержку.
    *   Отсутствие единого подхода к обработке ошибок.

**Рекомендации по улучшению**

1.  **Унификация кавычек**: Заменить двойные кавычки на одинарные в коде Python, оставить двойные только для вывода и логирования.
2.  **Удаление лишних импортов**: Убрать дублирующиеся и неиспользуемые импорты.
3.  **Добавление проверок типов**: Добавить проверки типов там, где это необходимо.
4.  **Разделение функций**: Разделить функции, выполняющие несколько задач, на более мелкие и специализированные.
5.  **Использование `logger.error`**: Заменить `try-except` на `logger.error` для обработки ошибок.
6.  **Рефакторинг**: Устранить дублирование кода, например, в функции `process_ai_category`.
7.  **Переименование переменных и функций**: Сделать имена более выразительными и понятными.
8.  **Улучшение документации**: Добавить недостающую документацию, привести документацию в соответствие со стандартами.
9.  **Обработка ошибок**: Унифицировать подход к обработке ошибок, избегать использования `...` в коде.
10. **Добавить описание модуля**:  Добавить описание модуля в начале файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для управления рекламными кампаниями AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliPromoCampaign`, который используется для управления рекламными кампаниями на платформе AliExpress.
Он позволяет обрабатывать данные о категориях и товарах, создавать и редактировать JSON-файлы с информацией о кампаниях,
а также использовать AI для генерации данных о кампаниях.

Класс `AliPromoCampaign` поддерживает загрузку и обработку данных рекламных кампаний, управление категориями и товарами,
а также использование ИИ для генерации описаний и других данных. Модуль поддерживает различные языки и валюты,
обеспечивая гибкость в настройке кампаний.

Пример использования
--------------------

Пример инициализации рекламной кампании:

.. code-block:: python

    campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    print(campaign.campaign_name)

Пример обработки всей кампании:

.. code-block:: python

    campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    campaign.process_campaign()

Пример обработки данных о товарах в категории:

.. code-block:: python

    campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    products = campaign.process_category_products('electronics')

Пример заполнения данных категорий с использованием AI:

.. code-block:: python

    campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    campaign.process_ai_category('Electronics')
"""
import asyncio
import copy
import html
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from types import SimpleNamespace

from src import gs
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils import locales
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel

# from src.suppliers.aliexpress.campaign.html_generators import (
#     ProductHTMLGenerator,
#     CategoryHTMLGenerator,
#     CampaignHTMLGenerator,
# )
from src.logger.logger import logger
from src.utils.file_async import (
    read_text_file,
    get_filenames_from_directory,
    get_directory_names,
)
from src.utils.jjson import j_dumps, j_loads_ns, j_loads
# from src.utils.convertors.csv import csv2dict
from src.utils.file import save_text_file
from src.utils.printer import pprint

from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids


class AliPromoCampaign:
    """Управление рекламной кампанией."""

    language: str = None
    currency: str = None
    base_path: Path = None
    campaign_name: str = None
    campaign: SimpleNamespace = None
    campaign_ai: SimpleNamespace = None
    gemini: GoogleGenerativeAI = None
    openai: OpenAIModel = None

    def __init__(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
        model: str = 'openai'
    ):
        """Инициализация объекта AliPromoCampaign для рекламной кампании.

        Args:
            campaign_name (str): Название кампании.
            language (Optional[str]): Язык, используемый в кампании.
            currency (Optional[str]): Валюта, используемая в кампании.
            model (str): Модель ИИ для использования.

        Returns:
            None

        Example:
            >>> campaign = AliPromoCampaign(campaign_name='SummerSale', language='EN', currency='USD')
            >>> print(campaign.campaign_name)
        """
        self.base_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name
        campaign_file_path = self.base_path / f'{language}_{currency}.json'
        self.campaign = j_loads_ns(
            campaign_file_path, exc_info=False
        )  # Файл может отсутствовать, если это новая рекламная кампания
        if not self.campaign:
            logger.warning(
                f'Campaign file not found at {campaign_file_path=}\\nStart as new \\n (Start build JSON file, categories, products etc.)'
            )
            # Если в корне рекламной кампании нет файла JSON, запускается процесс создания новой рекламной кампании
            # Создадутся категории из названий директорий в директории `category`,
            # соберутся affiliated товары в файлы <product_id>.JSON,
            # сгенерируются ai параметры
            self.process_new_campaign(
                campaign_name=campaign_name, language=language, currency=currency
            )
            return

        if self.campaign.language and self.campaign.currency:
            self.language, self.currency = (
                self.campaign.language,
                self.campaign.currency,
            )
        else:
            self.language, self.currency = language, currency
        self._models_payload()

    def _models_payload(self):
        """Инициализация моделей ИИ для использования в кампании."""
        system_instruction_path = gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'
        system_instruction: str = read_text_file(system_instruction_path)
        self.gemini = GoogleGenerativeAI(system_instruction=system_instruction)
        # TODO: Вынести assistant_id в настройки
        assistant_id = 'asst_dr5AgQnhhhnef5OSMzQ9zdk9'
        # self.openai = OpenAIModel(system_instruction=system_instruction, assistant_id=assistant_id)

    def process_campaign(self):
        """Итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

        Example:
            >>> campaign.process_campaign()
        """
        categories_names_list = get_directory_names(self.base_path / 'category')
        for category_name in categories_names_list:
            logger.info(f'Starting {category_name=}')
            self.process_category_products(category_name)
            logger.info(f'Starting AI category {category_name=}')
            self.process_ai_category(category_name)

    def process_campaign_category(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Обрабатывает определенную категорию в кампании для всех языков и валют.

        Args:
            category_name (str): Категория для обработки.

        Returns:
             Optional[List[SimpleNamespace]]: Список товаров в категории.
        """
        self.process_category_products(category_name=category_name)
        self.process_ai_category(category_name=category_name)

    def process_new_campaign(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
    ):
        """Создает новую рекламную кампанию.

        Условия для создания кампании:
            - директория кампании с питоник названием
            - вложенная директория `campaign`, в ней директории с питоник названиями категорий
            - файл sources.txt и/или директория `sources` с файлами `<product_id>.html`

        Args:
            campaign_name (Optional[str]): Название рекламной кампании.
            language (Optional[str]): Язык для кампании.
            currency (Optional[str]): Валюта для кампании.

        Returns:
            None

        Example:
             >>> campaign.process_new_campaign(campaign_name='HolidaySale', language='RU', currency='ILS')

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
            │currency}`                   │   │     "EN": "USD",                     │
            │                             │   │     "HE": "ILS",                     │
            │                             │   │     "RU": "ILS"                      │
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
            )  # Параллельно создаю ai кампанию
            self.campaign_ai_file_name = f'{language}_{currency}_AI_{gs.now}.json'
            for category_name in self.campaign.category.__dict__:
                self.process_category_products(category_name)
                self.process_ai_category(category_name)
                j_dumps(
                    self.campaign_ai,
                    self.base_path / f'{self.language}_{self.currency}.json',
                    exc_info=False
                )  # Вновь созданный файл категорий

    def process_ai_category(self, category_name: Optional[str] = None):
        """Обрабатывает AI данные для указанной категории или для всех категорий.

        Args:
            category_name (Optional[str]): Имя категории для обработки.
            Если не указано, обрабатываются все категории.

        Returns:
            None

        Example:
            >>> campaign.process_ai_category('Electronics')
            >>> campaign.process_ai_category()

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

        def _process_category(category_name: str):
            """Обрабатывает AI данные для категории и обновляет данные в кампании."""
            titles_path: Path = (
                self.base_path
                / 'category'
                / category_name
                / f'{campaign_ai.language}_{campaign_ai.currency}'
                / 'product_titles.txt'
            )
            product_titles = read_text_file(titles_path, as_list=True)
            prompt = f'language={campaign_ai.language}\\n{category_name=}\\n{product_titles=}'

            if not self.gemini or not self.openai:
                self._models_payload()

            def get_response(_attempts: int = 5):
                """Получает ответ от модели AI."""
                # return [self.gemini.ask(prompt), self.openai.ask(prompt)]
                return self.gemini.ask(prompt)

            response = get_response()
            if not response:
                return
            try:
                res_ns: SimpleNamespace = j_loads_ns(response)
                if hasattr(campaign_ai.category, category_name):
                    current_category = getattr(campaign_ai.category, category_name)
                    nested_category_ns = getattr(res_ns, category_name)
                    for key, value in vars(nested_category_ns).items():
                        setattr(current_category, key, fix_json_string(value))
                    logger.debug(f'Category {category_name=} updated', None, False)
                else:
                    setattr(campaign_ai.category, category_name, res_ns)
                    logger.debug(f'Category {category_name=} created')
            except Exception as ex:
                logger.error(f'Error updating campaign for {category_name=}: ', ex, exc_info=False)

        for category_name in vars(campaign_ai.category).keys():
            _process_category(category_name)

        j_dumps(campaign_ai, self.base_path / 'ai' / f'gemini_{gs.now}_{self.language}_{self.currency}.json', exc_info=False)
        return

    def process_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Обрабатывает товары в указанной категории.

        Args:
            category_name (str): Название категории.

        Returns:
             Optional[List[SimpleNamespace]]: Список товаров в виде объектов SimpleNamespace.

        Example:
            >>> products = campaign.process_category_products('Electronics')
            >>> print(len(products))
            20
            >>> for product in products:
            >>>     pprint(product)

        Notes:
            Функция пытается извлечь ID товаров из HTML-файлов и текстовых файлов в директории `sources` указанной категории.
            Если ID товаров не найдены, в лог записывается ошибка и возвращается `None`.
            Если партнерские продукты найдены, они возвращаются, иначе в лог записывается ошибка и возвращается `None`.

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
                Optional[List[str]]: Список ID продуктов или `None`, если не найдены.

            Example:
                 >>> product_ids = read_sources('Electronics')
                 >>> print(product_ids)
                ['12345', '67890', ...]

            Notes:
                Функция ищет ID товаров в HTML файлах и в файле `sources.txt`, расположенном
                в директории `sources` для указанной категории. Если ID товаров не найдены, возвращается `None`.
            """
            product_ids = []
            html_files = get_filenames_from_directory(
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
            return

        promo_generator = AliAffiliatedProducts(
            language=self.language, currency=self.currency
        )

        return asyncio.run(
            promo_generator.process_affiliate_products(
                prod_ids=prod_ids,
                category_root=self.base_path
                / 'category'
                / category_name,
            )
        )

    def dump_category_products_files(
        self, category_name: str, products: List[SimpleNamespace]
    ):
        """Сохраняет данные о товарах в JSON файлы.

        Args:
            category_name (str): Имя категории.
            products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

        Returns:
            None

        Example:
             >>> campaign.dump_category_products_files('Electronics', products)
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
            j_dumps(product, category_path / f'{product_id}.json', exc_info=False)

    def set_categories_from_directories(self):
        """Устанавливает категории рекламной кампании из названий директорий в `category`.

        Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
        `category_name`, `title`, и `description`.

        Returns:
            None

        Example:
             >>> self.set_categories_from_directories()
             >>> print(self.campaign.category.category1.category_name)
        """
        category_dirs = self.base_path / 'category'
        categories = get_directory_names(category_dirs)

        if not hasattr(self.campaign, 'category'):
            self.campaign.category = SimpleNamespace()

        for category_name in categories:
            setattr(
                self.campaign.category,
                category_name,
                SimpleNamespace(category_name=category_name, title='', description=''),
            )

    async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """Сохраняет данные о товарах в различных форматах.

        - `<product_id>.json`: Содержит все параметры товара, один файл на товар.
        - `ai_{timestamp}.json`: Общий файл для всех товаров с определенными ключами.
        - `promotion_links.txt`: Список ссылок на товары, создается в функции `save_promotion_links()`.
        - `category_products_titles.json`: Файл, содержащий название, `product_id`, `first_category_name` и `second_category_name` каждого товара в категории.

        Args:
            campaign_name (str): Название кампании для выходных файлов.
            category_path (str | Path): Путь для сохранения выходных файлов.
            products_list (list[SimpleNamespace] | SimpleNamespace): Список товаров или один товар для сохранения.

        Returns:
            None

        Example:
            >>> products_list: list[SimpleNamespace] = [
            ...     SimpleNamespace(product_id="123", product_title="Product A", promotion_link="http://example.com/product_a",
            ...                     first_level_category_id=1, first_level_category_name="Category1",
            ...                     second_level_category_id=2, second_level_category_name="Subcategory1",
            ...                     product_main_image_url="http://example.com/image.png", product_video_url="http://example.com/video.mp4"),
            ...     SimpleNamespace(product_id="124", product_title="Product B", promotion_link="http://example.com/product_b",
            ...                     first_level_category_id=1, first_level_category_name="Category1",
            ...                     second_level_category_id=3, second_level_category_name="Subcategory2",
            ...                     product_main_image_url="http://example.com/image2.png", product_video_url="http://example.com/video2.mp4")
            ... ]
            >>> category_path: Path = Path("/path/to/category")
            >>> await generate_output("CampaignName", category_path, products_list)

        Flowchart:
            ┌───────────────────────────────┐
            │  Start `generate_output`      │
            └───────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────────────┐
            │ Format `timestamp` for file   │
            │ names.                        │
            └───────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────────────┐
            │ Check if `products_list` is   │
            │ a list; if not, convert it to │
            │ a list.                       │
            └───────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │ Initialize `_data_for_openai`,│
        │ `_promotion_links_list`, and  │
        │ `_product_titles` lists.      │
        └───────────────────────────────┘
                        │
                        ▼
    ┌─────────────────────────────────────────┐
    │ For each `product` in `products_list`:  │
    └─────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 1. Create `categories_convertor` dictionary   │
    │ for `product`.                                │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 2. Add `categories_convertor` to `product`.   │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 3. Save `product` as `<product_id>.json`.     │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 4. Append `product_title` and                 │
    │ `promotion_link` to their respective lists.   │
    └───────────────────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │ Call `save_product_titles`    │
        │ with `_product_titles` and    │
        │ `category_path`.              │
        └───────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │ Call `save_promotion_links`   │
        │ with `_promotion_links_list`  │
        │ and `category_path`.          │
        └───────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │ Call `generate_html` with         │
        │ `campaign_name`, `category_path`, │
        │ and `products_list`.              │
        └───────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │  End `generate_output`        │
        └───────────────────────────────┘

        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H%M%S')
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
                    'PrestaShop_main_category': ''
                },
                str(product.second_level_category_id): {
                    'ali_category_name': product.second_level_category_name,
                    'ali_parent': str(product.first_level_category_id),
                    'PrestaShop_categories': [],
                    'PrestaShop_main_category': ''
                }
            }
            setattr(product, 'categories_convertor', categories_convertor)

            # Save individual product JSON
            j_dumps(product, Path(category_path / f'{self.language}_{self.currency}' / f'{product.product_id}.json'), exc_info=False)
            _product_titles.append(product.product_title)
            _promotion_links_list.append(product.promotion_link)
        await self.save_product_titles(product_titles=_product_titles, category_path=category_path)
        await self.save_promotion_links(promotion_links=_promotion_links_list, category_path=category_path)
        await self.generate_html(campaign_name=campaign_name, category_path=category_path, products_list=products_list)


    async def generate_html(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """Создает HTML файл для категории и корневой индексный файл.

        Args:
            products_list (list[SimpleNamespace] | SimpleNamespace): Список товаров для включения в HTML.
            category_path (str | Path): Путь для сохранения HTML файла.

        Returns:
            None
        """
        products_list = products_list if isinstance(products_list, list) else [products_list]
        category_name = Path(category_path).name
        category_html_path: Path = Path(category_path) / f'{self.language}_{self.currency}' / f'{category_name}.html'

        # Initialize the category dictionary to store product titles
        category = {
            'products_titles': []
        }

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
            category['products_titles'].append({
                'title': product.product_title,
                'product_id': product.product_id,
                'first_category_name': product.first_level_category_name,
                'second_category_name': product.second_level_category_name
            })

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