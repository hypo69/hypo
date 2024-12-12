# Анализ кода модуля post_message.py

**Качество кода**
    7
 -  Плюсы
        - Код хорошо структурирован с использованием функций для различных этапов процесса публикации сообщений.
        - Используются `SimpleNamespace` для передачи данных, что делает код более читаемым.
        - Применяется логирование с помощью `logger` для отслеживания ошибок и отладки.
        - Присутствуют docstring для функций, что помогает понять их назначение и использование.
        - Код использует `j_loads_ns` для загрузки данных из JSON, что соответствует требованиям.
        - Присутствует обработка различных типов входных данных (`str`, `SimpleNamespace`, `list`).
 -  Минусы
    - Некоторые комментарии не соответствуют формату reStructuredText.
    - Избыточное использование `try-except` в некоторых местах, где можно обойтись проверкой условий.
    - Не все функции имеют полные docstring (например, `publish`).
    - Есть повторение кода в обработке `d.execute_locator` с `locator.close_pop_up` и `locator.not_now`.
    - В функции `update_images_captions` не проверяется количество элементов в `textarea_list`.
    - В функции `post_message` есть неиспользуемый параметр images
    - Функция `promote_post` дублируется по функционалу с `post_message`

**Рекомендации по улучшению**

1.  **Унифицировать комментарии**: Переписать все комментарии в формате reStructuredText.
2.  **Улучшить обработку ошибок**: Использовать `logger.error` вместо избыточного `try-except` там, где это уместно, а также добавить обработку исключений в более общих блоках.
3.  **Дополнить docstring**: Добавить отсутствующие docstring для всех функций, включая `publish` и методы.
4.  **Избегать дублирования кода**: Вынести повторяющуюся логику обработки `d.execute_locator` с `locator.close_pop_up` и `locator.not_now` в отдельную функцию.
5.  **Проверки длинны textarea_list**: В функции `update_images_captions` проверять количество элементов в `textarea_list` перед итерацией
6.  **Удалить неиспользуемый параметр**: В функции `post_message` удалить неиспользуемый параметр `images`
7.  **Удалить дубликат функции**: Удалить функцию `promote_post`
8.  **Улучшить форматирование**: Добавить отступы и пустые строки в коде для лучшей читаемости
9.  **Добавить проверки**:  Проверять существование атрибутов у объектов перед их использованием, чтобы избежать потенциальных ошибок `AttributeError`.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для публикации сообщений в Facebook.
=========================================================================================

Этот модуль содержит функции для автоматизации процесса публикации сообщений,
включая добавление текста, загрузку медиафайлов и обновление подписей к изображениям.

"""
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List, Optional
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.utils.printer import pprint
from src.logger.logger import logger

MODE = 'dev'

# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param message: Заголовок и описание для отправки.
    :type message: SimpleNamespace | str
    :return: ``True``, если заголовок и описание были успешно отправлены, иначе ``None``.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    # Прокрутка страницы назад
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Прокрутка страницы не удалась во время отправки заголовка")
        return

    # Открытие окна добавления сообщения
    if not d.execute_locator(locator=locator.open_add_post_box):
        logger.debug("Не удалось открыть окно 'add post'")
        return

    # Формирование сообщения для отправки
    m = f"{message.title}\\n{message.description}" if isinstance(message, SimpleNamespace) else message

    # Добавление сообщения в поле ввода
    if not d.execute_locator(locator.add_message, message=m, timeout=5, timeout_for_event='element_to_be_clickable'):
        logger.debug(f"Не удалось добавить сообщение в поле ввода: {m=}")
        return

    return True


def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str], no_video: bool = False,
                 without_captions: bool = False) -> bool:
    """
    Загружает медиафайлы в раздел изображений и обновляет подписи.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param media: Список или отдельный объект медиафайлов для загрузки.
    :type media: SimpleNamespace | List[SimpleNamespace] | str | list[str]
    :param no_video: Если ``True``, загрузка видео игнорируется. По умолчанию ``False``.
    :type no_video: bool
    :param without_captions: Если ``True``, подписи не добавляются. По умолчанию ``False``.
    :type without_captions: bool
    :return: ``True``, если медиафайлы были успешно загружены, иначе ``None``.
    :rtype: bool

    :raises Exception: Если произошла ошибка во время загрузки или обновления подписей.

    :Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
    if not media:
        logger.debug("Нет медиа для сообщения!")
        return

    # Открытие формы 'add media', если она еще не открыта.
    if not d.execute_locator(locator.open_add_foto_video_form):
        return
    d.wait(0.5)

    # Преобразование `media` в список, если это не список
    media_list: list = media if isinstance(media, list) else [media]
    ret: bool = True

    # Итерация по списку медиа и загрузка
    for m in media_list:
        if isinstance(m, SimpleNamespace):
            try:
                media_path = m.local_saved_video if hasattr(m, 'local_saved_video') and not no_video else m.local_saved_image
            except AttributeError:
                logger.error("Ошибка в поле 'local_saved_image' или 'local_saved_video'")
                return
        elif isinstance(m, (str, Path)):
            media_path = m
        else:
             logger.error(f"Неподдерживаемый тип данных для медиа {type(m)}")
             return

        try:
            # Загрузка медиафайла
            if d.execute_locator(locator=locator.foto_video_input, message=str(media_path), timeout=20):
                d.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return
        except Exception as ex:
            logger.error("Ошибка во время загрузки медиа", ex, exc_info=True)
            return

    if without_captions:
        return True

    # Обновление подписей для загруженных медиа
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Не удалось нажать кнопку редактирования медиа")
        return
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    if not uploaded_media_frame:
        logger.debug(f"Не найдены поля ввода подписей к изображениям")
        return

    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator=locator.edit_image_properties_textarea, timeout=10,
                                      timeout_for_event='presence_of_element_located')
    if not textarea_list:
        logger.error("Не найдены поля ввода подписи к изображениям")
        return

    # Обновление подписей к изображениям.
    update_images_captions(d, media_list, textarea_list)

    return ret


def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Добавляет описания к загруженным медиафайлам.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param media: Список продуктов с деталями для обновления.
    :type media: List[SimpleNamespace]
    :param textarea_list: Список текстовых полей, в которые добавляются подписи.
    :type textarea_list: List[WebElement]

    :raises Exception: Если возникла ошибка при обновлении подписей.
    """
    local_units = j_loads_ns(
        Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """
        Обрабатывает обновление подписей медиа для отдельного продукта.

        :param product: Продукт для обновления.
        :type product: SimpleNamespace
        :param textarea_list: Список текстовых полей для добавления подписей.
        :type textarea_list: List[WebElement]
        :param i: Индекс продукта в списке.
        :type i: int
        """
        lang = product.language.upper()
        direction = getattr(local_units.LOCALE, lang, "LTR")
        message = ""

        try:
            if direction == "LTR":
                if hasattr(product, 'product_title'):
                    message += f"{product.product_title}\\n"

                if hasattr(product, 'description'):
                    message += f'{product.description}\\n'

                if hasattr(product, 'original_price'):
                    message += f"{getattr(local_units.original_price, lang)}: {product.original_price} {product.target_original_price_currency}\\n"

                if hasattr(product, 'sale_price') and hasattr(product, 'discount') and product.discount != '0%':
                    message += f"{getattr(local_units.discount, lang)}: {product.discount}\\n"
                    message += f"{getattr(local_units.sale_price, lang)}: {product.sale_price} {product.target_original_price_currency} \\n"

                if hasattr(product, 'evaluate_rate') and product.evaluate_rate != '0.0%':
                    message += f"{getattr(local_units.evaluate_rate, lang)}: {product.evaluate_rate}\\n"

                if hasattr(product, 'promotion_link'):
                    message += f"{getattr(local_units.promotion_link, lang)}: {product.promotion_link}\\n"

            else:  # RTL direction
                if hasattr(product, 'product_title'):
                    message += f"\\n{product.product_title}"

                if hasattr(product, 'description'):
                    message += f'{product.description}\\n'

                if hasattr(product, 'original_price'):
                    message += f"\\n {product.target_original_price_currency} {product.original_price} :{getattr(local_units.original_price, lang)}"

                if hasattr(product, 'sale_price') and hasattr(product, 'discount') and product.discount != '0%':
                    message += f"\\n{product.discount} :{getattr(local_units.discount, lang)}"
                    message += f"\\n {product.target_original_price_currency} {product.sale_price} :{getattr(local_units.sale_price, lang)}"

                if hasattr(product, 'evaluate_rate') and product.evaluate_rate != '0.0%':
                    message += f"\\n{product.evaluate_rate} :{getattr(local_units.evaluate_rate, lang)}"

                if hasattr(product, 'promotion_link'):
                    message += f"\\n{product.promotion_link} :{getattr(local_units.promotion_link, lang)}"


        except Exception as ex:
            logger.error("Ошибка при формировании сообщения", ex, exc_info=True)
            return

        # Отправка сообщения в текстовое поле
        try:
            if i < len(textarea_list):
                textarea_list[i].send_keys(message)
            else:
                logger.error(f"Индекс {i} за пределами списка textarea_list {len(textarea_list)}")

            return True
        except Exception as ex:
            logger.error("Ошибка при отправке сообщения в textarea", ex)
            return

    # Обработка продуктов и обновление их подписей
    for i, product in enumerate(media):
        handle_product(product, textarea_list, i)


def _handle_publish_popup(d: Driver, attempts: int) -> bool:
    """
    Обрабатывает всплывающие окна при публикации.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param attempts: Количество попыток.
    :type attempts: int
    :return: ``True``, если публикация прошла успешно, иначе ``False``.
    :rtype: bool
    """
    if d.execute_locator(locator.close_pop_up) or d.execute_locator(locator.not_now):
        if attempts > 0 :
            d.wait(2)
            return publish(d, attempts - 1)
        return False
    return True


def publish(d: Driver, attempts: int = 5) -> bool:
    """
    Публикует сообщение.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param attempts: Количество попыток публикации. По умолчанию 5.
    :type attempts: int
    :return: ``True``, если публикация прошла успешно, иначе ``False``.
    :rtype: bool
    """
    if attempts < 0:
        return False

    # Завершение редактирования
    if not d.execute_locator(locator.finish_editing_button, timeout=1):
        logger.debug(f"Не удалось обработать локатор {locator.finish_editing_button}")
        return False
    d.wait(1)

    # Публикация сообщения
    if not d.execute_locator(locator.publish, timeout=5):
        if not _handle_publish_popup(d, attempts):
            logger.debug(f"Не удалось обработать локатор {locator.finish_editing_button}")
            return False
        return publish(d,attempts-1)
    
    # Ожидание освобождения поля ввода
    while not d.execute_locator(locator=locator.open_add_post_box, timeout=10,
                                timeout_for_event='element_to_be_clickable'):
        logger.debug(f"Поле ввода не освободилось {attempts=}", None, False)
        if not _handle_publish_popup(d, attempts):
            return False
        return publish(d, attempts-1)
    return True


def post_message(d: Driver, message: SimpleNamespace, no_video: bool = False, without_captions: bool = False) -> bool:
    """
    Управляет процессом продвижения сообщения с заголовком, описанием и медиафайлами.

    :param d: Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
    :type d: Driver
    :param message: Детали сообщения, используемые для заголовка и описания.
    :type message: SimpleNamespace
    :param no_video: Если ``True``, загрузка видео игнорируется. По умолчанию ``False``.
    :type no_video: bool
    :param without_captions: Если ``True``, подписи не добавляются. По умолчанию ``False``.
    :type without_captions: bool
    :return: ``True``, если сообщение было успешно отправлено, иначе ``False``.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> post_message(driver, category, products)
    """
    # Отправка заголовка и описания
    if not post_title(d, message):
        return False
    d.wait(0.5)

    # Загрузка медиафайлов
    if not upload_media(d, message.products, no_video=no_video, without_captions=without_captions):
        return False
    d.wait(0.5)

    # Выход если было одно изображение
    if d.execute_locator(locator=locator.send):
        return True

    # Завершение редактирования
    if not d.execute_locator(locator=locator.finish_editing_button):
        return False
    # Публикация сообщения
    if not publish(d):
        return False

    return True