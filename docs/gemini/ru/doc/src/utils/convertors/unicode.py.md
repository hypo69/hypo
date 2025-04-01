# Модуль `unicode.py`

## Обзор

Модуль предоставляет функцию `decode_unicode_escape`, которая декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

## Подробней

Этот модуль полезен для обработки данных, полученных из источников, где юникодные символы представлены в виде escape-последовательностей (например, `\u05de`). Функция рекурсивно обрабатывает словари и списки, что позволяет применять её к сложным структурам данных. В случае, если входные данные не являются строкой, списком или словарём, функция возвращает их без изменений.

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

    if isinstance(input_data, dict):
        # Рекурсивная обработка значений словаря
        return {key: decode_unicode_escape(value) for key, value in input_data.items()}
    
    elif isinstance(input_data, list):
        # Рекурсивная обработка элементов списка
        return [decode_unicode_escape(item) for item in input_data]
    
    elif isinstance(input_data, str):
        # Функция декодирует строку, если она содержит escape-последовательности
        try:
            # Шаг 1: Декодирование строки с escape-последовательностями
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError:
            decoded_string = input_data
        
        # Шаг 2: Преобразование всех найденных последовательностей \\uXXXX
        unicode_escape_pattern = r'\\\\u[0-9a-fA-F]{4}'
        decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        
        return decoded_string
    
    else:
        # Если тип данных не поддерживается, функция вернет данные без изменений
        return input_data
```

**Назначение**: Декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности.

**Параметры**:
- `input_data` (Dict[str, Any] | list | str): Входные данные, которые могут быть словарём, списком или строкой.

**Возвращает**:
- `Dict[str, Any] | list | str`: Преобразованные данные, где escape-последовательности декодированы.

**Как работает функция**:

1.  **Определение типа входных данных**:
    *   Функция проверяет, является ли входной параметр словарем, списком или строкой.

2.  **Обработка словаря**:
    *   Если `input_data` - словарь, функция рекурсивно вызывает саму себя для каждого значения в словаре и возвращает новый словарь с декодированными значениями.

3.  **Обработка списка**:
    *   Если `input_data` - список, функция рекурсивно вызывает саму себя для каждого элемента в списке и возвращает новый список с декодированными элементами.

4.  **Обработка строки**:
    *   Если `input_data` - строка, функция пытается декодировать escape-последовательности в строке.

    *   Если происходит ошибка `UnicodeDecodeError`, строка возвращается без изменений.

    *   **Дополнительное преобразование**:

        *   Производится поиск всех последовательностей вида `\\\\uXXXX` (где XXXX - шестнадцатеричное число) и их преобразование.

5.  **Обработка других типов данных**:
    *   Если `input_data` не является словарём, списком или строкой, функция возвращает входные данные без изменений.

**Внутренние функции**: Нет

**ASCII flowchart**:

```
    Начало
    │
    ├───> input_data - словарь? 
    │     └───> Да: Рекурсивно обработать значения словаря
    │     └───> Нет:
    │
    ├───> input_data - список?
    │     └───> Да: Рекурсивно обработать элементы списка
    │     └───> Нет:
    │
    ├───> input_data - строка?
    │     └───> Да: Попытка декодирования escape-последовательностей
    │          │
    │          ├───> Успешно: Декодирование строки
    │          │
    │          └───> Ошибка UnicodeDecodeError: Вернуть строку без изменений
    │          │
    │          └───> Поиск и преобразование последовательностей \\uXXXX
    │
    └───> Вернуть input_data без изменений (если не словарь, не список и не строка)
    │
    Конец
```

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