```markdown
# Модуль: hypotez/src/goog/google_search.py

## Описание

Модуль `google_search.py` содержит класс `GoogleHtmlParser`, предназначенный для парсинга HTML-страниц поисковой выдачи Google и извлечения из них полезной информации. Он поддерживает как мобильные, так и десктопные версии страниц.


## Класс: `GoogleHtmlParser`

Класс `GoogleHtmlParser` обрабатывает HTML-код страницы и извлекает различные элементы, включая:

* Органические результаты поиска (`organic_results`).
* Featured snippet (`featured_snippet`).
* Карточку знаний (`knowledge_card`).
* Данные из скроллируемых виджетов (`scrolling_widgets`).
* Общее количество результатов (`estimated_results`).


### Методы:

* **`__init__(self, html_str: str, user_agent: str = 'desktop') -> None`**:
    Инициализирует парсер. Принимает HTML-код в виде строки и необязательный параметр `user_agent` (по умолчанию `desktop`), который определяет тип страницы (мобильная или десктопная).

* **`_clean(self, content: str) -> str`**:
    Очищает строку от лишних пробелов и символов.

* **`_normalize_dict_key(self, content: str) -> str`**:
    Нормализует строку для использования в качестве ключа словаря.

* **`_get_estimated_results(self) -> int`**:
    Извлекает общее количество результатов поиска.

* **`_get_organic(self) -> list`**:
    Извлекает список органических результатов поиска.  Обработка элементов `div[@class="g"]` включает  разбор возможных вариантов, когда встречаются `snippet` и `rich_snippet`. Обрабатываются различные варианты вложенности элементов, чтобы получить необходимую информацию.

* **`_get_featured_snippet(self) -> dict | None`**:
    Извлекает featured snippet, если он присутствует. Возвращает `None`, если его нет.

* **`_get_knowledge_card(self) -> dict | None`**:
    Извлекает карточку знаний, если она есть. Возвращает `None`, если нет.  Обработка сложной структуры карточки знаний.


* **`_get_scrolling_sections(self) -> list`**:
    Извлекает данные из скроллируемых виджетов (например, топ-истории).


* **`get_data(self) -> dict`**:
    Главный метод, собирающий все данные с поисковой страницы. Возвращает словарь с результатами.


### Атрибуты:

* **`tree (html.Element)`**: Дерево документа, полученное из HTML-строки.
* **`user_agent (str)`**: Тип пользователя (мобильный или десктопный), использовавшийся при получении HTML-кода.


## Использование

Для использования парсера:

```python
import requests
from lxml import html

from hypotez.src.goog import google_search

# Пример запроса
search_query = "python programming"
url = f"https://www.google.com/search?q={search_query}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'  # Добавляем User-Agent
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Обработка ошибок запроса

    parser = google_search.GoogleHtmlParser(response.text)
    data = parser.get_data()

    print(data)

except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
```

Этот код демонстрирует запрос к Google, обработку ответа и извлечение данных с помощью `GoogleHtmlParser`. Не забудьте установить необходимые библиотеки (`lxml`, `requests`).


## Замечания

* Код обрабатывает различные форматы HTML, встречающиеся на страницах поисковой выдачи Google.
* Обрабатываются потенциальные ошибки, например, отсутствие ожидаемых элементов на странице.
*  Добавлены комментарии и документация для улучшения читаемости и понимания кода.
* Пример использования теперь включает обработку ошибок запроса к Google.
* Указание корректного user-agent для запроса к Google.
