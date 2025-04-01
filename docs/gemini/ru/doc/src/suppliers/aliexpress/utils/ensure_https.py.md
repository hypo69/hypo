# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для проверки и добавления префикса `https://` к строкам URL или идентификаторам продуктов AliExpress. Если передается идентификатор продукта, модуль формирует полную ссылку с использованием этого идентификатора.

## Подробней

Этот модуль важен для обеспечения безопасного доступа к ресурсам AliExpress. Он проверяет, начинается ли URL с `https://`, и добавляет этот префикс, если он отсутствует. Если передается идентификатор продукта, он формирует полную ссылку на продукт на AliExpress.
Код используется в проекте `hypotez` для <целей проекта hypotez: для стандартизации и обеспечения безопасности URL-адресов при работе с данными о товарах с AliExpress>.

## Функции

### `ensure_https`

```python
def ensure_https(prod_ids: str | list[str]) -> str | list[str]:
    """ Ensures that the provided URL string(s) contain the https:// prefix.
    If the input is a product ID, it constructs a full URL with https:// prefix.

    Args:
        prod_ids (str | list[str]): A URL string or a list of URL strings to check and modify if necessary.

    Returns:
        str | list[str]: The URL string or list of URL strings with the https:// prefix.

    Raises:
        ValueError: If `prod_ids` is an instance of `WindowsPath`.

    Examples:
        >>> ensure_https("example_product_id")
        'https://www.aliexpress.com/item/example_product_id.html'

        >>> ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
        ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

        >>> ensure_https("https://www.example.com/item/example_product_id")
        'https://www.example.com/item/example_product_id'
    """
```

**Назначение**:
Функция `ensure_https` проверяет, содержит ли предоставленная строка URL или список URL-ов префикс `https://`. Если входные данные являются идентификатором продукта, функция создает полный URL с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): URL-адрес в виде строки или список URL-адресов для проверки и изменения при необходимости.

**Возвращает**:
- `str | list[str]`: URL-адрес в виде строки или список URL-адресов с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

**Как работает функция**:
1. Функция `ensure_https` принимает на вход строку `prod_ids`, которая может быть как отдельным URL или ID продукта, так и списком таких строк.
2. Проверяется, является ли `prod_ids` списком.
3. Если `prod_ids` является списком, то функция применяет внутреннюю функцию `ensure_https_single` к каждому элементу списка и возвращает новый список с обработанными URL.
4. Если `prod_ids` не является списком (то есть строка), функция вызывает `ensure_https_single` для этой строки и возвращает результат.

Внутри функции происходят следующие действия и преобразования:

A. **Проверка типа входных данных**: Определяется, является ли входной параметр списком или строкой.
|
B. **Обработка списка URL**: Если входной параметр является списком, каждый URL в списке обрабатывается с помощью функции `ensure_https_single`.
|
C. **Обработка отдельного URL**: Если входной параметр является строкой, он непосредственно передается в функцию `ensure_https_single`.

**Внутренние функции**:

#### `ensure_https_single`

```python
    def ensure_https_single(prod_id: str) -> str:
        """ Ensures a single URL or product ID string has the https:// prefix.

        Args:
            prod_id (str): The URL or product ID string.

        Returns:
            str: The URL string with the https:// prefix.

        Raises:
            ValueError: If `prod_id` is an instance of `WindowsPath`.

        Examples:
            >>> ensure_https_single("example_product_id")
            'https://www.aliexpress.com/item/example_product_id.html'

            >>> ensure_https_single("https://www.example.com/item/example_product_id")
            'https://www.example.com/item/example_product_id'
        """
        ...
        _prod_id = extract_prod_ids(prod_id)
        if _prod_id:
            return f"https://www.aliexpress.com/item/{_prod_id}.html"
        else:
            logger.error(f"Invalid product ID or URL: {prod_id=}", exc_info=False)
            return prod_id
```

**Назначение**:
Функция `ensure_https_single` обеспечивает добавление префикса `https://` к одному URL-адресу или идентификатору продукта.

**Параметры**:
- `prod_id` (str): URL-адрес или идентификатор продукта в виде строки.

**Возвращает**:
- `str`: URL-адрес с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Как работает функция**:

1. Функция `ensure_https_single` принимает на вход строку `prod_id`, которая может быть URL-ом или ID продукта.
2. Извлекает ID продукта из входной строки с помощью функции `extract_prod_ids`.
3. Если `_prod_id` не пустой, функция возвращает URL с префиксом `https://` и извлеченным ID продукта.
4. В противном случае, если `_prod_id` пустой, функция логирует ошибку и возвращает исходный `prod_id` без изменений.

Внутри функции происходят следующие действия и преобразования:

A. **Извлечение ID продукта**: Используется функция `extract_prod_ids` для извлечения ID продукта из входной строки.
|
B. **Проверка ID продукта**: Проверяется, был ли успешно извлечен ID продукта.
|
C. **Формирование URL**: Если ID продукта был успешно извлечен, формируется URL с использованием префикса `https://` и ID продукта.
|
D. **Обработка ошибки**: Если ID продукта не был извлечен, логируется ошибка и возвращается исходная строка.

**Примеры**:

- Пример 1: Проверка и добавление `https://` к идентификатору продукта.

```python
result = ensure_https("1234567890")
print(result)  # Вывод: https://www.aliexpress.com/item/1234567890.html
```

- Пример 2: Проверка URL-адреса с уже имеющимся `https://`.

```python
result = ensure_https("https://www.aliexpress.com/item/1234567890.html")
print(result)  # Вывод: https://www.aliexpress.com/item/1234567890.html
```

- Пример 3: Проверка списка URL-адресов и идентификаторов продуктов.

```python
result = ensure_https(["1234567890", "https://www.example.com/item/1234567890.html"])
print(result)  # Вывод: ['https://www.aliexpress.com/item/1234567890.html', 'https://www.example.com/item/1234567890.html']
```