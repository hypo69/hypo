# Модуль playwrid

## Обзор

Этот модуль предоставляет класс `Playwrid`, являющийся подклассом `PlaywrightCrawler`. Он расширяет функциональность, позволяя настраивать параметры браузера, профили и опции запуска с помощью Playwright.  Модуль загружает настройки из файла `playwrid.json` и предоставляет возможность переопределения настроек с помощью дополнительных файлов конфигурации.

## Классы

### `Playwrid`

**Описание**: Подкласс `PlaywrightCrawler`, предоставляющий расширенные возможности.

**Атрибуты**:

- `driver_name`: Название драйвера (`playwrid`).
- `context`: Текущий контекст (None по умолчанию).

**Методы**:

#### `__init__`

**Описание**: Инициализирует Playwright Crawler с заданными параметрами запуска, настройками и user agent.

**Параметры**:

- `settings_name` (Optional[str], необязательный): Имя файла настроек.
- `user_agent` (Optional[Dict[str, Any]], необязательный): Словарь с настройками user agent.

**Возвращает**:
- `None`

**Вызывает исключения**:
  - Любые исключения, возникающие при загрузке настроек или инициализации Playwright.


#### `_load_settings`

**Описание**: Загружает настройки для Playwrid Crawler.

**Параметры**:

- `settings_name` (Optional[str], необязательный): Имя файла настроек.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с загруженными настройками.

**Вызывает исключения**:
- Любые исключения, возникающие при чтении или парсинге файла настроек.


#### `_set_launch_options`

**Описание**: Настраивает параметры запуска для Playwright Crawler.

**Параметры**:

- `settings` (SimpleNamespace): Объект `SimpleNamespace` с настройками запуска.

**Возвращает**:
- `dict`: Словарь с параметрами запуска для Playwright.


#### `start`

**Описание**: Запускает Playwrid Crawler и переходит по указанному URL.

**Параметры**:

- `url` (str): URL для перехода.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`:  При возникновении ошибок во время работы программы.  Ошибки логгируются с помощью `logger.critical`.



#### `current_url`

**Описание**: Возвращает текущий URL (только проперти, не метод).

**Возвращает**:
- `str`: Текущий URL.

**Вызывает исключения**:
-  Любые исключения, связанные с доступом к текущему URL.

## Функции

(Нет функций в этом модуле)

## Конфигурация

Настройки хранятся в файле `playwrid.json` в каталоге `src/webdriver/playwright`.  Можно использовать дополнительные файлы конфигурации, добавив `.json` файл с именем, указанным в параметре `settings_name`.


```