# Анализ кода модуля `emil_design`

**Качество кода**
   -  Соответствие требованиям по оформлению кода: 7/10
   -  Плюсы:
        - Код структурирован и разбит на функции, что облегчает чтение и понимание.
        - Используются асинхронные операции, что позволяет эффективно работать с вводом-выводом.
        - Присутствуют комментарии, объясняющие назначение основных блоков кода.
   -  Минусы:
        - Не все функции имеют docstring.
        - Не используется `j_loads_ns` для чтения JSON конфигурационных файлов.
        - Присутствуют избыточные комментарии, такие как `здесь два разных типа байтового собедржимого картинки`.
        - Есть неиспользуемый импорт `header`.
        - Отсутствуют обработки ошибок с использованием `logger.error` внутри функций.
        - Используется `time.sleep` для задержки, что не является лучшей практикой в асинхронном коде.

**Рекомендации по улучшению**

1.  **Документирование**:
    *   Добавить docstring к классам, методам и функциям, используя формат RST.
    *   Включить описание аргументов, возвращаемых значений и возможных исключений.

2.  **Импорты**:
    *   Удалить неиспользуемый импорт `header`.
    *   Импортировать `logger` как `from src.logger.logger import logger`.
    *   Проверить и добавить недостающие импорты.

3.  **Конфигурация**:
    *   Использовать `j_loads_ns` для загрузки конфигурационных файлов `emil.json`.

4.  **Логирование**:
    *   Заменить блоки `try-except` на использование `logger.error` для обработки исключений.
    *   Добавить логирование важных этапов выполнения программы.

5.  **Обработка данных**:
    *   Уточнить комментарии, описывающие процесс, например, вместо "здесь два разных типа байтового содержимого картинки" использовать "Код получает байтовое представление изображения двумя различными способами".

6.  **Асинхронность**:
    *   Заменить `time.sleep` на `asyncio.sleep` для асинхронной задержки.

7.  **Общая структура**:
    *   Убедиться, что все переменные, функции и импорты имеют согласованные имена с ранее обработанными файлами.

**Оптимизированный код**

```python
from __future__ import annotations

import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

# Сторонние библиотеки
from src import gs

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
    post_title,
    upload_media,
)

# Утилиты
from src.utils.file_async import read_text_file, save_text_file, get_filenames_from_directory
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes, get_raw_image_data
from src.utils.convertors.ns import ns2dict

# Логирование
from src.logger.logger import logger


"""
Модуль для управления и обработки изображений, а также для их продвижения в Facebook и PrestaShop.
=================================================================================================

Этот модуль содержит класс :class:`EmilDesign`, который используется для описания изображений с помощью AI моделей,
а также для продвижения этих изображений и их описаний в социальных сетях и на платформах электронной коммерции.

Пример использования
--------------------

Пример использования класса `EmilDesign`:

.. code-block:: python

    emil = EmilDesign()
    asyncio.run(emil.describe_images(lang='he'))
"""

class EmilDesign:
    """
    Класс для проектирования и продвижения изображений через различные платформы.

    :var ENDPOINT: Конечная точка для модуля.
    :vartype ENDPOINT: str
    :var gemini: Экземпляр модели Google Gemini.
    :vartype gemini: GoogleGenerativeAI
    :var openai: Экземпляр модели OpenAI.
    :vartype openai: OpenAIModel
    :var base_path: Базовый путь к ресурсам модуля.
    :vartype base_path: Path
    :var config: Конфигурация модуля, загруженная из JSON.
    :vartype config: SimpleNamespace
    :var data_path: Путь к данным модуля.
    :vartype data_path: Path
    """

    # ---------------------------------
    ENDPOINT: str = 'emil'
    # ---------------------------------

    gemini: 'GoogleGenerativeAI'
    openai: 'OpenAIModel'

    base_path: Path = gs.path.endpoints / ENDPOINT
    # config: SimpleNamespace = j_loads_ns( base_path / f'{ENDPOINT}.json') # Загрузка конфигурации
    config: SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')
    
    data_path: Path = getattr(gs.path, config.storage, 'external_storage') / ENDPOINT
    
    def __init__(self):
        """
        Инициализирует класс EmilDesign.

        :raises Exception: Если произошла ошибка при инициализации.
        """
        ...

    async def describe_images(self, lang: str):
        """
        Описывает изображения на основе предоставленных инструкций и примеров.

        :param lang: Язык, на котором нужно описать изображения.
        :type lang: str
        :raises Exception: Если произошла ошибка во время описания изображений.

        :Example:
            >>> emil = EmilDesign()
            >>> asyncio.run(emil.describe_images(lang='he'))
        """
        # 1. Initialize the AI model with the system instructions
        # Код загружает системные инструкции для AI модели из файла.
        try:
            system_instruction: str = Path(
                self.base_path / 'instructions' / f'hand_made_furniture_{lang}.md'
            ).read_text(encoding='UTF-8')
        except Exception as e:
            logger.error(f'Ошибка чтения файла инструкций: {e}')
            return
        use_openai: bool = False
        if use_openai:
            self.openai = OpenAIModel(system_instruction=system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43')

        use_gemini: bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                api_key=gs.credentials.gemini.emil,
                model_name='gemini-1.5-flash',
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )

        # 2. Define paths for examples, images directory, and output file
        # Код загружает категории товаров и формирует путь к файлу вывода.
        try:
            furniture_categories: str = Path(
                self.base_path / 'categories' / 'main_categories_furniture.json'
            ).read_text(encoding='UTF-8').replace(r'\n', '').replace(r'\t', '')
            system_instruction += furniture_categories
        except Exception as e:
              logger.error(f'Ошибка чтения файла категорий мебели: {e}')
              return
        output_file: Path = self.data_path / f"described_images_{lang}.json"

        described_images_path: Path = self.data_path / 'described_images.txt'
        described_images: list = read_text_file(described_images_path, as_list=True) or []

        # 3. Define images paths
        # Код определяет путь к директории с изображениями и получает список файлов.
        images_dir = self.data_path / 'images' / 'furniture_images'
        images_files_list: list = get_filenames_from_directory(images_dir)

        # 4. Subtract described images from the list of all images
        # Код исключает уже описанные изображения из списка.
        images_to_process = [
            img for img in images_files_list if str(images_dir / img) not in described_images
        ]

        # 5. Define output file
        output_json: Path = Path(self.data_path / f'out_{gs.now}_{lang}.json')

        data: list = []  # <- список всех обработанных данных
        for img in images_to_process:
            print(f"starting process file {img}\\nsleep for 20 sec")
            await asyncio.sleep(20)
            img_path = str(images_dir / img)  # Store the full path for saving
            # Код получает байтовое представление изображения двумя различными способами.
            try:
                 # - using Pillow and returns its bytes in JPEG format
                img_bytes = get_image_bytes(images_dir / img)
                # - raw binary data of a file
                raw_img_data = get_raw_image_data(images_dir / img)
                response = await self.gemini.describe_image(
                    image=raw_img_data, mime_type='image/jpeg', prompt=system_instruction
                )
            except Exception as e:
                  logger.error(f'Ошибка при обработке изображения {img}: {e}')
                  continue


            if not response:
                continue

            # Process the response into a structured format
            # Код обрабатывает ответ от AI модели.
            try:
                res_ns: SimpleNamespace | list[SimpleNamespace] = j_loads_ns(response)
                res_ns: SimpleNamespace = res_ns[0] if isinstance(res_ns, list) else res_ns

                setattr(res_ns, 'local_image_path', str(Path(images_dir / img)))
                # Код добавляет структурированные данные в список и сохраняет в JSON файл.
                data.append(res_ns)
                j_dumps(data, output_json)
            except Exception as e:
                 logger.error(f'Ошибка обработки ответа от Gemini {e}')
                 continue


            # Add the processed image path to the list and save to file
            # Код добавляет путь к обработанному изображению в список и сохраняет в файл.
            described_images.append(img_path)
            await save_text_file(described_images_path, described_images)

    async def promote_to_facebook(self):
        """
        Продвигает изображения и их описания в Facebook.

        Эта функция выполняет вход в Facebook и публикует сообщения, основанные на описаниях изображений.

        :raises Exception: Если произошла ошибка во время публикации в Facebook.
        """
        d = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        try:
            messages: SimpleNamespace | list = j_loads_ns(self.base_path / "images_descritions_he.json")
        except Exception as e:
              logger.error(f'Ошибка чтения файла описаний: {e}')
              return

        for m in messages:
            message: SimpleNamespace = SimpleNamespace()
            setattr(message, 'title', f"{m.parent}\\n{m.category}")
            setattr(message, 'description', m.description)
            message.products = SimpleNamespace()
            setattr(message.products, 'local_image_path', [m.local_image_path])

            post_message(d, message, without_captions=True)
            ...

    async def upload_to_prestashop(self, products_list: Optional[SimpleNamespace | list[SimpleNamespace]] = None, lang: Optional[str] = None) -> bool:
        """
        Загружает информацию о товарах в PrestaShop.

        Эта функция инициализирует продукт и экземпляр PrestaShop для загрузки данных.

        :param products_list: Список продуктов для загрузки.
        :type products_list: Optional[SimpleNamespace | list[SimpleNamespace]]
        :param lang: Язык магазина.
        :type lang: Optional[str]
        :return: True, если загрузка прошла успешно, False в противном случае.
        :rtype: bool
        :raises Exception: Если произошла ошибка во время загрузки в PrestaShop.
        """
        # Код загружает список продуктов из JSON файла, если не передан явно.
        if not products_list:
            try:
                products_list = j_loads_ns(self.data_path / "out_250108230345305_he.json")
            except Exception as e:
                logger.error(f'Ошибка при загрузке списка товаров из файла: {e}')
                return False
        
        try:
            lang_ns = j_loads_ns(self.base_path / 'shop_locales' / 'locales.json')
        except Exception as e:
             logger.error(f'Ошибка при загрузке языковых настроек: {e}')
             return False

        lang_index = getattr(lang_ns, lang, None)
        if not lang_index:
            lang_index = lang_ns.he

        # convert to ProductFields
        # Код преобразует данные в формат ProductFields.
        f: ProductFields = ProductFields(lang_index=lang_index)
        host = gs.credentials.presta.client.emil_design.api_domain
        api_key = gs.credentials.presta.client.emil_design.api_key

        for product_ns in products_list:
             # Код устанавливает поля для продукта PrestaShop.
            try:
                f.name = product_ns.name
                f.id_category_default = product_ns.id_category_default
                f.id_supplier = 11366  # https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ
                f.description = product_ns.description
                f.images_urls = product_ns.local_image_path

                p: ProductAsync = ProductAsync(api_domain=host, api_key=api_key)
                product_id = await p.add_new_product(f)
            except Exception as e:
                logger.error(f'Ошибка при добавлении товара {product_ns}: {e}')
                continue

        return True

if __name__ == "__main__":
    emil = EmilDesign()
    asyncio.run(emil.upload_to_prestashop(lang='he'))

    # asyncio.run( emil.describe_images(lang='he')  )
    # emil.promote_to_facebook()