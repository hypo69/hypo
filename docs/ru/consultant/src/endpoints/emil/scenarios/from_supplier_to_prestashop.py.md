### Анализ кода модуля `from_supplier_to_prestashop`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован с использованием классов и методов, что улучшает читаемость и организацию.
    - Использование асинхронных операций для неблокирующего выполнения задач.
    - Присутствуют логирующие сообщения для отслеживания ошибок и хода выполнения.
    - Применение `j_loads` и `j_dumps` вместо стандартных `json.load` и `json.dumps`.
- **Минусы**:
    - Не все функции документированы в формате RST.
    - Присутствует избыточное использование `try-except` блоков.
    - Не везде используется `logger.error` для обработки ошибок, иногда используется простой `print`.
    - Не используется `from src.logger.logger import logger`.
    - Присутствуют `...` в коде как маркеры, которые лучше заменить на более конкретные комментарии.

**Рекомендации по улучшению**:
- Добавить RST-документацию для всех функций и методов, включая параметры и возвращаемые значения.
- Заменить множественные блоки `try-except` на более компактную обработку ошибок с использованием `logger.error`.
- Использовать `from src.logger.logger import logger` для логирования ошибок.
- Заменить `...` на конкретные маркеры, возможно, с более детальным описанием или комментарием.
- Улучшить обработку ошибок при загрузке конфигурации, добавив `raise` исключения для более явной сигнализации ошибок.
- В функции `run_scenario` добавить логирование перед выходом из функции при ошибках.
- Избегать дублирования кода при обработке ошибок.
- Привести код в соответствие с PEP8.
- Улучшить обработку ошибок, где используются `...` и добавить логирование с указанием контекста ошибки.
- В функции `convert_product_fields` при ошибке возвращать `None` вместо `{}`, чтобы было более явно видно ошибку, и исправить  `# <- сбой при получении полей товара.` на более точное описание проблемы.
- В функции `save_product_data`  возвращать `False` в случае ошибки.

**Оптимизированный код**:
```python
from __future__ import annotations

# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

.. module:: src.endpoints.emil.scenarios.from_supplier_to_prestashop 
    :platform: Windows, Unix
    :synopsis: Provides functionality for extracting, parsing, and processing product data from 
    various suppliers. The module handles data preparation, AI processing, 
    and integration with Prestashop for product posting.
"""
import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from dataclasses import field

from telegram import Update
from telegram.ext import CallbackContext

import header
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
from src.logger.logger import logger  # Исправлен импорт logger


class SupplierToPrestashopProvider:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: Driver
    :ivar export_path: Путь для экспорта данных.
    :vartype export_path: Path
    :ivar products_list: Список обработанных данных о продуктах.
    :vartype products_list: List[dict]
    :ivar mexiron_name: Название мехирона.
    :vartype mexiron_name: str
    :ivar price: Цена мехирона.
    :vartype price: float
    :ivar timestamp: Временная метка.
    :vartype timestamp: str
    :ivar model: Экземпляр модели Google Generative AI.
    :vartype model: GoogleGenerativeAI
    :ivar config: Конфигурация приложения.
    :vartype config: SimpleNamespace
    :ivar update: Объект телеграм обновления.
    :vartype update: Update
    :ivar context: Контекст телеграм.
    :vartype context: CallbackContext

    """

    driver: 'Driver'
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: 'GoogleGenerativeAI'
    config: SimpleNamespace
    update: 'Update'
    context: 'CallbackContext'

    def __init__(self, driver: Driver):
        """
        Инициализирует класс SupplierToPrestashopProvider необходимыми компонентами.

        :param driver: Selenium WebDriver instance.
        :type driver: Driver
        :raises Exception: Если не удается загрузить конфигурацию или создать путь для экспорта.
        """
        self.driver = driver
        try:
            self.config = j_loads_ns(gs.path.endpoints / 'emil' / 'emil.json')
        except Exception as ex:
            logger.error(f"Error loading configuration: {ex}")
            raise  #  Проброс исключения для явной сигнализации ошибки

        self.timestamp = gs.now
        
        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'emil'
        except Exception as ex:
             logger.error(f"Error constructing export path: {ex}")
             raise #  Проброс исключения для явной сигнализации ошибки


        try:
            system_instruction = (gs.path.endpoints / 'emil' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            api_key = gs.credentials.gemini.emil
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error(f"Error loading instructions or API key: {ex}")
            raise #  Проброс исключения для явной сигнализации ошибки


    async def run_scenario(
        self,
        update: Update,
        context: CallbackContext,
        urls: list[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = '',

    ) -> bool:
        """
        Выполняет сценарий: парсит товары, обрабатывает их через ИИ и сохраняет данные.

        :param update: Объект телеграм обновления.
        :type update: Update
        :param context: Контекст телеграм.
        :type context: CallbackContext
        :param urls: Список URL-адресов страниц товаров.
        :type urls: list[str]
        :param price: Цена для обработки.
        :type price: Optional[str], optional
        :param mexiron_name: Пользовательское название мехирона.
        :type mexiron_name: Optional[str], optional
        :return: True, если сценарий выполнен успешно, False в противном случае.
        :rtype: bool

        :raises Exception: Если возникает ошибка при выполнении сценария.

        .. todo::
            сделать логер перед отрицательным выходом из функции.
            Важно! модель ошибается.
        """
        self.update = update
        self.context = context

        # Не все поля товара надо заполнять. Вот кортеж необходимых полей:
        required_fields: tuple = ('id_product',
                                 'name',
                                 'description_short',
                                 'description',
                                 'specification',
                                 'local_image_path')
        products_list = []

        # 1. Сбор товаров
        for url in urls:

            graber = self.get_graber_by_supplier_url(url)

            if not graber:
                logger.debug(f"Нет грабера для: {url}") #  Логирование, что не найден грабер
                continue  # Переход к следующему URL

            try:
                await update.message.reply_text(f"""Process: \n {url}""") # Отправка сообщения о начале обработки
                f = await graber.grab_page(*required_fields)

                if gs.host_name == 'Vostro-3888':
                    #self.driver.wait(5)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Замедлитель
                    ...
            except Exception as ex:
                 logger.error(f"Ошибка получения полей товара {url}: {ex}")
                 continue #  Переход к следующему URL

            if not f:
                logger.debug(f'Failed to parse product fields for URL: {url}') #  Логирование ошибки парсинга
                continue # Переход к следующему URL

            product_data = await self.convert_product_fields(f)
            if not product_data:
                 logger.debug(f'Failed to convert product fields: {product_data}') #  Логирование ошибки конвертации
                 continue  # Переход к следующему URL

            if not await self.save_product_data(product_data):
                logger.error(f"Data not saved! {pprint(product_data)}") #  Логирование ошибки сохранения
                continue
            products_list.append(product_data)
        return True


    async def convert_product_fields(self, f: ProductFields) -> dict | None:
        """
        Конвертирует поля из объекта `ProductFields` в простой словарь для модели ИИ.

        :param f: Объект, содержащий разобранные данные о товаре.
        :type f: ProductFields
        :return: Отформатированный словарь с данными товара.
        :rtype: dict
        :raises Exception: Если не удается конвертировать поля товара.

        .. note:: Правила построения полей определяются в `ProductFields`
        """
        if not f.id_product:
            logger.debug(f"Не удалось получить id_product: {f}") #   Логирование ошибки, когда не удалось получить id товара
            return None # <- сбой при получении id товара. Такое может произойти, если вместо страницы товара попалась страница категории, при невнимательном составлении мехирона из комплектующих
        try:
            product_data = {
                'product_title': f.name['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"'),
                'product_id': f.id_product,
                'description_short': f.description_short['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
                'description': f.description['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
                'specification': f.specification['language'][0]['value'].strip().replace("'", "\\'").replace('"', '\\"').replace(';', '<br>'),
                'local_image_path': str(f.local_image_path),
            }
            return product_data
        except Exception as ex:
             logger.error(f"Ошибка конвертации полей товара: {ex}")
             return None


    async def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные об отдельном продукте в файл.

        :param product_data: Отформатированные данные о продукте.
        :type product_data: dict
        :return: True, если данные успешно сохранены, False в противном случае.
        :rtype: bool
        :raises Exception: Если не удается сохранить данные товара.
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {pprint(product_data)}\\n Путь: {file_path}')
            return False
        return True

    async def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> dict | None:
        """
        Обрабатывает список товаров через ИИ модель.

        :param products_list: Список словарей с данными о товарах в строковом представлении.
        :type products_list: List[str]
        :param lang: Язык, на котором необходимо получить ответ.
        :type lang: str
        :param attempts: Количество попыток повтора в случае сбоя. По умолчанию 3.
        :type attempts: int, optional
        :return: Обработанный ответ в форматах `ru` и `he`.
        :rtype: tuple
        :return: Возвращает None, если не удалось получить корректный ответ после всех попыток.
        :rtype: None

        .. note::
            Модель может возвращать невалидный результат.
            В таком случае я переспрашиваю модель разумное количество раз.
        """
        if attempts < 1:
            logger.error(f"Нет попыток для запроса ИИ.") #  Логирование, если не осталось попыток запроса к ИИ
            return None  # return early if no attempts are left
        try:
            model_command = Path(gs.path.endpoints / 'emil' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
            # Request response from the AI model
            q = model_command + '\n' + str(products_list)
            response = await self.model.ask(q)
            if not response:
                logger.error(f"Нет ответа от модели") #  Логирование, если модель не ответила
                return None

            response_dict: dict = j_loads(response)

            if not response_dict:
                logger.error("Ошибка парсинга ответа модели") #  Логирование ошибки парсинга ответа модели
                if attempts > 1:
                    return await self.process_ai(products_list, lang, attempts - 1)
                return None
            return response_dict
        except Exception as ex:
             logger.error(f"Ошибка при обращении к ИИ: {ex}")
             return None


    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Исполняет сценарий рекламного модуля `facebook`.

        :param mexiron:  Объект SimpleNamespace содержащий данные для публикации.
        :type mexiron: SimpleNamespace
        :return: True, если публикация прошла успешно, иначе False.
        :rtype: bool
        :raises Exception: Если возникает ошибка при публикации в Facebook.
        """
        try:
            self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
            currency = "ש''ח"
            title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
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
        except Exception as ex:
            logger.error(f"Ошибка публикации в Facebook: {ex}")
            return False

    async def create_report(self, data: dict, lang: str, html_file: Path, pdf_file: Path) -> bool:
        """
        Отправляет задание на создание мехирона в форматах `html` и `pdf`.

        Если мехирон в pdf создался (`generator.create_report()` вернул True) - отправить его боту.

        :param data: Данные для отчета.
        :type data: dict
        :param lang: Язык для отчета.
        :type lang: str
        :param html_file: Путь к HTML файлу отчета.
        :type html_file: Path
        :param pdf_file: Путь к PDF файлу отчета.
        :type pdf_file: Path
        :return: True, если отчет создан и отправлен, иначе False.
        :rtype: bool
        :raises Exception: Если не удается создать или отправить отчет.
        """
        from src.endpoints.emil.report.report_generator import ReportGenerator # Импорт внутри функции, чтобы избежать циклического импорта

        generator = ReportGenerator()

        try:
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
        except Exception as ex:
            logger.error(f"Ошибка при создании или отправке отчета: {ex}")
            return False

    def get_graber_by_supplier_url(self, url:str):
        """
        Возвращает объект грабера в зависимости от URL поставщика.

        :param url: URL поставщика.
        :type url: str
        :return: Объект грабера или None, если поставщик не поддерживается.
        :rtype: object
        """
        if 'aliexpress' in url:
            from src.suppliers.aliexpress import Aliexpress
            return Aliexpress(self.driver)
        return None