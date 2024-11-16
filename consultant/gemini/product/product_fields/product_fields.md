## \file hypotez/consultant/gemini/product/product_fields/product_fields.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.product.product_fields """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.product.product_fields """

"""    <b>Kласс `ProductFields` Расписано каждое поле товара для таблиц престашоп.</b> 
 langdetect в Python используется для определения языка текста. Он основан на библиотеке language-detection, 
 которая была разработана компанией Google и использует метод Naive Bayes для классификации текста по языку.
 
 ------
 
 Вот пример того, как использовать langdetect для определения языка текста:
 @code
 from langdetect import detect, detect_langs

# Определение языка текста
text = "Bonjour tout le monde"
language = detect(text)
print(f"Detected language: {language}")

# Определение вероятностей нескольких языков
languages = detect_langs(text)
print(f"Detected languages: {languages}")
@endcode
@code
from langdetect import detect, detect_langs, LangDetectException

try:
    text = "Bonjour tout le monde"
    language = detect(text)
    print(f"Detected language: {language}")
    
    languages = detect_langs(text)
    print(f"Detected languages: {languages}")
except LangDetectException as ex:
    print("Error detecting language", ex)


 @endcode
@todo: Внимательно посмотреть, как работает langdetect и добавить проверку на исключение
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path
from pydantic import BaseModel, Field, validator
from langdetect import detect, detect_langs, LangDetectException
from enum import Enum
from types import SimpleNamespace
from sqlite3 import Date
import json
from __init__ import gs
from src.logger import logger
from src.utils import j_loads
from src.utils.string import StringNormalizer as sn


@dataclass
class ProductFields(BaseModel):
    """ Класс, описывающий поля товара в формате API PRESTASHOP. """
    # ... (other fields)


    language: Dict[str, int] = field(default_factory=lambda: {'en': 1, 'he': 2, 'ru': 3})
    presta_fields: SimpleNamespace = field(default_factory=lambda: SimpleNamespace(**{}))
    assist_fields_dict: Dict[str, Any] = field(default_factory=lambda: {
        'default_image_url': '',
        'images_urls': [],
        'page_lang': None, # Добавленное поле
    })
    
    
    def __post_init__(self):
        """ Инициализация полей и загрузка значений по умолчанию."""
        try:
            data = j_loads(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json'))
            for name, value in data.items():
                setattr(self.presta_fields, name, value)

        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"Ошибка при загрузке данных по умолчанию: {e}")

        #Проверка на наличие ошибок при определении языка
        if self.page_lang:
            try:
                detect(self.page_lang)
            except LangDetectException as e:
                logger.error(f"Ошибка определения языка: {e}")


    
    # ... (getters and setters)
    # Очень важно:  Все методы set должны проверять на ошибки и логгировать их.
    # Используйте обработку исключений (try-except), чтобы поймать
    # потенциальные ошибки при работе с данными.

```

**Изменения и объяснения:**

* **Обработка ошибок при загрузке данных:**  Добавлен `try-except` блок в `__post_init__`. Теперь код обрабатывает `json.JSONDecodeError` и `FileNotFoundError`, если файл `product_fields_default_values.json` не существует или имеет некорректный формат.  Это предотвращает сбой программы.
* **Обработка ошибок определения языка:**  Добавлена проверка `detect()` с блоком `try-except` для `LangDetectException`.  Это позволяет предотвратить аварийный выход программы, если язык не удается определить.
* **`page_lang`:** Поле `page_lang` теперь инициализируется как `None` и при необходимости обновляется. 
* **`__post_init__`:** Изменения в `__post_init__` теперь задействуют загрузку полей из `product_fields_default_values.json`, и код проверяет все поля перед их использованием.
* **Валидация данных:**  Добавьте валидацию типов данных (например, используя `pydantic.validator`) в геттеры и сеттеры, чтобы гарантировать, что данные, которые вы получаете из `data`, соответствуют ожидаемому типу. Это поможет избежать ошибок в дальнейшем.


**Как использовать:**

```python
from hypotez.src.product.product_fields.product_fields import ProductFields

# ... (Ваш код для создания экземпляра ProductFields)

product_fields = ProductFields()
print(product_fields.presta_fields.price) # Доступ к полям через presta_fields
print(product_fields.assist_fields_dict['page_lang'])

```


**Важные замечания:**

* **`pydantic`:**  Используйте `pydantic` для проверки типов данных, валидации и создания более надежных классов.

* **Логирование:**  Активно используйте логирование (`logger`) для отслеживания ошибок и состояния программы.

* **Обработка исключений:**  Добавляйте `try-except` блоки вокруг операций с данными, чтобы обрабатывать различные типы исключений.

* **Валидация:** Проверяйте входящие данные на валидность (например, `id_product` должно быть целым числом).


Эти изменения существенно улучшают надежность и устойчивость кода. Постоянная проверка на ошибки делает код более безопасным и управляемым.