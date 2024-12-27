# Анализ кода модуля `post_message`

**Качество кода: 6/10**

-   **Плюсы:**
    *   Код разбит на отдельные функции, что способствует читаемости и повторному использованию.
    *   Используется `logger` для логирования ошибок и отладки.
    *   Присутствует документация в формате docstring для функций.
    *   Используется `j_loads_ns` для загрузки конфигураций.
-   **Минусы:**
    *   Много повторяющегося кода, особенно в обработке ошибок и повторных вызовов функций `publish`.
    *   Не все функции имеют docstring.
    *   Используется `try-except` блоки без необходимости.
    *   Не все комментарии соответствуют стандарту reStructuredText.
    *   Логика обработки медиа-файлов не совсем ясна и может быть упрощена.
    *   Некоторые `return` без значения.
    *   Использованы `...` в коде.
    *   Смешаны стили комментариев (`#` и docstrings)
    *   Слишком много проверок на `return`
    *   Не везде используется форматирование f-string

**Рекомендации по улучшению:**

1.  **Улучшить документацию:** Дополнить docstring для всех функций и параметров, используя reStructuredText.
2.  **Рефакторинг `publish`:** Упростить функцию `publish`, убрав лишние рекурсивные вызовы и проверки, а так же повторяющийся код.
3.  **Обработка ошибок:** Использовать `logger.error` с параметром `exc_info=True` для более детального логирования исключений, а также по возможности избавится от блоков `try/except`
4.  **Упростить обработку медиа:** Пересмотреть логику обработки медиа-файлов, использовать более явные имена переменных.
5.  **Унифицировать проверки:** Сделать проверки более компактными, используя `if not`  и  `or`.
6.  **Форматирование:** Использовать f-строки там, где это возможно.
7.  **Избавиться от `...`:** Заменить все `...` на конкретную логику или `pass`
8. **Улучшить стиль комментариев:** Привести все комментарии в единый вид RST

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
"""
Модуль для публикации сообщений в Facebook.
=========================================================================================

Этот модуль содержит функции для автоматизации процесса публикации сообщений, включая текст,
медиафайлы и обновление подписей.
"""
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List, Optional, Union
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.utils.printer import pprint
from src.logger.logger import logger

# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(d: Driver, message: Union[SimpleNamespace, str]) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param message: Сообщение для публикации, может быть строкой или SimpleNamespace
        с полями `title` и `description`.
    :type message: Union[SimpleNamespace, str]
    :return: True, если заголовок и описание были успешно отправлены, иначе False.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    # Прокрутка страницы назад
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Ошибка при прокрутке страницы назад во время публикации заголовка")
        return False

    # Открытие поля 'добавить сообщение'
    if not d.execute_locator(locator=locator.open_add_post_box):
        logger.debug("Не удалось открыть поле 'добавить сообщение'")
        return False

    # Формирование сообщения для публикации
    m = f"{message.title}\\n{message.description}" if isinstance(message, SimpleNamespace) else message

    # Отправка сообщения в поле сообщения
    if not d.execute_locator(locator.add_message, message=m, timeout=5, timeout_for_event='element_to_be_clickable'):
        logger.debug(f"Не удалось добавить сообщение в поле сообщения: {m=}")
        return False

    return True


def upload_media(d: Driver, media: Union[SimpleNamespace, List[SimpleNamespace], str, List[str]], no_video: bool = False,
                 without_captions: bool = False) -> bool:
    """
    Загружает медиафайлы и обновляет подписи.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param media: Пути к медиафайлам или список путей, а также может быть `SimpleNamespace` с атрибутами `local_saved_video`, `local_saved_image`.
    :type media: Union[SimpleNamespace, List[SimpleNamespace], str, List[str]]
    :param no_video: Флаг, указывающий, не использовать видео.
    :type no_video: bool
    :param without_captions: Флаг, указывающий, не добавлять подписи к изображениям.
    :type without_captions: bool
    :return: True, если медиафайлы были успешно загружены, иначе False.
    :rtype: bool
    :raises Exception: если произошла ошибка во время загрузки медиа или обновления подписей.

    :Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
    if not media:
        logger.debug("Нет медиа для сообщения!")
        return False

    # Открытие формы 'добавить медиа'
    if not d.execute_locator(locator.open_add_foto_video_form):
        return False
    d.wait(0.5)

    # Преобразование media в список, если это не список
    media_list: list = media if isinstance(media, list) else [media]

    # Загрузка медиафайлов
    for m in media_list:
        try:
            if isinstance(m, SimpleNamespace):
                media_path = m.local_saved_video if hasattr(m, 'local_saved_video') and not no_video else m.local_saved_image
            elif isinstance(m, (str, Path)):
                media_path = m
            else:
                logger.error(f"Неизвестный тип медиа: {type(m)}")
                return False

            # Загрузка медиафайла
            if not d.execute_locator(locator=locator.foto_video_input, message=str(media_path), timeout=20):
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return False
            d.wait(1.5)
        except Exception as ex:
            logger.error("Ошибка при загрузке медиа", exc_info=True)
            return False

    if without_captions:
        return True

    # Обновление подписей к загруженным медиа
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Ошибка нажатия кнопки редактирования медиа")
        return False

    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    if not uploaded_media_frame:
        logger.debug("Не найдены поля ввода подписей к изображениям")
        return False

    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator=locator.edit_image_properties_textarea, timeout=10,
                                      timeout_for_event='presence_of_element_located')
    if not textarea_list:
        logger.error("Не найдены поля ввода подписи к изображениям")
        return False

    # Обновление подписей
    update_images_captions(d, media, textarea_list)

    return True


def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Добавляет описания к загруженным медиафайлам.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param media: Список продуктов с деталями для обновления.
    :type media: List[SimpleNamespace]
    :param textarea_list: Список текстовых полей, где добавляются подписи.
    :type textarea_list: List[WebElement]
    :raises Exception: если произошла ошибка при обновлении подписей к медиа.
    """

    local_units = j_loads_ns(
        Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """
         Обрабатывает обновление подписей к медиа для одного продукта.

         :param product: Продукт для обновления.
         :type product: SimpleNamespace
         :param textarea_list: Список текстовых полей, где добавляются подписи.
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
            logger.error("Ошибка при формировании сообщения", exc_info=True)
            return

        # Отправка сообщения в textarea
        try:
            textarea_list[i].send_keys(message)
            return True
        except Exception as ex:
            logger.error("Ошибка при отправке текста в textarea", exc_info=True)
            return

    # Обработка продуктов и обновление их подписей
    for i, product in enumerate(media):
        handle_product(product, textarea_list, i)


def publish(d: Driver, attempts: int = 5) -> bool:
    """
    Публикует сообщение.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param attempts: Количество попыток публикации.
    :type attempts: int
    :return: True, если сообщение было успешно опубликовано, иначе False.
    :rtype: bool
    """
    if attempts < 0:
        return False

    if not d.execute_locator(locator.finish_editing_button, timeout=1):
        logger.debug(f"Не удалось обработать локатор {locator.finish_editing_button}")
        return False
    d.wait(1)

    if not d.execute_locator(locator.publish, timeout=5):
        if d.execute_locator(locator.close_pop_up) or d.execute_locator(locator.not_now):
            return publish(d, attempts - 1)
        if attempts > 0:
            d.wait(5)
            return publish(d, attempts - 1)

        logger.debug(f"Не удалось обработать локатор {locator.finish_editing_button}")
        return False

    while not d.execute_locator(locator=locator.open_add_post_box, timeout=10,
                                timeout_for_event='element_to_be_clickable'):
        logger.debug(f"не освободилось поле ввода {attempts=}", None, False)
        if d.execute_locator(locator.close_pop_up) or d.execute_locator(locator.not_now):
            return publish(d, attempts - 1)
        if attempts > 0:
            d.wait(2)
            return publish(d, attempts - 1)

    return True


def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param category: Детали категории, используемые для заголовка и описания поста.
    :type category: SimpleNamespace
    :param products: Список продуктов, содержащих медиафайлы и детали для публикации.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, не использовать видео.
    :type no_video: bool
    :return: True, если пост успешно опубликован, иначе False.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    if not post_title(d, category):
        return False
    d.wait(0.5)

    if not upload_media(d, products, no_video):
        return False

    if not d.execute_locator(locator=locator.finish_editing_button):
        return False
    if not d.execute_locator(locator.publish, timeout=20):
        print("Публикуется...")
        return False
    return True


def post_message(d: Driver, message: SimpleNamespace, no_video: bool = False,
                 images: Optional[Union[str, List[str]]] = None, without_captions: bool = False) -> bool:
    """
    Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param message: Детали сообщения, используемые для заголовка и описания поста.
    :type message: SimpleNamespace
    :param no_video: Флаг, указывающий, не использовать видео.
    :type no_video: bool
    :param images: Список изображений для публикации.
    :type images: Optional[Union[str, List[str]]]
    :param without_captions: Флаг, указывающий, не добавлять подписи к изображениям.
    :type without_captions: bool
    :return: True, если сообщение успешно опубликовано, иначе False.
    :rtype: bool

    :Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    if not post_title(d, message):
        return False
    d.wait(0.5)

    if not upload_media(d, message.products, no_video=no_video, without_captions=without_captions):
        return False
    d.wait(0.5)

    if d.execute_locator(locator=locator.send):
        """ Выход, если было одно изображение """
        return True

    if not d.execute_locator(locator=locator.finish_editing_button):
        return False

    if not publish(d):
        return False

    return True
```