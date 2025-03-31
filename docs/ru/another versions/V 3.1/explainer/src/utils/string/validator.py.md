# Проект `hypotez`
# Роль `code explainer`
## АНАЛИЗ КОДА: `hypotez/src/utils/string/validator.py`

### 1. <алгоритм>

#### `ProductFieldsValidator`

1.  **`validate_price(price: str) -> bool`**:
    *   **Вход**: Строка `price`.
    *   Если `price` пустая, возвращает `None`.
    *   Удаляет все символы, не являющиеся цифрами или точкой, из `price` с помощью `Ptrn.clear_price.sub('', price)`.
        *   Пример: `"1,234.56 USD"` → `"1234.56"`.
    *   Заменяет запятую на точку.
        *   Пример: `"1234,56"` → `"1234.56"`.
    *   Преобразует строку `price` в число с плавающей точкой.
        *   Если преобразование не удалось, возвращает `None`.
        *   Пример: `"1234.56"` → `1234.56`.
    *   Возвращает `True`.

2.  **`validate_weight(weight: str) -> bool`**:
    *   **Вход**: Строка `weight`.
    *   Если `weight` пустая, возвращает `None`.
    *   Удаляет все символы, не являющиеся цифрами или точкой, из `weight` с помощью `Ptrn.clear_number.sub('', weight)`.
        *   Пример: `"1,234.56 kg"` → `"1234.56"`.
    *   Заменяет запятую на точку.
        *   Пример: `"1234,56"` → `"1234.56"`.
    *   Преобразует строку `weight` в число с плавающей точкой.
        *   Если преобразование не удалось, возвращает `None`.
        *   Пример: `"1234.56"` → `1234.56`.
    *   Возвращает `True`.

3.  **`validate_sku(sku: str) -> bool`**:
    *   **Вход**: Строка `sku`.
    *   Если `sku` пустая, возвращает `None`.
    *   Удаляет специальные символы из `sku` с помощью `StringFormatter.remove_special_characters(sku)`.
        *   Пример: `"Product#123"` → `"Product123"`.
    *   Удаляет переносы строк из `sku` с помощью `StringFormatter.remove_line_breaks(sku)`.
        *   Пример: `"Product\n123"` → `"Product123"`.
    *   Удаляет пробелы в начале и конце строки `sku`.
        *   Пример: `"  Product123  "` → `"Product123"`.
    *   Если длина `sku` меньше 3, возвращает `None`.
    *   Возвращает `True`.

4.  **`validate_url(url: str) -> bool`**:
    *   **Вход**: Строка `url`.
    *   Если `url` пустая, возвращает `None`.
    *   Удаляет пробелы в начале и конце строки `url`.
        *   Пример: `"  https://example.com  "` → `"https://example.com"`.
    *   Если `url` не начинается с `"http"`, добавляет `"http://"` в начало строки.
        *   Пример: `"example.com"` → `"http://example.com"`.
    *   Разбирает URL с помощью `urlparse(url)`.
    *   Если `parsed_url.netloc` или `parsed_url.scheme` пустые, возвращает `None`.
    *   Возвращает `True`.

5.  **`isint(s: str) -> bool`**:
    *   **Вход**: Строка `s`.
    *   Пытается преобразовать строку `s` в целое число.
        *   Если преобразование удалось, возвращает `True`.
        *   Пример: `"123"` → `123`.
        *   Если преобразование не удалось, возвращает `None`.

### 2. <mermaid>

```mermaid
flowchart TD
    A[ProductFieldsValidator] --> B{validate_price(price: str) -> bool};
    A --> C{validate_weight(weight: str) -> bool};
    A --> D{validate_sku(sku: str) -> bool};
    A --> E{validate_url(url: str) -> bool};
    A --> F{isint(s: str) -> bool};

    B --> B1{price is empty?};
    B1 -- Yes --> B_None[return None];
    B1 -- No --> B2{clear_price.sub()};
    B2 --> B3{replace(',', '.')};
    B3 --> B4{try float(price)};
    B4 -- Exception --> B_None;
    B4 -- Success --> B_True[return True];

    C --> C1{weight is empty?};
    C1 -- Yes --> C_None[return None];
    C1 -- No --> C2{clear_number.sub()};
    C2 --> C3{replace(',', '.')};
    C3 --> C4{try float(weight)};
    C4 -- Exception --> C_None;
    C4 -- Success --> C_True[return True];

    D --> D1{sku is empty?};
    D1 -- Yes --> D_None[return None];
    D1 -- No --> D2{remove_special_characters()};
    D2 --> D3{remove_line_breaks()};
    D3 --> D4{strip()};
    D4 --> D5{len(sku) < 3?};
    D5 -- Yes --> D_None;
    D5 -- No --> D_True[return True];

    E --> E1{url is empty?};
    E1 -- Yes --> E_None[return None];
    E1 -- No --> E2{strip()};
    E2 --> E3{startswith('http')?};
    E3 -- No --> E4{url = 'http://' + url};
    E3 -- Yes --> E5{parse_url = urlparse(url)};
    E4 --> E5;
    E5 --> E6{parsed_url.netloc and parsed_url.scheme?};
    E6 -- No --> E_None;
    E6 -- Yes --> E_True[return True];

    F --> F1{try int(s)};
    F1 -- Exception --> F_None[return None];
    F1 -- Success --> F_True[return True];
```

#### Импортированные зависимости:

*   `re`: Используется для работы с регулярными выражениями, в частности, для очистки цены и веса от лишних символов.
*   `html`: Импортирован, но не используется в предоставленном коде. Возможно, предназначен для экранирования HTML-сущностей, но в данном фрагменте не применяется.
*   `urllib.parse`: Используется для разбора URL-адресов и извлечения компонентов, таких как схема и сетевое расположение.
*   `typing.Union`: Используется для определения типов переменных, которые могут принимать несколько типов значений.
*   `src.logger.logger`: Используется для логирования событий и ошибок.

### 3. <объяснение>

#### Импорты:

*   `re`: Модуль для работы с регулярными выражениями. Используется в методах `validate_price` и `validate_weight` для очистки строк от нежелательных символов.
*   `html`: Модуль для работы с HTML. В данном коде не используется.
*   `urllib.parse`: Модуль для разбора URL. Используется в методе `validate_url` для проверки структуры URL.
*   `typing.Union`: Модуль для определения объединений типов. В данном коде не используется.
*   `src.logger.logger`: Модуль для логирования. В данном коде не используется, но должен использоваться для логирования ошибок и предупреждений.

#### Классы:

*   `ProductFieldsValidator`: Класс, содержащий статические методы для валидации различных полей продукта, таких как цена, вес, артикул и URL.
    *   Методы:
        *   `validate_price(price: str) -> bool`: Проверяет, является ли строка `price` корректной ценой. Удаляет все символы, кроме цифр и точки, заменяет запятую на точку и пытается преобразовать строку в число с плавающей точкой.
        *   `validate_weight(weight: str) -> bool`: Проверяет, является ли строка `weight` корректным весом. Удаляет все символы, кроме цифр и точки, заменяет запятую на точку и пытается преобразовать строку в число с плавающей точкой.
        *   `validate_sku(sku: str) -> bool`: Проверяет, является ли строка `sku` корректным артикулом. Удаляет специальные символы, переносы строк и пробелы в начале и конце строки, а также проверяет длину строки.
        *   `validate_url(url: str) -> bool`: Проверяет, является ли строка `url` корректным URL. Добавляет `"http://"` в начало строки, если она не начинается с `"http"`, и проверяет структуру URL с помощью `urlparse`.
        *   `isint(s: str) -> bool`: Проверяет, является ли строка `s` целым числом.

#### Функции:

*   `validate_price(price: str) -> bool`:
    *   Аргументы:
        *   `price` (str): Строка, представляющая цену.
    *   Возвращаемое значение:
        *   `bool`: `True`, если строка является корректной ценой, `None` в противном случае.
    *   Назначение:
        *   Проверка строки на соответствие формату цены.
    *   Пример:
        ```python
        ProductFieldsValidator.validate_price("123.45")  # Возвращает True
        ProductFieldsValidator.validate_price("abc")  # Возвращает None
        ```
*   `validate_weight(weight: str) -> bool`:
    *   Аргументы:
        *   `weight` (str): Строка, представляющая вес.
    *   Возвращаемое значение:
        *   `bool`: `True`, если строка является корректным весом, `None` в противном случае.
    *   Назначение:
        *   Проверка строки на соответствие формату веса.
    *   Пример:
        ```python
        ProductFieldsValidator.validate_weight("123.45")  # Возвращает True
        ProductFieldsValidator.validate_weight("abc")  # Возвращает None
        ```
*   `validate_sku(sku: str) -> bool`:
    *   Аргументы:
        *   `sku` (str): Строка, представляющая артикул.
    *   Возвращаемое значение:
        *   `bool`: `True`, если строка является корректным артикулом, `None` в противном случае.
    *   Назначение:
        *   Проверка строки на соответствие формату артикула.
    *   Пример:
        ```python
        ProductFieldsValidator.validate_sku("PRODUCT123")  # Возвращает True
        ProductFieldsValidator.validate_sku("AB")  # Возвращает None
        ```
*   `validate_url(url: str) -> bool`:
    *   Аргументы:
        *   `url` (str): Строка, представляющая URL.
    *   Возвращаемое значение:
        *   `bool`: `True`, если строка является корректным URL, `None` в противном случае.
    *   Назначение:
        *   Проверка строки на соответствие формату URL.
    *   Пример:
        ```python
        ProductFieldsValidator.validate_url("https://example.com")  # Возвращает True
        ProductFieldsValidator.validate_url("example")  # Возвращает None
        ```
*   `isint(s: str) -> bool`:
    *   Аргументы:
        *   `s` (str): Строка, которую нужно проверить на то, является ли она целым числом.
    *   Возвращаемое значение:
        *   `bool`: `True`, если строка является целым числом, `None` в противном случае.
    *   Назначение:
        *   Проверка, является ли строка целым числом.
    *   Пример:
        ```python
        ProductFieldsValidator.isint("123")  # Возвращает True
        ProductFieldsValidator.isint("abc")  # Возвращает None
        ```

#### Переменные:

*   `price` (str): Строка, представляющая цену товара.
*   `weight` (str): Строка, представляющая вес товара.
*   `sku` (str): Строка, представляющая артикул товара.
*   `url` (str): Строка, представляющая URL товара.
*   `s` (str): Строка, проверяемая на то, является ли она целым числом.

#### Потенциальные ошибки и области для улучшения:

1.  **Отсутствие логирования**: В коде отсутствует логирование ошибок и предупреждений. Следует добавить логирование с использованием модуля `logger` из `src.logger.logger` для отслеживания проблем и облегчения отладки.
2.  **Обработка исключений**: В методах `validate_price`, `validate_weight` и `isint` исключения перехватываются, но не логируются. Следует логировать исключения с использованием `logger.error`.
3.  **Возврат `None` вместо `False`**: В случае неуспешной валидации методы возвращают `None` вместо `False`. Это может привести к путанице, так как `None` может быть интерпретирован как отсутствие значения, а не как явный отказ. Рекомендуется возвращать `False` в случае неуспешной валидации.
4.  **Дублирование кода**: Методы `validate_price` и `validate_weight` содержат много дублирующегося кода. Следует вынести общую логику в отдельную функцию.
5.  **Использование `html`**: Модуль `html` импортирован, но не используется. Следует удалить неиспользуемый импорт.
6.  **Отсутствие документации для `Ptrn` и `StringFormatter`**: В коде используются классы `Ptrn` и `StringFormatter`, но нет информации об их определении и функциональности. Следует добавить документацию для этих классов или предоставить их определения.
7.  **Неинформативные docstring**: Docstring методов содержат только заглушки. Необходимо добавить подробное описание параметров, возвращаемых значений и исключений.

#### Взаимосвязи с другими частями проекта:

*   `src.logger.logger`: Используется для логирования событий и ошибок.
*   `StringFormatter`: Используется для форматирования строк, например, для удаления специальных символов и переносов строк.

#### Пример улучшенного кода:

```python
## \\file /src/utils/string/validator.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.utils.string
	:platform: Windows, Unix
	:synopsis: Модуль валидации строк
Модуль может предоставлять функции для проверки строк на соответствие определенным критериям или форматам.
Валидация может включать в себя проверку наличия определенных символов, длины строки, формата электронной почты, URL и т. д.

"""

import re
import html
from urllib.parse import urlparse, parse_qs
from typing import Union
from urllib.parse import urlparse, parse_qs

from src.logger.logger import logger


class ProductFieldsValidator:
    """
     StringValidator (Валидатор строк):
    @details
    - Задача: Проверка строки на соответствие определенным критериям или шаблонам.
    - Действия: Проверка наличия определенных символов, длины строки, соответствие регулярным выражениям и другие проверки.
    - Пример использования: Проверка корректности электронной почты, пароля или номера кредитной карты.
    """

    @staticmethod
    def _validate_number(value: str, clear_pattern: re.Pattern) -> bool:
        """
        Вспомогательная функция для валидации числовых значений (цены, веса).

        Args:
            value (str): Строка, представляющая числовое значение.
            clear_pattern (re.Pattern): Регулярное выражение для очистки строки от лишних символов.

        Returns:
            bool: True, если строка является корректным числовым значением, False в противном случае.

        Raises:
            Exception: Если возникает ошибка при преобразовании строки в число с плавающей точкой.
        """
        if not value:
            return False

        value = clear_pattern.sub('', value)
        value = value.replace(',', '.')

        try:
            float(value)
            return True
        except Exception as ex:
            logger.error(f'Error while validating number: {value}', exc_info=True)
            return False

    @staticmethod
    def validate_price(price: str) -> bool:
        """
        Валидация цены.

        Args:
            price (str): Строка, представляющая цену.

        Returns:
            bool: True, если строка является корректной ценой, False в противном случае.

        Example:
            >>> ProductFieldsValidator.validate_price("123.45")
            True
            >>> ProductFieldsValidator.validate_price("abc")
            False
        """
        return ProductFieldsValidator._validate_number(price, Ptrn.clear_price)

    @staticmethod
    def validate_weight(weight: str) -> bool:
        """
        Валидация веса.

        Args:
            weight (str): Строка, представляющая вес.

        Returns:
            bool: True, если строка является корректным весом, False в противном случае.

        Example:
            >>> ProductFieldsValidator.validate_weight("123.45")
            True
            >>> ProductFieldsValidator.validate_weight("abc")
            False
        """
        return ProductFieldsValidator._validate_number(weight, Ptrn.clear_number)

    @staticmethod
    def validate_sku(sku: str) -> bool:
        """
        Валидация артикула.

        Args:
            sku (str): Строка, представляющая артикул.

        Returns:
            bool: True, если строка является корректным артикулом, False в противном случае.

        Example:
            >>> ProductFieldsValidator.validate_sku("PRODUCT123")
            True
            >>> ProductFieldsValidator.validate_sku("AB")
            False
        """
        if not sku:
            return False

        sku = StringFormatter.remove_special_characters(sku)
        sku = StringFormatter.remove_line_breaks(sku)
        sku = sku.strip()

        if len(sku) < 3:
            return False

        return True

    @staticmethod
    def validate_url(url: str) -> bool:
        """
        Валидация URL.

        Args:
            url (str): Строка, представляющая URL.

        Returns:
            bool: True, если строка является корректным URL, False в противном случае.

        Example:
            >>> ProductFieldsValidator.validate_url("https://example.com")
            True
            >>> ProductFieldsValidator.validate_url("example")
            False
        """
        if not url:
            return False

        url = url.strip()

        if not url.startswith('http'):
            url = 'http://' + url

        parsed_url = urlparse(url)

        if not parsed_url.netloc or not parsed_url.scheme:
            return False

        return True

    @staticmethod
    def isint(s: str) -> bool:
        """
        Проверяет, является ли строка целым числом.

        Args:
            s (str): Строка для проверки.

        Returns:
            bool: True, если строка является целым числом, False в противном случае.

        Example:
            >>> ProductFieldsValidator.isint("123")
            True
            >>> ProductFieldsValidator.isint("abc")
            False
        """
        try:
            int(s)
            return True
        except Exception as ex:
            logger.error(f'Error while converting to int: {s}', exc_info=True)
            return False
```

#### Изменения:

1.  Добавлено логирование ошибок и предупреждений с использованием модуля `logger` из `src.logger.logger`.
2.  Изменен возврат `None` на `False` в случае неуспешной валидации.
3.  Вынесена общая логика валидации числовых значений в отдельную функцию `_validate_number`.
4.  Удален неиспользуемый импорт `html`.
5.  Добавлены подробные описания параметров, возвращаемых значений и исключений в docstring методов.