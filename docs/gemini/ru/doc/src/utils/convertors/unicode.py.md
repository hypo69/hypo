# Модуль `unicode`

## Обзор

Модуль `unicode` предназначен для декодирования строк, списков или словарей, содержащих юникодные escape-последовательности. Он предоставляет функцию `decode_unicode_escape`, которая рекурсивно обрабатывает входные данные и преобразует escape-последовательности в читаемый текст.

## Подробней

Этот модуль полезен, когда необходимо преобразовать данные, полученные из внешних источников (например, из JSON-файлов или API), в которых юникодные символы представлены в виде escape-последовательностей (например, `\u05de`). Функция `decode_unicode_escape` обеспечивает корректное отображение таких символов, что позволяет использовать данные в удобочитаемом формате.

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
            'product_name': r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
            'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
            'price': 123.45
        }

        input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

        input_string = r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

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

**Назначение**: Декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

**Как работает функция**:
1.  Функция проверяет тип входных данных: словарь, список или строка.
2.  Если входные данные - словарь, функция рекурсивно вызывает саму себя для каждого значения в словаре и возвращает новый словарь с декодированными значениями.
3.  Если входные данные - список, функция рекурсивно вызывает саму себя для каждого элемента в списке и возвращает новый список с декодированными элементами.
4.  Если входные данные - строка, функция пытается декодировать строку, используя метод `encode('utf-8').decode('unicode_escape')`. Если происходит ошибка `UnicodeDecodeError`, строка возвращается без изменений.
5.  Затем функция ищет все последовательности `\\uXXXX` (где `XXXX` - шестнадцатеричное число) и преобразует их в соответствующие юникодные символы.
6.  Если входные данные имеют другой тип, функция возвращает их без изменений.

**Параметры**:

*   `input_data` (Dict[str, Any] | list | str): Входные данные, которые могут быть словарем, списком или строкой, содержащими юникодные escape-последовательности.

**Возвращает**:

*   Dict[str, Any] | list | str: Преобразованные данные, где юникодные escape-последовательности заменены на соответствующие символы.

**Примеры**:

```python
input_dict = {
    'product_name': r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
    'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
    'price': 123.45
}

input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

input_string = r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

# Применяем функцию
decoded_dict = decode_unicode_escape(input_dict)
decoded_list = decode_unicode_escape(input_list)
decoded_string = decode_unicode_escape(input_string)

print(decoded_dict)
print(decoded_list)
print(decoded_string)
```