# `unicode.py`

## Обзор

Модуль `unicode.py` содержит функцию `decode_unicode_escape`, предназначенную для декодирования юникодных escape-последовательностей в строках, словарях и списках. Функция рекурсивно обрабатывает значения, содержащие escape-последовательности, преобразуя их в читаемый текст.

## Содержание

- [Функции](#функции)
    - [`decode_unicode_escape`](#decode_unicode_escape)

## Функции

### `decode_unicode_escape`

**Описание**: Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

**Параметры**:
- `input_data` (Dict[str, Any] | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

**Возвращает**:
- `Dict[str, Any] | list | str`: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

**Пример использования**:
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