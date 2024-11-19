```diff
--- a/hypotez/src/product/product_fields/product_fields.py
+++ b/hypotez/src/product/product_fields/product_fields.py
@@ -1,6 +1,7 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-#! venv/Scripts/python.exe
+
+import json
 #! venv/bin/python
 """ module: src.product.product_fields """
 MODE = 'development'
@@ -23,7 +24,7 @@
     # Определение вероятностей нескольких языков
     languages = detect_langs(text)
     print(f"Detected languages: {languages}")
-    
+
     from langdetect import detect, detect_langs, LangDetectException
 
     try:
@@ -37,7 +38,7 @@
     except LangDetectException as ex:
         print("Error detecting language", ex)
 
-.. todo:: Внимательно посмотреть, как работает langdetect
+
 """
 Наименование полей в классе соответствуют именам полей в таблицах `PrestaShop`
 Порядок полей в этом файле соответствует номерам полей в таблице, 
@@ -82,13 +83,16 @@
 
 
 from pathlib import Path
-from typing import List, Dict, Optional, Callable, Any
+from typing import List, Dict, Optional, Any
 from pydantic import BaseModel, Field, validator
 from types import SimpleNamespace, MappingProxyType
-from sqlite3 import Date
-from langdetect import detect
+from datetime import date, datetime
+from src.utils.date import date_to_string
 from functools import wraps
 from enum import Enum
+
+
+
+
 
 import header
 from src.utils.jjson import j_loads, j_loads_ns
@@ -102,7 +106,7 @@
 
 
 class ProductFields(BaseModel):
-    """Класс, описывающий поля товара в формате API PrestaShop."""
+    """Model for product fields in PrestaShop format."""
     
     class Config:
         arbitrary_types_allowed = True
@@ -110,17 +114,19 @@
     product_fields_list: List[str] = Field(default_factory=lambda: [
         read_text_file(gs.path.src / 'product' / 'product_fields' / 'fields_list.txt', as_list=True)
     ])
-    language: Dict[str, int] = Field(default_factory=lambda: {'en': 1, 'he': 2, 'ru': 3})
+    language_codes: Dict[str, int] = Field(default_factory=lambda: {'en': 1, 'he': 2, 'ru': 3})
     presta_fields: SimpleNamespace = Field(init=False)
     assist_fields_dict: Dict[str, Optional[str]] = Field(default_factory=lambda: {
         'default_image_url': '', 
-        'images_urls': []
+        'images_urls': [],
     })
+    
+    
 
     def __post_init__(self):
         """Класс работы с полями товара. Поля берутся со страниц HTML или другого источника и форматируются в стандарте API PrestaShop Dictionary."""
         self.presta_fields = SimpleNamespace(**{key: None for key in self.product_fields_list})
-        self._payload()
+        self._load_default_values()
 
     def _payload(self) -> bool:
         """Загрузка дефолтных значений полей."""
@@ -130,7 +136,7 @@
             logger.debug(f"Ошибка загрузки полей из файла {gs.path.src}/product/product_fields/product_fields_default_values.json")
             return False
         for name, value in data.items():
-            setattr(self, name, value)
+            setattr(self, name, self._normalize_value(name, value))
         return True
 
     @property
@@ -141,7 +147,7 @@
 
     @associations.setter
     def associations(self, value: Dict[str, Optional[str]]):
-        """Устанавливает словарь ассоциаций."""
+        """Sets the associations dictionary."""
         self.presta_fields.associations = value
 
     
@@ -149,8 +155,7 @@
         self.presta_fields.associations = value
 
     @property    
-    def id_product(self) -> Optional[int]:
-        """ <sub>*[property]*</sub>  `ps_product.id: int(10) unsigned` """
+    def id_product(self) -> Optional[int]:  """ Product ID."""
         return self.presta_fields.id_product
 
     
@@ -166,12 +171,7 @@
             return
 
 
-#   2   Поставщик
     @property
-    def id_supplier(self):
-        """  <sub>*[property]*</sub>  `ps_product.id_supplier: int(10) unsigned`
-         @details: привязываю товар к id поставщика
-        """
+    def id_supplier(self) -> Optional[int]:  """ Supplier ID."""
         return self.presta_fields.id_supplier or None
     
     
@@ -186,13 +186,9 @@
             return
 
 
-#   3   Бренд
     
     @property
-    def id_manufacturer(self) -> int:
-        """  <sub>*[property]*</sub> `ps_product.id_manufacturer: int(10) unsigned`
-        field
-         @details: means BRAND. 
+    def id_manufacturer(self) -> Optional[int]:  """ Manufacturer (brand) ID."""
             Бренд может быть передан как по имени так и по ID.
             Таблица брендов:
 
@@ -202,12 +198,10 @@
         return self.presta_fields.id_manufacturer or None
     
     
-    @id_manufacturer.setter
-    def id_manufacturer(self, value: int = None):
-        """  <sub>*[setter]*</sub>  Бренд может быть передан как по имени так и по ID 
-
-         `ps_product.id_manufacturer`
-        field type: int(10) unsigned
+    @id_manufacturer.setter
+    def id_manufacturer(self, value: Optional[int]):  """ Sets the Manufacturer ID."""
+        
+        
          @details: привязываю товар к бренду
         """
         try:
@@ -310,7 +304,8 @@
         return self.presta_fields.quantity_discount  or None
 
     
-    @quantity_discount.setter
+    @quantity_discount.setter
+    def quantity_discount(self, value: int = 0) -> bool:  """Sets the quantity discount."""
      
     def quantity_discount(self, value: int = 0) -> bool:
         """  <sub>*[setter]*</sub>   """
@@ -1372,17 +1367,6 @@
         return self.presta_fields.local_saved_image  or None
 
     @local_saved_image.setter
-    def local_saved_image(self, value:str = None) -> bool:
-        """  <sub>*[setter]* local_saved_image</sub>   """
-        ...
-        try:
-            if value:
-                self.presta_fields.local_saved_image = value
-            ...
-        except ProductFieldException as ex:
-            logger.error(f"""Ошибка заполнения поля: 'local_saved_image' данными {value}""", ex)
-            ...
-            return    
 
     @property
     def local_saved_video(self):
@@ -1390,6 +1374,23 @@
             путь к видео , сохраннёному на диске"""
         return self.presta_fields.images_urls  or None
 
+    def _normalize_value(self, field_name: str, value: Any) -> Any:
+        """Normalizes the value based on the field name."""
+        if field_name == 'available_date' and isinstance(value, str):
+            try:
+                return datetime.strptime(value, '%Y-%m-%d').date()
+            except ValueError as e:
+                logger.error(f"Invalid date format for {field_name}: {value}, error: {e}")
+                return None
+        elif field_name == 'available_date' and isinstance(value, datetime):
+            return value.date()
+        elif field_name in ('price', 'ecotax', 'wholesale_price', 'width', 'height', 'depth', 'weight', 'minimal_quantity', 'low_stock_threshold', 'unit_price_ratio', 'additional_shipping_cost'):
+            try:
+                return float(value)
+            except ValueError as e:
+                logger.error(f"Invalid number format for {field_name}: {value}, error: {e}")
+                return None
+        return value
+
     @local_saved_video.setter
     def local_saved_video(self, value:str = None) -> bool:
         """  <sub>*[setter]* local_saved_image</sub>   """

```