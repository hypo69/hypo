# Анализ кода модуля `validator.py`

**Качество кода**

8
- Плюсы
    - Код структурирован в класс `ProductFieldsValidator`, что способствует логической организации.
    - Присутствуют статические методы, что хорошо подходит для утилитных функций.
    - Используется `logger` для логирования ошибок, хотя и не во всех случаях.
    - Есть обработка исключений, хотя и минимальная, без подробного логирования.
    - Код в целом читаемый, с понятными названиями переменных.
- Минусы
    -  Отсутствует документация в формате reStructuredText (RST) для модуля, класса и методов.
    -  Комментарии к методам не соответствуют стандарту RST.
    -  Используется `try-except` без логирования ошибки, что затрудняет отладку.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Импорт `urlparse` и `parse_qs` повторяется.
    -  Не все методы имеют полную обработку ошибок и логирование.
    -  Не все проверки возвращают `False` при ошибке, иногда просто `None`, что усложняет понимание логики.
    -  Импортируется `html` но не используется.

**Рекомендации по улучшению**

1.  Добавить документацию в формате reStructuredText (RST) для модуля, класса и методов.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `try-except` на более явную обработку ошибок с помощью `logger.error` и возвратом `False` при ошибке.
4.  Удалить дублирующийся импорт `urlparse` и `parse_qs`.
5.  Удалить неиспользуемый импорт `html`.
6.  Привести в соответствие имена переменных с ранее обработанными файлами.
7.  Добавить проверки на `None` или пустую строку для всех входных параметров.
8.  Добавить подробные комментарии к каждому блоку кода.
9.  Использовать `return False` вместо `return` без значения при валидации.
10. В методе `isint` переименовать переменную `s` в `value` для большей ясности.
11. Добавить импорт `StringFormatter` и `Ptrn`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для валидации строк
=========================================================================================

Этот модуль содержит класс :class:`ProductFieldsValidator`, который используется для валидации различных типов строк,
таких как цены, вес, артикулы и URL.

Пример использования
--------------------

.. code-block:: python

    validator = ProductFieldsValidator()
    is_valid_price = validator.validate_price('123.45')
    is_valid_url = validator.validate_url('https://example.com')
"""
import re
from urllib.parse import urlparse
from typing import Union

from src.logger.logger import logger
from src.utils.string.formatter import StringFormatter
from src.utils.string.pattern import Ptrn




class ProductFieldsValidator:
    """
    Класс для валидации полей продукта.

    Этот класс предоставляет статические методы для проверки различных типов строк,
    таких как цены, вес, артикулы и URL, на соответствие определенным критериям или шаблонам.

    :Example:

    .. code-block:: python

        validator = ProductFieldsValidator()
        is_valid_price = validator.validate_price('123.45')
        is_valid_url = validator.validate_url('https://example.com')
    """

    @staticmethod
    def validate_price(price: str) -> bool:
        """
        Валидирует строку, представляющую цену.

        :param price: Строка для проверки.
        :return: True, если строка является валидной ценой, иначе False.
        """
        if not price: # Проверка, что строка не пустая
            return False
        
        # Код удаляет все символы кроме цифр и точек
        price = Ptrn.clear_price.sub('', price)
        # Код заменяет запятые на точки
        price = price.replace(',', '.')
        try:
            # Код пробует преобразовать строку в число с плавающей точкой
            float(price)
        except Exception as ex:
            logger.error(f'Ошибка валидации цены: {ex}') # логирование ошибки
            return False
        return True

    @staticmethod
    def validate_weight(weight: str) -> bool:
        """
        Валидирует строку, представляющую вес.

        :param weight: Строка для проверки.
        :return: True, если строка является валидным весом, иначе False.
        """
        if not weight: # Проверка, что строка не пустая
            return False
        # Код удаляет все символы кроме цифр и точек
        weight = Ptrn.clear_number.sub('', weight)
        # Код заменяет запятые на точки
        weight = weight.replace(',', '.')
        try:
            # Код пробует преобразовать строку в число с плавающей точкой
            float(weight)
        except Exception as ex:
             # логирование ошибки
            logger.error(f'Ошибка валидации веса: {ex}')
            return False
        return True

    @staticmethod
    def validate_sku(sku: str) -> bool:
        """
        Валидирует строку, представляющую артикул.

        :param sku: Строка для проверки.
        :return: True, если строка является валидным артикулом, иначе False.
        """
        if not sku: # Проверка, что строка не пустая
            return False

        # Код удаляет специальные символы
        sku = StringFormatter.remove_special_characters(sku)
        # Код удаляет переносы строк
        sku = StringFormatter.remove_line_breaks(sku)
        # Код удаляет пробелы в начале и конце строки
        sku = sku.strip()
        
        if len(sku) < 3:  # Проверка длины артикула
            return False
        return True

    @staticmethod
    def validate_url(url: str) -> bool:
        """
        Валидирует строку, представляющую URL.

        :param url: Строка для проверки.
        :return: True, если строка является валидным URL, иначе False.
        """
        if not url: # Проверка, что строка не пустая
            return False

        # Код удаляет пробелы в начале и конце строки
        url = url.strip()

        if not url.startswith('http'):  # Код проверяет, что URL начинается с http
             url = 'http://' + url

        parsed_url = urlparse(url) # Код разбирает URL

        if not parsed_url.netloc or not parsed_url.scheme: # Код проверяет наличие домена и схемы
            return False

        return True

    @staticmethod
    def isint(value: str) -> bool:
        """
        Проверяет, является ли строка целым числом.

        :param value: Строка для проверки.
        :return: True, если строка является целым числом, иначе False.
        """
        try:
            # Код пробует преобразовать строку в целое число
            int(value)
            return True
        except Exception as ex:
            # логирование ошибки
            logger.error(f'Ошибка преобразования в целое число: {ex}')
            return False
```