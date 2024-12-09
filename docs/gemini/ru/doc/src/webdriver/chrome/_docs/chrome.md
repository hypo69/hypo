# Модуль `chrome`

## Обзор

Данный модуль предоставляет класс `Chrome`, расширяющий `selenium.webdriver.Chrome` для настройки и конфигурации экземпляра Chrome WebDriver.  Он предназначен для продвинутых задач и включает методы для поиска свободных портов, установки опций и инициализации WebDriver.  Конфигурация WebDriver осуществляется с использованием файла `chrome.json`.

## Оглавление

- [Модуль `chrome`](#модуль-chrome)
- [Обзор](#обзор)
- [Класс `Chrome`](#класс-chrome)
    - [Метод `__init__`](#метод-init)
    - [Метод `find_free_port`](#метод-find-free-port)
    - [Метод `set_options`](#метод-set-options)
- [Файл `chrome.json`](#файл-chromejson)
    - [Компоненты файла `chrome.json`](#компоненты-файла-chromejson)

## Класс `Chrome`

### Описание

Класс `Chrome` наследуется от `selenium.webdriver.Chrome` и предоставляет расширенные возможности для настройки WebDriver.

### Метод `__init__`

```python
def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
    """ Инициализирует Chrome WebDriver заданными параметрами и профилем.
    
    Args:
        user_agent (dict, optional): Параметры user-agent для Chrome WebDriver. 
        Ссылки: https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066.
        *args: Дополнительные аргументы для родительского класса.
        **kwargs: Дополнительные ключевые аргументы для родительского класса.
    
    Returns:
        None: Не возвращает значение.
    
    Raises:
        WebDriverException: Ошибка при инициализации Chrome WebDriver.
        Exception: Общая ошибка при работе с Chrome WebDriver.
    """
```

### Метод `find_free_port`

```python
def find_free_port(self, start_port: int, end_port: int) -> int | None:
    """
    Находит свободный порт в заданном диапазоне.

    Args:
        start_port: Начальный порт диапазона.
        end_port: Конечный порт диапазона.

    Returns:
        int | None: Свободный порт, если найден, иначе None.
    """
```

### Метод `set_options`

```python
def set_options(self, settings: list | dict | None = None) -> ChromeOptions:
    """ Устанавливает параметры запуска Chrome WebDriver.

    Args:
        settings: Параметры конфигурации опций Chrome.

    Returns:
        ChromeOptions: Объект ChromeOptions с заданными параметрами запуска.
    """
```

## Файл `chrome.json`

### Описание

Файл `chrome.json` используется для конфигурации Chrome WebDriver.

### Компоненты файла `chrome.json`

```json
{
  "profiles": {
      "one.last.bit": {
        "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data\\\\Default",
        "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
        "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data\\\\Default"
      },
      "@todo": "Организация управления из общей системы хранения `Keepass`"
    },
    "locator_description": "Можно использовать профили из разных каталогов. На системе может быть несколько профилей.",

  "driver": {
    "chromedriver": [ "webdrivers", "chrome", "125.0.6422.14", "chromedriver.exe" ],
    "chrome_binary": [ "webdrivers", "chrome", "125.0.6422.14", "win64-125.0.6422.14", "chrome-win64", "chrome.exe" ],
    "locator_description": "Разные версии драйвера находятся в разных папках. Работаю с протестированной версией браузера. Система обновляет до последней версии в фоновом режиме."
  },

  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "locator_description headers": "Настраивается для любого агента. Подробности в `fake-useragent`."
}
```

- `profiles`: Определяет каталоги для различных профилей Chrome.
- `driver`:
    - `chromedriver`: Путь к ChromeDriver.
    - `chrome_binary`: Путь к исполняемому файлу Chrome.
- `headers`: Умолчательные заголовки для WebDriver, включая User-Agent и другие HTTP заголовки.