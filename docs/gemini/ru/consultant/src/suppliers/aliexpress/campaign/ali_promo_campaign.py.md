# Анализ кода модуля `ali_promo_campaign.py`

**Качество кода**
8/10
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используется `SimpleNamespace` для хранения данных.
    - Есть базовая документация в виде docstring.
    - Присутствует логирование с помощью `logger`.
    - Используется `j_loads_ns` и `j_dumps` для работы с JSON.
- Минусы
    - Не все функции и методы имеют подробные комментарии в формате RST.
    - Некоторые комментарии после `#` не соответствуют стандарту reStructuredText (RST).
    - Избыточное использование `try-except` блоков в некоторых местах.
    - Не везде используется `logger.error` для обработки ошибок.
    - Присутствует дублирование импорта `header`.
    - Нарушение PEP8 в наименовании переменных.
    - Не везде корректно реализована обработка ошибок при работе с файлами.
    - Отсутствует обработка `async` функций в некоторых методах.

**Рекомендации по улучшению**

1.  **Документация**:
    - Дополнить docstring для всех функций, методов и классов в формате RST, включая описание параметров, возвращаемых значений и возможных исключений.
    - Переписать все комментарии после `#` в формате RST, объясняя назначение следующего блока кода.
2.  **Импорты**:
    - Удалить дублирование импорта `header`.
    - Проверить и добавить отсутствующие импорты, если это необходимо.
    - Сгруппировать импорты по категориям.
3.  **Обработка ошибок**:
    - Заменить избыточные `try-except` блоки на использование `logger.error` для логирования ошибок.
    - Добавить проверку на существование файлов перед их чтением.
4.  **Логирование**:
    - Убедиться, что все ошибки и предупреждения регистрируются с помощью `logger.error` и `logger.warning`.
    - Включить более подробные сообщения об ошибках, чтобы упростить отладку.
5.  **Код**:
    - Привести имена переменных в соответствие с PEP8 (например, `_l` переименовать в `locales_list`).
    - Разделить большие функции на более мелкие, чтобы улучшить читаемость.
    - Избавиться от использования `...` в коде, если это не является точкой остановки.
    - Заменить конструкции `if not x: return` на `if not x: ... return`
    - Заменить конструкцию `if x: ... else: ...` на `if x: ...` и отдельно `if not x: ...`
6.  **Асинхронность**:
    -  Использовать `async` и `await` для всех функций, которые взаимодействуют с `async` функциями (например, `process_affiliate_products`).
    - Использовать `asyncio.run()` в методах, вызывающих асинхронные функции.
7.  **Стиль кода**:
    - Придерживаться единого стиля кавычек (одинарные `''` или двойные `""`) в коде и комментариях.
    - Использовать f-строки для форматирования строк.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления рекламными кампаниями на AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliPromoCampaign`, который используется для управления рекламными
кампаниями на платформе AliExpress. Он включает в себя функциональность для обработки данных
о категориях и товарах, создания и редактирования JSON-файлов с информацией о кампаниях,
а также использование AI для генерации данных о кампаниях.

Пример использования
--------------------

Пример инициализации рекламной кампании:

.. code-block:: python

    campaign = AliPromoCampaign("new_campaign", "EN", "USD")
    print(campaign.campaign_name)

Пример обработки всей кампании:

.. code-block:: python

    campaign = AliPromoCampaign("new_campaign", "EN", "USD")
    campaign.process_campaign()

Пример обработки данных о товарах в категории:

.. code-block:: python

    campaign = AliPromoCampaign("new_campaign", "EN", "USD")
    products = campaign.process_category_products("electronics")

Пример заполнения данных категорий с использованием AI:

.. code-block:: python

    campaign = AliPromoCampaign("new_campaign", "EN", "USD")
    campaign.process_ai_category("Electronics")
"""
MODE = 'dev'
import asyncio
import copy
import html
import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional, Dict
import header # <- импорт есть, не убираю
from src import gs
from src.suppliers.aliexpress import campaign
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils import locales
from src.ai import GoogleGenerativeAI, OpenAIModel
from src.suppliers.aliexpress.campaign.html_generators import (
    ProductHTMLGenerator,
    CategoryHTMLGenerator,
    CampaignHTMLGenerator,
)
from src.logger.logger import logger

from src.utils.file import get_filenames, read_text_file, get_directory_names
from src.utils.jjson import j_dumps, j_loads_ns, j_loads
from src.utils.convertors.csv import csv2dict
from src.utils.file import save_text_file
from src.utils.printer import pprint

from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.logger.logger import logger


class AliPromoCampaign:
    """
    Управляет рекламной кампанией, включая загрузку, обработку и генерацию данных.

    :ivar language: Язык кампании.
    :vartype language: str
    :ivar currency: Валюта кампании.
    :vartype currency: str
    :ivar base_path: Базовый путь к файлам кампании.
    :vartype base_path: Path
    :ivar campaign_name: Название кампании.
    :vartype campaign_name: str
    :ivar campaign: Объект SimpleNamespace с данными кампании.
    :vartype campaign: SimpleNamespace
    :ivar campaign_ai: Объект SimpleNamespace с данными AI кампании.
    :vartype campaign_ai: SimpleNamespace
    :ivar gemini: Объект GoogleGenerativeAI для работы с Gemini.
    :vartype gemini: GoogleGenerativeAI
    :ivar openai: Объект OpenAIModel для работы с OpenAI.
    :vartype openai: OpenAIModel
    """

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
        """
        Инициализирует объект AliPromoCampaign.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык кампании (необязательно).
        :type language: Optional[str]
        :param currency: Валюта кампании (необязательно).
        :type currency: Optional[str]
        :param model: Модель ИИ для использования (необязательно).
        :type model: str

        :raises FileNotFoundError: Если файл кампании не найден и не создается новая кампания.

        :Example:
            >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
            >>> print(campaign.campaign_name)
        """
        # Установка базового пути для кампании
        self.base_path = gs.path.google_drive / "aliexpress" / "campaigns" / campaign_name
        # Формирование пути к файлу кампании
        campaign_file_path = self.base_path / f"{language}_{currency}.json"
        # Пытаемся загрузить файл кампании, если он существует
        self.campaign = j_loads_ns(
            campaign_file_path, exc_info=False
        )
        # Проверяем, существует ли файл кампании
        if not self.campaign:
            logger.warning(
                f"Campaign file not found at {campaign_file_path=}\\nStart as new \\n (Start build JSON file, categories, products etc.)"
            )
            # Если файл кампании не существует, создается новая кампания
            self.process_new_campaign(
                campaign_name=campaign_name, language=language, currency=currency
            )
            return
        # Если файл кампании существует, устанавливаем язык и валюту
        if self.campaign.language and self.campaign.currency:
            self.language, self.currency = (
                self.campaign.language,
                self.campaign.currency,
            )
        else:
            self.language, self.currency = language, currency
        # Загрузка моделей ИИ
        self._models_payload()

    def _models_payload(self):
        """
        Загружает и настраивает модели ИИ (Gemini и OpenAI).
        """
        # Формируем путь к файлу системных инструкций
        system_instruction_path = gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'
        # Читаем системные инструкции из файла
        system_instruction: str = read_text_file(system_instruction_path)
        # Инициализируем модель Gemini
        self.gemini = GoogleGenerativeAI(system_instruction=system_instruction)
        # Устанавливаем идентификатор ассистента для OpenAI (TODO: Рассмотреть возможность настройки извне)
        assistant_id = "asst_dr5AgQnhhhnef5OSMzQ9zdk9"
        # Инициализируем модель OpenAI
        #self.openai = OpenAIModel(system_instruction = system_instruction, assistant_id = assistant_id) # TODO:  Рассмотреть возможность использования OpenAI

    def process_campaign(self):
        """
        Итерирует по категориям рекламной кампании и обрабатывает товары, используя генератор партнерских ссылок.

        :Example:
            >>> campaign.process_campaign()
        """
        # Получаем список названий папок категорий
        categories_names_list = get_directory_names(self.base_path / 'category')
        # Итерируем по каждой категории и обрабатываем товары и AI данные
        for category_name in categories_names_list:
            logger.info(f"Starting {category_name=}")
            self.process_category_products(category_name)
            logger.info("Starting AI category")
            self.process_ai_category(category_name)
    
    def process_campaign_category(
        self, category_name: str
    ) -> list[SimpleNamespace] | None:
        """
        Обрабатывает определенную категорию в кампании для всех языков и валют.

        :param category_name: Название категории для обработки.
        :type category_name: str
        :return: Список названий товаров в категории.
        :rtype: list[SimpleNamespace] | None
        """
        # Обрабатываем продукты категории и AI данные
        self.process_category_products(category_name=category_name)
        self.process_ai_category(category_name=category_name)
    
    def process_new_campaign(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
    ):
        """
        Создает новую рекламную кампанию.

        :param campaign_name: Название рекламной кампании.
        :type campaign_name: str
        :param language: Язык для кампании (необязательно).
        :type language: Optional[str]
        :param currency: Валюта для кампании (необязательно).
        :type currency: Optional[str]

        :Example:
            >>> campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")

        :Flowchart:
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
        # Если язык и валюта не указаны, используем все локали
        if not language and not currency:
            locales_list = [(lang, curr) for locale in locales for lang, curr in locale.items()]
        else:
            locales_list = [(language, currency)]

        for language, currency in locales_list:
            self.language, self.currency = language, currency
            self.campaign = SimpleNamespace(
                **{
                    "campaign_name": campaign_name,
                    "title": "",
                    "language": language,
                    "currency": currency,
                    "description": "",
                    "category": SimpleNamespace(),
                }
            )
            self.set_categories_from_directories()
            # Создание копии кампании для AI
            self.campaign_ai = copy.copy(self.campaign)
            self.campaign_ai_file_name = f"{language}_{currency}_AI_{gs.now}.json"
            # Обработка категорий
            for category_name in vars(self.campaign.category).keys():
                self.process_category_products(category_name)
                self.process_ai_category(category_name)
            # Сохранение данных AI
            j_dumps(
                self.campaign_ai,
                self.base_path / f"{self.language}_{self.currency}.json",
            )
    
    def process_ai_category(self, category_name: Optional[str] = None):
        """
        Обрабатывает AI данные для заданной категории или для всех категорий.

        :param category_name: Имя категории для обработки (необязательно).
        :type category_name: Optional[str]

        :Example:
            >>> campaign.process_ai_category("Electronics")
            >>> campaign.process_ai_category()

        :Flowchart:
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
            """
            Обрабатывает AI данные для конкретной категории и обновляет данные кампании.

            :param category_name: Имя категории для обработки.
            :type category_name: str
            """
            # Формируем путь к файлу с названиями продуктов
            titles_path: Path = (
                self.base_path
                / "category"
                / category_name
                / f"{campaign_ai.language}_{campaign_ai.currency}"
                / "product_titles.txt"
            )
            # Читаем названия продуктов из файла
            product_titles = read_text_file(titles_path, as_list=True)
            # Формируем промпт для AI
            prompt = f"language={campaign_ai.language}\\n{category_name=}\\n{product_titles=}"
            # Проверяем инициализированы ли модели
            if not self.gemini or not self.openai:
                self._models_payload()
            
            def get_response(_attempts: int = 5):
                """
                Получает ответ от AI модели.

                :param _attempts: Количество попыток запроса (необязательно).
                :type _attempts: int
                :return: Ответ от AI модели.
                :rtype: str
                """
                # Используем только Gemini
                return self.gemini.ask(prompt)
            
            # Получаем ответ от AI
            response = get_response()
            if not response:
                return
            try:
                # Преобразуем ответ AI в SimpleNamespace
                res_ns: SimpleNamespace = j_loads_ns(response)
                # Обновляем или создаем категорию в campaign_ai
                if hasattr(campaign_ai.category, category_name):
                    current_category = getattr(campaign_ai.category, category_name)
                    nested_category_ns = getattr(res_ns, category_name)
                    for key, value in vars(nested_category_ns).items():
                        setattr(current_category, key, fix_json_string(value))
                    logger.debug(f"Category {category_name=} updated", None, False)
                else:
                    setattr(campaign_ai.category, category_name, res_ns)
                    logger.debug(f"Category {category_name=} created")
            except Exception as ex:
                logger.error(f"Error updating campaign for {category_name=}: ", ex, exc_info=False)

        for category_name in vars(campaign_ai.category).keys():
            _process_category(category_name)
        # Сохраняем обновленные AI данные
        j_dumps(campaign_ai, self.base_path / "ai" / f"gemini_{gs.now}_{self.language}_{self.currency}.json")

    def process_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """
        Обрабатывает продукты в заданной категории.

        :param category_name: Имя категории.
        :type category_name: str
        :return: Список объектов SimpleNamespace, представляющих продукты или None, если продукты не найдены.
        :rtype: Optional[List[SimpleNamespace]]

        :Example:
            >>> products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
            >>> print(len(products))
            20
            >>> for product in products:
            >>>     pprint(product)

        :Flowchart:
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
            """
            Читает источники продуктов и извлекает идентификаторы продуктов.

            :param category_name: Имя категории.
            :type category_name: str
            :return: Список идентификаторов продуктов или None, если идентификаторы не найдены.
            :rtype: Optional[List[str]]

            :Example:
                >>> product_ids: Optional[List[str]] = read_sources("Electronics")
                >>> print(product_ids)
                [\'12345\', \'67890\', ...]
            """
            product_ids = []
            # Получаем список HTML файлов
            html_files = get_filenames(
                self.base_path / "category" / category_name / "sources",
                extensions=".html",
                exc_info=False,
            )
            if html_files:
                product_ids.extend(extract_prod_ids(html_files))
            # Читаем список URL из файла sources.txt
            product_urls = read_text_file(
                self.base_path / "category" / category_name / "sources.txt",
                as_list = True,
                exc_info = False,
            )
            if product_urls:
                product_ids.extend(extract_prod_ids(product_urls))
            if not product_ids:
                return None
            return product_ids
        
        # Читаем источники продуктов
        prod_ids = read_sources(category_name)
        # Проверяем наличие ID продуктов
        if not prod_ids:
            logger.error(
                f"No products found in category {category_name}/{self.language}_{self.currency}.",
                exc_info=False,
            )
            return None
        # Инициализация генератора партнерских ссылок
        promo_generator = AliAffiliatedProducts(
            language = self.language, currency = self.currency
        )
        # Обработка партнерских продуктов
        return asyncio.run(promo_generator.process_affiliate_products(
            prod_ids = prod_ids,
            category_root = self.base_path
            / "category"
            / category_name,
        ))

    def dump_category_products_files(
        self, category_name: str, products: List[SimpleNamespace]
    ):
        """
        Сохраняет данные о товарах в JSON файлы.

        :param category_name: Имя категории.
        :type category_name: str
        :param products: Список объектов SimpleNamespace, представляющих товары.
        :type products: List[SimpleNamespace]

        :Example:
            >>> campaign.dump_category_products_files("Electronics", products)
        """
        if not products:
            logger.warning("No products to save.")
            return
        # Получаем путь к категории
        category_path = Path(self.base_path / "category" / category_name)
        # Сохраняем каждый продукт в отдельный файл JSON
        for product in products:
            product_id = getattr(product, "product_id", None)
            if not product_id:
                logger.warning(f"Skipping product without product_id: {product}")
                continue
            j_dumps(product, category_path / f"{product_id}.json")
    
    def set_categories_from_directories(self):
        """
        Устанавливает категории рекламной кампании из названий директорий в `category`.
        Каждая категория преобразуется в объект SimpleNamespace.

        :Example:
            >>> self.set_categories_from_directories()
            >>> print(self.campaign.category.category1.category_name)
        """
        # Формируем путь к директории с категориями
        category_dirs = self.base_path / "category"
        # Получаем список названий категорий
        categories = get_directory_names(category_dirs)
        # Гарантируем, что self.campaign.category является SimpleNamespace
        if not hasattr(self.campaign, "category"):
            self.campaign.category = SimpleNamespace()
        # Добавляем каждую категорию как атрибут SimpleNamespace
        for category_name in categories:
            setattr(
                self.campaign.category,
                category_name,
                SimpleNamespace(category_name=category_name, title="", description=""),
            )
    
    async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """
        Сохраняет данные о товарах в различных форматах.

        :param campaign_name: Название кампании для выходных файлов.
        :type campaign_name: str
        :param category_path: Путь для сохранения выходных файлов.
        :type category_path: str | Path
        :param products_list: Список товаров или один товар для сохранения.
        :type products_list: list[SimpleNamespace] | SimpleNamespace

        :Example:
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

        :Flowchart:
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
        # Формируем метку времени
        timestamp = datetime.now().strftime("%Y-%m-%d %H%M%S")
        # Гарантируем, что products_list является списком
        products_list = products_list if isinstance(products_list, list) else [products_list]
        _data_for_openai: dict = {}
        _promotion_links_list: list = []
        _product_titles: list = []

        for product in products_list:
            # Формируем словарь categories_convertor
            categories_convertor = {
                str(product.first_level_category_id): {
                    "ali_category_name": product.first_level_category_name,
                    "ali_parent": "",
                    "PrestaShop_categories": [],
                    "PrestaShop_main_category": ""
                },
                str(product.second_level_category_id): {
                    "ali_category_name": product.second_level_category_name,
                    "ali_parent": str(product.first_level_category_id),
                    "PrestaShop_categories": [],
                    "PrestaShop_main_category": ""
                }
            }
            # Добавляем словарь в объект продукта
            product.categories_convertor = categories_convertor
            # Сохраняем данные о продукте
            j_dumps(product, Path(category_path / f"{self.language}_{self.currency}" / f"{product.product_id}.json"), exc_info=False)
            # Добавляем название продукта и ссылку в списки
            _product_titles.append(product.product_title)
            _promotion_links_list.append(product.promotion_link)
        # Сохраняем названия продуктов и ссылки
        await self.save_product_titles(product_titles=_product_titles, category_path=category_path)
        await self.save_promotion_links(promotion_links=_promotion_links_list, category_path=category_path)
        # Генерируем HTML
        await self.generate_html(campaign_name=campaign_name, category_path=category_path, products_list=products_list)

    async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """
        Создает HTML файл для категории и индексный файл для кампании.

        :param products_list: Список продуктов для HTML.
        :type products_list: list[SimpleNamespace] | SimpleNamespace
        :param category_path: Путь для сохранения HTML файла.
        :type category_path: str | Path
        """
        # Гарантируем, что products_list является списком