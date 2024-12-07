# <input code>

```python
## \file hypotez/src/utils/string/url.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string 
	:platform: Windows, Unix
	:synopsis: Модуль для работы с URL строками, включая извлечение параметров запроса и проверку на валидность UR

"""
MODE = 'dev'


from urllib.parse import urlparse, parse_qs
import validators

def extract_url_params(url: str) -> dict | None:
    """ Извлекает параметры из строки URL.

    Args:
        url (str): Строка URL для парсинга.

    Returns:
        dict | None: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.
    """
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    
    # Преобразуем значения из списка в строку, если параметр имеет одно значение
    if params:
        params = {k: v if len(v) > 1 else v[0] for k, v in params.items()}
        return params
    return None

def is_url(text: str) -> bool:
    """ Проверяет, является ли переданный текст валидным URL с использованием библиотеки validators.

    Args:
        text (str): Строка для проверки.

    Returns:
        bool: `True` если строка является валидным URL, иначе `False`.
    """
    return validators.url(text)


if __name__ == "__main__":
    # Получаем строку URL от пользователя
    url = input("Введите URL: ")
    
    # Проверяем валидность URL
    if is_url(url):
        params = extract_url_params(url)
        
        # Выводим параметры
        if params:
            print("Параметры URL:")
            for key, value in params.items():
                print(f"{key}: {value}")
        else:
            print("URL не содержит параметров.")
    else:
        print("Введенная строка не является валидным URL.")
```

# <algorithm>

**Алгоритм работы модуля:**

1. **`extract_url_params(url)`:**
   - Принимает строку `url` в качестве входных данных.
   - Использует `urlparse` для разбора строки `url` на компоненты (схема, домен, путь, параметры и т.д.).
   - Извлекает параметры запроса `query` из результата парсинга.
   - Использует `parse_qs` для преобразования строки параметров в словарь, где ключи — имена параметров, а значения — списки значений.
   - Проверяет, если значение параметра в списке имеет длину больше 1, оставляет его в списке. Иначе преобразует значение в строку.
   - Возвращает словарь `params` или `None`, если параметры не найдены.

   **Пример:**
   Вход: `url = "https://example.com?param1=value1&param2=value2&param3="`
   Результат: `{ "param1": "value1", "param2": "value2", "param3": "" }`


2. **`is_url(text)`:**
   - Принимает строку `text` в качестве входных данных.
   - Использует функцию `validators.url(text)` из пакета `validators` для проверки валидности `text` как URL.
   - Возвращает `True`, если `text` является валидным URL, иначе `False`.

   **Пример:**
   Вход: `text = "https://example.com"`
   Результат: `True`


3. **`__main__` блок:**
   - Запрашивает URL у пользователя.
   - Вызывает `is_url` для проверки валидности.
   - Если URL валиден, вызывает `extract_url_params` для извлечения параметров.
   - Выводит параметры или сообщение об отсутствии параметров.

**Пример использования:**

Пользователь вводит `https://example.com?param1=value1&param2=value2`.
`is_url()` возвращает `True`.
`extract_url_params()` возвращает словарь параметров.
Программа выводит параметры.

# <mermaid>

```mermaid
graph TD
    A[Пользователь] --> B{Ввод URL};
    B -- URL валиден --> C[is_url(url)];
    B -- URL не валиден --> D[Вывод: "Не валиден"];
    C -- True --> E[extract_url_params(url)];
    C -- False --> D;
    E -- Параметры найдены --> F[Вывод параметров];
    E -- Параметров нет --> G[Вывод: "Нет параметров"];
    F --> H[Конец];
    G --> H;
    subgraph "src.utils.string.url"
        C -.-> is_url;
        E -.-> extract_url_params;
    end
    subgraph "urllib.parse"
        E -.-> urlparse;
        E -.-> parse_qs;
    end
    subgraph "validators"
        C -.-> validators.url;
    end
```

# <explanation>

**Импорты:**

- `from urllib.parse import urlparse, parse_qs`: Импортирует функции `urlparse` и `parse_qs` из модуля `urllib.parse`. Они используются для анализа и разбора URL-адресов.  `urllib.parse`  —  стандартная библиотека Python, предназначенная для работы с URL.


- `import validators`: Импортирует модуль `validators`, который используется для проверки валидности URL-адреса.  `validators` - сторонний пакет, который нужно установить.


**Классы:**

В данном коде нет классов.


**Функции:**

- `extract_url_params(url: str) -> dict | None`:
    - Принимает строку `url` в качестве аргумента, представляющую URL-адрес.
    - Возвращает словарь с параметрами URL или `None`, если параметры отсутствуют.
    - Использует `urlparse` для разбора URL на составляющие части, в том числе параметры запроса.
    - Использует `parse_qs` для преобразования строки параметров запроса в словарь.
    - Важное изменение: обрабатывает случаи, когда параметр имеет одно значение, превращая список из одного элемента в строку.

- `is_url(text: str) -> bool`:
    - Принимает строку `text` в качестве аргумента.
    - Использует `validators.url(text)` для проверки, является ли `text` валидным URL.
    - Возвращает `True`, если `text` валидный URL, и `False` в противном случае.



**Переменные:**

- `MODE = 'dev'`:  Переменная, вероятно, используется для настройки режима работы, например, в зависимости от стадии разработки (dev, production).

**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Код не обрабатывает потенциальные исключения, например, если входная строка `url` не является валидным URL-адресом.  Добавление обработки исключений (например, `try...except` блоков) улучшит надежность.


**Взаимосвязи с другими частями проекта:**

Этот модуль `utils/string/url.py` представляет собой утилиту для работы с URL, которую, вероятно, будут использовать другие части приложения (`hypotez`).  Отсутствие контекста приложения затрудняет полное понимание всей цепочки взаимосвязей.

**Общее:**

Код хорошо структурирован, содержит docstrings, и демонстрирует корректный подход к обработке URL.  Добавление обработки ошибок и более подробных проверок сделает его более robust.