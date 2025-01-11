### Анализ кода модуля `scenario_pricelist`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован с использованием классов и функций для разделения логики.
    - Применяется асинхронное программирование для неблокирующих операций.
    - Используются кастомные граберы для различных поставщиков, что обеспечивает гибкость.
    - Логирование ошибок с использованием `logger`.
- **Минусы**:
    - Много `...` маркеров в коде, что затрудняет понимание логики и усложняет отладку.
    - Используются двойные кавычки в коде, а не одинарные.
    - Присутствуют конструкции `try-except` без конкретной обработки ошибок.
    - Не все функции имеют `RST`-документацию.
    - Некоторые комментарии не достаточно информативны.
    - Есть повторяющийся код и логика.

**Рекомендации по улучшению**:

1.  Заменить все маркеры `...` на конкретную логику или убрать их, если они не несут смысловой нагрузки.
2.  Исправить использование двойных кавычек в коде на одинарные.
3.  Улучшить обработку ошибок, заменив общие блоки `try-except` на более специфичные с использованием `logger.error` для логирования ошибок.
4.  Добавить `RST`-документацию ко всем функциям и методам, включая параметры, возвращаемые значения и примеры использования.
5.  Уточнить комментарии, избегая размытых формулировок типа "получаем" или "делаем".
6.  Оптимизировать код, убрав повторяющиеся участки и улучшить читаемость кода.
7.  Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для работы с JSON.
8.  Убрать излишнее логирование отладочной информации, оставив только важные сообщения об ошибках.
9.  Использовать `from src.logger.logger import logger` для импорта логгера.

**Оптимизированный код**:

```python
"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

:platform: Windows, Unix
:synopsis: Provides functionality for extracting, parsing, and processing product data from 
    various suppliers. The module handles data preparation, AI processing, 
    and integration with Facebook for product posting.
"""
import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from dataclasses import field

import header
from src import gs
from src.endpoints.prestashop.product_fields import ProductFields
from src.webdriver.playwright import Playwrid
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
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
from src.utils.image import save_image_from_url, save_image
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger.logger import logger  # Используем явный импорт логгера


class MexironBuilder:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

    :ivar driver: Экземпляр Playwright.
    :vartype driver: Playwrid
    :ivar export_path: Путь для экспорта данных.
    :vartype export_path: Path
    :ivar products_list: Список обработанных данных о продуктах.
    :vartype products_list: List[dict]
    :ivar mexiron_name: Название мехирона.
    :vartype mexiron_name: str
    :ivar price: Цена.
    :vartype price: float
    :ivar timestamp: Временная метка.
    :vartype timestamp: str
    :ivar model: Экземпляр Google Generative AI.
    :vartype model: GoogleGenerativeAI
    :ivar config: Конфигурация.
    :vartype config: SimpleNamespace
    :ivar translations: Переводы.
    :vartype translations: SimpleNamespace
    :ivar update: Обновление телеграм.
    :vartype update: Update
    :ivar context: Контекст телеграм.
    :vartype context: CallbackContext
    """
    driver: Playwrid = Playwrid()
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    config: SimpleNamespace
    translations: SimpleNamespace = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'translations' / 'mexiron.json')
    # telegram
    update: Update
    context: CallbackContext

    def __init__(self, mexiron_name: Optional[str] = None):
        """
        Инициализирует класс MexironBuilder с необходимыми компонентами.

        :param mexiron_name: Необязательное имя для процесса мехирона.
        :type mexiron_name: Optional[str]
        :raises Exception: Если не удается загрузить конфигурацию или создать путь экспорта.

        :Example:
            >>> mexiron_builder = MexironBuilder(mexiron_name='test_mexiron')
        """
        try:
            self.config = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
        except Exception as e:
            logger.error(f'Error loading configuration: {e}')
            return  # or raise an exception, depending on your error handling strategy

        self.timestamp = gs.now
        self.mexiron_name = mexiron_name or self.timestamp

        try:
            storage = gs.path.external_storage if self.config.storage == 'external_storage' else gs.path.data if self.config.storage == 'data' else gs.path.goog
            self.export_path = storage / 'kazarinov' / 'mexironim' / self.mexiron_name
        except Exception as ex:
            logger.error(f'Error constructing export path: {ex}')
            return

        try:
            system_instruction = (gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
            api_key = gs.credentials.gemini.kazarinov
            self.model = GoogleGenerativeAI(
                api_key=api_key,
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )
        except Exception as ex:
            logger.error(f'Error loading instructions or API key: {ex}')
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
        Выполняет сценарий: разбирает продукты, обрабатывает их через AI и сохраняет данные.

        :param update: Обновление телеграм.
        :type update: Update
        :param context: Контекст телеграм.
        :type context: CallbackContext
        :param urls: Список URL-адресов страниц товаров.
        :type urls: list[str]
        :param price: Цена для обработки.
        :type price: Optional[str]
        :param mexiron_name: Пользовательское имя мехирона.
        :type mexiron_name: Optional[str]
        :return: True, если сценарий выполнен успешно, False в противном случае.
        :rtype: bool

        :raises Exception: В случае ошибки получения или обработки данных.
        """
        self.update = update
        self.context = context

        required_fields: tuple = (
            'id_product',
            'name',
            'description_short',
            'description',
            'specification',
            'local_image_path'
        )
        products_list = []

        for url in urls:
            graber = self.get_graber_by_supplier_url(url)
            if not graber:
                logger.debug(f'Нет грабера для: {url}')
                continue

            try:
                await update.message.reply_text(f'Process: \n{url}')
                f = await graber.grab_page(*required_fields)

                if gs.host_name == 'Vostro-3888':
                   pass  # placeholder замедлитель - убрал многоточие
            except Exception as ex:
                logger.error(f'Ошибка получения полей товара: {ex}')
                continue

            if not f:
                logger.debug(f'Failed to parse product fields for URL: {url}')
                continue

            product_data = await self.convert_product_fields(f)
            if not product_data:
                logger.debug(f'Failed to convert product fields: {product_data}')
                continue

            if not await self.save_product_data(product_data):
                logger.error(f'Data not saved! {pprint(product_data)}')
                continue
            products_list.append(product_data)

        langs_list: list = ['he', 'ru']
        for lang in langs_list:
            await update.message.reply_text(f'AI processing lang = {lang}')
            data: dict = await self.process_ai(products_list, lang)
            if not data:
                await update.message.reply_text('Ошибка модели')
                continue

            data[lang]['price'] = price
            data[lang]['currency'] = getattr(self.translations.currency, lang, "ש''ח")

            if not j_dumps(data, self.export_path / f'{self.mexiron_name}_{lang}.json'):
                await update.message.reply_text('Ошибка JSON')
                continue

            html_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.html')
            pdf_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.pdf')
            if await self.create_report(data[lang], lang, html_file, pdf_file):
                await update.message.reply_text('successfull')
        return True


    def get_graber_by_supplier_url(self, url: str):
        """
        Возвращает соответствующий грабер для заданного URL-адреса поставщика.

        :param url: URL-адрес страницы поставщика.
        :type url: str
        :return: Экземпляр грабера, если совпадение найдено, иначе None.
        :rtype: Optional[object]

        :Example:
            >>> graber = get_graber_by_supplier_url('https://www.ksp.co.il/...')
        """
        self.driver.get_url(url)
        if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
            return MorleviGraber(self.driver)
        if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
            return KspGraber(self.driver)
        if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
            return GrandadvanceGraber(self.driver)
        if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
            return IvoryGraber(self.driver)
        logger.debug(f'No graber found for URL: {url}')
        return None

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Преобразует поля продукта в словарь.

        :param f: Объект, содержащий разобранные данные о продукте.
        :type f: ProductFields
        :return: Словарь с отформатированными данными о продукте.
        :rtype: dict

        :Example:
            >>> product_data = await convert_product_fields(f)
        """
        if not f.id_product:
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
        Сохраняет данные отдельного продукта в файл.

        :param product_data: Словарь с отформатированными данными о продукте.
        :type product_data: dict
        :return: True в случае успешного сохранения, иначе False.
        :rtype: bool

        :raises Exception: Если не удается сохранить данные продукта.

        :Example:
            >>> await save_product_data(product_data)
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        if not j_dumps(product_data, file_path, ensure_ascii=False):
            logger.error(f'Ошибка сохранения словаря {pprint(product_data)}\\n Путь: {file_path}')
            return False
        return True

    async def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> dict:
        """
        Обрабатывает список продуктов через AI-модель.

        :param products_list: Список словарей с данными о продуктах.
        :type products_list: List[str]
        :param lang: Язык для обработки.
        :type lang: str
        :param attempts: Количество попыток повтора в случае неудачи.
        :type attempts: int, optional
        :return: Обработанный ответ в виде словаря.
        :rtype: dict

        :raises Exception: В случае ошибки от AI.

         :Example:
           >>> data = await process_ai(products_list, lang='ru', attempts=3)
        """
        if attempts < 1:
            return {}
        model_command = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
        q = model_command + '\n' + str(products_list)
        response = await self.model.ask(q)
        if not response:
            logger.error('Нет ответа от модели')
            return {}

        response_dict: dict = j_loads(response)

        if not response_dict:
            logger.error('Ошибка парсинга ответа модели')
            if attempts > 1:
                return await self.process_ai(products_list, lang, attempts - 1)
            return {}
        return response_dict

    async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Исполняет сценарий рекламного модуля `facebook`.
        :param mexiron: SimpleNamespace с данными мехирона
        :type mexiron: SimpleNamespace
        :return: True если публикация успешна, иначе False
        :rtype: bool
        """
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

    async def create_report(self, data: dict, lang: str, html_file: Path, pdf_file: Path) -> bool:
        """
        Отправляет задание на создание мехирона в формате `html` и `pdf`.

        :param data: Данные для отчета.
        :type data: dict
        :param lang: Язык для отчета.
        :type lang: str
        :param html_file: Путь для HTML-файла.
        :type html_file: Path
        :param pdf_file: Путь для PDF-файла.
        :type pdf_file: Path
        :return: True, если отчет успешно создан и отправлен, False в противном случае.
        :rtype: bool

        :raises Exception: Если не удается создать PDF-файл или отправить его.
        """
        generator = ReportGenerator()

        if await generator.create_report(data, lang, html_file, pdf_file):
            if pdf_file.exists() and pdf_file.is_file():
                await self.update.message.reply_document(document=pdf_file)
                return True
            else:
                logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
                return False
        return False