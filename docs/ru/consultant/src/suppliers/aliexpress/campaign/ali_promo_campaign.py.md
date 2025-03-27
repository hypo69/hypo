## Анализ кода модуля `ali_promo_campaign`

**Качество кода:**

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются асинхронные операции, что способствует производительности.
    - Присутствует базовая документация в формате docstring.
    - Активно используется логирование для отслеживания выполнения кода.
- **Минусы**:
    - Не везде используется `j_loads_ns` и `j_dumps`.
    - В некоторых местах используются двойные кавычки для строк, что противоречит гайдлайну.
    - Есть избыточные импорты `header`.
    - Не все функции и методы имеют RST-документацию.
    - Использование `try-except` без логирования.
    - Не всегда используется f-строки для форматирования строк.
    - Повторяющиеся импорты.

**Рекомендации по улучшению:**

1.  **Форматирование строк**:
    -   Используйте одинарные кавычки для строк в коде, кроме `print`, `input`, `logger.error`.
    -   Используйте f-строки для форматирования, чтобы улучшить читаемость.
2.  **Импорты**:
    -   Удалите дублирующиеся импорты и импорт `header`.
    -   Используйте `from src.logger.logger import logger` для логирования.
3.  **Обработка JSON**:
    -   Используйте `j_loads_ns` и `j_dumps` из `src.utils.jjson` везде, где работаете с JSON.
4.  **Документация**:
    -   Добавьте RST-документацию для всех функций, методов и классов.
5.  **Обработка ошибок**:
    -   Используйте `logger.error` для обработки исключений вместо `try-except` без логирования.
6.  **Улучшение читаемости**:
    -   Разбейте длинные функции на более мелкие и специализированные.
    -   Избегайте неясных формулировок в комментариях, таких как "получаем" или "делаем". Вместо этого используйте более точные описания: "проверяем", "отправляем", "выполняем".
7.  **Переименование переменных**:
    -   Переименуйте переменные для более ясного понимания их назначения.
8.  **Удаление лишнего кода**:
    -   Удалить закомментированный код.
    -   Убрать лишние импорты.
    -   Упростить логику там, где это возможно.

**Оптимизированный код:**

```python
"""
Модуль для управления рекламными кампаниями на AliExpress.
==========================================================

Модуль `ali_promo_campaign` предназначен для управления рекламными кампаниями на платформе AliExpress,
включая обработку данных о категориях и товарах, создание и редактирование JSON-файлов с информацией о
кампаниях, а также использование AI для генерации данных о кампаниях.

Примеры
--------

Инициализация рекламной кампании:

.. code-block:: python

    >>> campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    >>> print(campaign.campaign_name)

Обработка всей кампании:

.. code-block:: python

    >>> campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    >>> campaign.process_campaign()

Обработка данных о товарах в категории:

.. code-block:: python

    >>> campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    >>> products = campaign.process_category_products('electronics')

Заполнение данных категорий с использованием AI:

.. code-block:: python

    >>> campaign = AliPromoCampaign('new_campaign', 'EN', 'USD')
    >>> campaign.process_ai_category('Electronics')
"""
import asyncio
import copy
import html
import time  # Import time
from pathlib import Path
from typing import List, Optional, Dict
from types import SimpleNamespace

from src import gs
from src.suppliers.aliexpress import campaign
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils import locales
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.suppliers.aliexpress.campaign.html_generators import (
    ProductHTMLGenerator,
    CategoryHTMLGenerator,
    CampaignHTMLGenerator,
)
from src.logger.logger import logger
from src.utils.file_async import (
    read_text_file,
    get_filenames_from_directory,
    get_directory_names,
)
from src.utils.jjson import j_dumps, j_loads_ns, j_loads
from src.utils.convertors.csv import csv2dict
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

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык, используемый в кампании.
        :type language: Optional[str]
        :param currency: Валюта, используемая в кампании.
        :type currency: Optional[str]
        :param model: Модель ИИ для использования ('openai' или 'gemini').
        :type model: str
        :raises FileNotFoundError: Если файл кампании не найден.

        :Example:
        >>> campaign = AliPromoCampaign(campaign_name='SummerSale', language='EN', currency='USD')
        >>> print(campaign.campaign_name)
        """
        self.base_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name
        campaign_file_path = self.base_path / f'{language}_{currency}.json'
        self.campaign = j_loads_ns(
            campaign_file_path, exc_info=False
        )  # Файл может не существовать при создании новой кампании
        if not self.campaign:
            logger.warning(
                f'Campaign file not found at {campaign_file_path=}\nStart as new \n(Start build JSON file, categories, products etc.)'
            )
            # Если в корне рекламной кампании нет файла JSON -> запускается процесс создания новой реклмной кампании
            # создадутся категории из названий директорий ц директории `catergorry`,
            # соберутся affiliated товары в файлы <product_id>.JSON
            # сгенеририуется ai параметры
            self.process_new_campaign(
                campaign_name=campaign_name, language=language, currency=currency
            )  # Создание новой рекламной кампании
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
        """Настраивает модели ИИ для использования."""
        system_instruction_path = gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'
        system_instruction: str = read_text_file(system_instruction_path)
        self.gemini = GoogleGenerativeAI(system_instruction = system_instruction)
        assistant_id = 'asst_dr5AgQnhhhnef5OSMzQ9zdk9'  # <- задача asst_dr5AgQnhhhnef5OSMzQ9zdk9 создание категорий и описаний на основе списка названий товаров


    def process_campaign(self):
        """Итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

        :Example:
        >>> campaign.process_campaign()
        """
        categories_names_list = get_directory_names(self.base_path / 'category') # Читаю название папок категорий
        for category_name in categories_names_list:
            logger.info(f'Starting {category_name=}')
            self.process_category_products(category_name)
            logger.info(f'Starting AI category')
            self.process_ai_category(category_name)


    def process_campaign_category(
        self, category_name: str
    ) -> list[SimpleNamespace] | None:
        """Обрабатывает конкретную категорию в рамках кампании.
        :param category_name: Название категории.
        :type category_name: str
        :return: Список товаров в категории.
        :rtype: Optional[List[SimpleNamespace]]
        :Example:
            >>> campaign.process_campaign_category(category_name='electronics')
        """
        self.process_category_products(category_name=category_name)
        self.process_ai_category(category_name=category_name)


    def process_new_campaign(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
    ):
        """Создание новой рекламной кампании.
        Условия для создания кампании:
        - директория кампании с питоник названием
        - вложенная директория `campaign`, в ней директории с питоник названиями категорий
        - файл sources.txt и/или директория `sources` с файлами `<product)id>.html`

        :param campaign_name: Название рекламной кампании.
        :type campaign_name: str
        :param language: Язык для кампании (необязательно).
        :type language: Optional[str]
        :param currency: Валюта для кампании (необязательно).
        :type currency: Optional[str]
        :return: Список кортежей с именами категорий и их обработанными результатами.
        :rtype: List[Tuple[str, Any]]

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
            )  # Паралельно создаю ai кампанию
            self.campaign_ai_file_name = f'{language}_{currency}_AI_{gs.now}.json'
            for category_name in vars(self.campaign.category):
                self.process_category_products(category_name)
                self.process_ai_category(category_name)
                j_dumps(
                    self.campaign_ai,
                    self.base_path / f'{self.language}_{self.currency}.json',
                )  # В вновь созданный файл категорий


    def process_ai_category(self, category_name: Optional[str] = None):
        """Обрабатывает AI-данные для указанной категории или всех категорий.

        :param category_name: Название категории для обработки. Если не указано, обрабатываются все категории.
        :type category_name: Optional[str]
        :Example:
            >>> campaign.process_ai_category('Electronics')
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
            """Обрабатывает AI-данные для категории и обновляет данные кампании."""

            titles_path: Path = (
                self.base_path
                / 'category'
                / category_name
                / f'{campaign_ai.language}_{campaign_ai.currency}'
                / 'product_titles.txt'
            )
            product_titles = read_text_file(titles_path, as_list=True)
            prompt = f'language={campaign_ai.language}\n{category_name=}\n{product_titles=}'

            if not self.gemini or not self.openai:
                self._models_payload()

            def get_response(_attempts: int = 5):
                """Получает ответ от AI модели."""
                return self.gemini.ask(prompt)

            response = get_response()
            if not response:
                return

            try:
                res_ns: SimpleNamespace = j_loads_ns(response)  # Превращаю ответ машины в объект SimpleNamespace
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
                logger.error(f'Error updating campaign for {category_name=}: {ex}', exc_info=False)

        for category_name in vars(campaign_ai.category):
            _process_category(category_name)

        j_dumps(campaign_ai, self.base_path / 'ai' / f'gemini_{gs.now}_{self.language}_{self.currency}.json')
        return


    def process_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Обрабатывает товары в указанной категории.

        :param category_name: Название категории.
        :type category_name: str
        :return: Список объектов SimpleNamespace, представляющих товары.
        :rtype: Optional[List[SimpleNamespace]]
        :raises FileNotFoundError: If no products found in category.
        :Example:
            >>> products: List[SimpleNamespace] = campaign.process_category_products('Electronics')
            >>> print(len(products))
            20
            >>> for product in products:
            >>>     pprint(product)  # Use pprint from `src.utils.pprint`

        :Notes:
            Функция пытается прочитать ID товаров из HTML-файлов и текстовых файлов
            в директории `sources` указанной категории. Если ID товаров не найдены,
            возвращает `None`.
            Если партнерские товары найдены, они возвращаются; в противном случае,
            возвращается `None` и в лог записывается ошибка.

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
            """Читает источники товаров и извлекает ID товаров.

            :param category_name: Название категории.
            :type category_name: str
            :return: Список ID товаров, если найдены, иначе None.
            :rtype: Optional[List[str]]
            :Example:
                >>> product_ids: Optional[List[str]] = read_sources('Electronics')
                >>> print(product_ids)
                ['12345', '67890', ...]

            :Notes:
                Функция ищет ID товаров как в HTML файлах, так и в файле `sources.txt`,
                расположенных в директории `sources` категории. Если ID товаров не найдены,
                функция возвращает `None`.
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
                f'No products found in category {category_name}/{self.language}_{self.currency}.',
                exc_info=False,
            )
            return

        promo_generator = AliAffiliatedProducts(
            language = self.language, currency = self.currency
        )

        return asyncio.run(promo_generator.process_affiliate_products(
            prod_ids = prod_ids,
            category_root = self.base_path
            / 'category'
            / category_name,
        ))


    def dump_category_products_files(
        self, category_name: str, products: List[SimpleNamespace]
    ):
        """Сохранение данных о товарах в JSON-файлы.

        :param category_name: Имя категории.
        :type category_name: str
        :param products: Список объектов SimpleNamespace, представляющих товары.
        :type products: List[SimpleNamespace]

        :Example:
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
            j_dumps(product, category_path / f'{product_id}.json')


    def set_categories_from_directories(self):
        """Устанавливает категории рекламной кампании из названий директорий в `category`.

        :Notes:
            Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
            `category_name`, `title` и `description`.

        :Example:
            >>> self.set_categories_from_directories()
            >>> print(self.campaign.category.category1.category_name)
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

    async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """Сохраняет данные о товарах в различных форматах.

        - `<product_id>.json`: Содержит все параметры продукта, один файл на продукт.
        - `ai_{timestamp}.json`: Общий файл для всех продуктов с определенными ключами.
        - `promotion_links.txt`: Список ссылок на продукты, созданный в `save_promotion_links()`.
        - `category_products_titles.json`: Файл, содержащий `title`, `product_id`,
        `first_category_name` и `second_category_name` каждого товара в категории.

        :param campaign_name: Название кампании для выходных файлов.
        :type campaign_name: str
        :param category_path: Путь для сохранения выходных файлов.
        :type category_path: str | Path
        :param products_list: Список товаров или один товар для сохранения.
        :type products_list: list[SimpleNamespace] | SimpleNamespace

        :Example:
            >>> products_list: list[SimpleNamespace] = [
            ...     SimpleNamespace(product_id='123', product_title='Product A', promotion_link='http://example.com/product_a',
            ...                     first_level_category_id=1, first_level_category_name='Category1',
            ...                     second_level_category_id=2, second_level_category_name='Subcategory1',
            ...                     product_main_image_url='http://example.com/image.png', product_video_url='http://example.com/video.mp4'),
            ...     SimpleNamespace(product_id='124', product_title='Product B', promotion_link='http://example.com/product_b',
            ...                     first_level_category_id=1, first_level_category_name='Category1',
            ...                     second_level_category_id=3, second_level_category_name='Subcategory2',
            ...                     product_main_image_url='http://example.com/image2.png', product_video_url='http://example.com/video2.mp4')
            ... ]
            >>> category_path: Path = Path('/path/to/category')
            >>> await generate_output('CampaignName', category_path, products_list)

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
                    'PrestaShop_main_category': ''
                },
                str(product.second_level_category_id): {
                    'ali_category_name': product.second_level_category_name,
                    'ali_parent': str(product.first_level_category_id),
                    'PrestaShop_categories': [],
                    'PrestaShop_main_category': ''
                }
            }
            product.categories_convertor = categories_convertor

            # Save individual product JSON
            j_dumps(product, Path(category_path / f'{self.language}_{self.currency}' / f'{product.product_id}.json'), exc_info=False)
            _product_titles.append(product.product_title)
            _promotion_links_list.append(product.promotion_link)

        await self.save_product_titles(product_titles=_product_titles, category_path=category_path)
        await self.save_promotion_links(promotion_links=_promotion_links_list, category_path=category_path)
        await self.generate_html(campaign_name=campaign_name, category_path=category_path, products_list=products_list)

    async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """Создает HTML-файл для категории и корневой индексный файл.
    
        :param products_list: Список продуктов для включения в HTML.
        :type products_list: list[SimpleNamespace] | SimpleNamespace
        :param category_path: Путь для сохранения HTML-файла.
        :type category_path: str | Path
        """
        products_list = products_list if isinstance(products_list, list) else [products_list]

        category_name = Path(category_path).name
        category_html_path:Path = Path(category_path) /  f'{self.language}_{self.currency}' / f'{category_name}.html'
    
        # Initialize the category dictionary to store product titles
        category = {
            'products_titles': []
        }
    
        html_content = f"""<!DOCTYPE html>
        <html lang='en'>
        <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>{category_name} Products</title>
        <link rel='stylesheet' href='styles.css'>
        </head>
        <body>
        <h1>{category_name} Products</h1>
        <div class='product-grid'>
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
            <div class='product-card'>
            <img src='{product.local_image_path}' alt='{html.escape(product.product_title)}' class='product-image'>
            <div class='product-info'>
            <h2 class='product-title'>{html.escape(product.product_title)}</h2>
            <p class='product-price'>{product.target_sale_price} {product.target_sale_price_currency}</p>
            <p class='product-original-price'>{product