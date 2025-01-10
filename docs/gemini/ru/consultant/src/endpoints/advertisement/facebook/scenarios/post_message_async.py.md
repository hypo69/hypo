# Анализ кода модуля `post_message_async`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, с разделением на функции для каждой задачи (публикация заголовка, загрузка медиа, обновление подписей).
    - Используется асинхронность для выполнения задач, что может улучшить производительность.
    - Присутствует логирование ошибок с использованием `logger.error`, что помогает в отладке.
    - Используется `j_loads_ns` для загрузки локаторов, что соответствует требованиям.
- Минусы
    - Не все функции и методы имеют docstring в формате reStructuredText (RST).
    - Используются устаревшие комментарии `# ...`, необходимо переделать их в формат docstring
    - В некоторых местах используется `try-except` без необходимости, лучше использовать logger.error().
    - Использование `exc_info=True` в logger.error не всегда оправдано, так как может мешать читаемости логов.
    - В функции `handle_product` не возвращается значение, хотя это ожидается в цикле `await asyncio.to_thread`.
   - Есть небольшие несоответствия в комментариях и реальным действиям кода.
   - Есть дублирование кода `logger.error(f"Ошибка загрузки изображения {media_path=}")`

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST для всех функций, методов, классов и модуля.
2.  Убрать избыточные блоки `try-except`, заменив их на `logger.error`.
3.  Использовать `exc_info=False` по умолчанию в logger.error, если не требуется трассировка стека.
4.  Сделать функцию `handle_product` возвращающей значение.
5.  Устранить дублирование кода в logger.error, вынеся его в отдельную функцию или переменну.
6.  Использовать более конкретные сообщения в logger.error, чтобы упростить отладку.
7.  Добавить проверки на наличие атрибутов объекта перед их использованием.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для асинхронной публикации сообщений в Facebook.
======================================================

Этот модуль предоставляет функции для автоматической публикации сообщений,
включая текст, изображения и видео, на странице Facebook с использованием
Selenium WebDriver. Функции обеспечивают загрузку медиафайлов, добавление
описаний к ним и публикацию поста.

Пример использования:
--------------------

.. code-block:: python

    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs
    import asyncio

    async def main():
        driver = Driver()
        category = j_loads_ns({'title': "Заголовок", 'description': "Описание"})
        products = [j_loads_ns({'local_image_path': "path/to/image.jpg", 'product_title': "Продукт", 'original_price': "100", 'sale_price': "50", 'discount': "50%", 'evaluate_rate': "5", 'promotion_link': "https://example.com", 'tags': "#tag1 #tag2", 'language': 'ru'})]
        await promote_post(driver, category, products)

    if __name__ == "__main__":
        asyncio.run(main())

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


# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)

def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения.

    :param d: Экземпляр драйвера WebDriver.
    :type d: Driver
    :param category: SimpleNamespace, содержащий заголовок и описание.
    :type category: SimpleNamespace
    :return: True, если заголовок и описание успешно отправлены, иначе None.
    :rtype: bool
    """
    # Проверка и прокрутка страницы назад
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Ошибка прокрутки страницы при отправке заголовка")
        return False

    # Открытие окна добавления сообщения
    if not d.execute_locator(locator.open_add_post_box):
        logger.error("Не удалось открыть окно добавления сообщения")
        return False

    # Формирование сообщения из заголовка и описания
    message = f"{category.title}; {category.description};"

    # Добавление сообщения в поле сообщения
    if not d.execute_locator(locator.add_message, message):
        logger.error(f"Не удалось добавить сообщение в поле: {message=}")
        return False

    return True

async def upload_media(d: Driver, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """
    Загружает медиафайлы (изображения или видео) и обновляет подписи к ним.

    :param d: Экземпляр драйвера WebDriver.
    :type d: Driver
    :param products: Список SimpleNamespace, содержащих пути к медиафайлам.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий на отсутствие видео.
    :type no_video: bool
    :return: True, если медиафайлы успешно загружены и подписи обновлены, иначе None.
    :rtype: bool
    :raises Exception: Если произошла ошибка во время загрузки или обновления подписей.
    """
    # Открытие формы добавления медиа
    if not d.execute_locator(locator.open_add_foto_video_form):
        logger.error("Не удалось открыть форму добавления медиа")
        return False
    d.wait(0.5)

    # Приведение products к списку
    products = products if isinstance(products, list) else [products]
    ret: bool = True

    # Загрузка медиафайлов
    for product in products:
        media_path = product.local_video_path if hasattr(product, 'local_video_path') and not no_video else product.local_image_path
        try:
            # Загрузка медиафайла
            if d.execute_locator(locator.foto_video_input, media_path):
                d.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return False
        except Exception as ex:
            logger.error("Ошибка при загрузке медиа", exc_info=False)
            return False

    # Обновление подписей для загруженных медиафайлов
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Не удалось нажать кнопку редактирования загруженных медиа {media_path=}")
        return False
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)
    textarea_list = d.execute_locator(locator.edit_image_properties_textarea)
    if not textarea_list:
        logger.error("Не найдены поля ввода подписи к изображениям")
        return False
    # Асинхронное обновление подписей
    await update_images_captions(d, products, textarea_list)

    return ret


async def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Добавляет описания к загруженным медиафайлам асинхронно.

    :param d: Экземпляр драйвера WebDriver.
    :type d: Driver
    :param products: Список объектов SimpleNamespace с информацией о продуктах.
    :type products: List[SimpleNamespace]
    :param textarea_list: Список веб-элементов textarea для ввода подписей.
    :type textarea_list: List[WebElement]
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea: WebElement, i: int) -> bool:
        """
        Обрабатывает обновление подписи к медиафайлу для одного продукта.

        :param product: Объект SimpleNamespace с информацией о продукте.
        :type product: SimpleNamespace
        :param textarea: Веб-элемент textarea для ввода подписи.
        :type textarea: WebElement
        :param i: Индекс продукта в списке.
        :type i: int
        :return: True, если подпись успешно добавлена, иначе None.
        :rtype: bool
        """
        direction = getattr(local_units.LOCALE, product.language, "LTR")
        message = ""
        # Сборка сообщения для подписи
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
            logger.error("Ошибка при генерации сообщения для подписи", exc_info=False)
            return False

        # Отправка сообщения в textarea
        if textarea.send_keys(message):
            return True
        else:
             logger.error("Ошибка при отправке текста в textarea")
             return False

    # Асинхронная обработка продуктов
    for i, (product, textarea) in enumerate(zip(products, textarea_list)):
        await asyncio.to_thread(handle_product, product, textarea, i)


async def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """
    Управляет процессом публикации сообщения, включая заголовок, описание и медиафайлы.

    :param d: Экземпляр драйвера WebDriver.
    :type d: Driver
    :param category: SimpleNamespace с данными о категории для заголовка и описания.
    :type category: SimpleNamespace
    :param products: Список SimpleNamespace с информацией о продуктах и медиафайлах.
    :type products: List[SimpleNamespace]
    :param no_video: Флаг, указывающий на отсутствие видео.
    :type no_video: bool
    :return: True, если сообщение успешно опубликовано, иначе None.
    :rtype: bool
    """
    # Публикация заголовка и описания
    if not post_title(d, category):
        return False
    d.wait(0.5)
    # Загрузка медиа
    if not await upload_media(d, products, no_video):
        return False
    # Завершение редактирования
    if not d.execute_locator(locator.finish_editing_button):
        return False
    # Публикация
    if not d.execute_locator(locator.publish):
        return False
    return True
```