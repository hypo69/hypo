# Модуль hypotez/src/webdriver/bs/bs.py

## Обзор

Модуль `bs.py` предоставляет класс `BS` для парсинга HTML контента, полученного из файла или URL, с использованием библиотек `BeautifulSoup` и `lxml`.  Он поддерживает загрузку данных как из локальных файлов, так и из веб-страниц.  Модуль содержит функции для извлечения данных по заданному локейтору.

## Классы

### `BS`

**Описание**: Класс `BS` предназначен для парсинга HTML содержимого.  Он хранит загруженное HTML-содержимое и предоставляет методы для его обработки.

**Атрибуты**:

- `html_content`:  Содержимое HTML страницы (строка).


**Методы**:

#### `get_url(self, url: str)`

**Описание**: Загружает HTML содержимое из указанного источника.  Может получать данные из локального файла или из веб-ресурса.

**Параметры**:

- `url` (str): Путь к файлу или URL-адрес.


**Возвращает**:

- `bool`: `True` при успешной загрузке, `False` в противном случае.


**Обрабатывает исключения**:

- `Exception`: При проблемах с чтением локального файла.
- `requests.RequestException`: При проблемах с запросом к веб-ресурсу.
- Возвращает `None` если содержимое не удалось загрузить.


#### `execute_locator(self, locator: SimpleNamespace | dict, url: str = None)`

**Описание**:  Выполняет поиск элементов в загруженном HTML содержимом по заданному локейтору.

**Параметры**:

- `locator` (SimpleNamespace | dict): Объект, содержащий параметры поиска (например, тип селектора, атрибут и т.д.).
- `url` (str, optional): URL страницы для парсинга, если необходимо перечитать содержимое. По умолчанию `None`.


**Возвращает**:

- `list`: Список результатов поиска (элементы HTML).


**Обрабатывает исключения**:

- `Exception`: Обрабатывает возможные ошибки при парсинге.


## Функции

(В данном модуле нет самостоятельных функций, помимо методов класса `BS`)


## Примеры использования

```python
from src.webdriver import Driver
from hypotez.src.webdriver.bs import BS


# Пример использования для файла:
bs_instance = BS()
file_path = 'path/to/your/file.html'  # Замените на действительный путь
success = bs_instance.get_url(f'file://{file_path}')
if success:
    locator = SimpleNamespace(attribute='someId', by='id', selector='//some_tag') # пример локейтора
    elements = bs_instance.execute_locator(locator)
    if elements:
        print("Найденные элементы:", elements)
    else:
        print("Элементы не найдены.")

# Пример использования для URL:
url = 'https://example.com'
bs_instance = BS()
success = bs_instance.get_url(url)
if success:
  locator = SimpleNamespace(attribute='someClass', by='css', selector='//*[contains(@class, "someClass")]')
  elements = bs_instance.execute_locator(locator)
  if elements:
        print("Найденные элементы:", elements)
  else:
        print("Элементы не найдены.")
```

**Примечание:**  Замените `'path/to/your/file.html'` и `'someClass'` на действительные значения.  Пример кода предполагает использование `SimpleNamespace` для хранения локейтора.  Для корректной работы необходимо импортировать `SimpleNamespace` из `types`.  Код для `Driver` класса не показан, но подразумевается, что он существует в модуле `src.webdriver`.
```