# Модуль для декодирования Unicode escape-последовательностей

## Обзор

Модуль предназначен для преобразования строк, списков или словарей, содержащих Unicode escape-последовательности, в читаемый формат. Он рекурсивно обрабатывает структуры данных, обеспечивая корректное отображение текста.

## Подробней

Этот модуль предоставляет функцию `decode_unicode_escape`, которая позволяет декодировать Unicode escape-последовательности в строках, списках и словарях. Это особенно полезно при работе с данными, полученными из источников, где Unicode символы представлены в виде `\\uXXXX`.

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

**Как работает функция**:
Функция `decode_unicode_escape` принимает словарь, список или строку в качестве входных данных и рекурсивно декодирует все Unicode escape-последовательности (`\uXXXX`) в этих данных.

1.  **Обработка словаря**: Если входные данные - словарь, функция создает новый словарь, в котором каждое значение рекурсивно обрабатывается функцией `decode_unicode_escape`.
2.  **Обработка списка**: Если входные данные - список, функция создает новый список, в котором каждый элемент рекурсивно обрабатывается функцией `decode_unicode_escape`.
3.  **Обработка строки**: Если входные данные - строка, функция пытается декодировать escape-последовательности в строке. Сначала строка кодируется в `utf-8`, а затем декодируется с использованием `unicode_escape`. Если это вызывает ошибку `UnicodeDecodeError`, строка возвращается без изменений. Затем функция ищет все последовательности вида `\\uXXXX` и преобразует их в соответствующие Unicode символы.
4.  **Обработка других типов данных**: Если входные данные не являются ни словарем, ни списком, ни строкой, функция возвращает данные без изменений.

**Параметры**:

*   `input_data` (Dict[str, Any] | list | str): Входные данные (словарь, список или строка), содержащие Unicode escape-последовательности.

**Возвращает**:

*   Dict[str, Any] | list | str: Преобразованные данные с декодированными Unicode escape-последовательностями.

**Примеры**:

Пример использования для словаря:

```python
input_dict = {
    'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
    'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
    'price': 123.45
}
decoded_dict = decode_unicode_escape(input_dict)
print(decoded_dict)
# {'product_name': 'מ"קט יצרן\nH510M K V2', 'category': 'ערכת שבבים', 'price': 123.45}
```

Пример использования для списка:

```python
input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']
decoded_list = decode_unicode_escape(input_list)
print(decoded_list)
# ['ערכת שבבים', 'H510M K V2']
```

Пример использования для строки:

```python
input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'
decoded_string = decode_unicode_escape(input_string)
print(decoded_string)
# מ"קט יצרן
# H510M K V2
```