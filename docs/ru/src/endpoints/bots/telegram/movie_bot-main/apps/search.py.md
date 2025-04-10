# Модуль для поиска фильмов и сериалов на Kinopoisk через Google

## Обзор

Модуль предназначен для поиска информации о фильмах и сериалах на сайте Kinopoisk.ru с использованием поисковой системы Google. Он принимает поисковый запрос и тип контента (фильм или сериал) и возвращает ссылку, заголовок и описание найденного результата.

## Подробней

Этот модуль использует библиотеки `requests` для отправки HTTP-запросов, `bs4` (Beautiful Soup) для парсинга HTML-ответов, `dotenv` для загрузки переменных окружения и модуль `useragent` для получения случайного User-Agent.
Основная функция `search_query` выполняет поиск на Google с заданным запросом и типом контента, а затем извлекает релевантную информацию о фильме или сериале с сайта Kinopoisk.

## Функции

### `search_query`

```python
def search_query(query: str, type_movie: str = 'series') -> dict | None:
    """
    Выполняет поиск фильма или сериала на Kinopoisk через Google.

    Args:
        query (str): Поисковый запрос.
        type_movie (str, optional): Тип контента ('series' для сериалов, 'films' для фильмов). По умолчанию 'series'.

    Returns:
        dict | None: Словарь с информацией о фильме/сериале (ссылка, заголовок, описание) или None, если ничего не найдено.

    Example:
        >>> search_query('теория большого взрыва')
        {'link': 'https://w2.kpfr.wiki/series/...', 'title': '...', 'description': '...'}
    """
```

**Как работает функция**:

1.  **Формирование поискового запроса**:
    -   Формирует поисковый запрос для Google, используя переданные аргументы `query` (поисковый запрос) и `type_movie` (тип контента, по умолчанию `series`). Запрос формируется в виде `'site:www.kinopoisk.ru/{type_movie} {query}'`.

2.  **Выполнение поискового запроса**:
    -   Отправляет HTTP-запрос к Google с использованием библиотеки `requests`.
    -   В заголовках запроса передается случайно сгенерированный User-Agent для имитации запроса от браузера.
    -   Параметры запроса включают поисковый запрос (`q`), язык (`hl=ru`) и таймаут ожидания ответа (5 секунд).

3.  **Обработка ответа**:
    -   Полученный HTML-ответ передается в библиотеку `Beautiful Soup` для парсинга.

4.  **Извлечение результатов поиска**:
    -   Ищет все блоки `div` с классом `"g"` в HTML-структуре, которые содержат результаты поиска.

5.  **Анализ результатов**:
    -   Для каждого найденного результата пытается извлечь ссылку (`a`), заголовок (`h3`) и описание (`div` с атрибутом `style="-webkit-line-clamp:2"`).
    -   Проверяет наличие всех трех элементов.
    -   Проверяет, что предпоследний элемент ссылки (идентификатор фильма/сериала) является числом.

6.  **Формирование результата**:
    -   Если все условия выполнены, формирует словарь с информацией о фильме/сериале, включая:
        -   `link`: Ссылка на страницу фильма/сериала на Kinopoisk.
        -   `title`: Заголовок результата поиска.
        -   `description`: Описание результата поиска (обрезается до определенной длины и добавляется "...").

7.  **Возврат результата**:
    -   Если найден хотя бы один подходящий результат, функция возвращает словарь с информацией о фильме/сериале.
    -   Если ничего не найдено, функция возвращает `None`.

```
Поисковый запрос --> HTTP запрос к Google --> HTML ответ --> BeautifulSoup парсинг
    |                                                                                     |
    V                                                                                     |
Извлечение результатов поиска (div с классом "g") ----------------------------------------> Анализ результатов
    |                                                                                     |
    V                                                                                     |
  Ссылка, заголовок, описание? --> Да --> Формирование результата (словарь) --> Возврат словаря
                                  |
                                  Нет
                                  |
                                  V
                                  Возврат None
```

**Примеры**:

```python
search_query('теория большого взрыва')
# Возвращает словарь с информацией о сериале "Теория большого взрыва"

search_query('matrix', type_movie='films')
# Возвращает словарь с информацией о фильме "Матрица"

search_query('nonexistent movie')
# Возвращает None, если фильм или сериал с таким названием не найден
```

### `get_useragent`

Эта функция импортируется из модуля `apps.useragent`. Описание этой функции находится в файле `apps/useragent.py`. Функция используется для получения случайного User-Agent.

### \_\_name\_\_ == '\_\_main\_\_'

Этот блок кода предназначен для тестирования функции `search_query`. Он выполняется только при запуске модуля как основного скрипта.
В данном случае он вызывает функцию `search_query` с запросом `'теория большого взрыва'` и выводит результат в консоль.