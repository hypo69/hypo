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
    """ Sends the title and description of a campaign to the post message box.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category containing the title and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    # Scroll backward in the page
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Scroll failed during post title")
        return

    # Open the 'add post' box
    if not d.execute_locator(locator = locator.open_add_post_box):
        logger.debug("Failed to open 'add post' box")
        return

    # Add the message to the post box
    m =  f"{message.title}\n{message.description}" if isinstance(message, SimpleNamespace) else message
    # if isinstance(message, SimpleNamespace) and hasattr( message,'tags'):
    #     m = f"{m}\nTags: {message.tags}"

    if not d.execute_locator(locator.add_message, message = m, timeout = 5, timeout_for_event = 'element_to_be_clickable'):
        logger.debug(f"Failed to add message to post box: {m=}")
        return

    return True

def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],   no_video: bool = False, without_captions:bool = False) -> bool:
    """ Uploads media files to the images section and updates captions.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products containing media file paths.

    Returns:
        bool: `True` if media files were uploaded successfully, otherwise `None`.

    Raises:
        Exception: If there is an error during media upload or caption update.

    Examples:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
    if not media:
        logger.debug("Нет медиа для сообщения!")
        return
    # Step 1: Open the 'add media' form. It may already be open.
    if not d.execute_locator(locator.open_add_foto_video_form): 
        return
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
                logger.debug(f"Ошибка в поле 'local_image_path'")
                ...
        elif isinstance(m, (str, Path)):
            media_path = m
        ...
        try:
            # Upload the media file.
            if d.execute_locator(locator = locator.foto_video_input, message = str(media_path) , timeout = 20):
                d.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return
        except Exception as ex:                                                                 
            logger.error("Error in media upload", ex, exc_info=True)
            return
    if without_captions:
        return True
    # Step 3: Update captions for the uploaded media.
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Ошибка загрузки изображения {media_path=}")
        return
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    if not uploaded_media_frame:
        logger.debug(f"Не нашлись поля ввода подписей к изображениям")
        return

    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)

    textarea_list = d.execute_locator(locator = locator.edit_image_properties_textarea, timeout = 10, timeout_for_event = 'presence_of_element_located' )
    if not textarea_list:
        logger.error("Не нашлись поля ввода подписи к изображениям")
        return
    # Update image captions.
    update_images_captions(d, media, textarea_list)

    return ret


def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """ Adds descriptions to uploaded media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.

    Raises:
        Exception: If there's an error updating the media captions.
    """
    local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))

    def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
        """ Handles the update of media captions for a single product.

        Args:
            product (SimpleNamespace): The product to update.
            textarea_list (List[WebElement]): List of textareas where captions are added.
            i (int): Index of the product in the list.
        """
        lang = product.language.upper()
        direction = getattr(local_units.LOCALE, lang, "LTR")
        message = ""

        # Add product details to message.
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

                # if hasattr(product, 'tags'):
                #     message += f"{getattr(local_units.tags, lang)}: {product.tags}\n"
                # message += f"{getattr(local_units.COPYRIGHT, lang)}"
                
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

                # if hasattr(product, 'tags'):
                #     message += f"\n{product.tags} :{getattr(local_units.tags, lang)}"
                # message += f"\n{getattr(local_units.COPYRIGHT, lang)}"
                
        except Exception as ex:
            logger.error("Error in message generation", ex, exc_info=True)
            return 

        # Send message to textarea.
        try:
            textarea_list[i].send_keys(message) 
            return True
        except Exception as ex:
            logger.error("Error in sending keys to textarea", ex)
            return

    # Process products and update their captions.
    for i, product in enumerate(media):
        handle_product(product, textarea_list, i)

def publish(d:Driver, attempts = 5) -> bool:
    """"""
    ...
    if attempts < 0:
        return 
    if not d.execute_locator(locator.finish_editing_button, timeout = 1):
        logger.debug(f"Неудача обработки локатора {locator.finish_editing_button}")
        return 
    d.wait(1)
    if not d.execute_locator(locator.publish, timeout = 5): 
        if d.execute_locator(locator.close_pop_up):
            publish(d, attempts -1)
        if d.execute_locator(locator.not_now):
            publish(d, attempts -1)
        if attempts > 0:
           d.wait(5)
           publish(d, attempts -1)

        logger.debug(f"Неудача обработки локатора {locator.finish_editing_button}")
        return

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
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    if not post_title(d, category): 
        return
    d.wait(0.5)

    if not upload_media(d, products, no_video): 
        return
    if not d.execute_locator(locator = locator.finish_editing_button): 
        return
    if not d.execute_locator(locator.publish, timeout = 20):
        print("Publishing...")
        return
    return True



def post_message(d: Driver, message: SimpleNamespace,  no_video: bool = False,  images:Optional[str | list[str]] = None, without_captions:bool = False) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        message (SimpleNamespace): The message details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    if not post_title(d, message): 
        return
    d.wait(0.5)

    if not upload_media(d, message.products, no_video = no_video, without_captions = without_captions): 
        return
    d.wait(0.5)

    if d.execute_locator(locator = locator.send): 
        """ Выход, если было одно изображение """
        return True

    if not d.execute_locator(locator = locator.finish_editing_button): 
        return

    if not publish(d):
        return


    return True

