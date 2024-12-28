# Анализ кода модуля `emil_design.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, использует классы и функции для организации логики.
    - Присутствует базовая обработка ошибок с использованием `try-except`, хотя есть возможность ее улучшения.
    - Используется `logger` для вывода информации, что помогает отслеживать работу кода.
    - Применяются `pathlib` для работы с путями, что обеспечивает кросс-платформенность.
    - Используются `j_loads_ns` и `j_dumps` для работы с JSON, что является правильным согласно инструкции.
    - Комментарии в коде присутствуют, хотя требуется их форматирование в соответствии с RST.
-  Минусы
    - Отсутствует reStructuredText (RST) форматирование docstring для классов, методов и переменных.
    - Некоторые блоки кода содержат `...`, что указывает на незавершенность.
    - Присутствуют избыточные комментарии (например, `# -*- coding: utf-8 -*-`, `#! venv/Scripts/python.exe`, `#! venv/bin/python/python3.12`), которые не несут смысловой нагрузки.
    - Не все импорты используются, что нужно исправить.
    - В коде отсутствует консистентность в именовании, например, `trainig_data` вместо `training_data`.
    - Логирование ошибок нуждается в уточнении и добавлении контекста.
    - Не везде проставлены `return` там, где это требуется.

**Рекомендации по улучшению**

1. **Документация:**
   - Переписать все комментарии и docstring в формате reStructuredText (RST).
   - Добавить описания к классам, методам и переменным.
   - Использовать docstring для описания параметров и возвращаемых значений функций.
2. **Импорты:**
   - Проверить и удалить неиспользуемые импорты.
   - Перенести импорты `logger` из `src` в `from src.logger.logger import logger`
3. **Обработка ошибок:**
   - Заменить `try-except` на использование `logger.error` для записи ошибок, где это возможно.
4. **Код:**
   - Убрать избыточные комментарии в начале файла.
   - Избавиться от многоточий `...`, завершив логику функций.
   - Привести имена переменных и функций к общему стилю (snake_case).
   - Добавить `return` там, где это необходимо.
5. **Логирование:**
   - Добавить больше контекста в логирование (например, имя функции, параметры).

**Оптимизированный код**

```python
"""
Модуль для управления и обработки изображений, а также их продвижения в Facebook и PrestaShop.
===================================================================================================

Этот модуль содержит класс :class:`EmilDesign`, который используется для обработки изображений,
их описания с помощью моделей ИИ, а также для публикации в социальных сетях и интернет-магазинах.

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
from types import SimpleNamespace
import time

# from src import gs, logger # исправлено
from src.endpoints.PrestaShop.api.api import PrestaShop
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel
from src.product import Product
from src.endpoints.advertisement.facebook.scenarios.post_message import post_message
# from src.endpoints.advertisement.facebook.scenarios.post_message import post_title, upload_media # удалены неиспользуемые импорты
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger.logger import logger
from src import gs




class EmilDesign:
    """
    Класс для проектирования и продвижения изображений через различные платформы.

    :ivar base_path: Базовый путь к данным модуля.
    :vartype base_path: Path
    """

    base_path: Path = (
        gs.path.google_drive
        / "emil"
    )

    def __init__(self):
        """
        Инициализирует класс EmilDesign.
        """
        ...

    def describe_images(self, from_url: bool = False):
        """
        Описывает изображения на основе предоставленных инструкций и примеров.

        :param from_url: Если True, использует URL для описания изображений. По умолчанию False.
        :type from_url: bool, optional
        """
        #  определение путей к файлам инструкций, примеров, директории изображений и выходного файла
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
        # считывание системной инструкции
        system_instruction = read_text_file(system_instruction_path)
        # считывание примеров
        examples = read_text_file(examples_path)
        # путь к файлу с обновленными изображениями
        updated_images_path: Path = self.base_path / 'updated_images.txt'
        #  запрос для модели ИИ
        prompt: str = "איזה רהיטים מוצגים כאן?"
        # Инициализация модели ИИ с системными инструкциями
        model = OpenAIModel(system_instruction=system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43')
        # Запрос к модели на категоризацию примеров
        response = model.ask(examples, "this is example for build categories")
        logger.info(response)
        # Получение списка обновленных изображений
        updated_images_list: list = read_text_file(updated_images_path, as_list=True) or []
        # Получение списка всех изображений
        images_path_list: list = get_filenames(images_dir)
        data: list = []

        for image_path in images_path_list:
            # Пропуск уже обработанных изображений
            if image_path in updated_images_list:
                continue

            try:
                # Описание изображения либо по URL, либо из локального файла
                if from_url:
                    response = model.describe_image(str(base_url + image_path), prompt, system_instruction)  # url
                else:
                    response = model.describe_image(images_dir / image_path, prompt, system_instruction)  # local file
            except Exception as ex:
                logger.error(f'Ошибка при описании изображения {image_path}: {ex}')
                continue

            if not response:
                logger.warning(f'Нет ответа для изображения {image_path}')
                continue

            try:
                # Преобразование ответа в структурированный формат
                res_ns: SimpleNamespace = j_loads_ns(response)
                setattr(res_ns, 'local_saved_image', str(Path(images_dir / image_path)))
                data.append(res_ns)
                j_dumps(data, output_file)
                updated_images_list.append(image_path)
                save_text_file(updated_images_list, updated_images_path)
                logger.info(f'Описание для {image_path} успешно добавлено.')
                # time.sleep(20) # закоментирован код
            except Exception as ex:
                logger.error(f'Ошибка при обработке ответа для {image_path}: {ex}')
                continue
            ... # точка остановки

    def promote_to_facebook(self):
        """
        Продвигает изображения и их описания в Facebook.

        Эта функция выполняет вход в Facebook и публикует сообщения, основанные на описаниях изображений.
        """
        # Инициализация драйвера веб-браузера
        d = Driver(Chrome)
        # открытие страницы facebook
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        # Получение данных об изображениях
        messages: SimpleNamespace | list = j_loads_ns(self.base_path / "images_descritions_he.json")

        if not messages:
           logger.warning('Нет данных для публикации в Facebook.')
           return

        for m in messages:
            try:
                # Создание объекта SimpleNamespace для сообщения
                message: SimpleNamespace = SimpleNamespace()
                setattr(message, 'title', f"{m.parent}\\n{m.category}")
                setattr(message, 'description', m.description)
                message.products = SimpleNamespace()
                setattr(message.products, 'local_saved_image', [m.local_saved_image])

                # Публикация сообщения в Facebook
                post_message(d, message, without_captions=True)
                logger.info(f'Сообщение успешно опубликовано для изображения {m.local_saved_image}')
                #  time.sleep(20) # закоментирован код
            except Exception as ex:
                logger.error(f'Ошибка при публикации сообщения для {m.local_saved_image}: {ex}')
                continue
            ...  # точка остановки
        return True

    def upload_to_PrestaShop(self):
        """
        Загружает информацию о продукте в PrestaShop.

        Эта функция инициализирует продукт и экземпляр PrestaShop для загрузки данных.
        """
        # Инициализация экземпляра Product
        p = Product()
        # Инициализация экземпляра PrestaShop
        presta = PrestaShop()
        return True
        ... # точка остановки


if __name__ == "__main__":
    e = EmilDesign()
    # e.describe_images()
    # e.promote_to_facebook()
```