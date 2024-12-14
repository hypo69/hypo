# Анализ кода модуля `post_message.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на функции, каждая из которых выполняет свою задачу.
    - Используются docstring для описания функций, что облегчает понимание кода.
    - Присутствует логирование ошибок с использованием `logger.error` и `logger.debug`.
    - Код использует кастомные `j_loads_ns` для загрузки данных из json файлов.
    - Используются константы `MODE`.
- Минусы
    - Присутствуют избыточные блоки `try-except`
    - Используется `...` как точки остановки.
    - В некоторых местах используется `print()` вместо `logger.debug()`.
    - Некоторые комментарии не соответствуют стандарту reStructuredText (RST).
    - Отсутствует проверка наличия атрибутов у `SimpleNamespace` перед их использованием.
    - Местами используется неявная передача аргументов.

**Рекомендации по улучшению**

1.  **Импорты**: Добавьте недостающие импорты (если есть).
2.  **Форматирование**: Приведите в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
3.  **Комментарии**: Переписать все комментарии в формате RST.
4.  **Обработка ошибок**: Избегайте избыточного использования стандартных блоков `try-except`. Обрабатывать ошибки через `logger.error`.
5.  **Логирование**: Заменить `print` на `logger.debug`.
6.  **Проверка атрибутов**: Проверяйте наличие атрибутов в объектах `SimpleNamespace` перед их использованием.
7.  **Удаление `...`**: Заменить `...` на более явные действия, например, `pass` или логирование.
8.  **Явные аргументы**: Уточнить передачу аргументов в функции.
9.  **Согласованность**: Привести код к единому стилю.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления публикацией сообщений в Facebook.
=========================================================================================

Этот модуль предоставляет функции для публикации сообщений,
включая текст, изображения и видео, используя Selenium WebDriver.

:platform: Windows, Unix
:synopsis: Публикация сообщения в Facebook
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
MODE = 'dev'

# Загружает локаторы из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)

def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """Отправляет заголовок и описание кампании в поле сообщения.

    :param d: Экземпляр драйвера, используемый для взаимодействия со страницей.
    :type d: Driver
    :param message: Сообщение для публикации. Может быть экземпляром SimpleNamespace или строкой.
    :type message: SimpleNamespace | str
    :return: True, если заголовок и описание были успешно отправлены, иначе None.
    :rtype: bool | None

    :Example:

    .. code-block:: python

        driver = Driver(...)
        message = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
        post_title(driver, message)
        True
    """
    # Выполняет прокрутку страницы назад.
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Прокрутка страницы не удалась во время добавления заголовка.")
        return

    # Открывает окно добавления сообщения.
    if not d.execute_locator(locator=locator.open_add_post_box):
        logger.debug("Не удалось открыть окно 'добавить сообщение'.")
        return

    # Добавляет сообщение в поле ввода сообщения.
    m = f"{message.title}\n{message.description}" if isinstance(message, SimpleNamespace) else message
    if not d.execute_locator(locator=locator.add_message, message=m, timeout=5, timeout_for_event='element_to_be_clickable'):
        logger.debug(f"Не удалось добавить сообщение в поле ввода сообщения: {m=}")
        return

    return True


def upload_media(d: Driver, media:  Union[SimpleNamespace, List[SimpleNamespace], str, List[str]], no_video: bool = False, without_captions: bool = False) -> bool:
    """Загружает медиафайлы в раздел изображений и обновляет подписи.

    :param d: Экземпляр драйвера, используемый для взаимодействия со страницей.
    :type d: Driver
    :param media: Список объектов SimpleNamespace с путями к медиафайлам.
        Может быть как одним файлом так и списком.
    :type media: Union[SimpleNamespace, List[SimpleNamespace], str, List[str]]
    :param no_video: Флаг, указывающий, что видео не загружается.
    :type no_video: bool, optional
    :param without_captions: Флаг, указывающий, что подписи не добавляются.
    :type without_captions: bool, optional
    :return: True, если медиафайлы были успешно загружены, иначе None.
    :rtype: bool | None

    :raises Exception: Если возникла ошибка во время загрузки медиа или обновления подписи.

    :Example:

    .. code-block:: python

        driver = Driver(...)
        products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        upload_media(driver, products)
        True
    """
    if not media:
        logger.debug("Нет медиа для сообщения!")
        return

    # Открывает форму 'добавить медиа'.
    if not d.execute_locator(locator=locator.open_add_foto_video_form):
        return
    d.wait(0.5)

    # Убеждаемся, что products это список.
    media_list: list = media if isinstance(media, list) else [media]
    ret: bool = True

    # Итерируется по продуктам и загружает медиафайлы.
    for m in media_list:
        if isinstance(m, SimpleNamespace):
            try:
                # Определяет путь к медиафайлу в зависимости от наличия атрибута 'local_saved_video' и флага no_video.
                media_path = m.local_saved_video if hasattr(m, 'local_saved_video') and not no_video else m.local_saved_image
            except Exception as ex:
                logger.error(f"Ошибка в поле \'local_saved_image\'", exc_info=True)
                continue  # Переходим к следующему медиафайлу
        elif isinstance(m, (str, Path)):
             media_path = m
        else:
            logger.error(f"Неверный тип медиафайла: {type(m)}")
            continue  # Переходим к следующему медиафайлу

        try:
            # Загружает медиафайл.
            if d.execute_locator(locator=locator.foto_video_input, message=str(media_path), timeout=20):
                d.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return
        except Exception as ex:
            logger.error("Ошибка при загрузке медиа", ex, exc_info=True)
            return
    if without_captions:
        return True
    # Обновляет подписи к загруженным медиафайлам.
    if not d.execute_locator(locator=locator.edit_uloaded_media_button):
        logger.error(f"Не удалось нажать кнопку редактирования загруженного изображения")
        return

    uploaded_media_frame = d.execute_locator(locator=locator.uploaded_media_frame)
    if not uploaded_media_frame:
        logger.debug(f"Не найдены поля ввода подписей к изображениям")
        return

    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator=locator.edit_image_properties_textarea, timeout=10, timeout_for_event='presence_of_element_located')
    if not textarea_list:
        logger.error("Не найдены поля ввода подписи к изображениям")
        return

    # Обновляет подписи к изображениям.
    update_images_captions(d, media_list, textarea_list)

    return ret

def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """Добавляет описания к загруженным медиафайлам.

    :param d: Экземпляр драйвера, используемый для взаимодействия со страницей.
    :type d: Driver
    :param media: Список объектов SimpleNamespace с данными для обновления подписей.
    :type media: List[SimpleNamespace]
    :param textarea_list: Список элементов textarea, куда добавляются подписи.
    :type textarea_list: List[WebElement]
    :raises Exception: Если возникла ошибка при обновлении подписей к медиа.
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))


    def handle_product(product: SimpleNamespace, textarea: WebElement, i: int) -> None:
        """Обновляет подписи к медиа для одного продукта.

        :param product: Продукт, для которого обновляются подписи.
        :type product: SimpleNamespace
        :param textarea: Элемент textarea, куда добавляется подпись.
        :type textarea: WebElement
        :param i: Индекс продукта в списке.
        :type i: int
        """
        lang = product.language.upper()
        direction = getattr(local_units.LOCALE, lang, "LTR")
        message = ""
         # Добавляет детали продукта в сообщение.
        try:
            if direction == "LTR":
                if hasattr(product, 'product_title'):
                    message += f"{product.product_title}\n"

                if hasattr(product, 'description'):
                    message += f'{product.description}\n'

                if hasattr(product, 'original_price'):
                    message += f"{getattr(local_units.original_price, lang)}: {product.original_price} {product.target_original_price_currency}\n"

                if hasattr(product, 'sale_price') and hasattr(product, 'discount') and product.discount != '0%':
                    message += f"{getattr(local_units.discount, lang)}: {product.discount}\n"
                    message += f"{getattr(local_units.sale_price, lang)}: {product.sale_price} {product.target_original_price_currency} \n"

                if hasattr(product, 'evaluate_rate') and product.evaluate_rate != '0.0%':
                    message += f"{getattr(local_units.evaluate_rate, lang)}: {product.evaluate_rate}\n"

                if hasattr(product, 'promotion_link'):
                    message += f"{getattr(local_units.promotion_link, lang)}: {product.promotion_link}\n"
            else:  # RTL direction
                if hasattr(product, 'product_title'):
                     message += f"\n{product.product_title}"

                if hasattr(product, 'description'):
                    message += f'{product.description}\n'

                if hasattr(product, 'original_price'):
                    message += f"\n {product.target_original_price_currency} {product.original_price} :{getattr(local_units.original_price, lang)}"

                if hasattr(product, 'sale_price') and hasattr(product, 'discount') and product.discount != '0%':
                    message += f"\n{product.discount} :{getattr(local_units.discount, lang)}"
                    message += f"\n {product.target_original_price_currency} {product.sale_price} :{getattr(local_units.sale_price, lang)}"

                if hasattr(product, 'evaluate_rate') and product.evaluate_rate != '0.0%':
                    message += f"\n{product.evaluate_rate} :{getattr(local_units.evaluate_rate, lang)}"

                if hasattr(product, 'promotion_link'):
                    message += f"\n{product.promotion_link} :{getattr(local_units.promotion_link, lang)}"
        except Exception as ex:
            logger.error("Ошибка при генерации сообщения", ex, exc_info=True)
            return

        # Отправляет сообщение в textarea.
        try:
            textarea.send_keys(message)
            return True
        except Exception as ex:
            logger.error("Ошибка при отправке текста в textarea", ex)
            return

    # Обрабатывает каждый продукт и обновляет его подпись.
    for i, product in enumerate(media):
         if i < len(textarea_list):
            handle_product(product, textarea_list[i], i)
         else:
            logger.warning(f"Пропущена подпись для продукта {product} из-за нехватки textarea")

def publish(d:Driver, attempts: int = 5) -> bool:
    """Публикует сообщение.

     :param d: Экземпляр драйвера, используемый для взаимодействия со страницей.
    :type d: Driver
    :param attempts: Количество попыток публикации сообщения.
    :type attempts: int
    :return: True, если публикация прошла успешно, иначе None.
    :rtype: bool | None
    """
    if attempts < 0:
        return

    if not d.execute_locator(locator=locator.finish_editing_button, timeout=1):
        logger.debug(f"Не удалось обработать локатор {locator.finish_editing_button}")
        return
    d.wait(1)

    if not d.execute_locator(locator=locator.publish, timeout=5):
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts - 1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts - 1)
        if attempts > 0:
            d.wait(5)
            publish(d, attempts - 1)

        logger.debug(f"Не удалось обработать локатор {locator.finish_editing_button}")
        return

    while not d.execute_locator(locator=locator.open_add_post_box, timeout=10, timeout_for_event='element_to_be_clickable'):
        logger.debug(f"Не освободилось поле ввода {attempts=}",None, False)
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts - 1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts - 1)
        if attempts > 0:
            d.wait(2)
            publish(d, attempts - 1)

    return True


def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """Управляет процессом продвижения сообщения с заголовком, описанием и медиафайлами.

    :param d: Экземпляр драйвера, используемый для взаимодействия со страницей.
    :type d: Driver
    :param category: Детали категории для заголовка и описания сообщения.
    :type category: SimpleNamespace
    :param products: Список продуктов, содержащих медиа и детали для публикации.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий, что видео не загружается.
    :type no_video: bool, optional

    :Example:

    .. code-block:: python

        driver = Driver(...)
        category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
        products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
        promote_post(driver, category, products)
    """
    if not post_title(d, category):
        return
    d.wait(0.5)

    if not upload_media(d, products, no_video):
        return
    if not d.execute_locator(locator=locator.finish_editing_button):
        return
    if not d.execute_locator(locator=locator.publish, timeout=20):
        logger.debug("Публикация...")
        return
    return True

def post_message(d: Driver, message: SimpleNamespace, no_video: bool = False, images: Optional[Union[str, List[str]]] = None, without_captions: bool = False) -> bool:
    """Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

    :param d: Экземпляр драйвера, используемый для взаимодействия со страницей.
    :type d: Driver
    :param message: Детали сообщения для заголовка и описания.
    :type message: SimpleNamespace
    :param no_video: Флаг, указывающий, что видео не загружается.
    :type no_video: bool, optional
    :param images: Путь к изображению или список путей к изображениям.
    :type images: Optional[Union[str, List[str]]], optional
    :param without_captions: Флаг, указывающий, что подписи не добавляются.
    :type without_captions: bool, optional
    :return: True, если публикация прошла успешно, иначе None.
    :rtype: bool | None
    :Example:

    .. code-block:: python

        driver = Driver(...)
        message = SimpleNamespace(title="Заголовок сообщения", description="Описание сообщения")
        post_message(driver, message,  images=['path/to/image1.jpg', 'path/to/image2.jpg'])
    """
    if not post_title(d, message):
        return
    d.wait(0.5)

    if not upload_media(d, message.products, no_video=no_video, without_captions=without_captions):
        return
    d.wait(0.5)

    if d.execute_locator(locator=locator.send):
        """Выход, если было одно изображение"""
        return True

    if not d.execute_locator(locator=locator.finish_editing_button):
        return

    if not publish(d):
        return

    return True
```