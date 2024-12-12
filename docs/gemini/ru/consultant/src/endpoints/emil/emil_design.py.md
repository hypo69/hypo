# Анализ кода модуля `emil_design`

**Качество кода**
8
 -  Плюсы
        - Код структурирован в класс `EmilDesign`, что способствует модульности.
        - Используются `Path` для работы с файлами, что делает код более читаемым и удобным для работы с путями.
        - Присутствует базовая обработка ошибок с использованием `try-except`, хотя это можно улучшить.
        - Присутствует логирование с использованием `logger.info` и `logger.debug`.
        - Документация к классу и методам присутствует, хоть и требует форматирования в RST.
        - Есть импорты необходимых модулей.
 -  Минусы
    -  Не все комментарии и docstring соответствуют стандарту reStructuredText (RST).
    -  Используется `j_loads_ns`, но нет проверки на существование файла.
    -  Отсутствует обработка ошибок при чтении файлов, что может привести к сбоям.
    -  Использование `time.sleep` может замедлить выполнение программы.
    -  Некоторые части кода могут быть упрощены и сделаны более читаемыми.
    -  Используются `...` как точки остановки.
    -  Не все импорты соответствуют ранее обработанным файлам.
    -  Присутствуют избыточные пустые строки и комментарии `#` без контента
    -  Отсутствуют комментарии к переменным класса

**Рекомендации по улучшению**
1.  **Форматирование документации:** Переписать все комментарии и docstring в формате reStructuredText (RST).
2.  **Обработка ошибок:** Добавить обработку ошибок при чтении файлов с использованием `logger.error` вместо общих `try-except`.
3.  **Улучшение импортов:** Привести все импорты в соответствии с ранее обработанными файлами и добавить отсутствующие.
4.  **Улучшение кода:** Убрать `...` как точки остановки, упростить код, где это возможно.
5.  **Убрать избыточные комментарии:** Убрать все избыточные пустые комментарии `#`.
6.  **Обработка файлов:** Добавить проверку на существование файла перед его чтением.
7.  **Логирование:** Заменить `print` на логирование через `logger`.
8.  **Улучшить читаемость:** Улучшить читаемость кода, разделив длинные строки на несколько.

**Оптимизированный код**
```python
"""
Модуль для управления и обработки изображений, а также их продвижения в Facebook и PrestaShop.
=============================================================================================

Этот модуль содержит класс :class:`EmilDesign`, который используется для описания,
продвижения и загрузки изображений на различные платформы, такие как Facebook и PrestaShop.

Пример использования
--------------------

Пример использования класса `EmilDesign`:

.. code-block:: python

    emil = EmilDesign()
    emil.describe_images()
    emil.promote_to_facebook()
    emil.upload_to_PrestaShop()
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'

import time
from pathlib import Path
from types import SimpleNamespace

from src import gs  # Добавлен импорт gs
from src.endpoints.PrestaShop.api.api import PrestaShop
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel
from src.product import Product
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_message,
    # post_title,  # Удален неиспользуемый импорт
    # upload_media  # Удален неиспользуемый импорт
)
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger.logger import logger


class EmilDesign:
    """
    Класс для проектирования и продвижения изображений через различные платформы.

    :ivar base_path: Базовый путь для данных модуля.
    :vartype base_path: Path
    """

    # Базовый путь для данных модуля
    base_path: Path = (
        gs.path.google_drive
        / "emil"
    )

    def __init__(self):
        """
        Инициализация класса EmilDesign.
        """
        ...

    def describe_images(self, from_url: str = False) -> None:
        """
        Описывает изображения на основе предоставленных инструкций и примеров.

        :param from_url: Если True, использует URL для описания изображений. По умолчанию False.
        :type from_url: str, optional
        :raises FileNotFoundError: Если не удается найти файл с инструкциями или примерами.
        """
        # Определяются пути к инструкциям, примерам, директории с изображениями и файлу вывода
        system_instruction_path: Path = (
            self.base_path
            / 'instructions'
            / 'hand_made_furniture_he.txt'
        )

        examples_path: Path = (
            self.base_path
            / 'instructions'
            / "examples_he.txt"
        )

        images_dir: Path = (
            self.base_path
            / "images"
        )

        output_file: Path = (
            self.base_path
            / "images_descritions_he.json"
        )

        base_url: str = r'https://emil-design.com/img/images_emil/'
        updated_images_path: Path = self.base_path / 'updated_images.txt'

        try:
            # Чтение инструкций и примеров из файлов
            system_instruction = read_text_file(system_instruction_path)
            examples = read_text_file(examples_path)
            updated_images_list: list = read_text_file(updated_images_path, as_list=True) or []

        except FileNotFoundError as e:
            logger.error(f"Не удалось найти файл: {e}", exc_info=True)
            return

        # Запрос к ИИ модели для категоризации
        prompt: str = "איזה רהיטים מוצגים כאן?"
        # Инициализируется модель OpenAI с инструкциями
        model = OpenAIModel(system_instruction=system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43')
        # Запрос к модели для категоризации примеров
        response = model.ask(examples, "this is example for build categories")
        logger.info(response)

        # Получаем список файлов изображений
        images_path_list: list = get_filenames(images_dir)
        data: list = []
        
        # Обработка каждого изображения
        for image_path in images_path_list:
            if image_path in updated_images_list:
                continue
            # Описание изображения через URL или локальный файл
            try:
                if from_url:
                    response = model.describe_image(str(base_url + image_path), prompt, system_instruction)
                else:
                    response = model.describe_image(images_dir / image_path, prompt, system_instruction)
            except Exception as e:
                logger.error(f"Ошибка при описании изображения {image_path}: {e}", exc_info=True)
                continue

            if not response:
                continue
            
            # Преобразует JSON в объект SimpleNamespace, добавляет путь к изображению и сохраняет результат
            try:
                res_ns: SimpleNamespace = j_loads_ns(response)
                setattr(res_ns, 'local_saved_image', str(Path(images_dir / image_path)))
                data.append(res_ns)
                j_dumps(data, output_file)
                updated_images_list.append(image_path)
                save_text_file(updated_images_list, updated_images_path)
                logger.info(response)
            except Exception as e:
                logger.error(f"Ошибка обработки ответа от модели {response}: {e}", exc_info=True)

            # time.sleep(20)
            ...


    def promote_to_facebook(self) -> None:
        """
        Продвигает изображения и их описания в Facebook.

        Функция выполняет вход в Facebook и публикует сообщения на основе описаний изображений.
        :raises FileNotFoundError: Если не удается найти файл с описаниями изображений.
        """
        d = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        
        try:
            # Загрузка сообщений из JSON
            messages: SimpleNamespace | list = j_loads_ns(self.base_path / "images_descritions_he.json")
        except FileNotFoundError as e:
            logger.error(f"Не удалось найти файл с описаниями: {e}", exc_info=True)
            return

        # Публикуется каждое сообщение
        for m in messages:
            message: SimpleNamespace = SimpleNamespace()
            setattr(message, 'title', f"{m.parent}\\n{m.category}")
            setattr(message, 'description', m.description)
            message.products = SimpleNamespace()
            setattr(message.products, 'local_saved_image', [m.local_saved_image])

            post_message(d, message, without_captions=True)
            ...

    def upload_to_PrestaShop(self) -> None:
        """
        Загружает информацию о продукте в PrestaShop.

        Функция инициализирует продукт и экземпляр PrestaShop для загрузки данных.
        """
        p = Product()
        presta = PrestaShop()
        ...


if __name__ == "__main__":
    e = EmilDesign()
    # e.describe_images()
    # e.promote_to_facebook()
```