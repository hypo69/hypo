# Анализ кода модуля `search.py`

**Качество кода**
6
- Плюсы
    - Код выполняет поставленную задачу - поиск фильмов или сериалов на kinopoisk.ru через поисковую систему Google.
    - Используется библиотека `BeautifulSoup` для парсинга HTML.
    - Присутствует базовая обработка результатов поиска.
- Минусы
    - Отсутствует документация к модулю и функции.
    - Не используются `j_loads` или `j_loads_ns` для чтения данных.
    - Не все импорты соответствуют общему стилю (например, `from src.logger import logger`).
    - Отсутствует логирование ошибок.
    -  Используется стандартный `print` для вывода результатов, что не является хорошей практикой в production коде.

**Рекомендации по улучшению**

1.  **Добавить документацию:** Добавить docstring к модулю и функции `search_query` для описания их назначения, аргументов и возвращаемых значений.
2.  **Использовать `j_loads`:** В данном коде не происходит чтение json, но если в будущем оно понадобится, следует использовать  `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
3.  **Импортировать `logger`:** Заменить `from src.logger import logger` на `from src.logger.logger import logger`.
4.  **Добавить логирование ошибок:**  Добавить логирование ошибок с использованием `logger.error` в блоке `try-except` (которого пока нет, но рекомендуется добавить для обработки возможных ошибок при запросах и парсинге).
5.  **Использовать f-строки:** Использовать f-строки для форматирования строк, что делает код более читаемым и эффективным.
6. **Изменить способ формирования ссылки**: Использовать `os.path.join()` для корректного формирования URL.
7.  **Избегать жестких привязок:** Заменить жестко заданный URL `https://w2.kpfr.wiki` на константу или конфигурацию.
8. **Убрать `if __name__ == '__main__'`:** Код в `if __name__ == '__main__':` убрать, поскольку это не является частью рабочей функции.
9. **Улучшить возврат результата:** Возвращать словарь в формате {'data': result}, чтобы была возможность добавлять в него дополнительную информацию в будущем.

**Оптимизированный код**

```python
"""
Модуль для поиска фильмов и сериалов на Kinopoisk через поисковую систему Google.
=========================================================================================

Этот модуль предоставляет функцию `search_query`, которая ищет информацию о фильмах или сериалах на Kinopoisk, используя поисковую систему Google.

Пример использования
--------------------

Пример использования функции `search_query`:

.. code-block:: python

    result = search_query(query='теория большого взрыва', type_movie='series')
    if result:
        print(result)
    else:
        print('Ничего не найдено')
"""
import os
from typing import Any, Dict, Optional

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests import get
from src.logger.logger import logger  # Исправлен импорт логгера

from apps.useragent import get_useragent

load_dotenv()

KINOPOISK_BASE_URL = 'https://w2.kpfr.wiki' # Константа для базового URL


def search_query(query: str, type_movie: str = 'series') -> Optional[Dict[str, Any]]:
    """
    Ищет фильм или сериал на Kinopoisk через поисковую систему Google.

    Args:
        query (str): Поисковый запрос (название фильма или сериала).
        type_movie (str, optional): Тип контента ('series' или 'movie'). Defaults to 'series'.

    Returns:
        Optional[Dict[str, Any]]: Словарь с данными о фильме/сериале (ссылка, название, описание),
        или None, если ничего не найдено.
        Формат возвращаемого словаря: {'data': {'link': link, 'title': title, 'description': description}}
    
    Raises:
        Exception: В случае ошибки при выполнении HTTP запроса или парсинга HTML.
    
    Example:
        >>> result = search_query('теория большого взрыва', type_movie='series')
        >>> if result:
        >>>     print(result)
    """
    term = f'site:www.kinopoisk.ru/{type_movie} {query}'
    try:
        # Код исполняет отправку запроса к поисковой системе google
        resp = get(
            url="https://www.google.com/search",
            headers={"User-Agent": get_useragent()},
            params={"q": term, "hl": "ru"},
            timeout=5,
        )
        resp.raise_for_status() # Код проверяет статус ответа, вызывает исключение для кодов ошибок
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        if result_block:
            for result in result_block:
                link = result.find("a", href=True)
                title = result.find("h3")
                description = result.find("div", {"style": "-webkit-line-clamp:2"})
                if link and title and description:
                    if link["href"].split("/")[-2].isdigit():
                         # Код формирует ссылку на фильм/сериал, используя базовый URL и id
                        full_link = os.path.join(KINOPOISK_BASE_URL, type_movie, link["href"].split("/")[-2])
                        return {
                            'data': {
                                'link': full_link,
                                'title': title.text,
                                'description': f'{description.text[:-4]}...',
                            }
                        }
        return None
    except Exception as ex:
        logger.error(f'Произошла ошибка при поиске {query=}', exc_info=ex)
        return None
```