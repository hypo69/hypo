```diff
--- a/hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py
+++ b/hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py
@@ -1,16 +1,15 @@
 # -*- coding: utf-8 -*-
-#! venv/Scripts/python.exe
-#! venv/bin/python
 """ module: src.endpoints.advertisement.facebook.scenarios """
 MODE = 'development'
 
-
-
 """ Публикация сообщения из алиэкспресс промо """
 
+import asyncio
 import time
-import asyncio
+from json import JSONDecodeError
+
+import json
 from pathlib import Path
 from types import SimpleNamespace
 from typing import Dict, List
@@ -18,6 +17,7 @@
 from src import gs
 from src.webdriver import Driver
 from src.utils import j_loads_ns, pprint
+from src.utils import j_loads
 from src.logger import logger
 
 # Load locators from JSON file.
@@ -25,6 +25,17 @@
     Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
 )
 
+
+def _validate_driver(d: Driver) -> bool:
+    """Проверка, что драйвер работает."""
+    if not d:
+        logger.error("Драйвер не инициализирован.")
+        return False
+    return True
+
+
+
+
 def post_title(d: Driver, category: SimpleNamespace) -> bool:
     """ Sends the title and description of a campaign to the post message box.
 
@@ -38,15 +49,15 @@
         >>> post_title(driver, category)
         True
     """
-    # Scroll backward in the page
-    if not d.scroll(1, 1200, 'backward'):
-        logger.error("Scroll failed during post title", exc_info=False)
-        return
-
-    # Open the 'add post' box
-    if not d.execute_locator(locator.open_add_post_box):
-        logger.error("Failed to open 'add post' box", exc_info=False)
-        return
+    if not _validate_driver(d):
+        return False
+
+    if not d.scroll(1, 1200, 'backward'):
+        logger.error("Прокрутка страницы не удалась.")
+        return False
+
+    if not d.execute_locator(locator.open_add_post_box):
+        logger.error("Не удалось открыть окно публикации.")
+        return False
 
     # Construct the message with title and description
     message = f"{category.title}; {category.description};"
@@ -54,7 +65,7 @@
     # Add the message to the post box
     if not d.execute_locator(locator.add_message, message):
         logger.error(f"Не удалось добавить сообщение в поле: {message=}", exc_info=False)
-        return
+        return False
 
     return True
 
@@ -76,20 +87,24 @@
         >>> await upload_media(driver, products)
         True
     """
-    # Step 1: Open the 'add media' form. It may already be open.
-    if not d.execute_locator(locator.open_add_foto_video_form): 
-        return
+    if not _validate_driver(d):
+        return False
+
+    if not d.execute_locator(locator.open_add_foto_video_form):
+        logger.error("Не удалось открыть форму добавления медиа.")
+        return False
+
     d.wait(0.5)
 
-    # Step 2: Ensure products is a list.
     products = products if isinstance(products, list) else [products]
     ret: bool = True
 
     # Iterate over products and upload media.
     for product in products:
         media_path = product.local_saved_video if hasattr(product, 'local_saved_video') and not no_video else product.local_saved_image
-        try:
-            # Upload the media file.
+        if not media_path:
+            logger.error(f"Путь к медиафайлу не указан: {media_path=}")
+            return False
+
+        # Upload media file.
             if d.execute_locator(locator.foto_video_input, media_path):
                 d.wait(1.5)
             else:
@@ -97,27 +112,27 @@
                 return
         except Exception as ex:
             logger.error("Error in media upload", ex, exc_info=True)
-            return
+            return False
 
-    # Step 3: Update captions for the uploaded media.
-    if not d.execute_locator(locator.edit_uloaded_media_button):
-        logger.error(f"Ошибка загрузки изображения {media_path=}")
-        return
+    if not d.execute_locator(locator.edit_uloaded_media_button):
+        logger.error("Не удалось найти кнопку редактирования медиа.")
+        return False
     uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
     uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
     d.wait(0.3)
 
     textarea_list = d.execute_locator(locator.edit_image_properties_textarea)
-    if not textarea_list:
-        logger.error("Не нашлись пля ввода подписи к изображениям")
-        return
+    if not textarea_list or not isinstance(textarea_list,list):
+        logger.error("Не удалось найти поля для ввода подписи к изображениям.")
+        return False
     # Asynchronously update image captions.
     await update_images_captions(d, products, textarea_list)
 
     return ret
 
 
-async def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
+async def update_images_captions(
+    d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]
+) -> None:
     """ Adds descriptions to uploaded media files asynchronously.
 
     Args:
@@ -130,7 +145,7 @@
 
     Raises:
         Exception: If there's an error updating the media captions.
-    """
+    """  
     local_units = j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))
 
     def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
@@ -151,7 +166,7 @@
                     message += f"{getattr(local_units.original_price, product.language)}: {product.original_price}\n"
                 if hasattr(product, 'sale_price'):
                     message += f"{getattr(local_units.sale_price, product.language)}: {product.sale_price}\n"
-                if hasattr(product, 'discount'):
+                if hasattr(product, 'discount') and product.discount:
                     message += f"{getattr(local_units.discount, product.language)}: {product.discount}\n"
                 if hasattr(product, 'evaluate_rate'):
                     message += f"{getattr(local_units.evaluate_rate, product.language)}: {product.evaluate_rate}\n"
@@ -171,7 +186,7 @@
                     message += f"\n{product.promotion_link} :{getattr(local_units.promotion_link, product.language)}"
                 if hasattr(product, 'tags'):
                     message += f"\n{product.tags} :{getattr(local_units.tags, product.language)}"
-                message += f"\n{getattr(local_units.COPYRIGHT, product.language)}"
+                message += f"\n{getattr(local_units.COPYRIGHT, product.language, '')}"
                 
         except Exception as ex:
             logger.error("Error in message generation", ex, exc_info=True)
@@ -180,9 +195,12 @@
         # Send message to textarea.
         if textarea_list[i].send_keys(message): 
             return True
-
-        logger.error("Error in sending keys to textarea")
-
+        else:
+           logger.error("Ошибка отправки текста в textarea.")
+           return False
+
+    return False
+
     # Process products and update their captions asynchronously.
     for i, product in enumerate(products):
         await asyncio.to_thread(handle_product, product, textarea_list, i)
@@ -194,12 +212,15 @@
         d (Driver): The driver instance used for interacting with the webpage.
         category (SimpleNamespace): The category details used for the post title and description.
         products (List[SimpleNamespace]): List of products containing media and details to be posted.
+        no_video (bool): Optional flag to skip video upload (defaults to False).
 
     Examples:
         >>> driver = Driver(...)
         >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
         >>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
         >>> await promote_post(driver, category, products)
+
+    Returns:
+        bool: True if post promotion was successful, otherwise False.
     """
     if not post_title(d, category): 
         return

```