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

**Блок-схема:**

```mermaid
graph TD
    A[Пользователь вводит URL] --> B{is_url(URL)};
    B -- True --> C[extract_url_params(URL)];
    B -- False --> F[Вывод "Не валидный URL"];
    C --> D{params is not None};
    D -- True --> E[Вывод параметров];
    D -- False --> G[Вывод "URL не содержит параметров"];
    E --> H[Конец];
    G --> H;
    F --> H;


subgraph extract_url_params(url)
    I[urlparse(url)] --> J{parsed_url.query};
    J --> K[parse_qs(parsed_url.query)] --> L{params is empty};
    L -- True --> M[Возврат None];
    L -- False --> N[Цикл по параметрам];
    N --> O{len(v) > 1};
    O -- True --> P[params[k] = v];
    O -- False --> Q[params[k] = v[0]];
    P --> R[Возврат params];
    Q --> R;
    M --> R;
end
```

**Пример:**

Пользователь вводит `https://example.com/page?param1=value1&param2=value2&param3=`.

1. **is_url(URL):** Функция проверяет, является ли строка `https://example.com/page?param1=value1&param2=value2&param3=` валидным URL. Результат - `True`.
2. **extract_url_params(URL):**
   - `urlparse(URL)` возвращает объект `ParseResult` с разложенной информацией о URL.
   - `parsed_url.query` содержит строку `param1=value1&param2=value2&param3=`.
   - `parse_qs(parsed_url.query)` создает словарь параметров.
   - Параметры `param1` и `param2` имеют несколько значений, а `param3` имеет одно значение.
   - `params = { 'param1': ['value1'], 'param2': ['value2'], 'param3': [''] }`.
   - Функция преобразует список значений в строку для параметров с единственным значением.
   - `params = {'param1': 'value1', 'param2': 'value2', 'param3': ''}`.
   - Функция возвращает словарь `params`.
3. **Вывод параметров:**
   - Вывод параметров `param1: value1`, `param2: value2`, `param3: ''`.


# <mermaid>

```mermaid
graph LR
    A[Пользователь] --> B(Ввод URL);
    B --> C[is_url];
    C -- true --> D[extract_url_params];
    C -- false --> G(Вывод "Не валидный URL");
    D --> E[urlparse];
    E --> F[parse_qs];
    F --> H{params пустой?};
    H -- true --> I(Вывод "URL не содержит параметров");
    H -- false --> J(Обработка параметров);
    J --> K{длина списка значений > 1?};
    K -- true --> L(значение = список);
    K -- false --> M(значение = первый элемент списка);
    L --> N(Вывод параметров);
    M --> N;
    I --> O(Конец);
    N --> O;
    G --> O;

    subgraph urllib.parse
        E --> F;
    end

    subgraph validators
        C --> C;
    end

    subgraph utils.string
        C --> D;
        D --> E;
        E --> F;
        F --> H;
        H --> J;
        J --> K;
        K --> L;
        K --> M;
        L --> N;
        M --> N;

        N --> I;
    end


```

# <explanation>

**Импорты:**

- `from urllib.parse import urlparse, parse_qs`: Импортирует функции `urlparse` для разбора URL и `parse_qs` для парсинга параметров запроса из библиотеки `urllib.parse`. Эти функции необходимы для работы с URL-адресами.
- `import validators`: Импортирует модуль `validators` для проверки валидности URL-адресов.


**Классы:**

В коде нет классов.


**Функции:**

- `extract_url_params(url: str) -> dict | None`: Эта функция извлекает параметры из строки URL. Она принимает URL-адрес в качестве аргумента и возвращает словарь с параметрами и их значениями. Если URL не содержит параметров, возвращает `None`.
  - Пример: `extract_url_params("https://example.com/page?param1=value1&param2=value2")` вернет `{ 'param1': 'value1', 'param2': 'value2' }`.
- `is_url(text: str) -> bool`: Эта функция проверяет, является ли переданный текст валидным URL-адресом. Она принимает текст и возвращает `True`, если он является URL, и `False` в противном случае.
  - Пример: `is_url("https://example.com")` вернет `True`, `is_url("invalid_url")` вернет `False`.

**Переменные:**

- `MODE = 'dev'`:  Переменная, вероятно, используется для обозначения режима работы (например, разработки или производства).

**Возможные ошибки и улучшения:**

- Обработка ошибок: Функция `extract_url_params` могла бы обрабатывать случаи, когда `urlparse` или `parse_qs` возвращают `ValueError`, например, при некорректном формате URL.
- Более подробные проверки: Функция `is_url` может быть улучшена с добавлением проверок на корректность URL схемы, например, если url не `http`, или `https` или другой поддерживаемый `validators`.
- Дополнительные проверки параметров: Можно добавить дополнительные проверки параметров, чтобы убедиться в корректном формате данных.


**Взаимосвязи с другими частями проекта:**

Код находится в модуле `utils/string/url.py`. Он предоставляет инструменты для работы с URL, которые могут быть использованы другими частями приложения, которые обрабатывают запросы, URL-адреса.


**Общее впечатление:**

Код написан чётко и лаконично.  Использование типов в аннотациях функций и типов возвращаемых значений – хороший стиль.  Функции `is_url` и `extract_url_params` хорошо документированы и легко читаемы.  Для добавления функциональности и надежности можно рассмотреть обработку потенциальных исключений и валидацию данных.