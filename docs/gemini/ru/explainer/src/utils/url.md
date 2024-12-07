```MD
# <input code>

```python
## \file hypotez/src/utils/string/url.py
# -*- coding: utf-8 -*-
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

**Шаг 1: Ввод URL**

Пользователь вводит URL-адрес в консоль.

**Пример:** `https://example.com/page?param1=value1&param2=value2&param3=`


**Шаг 2: Проверка валидности URL**

Функция `is_url(url)` проверяет, соответствует ли введённая строка формату URL, используя библиотеку `validators`.


**Пример:**

`is_url("https://example.com/page?param1=value1&param2=value2&param3=") --> True`
`is_url("невалидный URL") --> False`

**Шаг 3: Извлечение параметров**

Если URL валидный, функция `extract_url_params(url)` анализирует строку URL, используя `urllib.parse.urlparse` для разбора и `urllib.parse.parse_qs` для извлечения параметров.

**Пример:**

`extract_url_params("https://example.com/page?param1=value1&param2=value2&param3=") --> {"param1": "value1", "param2": "value2", "param3": None}`

**Шаг 4: Обработка параметров**

Результат `parse_qs` — словарь, где ключи — имена параметров, а значения — списки возможных значений. Код преобразует список значений в строку для удобства отображения, если параметр имеет только одно значение.

**Пример:**
`{"param1": ["value1"], "param2": ["value2"], "param3": []} --> {"param1": "value1", "param2": "value2", "param3": None}`

**Шаг 5: Вывод результата**

Если извлеченные параметры есть, программа выводит их в виде ключ-значение. Иначе выводится сообщение о том, что параметров нет.


# <mermaid>

```mermaid
graph TD
    A[Пользователь вводит URL] --> B{Проверка валидности URL};
    B -- Да --> C[extract_url_params(URL)];
    B -- Нет --> D[Вывод "Невалидный URL"];
    C --> E{Извлечение параметров};
    E -- Да --> F[Вывод параметров];
    E -- Нет --> G[Вывод "URL не содержит параметров"];
    F --> H[Конец];
    G --> H;
    D --> H;

    subgraph "extract_url_params"
        C --> I[urlparse(URL)];
        I --> J[parse_qs(query)];
        J --> K{Обработка значений};
        K -- Единственное значение --> L[Возврат словаря];
        K -- Множество значений --> L;

    end
```

**Объяснение зависимостей в диаграмме:**

* `urllib.parse`: Библиотека для работы с URL-адресами (разбор, извлечение параметров).
* `validators`: Библиотека для проверки валидности URL.


# <explanation>

**Импорты:**

* `from urllib.parse import urlparse, parse_qs`: Импортирует функции для работы с URL-адресами. `urlparse` разбирает URL-адрес на составляющие части, а `parse_qs` извлекает параметры из строки запроса.
* `import validators`: Импортирует модуль `validators` для проверки валидности URL-адресов. Эта библиотека может быть установлена через pip (`pip install validators`).


**Функции:**

* `extract_url_params(url: str) -> dict | None`: Извлекает параметры из строки URL. Возвращает словарь, содержащий параметры и их значения, или `None`, если параметры отсутствуют.
* `is_url(text: str) -> bool`: Проверяет, является ли переданная строка валидным URL-адресом. Возвращает `True`, если строка является валидным URL, и `False` в противном случае.

**Переменные:**

* `MODE`: Переменная, вероятно, используется для выбора режима работы программы (например, `dev`, `prod`). В данном случае она не используется в коде.

**Возможное улучшение:**

* Обработка ошибок: Функция `extract_url_params` могла бы обрабатывать исключения (например, `ValueError` если URL невалидный), а не просто возвращать `None`.
* Более информативные сообщения об ошибках: При ошибках выводить более подробные сообщения, чтобы облегчить отладку.
* Документация: Добавить описание типов возвращаемых значений для функций.

**Взаимосвязь с другими частями проекта:**

Код в модуле `utils/string/url.py` предоставляет функции для работы с URL-адресами и может быть использован другими частями проекта, которые нуждаются в обработке данных из URL. Например, функции для обработки данных, полученных из запросов по URL.

**Общий вывод:**

Код хорошо структурирован и выполняет свои задачи.  Он использует библиотеки `urllib.parse` и `validators` для эффективной обработки URL-адресов, что делает код более читаемым и надежным.  Возможные улучшения касаются более подробной обработки ошибок и улучшения информативности сообщений об ошибках.