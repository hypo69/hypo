# Анализ кода модуля `post_message_async.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используется `asyncio` для асинхронных операций, что повышает производительность.
    - Присутствует базовая обработка ошибок с использованием `logger.error`.
    - Используются `SimpleNamespace` для хранения данных, что делает код более читаемым.
    - Есть docstring к каждой функции, что способствует пониманию кода.
- Минусы
    - Некоторые комментарии `#` не соответствуют стилю RST.
    - Не везде используется `exc_info=True` при логировании ошибок.
    - Есть места, где можно улучшить обработку ошибок, убрав лишние `return` внутри `try except`.
    - В некоторых местах используется `isinstance(products, list)`, что может быть заменено на более pythonic проверку.
    - Функция `handle_product` объявлена внутри `update_images_captions`, что может усложнить чтение кода.
    - Использование `getattr(local_units.LOCALE, product.language, "LTR")` можно заменить на более понятную конструкцию с проверкой наличия ключа в словаре.

**Рекомендации по улучшению**
1. **Документация**:
    - Переписать все комментарии в формате RST, включая docstring.
    - Дополнить примеры использования в docstring.
2. **Импорты**:
    - Проверить и добавить отсутствующие импорты.
3. **Обработка ошибок**:
    -  Удалить лишние `return` из блоков `try-except`, если ошибка логируется с помощью `logger.error`.
    - Использовать `exc_info=True` в `logger.error` для более полной информации об ошибках.
4. **Рефакторинг**:
   - Вынести функцию `handle_product` из `update_images_captions` для улучшения читаемости.
   - Заменить `isinstance(products, list)` на `if not isinstance(products, list): products = [products]`
   - Улучшить логику выбора направления текста (LTR/RTL) через явную проверку ключа в `local_units.LOCALE`.
5. **Логирование**:
    - Применять  `logger.error` с `exc_info=True` для отслеживания ошибок.
6. **Переменные**:
    - Привести все переменные к нижнему регистру с подчеркиванием.
7. **Форматирование**:
    - Код должен соответствовать PEP 8.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для асинхронной публикации сообщений в Facebook.
=====================================================

Этот модуль предоставляет функциональность для автоматической публикации сообщений,
включая текст, изображения и видео, в Facebook.

Он использует асинхронные операции для эффективного управления процессом
публикации.

:platform: Windows, Unix
:synopsis: Публикация сообщения из `aliexpress` промо
"""

import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import List
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(driver: Driver, category: SimpleNamespace) -> bool:
    """Отправляет заголовок и описание кампании в поле сообщения.

    :param driver: Экземпляр драйвера для взаимодействия со страницей.
    :type driver: Driver
    :param category: Объект SimpleNamespace, содержащий заголовок и описание.
    :type category: SimpleNamespace
    :return: True, если заголовок и описание успешно отправлены, иначе None.
    :rtype: bool
    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    #  код прокручивает страницу назад
    if not driver.scroll(1, 1200, 'backward'):
        logger.error("Ошибка прокрутки страницы во время добавления заголовка", exc_info=True)
        return

    #  код открывает окно "добавить пост"
    if not driver.execute_locator(locator.open_add_post_box):
        logger.error("Не удалось открыть окно \'добавить пост\'", exc_info=True)
        return

    #  формирует сообщение из заголовка и описания
    message = f"{category.title}; {category.description};"

    #  код добавляет сообщение в поле ввода
    if not driver.execute_locator(locator.add_message, message):
        logger.error(f"Не удалось добавить сообщение в поле ввода: {message=}", exc_info=True)
        return

    return True


async def upload_media(driver: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """Загружает медиафайлы в раздел изображений и обновляет подписи.

    :param driver: Экземпляр драйвера для взаимодействия со страницей.
    :type driver: Driver
    :param products: Список объектов SimpleNamespace, содержащих пути к медиафайлам.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, что видео не нужно загружать.
    :type no_video: bool
    :return: True, если медиафайлы успешно загружены, иначе None.
    :rtype: bool
    :raises Exception: Если возникает ошибка при загрузке медиа или обновлении подписей.
    :Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> await upload_media(driver, products)
        True
    """
    #  код открывает форму "добавить медиа".
    if not driver.execute_locator(locator.open_add_foto_video_form):
        return
    driver.wait(0.5)

    #  код проверяет, является ли `products` списком и преобразовывает если нет
    if not isinstance(products, list):
        products = [products]
    ret: bool = True

    #  код итерируется по продуктам и загружает медиафайлы
    for product in products:
        media_path = product.local_saved_video if hasattr(product, 'local_saved_video') and not no_video else product.local_saved_image
        try:
            #  код загружает медиафайл
            if driver.execute_locator(locator.foto_video_input, media_path):
                driver.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}", exc_info=True)
                return
        except Exception as ex:
            logger.error("Ошибка при загрузке медиа", exc_info=True)
            return

    # код нажимает на кнопку редактирования загруженных медиа
    if not driver.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Ошибка при нажатии кнопки редактирования загруженных медиа {media_path=}", exc_info=True)
        return
    uploaded_media_frame = driver.execute_locator(locator.uploaded_media_frame)
    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    driver.wait(0.3)

    textarea_list = driver.execute_locator(locator.edit_image_properties_textarea)
    if not textarea_list:
        logger.error("Не найдены поля ввода подписи к изображениям", exc_info=True)
        return
    #  асинхронно обновляет подписи к изображениям
    await update_images_captions(driver, products, textarea_list)

    return ret


async def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
    """Обновляет подписи к медиа для одного продукта.

    :param product: Продукт, для которого нужно обновить подпись.
    :type product: SimpleNamespace
    :param textarea_list: Список полей ввода для подписей.
    :type textarea_list: List[WebElement]
    :param i: Индекс продукта в списке.
    :type i: int
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    direction = local_units.LOCALE.get(product.language, "LTR")
    message = ""

    # Формирует сообщение на основе данных продукта.
    try:
        if direction == "LTR":
            if hasattr(product, 'product_title'):
                message += f"{product.product_title}\\n"
            if hasattr(product, 'original_price'):
                message += f"{getattr(local_units.original_price, product.language)}: {product.original_price}\\n"
            if hasattr(product, 'sale_price'):
                message += f"{getattr(local_units.sale_price, product.language)}: {product.sale_price}\\n"
            if hasattr(product, 'discount'):
                message += f"{getattr(local_units.discount, product.language)}: {product.discount}\\n"
            if hasattr(product, 'evaluate_rate'):
                message += f"{getattr(local_units.evaluate_rate, product.language)}: {product.evaluate_rate}\\n"
            if hasattr(product, 'promotion_link'):
                message += f"{getattr(local_units.promotion_link, product.language)}: {product.promotion_link}\\n"
            if hasattr(product, 'tags'):
                message += f"{getattr(local_units.tags, product.language)}: {product.tags}\\n"
            message += f"{getattr(local_units.COPYRIGHT, product.language)}"

        else:  # RTL direction
            if hasattr(product, 'product_title'):
                message += f"\\n{product.product_title}"
            if hasattr(product, 'original_price'):
                message += f"\\n{product.original_price} :{getattr(local_units.original_price, product.language)}"
            if hasattr(product, 'discount'):
                message += f"\\n{product.discount} :{getattr(local_units.discount, product.language)}"
            if hasattr(product, 'sale_price'):
                message += f"\\n{product.sale_price} :{getattr(local_units.sale_price, product.language)}"
            if hasattr(product, 'evaluate_rate'):
                message += f"\\n{product.evaluate_rate} :{getattr(local_units.evaluate_rate, product.language)}"
            if hasattr(product, 'promotion_link'):
                message += f"\\n{product.promotion_link} :{getattr(local_units.promotion_link, product.language)}"
            if hasattr(product, 'tags'):
                message += f"\\n{product.tags} :{getattr(local_units.tags, product.language)}"
            message += f"\\n{getattr(local_units.COPYRIGHT, product.language)}"

    except Exception as ex:
        logger.error("Ошибка при формировании сообщения", ex, exc_info=True)

    #  код отправляет сообщение в textarea
    if textarea_list[i].send_keys(message):
        return

    logger.error("Ошибка при отправке текста в textarea", exc_info=True)


async def update_images_captions(driver: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """Добавляет описания к загруженным медиафайлам асинхронно.

    :param driver: Экземпляр драйвера для взаимодействия со страницей.
    :type driver: Driver
    :param products: Список объектов SimpleNamespace, содержащих данные о продуктах.
    :type products: List[SimpleNamespace]
    :param textarea_list: Список элементов textarea для ввода подписей.
    :type textarea_list: List[WebElement]
    :raises Exception: Если возникает ошибка при обновлении подписей к медиа.
    """

    #  код обрабатывает продукты и обновляет их подписи асинхронно
    for i, product in enumerate(products):
         await asyncio.to_thread(handle_product, product, textarea_list, i)


async def promote_post(driver: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    :param driver: Экземпляр драйвера для взаимодействия со страницей.
    :type driver: Driver
    :param category: Объект SimpleNamespace, содержащий детали категории для заголовка и описания.
    :type category: SimpleNamespace
    :param products: Список объектов SimpleNamespace, содержащих медиа и детали для публикации.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, что видео не нужно загружать.
    :type no_video: bool
    :return: True, если пост успешно опубликован, иначе None.
    :rtype: bool
    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> await promote_post(driver, category, products)
    """
    #  код публикует заголовок
    if not post_title(driver, category):
        return
    driver.wait(0.5)

    #  код загружает медиафайлы
    if not await upload_media(driver, products, no_video):
        return
    #  код нажимает на кнопку "Закончить редактирование"
    if not driver.execute_locator(locator.finish_editing_button):
        return
    # код нажимает на кнопку "Опубликовать"
    if not driver.execute_locator(locator.publish):
        return
    return True
```