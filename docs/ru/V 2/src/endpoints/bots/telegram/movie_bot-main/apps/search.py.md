# Модуль `search.py`

## Обзор

Модуль `search.py` предназначен для выполнения поиска фильмов и сериалов на сайте kinopoisk.ru с использованием поисковой системы Google. Он использует библиотеки `requests` для выполнения HTTP-запросов, `BeautifulSoup` для парсинга HTML-контента и `dotenv` для загрузки переменных окружения.

## Содержание

1.  [Функции](#Функции)
    -   [`search_query`](#search_query)

## Функции

### `search_query`

**Описание**: Выполняет поиск фильма или сериала на сайте kinopoisk.ru через Google и возвращает информацию о первом найденном результате.

**Параметры**:
- `query` (str): Поисковый запрос.
- `type_movie` (str, optional): Тип искомого контента ('series' для сериалов, по умолчанию 'series').

**Возвращает**:
- `dict | None`: Словарь с информацией о найденном фильме/сериале (ссылка, название, описание) или `None`, если ничего не найдено.

**Пример возвращаемого словаря:**
```python
{
    'link': 'https://w2.kpfr.wiki/series/12345/',
    'title': 'Название фильма/сериала',
    'description': 'Краткое описание фильма/сериала...'
}
```

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Возникает при ошибке выполнения HTTP-запроса.

```python
def search_query(query, type_movie='series'):
    """
    Args:
        query (str): Поисковый запрос.
        type_movie (str, optional): Тип искомого контента ('series' для сериалов, по умолчанию 'series').

    Returns:
        dict | None: Словарь с информацией о найденном фильме/сериале (ссылка, название, описание) или None, если ничего не найдено.

    Raises:
        requests.exceptions.RequestException: Возникает при ошибке выполнения HTTP-запроса.
    """
    term = f'site:www.kinopoisk.ru/{type_movie} {query}'
    try:
        resp = get(
            url="https://www.google.com/search",
            headers={"User-Agent": get_useragent()},
            params={"q": term, "hl": "ru"},
            timeout=5
        )
        resp.raise_for_status()
    except Exception as ex:
        print(f"Error during request: {ex}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    result_block = soup.find_all("div", attrs={"class": "g"})
    if result_block:
        for result in result_block:
            link = result.find("a", href=True)
            title = result.find("h3")
            description = result.find("div", {"style": "-webkit-line-clamp:2"})
            if link and title and description:
                if link["href"].split("/")[-2].isdigit():
                    return {
                        'link': f'https://w2.kpfr.wiki/{type_movie}/'
                                f'{link["href"].split("/")[-2]}',
                        'title': title.text,
                        'description': description.text[:-4] + '...',
                    }
    return None
```