# Модуль `chrome`

## Обзор

Этот модуль предоставляет класс `Chrome`, который расширяет `selenium.webdriver.Chrome`, добавляя дополнительную функциональность для настройки и конфигурации экземпляра Chrome WebDriver.  Класс предназначен для продвинутых случаев использования и включает методы для поиска свободных портов, настройки опций и инициализации WebDriver.  Он использует конфигурационный файл `chrome.json` для управления путями к драйверу и исполняемому файлу Chrome.

## Файл `chrome.json`

Этот файл содержит конфигурацию для Chrome WebDriver, включая пути к исполняемому файлу и драйверу.

```json
{
  "profiles": {
      "one.last.bit": {
        "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data\\\\Default",
        "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
        "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data\\\\Default"
      },
      "@todo": "Организовать управление профилями из общей системы хранения (например, Keepass)"
    },
    "locator_description": "Можно использовать профили из разных директорий. На системе может быть несколько профилей.",

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
  "locator_description headers": "Настраиваемые для любого агента. Подробности в `fake-useragent`."
}
```

**Компоненты файла `chrome.json`:**

- **`profiles`**: Определяет директории для разных профилей Chrome.
- **`driver`**:
    - **`chromedriver`**: Конфигурация пути к ChromeDriver.
    - **`chrome_binary`**: Конфигурация пути к исполняемому файлу Chrome.
- **`headers`**: Стандартные заголовки для WebDriver, включая user-agent и другие HTTP заголовки.

## Класс `Chrome`

### Описание

Класс `Chrome` расширяет `selenium.webdriver.Chrome`, добавляя функциональность для настройки WebDriver.

### Атрибуты

- `driver_name`: Имя используемого WebDriver.
- `d`: Экземпляр WebDriver.
- `options`: Объект `ChromeOptions` для конфигурации.
- `user_agent`: Параметры user-agent для WebDriver.

### Методы

#### `__init__(self, user_agent: dict = None, *args, **kwargs) -> None`

Инициализирует Chrome WebDriver со специфицированными опциями и профилем.

**Параметры:**

- `user_agent (dict, optional):` Настройки user-agent для Chrome WebDriver.  Ссылка: https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066


#### `find_free_port(self, start_port: int, end_port: int) -> int |  None`

Ищет свободный порт в заданном диапазоне.

**Параметры:**

- `start_port`: Начальный порт диапазона.
- `end_port`: Конечный порт диапазона.

**Возвращает:**

- Свободный порт, если доступен, иначе None.


#### `set_options(self, settings: list | dict | None = None) -> ChromeOptions`

Устанавливает параметры запуска для Chrome WebDriver.

**Параметры:**

- `settings`: Настройки параметров Chrome.

**Возвращает:**

- Объект `ChromeOptions` со специфицированными параметрами запуска.

## Функции

(Здесь перечислены и описаны любые другие функции из модуля)

## Обработка исключений

Все блоки обработки исключений (`try...except`) должны содержать описание возможных ошибок, с использованием `ex` вместо `e`.


```