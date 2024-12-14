# Анализ кода модуля `post_message_async.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используется асинхронное программирование, что является плюсом для производительности.
    - Присутствует логирование ошибок, что облегчает отладку.
    - Код использует `SimpleNamespace` для хранения данных, что упрощает работу с атрибутами объектов.
    - Использование `j_loads_ns` для загрузки JSON-файлов.
    - Применены docstring для описания функций.
- Минусы
    -  Некоторые docstring не соответствуют стандарту reStructuredText.
    -  Используется избыточное  `return` без значения.
    -  Некоторые комментарии `#` не содержат подробного объяснения, следующего за ними блока кода.
    -  Не все ошибки обрабатываются через `logger.error`.
    -  В docstring отсутствует описание возвращаемого значения в некоторых случаях.

**Рекомендации по улучшению**

1.  Привести все docstring к формату reStructuredText.
2.  Удалить избыточные  `return` без значения.
3.  В комментариях `#` добавить подробное объяснение следующего за ними блока кода.
4.  Использовать `logger.error` для логирования всех ошибок, избегая общих try-except.
5.  Добавить описание возвращаемого значения в docstring там, где оно отсутствует.
6.  Сделать импорты более явными и упорядоченными.
7.  Уточнить комментарии к функциям и их параметрам.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
# file: hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py
"""
Модуль для асинхронной публикации сообщений в Facebook.
========================================================

Этот модуль содержит функции для автоматизации процесса публикации сообщений,
включая загрузку медиафайлов и добавление описаний.
Модуль использует асинхронные операции для повышения производительности.

Пример использования
--------------------

.. code-block:: python

    driver = Driver(...)
    category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
    products = [SimpleNamespace(local_saved_image="path/to/image.jpg", ...)]
    await promote_post(driver, category, products)
"""
import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

MODE = 'dev'

# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(d: Driver, category: SimpleNamespace) -> Optional[bool]:
    """
    Отправляет заголовок и описание кампании в поле сообщения.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param category: Объект SimpleNamespace, содержащий заголовок и описание.
    :type category: SimpleNamespace
    :return: True, если заголовок и описание отправлены успешно, иначе None.
    :rtype: Optional[bool]

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    # Проверка прокрутки страницы назад
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Прокрутка страницы не удалась при установке заголовка сообщения")
        return None

    # Открытие окна добавления сообщения
    if not d.execute_locator(locator.open_add_post_box):
        logger.error("Не удалось открыть окно добавления сообщения")
        return None

    # Формирование сообщения с заголовком и описанием
    message = f"{category.title}; {category.description};"

    # Отправка сообщения в поле сообщения
    if not d.execute_locator(locator.add_message, message):
        logger.error(f"Не удалось добавить сообщение в поле: {message=}")
        return None

    return True


async def upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> Optional[bool]:
    """
    Загружает медиафайлы и обновляет подписи к изображениям.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param products: Список объектов SimpleNamespace, содержащих пути к медиафайлам.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, нужно ли загружать видео. По умолчанию False.
    :type no_video: bool
    :return: True, если медиафайлы успешно загружены, иначе None.
    :rtype: Optional[bool]

    :raises Exception: Если возникает ошибка при загрузке медиафайлов или обновлении подписей.

    :Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> await upload_media(driver, products)
        True
    """
    # Открытие формы добавления медиа.
    if not d.execute_locator(locator.open_add_foto_video_form):
        return None
    d.wait(0.5)

    # Проверка, что products это список.
    products = products if isinstance(products, list) else [products]
    ret: bool = True

    # Итерация по продуктам и загрузка медиа.
    for product in products:
        media_path = product.local_saved_video if hasattr(product, 'local_saved_video') and not no_video else product.local_saved_image
        try:
            # Загрузка медиафайла.
            if d.execute_locator(locator.foto_video_input, media_path):
                d.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return None
        except Exception as ex:
            logger.error("Ошибка при загрузке медиа", exc_info=True, extra={'exception': ex})
            return None

    # Обновление подписей к загруженным медиафайлам.
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Ошибка при нажатии кнопки редактирования медиа {media_path=}")
        return None
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator.edit_image_properties_textarea)
    if not textarea_list:
        logger.error("Не найдены поля ввода подписи к изображениям")
        return None

    # Асинхронное обновление подписей к изображениям.
    await update_images_captions(d, products, textarea_list)

    return ret


async def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Добавляет описания к загруженным медиафайлам асинхронно.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param products: Список объектов SimpleNamespace, содержащих данные для обновления.
    :type products: List[SimpleNamespace]
    :param textarea_list: Список веб-элементов, представляющих поля ввода подписей.
    :type textarea_list: List[WebElement]

    :raises Exception: Если возникает ошибка при обновлении подписей к медиафайлам.
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """
        Обновляет подпись к медиафайлу для одного продукта синхронно.

        :param product: Объект SimpleNamespace, содержащий данные продукта.
        :type product: SimpleNamespace
        :param textarea_list: Список веб-элементов, представляющих поля ввода подписей.
        :type textarea_list: List[WebElement]
        :param i: Индекс продукта в списке.
        :type i: int
        """
        direction = getattr(local_units.LOCALE, product.language, "LTR")
        message = ""

        # Формирование сообщения на основе данных продукта.
        try:
            if direction == "LTR":
                if hasattr(product, 'product_title'):
                    message += f"{product.product_title}\n"
                if hasattr(product, 'original_price'):
                    message += f"{getattr(local_units.original_price, product.language)}: {product.original_price}\n"
                if hasattr(product, 'sale_price'):
                    message += f"{getattr(local_units.sale_price, product.language)}: {product.sale_price}\n"
                if hasattr(product, 'discount'):
                    message += f"{getattr(local_units.discount, product.language)}: {product.discount}\n"
                if hasattr(product, 'evaluate_rate'):
                    message += f"{getattr(local_units.evaluate_rate, product.language)}: {product.evaluate_rate}\n"
                if hasattr(product, 'promotion_link'):
                    message += f"{getattr(local_units.promotion_link, product.language)}: {product.promotion_link}\n"
                if hasattr(product, 'tags'):
                    message += f"{getattr(local_units.tags, product.language)}: {product.tags}\n"
                message += f"{getattr(local_units.COPYRIGHT, product.language)}"

            else:  # RTL direction
                if hasattr(product, 'product_title'):
                    message += f"\n{product.product_title}"
                if hasattr(product, 'original_price'):
                    message += f"\n{product.original_price} :{getattr(local_units.original_price, product.language)}"
                if hasattr(product, 'discount'):
                    message += f"\n{product.discount} :{getattr(local_units.discount, product.language)}"
                if hasattr(product, 'sale_price'):
                    message += f"\n{product.sale_price} :{getattr(local_units.sale_price, product.language)}"
                if hasattr(product, 'evaluate_rate'):
                    message += f"\n{product.evaluate_rate} :{getattr(local_units.evaluate_rate, product.language)}"
                if hasattr(product, 'promotion_link'):
                    message += f"\n{product.promotion_link} :{getattr(local_units.promotion_link, product.language)}"
                if hasattr(product, 'tags'):
                    message += f"\n{product.tags} :{getattr(local_units.tags, product.language)}"
                message += f"\n{getattr(local_units.COPYRIGHT, product.language)}"

        except Exception as ex:
            logger.error("Ошибка при формировании сообщения", exc_info=True, extra={'exception': ex})

        # Отправка сообщения в поле ввода.
        try:
            textarea_list[i].send_keys(message)
        except Exception as ex:
           logger.error("Ошибка при отправке сообщения в поле ввода", exc_info=True, extra={'exception': ex})

    # Асинхронная обработка продуктов и обновление их подписей.
    for i, product in enumerate(products):
        await asyncio.to_thread(handle_product, product, textarea_list, i)


async def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> Optional[bool]:
    """
    Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param category: Объект SimpleNamespace, содержащий данные для заголовка и описания сообщения.
    :type category: SimpleNamespace
    :param products: Список объектов SimpleNamespace, содержащих медиа и данные для публикации.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, нужно ли загружать видео. По умолчанию False.
    :type no_video: bool
    :return: True, если сообщение успешно опубликовано, иначе None.
    :rtype: Optional[bool]

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> await promote_post(driver, category, products)
    """
    # Публикация заголовка сообщения.
    if not post_title(d, category):
        return None
    d.wait(0.5)

    # Загрузка медиафайлов.
    if not await upload_media(d, products, no_video):
        return None

    # Нажатие кнопки "Готово".
    if not d.execute_locator(locator.finish_editing_button):
        return None

    # Публикация сообщения.
    if not d.execute_locator(locator.publish):
        return None
    return True
```