# <input code>

```python
import re
from typing import Dict, Any

def decode_unicode_escape(input_data: Dict[str, Any] | list | str) -> Dict[str, Any] | list | str:
    """Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

    Args:
        input_data (dict | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

    Returns:
        dict | list | str: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

    Пример использования:
    .. code-block:: python
        input_dict = {
            'product_name': r'\u05de\u05e7"\\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
            'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
            'price': 123.45
        }

        input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

        input_string = r'\u05de\u05e7"\\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

        # Применяем функцию
        decoded_dict = decode_unicode_escape(input_dict)
        decoded_list = decode_unicode_escape(input_list)
        decoded_string = decode_unicode_escape(input_string)

        print(decoded_dict)
        print(decoded_list)
        print(decoded_string)

    """
    if isinstance(input_data, dict):
        return {key: decode_unicode_escape(value) for key, value in input_data.items()}
    elif isinstance(input_data, list):
        return [decode_unicode_escape(item) for item in input_data]
    elif isinstance(input_data, str):
        try:
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError:
            decoded_string = input_data
        unicode_escape_pattern = r'\u[0-9a-fA-F]{4}'
        decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        return decoded_string
    else:
        return input_data
```

# <algorithm>

**Шаг 1:** Функция `decode_unicode_escape` принимает входные данные (словарь, список или строку).

**Шаг 2:** Если входные данные - словарь, функция рекурсивно вызывает себя для каждого значения в словаре.

**Шаг 3:** Если входные данные - список, функция рекурсивно вызывает себя для каждого элемента списка.

**Шаг 4:** Если входные данные - строка:
    * **Шаг 4.1:**  Декодирует строку с использованием `input_data.encode('utf-8').decode('unicode_escape')`. Обрабатывает возможные `UnicodeDecodeError`, возвращая исходную строку в случае ошибки.
    * **Шаг 4.2:** Ищет все последовательности `\uXXXX` с помощью регулярного выражения `r'\u[0-9a-fA-F]{4}'`.
    * **Шаг 4.3:** Заменяет каждую найденную последовательность на ее декодированное значение, используя функцию `lambda`.


**Шаг 5:** Если входные данные не являются ни словарем, ни списком, ни строкой, функция возвращает исходные данные без изменений.


**Пример:**

Вход: `{ 'key': '\u0048\u0065\u006c\u006c\u006f' }`

Выход: `{ 'key': 'Hello' }`

Данные проходят через рекурсивные вызовы для словарей и списков.


# <mermaid>

```mermaid
graph TD
    A[input_data] --> B{isinstance(dict)};
    B -- True --> C[decode_unicode_escape(value) for key, value in input_data.items()];
    B -- False --> D{isinstance(list)};
    D -- True --> E[decode_unicode_escape(item) for item in input_data];
    D -- False --> F{isinstance(str)};
    F -- True --> G[encode('utf-8')];
    G --> H[decode('unicode_escape')];
    H --> I{UnicodeDecodeError?};
    I -- True --> J[input_data];
    I -- False --> K[re.sub(r'\u[0-9a-fA-F]{4}, lambda match: ...)];
    K --> L[return decoded_string];
    F -- False --> M[return input_data];
```


# <explanation>

**Импорты:**

* `import re`: Импортирует модуль регулярных выражений `re` для поиска и замены последовательностей `\uXXXX` в строках.
* `from typing import Dict, Any`: Импортирует типы данных `Dict` и `Any` из модуля `typing` для явного определения типов входных данных и возвращаемого значения функции.


**Функция `decode_unicode_escape`:**

* Принимает на вход данные типа `dict`, `list` или `str`.
* Возвращает данные того же типа, но с декодированными юникодными escape-последовательностями.
* Использует рекурсию для обработки вложенных словарей и списков.
* Обрабатывает возможные ошибки декодирования `UnicodeDecodeError`, возвращая исходную строку при ошибке.
* Использует регулярное выражение для поиска всех последовательностей `\uXXXX`, а не только первой.


**Возможные ошибки и улучшения:**

* **Неустойчивость к различным форматам:** Функция работает с escape последовательностями `\uXXXX`, но не работает с `\UXXXX` или другими типами escape-последовательностей.  Дополнительно  необходима проверка на входящие данные, чтобы убедиться, что они имеют правильный формат или выкинуть исключение, вместо возврата исходных данных.
* **Повышение производительности:** Для больших данных, возможно, использование более эффективных методов, чем `re.sub` для поиска и замены.
* **Проверка на корректные юникодные последовательности:** Необходимо добавить проверку на корректность  `\uXXXX` (не только на формат, но и на то, что такое кодирование действительно соответствует существующему кодовому значению в юникоде). Это позволит предотвратить обработку невалидных escape-последовательностей.
* **Документация:** Дополнить документацию примерами обработки различных типов входных данных, включая строки с несколькими escape-последовательностями, а также исключения `UnicodeDecodeError` .


**Взаимосвязи с другими частями проекта:**

Функция `decode_unicode_escape` скорее всего используется в других частях проекта для обработки данных, содержащих юникодные escape-последовательности, например, при чтении данных из файлов, веб-страниц, или из базы данных.  Ожидается, что данные, полученные из внешних источников, могут содержать различные форматы кодирования, а эта функция является вспомогательным средством для обработки таких данных.