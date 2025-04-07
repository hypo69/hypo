# Модуль для декодирования Unicode escape-последовательностей
=========================================================

Модуль содержит функцию `decode_unicode_escape`, которая используется для преобразования Unicode escape-последовательностей в читаемый текст.

Пример использования
----------------------

```python
input_dict = {
    'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
    'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
    'price': 123.45
}

input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']

input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'

# Применяем функцию
decoded_dict = decode_unicode_escape(input_dict)
decoded_list = decode_unicode_escape(input_list)
decoded_string = decode_unicode_escape(input_string)

print(decoded_dict)
print(decoded_list)
print(decoded_string)
```

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Функции](#функции)
    - [decode_unicode_escape](#decode_unicode_escape)

## Обзор

Модуль предоставляет функцию `decode_unicode_escape`, которая декодирует строки, списки или словари, содержащие Unicode escape-последовательности, в читаемый формат. Это полезно при работе с данными, полученными из источников, где Unicode символы представлены в виде escape-последовательностей (например, `\uXXXX`).

## Подробнее

Этот модуль предназначен для обработки данных, которые могут содержать Unicode символы, представленные в виде escape-последовательностей. Функция `decode_unicode_escape` рекурсивно обрабатывает словари и списки, применяя декодирование к строковым значениям. Это гарантирует, что все строковые данные будут представлены в читаемом виде.

## Функции

### `decode_unicode_escape`

```python
def decode_unicode_escape(input_data: Dict[str, Any] | list | str) -> Dict[str, Any] | list | str:
    """Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

    Args:
        input_data (dict | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

    Returns:
        dict | list | str: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

    Пример использования:
    .. code-block:: python
        input_dict = {
            'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
            'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
            'price': 123.45
        }

        input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']

        input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'

        # Применяем функцию
        decoded_dict = decode_unicode_escape(input_dict)
        decoded_list = decode_unicode_escape(input_list)
        decoded_string = decode_unicode_escape(input_string)

        print(decoded_dict)
        print(decoded_list)
        print(decoded_string)

    """
```

**Назначение**: Декодирование Unicode escape-последовательностей в строках, списках или словарях.

**Параметры**:

- `input_data` (Dict[str, Any] | list | str): Входные данные, которые могут быть словарем, списком или строкой, содержащей Unicode escape-последовательности.

**Возвращает**:

- Dict[str, Any] | list | str: Преобразованные данные. Если входные данные - строка, возвращается декодированная строка. Если входные данные - словарь или список, возвращается словарь или список с рекурсивно обработанными значениями.

**Как работает функция**:

1. **Определение типа входных данных**:
   - Функция проверяет, является ли входной параметр словарем, списком или строкой.

2. **Обработка словаря**:
   - Если входные данные - словарь, функция рекурсивно вызывает себя для каждого значения в словаре и создает новый словарь с декодированными значениями.

3. **Обработка списка**:
   - Если входные данные - список, функция рекурсивно вызывает себя для каждого элемента в списке и создает новый список с декодированными элементами.

4. **Обработка строки**:
   - Если входные данные - строка, функция пытается декодировать escape-последовательности. Сначала строка кодируется в UTF-8, а затем декодируется с использованием `unicode_escape`.

5. **Дополнительная обработка Unicode escape-последовательностей**:
   - Функция ищет все последовательности вида `\\\\uXXXX` (где `XXXX` - шестнадцатеричное число) и преобразует их в соответствующие Unicode символы.

6. **Возврат результата**:
   - Если входные данные не являются словарем, списком или строкой, функция возвращает входные данные без изменений.

**Внутренние функции**:
- Внутри данной функции нет внутренних функций.

**Примеры**:

```python
input_dict = {
    'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
    'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
    'price': 123.45
}

input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']

input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'

# Применяем функцию
decoded_dict = decode_unicode_escape(input_dict)
decoded_list = decode_unicode_escape(input_list)
decoded_string = decode_unicode_escape(input_string)

print(decoded_dict)
print(decoded_list)
print(decoded_string)
```

**ASCII flowchart**:

```
A [Входные данные: input_data]
|
B [Определение типа данных: словарь, список, строка]
|
C [Если словарь: рекурсивная обработка значений]
|
D [Если список: рекурсивная обработка элементов]
|
E [Если строка: декодирование escape-последовательностей]
|
F [Дополнительная обработка Unicode escape-последовательностей]
|
G [Возврат преобразованных данных]
```

**Примеры**:

1. Декодирование словаря:

```python
input_dict = {'name': r'\\u0410\\u043d\\u0434\\u0440\\u0435\\u0439'}
decoded_dict = decode_unicode_escape(input_dict)
print(decoded_dict)  # Вывод: {'name': 'Андрей'}
```

2. Декодирование списка:

```python
input_list = [r'\\u0412\\u0430\\u0441\\u0438\\u043b\\u0438\\u0439', r'\\u041f\\u0435\\u0442\\u0440']
decoded_list = decode_unicode_escape(input_list)
print(decoded_list)  # Вывод: ['Василий', 'Петр']
```

3. Декодирование строки:

```python
input_string = r'\\u041c\\u0438\\u0445\\u0430\\u0438\\u043b'
decoded_string = decode_unicode_escape(input_string)
print(decoded_string)  # Вывод: Михаил
```