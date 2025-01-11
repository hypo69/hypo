## Анализ кода модуля `post_message_async.py`

**Качество кода**

-   **Соответствие требованиям**: 7/10
-   **Плюсы**
    *   Используется асинхронный подход для загрузки медиа и обновления подписей.
    *   Присутствует подробное описание функций и их параметров.
    *   Логирование ошибок выполнено с использованием `logger.error`.
    *   Используется `j_loads_ns` для загрузки JSON.
-   **Минусы**
    *   Не везде используются docstring в стиле RST.
    *   В некоторых местах нет обработки ошибок.
    *   Не все переменные и функции имеют snake_case.
    *   Используются return без значения.

**Рекомендации по улучшению**

1.  Добавить docstring в стиле RST для всех функций, методов и переменных.
2.  Улучшить обработку ошибок с использованием `try-except` и `logger.error`.
3.  Привести все переменные и имена функций к snake_case.
4.  Использовать `return True` или `return False` вместо `return` без значения.
5.  Использовать f-строки для форматирования логов.
6.  Убрать избыточные комментарии.
7.  Добавить описание модуля в начале файла.
8.  Избегать вызова функции `d.wait` без необходимости.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для публикации сообщений в Facebook, включая текст, изображения и видео.
=========================================================================================

Этот модуль содержит функции для автоматизации процесса публикации сообщений в Facebook,
включая ввод текста, загрузку медиафайлов и добавление подписей.

Пример использования
--------------------

Пример использования функций `promote_post`, `upload_media` и `post_title`:

.. code-block:: python

    driver = Driver(...)
    category = SimpleNamespace(title='Заголовок кампании', description='Описание кампании')
    products = [SimpleNamespace(local_image_path='path/to/image.jpg',
                               product_title='Название продукта',
                               original_price='100',
                               sale_price='80',
                               discount='20%',
                               evaluate_rate='5',
                               promotion_link='https://example.com',
                               tags='#tag1 #tag2',
                               language='ru')]
    await promote_post(driver, category, products)
"""
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List, Any
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


# Загрузка локаторов из JSON-файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(driver: Driver, category: SimpleNamespace) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения.

    :param driver: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type driver: Driver
    :param category: Объект SimpleNamespace, содержащий заголовок и описание.
    :type category: SimpleNamespace
    :return: True, если заголовок и описание успешно отправлены, иначе False.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title='Заголовок кампании', description='Описание кампании')
        >>> post_title(driver, category)
        True
    """
    # Прокрутка страницы назад
    if not driver.scroll(1, 1200, 'backward'):
        logger.error('Ошибка прокрутки страницы во время ввода заголовка')
        return False

    # Открытие поля "добавить публикацию"
    if not driver.execute_locator(locator.open_add_post_box):
        logger.error('Не удалось открыть поле "добавить публикацию"')
        return False

    # Формирование сообщения с заголовком и описанием
    message = f'{category.title}; {category.description};'

    # Добавление сообщения в поле ввода
    if not driver.execute_locator(locator.add_message, message):
        logger.error(f'Не удалось добавить сообщение в поле ввода: {message=}')
        return False

    return True


async def upload_media(driver: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Загружает медиафайлы и обновляет подписи.

    :param driver: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type driver: Driver
    :param products: Список продуктов с путями к медиафайлам.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, нужно ли пропускать загрузку видео (по умолчанию False).
    :type no_video: bool
    :return: True, если медиафайлы успешно загружены, иначе False.
    :rtype: bool

    :raises Exception: В случае ошибки во время загрузки медиа или обновления подписей.
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> await upload_media(driver, products)
        True
    """
    # Открытие формы добавления медиафайлов (если она еще не открыта)
    if not driver.execute_locator(locator.open_add_foto_video_form):
        return False
    driver.wait(0.5)

    # Проверка, является ли products списком, если нет, то преобразуем его в список
    products = products if isinstance(products, list) else [products]

    # Итерирование по продуктам и загрузка медиафайлов
    for product in products:
        media_path = product.local_video_path if hasattr(product, 'local_video_path') and not no_video else product.local_image_path
        try:
            # Загрузка медиафайла
            if not driver.execute_locator(locator.foto_video_input, media_path):
                 logger.error(f'Ошибка загрузки изображения {media_path=}')
                 return False
            driver.wait(1.5)
        except Exception as ex:
            logger.error(f'Ошибка при загрузке медиа {ex=}', exc_info=True)
            return False

    # Нажатие кнопки редактирования загруженных медиафайлов
    if not driver.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f'Ошибка нажатия на кнопку редактирования медиафайлов {media_path=}')
        return False

    uploaded_media_frame = driver.execute_locator(locator.uploaded_media_frame)
    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    driver.wait(0.3)

    textarea_list = driver.execute_locator(locator.edit_image_properties_textarea)
    if not textarea_list:
        logger.error('Не найдены поля ввода подписи к изображениям')
        return False

    # Асинхронное обновление подписей к изображениям
    await update_images_captions(driver, products, textarea_list)

    return True


async def update_images_captions(driver: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Добавляет описания к загруженным медиафайлам асинхронно.

    :param driver: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type driver: Driver
    :param products: Список продуктов с данными для обновления.
    :type products: List[SimpleNamespace]
    :param textarea_list: Список текстовых полей для добавления подписей.
    :type textarea_list: List[WebElement]
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """
        Обрабатывает обновление подписи для одного продукта синхронно.

        :param product: Продукт для обновления.
        :type product: SimpleNamespace
        :param textarea_list: Список текстовых полей для добавления подписей.
        :type textarea_list: List[WebElement]
        :param i: Индекс продукта в списке.
        :type i: int
        """
        direction = getattr(local_units.LOCALE, product.language, 'LTR')
        message = ''
        # Добавление информации о продукте в сообщение
        try:
            if direction == 'LTR':
                if hasattr(product, 'product_title'):
                    message += f'{product.product_title}\\n'
                if hasattr(product, 'original_price'):
                    message += f'{getattr(local_units.original_price, product.language)}: {product.original_price}\\n'
                if hasattr(product, 'sale_price'):
                    message += f'{getattr(local_units.sale_price, product.language)}: {product.sale_price}\\n'
                if hasattr(product, 'discount'):
                    message += f'{getattr(local_units.discount, product.language)}: {product.discount}\\n'
                if hasattr(product, 'evaluate_rate'):
                    message += f'{getattr(local_units.evaluate_rate, product.language)}: {product.evaluate_rate}\\n'
                if hasattr(product, 'promotion_link'):
                    message += f'{getattr(local_units.promotion_link, product.language)}: {product.promotion_link}\\n'
                if hasattr(product, 'tags'):
                    message += f'{getattr(local_units.tags, product.language)}: {product.tags}\\n'
                message += f'{getattr(local_units.COPYRIGHT, product.language)}'

            else:  # RTL direction
                if hasattr(product, 'product_title'):
                    message += f'\\n{product.product_title}'
                if hasattr(product, 'original_price'):
                    message += f'\\n{product.original_price} :{getattr(local_units.original_price, product.language)}'
                if hasattr(product, 'discount'):
                    message += f'\\n{product.discount} :{getattr(local_units.discount, product.language)}'
                if hasattr(product, 'sale_price'):
                    message += f'\\n{product.sale_price} :{getattr(local_units.sale_price, product.language)}'
                if hasattr(product, 'evaluate_rate'):
                    message += f'\\n{product.evaluate_rate} :{getattr(local_units.evaluate_rate, product.language)}'
                if hasattr(product, 'promotion_link'):
                    message += f'\\n{product.promotion_link} :{getattr(local_units.promotion_link, product.language)}'
                if hasattr(product, 'tags'):
                    message += f'\\n{product.tags} :{getattr(local_units.tags, product.language)}'
                message += f'\\n{getattr(local_units.COPYRIGHT, product.language)}'

        except Exception as ex:
            logger.error(f'Ошибка при формировании сообщения {ex=}', exc_info=True)

        # Отправка сообщения в textarea
        if not textarea_list[i].send_keys(message):
            logger.error('Ошибка при отправке текста в поле ввода')

    # Обработка продуктов и обновление их подписей асинхронно
    for i, product in enumerate(products):
        await asyncio.to_thread(handle_product, product, textarea_list, i)


async def promote_post(driver: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Управляет процессом продвижения публикации с заголовком, описанием и медиафайлами.

    :param driver: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type driver: Driver
    :param category: Объект SimpleNamespace с деталями категории для заголовка и описания.
    :type category: SimpleNamespace
    :param products: Список продуктов, содержащих медиа и детали для публикации.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, нужно ли пропускать загрузку видео (по умолчанию False).
    :type no_video: bool
    :return: True, если публикация успешно продвинута, иначе False.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title='Заголовок кампании', description='Описание кампании')
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> await promote_post(driver, category, products)
    """
    if not post_title(driver, category):
        return False
    driver.wait(0.5)

    if not await upload_media(driver, products, no_video):
        return False
    if not driver.execute_locator(locator.finish_editing_button):
        return False
    if not driver.execute_locator(locator.publish):
        return False
    return True