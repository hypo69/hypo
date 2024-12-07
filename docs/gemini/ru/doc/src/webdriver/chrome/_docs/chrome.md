# Модуль chrome

## Обзор

Данный модуль предоставляет класс `Chrome`, расширяющий `selenium.webdriver.Chrome` для дополнительной функциональности настройки и конфигурации экземпляра Chrome WebDriver. Класс предназначен для сложных сценариев и включает методы для поиска свободных портов, установки опций и инициализации WebDriver.

## Файл chrome.json

Файл `chrome.json` содержит конфигурацию для Chrome WebDriver, включая пути к драйверу и исполняемому файлу браузера, а также параметры для загрузки профилей.

### Структура файла `chrome.json`

```json
{
  "profiles": {
      "one.last.bit": {
        "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data\\\\Default",
        "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
        "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data\\\\Default"
      },
      "@todo": "Организовать управление из системы общего хранения `Keepass`"
    },
    "locator_description": "Можно использовать профили из разных каталогов. На системе могут быть доступны несколько профилей.",

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
  "locator_description headers": "Настраиваемый для любого агента. Подробности в `fake-useragent`."
}
```

## Классы

### `Chrome`

**Описание**: Подкласс `selenium.webdriver.Chrome`, предоставляющий дополнительную функциональность.

**Атрибуты**:

- `driver_name` (str): Имя используемого WebDriver.
- `d` (webdriver.Chrome): Экземпляр WebDriver.
- `options` (ChromeOptions): Опции для конфигурации Chrome.
- `user_agent` (dict): Параметры user-agent для WebDriver.


**Методы**:

#### `__init__`

**Описание**: Инициализирует Chrome WebDriver с указанными параметрами и профилем.

**Параметры**:

- `user_agent` (dict): Параметры user-agent для Chrome WebDriver.
  
**Возвращает**:
  - None

#### `find_free_port`

**Описание**: Находит свободный порт в заданном диапазоне.

**Параметры**:

- `start_port` (int): Начальный порт диапазона.
- `end_port` (int): Конечный порт диапазона.

**Возвращает**:
- int | None: Свободный порт, если найден, иначе None.

#### `set_options`

**Описание**: Устанавливает параметры запуска для Chrome WebDriver.

**Параметры**:

- `settings` (list | dict | None): Параметры конфигурации для опций Chrome.


**Возвращает**:
- ChromeOptions: Объект `ChromeOptions` с указанными параметрами запуска.

**Обрабатывает исключения**:


- `WebDriverException`: Ошибка при инициализации Chrome WebDriver.
- `Exception`: Общая ошибка при работе с Chrome WebDriver. (требуется дополнительная обработка).


## Функции

(Нет функций в коде, только методы класса.)


```