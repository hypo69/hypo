# Модуль для шифрования и дешифрования данных

## Обзор

Модуль предоставляет функции для шифрования и дешифрования данных с использованием алгоритма AES. Он включает в себя функции для добавления отступов к данным, шифрования, удаления отступов и дешифрования.

## Подробней

Этот модуль предназначен для обеспечения безопасности данных путем их шифрования. Он использует алгоритм AES в режиме CBC с ключом, полученным из пароля и соли. Функции `encrypt` и `decrypt` позволяют шифровать и дешифровать данные, а функции `pad` и `unpad` обеспечивают правильную обработку отступов.

## Функции

### `pad`

```python
def pad(data: str) -> bytes:
    """
    Дополняет строку данных до кратного 16 байтам, добавляя байты отступа.

    Args:
        data (str): Строка для дополнения.

    Returns:
        bytes: Дополненная строка в байтах.

    Как работает функция:
    1. Преобразует входную строку в байты.
    2. Вычисляет количество байтов, необходимых для дополнения, чтобы длина данных стала кратной 16.
    3. Добавляет байты отступа, каждый из которых имеет значение, равное количеству добавленных байтов.

    ```
    Строка -> Преобразование в байты -> Вычисление отступа -> Добавление отступа
    ```

    Примеры:
        >>> pad("example")
        b'example\\t\\t\\t\\t\\t\\t\\t\\t\\t'

        >>> pad("example12345678")
        b'example12345678\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08'
    """
    ...
```

### `encrypt`

```python
def encrypt(data: str, key: str) -> str:
    """
    Шифрует данные с использованием алгоритма AES.

    Args:
        data (str): Данные для шифрования.
        key (str): Ключ шифрования.

    Returns:
        str: JSON-строка, содержащая зашифрованные данные, вектор инициализации (IV) и соль.

    Как работает функция:

    1. Генерирует случайную соль длиной 8 символов.
    2. Создает ключ шифрования и вектор инициализации (IV) на основе ключа и соли путем повторного хеширования с использованием MD5.
    3. Дополняет данные с помощью функции `pad`.
    4. Шифрует дополненные данные с использованием AES в режиме CBC.
    5. Формирует JSON-строку, содержащую зашифрованные данные в base64, IV и соль.

    ```
    Входные данные -> Генерация соли -> Формирование ключа и IV -> Дополнение данных -> Шифрование AES -> Формирование JSON
    ```

    Примеры:
        >>> encrypt("example", "secret")
        '{"ct": "...", "iv": "...", "s": "..."}'

    """
    ...
```

### `unpad`

```python
def unpad(data: bytes) -> bytes:
    """
    Удаляет отступы из байтовой строки данных.

    Args:
        data (bytes): Данные с отступами.

    Returns:
        bytes: Данные без отступов.

    Как работает функция:
    1. Извлекает значение отступа из последнего байта данных.
    2. Удаляет байты отступа на основе полученного значения.

    ```
    Данные с отступами -> Извлечение значения отступа -> Удаление отступа -> Данные без отступов
    ```

    Примеры:
        >>> unpad(b'example\\t\\t\\t\\t\\t\\t\\t\\t\\t')
        b'example'

        >>> unpad(b'example12345678\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08')
        b'example12345678'
    """
    ...
```

### `decrypt`

```python
def decrypt(data: str, key: str) -> str:
    """
    Дешифрует данные с использованием алгоритма AES.

    Args:
        data (str): JSON-строка, содержащая зашифрованные данные, вектор инициализации (IV) и соль.
        key (str): Ключ шифрования.

    Returns:
        str: Дешифрованные данные.

    Как работает функция:
    1. Декодирует JSON-строку, чтобы извлечь зашифрованные данные, IV и соль.
    2. Создает ключ шифрования и IV на основе ключа и соли путем повторного хеширования с использованием MD5.
    3. Дешифрует данные с использованием AES в режиме CBC.
    4. Удаляет отступы с помощью функции `unpad`.

    ```
    JSON -> Декодирование -> Формирование ключа и IV -> Дешифрование AES -> Удаление отступа -> Дешифрованные данные
    ```

    Примеры:
        >>> encrypted_data = encrypt("example", "secret")
        >>> decrypt(encrypted_data, "secret")
        'example'
    """
    ...