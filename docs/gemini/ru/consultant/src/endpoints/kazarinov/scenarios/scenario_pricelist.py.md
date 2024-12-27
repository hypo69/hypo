# Анализ кода модуля `scenario_pricelist`

**Качество кода**

-  Соответствие требованиям по оформлению кода: 8/10
    -   **Плюсы:**
        -   Код хорошо структурирован, с использованием классов и функций.
        -   Используются `logger` для логирования ошибок и отладочной информации.
        -   Импорты организованы в начале файла.
        -   Применяются `async/await` для асинхронных операций.
        -   Используется reStructuredText (RST) для docstring.
    -   **Минусы:**
        -   Некоторые комментарии `#` не следуют стандарту RST.
        -   Не везде используются `j_loads_ns`, `j_dumps` для работы с JSON.
        -   Присутствуют `...` в коде, что может указывать на неполную реализацию.
        -   В некоторых местах `try-except` блоки избыточны или не логируются с помощью `logger`.
        -   Не всегда в docstring описаны типы возвращаемых значений.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Привести все комментарии в docstring в формат RST, включая описание параметров, возвращаемых значений и исключений.
    -   Добавить описание типов для всех параметров и возвращаемых значений.
2.  **Обработка JSON:**
    -   Использовать `j_loads` или `j_loads_ns` для чтения всех JSON-файлов.
    -   Использовать `j_dumps` для записи всех JSON-файлов.
3.  **Обработка ошибок:**
    -   Заменить `try-except` на `logger.error` для обработки ошибок.
    -   Избегать использования `...` в коде, добавить полноценную реализацию или логику.
4.  **Импорты:**
    -   Проверить и добавить недостающие импорты.
5.  **Комментарии:**
    -   Переписать все комментарии `#` в формат RST.
    -   Использовать в комментариях глаголы, описывающие действие, а не состояние ('проверка', 'отправка' вместо 'получение', 'делаем').
6.  **Общее:**
    -   Переименовать `MexironBuilder` в `PricelistBuilder`, для соответствия именования модуля.
    -   Разделить логику граббинга и обработки данных на более мелкие функции.
    -   Улучшить обработку исключений в `run_scenario` и `process_ai`.

**Оптимизированный код**

```python
"""
Модуль исполнения сценария создания прайс-листа для Сергея Казаринова.
==================================================================

:platform: Windows, Unix
:synopsis: Обеспечивает функциональность для извлечения, разбора и обработки данных о продуктах от различных поставщиков.
           Модуль обрабатывает подготовку данных, обработку с помощью ИИ и интеграцию с Facebook для публикации продуктов.
"""
from __future__ import annotations

import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List, Tuple, Dict, Any
from types import SimpleNamespace
from dataclasses import field

import header
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver.driver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title,
    upload_post_media,
    message_publish,
)
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.endpoints.kazarinov.pricelist_generator import ReportGenerator
from telegram import Update
from telegram.ext import CallbackContext

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_png_from_url, save_png
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger.logger import logger


MODE = 'dev'


class PricelistBuilder:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: Driver
    :ivar export_path: Путь для экспорта данных.
    :vartype export_path: Path
    :ivar products_list: Список обработанных данных о продуктах.
    :vartype products_list: List[dict]
    :ivar mexiron_name: Название прайса.
    :vartype mexiron_name: str
    :ivar price: Цена.
    :vartype price: float
    :ivar timestamp: Время создания.
    :vartype timestamp: str
    :ivar model: Модель генеративного ИИ.
    :vartype model: GoogleGenerativeAI
    :ivar config: Конфигурация.
    :vartype config: SimpleNamespace
    :ivar translations: Переводы.
    :vartype translations: SimpleNamespace
    :ivar update: Объект обновления Telegram.
    :vartype update: Update
    :ivar context: Контекст Telegram.
    :vartype context: CallbackContext
    """

    driver: Driver
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    config: SimpleNamespace
    translations: SimpleNamespace = j_loads_ns(
        gs.path.endpoints / 'kazarinov' / 'translations' / 'mexiron.json'
    )
    # telegram
    update: Update
    context: CallbackContext

    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None) -> None:
        """
        Инициализирует класс PricelistBuilder.

        :param driver: Экземпляр Selenium WebDriver.
        :type driver: Driver
        :param mexiron_name: Необязательное пользовательское имя для процесса прайс-листа.
        :type mexiron_name: Optional[str]
        """
        try:
            self.config = j_loads_ns(
                gs.path.endpoints / 'kazarinov' / 'kazarinov.json'
            )
        except Exception as e:
            logger.error(f"Ошибка загрузки конфигурации: {e}")
            return  # или вызвать исключение, в зависимости от стратегии обработки ошибок

        self.timestamp = gs.now
        self.driver = driver
        self.mexiron_name = mexiron_name or self.timestamp

        try:
            storage = (
                gs.path.external_storage
                if self.config.storage == 'external_storage'
                else gs.path.data
                if self.config.storage == 'data'
                else gs.path.goog
            )
            self.export_path = (
                storage / 'kazarinov' / 'mexironim' / self.mexiron_name
            )
        except Exception as e:
            logger.error(f"Ошибка при создании пути экспорта: {e}")
            return

        try:
            system_instruction = (
                gs.path.endpoints
                / 'kazarinov'
                / 'instructions'
                / 'system_instruction_mexiron.md'
            ).read_text(encoding='UTF-8')

            api_key = gs.credentials.gemini.kazarinov
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'},
            )
        except Exception as ex:
            logger.error(f"Ошибка загрузки инструкций или ключа API: {ex}")
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
        Выполняет сценарий: разбирает продукты, обрабатывает их через ИИ и сохраняет данные.

        :param update: Объект обновления Telegram.
        :type update: Update
        :param context: Контекст Telegram.
        :type context: CallbackContext
        :param urls: Список URL-адресов страниц продуктов.
        :type urls: list[str]
        :param price: Цена для обработки.
        :type price: Optional[str]
        :param mexiron_name: Пользовательское имя прайс-листа.
        :type mexiron_name: Optional[str]
        :return: True, если сценарий выполнен успешно, False в противном случае.
        :rtype: bool

        .. todo::
            сделать логер перед отрицательным выходом из функции.
            Важно! модель ошибается.
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
            'local_saved_image',
        )
        products_list = []

        # 1. Сбор товаров
        for url in urls:
            graber = self.get_graber_by_supplier_url(url)

            if not graber:
                logger.debug(f"Нет грабера для: {url}", None, False)
                continue

            try:
                await update.message.reply_text(f"""Process: \n                {url}""")
                f = await graber.grab_page(*required_fields)

                if gs.host_name == 'Vostro-3888':
                    ...
                    # self.driver.wait(5)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара", ex, False)
                continue

            if not f:
                logger.debug(f'Не удалось разобрать поля товара для URL: {url}')
                continue

            product_data = await self.convert_product_fields(f)
            if not product_data:
                logger.debug(
                    f'Не удалось преобразовать поля товара: {product_data}'
                )
                continue

            if not await self.save_product_data(product_data):
                logger.error(f"Данные не сохранены! {pprint(product_data)}")
                continue
            products_list.append(product_data)

        # 2. AI processing
        """ список компонентов сборки компьютера уходит в обработку моделью (`gemini`) ->
        модель парсит данные, делает перевод на `ru`, `he` и возвращает кортеж словарей по языкам.
        Внимание! модель может ошибаться"""

        langs_list: list = ['he', 'ru']
        for lang in langs_list:
            await update.message.reply_text(f"AI processing lang = {lang}")
            data: dict = await self.process_ai(products_list, lang)
            if not data:
                await update.message.reply_text("Ошибка модели")
                continue

            data[lang]['price'] = price
            data[lang]['currency'] = getattr(
                self.translations.currency, lang, "ש''ח"
            )

            if not j_dumps(data, self.export_path / f'{self.mexiron_name}_{lang}.json'):
                await update.message.reply_text("Ошибка JSON")

            html_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.html')
            pdf_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.pdf')
            # 3. Report creating
            if await self.create_report(data[lang], lang, html_file, pdf_file):
                await update.message.reply_text("successfull")
        return True

    def get_graber_by_supplier_url(self, url: str) -> object | None:
        """
        Возвращает соответствующий грабер для заданного URL-адреса поставщика.
        Для каждого поставщика реализован свой грабер, который извлекает значения полей с целевой html страницы

        :param url: URL-адрес страницы поставщика.
        :type url: str
        :return: Экземпляр грабера, если найдено совпадение, иначе None.
        :rtype: Optional[object]
        """
        self.driver.get_url(url)
        if url.startswith(
            ('https://morlevi.co.il', 'https://www.morlevi.co.il')
        ):
            return MorleviGraber(self.driver)
        if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
            return KspGraber(self.driver)
        if url.startswith(
            ('https://grandadvance.co.il', 'https://www.grandadvance.co.il')
        ):
            return GrandadvanceGraber(self.driver)
        if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
            return IvoryGraber(self.driver)
        logger.debug(f'Не найден грабер для URL: {url}')
        return None

    async def convert_product_fields(self, f: ProductFields) -> Dict:
        """
        Преобразует поля продукта в словарь.
        Функция конвертирует поля из объекта `ProductFields` в простой словарь для модели ии.

        :param f: Объект, содержащий разобранные данные о продукте.
        :type f: ProductFields
        :return: Отформатированный словарь с данными о продукте.
        :rtype: dict

        .. note:: Правила построения полей определяются в `ProductFields`
        """
        if not f.id_product:
            return {}  # <- сбой при получении полей товара. Такое может произойти если вместо страницы товара попалась страница категории, при невнимательном составлении мехирона из комплектующих
        return {
            'product_title': f.name['language'][0]['value']
            .strip()
            .replace("'", "\\'")
            .replace('"', '\\"'),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value']
            .strip()
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace(';', '<br>'),
            'description': f.description['language'][0]['value']
            .strip()
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace(';', '<br>'),
            'specification': f.specification['language'][0]['value']
            .strip()
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace(';', '<br>'),
            'local_saved_image': str(f.local_saved_image),
        }

    async def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные об отдельном продукте в файл.

        :param product_data: Отформатированные данные о продукте.
        :type product_data: dict
        :return: True, если сохранение успешно, иначе None.
        :rtype: bool
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(
                f'Ошибка сохранения словаря {pprint(product_data)}\\n Путь: {file_path}'
            )
            return False
        return True

    async def process_ai(
        self, products_list: List[str], lang: str, attempts: int = 3
    ) -> dict | bool:
        """
        Обрабатывает список продуктов с помощью модели ИИ.

        :param products_list: Список словарей с данными о продуктах.
        :type products_list: List[str]
        :param lang: Язык для обработки.
        :type lang: str
        :param attempts: Количество попыток переповтора в случае неудачи. По умолчанию 3.
        :type attempts: int
        :return: Обработанный ответ в формате `ru` и `he`.
        :rtype: dict | bool

        .. note::
            Модель может возвращать невелидный результат.
            В таком случае я переспрашиваю модель разумное количество раз.
        """
        if attempts < 1:
            return {}  # возвращаем рано, если не осталось попыток
        model_command = (
            gs.path.endpoints
            / 'kazarinov'
            / 'instructions'
            / f'command_instruction_mexiron_{lang}.md'
        ).read_text(encoding='UTF-8')
        # Request response from the AI model
        q = model_command + '\n' + str(products_list)
        response = await self.model.ask(q)
        if not response:
            logger.error(f"Нет ответа от модели")
            return {}

        try:
            response_dict: dict = j_loads(response)
        except Exception as e:
            logger.error(f"Ошибка парсинга ответа модели: {e}", exc_info=True)
            if attempts > 1:
                return await self.process_ai(products_list, lang, attempts - 1)
            return {}
        return response_dict

    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """Функция исполняет сценарий рекламного модуля `facvebook`.

        :param mexiron: Пространство имен с данными для публикации в Facebook.
        :type mexiron: SimpleNamespace
        :return: True, если публикация успешна.
        :rtype: bool
        """
        self.driver.get_url(
            r'https://www.facebook.com/profile.php?id=61566067514123'
        )
        currency = "ש''ח"
        title = f'{mexiron.title}\\n{mexiron.description}\\n{mexiron.price} {currency}'
        if not post_message_title(self.driver, title):
            logger.warning(f'Не получилось отправить название мехирона')
            return False

        if not upload_post_media(self.driver, media=mexiron.products):
            logger.warning(f'Не получилось отправить media')
            return False
        if not message_publish(self.driver):
            logger.warning(f'Не получилось отправить media')
            return False

        return True

    async def create_report(
        self, data: dict, lang: str, html_file: Path, pdf_file: Path
    ) -> bool:
        """
        Отправляет запрос на создание прайс-листа в формате `html` и `pdf`.
        Если прайс-лист в pdf создан (``generator.create_report()`` вернул True) -
        отправить его боту.

        :param data: Данные для отчета.
        :type data: dict
        :param lang: Язык отчета.
        :type lang: str
        :param html_file: Путь к html файлу.
        :type html_file: Path
        :param pdf_file: Путь к pdf файлу.
        :type pdf_file: Path
        :return: True если отчет создан и отправлен.
        :rtype: bool
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
        return False

```