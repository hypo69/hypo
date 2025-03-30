# Модуль `unicode`

## Обзор

Модуль `unicode` содержит функцию `decode_unicode_escape`, предназначенную для декодирования юникодных escape-последовательностей в строках, списках и словарях. Это полезно при работе с данными, которые могут содержать экранированные символы Unicode, и требуется представить их в читаемом формате.

## Подробней

Функция `decode_unicode_escape` рекурсивно обрабатывает входные данные, будь то словарь, список или строка. Если входные данные — строка, она пытается декодировать escape-последовательности Unicode. Если входные данные — словарь или список, функция рекурсивно применяется к каждому элементу. Это позволяет обрабатывать сложные структуры данных, содержащие escape-последовательности Unicode.

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
    ...
```

**Описание**: Декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

**Параметры**:
- `input_data` (Dict[str, Any] | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

**Возвращает**:
- `Dict[str, Any] | list | str`: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

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