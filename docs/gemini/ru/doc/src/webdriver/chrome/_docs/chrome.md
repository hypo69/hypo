# Модуль `chrome`

## Обзор

Этот модуль предоставляет класс `Chrome`, который расширяет `selenium.webdriver.Chrome`, добавляя дополнительные возможности для настройки и конфигурации экземпляра Chrome WebDriver.  Класс предназначен для расширенных случаев использования, включая поиск свободных портов, настройку опций и инициализацию WebDriver.  Конфигурация WebDriver хранится в файле `chrome.json`.

## Оглавление

* [Модуль `chrome`](#модуль-chrome)
* [Обзор](#обзор)
* [Класс `Chrome`](#класс-chrome)
    * [Метод `__init__`](#метод-init)
    * [Метод `find_free_port`](#метод-find_free_port)
    * [Метод `set_options`](#метод-set_options)
* [Файл `chrome.json`](#файл-chromejson)
    * [Структура файла](#структура-файла)


## Класс `Chrome`

### Описание

Класс `Chrome` наследуется от `selenium.webdriver.Chrome` и предоставляет расширенные возможности для настройки Chrome WebDriver.

### Атрибуты

* `driver_name`: Имя используемого WebDriver. Значение: 'chrome'.
* `d`: Экземпляр WebDriver.
* `options`: Объект `ChromeOptions` для конфигурации.
* `user_agent`: Настройки User-Agent для WebDriver.

### Методы

#### `__init__`

```python
def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
    """ Инициализирует Chrome WebDriver с указанными опциями и профилем.
    
    Args:
        user_agent (dict, optional): Настройки User-Agent для Chrome WebDriver. 
        Ссылка: https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066
    
    Returns:
        None
    
    Raises:
        Exception: Возникает при ошибках инициализации.
    """
```

#### `find_free_port`

```python
def find_free_port(self, start_port: int, end_port: int) -> int |  None:
    """
    Находит свободный порт в заданном диапазоне.
    
    Args:
        start_port: Начальный порт диапазона.
        end_port: Конечный порт диапазона.
    
    Returns:
        Свободный порт, если найден, иначе None.
    """
```

#### `set_options`

```python
def set_options(self, settings: list | dict | None = None) -> ChromeOptions:
    """ Устанавливает опции запуска для Chrome WebDriver.
    
    Args:
        settings: Настройки опций Chrome.
    
    Returns:
        Объект `ChromeOptions` с заданными опциями запуска.
    """
```


## Файл `chrome.json`

### Структура файла

Файл `chrome.json` содержит конфигурацию для Chrome WebDriver.

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

Файл содержит информацию о путях к ChromeDriver и Chrome, профилях пользователя, а также заголовки HTTP.  Ключи `profiles` и `driver` содержат пути и конфигурацию для работы с разными версиями браузера и профилями.

```