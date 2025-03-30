## Анализ кода модуля `post_message`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Код хорошо структурирован и содержит docstring для большинства функций.
  - Используются `SimpleNamespace` для хранения данных, что упрощает доступ к атрибутам.
  - Присутствуют логирование с использованием `logger`.
- **Минусы**:
  - Не все функции имеют docstring.
  - В некоторых местах используются `...` как заполнители, что указывает на незавершенность кода.
  - Некоторые docstring требуют уточнения и дополнения.
  - Есть места, где не хватает обработки исключений.
  - Не везде аннотированы типы.

**Рекомендации по улучшению**:

1. **Документация**:
   - Добавить docstring для функции `publish`.
   - Улучшить существующие docstring, добавив более подробное описание аргументов и возвращаемых значений.
   - Добавить примеры использования в docstring, где это возможно.

2. **Обработка исключений**:
   - Добавить обработку исключений в тех местах, где сейчас используется `...`.
   - Уточнить сообщения логирования, чтобы они были более информативными.

3. **Типизация**:
   - Добавить аннотации типов для всех аргументов и возвращаемых значений функций, где это отсутствует.

4. **Использование `j_loads_ns`**:
   - Убедиться, что все JSON файлы загружаются с использованием `j_loads_ns` для единообразия.

5. **Комментарии**:
   - Пересмотреть и, при необходимости, обновить комментарии, чтобы они соответствовали текущему коду.
   - Избегать общих фраз, таких как "получаем" или "делаем". Использовать более конкретные: "извлекаем", "проверяем", "выполняем".

6. **Улучшение логики**:
   - В функции `upload_media` добавить более детальное логирование при ошибке загрузки изображения.
   - В функции `update_images_captions` добавить логирование при возникновении ошибки генерации сообщения.

**Оптимизированный код**:

```python
## \file /src/endpoints/advertisement/facebook/scenarios/post_message.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.advertisement.facebook.scenarios
	:platform: Windows, Unix
	:synopsis: Публикация сообщения

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


# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement'/ 'facebook' / 'locators'/ 'post_message.json')
)

def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """Отправляет заголовок и описание кампании в поле сообщения.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        message (SimpleNamespace | str): Объект SimpleNamespace или строка, содержащая заголовок и описание для отправки.

    Returns:
        bool: `True`, если заголовок и описание были успешно отправлены, иначе `False`.

    Example:
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, message)
        True
    """
    # Scroll backward in the page
    if not d.scroll(1, 1200, 'backward'):
        logger.error('Scroll failed during post title')
        return False

    # Open the 'add post' box
    if not d.execute_locator(locator = locator.open_add_post_box):
        logger.debug('Failed to open \'add post\' box')
        return False

    # Add the message to the post box
    m =  f'{message.title}\\n{message.description}' if isinstance(message, SimpleNamespace) else message
    # if isinstance(message, SimpleNamespace) and hasattr( message,'tags'):
    #     m = f"{m}\\nTags: {message.tags}"

    if not d.execute_locator(locator.add_message, message = m, timeout = 5, timeout_for_event = 'element_to_be_clickable'):
        logger.debug(f'Failed to add message to post box: {m=}')
        return False

    return True

def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],   no_video: bool = False, without_captions:bool = False) -> bool:
    """Загружает медиафайлы в раздел изображений и обновляет подписи.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        media (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Список продуктов, содержащих пути к медиафайлам.
        no_video (bool): Флаг, указывающий, следует ли игнорировать видео.
        without_captions (bool): Флаг, указывающий, следует ли пропускать обновление подписей.

    Returns:
        bool: `True`, если медиафайлы были успешно загружены, иначе `False`.

    Raises:
        Exception: Если возникает ошибка во время загрузки медиа или обновления подписи.

    Example:
        >>> driver = Driver(...)
        >>> media = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, media)
        True
    """
    if not media:
        logger.debug('Нет медиа для сообщения!')
        return False
    # Step 1: Open the 'add media' form. It may already be open.
    if not d.execute_locator(locator.open_add_foto_video_form):
        return False
    d.wait(0.5)

    # Step 2: Ensure products is a list.
    media_list:list = media if  isinstance(media, list) else [media]
    ret: bool = True

    # Iterate over products and upload media.
    for m in media_list:
        if isinstance(m, SimpleNamespace):
            try:
                media_path = m.local_video_path if hasattr(m, 'local_video_path') and not no_video else m.local_image_path
            except Exception as ex:
                logger.debug('Ошибка в поле \'local_image_path\'')
                ...
        elif isinstance(m, (str, Path)):
            media_path = m
        ...
        try:
            # Upload the media file.
            if d.execute_locator(locator = locator.foto_video_input, message = str(media_path) , timeout = 20):
                d.wait(1.5)
            else:
                logger.error(f'Ошибка загрузки изображения {media_path=}')
                return False
        except Exception as ex:
            logger.error('Error in media upload', ex, exc_info=True)
            return False
    if without_captions:
        return True
    # Step 3: Update captions for the uploaded media.
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f'Ошибка загрузки изображения {media_path=}')
        return False
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    if not uploaded_media_frame:
        logger.debug('Не нашлись поля ввода подписей к изображениям')
        return False

    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator = locator.edit_image_properties_textarea, timeout = 10, timeout_for_event = 'presence_of_element_located' )
    if not textarea_list:
        logger.error('Не нашлись поля ввода подписи к изображениям')
        return False
    # Update image captions.
    update_images_captions(d, media, textarea_list)

    return ret

def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """Добавляет описания к загруженным медиафайлам.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        media (List[SimpleNamespace]): Список продуктов с деталями для обновления.
        textarea_list (List[WebElement]): Список текстовых областей, в которые добавляются подписи.

    Raises:
        Exception: Если возникает ошибка при обновлении подписей медиафайлов.
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """Обновляет подписи медиафайлов для одного продукта.

        Args:
            product (SimpleNamespace): Продукт для обновления.
            textarea_list (List[WebElement]): Список текстовых областей, в которые добавляются подписи.
            i (int): Индекс продукта в списке.
        """
        lang = product.language.upper()
        direction = getattr(local_units.LOCALE, lang, 'LTR')
        message = ''

        # Add product details to message.
        try:
            if direction == 'LTR':
                if hasattr(product, 'product_title'):
                    message += f'{product.product_title}\\n'

                if hasattr(product, 'description'):
                    message += f'{product.description}\\n'

                if hasattr(product, 'original_price'):
                    message += f'{getattr(local_units.original_price, lang)}: {product.original_price} {product.target_original_price_currency}\\n'

                if hasattr(product, 'sale_price') and hasattr(product, 'discount') and product.discount != '0%':
                    message += f'{getattr(local_units.discount, lang)}: {product.discount}\\n'
                    message += f'{getattr(local_units.sale_price, lang)}: {product.sale_price} {product.target_original_price_currency} \\n'

                if hasattr(product, 'evaluate_rate') and product.evaluate_rate != '0.0%':
                    message += f'{getattr(local_units.evaluate_rate, lang)}: {product.evaluate_rate}\\n'

                if hasattr(product, 'promotion_link'):
                    message += f'{getattr(local_units.promotion_link, lang)}: {product.promotion_link}\\n'

                # if hasattr(product, 'tags'):
                #     message += f"{getattr(local_units.tags, lang)}: {product.tags}\\n"
                # message += f"{getattr(local_units.COPYRIGHT, lang)}"

            else:  # RTL direction
                if hasattr(product, 'product_title'):
                    message += f'\\n{product.product_title}'

                if hasattr(product, 'description'):
                    message += f'{product.description}\\n'

                if hasattr(product, 'original_price'):
                    message += f'\\n {product.target_original_price_currency} {product.original_price} :{getattr(local_units.original_price, lang)}'

                if hasattr(product, 'sale_price') and hasattr(product, 'discount') and product.discount != '0%':
                    message += f'\\n{product.discount} :{getattr(local_units.discount, lang)}'
                    message += f'\\n {product.target_original_price_currency} {product.sale_price} :{getattr(local_units.sale_price, lang)}'

                if hasattr(product, 'evaluate_rate') and product.evaluate_rate != '0.0%':
                    message += f'\\n{product.evaluate_rate} :{getattr(local_units.evaluate_rate, lang)}'

                if hasattr(product, 'promotion_link'):
                    message += f'\\n{product.promotion_link} :{getattr(local_units.promotion_link, lang)}'

                # if hasattr(product, 'tags'):
                #     message += f"\\n{product.tags} :{getattr(local_units.tags, lang)}"
                # message += f"\\n{getattr(local_units.COPYRIGHT, lang)}"

        except Exception as ex:
            logger.error('Error in message generation', ex, exc_info=True)
            return

        # Send message to textarea.
        try:
            textarea_list[i].send_keys(message)
            return True
        except Exception as ex:
            logger.error('Error in sending keys to textarea', ex)
            return

    # Process products and update their captions.
    for i, product in enumerate(media):
        handle_product(product, textarea_list, i)

def publish(d: Driver, attempts: int = 5) -> bool:
    """Опубликовывает сообщение после редактирования.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        attempts (int, optional): Количество попыток публикации. По умолчанию 5.

    Returns:
        bool: `True`, если публикация прошла успешно, иначе `False`.
    """
    ...
    if attempts < 0:
        return False
    if not d.execute_locator(locator.finish_editing_button, timeout = 1):
        logger.debug(f'Неудача обработки локатора {locator.finish_editing_button}')
        return False
    d.wait(1)
    if not d.execute_locator(locator.publish, timeout = 5):
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts -1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts -1)
        if attempts > 0:
           d.wait(5)
           publish(d, attempts -1)

        logger.debug(f'Неудача обработки локатора {locator.finish_editing_button}')
        return False

    while not d.execute_locator(locator = locator.open_add_post_box, timeout = 10, timeout_for_event = 'element_to_be_clickable'):
        logger.debug(f'не освободилось поле ввода {attempts=}',None, False)
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts -1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts -1)
        if attempts > 0:
           d.wait(2)
           publish(d, attempts -1)

    return True


def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        category (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
        products (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.

    Returns:
        bool: `True`, если продвижение прошло успешно, иначе `False`.

    Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    if not post_title(d, category):
        return False
    d.wait(0.5)

    if not upload_media(d, products, no_video):
        return False
    if not d.execute_locator(locator = locator.finish_editing_button):
        return False
    if not d.execute_locator(locator.publish, timeout = 20):
        print('Publishing...')
        return False
    return True


def post_message(d: Driver, message: SimpleNamespace,  no_video: bool = False,  images:Optional[str | list[str]] = None, without_captions:bool = False) -> bool:
    """Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        message (SimpleNamespace): Детали сообщения, используемые для заголовка и описания поста.
        no_video (bool): Флаг, указывающий, следует ли игнорировать видео.
        images (Optional[str | list[str]], optional): Список изображений для загрузки. По умолчанию `None`.
        without_captions (bool): Флаг, указывающий, следует ли пропускать обновление подписей.

    Returns:
        bool: `True`, если продвижение прошло успешно, иначе `False`.

    Example:
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_message(driver, message)
    """
    if not post_title(d, message):
        return False
    d.wait(0.5)

    if not upload_media(d, message.products, no_video = no_video, without_captions = without_captions):
        return False
    d.wait(0.5)

    if d.execute_locator(locator = locator.send):
        """ Выход, если было одно изображение """
        return True

    if not d.execute_locator(locator = locator.finish_editing_button):
        return False

    if not publish(d):
        return False

    return True