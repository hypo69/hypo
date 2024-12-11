# Модуль chrome

## Обзор

Этот модуль предоставляет класс `Chrome`, расширяющий `selenium.webdriver.Chrome` для настройки и конфигурации экземпляра Chrome WebDriver с дополнительными опциями.  Класс предназначен для продвинутых случаев использования и включает методы для поиска свободных портов, настройки опций и инициализации WebDriver.  Модуль использует файл `chrome.json` для конфигурации различных параметров, включая пути к драйверу и исполняемому файлу браузера.

## Оглавление

* [Модуль chrome](#модуль-chrome)
* [Обзор](#обзор)
* [Класс Chrome](#класс-chrome)
    * [__init__](#__init__)
    * [find_free_port](#find_free_port)
    * [set_options](#set-options)
* [Файл chrome.json](#файл-chromejson)
    * [Компоненты файла chrome.json](#компоненты-файла-chromejson)


## Класс Chrome

### `Chrome`

**Описание**: Наследуется от `selenium.webdriver.Chrome` и предоставляет расширенные возможности для инициализации и настройки Chrome WebDriver.

**Атрибуты**:

- `driver_name` (str): Название используемого WebDriver.
- `d` (webdriver.Chrome): Экземпляр WebDriver.
- `options` (ChromeOptions): Опции Chrome для конфигурации.
- `user_agent` (dict): Настройки user-agent для WebDriver.


**Методы**:

#### `__init__`

```python
def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
    """ Инициализирует Chrome WebDriver с указанными опциями и профилем.
    Args:
        user_agent (dict, optional): Настройки user-agent для Chrome WebDriver.
        *args, **kwargs: Дополнительные аргументы для конструктора родительского класса.
    """
```

#### `find_free_port`

```python
def find_free_port(self, start_port: int, end_port: int) -> int |  None:
    """
    Находит свободный порт в указанном диапазоне.

    Args:
        start_port (int): Начальный порт диапазона.
        end_port (int): Конечный порт диапазона.

    Returns:
        int | None: Свободный порт, если доступен, или None, если свободный порт не найден.
    """
```

#### `set_options`

```python
def set_options(self, settings: list | dict | None = None) -> ChromeOptions:
    """ Устанавливает параметры запуска для Chrome WebDriver.
    Args:
        settings (list | dict | None, optional): Настройки опций Chrome.

    Returns:
        ChromeOptions: Объект ChromeOptions с указанными параметрами запуска.
    """
```


## Файл chrome.json

### Компоненты файла chrome.json

Файл `chrome.json` используется для конфигурации различных параметров, включая пути к драйверу и исполняемому файлу браузера, профили браузера, пользовательские заголовки и другие настройки.

**Структура файла:**

```json
{
  "profiles": {
    // ... конфигурация профилей
  },
  "driver": {
    "chromedriver": [ "webdrivers", "chrome", "125.0.6422.14", "chromedriver.exe" ],
    "chrome_binary": [ "webdrivers", "chrome", "125.0.6422.14", "win64-125.0.6422.14", "chrome-win64", "chrome.exe" ],
    // ... другие настройки драйвера
  },
  "headers": {
    // ... пользовательские заголовки
  },
  // ... другие настройки
}
```

**Важные поля:**

- `"profiles"`:  Конфигурация профилей Chrome.
- `"driver"`: Настройки пути к ChromeDriver и исполняемому файлу Chrome.
- `"headers"`: Настройки пользовательских HTTP-заголовков.

Обратите внимание на использование `gs.default_webdriver` для динамического пути к ChromeDriver.