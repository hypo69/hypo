## Анализ кода модуля `post_message.py`

**Качество кода**

-   Соответствие требованиям: 8/10
    -   **Плюсы:**
        -   Используется `j_loads_ns` для загрузки JSON.
        -   Присутствуют docstring для функций, что соответствует требованиям.
        -   Используется `logger` для логирования ошибок.
        -   Код разбит на логические функции, что улучшает читаемость.
    -   **Минусы:**
        -   Не везде используются константы для timeout значений, что затрудняет изменение значений в одном месте.
        -   В некоторых местах используются `print()` вместо `logger.debug`.
        -   Некоторые блоки `try-except` слишком общие, можно уточнить тип исключений.
        -   Иногда используется `return` без значения, что может привести к неопределенному поведению.
        -   Отсутствует описание модуля в начале файла.
        -   Не все переменные имеют описания.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:** В начале файла необходимо добавить описание модуля в формате, указанном в инструкции.
2.  **Использовать константы для таймаутов:**  Вместо магических чисел для таймаутов, использовать константы, чтобы было легче управлять временем ожидания.
3.  **Заменить `print()` на `logger.debug()`:** Использовать `logger.debug()` для отладочных сообщений вместо `print()`.
4.  **Уточнить типы исключений:** Вместо общих `Exception`, использовать более конкретные типы исключений.
5.  **Проверять возвращаемое значение функций:** Убедиться, что функции, которые должны возвращать `bool` или значения, действительно это делают.
6.  **Добавить комментарии к переменным:** Описать переменные для улучшения читаемости кода.
7.  **Улучшить обработку ошибок:**  Добавить обработку ошибок в `try except` с указанием исключения.
8.  **Проверять наличие атрибутов:** Перед обращением к атрибутам объекта проверять их наличие с помощью `hasattr()`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
# file: /src/endpoints/advertisement/facebook/scenarios/post_message.py

#! venv/bin/python/python3.12

"""
Модуль для управления публикациями сообщений в Facebook.
=========================================================================================

Этот модуль предоставляет функции для автоматизации процесса публикации сообщений в Facebook,
включая добавление текста, загрузку медиафайлов и обновление подписей к изображениям.

Пример использования
--------------------

Пример использования функции `post_message`:

.. code-block:: python

    from src.webdriver.driver import Driver
    from types import SimpleNamespace

    driver = Driver(...)
    message = SimpleNamespace(
        title='Заголовок сообщения',
        description='Описание сообщения',
        products=[
            SimpleNamespace(local_image_path='path/to/image.jpg',
                         product_title='Название продукта',
                         description='Описание продукта',
                         original_price='100',
                         sale_price='90',
                         discount='10%',
                         evaluate_rate='4.5',
                         promotion_link='https://example.com'),
            SimpleNamespace(local_image_path='path/to/image2.jpg',
                         product_title='Название продукта 2',
                         description='Описание продукта 2',
                         original_price='200',
                         sale_price='180',
                         discount='10%',
                         evaluate_rate='4.8',
                         promotion_link='https://example2.com'),
        ]
    )
    result = post_message(driver, message)
    print(result)  # Выведет True, если публикация прошла успешно
"""

import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List, Optional, Any
from selenium.webdriver.remote.webelement import WebElement
from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.utils.printer import pprint
from src.logger.logger import logger

# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement'/ 'facebook' / 'locators'/ 'post_message.json')
)

# Константы для таймаутов
TIMEOUT_SHORT: int = 1
TIMEOUT_MEDIUM: int = 5
TIMEOUT_LONG: int = 20

def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        message (SimpleNamespace | str): Сообщение для публикации. Может быть объектом SimpleNamespace с полями
            `title` и `description` или просто строкой.

    Returns:
        bool: True, если заголовок и описание были успешно отправлены, иначе False.

    Example:
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, message)
        True
    """
    # Код прокручивает страницу назад
    if not d.scroll(1, 1200, 'backward'):
        logger.error('Не удалось прокрутить страницу во время установки заголовка')
        return False

    # Код открывает окно добавления сообщения
    if not d.execute_locator(locator = locator.open_add_post_box):
        logger.debug('Не удалось открыть окно \'add post\'')
        return False

    # Формирует сообщение для отправки
    m =  f"{message.title}\\n{message.description}" if isinstance(message, SimpleNamespace) else message
    # if isinstance(message, SimpleNamespace) and hasattr( message,'tags'):
    #     m = f"{m}\\nTags: {message.tags}"

    # Код добавляет сообщение в поле
    if not d.execute_locator(locator.add_message, message = m, timeout = TIMEOUT_MEDIUM, timeout_for_event = 'element_to_be_clickable'):
        logger.debug(f'Не удалось добавить сообщение в поле ввода: {m=}')
        return False

    return True


def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],   no_video: bool = False, without_captions:bool = False) -> bool:
    """
    Загружает медиафайлы и обновляет подписи к ним.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        media (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Медиафайлы для загрузки.
            Может быть одним объектом `SimpleNamespace` или списком объектов с полями `local_image_path`
            или `local_video_path`, строкой с путем к файлу или списком строк.
        no_video (bool, optional): Если True, то не загружать видео. По умолчанию False.
        without_captions (bool, optional): Если True, то не обновлять подписи. По умолчанию False.

    Returns:
        bool: True, если медиафайлы успешно загружены, иначе False.

    Raises:
        Exception: Если произошла ошибка при загрузке медиа или обновлении подписей.

    Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
    if not media:
        logger.debug('Нет медиа для сообщения!')
        return False

    # Код открывает форму добавления медиафайлов
    if not d.execute_locator(locator.open_add_foto_video_form):
        return False
    d.wait(0.5)

    # Код приводит медиа к списку для итерации
    media_list:list = media if  isinstance(media, list) else [media]
    ret: bool = True

    # Код итерируется по списку медиафайлов и загружает их
    for m in media_list:
        if isinstance(m, SimpleNamespace):
            try:
                media_path = m.local_video_path if hasattr(m, 'local_video_path') and not no_video else m.local_image_path
            except Exception as ex:
                logger.debug(f"Ошибка в поле \'local_image_path\'", exc_info=True)
                ...
                continue
        elif isinstance(m, (str, Path)):
            media_path = m
        else:
            continue
        try:
            # Код загружает медиафайл
            if d.execute_locator(locator = locator.foto_video_input, message = str(media_path) , timeout = TIMEOUT_LONG):
                d.wait(1.5)
            else:
                logger.error(f'Ошибка загрузки изображения {media_path=}')
                return False
        except Exception as ex:
            logger.error('Ошибка при загрузке медиа', exc_info=True)
            return False
    if without_captions:
        return True
    # Код открывает форму редактирования загруженных медиафайлов
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f'Ошибка открытия окна редактирования загруженных изображений')
        return False
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    if not uploaded_media_frame:
        logger.debug('Не найдены поля ввода подписей к изображениям')
        return False

    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator = locator.edit_image_properties_textarea, timeout = 10, timeout_for_event = 'presence_of_element_located' )
    if not textarea_list:
        logger.error('Не найдены поля ввода подписи к изображениям')
        return False
    # Код обновляет подписи к изображениям
    update_images_captions(d, media, textarea_list)

    return ret


def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Добавляет описания к загруженным медиафайлам.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        media (List[SimpleNamespace]): Список объектов `SimpleNamespace` с деталями для обновления.
        textarea_list (List[WebElement]): Список полей ввода текста, куда добавляются подписи.

    Raises:
        Exception: Если произошла ошибка при обновлении подписей к медиа.
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """
        Обновляет подписи к медиафайлу для одного продукта.

        Args:
            product (SimpleNamespace): Продукт, для которого нужно обновить подписи.
            textarea_list (List[WebElement]): Список полей ввода текста.
            i (int): Индекс продукта в списке.
        """
        lang = product.language.upper()
        direction = getattr(local_units.LOCALE, lang, "LTR")
        message = ""

        # Код добавляет детали продукта в сообщение в зависимости от направления текста
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

                # if hasattr(product, 'tags'):
                #     message += f"{getattr(local_units.tags, lang)}: {product.tags}\\n"
                # message += f"{getattr(local_units.COPYRIGHT, lang)}"

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

                # if hasattr(product, 'tags'):
                #     message += f"\\n{product.tags} :{getattr(local_units.tags, lang)}"
                # message += f"\\n{getattr(local_units.COPYRIGHT, lang)}"

        except Exception as ex:
            logger.error("Ошибка при формировании сообщения", ex, exc_info=True)
            return

        # Код отправляет сообщение в поле ввода
        try:
            textarea_list[i].send_keys(message)
            return True
        except Exception as ex:
            logger.error("Ошибка при отправке сообщения в поле ввода", ex)
            return

    # Код итерируется по списку медиа и обновляет их подписи
    for i, product in enumerate(media):
        handle_product(product, textarea_list, i)


def publish(d:Driver, attempts: int = 5) -> bool:
    """
    Публикует сообщение.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        attempts (int, optional): Количество попыток публикации. По умолчанию 5.

    Returns:
        bool: True, если публикация прошла успешно, иначе False.
    """
    if attempts < 0:
        return False
    # Код нажимает кнопку завершения редактирования
    if not d.execute_locator(locator.finish_editing_button, timeout = TIMEOUT_SHORT):
        logger.debug(f"Неудача обработки локатора {locator.finish_editing_button}")
        return False
    d.wait(1)
    # Код нажимает кнопку публикации
    if not d.execute_locator(locator.publish, timeout = TIMEOUT_MEDIUM):
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts -1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts -1)
        if attempts > 0:
           d.wait(5)
           publish(d, attempts -1)

        logger.debug(f"Неудача обработки локатора {locator.finish_editing_button}")
        return False
    # Код ждет пока поле ввода не станет доступным
    while not d.execute_locator(locator = locator.open_add_post_box, timeout = 10, timeout_for_event = 'element_to_be_clickable'):
        logger.debug(f"не освободилось поле ввода {attempts=}",None, False)
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts -1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts -1)
        if attempts > 0:
           d.wait(2)
           publish(d, attempts -1)

    return True


def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Управляет процессом продвижения публикации, включая заголовок, описание и медиафайлы.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        category (SimpleNamespace): Детали категории, используемые для заголовка и описания публикации.
        products (List[SimpleNamespace]): Список продуктов, содержащих медиафайлы и детали для публикации.
        no_video (bool, optional): Если True, то не загружать видео. По умолчанию False.

    Returns:
        bool: True, если продвижение прошло успешно, иначе False.

    Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    # Код публикует заголовок
    if not post_title(d, category):
        return False
    d.wait(0.5)
    # Код загружает медиафайлы
    if not upload_media(d, products, no_video):
        return False
    # Код нажимает кнопку завершения редактирования
    if not d.execute_locator(locator = locator.finish_editing_button):
        return False
    # Код нажимает кнопку публикации
    if not d.execute_locator(locator.publish, timeout = TIMEOUT_LONG):
        print('Публикация...')
        return False
    return True


def post_message(d: Driver, message: SimpleNamespace,  no_video: bool = False,  images:Optional[str | list[str]] = None, without_captions:bool = False) -> bool:
    """
    Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        message (SimpleNamespace): Детали сообщения, используемые для заголовка и описания публикации.
        no_video (bool, optional): Если True, то не загружать видео. По умолчанию False.
        images (Optional[str | list[str]], optional): Путь к медиафайлу или список путей. По умолчанию None.
        without_captions (bool, optional): Если True, то не обновлять подписи. По умолчанию False.

    Returns:
        bool: True, если публикация прошла успешно, иначе False.

    Example:
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(title="Campaign Title", description="Campaign Description", products=[...])
        >>> post_message(driver, message)
        True
    """
    # Код устанавливает заголовок сообщения
    if not post_title(d, message):
        return False
    d.wait(0.5)
    # Код загружает медиафайлы
    if not upload_media(d, message.products, no_video = no_video, without_captions = without_captions):
        return False
    d.wait(0.5)

    # Код проверяет было ли одно изображение
    if d.execute_locator(locator = locator.send):
        return True
    # Код нажимает кнопку завершения редактирования
    if not d.execute_locator(locator = locator.finish_editing_button):
        return False
    # Код публикует сообщение
    if not publish(d):
        return False

    return True