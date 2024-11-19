```diff
--- a/hypotez/src/suppliers/amazon/product_fields.py
+++ b/hypotez/src/suppliers/amazon/product_fields.py
@@ -1,6 +1,6 @@
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
-#! venv/Scripts/python.exe
+
 #! venv/bin/python
 """ module: src.suppliers.amazon """
 MODE = 'development'
@@ -19,7 +19,6 @@
 """ Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
 1. Заполняю поля, необходимые для создания нового товара
 2. Получаю `id_product` созданного товара
-3. Используя полученный `id_product` загружаю дефолтную картинку
 4. итд.
 """
 
@@ -31,6 +30,7 @@
 from src.logger import logger
 from src.utils import StringFormatter, StringNormalizer
 from src.product import Product, ProductFields
+import asyncio
 from src.suppliers import Supplier
 # ----------------------------
 
@@ -42,38 +42,47 @@
     1. (->) Добавляю поля, необходимые для создания нового товара
     2. (<-) Получаю `id_product` созданного товара
     3. (->) Используя полученный `id_product` загружаю дефолтную картинку и другие элементы
-            в новый товар
+       в новый товар
     4. итд.
     """
 
+    # Обработка полей, которые вероятно требуют асинхронной операции
+    # (следует пересмотреть логику и заменить asyncio.run на соответствующие
+    # асинхронные функции или методы)
+    #TODO:  Асинхронные операции требуют переработки
 
-    
-    _field.active = asyncio.run (  )
-    _field.additional_delivery_times = asyncio.run (  )
-    _field.additional_shipping_cost  = asyncio.run (  )
-    _field.advanced_stock_management = asyncio.run (  )
-    _field.affiliate_short_link = asyncio.run (  )
-    _field.affiliate_summary = asyncio.run (  )
-    _field.affiliate_summary_2 = asyncio.run (  )
-    _field.affiliate_text = asyncio.run (  )
-    _field.available_date = asyncio.run (  )
-    _field.available_for_order = asyncio.run (  )
-    _field.available_later = asyncio.run (  )
-    _field.available_now = asyncio.run (  )
-    _field.cache_default_attribute = asyncio.run (  )
-    _field.cache_has_attachments = asyncio.run (  )
-    _field.cache_is_pack = asyncio.run (  )
-    #_field.category_ids_append <- добавочные категории.
-    #_field.category_ids <- 
-    _field.condition = asyncio.run (  )
-    _field.customizable = asyncio.run (  )
-    _field.date_add = asyncio.run (  )
-    _field.date_upd = asyncio.run (  )
-    _field.delivery_in_stock = asyncio.run (  )
-    _field.delivery_out_stock = asyncio.run (  )
-    _field.depth = asyncio.run (  )
-    _field.description = asyncio.run (  )
-    _field.description_short = asyncio.run (  )
-    _field.ean13 = asyncio.run (  )
-    _field.ecotax = asyncio.run (  )
-    _field.height = asyncio.run (  )
+    # Пример обработки поля
+    try:
+        f.active = await s.driver.execute_locator(l['active'])
+    except Exception as e:
+        logger.error(f"Error processing 'active': {e}")
+    # ... аналогично для остальных полей
+
+    # Избегайте повторения кода. Используйте цикл или list comprehension
+    # для обработки полей. Пример:
+    # for field in f.__dict__:
+    #     try:
+    #         f.__dict__[field] = await s.driver.execute_locator(l[field])
+    #     except Exception as e:
+    #         logger.error(f"Error processing '{field}': {e}")
+
+    # Далее код для заполнения других полей
+    l = s.reread_locators('product')
+    _ = s.driver.execute_locator
+
+    # Поля, которые требуют обработки
+    for field_name in ['price', 'name', 'description_short', 'affiliate_short_link', 'images_urls']:
+        try:
+            f.__dict__[field_name] = _(l[field_name])[0]
+        except (KeyError, IndexError) as e:
+            logger.error(f"Error getting '{field_name}': {e}")
+
+    #TODO: Обработать исключения при загрузке данных из locators
     _field.how_to_use = asyncio.run (  )
     _field.id_category_default = asyncio.run (  )
     _field.id_default_combination = asyncio.run (  )

```