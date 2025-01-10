# Анализ кода модуля `emil_design`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что облегчает его понимание и поддержку.
    - Используются асинхронные операции, что улучшает производительность при работе с I/O.
    - Применение `SimpleNamespace` для хранения данных упрощает доступ к атрибутам.
    - Код содержит docstrings для функций, что помогает документировать код.
    - Использование `Path` для работы с путями обеспечивает кроссплатформенную совместимость.
    - Код использует кастомные утилиты для работы с файлами, json, и изображениями, что способствует переиспользованию кода.
    - Присутствует базовая обработка ошибок через `try-except` блоки.
-  Минусы
    -  Не все docstring соответствуют стандарту reStructuredText (RST).
    -  Не всегда используется `logger.error` для обработки ошибок, предпочитая `...`.
    -  Присутствует избыточное использование `try-except` блоков.
    -  Используются как двойные так и одинарные кавычки в строках.
    -  Некоторые комментарии не полные и требуют больше конкретики.
    -  Не везде соблюдено именование переменных, иногда можно более явно.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Привести все docstring к формату reStructuredText (RST).
    *   Добавить примеры использования функций, особенно для `save_text_file`.
    *   Убедиться, что все параметры и возвращаемые значения функций документированы.
2.  **Логирование:**
    *   Заменить `...` на `logger.error` в обработке ошибок, где это необходимо.
    *   Использовать `logger.debug` для отладочной информации, особенно для невалидных результатов.
3.  **Обработка ошибок:**
    *   Избегать избыточных `try-except` блоков, использовать `logger.error` для логирования ошибок.
4.  **Стиль кода:**
    *   Использовать одинарные кавычки (`'`) для строк в коде.
    *   Придерживаться единого стиля именования переменных, функций и методов.
    *   Более явно называть переменные, где это возможно.
5.  **Производительность:**
    *   Избегать блокировок `time.sleep(20)` во время обработки изображений. Рассмотреть асинхронные таймеры или другие способы ожидания.
6.  **Улучшение комментариев:**
    *  Более подробно комментировать каждый блок кода, объясняя его назначение.

**Оптимизированный код**

```python
"""
Модуль для управления и обработки изображений, а также продвижения в Facebook и PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`EmilDesign`, который используется для обработки изображений,
их описания с помощью моделей ИИ (Google Gemini и OpenAI), и дальнейшего продвижения
на платформах Facebook и PrestaShop.

Пример использования
--------------------

Пример использования класса `EmilDesign`:

.. code-block:: python

    emil = EmilDesign()
    asyncio.run(emil.describe_images(lang='he'))
"""
from __future__ import annotations

import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

# Сторонние библиотеки
from src import gs
from src.logger.logger import logger

# Веб-драйверы
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
# TODO: Add drivers e.g. Edge, crawlee_python, playwright

# AI модели
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel

# Обработка товаров
from src.endpoints.prestashop.product_fields import ProductFields
from src.endpoints.prestashop.product_async import ProductAsync

# Работа с соцсетями
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_message,
)

# Утилиты
from src.utils.file_async import read_text_file, save_text_file, get_filenames_from_directory
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes, get_raw_image_data


class EmilDesign:
    """
    Класс для обработки изображений и их продвижения на различных платформах.

    :cvar ENDPOINT: Имя эндпоинта для конфигурации.
    :vartype ENDPOINT: str
    :ivar gemini: Экземпляр модели Google Gemini.
    :vartype gemini: GoogleGenerativeAI
    :ivar openai: Экземпляр модели OpenAI.
    :vartype openai: OpenAIModel
    :ivar base_path: Базовый путь к файлам конфигурации.
    :vartype base_path: Path
    :ivar config: Конфигурация эндпоинта.
    :vartype config: SimpleNamespace
    :ivar data_path: Путь к данным эндпоинта.
    :vartype data_path: Path
    """

    # ---------------------------------
    ENDPOINT: str = 'emil'
    # ---------------------------------

    gemini: 'GoogleGenerativeAI'
    openai: 'OpenAIModel'

    base_path: Path = gs.path.endpoints / ENDPOINT
    config: SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')
    
    data_path: Path = getattr(gs.path, config.storage, 'external_storage') / ENDPOINT
    
    def __init__(self):
        """Инициализирует класс EmilDesign."""
        ...

    async def describe_images(self, lang: str):
        """
        Описывает изображения на основе предоставленных инструкций и примеров.

        Args:
            lang (str): Язык, на котором нужно описать изображения.
        """
        # 1. Инициализация модели ИИ с системными инструкциями.
        system_instruction: str = (
            Path(self.base_path / 'instructions' / f'hand_made_furniture_{lang}.md')
            .read_text(encoding='UTF-8')
        )

        use_openai: bool = False
        if use_openai:
            self.openai = OpenAIModel(
                system_instruction=system_instruction,
                assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43',
            )

        use_gemini: bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                api_key=gs.credentials.gemini.emil,
                model_name='gemini-1.5-flash',
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'},
            )

        # 2. Определение путей для примеров, директории с изображениями и выходного файла.
        furniture_categories: str = (
            Path(self.base_path / 'categories' / 'main_categories_furniture.json')
            .read_text(encoding='UTF-8')
            .replace(r'\n', '')
            .replace(r'\t', '')
        )
        system_instruction += furniture_categories

        output_file: Path = self.data_path / f'described_images_{lang}.json'

        described_images_path: Path = self.data_path / 'described_images.txt'
        described_images: list = read_text_file(
            described_images_path, as_list=True
        ) or []

        # 3. Определение путей к изображениям.
        images_dir: Path = self.data_path / 'images' / 'furniture_images'
        images_files_list: list = get_filenames_from_directory(images_dir)

        # 4. Вычитание описанных изображений из списка всех изображений.
        images_to_process = [
            img
            for img in images_files_list
            if str(images_dir / img) not in described_images
        ]

        # 5. Определение выходного файла.
        output_json: Path = Path(self.data_path / f'out_{gs.now}_{lang}.json')

        data: list = []  # список всех обработанных данных
        for img in images_to_process:
            print(f'starting process file {img}\\nsleep for 20 sec')
            time.sleep(20)
            img_path: str = str(images_dir / img)  # Сохранение полного пути

            # два разных типа байтового содержимого картинки.
            # Если модель ругается на один, то можно выбрать другой

            # - Использование Pillow для преобразования в JPEG
            img_bytes: bytes = get_image_bytes(images_dir / img)

            # - получение raw binary data
            raw_img_data: bytes = get_raw_image_data(images_dir / img)

            response: str = await self.gemini.describe_image(
                image=raw_img_data, mime_type='image/jpeg', prompt=system_instruction
            )

            if not response:
                logger.error(f'Не удалось получить описание для изображения {img}')
                continue

            # Преобразование ответа в структурированный формат.
            res_ns: SimpleNamespace | list[SimpleNamespace] = j_loads_ns(response)
            res_ns: SimpleNamespace = (
                res_ns[0] if isinstance(res_ns, list) else res_ns
            )

            setattr(res_ns, 'local_image_path', str(Path(images_dir / img)))

            # добавление структурированных данных в список
            data.append(res_ns)
            j_dumps(data, output_json)

            # добавление пути обработанного изображения в список и сохранение в файл
            described_images.append(img_path)
            await save_text_file(described_images_path, described_images)

    async def promote_to_facebook(self):
        """
        Продвигает изображения и их описания в Facebook.

        Эта функция выполняет вход в Facebook и публикует сообщения на основе описаний изображений.
        """
        d: Driver = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        messages: SimpleNamespace | list = j_loads_ns(
            self.base_path / 'images_descritions_he.json'
        )

        for m in messages:
            message: SimpleNamespace = SimpleNamespace()
            setattr(message, 'title', f'{m.parent}\\n{m.category}')
            setattr(message, 'description', m.description)
            message.products = SimpleNamespace()
            setattr(message.products, 'local_image_path', [m.local_image_path])

            post_message(d, message, without_captions=True)
            ...

    async def upload_to_prestashop(
        self,
        products_list: Optional[SimpleNamespace | list[SimpleNamespace]] = None,
        lang: Optional[str] = None,
    ) -> bool:
        """
        Загружает информацию о товаре в PrestaShop.

        Args:
            products_list (Optional[SimpleNamespace | list[SimpleNamespace]], optional): Список товаров для загрузки.
                Если не указан, загружается из файла `out_{timestamp}_{lang}.json`. Defaults to None.
            lang (Optional[str], optional): Язык для загрузки. Defaults to None.

        Returns:
            bool: Возвращает True, если загрузка прошла успешно.
        """
        products_list: SimpleNamespace | list[
            SimpleNamespace
        ] = products_list if products_list else j_loads_ns(
            self.data_path / 'out_250108230345305_he.json'
        )
        
        if not products_list:
            logger.error('Не удалось загрузить список продуктов для PrestaShop')
            return False
            
        lang_ns:SimpleNamespace = j_loads_ns(
            self.base_path / 'shop_locales' / 'locales.json'
        )

        lang_index: str = getattr(lang_ns, lang)

        # Преобразование к ProductFields
        f: ProductFields = ProductFields(lang_index=lang_index or lang_ns.he)
        host: str = gs.credentials.presta.client.emil_design.api_domain
        api_key: str = gs.credentials.presta.client.emil_design.api_key

        for product_ns in products_list:
            # преобразование к полям PrestaShop
            f.name = product_ns.name
            f.id_category_default = product_ns.category
            f.id_supplier = (
                11366  # https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ
            )
            f.description = product_ns.description
            f.images_urls = product_ns.local_image_path

            p: ProductAsync = ProductAsync(api_domain=host, api_key=api_key)
            product_id: int = await p.add_new_product(f)

        return True

if __name__ == '__main__':
    emil: EmilDesign = EmilDesign()
    asyncio.run(emil.upload_to_prestashop(lang='he'))

    # asyncio.run( emil.describe_images(lang='he') )
    # emil.promote_to_facebook()
```