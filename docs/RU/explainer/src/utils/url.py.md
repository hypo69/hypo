## Анализ кода `src/utils/url.py`

### 1. <алгоритм>

**Функция `extract_url_params(url: str)`:**

1.  **Начало:** Функция принимает строку `url` в качестве аргумента.
    *   Пример: `url` = `"https://example.com/path?param1=value1&param2=value2&param2=value3"`
2.  **Парсинг URL:** Используется `urlparse(url)` для разбора URL на составляющие, включая параметры запроса (query string).
    *   Пример: `parsed_url` = `ParseResult(scheme='https', netloc='example.com', path='/path', params='', query='param1=value1&param2=value2&param2=value3', fragment='')`
3.  **Извлечение параметров запроса:** `parse_qs(parsed_url.query)` извлекает параметры из query string в виде словаря, где ключи - это имена параметров, а значения - списки значений (т.к. параметр может повторяться).
    *   Пример: `params` = `{'param1': ['value1'], 'param2': ['value2', 'value3']}`
4.  **Преобразование значений:** Если `params` не пуст, значения параметров преобразуются из списка в строку, если список содержит только один элемент.
    *   Пример: `params` после преобразования = `{'param1': 'value1', 'param2': ['value2', 'value3']}`
5.  **Возврат результата:** Возвращается преобразованный словарь параметров, если они есть. Иначе возвращается `None`.
6.  **Конец.**

**Функция `is_url(text: str)`:**

1.  **Начало:** Функция принимает строку `text` для проверки.
    *   Пример: `text` = `"https://example.com"` или `text` = `"not a url"`
2.  **Проверка URL:** Используется `validators.url(text)` для проверки, является ли `text` валидным URL.
3.  **Возврат результата:** Возвращается `True`, если `text` - валидный URL, иначе `False`.
4.  **Конец.**

**Функция `url_shortener(long_url: str)`:**

1.  **Начало:** Функция принимает строку `long_url` для сокращения.
    *   Пример: `long_url` = `"https://example.com/very/long/path/to/resource"`
2.  **Формирование запроса:** Формируется строка запроса к API TinyURL.
    *   Пример: `url` = `"http://tinyurl.com/api-create.php?url=https://example.com/very/long/path/to/resource"`
3.  **Отправка запроса:** Используется `requests.get(url)` для отправки GET запроса к TinyURL API.
4.  **Обработка ответа:** Если статус код ответа равен 200, возвращается текст ответа (сокращенный URL), иначе возвращается `None`.
5.  **Конец.**

**Основной блок `if __name__ == "__main__":`:**

1.  **Начало:** Блок выполняется, если скрипт запущен напрямую.
2.  **Ввод URL:** Запрашивается URL у пользователя.
3.  **Проверка URL:** Проверяется валидность введенного URL с помощью функции `is_url`.
4.  **Обработка параметров:**
    *   Если URL валидный, извлекаются параметры с помощью `extract_url_params`.
    *   Если параметры существуют, они выводятся в консоль.
    *   Если параметров нет, выводится сообщение об их отсутствии.
5.  **Сокращение URL:**
    *   Предлагается сократить URL.
    *   Если пользователь соглашается, вызывается функция `url_shortener`.
    *   Если сокращение прошло успешно, выводится сокращенный URL.
    *   Если произошла ошибка, выводится сообщение об ошибке.
6.  **Обработка невалидного URL:** Если URL невалидный, выводится сообщение об этом.
7.  **Конец.**

### 2. <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> InputURL[Ввод URL от пользователя]
    InputURL --> IsValidURL{Проверка валидности URL <br> is_url(url)}
    IsValidURL -- True --> ExtractParams{Извлечение параметров <br> params = extract_url_params(url)}
    IsValidURL -- False --> InvalidURLError[Вывод: "Введенная строка не является валидным URL."]
    ExtractParams -- Params Exist --> OutputParams[Вывод параметров URL]
    ExtractParams -- No Params --> NoParamsMessage[Вывод: "URL не содержит параметров."]
    OutputParams --> AskShorten[Запрос на сокращение URL]
    NoParamsMessage --> AskShorten
    AskShorten --> ShortenURL{Сократить URL <br> url_shortener(url)}
    ShortenURL -- Success --> OutputShortURL[Вывод сокращенного URL]
    ShortenURL -- Fail --> ShortenURLError[Вывод: "Ошибка при сокращении URL."]
     InvalidURLError --> End[Конец]
    OutputShortURL --> End
    ShortenURLError --> End
    
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style End fill:#f9f,stroke:#333,stroke-width:2px
    style InputURL fill:#ccf,stroke:#333,stroke-width:2px
    style IsValidURL fill:#ccf,stroke:#333,stroke-width:2px
    style ExtractParams fill:#ccf,stroke:#333,stroke-width:2px
    style OutputParams fill:#ccf,stroke:#333,stroke-width:2px
    style NoParamsMessage fill:#ccf,stroke:#333,stroke-width:2px
    style AskShorten fill:#ccf,stroke:#333,stroke-width:2px
    style ShortenURL fill:#ccf,stroke:#333,stroke-width:2px
     style OutputShortURL fill:#ccf,stroke:#333,stroke-width:2px
    style ShortenURLError fill:#ccf,stroke:#333,stroke-width:2px
    style InvalidURLError fill:#ccf,stroke:#333,stroke-width:2px

```

### 3. <объяснение>

**Импорты:**

*   `from urllib.parse import urlparse, parse_qs`:
    *   `urlparse`: Функция из модуля `urllib.parse` используется для разбора URL-адреса на компоненты (схема, сетевое расположение, путь, параметры запроса и т.д.). Это позволяет легко извлечь параметры запроса из URL.
    *   `parse_qs`: Функция из модуля `urllib.parse` используется для разбора строки параметров запроса (query string) в словарь, где ключи - имена параметров, а значения - списки значений параметров.
*   `import validators`:
    *   Библиотека `validators` используется для валидации различных типов данных, включая URL. Функция `validators.url(text)` проверяет, является ли переданный текст валидным URL.
*   `import requests`:
    *   Библиотека `requests` используется для отправки HTTP-запросов (в данном случае GET-запрос) к API сервиса TinyURL для сокращения URL.

**Функции:**

*   `extract_url_params(url: str) -> dict | None`:
    *   **Аргументы:**
        *   `url` (str): Строка URL, из которой нужно извлечь параметры.
    *   **Возвращаемое значение:**
        *   `dict | None`: Словарь, содержащий параметры URL, где ключи - имена параметров, а значения - соответствующие значения параметров, либо `None`, если URL не содержит параметров.
    *   **Назначение:** Функция разбирает URL, извлекает параметры запроса и возвращает их в виде словаря. Если параметр имеет несколько значений, возвращается список, в противном случае - строка.
    *   **Примеры:**
        *   `extract_url_params("https://example.com/path?param1=value1&param2=value2")` вернет `{'param1': 'value1', 'param2': 'value2'}`.
        *   `extract_url_params("https://example.com/path?param1=value1&param2=value2&param2=value3")` вернет `{'param1': 'value1', 'param2': ['value2', 'value3']}`.
        *   `extract_url_params("https://example.com/path")` вернет `None`.
*   `is_url(text: str) -> bool`:
    *   **Аргументы:**
        *   `text` (str): Строка, которую нужно проверить на валидность URL.
    *   **Возвращаемое значение:**
        *   `bool`: `True`, если строка является валидным URL, иначе `False`.
    *   **Назначение:** Функция проверяет, является ли переданный текст валидным URL, используя библиотеку `validators`.
    *   **Примеры:**
        *   `is_url("https://example.com")` вернет `True`.
        *   `is_url("not a url")` вернет `False`.
*   `url_shortener(long_url: str) -> str | None`:
    *   **Аргументы:**
        *   `long_url` (str): Длинный URL, который нужно сократить.
    *   **Возвращаемое значение:**
        *   `str | None`: Сокращённый URL в виде строки или `None`, если произошла ошибка при сокращении.
    *   **Назначение:** Функция отправляет запрос к API TinyURL для сокращения длинного URL.
    *   **Примеры:**
        *   `url_shortener("https://example.com/very/long/path/to/resource")` вернет `"http://tinyurl.com/xxxxxxx"`.
        *   Если произойдет ошибка, `url_shortener("https://example.com/very/long/path/to/resource")` вернет `None`.

**Переменные:**

*   В основном блоке `if __name__ == "__main__":`:
    *   `url` (str): Строка, введенная пользователем, представляющая URL.
    *   `params` (dict | None): Словарь с параметрами URL или `None`.
    *   `shorten` (str): Строка, введенная пользователем ("y" или "n"), отвечающая на вопрос о сокращении URL.
    *   `short_url` (str | None): Сокращенный URL или `None`.

**Взаимосвязи с другими частями проекта:**

*   Данный модуль является утилитарным и не зависит от других частей проекта, кроме импортированных библиотек. Его основная задача - предоставлять функции для работы с URL-адресами.
*   Этот модуль может быть использован в других частях проекта, где требуется парсинг, валидация или сокращение URL-адресов.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок:** Функция `url_shortener` может возвращать `None` в случае ошибки, но не предоставляет подробной информации о причине ошибки. Можно добавить обработку исключений (например, `requests.exceptions.RequestException`) и логирование ошибок.
*   **Выбор сервиса сокращения URL:** Используется только TinyURL. Можно добавить возможность выбора другого сервиса сокращения URL или использования собственного.
*   **Валидация URL:** Можно усилить валидацию URL, добавив проверки на корректность схемы (http, https) или другие параметры.
*   **Тестирование:** Нет тестов. Для обеспечения надежности кода необходимо добавить unit-тесты.

В целом, данный модуль предоставляет базовый набор функций для работы с URL, но может быть расширен и улучшен для повышения надежности и функциональности.