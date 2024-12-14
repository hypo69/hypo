# Анализ кода модуля `emil_design.py`

**Качество кода**
1/10
- Плюсы
    - Присутствует базовая структура класса.
    - Используются импорты для необходимых модулей.
    - Есть разделение на функции для описания изображений, продвижения в Facebook и загрузки в PrestaShop.
- Минусы
    - Отсутствует docstring у модуля.
    - Очень много повторений `""" ... """`.
    - Отсутствует обработка ошибок, используется `...` для остановки в неожиданных моментах.
    - Не используются `j_loads` и `j_dumps` из `src.utils.jjson` в некоторых местах.
    - Не все функции и методы имеют docstring, который соответствуют reStructuredText (RST) формату.
    - Не используются логи в нужных местах, где это требуется, как в блоке except.
    - Код не соответствует PEP 8.
    - Присутствует неиспользуемый импорт `header`.
    - Не все переменные имеют тип.
    - Используется `time.sleep` в коде, что может замедлить работу скрипта.
    -  `SimpleNamespace` используется без явной надобности.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате reStructuredText (RST) для модуля, класса и всех функций.
    -   Переписать все комментарии в формате RST.
2.  **Импорты**:
    -   Удалить неиспользуемый импорт `header`.
3.  **Обработка ошибок**:
    -   Заменить использование `...` на логирование ошибок с помощью `logger.error` и  обработкой исключений.
4.  **Работа с JSON**:
    -  Использовать `j_loads` и `j_dumps` из `src.utils.jjson`.
5.  **Переменные**:
    -   Добавить аннотации типов для переменных.
6. **Логирование**:
    -   Добавить логирование для важных операций и ошибок.
7.  **Удаление лишнего кода**:
    -   Удалить лишние комментарии.
8.  **Улучшить читаемость**:
    -   Улучшить читаемость кода, разбив длинные строки и добавив поясняющие комментарии.
9.  **`SimpleNamespace`**:
    -   Пересмотреть использование `SimpleNamespace` и использовать более структурированные данные, если это необходимо.
10. **Задержки**:
    -  Удалить `time.sleep`, так как это замедляет код, если это не является необходимостью для теста.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для управления и обработки изображений, а также их продвижения на Facebook и PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`EmilDesign`, который используется для описания,
продвижения и загрузки изображений на различные платформы, включая Facebook и PrestaShop.

Пример использования
--------------------

Пример использования класса `EmilDesign`:

.. code-block:: python

    emil_design = EmilDesign()
    emil_design.describe_images()
    emil_design.promote_to_facebook()
    emil_design.upload_to_PrestaShop()

"""
from pathlib import Path
from typing import List
import time

from src import gs
from src.endpoints.PrestaShop.api.api import PrestaShop
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel
from src.product import Product
from src.endpoints.advertisement.facebook.scenarios.post_message import post_message
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger.logger import logger

MODE: str = 'dev'


class EmilDesign:
    """
    Класс для проектирования и продвижения изображений через различные платформы.
    """

    base_path: Path = (
        gs.path.google_drive
        / "emil"
    )
    """
    Базовый путь к данным модуля.

    :type: pathlib.Path
    """

    def __init__(self) -> None:
        """
        Инициализирует класс EmilDesign.
        """
        pass  # TODO: Добавить инициализацию переменных, если это необходимо

    def describe_images(self, from_url: bool = False) -> None:
        """
        Описывает изображения на основе предоставленной инструкции и примеров.

        :param from_url: Если True, использует URL для описания изображений. По умолчанию False.
        :type from_url: bool
        """
        # Определяем пути к файлам с инструкциями, примерами, директории с изображениями и выходному файлу
        system_instruction_path: Path = (
            self.base_path
            / 'instructions'
            / 'hand_made_furniture_he.txt'
        )
        """Путь к файлу с системными инструкциями."""
        examples_path: Path = (
            self.base_path
            / 'instructions'
            / "examples_he.txt"
        )
        """Путь к файлу с примерами."""
        images_dir: Path = (
            self.base_path
            / "images"
        )
        """Путь к директории с изображениями."""
        output_file: Path = (
            self.base_path
            / "images_descritions_he.json"
        )
        """Путь к выходному файлу."""
        base_url: str = r'https://emil-design.com/img/images_emil/'
        """Базовый URL для изображений."""
        updated_images_path: Path = self.base_path / 'updated_images.txt'
        """Путь к файлу со списком обработанных изображений."""

        try:
            # Чтение системных инструкций и примеров из файлов
            system_instruction: str = read_text_file(system_instruction_path)
            examples: str = read_text_file(examples_path)
        except Exception as e:
            logger.error(f"Ошибка чтения файлов инструкций или примеров: {e}")
            return

        # Prompt для модели ИИ
        prompt: str = "איזה רהיטים מוצגים כאן?"
        """Текст запроса к ИИ."""

        # Инициализация модели ИИ
        model: OpenAIModel = OpenAIModel(
            system_instruction=system_instruction,
            assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43'
        )

        # Запрос модели на категоризацию примеров
        try:
            response: str = model.ask(examples, "this is example for build categories")
            logger.info(response)
        except Exception as e:
             logger.error(f"Ошибка запроса к модели ИИ: {e}")
             return

        # Чтение списка обновленных изображений
        updated_images_list: List[str] = read_text_file(updated_images_path, as_list=True) or []
        """Список путей к обновленным изображениям."""

        # Получаем список путей ко всем изображениям
        images_path_list: List[str] = get_filenames(images_dir)
        """Список путей ко всем изображениям."""
        data: List[object] = []
        """Список для хранения данных об изображениях."""
        # Перебор всех путей к изображениям
        for image_path in images_path_list:
            # Проверяем, было ли изображение обработано
            if image_path in updated_images_list:
                continue

            # Описываем изображение, либо по URL, либо по локальному пути
            try:
                if from_url:
                    response: str = model.describe_image(
                        str(base_url + image_path), prompt, system_instruction
                    )  # <- url
                else:
                    response: str = model.describe_image(
                         images_dir / image_path, prompt, system_instruction
                     )  # <- local file
            except Exception as e:
                logger.error(f"Ошибка при описании изображения {image_path}: {e}")
                continue

            # Проверяем, был ли получен ответ
            if not response:
                continue

            # Преобразуем ответ в структурированный формат
            try:
                res_ns = j_loads_ns(response)
                setattr(res_ns, 'local_saved_image', str(Path(images_dir / image_path)))
                data.append(res_ns)
                j_dumps(data, output_file)
                updated_images_list.append(image_path)
                save_text_file(updated_images_list, updated_images_path)
                logger.info(response)
            except Exception as e:
                logger.error(f"Ошибка обработки ответа {response} {e}")
                continue

    def promote_to_facebook(self) -> None:
        """
        Продвигает изображения и их описания в Facebook.

        Эта функция входит в Facebook и публикует сообщения, основанные на описаниях изображений.
        """
        d: Driver = Driver(Chrome)
        """Драйвер для управления браузером Chrome."""
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        try:
             messages = j_loads_ns(self.base_path / "images_descritions_he.json")
        except Exception as e:
             logger.error(f'Ошибка чтения файла JSON {e}')
             return

        if not messages:
             logger.warning(f'Нет данных для постинга')
             return

        for m in messages:
            try:
               message =  j_loads_ns('{}')
               setattr(message, 'title', f"{m.parent}\\n{m.category}")
               setattr(message, 'description', m.description)
               setattr(message, 'products', j_loads_ns('{}'))
               setattr(message.products, 'local_saved_image', [m.local_saved_image])

               post_message(d, message, without_captions=True)
            except Exception as e:
                 logger.error(f'Ошибка создания сообщения для поста {e}')
                 continue


    def upload_to_PrestaShop(self) -> None:
        """
        Загружает информацию о продукте в PrestaShop.

        Эта функция инициализирует продукт и экземпляр PrestaShop для загрузки данных.
        """
        p: Product = Product()
        """Экземпляр класса Product."""
        presta: PrestaShop = PrestaShop()
        """Экземпляр класса PrestaShop."""


if __name__ == "__main__":
    e: EmilDesign = EmilDesign()
    # e.describe_images()
    # e.promote_to_facebook()
```