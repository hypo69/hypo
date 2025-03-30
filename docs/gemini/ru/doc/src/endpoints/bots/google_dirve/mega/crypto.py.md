# Модуль crypto

## Обзор

Модуль `crypto.py` содержит функции для шифрования и дешифрования данных, используемые в контексте работы с Mega.co.nz. Он включает в себя реализацию AES-CBC шифрования, хеширования строк, подготовки ключей и обработки атрибутов.

## Подробней

Этот модуль предоставляет криптографические функции, необходимые для обеспечения безопасности при работе с Mega. Он использует библиотеку `Crypto` для выполнения операций AES. Модуль включает функции для шифрования и дешифрования данных с использованием AES в режиме CBC, а также функции для подготовки и обработки ключей.

## Функции

### `aes_cbc_encrypt`

```python
def aes_cbc_encrypt(data: bytes, key: bytes) -> bytes:
    """
    Args:
        data (bytes): Данные для шифрования.
        key (bytes): Ключ шифрования.

    Returns:
        bytes: Зашифрованные данные.

    Raises:
        ValueError: Если длина данных не кратна размеру блока.
    """
```

**Описание**: Шифрует данные с использованием алгоритма AES в режиме CBC.

**Параметры**:
- `data` (bytes): Данные, которые необходимо зашифровать.
- `key` (bytes): Ключ, используемый для шифрования данных.

**Возвращает**:
- `bytes`: Зашифрованные данные.

**Примеры**:
```python
key = b'\\0' * 16
data = b'Test data'
encrypted_data = aes_cbc_encrypt(data, key)
print(encrypted_data)
```

### `aes_cbc_decrypt`

```python
def aes_cbc_decrypt(data: bytes, key: bytes) -> bytes:
    """
    Args:
        data (bytes): Данные для дешифрования.
        key (bytes): Ключ дешифрования.

    Returns:
        bytes: Дешифрованные данные.

    Raises:
        ValueError: Если длина данных не кратна размеру блока.
    """
```

**Описание**: Дешифрует данные, зашифрованные алгоритмом AES в режиме CBC.

**Параметры**:
- `data` (bytes): Зашифрованные данные.
- `key` (bytes): Ключ, используемый для дешифрования данных.

**Возвращает**:
- `bytes`: Дешифрованные данные.

**Примеры**:
```python
key = b'\\0' * 16
data = b'Test data'
encrypted_data = aes_cbc_encrypt(data, key)
decrypted_data = aes_cbc_decrypt(encrypted_data, key)
print(decrypted_data)
```

### `aes_cbc_encrypt_a32`

```python
def aes_cbc_encrypt_a32(data: list[int], key: list[int]) -> list[int]:
    """
    Args:
        data (list[int]): Данные для шифрования в формате списка 32-битных целых чисел.
        key (list[int]): Ключ шифрования в формате списка 32-битных целых чисел.

    Returns:
        list[int]: Зашифрованные данные в формате списка 32-битных целых чисел.
    """
```

**Описание**: Шифрует данные (представленные в виде списка 32-битных целых чисел) с использованием AES в режиме CBC.

**Параметры**:
- `data` (list[int]): Список 32-битных целых чисел, представляющих данные для шифрования.
- `key` (list[int]): Список 32-битных целых чисел, представляющих ключ шифрования.

**Возвращает**:
- `list[int]`: Зашифрованные данные в виде списка 32-битных целых чисел.

**Примеры**:
```python
data = [1, 2, 3, 4]
key = [5, 6, 7, 8]
encrypted_data = aes_cbc_encrypt_a32(data, key)
print(encrypted_data)
```

### `aes_cbc_decrypt_a32`

```python
def aes_cbc_decrypt_a32(data: list[int], key: list[int]) -> list[int]:
    """
    Args:
        data (list[int]): Данные для дешифрования в формате списка 32-битных целых чисел.
        key (list[int]): Ключ дешифрования в формате списка 32-битных целых чисел.

    Returns:
        list[int]: Дешифрованные данные в формате списка 32-битных целых чисел.
    """
```

**Описание**: Дешифрует данные (представленные в виде списка 32-битных целых чисел), зашифрованные алгоритмом AES в режиме CBC.

**Параметры**:
- `data` (list[int]): Список 32-битных целых чисел, представляющих зашифрованные данные.
- `key` (list[int]): Список 32-битных целых чисел, представляющих ключ дешифрования.

**Возвращает**:
- `list[int]`: Дешифрованные данные в виде списка 32-битных целых чисел.

**Примеры**:
```python
data = [1, 2, 3, 4]
key = [5, 6, 7, 8]
encrypted_data = aes_cbc_encrypt_a32(data, key)
decrypted_data = aes_cbc_decrypt_a32(encrypted_data, key)
print(decrypted_data)
```

### `stringhash`

```python
def stringhash(s: str, aeskey: list[int]) -> str:
    """
    Args:
        s (str): Строка для хеширования.
        aeskey (list[int]): Ключ AES в формате списка 32-битных целых чисел.

    Returns:
        str: Хеш строки в формате Base64.
    """
```

**Описание**: Вычисляет хеш строки, используя AES-CBC для перемешивания.

**Параметры**:
- `s` (str): Строка, которую необходимо хешировать.
- `aeskey` (list[int]): Ключ AES, используемый в процессе хеширования.

**Возвращает**:
- `str`: Хеш строки, закодированный в формате Base64.

**Примеры**:
```python
s = 'example_string'
aeskey = [1, 2, 3, 4]
hashed_string = stringhash(s, aeskey)
print(hashed_string)
```

### `prepare_key`

```python
def prepare_key(a: list[int]) -> list[int]:
    """
    Args:
        a (list[int]): Список 32-битных целых чисел для подготовки ключа.

    Returns:
        list[int]: Подготовленный ключ в формате списка 32-битных целых чисел.
    """
```

**Описание**: Подготавливает ключ для шифрования путем многократного применения AES-CBC.

**Параметры**:
- `a` (list[int]): Список 32-битных целых чисел, используемый для подготовки ключа.

**Возвращает**:
- `list[int]`: Подготовленный ключ в формате списка 32-битных целых чисел.

**Примеры**:
```python
a = [1, 2, 3, 4, 5, 6, 7, 8]
prepared_key = prepare_key(a)
print(prepared_key)
```

### `encrypt_key`

```python
def encrypt_key(a: list[int], key: list[int]) -> list[int]:
    """
    Args:
        a (list[int]): Ключ для шифрования в формате списка 32-битных целых чисел.
        key (list[int]): Ключ шифрования в формате списка 32-битных целых чисел.

    Returns:
        list[int]: Зашифрованный ключ в формате списка 32-битных целых чисел.
    """
```

**Описание**: Шифрует ключ, используя AES-CBC.

**Параметры**:
- `a` (list[int]): Ключ, который необходимо зашифровать.
- `key` (list[int]): Ключ шифрования.

**Возвращает**:
- `list[int]`: Зашифрованный ключ.

**Примеры**:
```python
a = [1, 2, 3, 4, 5, 6, 7, 8]
key = [9, 10, 11, 12]
encrypted_key = encrypt_key(a, key)
print(encrypted_key)
```

### `decrypt_key`

```python
def decrypt_key(a: list[int], key: list[int]) -> list[int]:
    """
    Args:
        a (list[int]): Ключ для дешифрования в формате списка 32-битных целых чисел.
        key (list[int]): Ключ дешифрования в формате списка 32-битных целых чисел.

    Returns:
        list[int]: Дешифрованный ключ в формате списка 32-битных целых чисел.
    """
```

**Описание**: Дешифрует ключ, зашифрованный с использованием AES-CBC.

**Параметры**:
- `a` (list[int]): Зашифрованный ключ.
- `key` (list[int]): Ключ дешифрования.

**Возвращает**:
- `list[int]`: Дешифрованный ключ.

**Примеры**:
```python
a = [1, 2, 3, 4, 5, 6, 7, 8]
key = [9, 10, 11, 12]
encrypted_key = encrypt_key(a, key)
decrypted_key = decrypt_key(encrypted_key, key)
print(decrypted_key)
```

### `enc_attr`

```python
def enc_attr(attr: dict, key: list[int]) -> bytes:
    """
    Args:
        attr (dict): Атрибуты для шифрования в виде словаря.
        key (list[int]): Ключ шифрования в формате списка 32-битных целых чисел.

    Returns:
        bytes: Зашифрованные атрибуты.
    """
```

**Описание**: Шифрует атрибуты, представленные в виде словаря, используя AES-CBC.

**Параметры**:
- `attr` (dict): Словарь атрибутов для шифрования.
- `key` (list[int]): Ключ шифрования.

**Возвращает**:
- `bytes`: Зашифрованные атрибуты.

**Примеры**:
```python
attr = {'name': 'example', 'size': 1024}
key = [1, 2, 3, 4]
encrypted_attr = enc_attr(attr, key)
print(encrypted_attr)
```

### `dec_attr`

```python
def dec_attr(attr: bytes, key: list[int]) -> dict:
    """
    Args:
        attr (bytes): Зашифрованные атрибуты.
        key (list[int]): Ключ дешифрования в формате списка 32-битных целых чисел.

    Returns:
        dict: Дешифрованные атрибуты в виде словаря.
    """
```

**Описание**: Дешифрует атрибуты, зашифрованные с использованием AES-CBC.

**Параметры**:
- `attr` (bytes): Зашифрованные атрибуты.
- `key` (list[int]): Ключ дешифрования.

**Возвращает**:
- `dict`: Дешифрованные атрибуты в виде словаря.

**Примеры**:
```python
attr = {'name': 'example', 'size': 1024}
key = [1, 2, 3, 4]
encrypted_attr = enc_attr(attr, key)
decrypted_attr = dec_attr(encrypted_attr, key)
print(decrypted_attr)