# Модуль unicode

## Обзор

Модуль `unicode.py` предназначен для декодирования строк, списков или словарей, содержащих юникодные escape-последовательности, в читаемый текст. Он содержит функцию `decode_unicode_escape`, которая рекурсивно обрабатывает данные различных типов, преобразуя escape-последовательности в удобочитаемые символы.

## Подробней

Этот модуль важен для обработки данных, полученных из внешних источников, таких как JSON-файлы или API, где юникодные символы могут быть представлены в виде escape-последовательностей. Он гарантирует, что эти данные будут правильно отображаться и использоваться в приложении. Расположение файла `hypotez/src/utils/convertors/unicode.py` указывает на то, что он является частью утилит преобразования данных, используемых в проекте `hypotez`.

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

     **Как работает функция**:

     ```mermaid
     graph TD
         A[Начало] --> B{Тип входных данных?};
         B -- Словарь --> C[Рекурсивно обработать значения словаря];
         C --> B;
         B -- Список --> D[Рекурсивно обработать элементы списка];
         D --> B;
         B -- Строка --> E[Декодировать escape-последовательности];
         E --> F[Преобразовать последовательности \\uXXXX];
         F --> G[Вернуть декодированную строку];
         B -- Другой тип --> H[Вернуть входные данные без изменений];
         G --> I[Конец];
         H --> I;
     ```
    """
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