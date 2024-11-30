# Модуль chrome

## Обзор

Данный модуль предоставляет класс `Chrome`, расширяющий `selenium.webdriver.Chrome` для настройки и конфигурации экземпляра Chrome WebDriver. Класс предназначен для продвинутых случаев использования и включает методы поиска свободных портов, установки опций и инициализации WebDriver.

## Файл chrome.json

Файл `chrome.json` служит для конфигурации параметров Chrome WebDriver.  В нем определены пути к исполняемому файлу ChromeDriver, Chrome браузеру, профилям, а также заголовки HTTP.  Файл `chrome.json` предоставляет гибкость в настройке, позволяя задавать различные профили и параметры запуска.

### Структура файла chrome.json

```json
{
  "profiles": {
      "one.last.bit": {
        "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data\\\\Default",
        "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
        "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data\\\\Default"
      },
      "@todo": "Organize management from a shared storage system `Keepass`"
    },
    "locator_description": "You can use profiles from different directories. Multiple profiles can be available on the system.",

  "driver": {
    "chromedriver": [ "webdrivers", "chrome", "125.0.6422.14", "chromedriver.exe" ],
    "chrome_binary": [ "webdrivers", "chrome", "125.0.6422.14", "win64-125.0.6422.14", "chrome-win64", "chrome.exe" ],
    "locator_description": "Different driver versions are in different folders. I work with a tested version of the browser. The system updates to the latest version in the background."
  },

  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "locator_description headers": "Adjustable for any agent. Details in `fake-useragent`."
}
```

**Описание разделов файла `chrome.json`:**

- **`profiles`**: Определяет пути к различным профилям Chrome.
- **`driver`**:
    - **`chromedriver`**: Путь к исполняемому файлу ChromeDriver.
    - **`chrome_binary`**: Путь к исполняемому файлу Chrome.
- **`headers`**: Заголовки HTTP для запросов, включая user-agent и другие.

## Классы

### `Chrome`

**Описание**: Класс `Chrome` расширяет базовый класс `selenium.webdriver.Chrome` и добавляет функциональность для настройки и инициализации Chrome WebDriver.

**Атрибуты**:

- `driver_name`: Имя используемого WebDriver'а.
- `d`: Экземпляр WebDriver.
- `options`: Опции для Chrome.
- `user_agent`: Настройки user-agent.


**Методы**:

#### `__init__(self, user_agent: dict = None, *args, **kwargs) -> None`

**Описание**: Инициализирует Chrome WebDriver с указанными опциями и профилем.

**Параметры**:

- `user_agent (dict, optional)`: Настройки user-agent для Chrome WebDriver.


#### `find_free_port(self, start_port: int, end_port: int) -> int | None`

**Описание**: Находит свободный порт в указанном диапазоне.

**Параметры**:

- `start_port (int)`: Начальный порт диапазона.
- `end_port (int)`: Конечный порт диапазона.

**Возвращает**:

- `int | None`: Свободный порт, если найден, или `None`, если свободный порт не найден.

#### `set_options(self, settings: list | dict | None = None) -> ChromeOptions`

**Описание**: Устанавливает опции запуска для Chrome WebDriver.

**Параметры**:

- `settings (list | dict | None, optional)`: Настройки опций Chrome.

**Возвращает**:

- `ChromeOptions`: Объект с указанными опциями запуска.


**Обрабатываемые исключения**:

- `WebDriverException`: Ошибка при инициализации Chrome WebDriver.
- `Exception`: Общая ошибка при работе с Chrome WebDriver.


## Функции

(Нет функций в данном коде, кроме методов класса.)


```