# Модуль валидации строк

## Обзор

Модуль `src.utils.string.validator` предназначен для валидации строк на соответствие определенным критериям и форматам. Он содержит класс `ProductFieldsValidator`, который предоставляет статические методы для проверки различных типов данных, таких как цены, вес, артикулы и URL. Модуль использует регулярные выражения и другие методы для обеспечения корректности данных.

## Подробней

Этот модуль играет важную роль в обеспечении качества данных, поступающих в систему. Он помогает предотвратить ошибки, связанные с некорректным форматом данных, и обеспечивает соответствие данных заданным требованиям. Валидация данных является важной частью любого приложения, так как позволяет убедиться, что данные, хранящиеся в базе данных или используемые в бизнес-логике, являются корректными и согласованными.

## Классы

### `ProductFieldsValidator`

**Описание**: Класс, предоставляющий статические методы для валидации различных полей продукта, таких как цена, вес, артикул и URL.

**Методы**:

- `validate_price`: Валидирует строку цены.
- `validate_weight`: Валидирует строку веса.
- `validate_sku`: Валидирует строку артикула.
- `validate_url`: Валидирует строку URL.
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

**Описание**: Валидирует строку, представляющую цену товара.

**Параметры**:

- `price` (str): Строка, содержащая цену товара.

**Возвращает**:

- `bool`: `True`, если строка является корректной ценой, иначе `False`.

**Примеры**:

```python
    >>> ProductFieldsValidator.validate_price('100.00')
    True
    >>> ProductFieldsValidator.validate_price('100,00')
    True
    >>> ProductFieldsValidator.validate_price('abc')
    False
```

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

**Описание**: Валидирует строку, представляющую вес товара.

**Параметры**:

- `weight` (str): Строка, содержащая вес товара.

**Возвращает**:

- `bool`: `True`, если строка является корректным весом, иначе `False`.

**Примеры**:

```python
    >>> ProductFieldsValidator.validate_weight('1.5')
    True
    >>> ProductFieldsValidator.validate_weight('1,5')
    True
    >>> ProductFieldsValidator.validate_weight('abc')
    False
```

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

**Описание**: Валидирует строку, представляющую артикул товара.

**Параметры**:

- `sku` (str): Строка, содержащая артикул товара.

**Возвращает**:

- `bool`: `True`, если строка является корректным артикулом, иначе `False`.

**Примеры**:

```python
    >>> ProductFieldsValidator.validate_sku('12345')
    True
    >>> ProductFieldsValidator.validate_sku('12')
    False
    >>> ProductFieldsValidator.validate_sku(None)
    False
```

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

**Описание**: Валидирует строку, представляющую URL.

**Параметры**:

- `url` (str): Строка, содержащая URL.

**Возвращает**:

- `bool`: `True`, если строка является корректным URL, иначе `False`.

**Примеры**:

```python
    >>> ProductFieldsValidator.validate_url('https://www.example.com')
    True
    >>> ProductFieldsValidator.validate_url('www.example.com')
    True
    >>> ProductFieldsValidator.validate_url('example')
    False
```

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

**Описание**: Проверяет, является ли строка целым числом.

**Параметры**:

- `s` (str): Строка для проверки.

**Возвращает**:

- `bool`: `True`, если строка является целым числом, иначе `False`.

**Примеры**:

```python
    >>> ProductFieldsValidator.isint('123')
    True
    >>> ProductFieldsValidator.isint('abc')
    False