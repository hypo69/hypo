# Модуль валидации строк

## Обзор

Модуль `src.utils.string.validator` предоставляет инструменты для валидации строк на соответствие различным критериям и форматам. Он содержит класс `ProductFieldsValidator` с набором статических методов для проверки цен, веса, артикулов и URL.

## Подробней

Этот модуль предназначен для проверки корректности и соответствия строк заданным требованиям. Он может быть использован для валидации данных, вводимых пользователем, или данных, получаемых из внешних источников. Расположение файла в проекте `hypotez` указывает на то, что он является частью утилит для работы со строками.

## Классы

### `ProductFieldsValidator`

**Описание**: Класс, содержащий статические методы для валидации различных полей продукта, таких как цена, вес, артикул и URL.

**Как работает класс**:
Класс предоставляет набор статических методов, каждый из которых выполняет определенную проверку строки на соответствие заданным критериям. Например, метод `validate_price` проверяет, является ли строка корректной ценой, `validate_weight` проверяет вес, `validate_sku` проверяет артикул, а `validate_url` проверяет, является ли строка корректным URL.

**Методы**:
- `validate_price`: Валидирует строку, представляющую цену.
- `validate_weight`: Валидирует строку, представляющую вес.
- `validate_sku`: Валидирует строку, представляющую артикул.
- `validate_url`: Валидирует строку, представляющую URL.
- `isint`: Проверяет, является ли строка целым числом.

## Функции

### `validate_price`

```python
@staticmethod
def validate_price(price: str) -> bool:
    """
     [Function's description]

    Parameters : 
        @param price : str  :  [description]
    Returns : 
        @return bool  :  [description]

    """
    """
    Валидация цены
    """
    if not price:
        return
    price = Ptrn.clear_price.sub('', price)
    price = price.replace(',', '.')
    try:
        float(price)
    except:
        return
    return True
```

**Описание**: Проверяет, является ли предоставленная строка допустимой ценой.

**Как работает функция**:
1. Если строка `price` пуста, функция возвращает `None`.
2. Удаляет все символы, не являющиеся цифрами или точкой, из строки `price`.
3. Заменяет все запятые на точки в строке `price`.
4. Пытается преобразовать строку `price` в число с плавающей точкой. Если преобразование успешно, функция возвращает `True`, иначе - `None`.

**Параметры**:
- `price` (str): Строка, представляющая цену.

**Возвращает**:
- `bool`: `True`, если строка является допустимой ценой, иначе `None`.

### `validate_weight`

```python
@staticmethod
def validate_weight(weight: str) -> bool:
    """
     [Function's description]

    Parameters : 
        @param weight : str  :  [description]
    Returns : 
        @return bool  :  [description]

    """
    """
    Валидация веса
    """
    if not weight:
        return
    weight = Ptrn.clear_number.sub('', weight)
    weight = weight.replace(',', '.')
    try:
        float(weight)
    except:
        return
    return True
```

**Описание**: Проверяет, является ли предоставленная строка допустимым весом.

**Как работает функция**:
1. Если строка `weight` пуста, функция возвращает `None`.
2. Удаляет все символы, не являющиеся цифрами или точкой, из строки `weight`.
3. Заменяет все запятые на точки в строке `weight`.
4. Пытается преобразовать строку `weight` в число с плавающей точкой. Если преобразование успешно, функция возвращает `True`, иначе - `None`.

**Параметры**:
- `weight` (str): Строка, представляющая вес.

**Возвращает**:
- `bool`: `True`, если строка является допустимым весом, иначе `None`.

### `validate_sku`

```python
@staticmethod
def validate_sku(sku: str) -> bool:
    """
     [Function's description]

    Parameters : 
        @param sku : str  :  [description]
    Returns : 
        @return bool  :  [description]

    """
    """
    Валидация артикула
    """
    if not sku:
        return
    sku = StringFormatter.remove_special_characters(sku)
    sku = StringFormatter.remove_line_breaks(sku)
    sku = sku.strip()
    if len(sku) < 3:
        return
    return True
```

**Описание**: Проверяет, является ли предоставленная строка допустимым артикулом (SKU).

**Как работает функция**:
1. Если строка `sku` пуста, функция возвращает `None`.
2. Удаляет специальные символы из строки `sku` с помощью `StringFormatter.remove_special_characters`.
3. Удаляет переносы строк из строки `sku` с помощью `StringFormatter.remove_line_breaks`.
4. Удаляет начальные и конечные пробелы из строки `sku`.
5. Если длина строки `sku` меньше 3, функция возвращает `None`.
6. Возвращает `True`, если все проверки пройдены.

**Параметры**:
- `sku` (str): Строка, представляющая артикул.

**Возвращает**:
- `bool`: `True`, если строка является допустимым артикулом, иначе `None`.

### `validate_url`

```python
@staticmethod
def validate_url(url: str) -> bool:
    """
     [Function's description]

    Parameters : 
        @param url : str  :  [description]
    Returns : 
        @return bool  :  [description]

    """
    """
    Валидация URL
    """
    if not url:
        return

    url = url.strip()

    if not url.startswith('http'):
        url = 'http://' + url

    parsed_url = urlparse(url)

    if not parsed_url.netloc or not parsed_url.scheme:
        return

    return True
```

**Описание**: Проверяет, является ли предоставленная строка допустимым URL.

**Как работает функция**:
1. Если строка `url` пуста, функция возвращает `None`.
2. Удаляет начальные и конечные пробелы из строки `url`.
3. Если строка `url` не начинается с "http", добавляет "http://" в начало строки.
4. Пытается разобрать строку `url` с помощью `urllib.parse.urlparse`.
5. Если у разобранного URL отсутствуют сетевое расположение (`netloc`) или схема (`scheme`), функция возвращает `None`.
6. Возвращает `True`, если все проверки пройдены.

**Параметры**:
- `url` (str): Строка, представляющая URL.

**Возвращает**:
- `bool`: `True`, если строка является допустимым URL, иначе `None`.

### `isint`

```python
@staticmethod
def isint(s: str) -> bool:
    """
     [Function's description]

    Parameters : 
        @param s : str  :  [description]
    Returns : 
        @return bool  :  [description]

    """
    try:
        s = int(s)
        return True
    except Exception as ex:
        return
```

**Описание**: Проверяет, является ли предоставленная строка целым числом.

**Как работает функция**:
1. Пытается преобразовать строку `s` в целое число.
2. Если преобразование успешно, функция возвращает `True`.
3. Если возникает исключение, функция возвращает `None`.

**Параметры**:
- `s` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True`, если строка является целым числом, иначе `None`.