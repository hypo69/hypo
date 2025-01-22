### Анализ кода модуля `emil_design`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, разделен на классы и функции, что облегчает чтение и понимание.
    - Используются асинхронные операции, что позволяет эффективно обрабатывать запросы к внешним API и файловой системе.
    - Применение `SimpleNamespace` для хранения данных упрощает доступ к атрибутам.
- **Минусы**:
    - Многоточия (`...`) в коде используются как маркеры, что затрудняет понимание логики.
    - Не все функции имеют подробную документацию в формате RST.
    - Смешение стилей кавычек.
    - Использование `time.sleep(20)` замедляет выполнение программы.
    - Не везде используется `logger.error` для обработки ошибок.
    - Присутствует избыточность импортов.
    - Отсутствует проверка на наличие файла конфигурации, что может привести к ошибкам.
    - Не выровнены названия переменных и функций.

**Рекомендации по улучшению**:
- Заменить все `...` на конкретную реализацию или поясняющие комментарии.
- Добавить подробные docstring в формате RST для всех функций и классов.
- Использовать только одинарные кавычки в коде, двойные - только для `print`, `input` и `logger`.
- Избегать `time.sleep()` в пользу асинхронных задержек, если это необходимо, или более эффективных механизмов ожидания.
- Заменить стандартные `try-except` блоками на логирование ошибок через `logger.error`.
- Устранить избыточность импортов, оставив только необходимые.
- Добавить проверку на существование файла конфигурации перед его чтением.
- Выровнять имена переменных и функций по PEP8.
- Оптимизировать код, убрав дублирование.
- Все импорты должны быть отсортированы.
- Удалить неиспользуемый импорт `header`.
- Описать все переменные типов.

**Оптимизированный код**:
```python
"""
Модуль для работы с дизайном и продвижением изображений.
=========================================================

Модуль содержит класс :class:`EmilDesign`, который используется для описания,
продвижения и загрузки изображений на различные платформы, включая Facebook и PrestaShop.

Пример использования
--------------------
.. code-block:: python

    emil = EmilDesign()
    asyncio.run(emil.upload_to_prestashop(lang='he'))
    # asyncio.run(emil.describe_images(lang='he'))
    # emil.promote_to_facebook()
"""
from __future__ import annotations

import asyncio
import time
from pathlib import Path
from typing import Optional
from types import SimpleNamespace

# Сторонние библиотеки
from src import gs

# Веб-драйверы
from src.webdriver.chrome import Chrome
from src.webdriver.driver import Driver

# AI модели
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel

# Обработка товаров
from src.endpoints.prestashop.product_async import ProductAsync
from src.endpoints.prestashop.product_fields import ProductFields

# Работа с соцсетями
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_message,
)

# Утилиты
from src.utils.convertors.ns import ns2dict
from src.utils.file_async import get_filenames_from_directory, read_text_file, save_text_file
from src.utils.image import get_image_bytes, get_raw_image_data
from src.utils.jjson import j_dumps, j_loads_ns
# Логирование
from src.logger.logger import logger


class EmilDesign:
    """
    Класс для проектирования и продвижения изображений через различные платформы.

    :cvar ENDPOINT: Конечная точка (endpoint) для данного модуля.
    :vartype ENDPOINT: str
    :cvar base_path: Базовый путь к файлам конфигурации.
    :vartype base_path: Path
    :cvar config: Конфигурация модуля.
    :vartype config: SimpleNamespace
    :cvar data_path: Путь к данным модуля.
    :vartype data_path: Path
    :ivar gemini: Экземпляр модели Google Gemini.
    :vartype gemini: GoogleGenerativeAI
    :ivar openai: Экземпляр модели OpenAI.
    :vartype openai: OpenAIModel
    """

    # ---------------------------------
    ENDPOINT: str = 'emil'
    # ---------------------------------

    gemini: 'GoogleGenerativeAI'
    openai: 'OpenAIModel'

    base_path: Path = gs.path.endpoints / ENDPOINT
    config: SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')  # Load configuration
    data_path: Path = getattr(gs.path, config.storage, 'external_storage') / ENDPOINT

    def __init__(self) -> None:
        """
        Инициализирует класс EmilDesign.

        :raises FileNotFoundError: Если файл конфигурации не найден.
        """
        if not (self.base_path / f'{self.ENDPOINT}.json').exists():  # check for config file
            logger.error(f'Config file not found: {self.base_path / f"{self.ENDPOINT}.json"}')
            raise FileNotFoundError(f'Config file not found: {self.base_path / f"{self.ENDPOINT}.json"}')
        logger.info(f'EmilDesign initialized with config: {self.config}')

    async def describe_images(self, lang: str) -> None:
        """
        Описывает изображения на основе предоставленных инструкций и примеров.

        :param lang: Язык, на котором будет выполняться описание.
        :type lang: str
        :raises Exception: Если возникает ошибка во время обработки.

        .. code-block:: python

            emil = EmilDesign()
            asyncio.run(emil.describe_images(lang='he'))

        """
        # 1. Initialize the AI model with the system instructions
        system_instruction: str = (
            Path(self.base_path / 'instructions' / f'hand_made_furniture_{lang}.md')
            .read_text(encoding='UTF-8')
        )

        use_openai: bool = False
        if use_openai:
            self.openai = OpenAIModel(
                system_instruction=system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43'
            )

        use_gemini: bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                api_key=gs.credentials.gemini.emil,
                model_name='gemini-1.5-flash',
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'},
            )
        # 2. Define paths for examples, images directory, and output file

        furniture_categories: str = (
            Path(self.base_path / 'categories' / 'main_categories_furniture.json')
            .read_text(encoding='UTF-8')
            .replace(r'\n', '')
            .replace(r'\t', '')
        )
        system_instruction += furniture_categories

        output_file: Path = self.data_path / f'described_images_{lang}.json'

        described_images_path: Path = self.data_path / 'described_images.txt'
        described_images: list[str] = read_text_file(described_images_path, as_list=True) or []

        # 3. Define images paths
        images_dir: Path = self.data_path / 'images' / 'furniture_images'
        images_files_list: list[str] = get_filenames_from_directory(images_dir)

        # 4. Subtract described images from the list of all images
        images_to_process: list[str] = [
            img for img in images_files_list if str(images_dir / img) not in described_images
        ]

        # 5. Define output file
        output_json: Path = Path(self.data_path / f'out_{gs.now}_{lang}.json')
        data: list[SimpleNamespace] = []  # <- список всех обработанных данных

        for img in images_to_process:
            print(f'starting process file {img}\nsleep for 20 sec')
            await asyncio.sleep(20) # replaced time.sleep() with asyncio.sleep()
            img_path: str = str(images_dir / img)  # Store the full path for saving

            # here are two different types of byte image content.
            # If the model swears at one, then you can choose another
            # - using Pillow and returns its bytes in JPEG format
            try:
                img_bytes: bytes = get_image_bytes(images_dir / img)
                # - raw binary data of a file
                raw_img_data: bytes = get_raw_image_data(images_dir / img)
                response: str = await self.gemini.describe_image(
                    image=raw_img_data, mime_type='image/jpeg', prompt=system_instruction
                )
            except Exception as e:
                logger.error(f'Error processing image {img}: {e}')
                continue  # Skip to next image in case of an error

            if not response:
                logger.error(f'No response for image {img}')
                continue

            # Process the response into a structured format
            try:
                res_ns: SimpleNamespace | list[SimpleNamespace] = j_loads_ns(response)
                res_ns: SimpleNamespace = res_ns[0] if isinstance(res_ns, list) else res_ns
                setattr(res_ns, 'local_image_path', str(Path(images_dir / img)))
                # append structured data to list of products
                data.append(res_ns)
                j_dumps(data, output_json)

                # Add the processed image path to the list and save to file
                described_images.append(img_path)
                await save_text_file(described_images_path, described_images)

            except Exception as e:
                logger.error(f'Error processing response for image {img}: {e}')

        logger.info(f'Images described and saved to {output_json}')

    async def promote_to_facebook(self) -> None:
        """
        Продвигает изображения и их описания в Facebook.

        Эта функция входит в Facebook и публикует сообщения, полученные из описаний изображений.

        :raises Exception: Если возникает ошибка во время работы с Facebook.
        """
        d = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        messages: SimpleNamespace | list[SimpleNamespace] = j_loads_ns(
            self.base_path / 'images_descritions_he.json'
        )

        for m in messages:
            message: SimpleNamespace = SimpleNamespace()
            setattr(message, 'title', f'{m.parent}\n{m.category}')
            setattr(message, 'description', m.description)
            message.products = SimpleNamespace()
            setattr(message.products, 'local_image_path', [m.local_image_path])

            try:
                post_message(d, message, without_captions=True)
            except Exception as e:
                logger.error(f'Error posting to Facebook: {e}')

    async def upload_to_prestashop(
        self, products_list: Optional[SimpleNamespace | list[SimpleNamespace]] = None, lang: Optional[str] = None
    ) -> bool:
        """
        Загружает информацию о продуктах в PrestaShop.

        Инициализирует продукт и экземпляр PrestaShop для загрузки данных.

        :param products_list: Список продуктов для загрузки.
        :type products_list: Optional[SimpleNamespace | list[SimpleNamespace]]
        :param lang: Язык, на котором будет загружаться продукт.
        :type lang: Optional[str]
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        :raises Exception: Если возникает ошибка во время загрузки в PrestaShop.
        """
        products_list = products_list if products_list else j_loads_ns(
            self.data_path / 'out_250108230345305_he.json'
        )
        lang_ns = j_loads_ns(self.base_path / 'shop_locales' / 'locales.json')
        lang_index = getattr(lang_ns, lang)
        # convert to ProductFields
        f: ProductFields = ProductFields(lang_index=lang_index or lang_ns.he)
        host: str = gs.credentials.presta.client.emil_design.api_domain
        api_key: str = gs.credentials.presta.client.emil_design.api_key

        for product_ns in products_list:
            # convert to prestashop fields
            f.name = product_ns.name
            f.id_category_default = product_ns.id_category_default
            f.id_supplier = 11366  # https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ
            f.description = product_ns.description
            f.images_urls = product_ns.local_image_path

            try:
                p: ProductAsync = ProductAsync(api_domain=host, api_key=api_key)
                product_id: int = await p.add_new_product(f)
                logger.info(f'Product {product_ns.name} uploaded with ID: {product_id}')
            except Exception as e:
                logger.error(f'Error uploading product {product_ns.name}: {e}')
                return False
        logger.info('All products uploaded to PrestaShop')
        return True


if __name__ == '__main__':
    emil = EmilDesign()
    asyncio.run(emil.upload_to_prestashop(lang='he'))
    # asyncio.run(emil.describe_images(lang='he'))
    # emil.promote_to_facebook()