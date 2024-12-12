## Анализ кода модуля `ali_promo_campaign.py`

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован с использованием классов и функций, что облегчает понимание и поддержку.
    - Присутствует документация в виде docstrings, что помогает разобраться в назначении функций и классов.
    - Используются `SimpleNamespace` для динамического создания объектов.
    - Код использует логирование ошибок, что способствует отладке и мониторингу работы программы.
    - Присутствует обработка исключений, хоть и не всегда оптимальная.
    - Применяются `asyncio` для асинхронных операций.
-  Минусы
    - Не везде используется `j_loads_ns` или `j_loads`, как требуется в инструкции.
    - Некоторые docstring нуждаются в доработке, особенно в части форматирования reStructuredText (RST).
    - Присутствуют избыточные `try-except` блоки, которые можно заменить на логирование ошибок.
    - Не все комментарии соответствуют формату RST.
    - Отсутствуют проверки на наличие необходимых файлов и каталогов перед их использованием.
    - Есть дублирование кода.

**Рекомендации по улучшению**

1.  **Использование `j_loads` и `j_loads_ns`**: Заменить все стандартные `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  **Документация RST**: Переписать все docstrings в формате reStructuredText (RST). Добавить более подробные описания к функциям, методам и классам, включая параметры и возвращаемые значения.
3.  **Логирование ошибок**: Заменить избыточные блоки `try-except` на логирование ошибок через `logger.error`.
4.  **Унификация импортов**: Привести в соответствие импорты с ранее обработанными файлами.
5.  **Обработка ошибок**: Добавить проверки на существование файлов и каталогов перед их использованием.
6.  **Комментарии в коде**: Переписать все комментарии после `#` в соответствии с инструкциями, описывая действия кода.
7.  **Рефакторинг**: Убрать дублирование кода.
8.  **Типизация**: Добавить типы для переменных, где это уместно.
9.  **Улучшить форматирование кода**: Сделать код более читаемым.
10. **Генерация HTML**: Пересмотреть логику генерации HTML, возможно использовать шаблонизатор.

**Оптимизиробанный код**

```python
"""
.. module:: src.suppliers.aliexpress.campaign
   :platform: Windows, Unix
   :synopsis: AliPromoCampaign

Модуль для управления рекламными кампаниями на платформе AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliPromoCampaign`, который управляет рекламными кампаниями на платформе AliExpress,
включая обработку данных о категориях и товарах, создание и редактирование JSON-файлов с информацией о кампаниях,
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
import time
import copy
import html
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional, Dict, Any
from datetime import datetime

from src import gs
from src.suppliers.aliexpress import campaign
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils import locales
from src.ai import GoogleGenerativeAI, OpenAIModel
#from src.suppliers.aliexpress.campaign.html_generators import (
#    ProductHTMLGenerator,
#    CategoryHTMLGenerator,
#    CampaignHTMLGenerator,
#)
from src.logger.logger import logger
from src.utils.file import get_filenames, read_text_file, get_directory_names
from src.utils.jjson import j_dumps, j_loads_ns, j_loads
#from src.utils.convertors.csv import csv2dict
from src.utils.file import save_text_file
from src.utils.printer import pprint
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids

class AliPromoCampaign:
    """
    Управляет рекламными кампаниями на AliExpress.
    =================================================

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
    :ivar campaign_ai: Объект SimpleNamespace с AI-данными кампании.
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
        model:str = 'openai'
    ):
        """
        Инициализация объекта AliPromoCampaign.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык кампании (необязательно).
        :type language: Optional[str]
        :param currency: Валюта кампании (необязательно).
        :type currency: Optional[str]
        :param model: Модель AI для использования.
        :type model: str
        :raises FileNotFoundError: Если файл кампании не найден.

        :Example:
            >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
            >>> print(campaign.campaign_name)
        """
        self.base_path = gs.path.google_drive / "aliexpress" / "campaigns" / campaign_name
        campaign_file_path = self.base_path / f"{language}_{currency}.json"
        # Код загружает данные кампании из JSON файла или начинает создание новой, если файл не найден
        self.campaign = j_loads_ns(campaign_file_path, exc_info=False)
        if not self.campaign:
            logger.warning(
                f"Campaign file not found at {campaign_file_path=}\\nStart as new \\n (Start build JSON file, categories, products etc.)"
            )
            # Код запускает создание новой рекламной кампании, если файл не найден
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
        """
        Инициализирует модели AI (Gemini, OpenAI).

        :return: None
        """
        system_instruction_path = gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'
        system_instruction: str = read_text_file(system_instruction_path)
        self.gemini = GoogleGenerativeAI(system_instruction = system_instruction)
        assistant_id = "asst_dr5AgQnhhhnef5OSMzQ9zdk9" # <-  задача asst_dr5AgQnhhhnef5OSMzQ9zdk9 создание категорий и описаний на основе списка названий товаров
        #self.openai = OpenAIModel(system_instruction = system_instruction, assistant_id = assistant_id)

    def process_campaign(self):
        """
        Итерируется по категориям рекламной кампании и обрабатывает товары категории.

        :return: None

        :Example:
            >>> campaign.process_campaign()
        """
        categories_names_list = get_directory_names(self.base_path / 'category') # читает названия папок категорий
        for category_name in categories_names_list:
            logger.info(f"Starting {category_name=}")
            self.process_category_products(category_name) # Код обрабатывает товары категории
            logger.info(f"Starting AI category")
            self.process_ai_category(category_name) # Код запускает обработку категории с помощью AI


    def process_campaign_category(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """
        Обрабатывает конкретную категорию в рамках кампании для всех языков и валют.

        :param category_name: Название категории.
        :type category_name: str
        :return: Список наименований товаров в категории или None, если товары не найдены
        :rtype: Optional[List[SimpleNamespace]]

        """
        # Код обрабатывает товары категории и запускает обработку AI для категории
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
        :param language: Язык кампании (необязательно).
        :type language: Optional[str]
        :param currency: Валюта кампании (необязательно).
        :type currency: Optional[str]

        :Example:
            >>> campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")
        """
        if not language and not currency:
            # Код обрабатывает все локали, если язык или валюта не указаны
            _l = [(lang, curr) for locale in locales for lang, curr in locale.items()]
        else:
            _l = [(language, currency)]

        for language, currency in _l:
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
            # Код устанавливает категории из директорий
            self.set_categories_from_directories()
            self.campaign_ai = copy.copy(self.campaign)  # Создаётся копия для AI
            self.campaign_ai_file_name = f"{language}_{currency}_AI_{gs.now}.json"
            for category_name in self.campaign.category.__dict__:
                self.process_category_products(category_name) # Код обрабатывает товары для категории
                self.process_ai_category(category_name) # Код запускает обработку категории с помощью AI
                j_dumps(
                    self.campaign_ai,
                    self.base_path / f"{self.language}_{self.currency}.json",
                    exc_info=False
                ) # Сохраняется AI данные кампании в файл


    def process_ai_category(self, category_name: Optional[str] = None):
        """
        Обрабатывает AI-данные для указанной категории или всех категорий.

        :param category_name: Название категории для обработки (необязательно).
        :type category_name: Optional[str]

        :Example:
            >>> campaign.process_ai_category("Electronics")
            >>> campaign.process_ai_category()
        """
        campaign_ai = copy.copy(self.campaign)


        def _process_category(category_name: str):
            """
            Обрабатывает AI-данные для категории и обновляет данные кампании.

            :param category_name: Название категории.
            :type category_name: str
            :return: None
            """
            titles_path: Path = (
                self.base_path
                / "category"
                / category_name
                / f"{campaign_ai.language}_{campaign_ai.currency}"
                / "product_titles.txt"
            )
            product_titles = read_text_file(titles_path, as_list=True)
            prompt = f"language={campaign_ai.language}\\n{category_name=}\\n{product_titles=}"

            if not self.gemini or not self.openai:
                self._models_payload()

            def get_response(_attempts: int = 5) -> Optional[str]:
                """
                 Код получает ответ от AI модели.

                :param _attempts: Количество попыток.
                :type _attempts: int
                :return: Ответ от модели или None
                :rtype: Optional[str]
                """
                return self.gemini.ask(prompt)
                

            response = get_response()
            if not response:
                return
            
            try:
                # Код преобразует ответ AI в объект SimpleNamespace
                res_ns: SimpleNamespace = j_loads_ns(response)
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
            _process_category(category_name) # Код обрабатывает каждую категорию

        # Код сохраняет AI данные кампании в JSON файл
        j_dumps(campaign_ai, self.base_path / "ai" / f"gemini_{gs.now}_{self.language}_{self.currency}.json", exc_info = False)
        return


    def process_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """
        Обрабатывает товары в указанной категории.

        :param category_name: Название категории.
        :type category_name: str
        :return: Список объектов SimpleNamespace, представляющих товары или None, если товары не найдены.
        :rtype: Optional[List[SimpleNamespace]]

        :Example:
            >>> products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
            >>> print(len(products))
            20
            >>> for product in products:
            >>>     pprint(product)
        """

        def read_sources(category_name: str) -> Optional[List[str]]:
            """
            Читает источники товаров и извлекает их ID.

            :param category_name: Название категории.
            :type category_name: str
            :return: Список ID товаров или None, если ID не найдены.
            :rtype: Optional[List[str]]

            :Example:
                >>> product_ids: Optional[List[str]] = read_sources("Electronics")
                >>> print(product_ids)
                ['12345', '67890', ...]
            """
            product_ids = []
            html_files = get_filenames(
                self.base_path / "category" / category_name / "sources",
                extensions=".html",
                exc_info=False,
            )
            if html_files:
                product_ids.extend(extract_prod_ids(html_files))
            product_urls = read_text_file(
                self.base_path / "category" / category_name / "sources.txt",
                as_list = True,
                exc_info = False,
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
                f"No products found in category {category_name}/{self.language}_{self.currency}.",
                exc_info=False,
            )
            return
        # Код инициализирует генератор партнерских ссылок
        promo_generator = AliAffiliatedProducts(
            language = self.language, currency = self.currency
        )

        # Код обрабатывает аффилированные продукты и возвращает их
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
        Сохраняет данные о товарах в JSON-файлы.

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

        category_path = Path(self.base_path / "category" / category_name)
        for product in products:
            product_id = getattr(product, "product_id", None)
            if not product_id:
                logger.warning(f"Skipping product without product_id: {product}")
                continue
            # Код сохраняет данные товара в JSON файл
            j_dumps(product, category_path / f"{product_id}.json", exc_info = False)


    def set_categories_from_directories(self):
        """
        Устанавливает категории рекламной кампании из названий директорий.

        :return: None

        :Example:
            >>> self.set_categories_from_directories()
            >>> print(self.campaign.category.category1.category_name)
        """
        category_dirs = self.base_path / "category"
        categories = get_directory_names(category_dirs)
        if not hasattr(self.campaign, "category"):
            self.campaign.category = SimpleNamespace()

        for category_name in categories:
            # Код добавляет каждую категорию как атрибут объекта SimpleNamespace
            setattr(
                self.campaign.category,
                category_name,
                SimpleNamespace(category_name=category_name, title="", description=""),
            )


    async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """
        Сохраняет данные о товарах в различных форматах.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param category_path: Путь для сохранения файлов.
        :type category_path: str | Path
        :param products_list: Список или объект SimpleNamespace товаров.
        :type products_list: list[SimpleNamespace] | SimpleNamespace

        :return: None

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
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H%M%S")
        products_list = products_list if isinstance(products_list, list) else [products_list]
        _data_for_openai: dict = {}
        _promotion_links_list: list = []
        _product_titles: list = []

        for product in products_list:
            # Код добавляет словарь категорий
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
            product.categories_convertor = categories_convertor
            # Код сохраняет данные товара в JSON файл
            j_dumps(product, Path(category_path / f"{self.language}_{self.currency}" / f"{product.product_id}.json"), exc_info = False)
            _product_titles.append(product.product_title)
            _promotion_links_list.append(product.promotion_link)

        await self.save_product_titles(product_titles=_product_titles, category_path=category_path)
        await self.save_promotion_links(promotion_links=_promotion_links_list, category_path=category_path)
        await self.generate_html(campaign_name=campaign_name, category_path=category_path, products_list=products_list)


    async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """
        Создает HTML-файл для категории и корневой индексный файл.

        :param products_list: Список товаров для включения в HTML.
        :type products_list: list[SimpleNamespace] | SimpleNamespace
        :param category_path: Путь для сохранения HTML-файла.
        :type category_path: str | Path
        :return: None
        """
        products_list = products_list if isinstance(products_list, list) else [products_list]

        category_name = Path(category_path).name
        category_html_path:Path = Path(category_path) /  f"{self.language}_{self.currency}" / f'{category_name}.html'

        # Инициализация словаря для хранения заголовков товаров
        category = {
            "products_titles": []
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
            # Код добавляет данные товара в словарь
            category["products_titles"].append({
                "title": product.product_title,
                "product_id": product.product_id,
                "first_category_name": product.first_level_category_name,
                "second_category_name": product.second_level_category_name
            })

            html_content += f"""
            <div class="product-card">
            <img src="{product.local_saved_image}" alt="{html.escape(product.product_title)}" class="product-image">
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

        # Код сохраняет HTML-содержимое в файл
        save_text_file(html_content, category_html_path)
        # Код генерирует главный index.html файл
        campaign_path  = gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name
        campaign_path.mkdir(parents=True, exist_ok=True)
        index_html_path = campaign_path / 'index.html'


        # Код собирает ссылки на все категории
        category_links = []
        categories =  get_directory_names(campaign_path / 'category')
        for _category_path in categories:
            category_name = Path(_category_path).name
            category_link = f"{category_name}/{category_name}.html"
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
        {"".join(category_links)}
        </ul>
        </body>
        </html>
        """

        # Код сохраняет HTML-содержимое главного индексного файла
        save_text_file(index_html_content, index_html_path)


    def generate_html_for_campaign(self, campaign_name: str):
        """
        Генерирует HTML-страницы для рекламной кампании.

        :param campaign_name: Имя рекламной кампании.
        :type campaign_name: str
        :return: None

        :Example:
            >>> campaign.generate_html_for_campaign("HolidaySale")
        """
        campaign_root = Path(gs.path.google_drive / "aliexpress" / "campaigns" / campaign_name)
        categories = get_filenames(campaign_root / "category", extensions="")

        # Код генерирует HTML-страницы для каждой категории
        for category_name in categories:
            category_path = campaign_root / "category" / category_name
            products = self.get_category_products(category_name=category_name)

            if products:
                # Код генерирует страницы для каждого товара
                for product in products:
                    ProductHTMLGenerator.set_product_html(product, category_path)
                # Код генерирует страницы для категории
                CategoryHTMLGenerator.set_category_html(products, category_path)
            else:
                logger.warning(f"No products found for category {category_name}.")
        # Код генерирует страницу рекламной кампании
        CampaignHTMLGenerator.set_campaign_html(categories, campaign_root)


    async def save_product_titles(self, product_titles: list[str], category_path: Path):
         """
         Сохраняет заголовки товаров в файл `product_titles.txt`.
    
         :param product_titles: Список заголовков товаров.
         :type product_titles: list[str]
         :param category_path: Путь к директории категории.
         :type category_path: Path
         :return: None
         """
         if not product_titles:
             logger.warning(f'Не переданы заголовки товаров {product_titles=}')
             return
         file_path = Path(category_path / f"{self.language}_{self.currency}" / 'product_titles.txt')
         save_text_file('\n'.join(product_titles), file_path)
         return
    
    
    async def save_promotion_links(self, promotion_links: list[str], category_path: Path):
         """
         Сохраняет партнерские ссылки товаров в файл `promotion_links.txt`.
    
         :param promotion_links: Список партнерских ссылок.
         :type promotion_links: list[str]
         :param category_path: Путь к директории категории.
         :type category_path: Path
         :return: None
         """
         if not promotion_links:
             logger.warning(f'Не переданы партнерские ссылки {promotion_links=}')
             return
         file_path = Path(category_path / f"{self.language}_{self.currency}"/ 'promotion_links.txt')
         save_text_file('\n'.join(promotion_links), file_path)
         return

def fix_json_string(value: Any) -> str:
    """
    Преобразует значение в строку, экранируя специальные символы.

    :param value: Значение для преобразования.
    :type value: Any
    :return: Экранированная строка.
    :rtype: str
    """
    if isinstance(value, str):
        return html.escape(value).replace('\\\\', '\\')
    return str(value)