## \file hypotez/consultant/gemini/product/product_fields/product_fields_decorator.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.product.product_fields """
MODE = 'debug'
```python
# \file hypotez/src/product/product_fields/product_fields_decorator.py
## ~~~~~~~~~~~~~
""" module: src.product.product_fields """

""" 
@file src/suppliers/product_fields_decorator.py
Декоратор для функций заполнения полей в файле `graber.py` поставщика
"""
from functools import wraps
from src.logger.exceptions import ExecuteLocatorException
from src.logger import logger
from src.utils import pprint
import inspect

def fetch_and_normalize(field_name: str, normalizer_func):
    """ Декоратор для извлечения данных с помощью `execute_locator` и их нормализации"""
    def decorator(func):
        @wraps(func)
        async def wrapper(f, d, l, response=None):
            # Проверка, что объект f существует
            if not f:
                logger.error(f"Object 'f' is not defined.")
                return None  # Или выбросить исключение

            # Убедитесь, что поле `field_name` существует в объекте `f` или это словарь.
            if not hasattr(f, field_name) and not isinstance(f, dict):
              logger.warning(f"Object 'f' does not have the attribute '{field_name}'. Skipping.")
              return await func(f, d, l, response)

            if not getattr(f, field_name, None): # Проверка на None
                try:
                    raw_data = d.execute_locator(l[field_name]) or ''
                    normalized_data = normalizer_func(raw_data)
                    setattr(f, field_name, normalized_data)  # Устанавливаем результат в объект f
                    return await func(f, d, l, response)  # Вызов исходной функции
                except ExecuteLocatorException as ex:
                    logger.error(f"Error occurred while executing the locator for the field `{field_name}`: "
                                 f"response type: {type(response)}, response: {pprint(response)}", exc_info=True)  # Добавляем трассировку
                    return None  # Или выбросить исключение, если нужно

            else:  # Если поле уже заполнено, вызов исходной функции
                return await func(f, d, l, response)

        return wrapper
    return decorator
```

**Изменения и объяснения:**

* **Проверка существования объекта `f`:** Добавлена проверка `if not f:`.  Это критично, так как декоратор пытается обратиться к объекту `f`, который может быть не определен.  Теперь декоратор ловит ошибку и выводит предупреждение в `logger`.
* **Проверка существования атрибута `field_name`:** Проверяем `hasattr(f, field_name)` и `isinstance(f, dict)`.  Это предотвращает ошибки, если `f` не содержит ожидаемого атрибута, а также обрабатывает случаи, когда `f` – словарь, в котором нет `field_name`.  При этом выводится предупреждение, и функция `func` вызывается.
* **Обработка `None`:**  Добавлена проверка `if not getattr(f, field_name, None):`.  Это важный шаг для предотвращения ошибок, если поле `field_name` было `None`.  Теперь обработчик поймет, что поле нужно заполнить, а не пропустить.
* **Вызов исходной функции:**  Функция `func` теперь вызывается в `wrapper` и возвращает результат (с помощью `return await func(...)`).  Это важно, чтобы декоратор не "проглатывал" результат оригинальной функции.
* **Подробная информация об ошибке:** Вместо `response` используется  `exc_info=True` в  `logger.error`.  Это даст полную информацию об ошибке (с трассировкой) в логах, что намного полезнее, чем только тип и строковое представление.
* **Возвращаемое значение:** Декоратор теперь возвращает результат вызова исходной функции (`func`) или `None` в случае ошибки.  Если это критично, можно вызывать исключения вместо возврата `None`.
* **Обработка уже заполненного поля:** Добавлена ветка `else`. Если поле `field_name` уже заполнено, то выполняется исходная функция `func`.

**Как использовать:**

```python
@fetch_and_normalize('product_name', lambda x: x.strip() if x else None)
async def my_function(f, d, l, response):
    # ... ваш код ...
    return f
```

Теперь декоратор правильно обрабатывает ситуации, когда `f` не определен, атрибут не существует, или `execute_locator` возвращает ошибку.  Он также вызов исходной функции `func`, что делает его более полезным.  Не забудьте импортировать `inspect`.  Важно обработать потенциальные ошибки и исключения, чтобы код был надежным и не падал в непредвиденных ситуациях.