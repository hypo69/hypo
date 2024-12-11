# Chrome WebDriver для Selenium

## Обзор

Этот репозиторий предоставляет пользовательскую реализацию Chrome WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определенные в файле `chrome.json`, такие как пользовательский агент и настройки профиля браузера, для обеспечения гибких и автоматизированных взаимодействий с браузером.

## Содержание

### Оглавление

- [Chrome WebDriver для Selenium](#chrome-webdriver-для-selenium)
- [Обзор](#обзор)
- [Основные возможности](#ключевые-возможности)
- [Предварительные требования](#предварительные-требования)
- [Конфигурация](#конфигурация)
    - [Пример конфигурации (`chrome.json`)](#пример-конфигурации-chromejson)
    - [Поля конфигурации](#поля-конфигурации)
        - [`options`](#options)
        - [`disabled_options`](#disabled_options)
        - [`profile_directory`](#profile_directory)
        - [`binary_location`](#binary_location)
        - [`headers`](#headers)
        - [`proxy_enabled`](#proxy_enabled)
- [Использование](#использование)
    - [Образец кода](#образец-кода)
- [Обработка исключений (Singleton)](#обработка-исключений-singleton)
- [Логирование и отладка](#логирование-и-отладка)
    - [Примеры логов](#примеры-логов)
- [Лицензия](#лицензия)


## Ключевые возможности

- **Централизованная конфигурация**: Конфигурация управляется файлом `chrome.json`.
- **Множественные профили браузера**: Поддерживает несколько профилей браузера, позволяя пользователям настраивать различные параметры для тестирования.
- **Улучшенное логирование и обработка ошибок**: Предоставляет подробные журналы для инициализации, проблем с конфигурацией и ошибок WebDriver.


## Предварительные требования

Перед использованием этого WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Бинарный файл WebDriver для Chrome (например, `chromedriver`).

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Кроме того, убедитесь, что бинарный файл `chromedriver` доступен в переменной среды `PATH` или укажите путь к нему в конфигурации.


## Конфигурация

Конфигурация Chrome WebDriver хранится в файле `chrome.json`. Ниже приведен пример структуры файла конфигурации и его описание.

### Пример конфигурации (`chrome.json`)

```json
{
  "options": {
    "log-level": "5",
    "disable-dev-shm-usage": "",
    "remote-debugging-port": "0",
    "arguments": [ "--kiosk", "--disable-gpu" ]
  },
  "disabled_options": { "headless": "" },
  "profile_directory": {
    "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data",
    "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
    "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data"
  },
  "binary_location": {
    "os": "C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
    "exe": "bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\chromedriver.exe",
    "binary": "bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\win64-125.0.6422.14\\\\chrome-win64\\\\chrome.exe",
    "chromium": "bin\\\\webdrivers\\\\chromium\\\\chrome-win\\\\chrome.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "proxy_enabled": false
}
```

### Поля конфигурации

#### `options`
Словарь опций Chrome для модификации поведения браузера:
- `log-level`: Установка уровня ведения журнала. Значение `5` соответствует самому подробному уровню логирования.
- `disable-dev-shm-usage`: Отключает использование `/dev/shm` в контейнерах Docker (полезно для избежания ошибок в контейнерных средах).
- `remote-debugging-port`: Установка порта для удаженной отладки Chrome. `0` означает, что будет назначен случайный порт.
- `arguments`: Список аргументов командной строки для передачи в Chrome. Примеры: `--kiosk` для запуска в режиме киоска и `--disable-gpu` для отключения GPU-ускорения.


#### `disabled_options`
Опции, которые явно отключены. В данном случае режим `headless` отключен, что означает, что браузер Chrome будет работать в видимом окне, а не в режиме headless.

#### `profile_directory`
Пути к каталогам данных пользователя Chrome для различных сред:
- `os`: Путь к каталогу данных пользователя по умолчанию (обычно для систем Windows).
- `internal`: Внутренний путь для профиля WebDriver по умолчанию.
- `testing`: Путь к каталогу данных пользователя, специально настроенному для тестирования.

#### `binary_location`
Пути к различным бинарникам Chrome:
- `os`: Путь к установленному бинарнику Chrome для операционной системы.
- `exe`: Путь к исполняемому файлу ChromeDriver.
- `binary`: Конкретный путь к версии Chrome для тестирования.
- `chromium`: Путь к бинарнику Chromium, который можно использовать как альтернативу Chrome.


#### `headers`
Настраиваемые HTTP-заголовки для использования в запросах браузера:
- `User-Agent`: Указывает строку пользовательского агента браузера.
- `Accept`, `Accept-Charset`, `Accept-Encoding`, `Accept-Language`, `Connection`: Стандартные HTTP-заголовки.

#### `proxy_enabled`
Булево значение, указывающее, следует ли использовать прокси-сервер для WebDriver. По умолчанию установлено `false`.


## Использование

Для использования `Chrome` WebDriver в вашем проекте достаточно импортировать его и инициализировать:

### Образец кода

```python
from src.webdriver.chrome import Chrome

# Инициализируйте Chrome WebDriver с настройками пользовательского агента
browser = Chrome(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# Откройте веб-сайт
browser.get("https://www.example.com")

# Закройте браузер
browser.quit()
```

Класс `Chrome` автоматически загружает настройки из файла `chrome.json` и использует их для настройки WebDriver. Вы также можете указать пользовательский агент при инициализации WebDriver.


## Обработка исключений (Singleton)

WebDriver `Chrome` следует паттерну Singleton. Это означает, что будет создан только один экземпляр `Chrome` WebDriver. Если экземпляр уже существует, будет повторно использован тот же экземпляр, и откроется новое окно.


## Логирование и отладка

Класс WebDriver использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации. Любые проблемы во время инициализации, конфигурации или выполнения будут записаны в журнал для облегчения отладки.

### Примеры логов

- Ошибка при инициализации WebDriver: `Ошибка инициализации Chrome WebDriver: <подробности ошибки>`
- Проблемы с конфигурацией: `Ошибка в файле chrome.json: <подробности проблемы>`


## Лицензия

Этот проект лицензирован по MIT. Подробности см. в файле [LICENSE](LICENSE).