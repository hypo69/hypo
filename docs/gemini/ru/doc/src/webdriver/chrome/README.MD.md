# Модуль Custom Chrome WebDriver для Selenium

## Обзор

Этот модуль предоставляет пользовательскую реализацию Chrome WebDriver с использованием Selenium. Он интегрирует параметры конфигурации, определенные в файле `chrome.json`, такие как user-agent и настройки профиля браузера, чтобы обеспечить гибкое и автоматизированное взаимодействие с браузером.

## Подорбней

Этот модуль предназначен для упрощения и централизации конфигурации Chrome WebDriver в проектах Selenium. Он позволяет легко управлять настройками браузера через файл `chrome.json` и поддерживает различные профили браузера для тестирования. Использование Singleton паттерна гарантирует, что будет создан только один экземпляр WebDriver.

## Ключевые особенности

- **Централизованная конфигурация**: Управление конфигурацией осуществляется через файл `chrome.json`.
- **Поддержка нескольких профилей браузера**: Поддерживает несколько профилей браузера, что позволяет настраивать различные параметры для тестирования.
- **Расширенное ведение журнала и обработка ошибок**: Предоставляет подробные журналы для инициализации, проблем с конфигурацией и ошибок WebDriver.
- **Возможность передачи пользовательских опций**: Поддерживает передачу пользовательских опций во время инициализации WebDriver.

## Требования

Перед использованием этого WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Chrome WebDriver binary (e.g., `chromedriver`)

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Кроме того, убедитесь, что двоичный файл `chromedriver` доступен в системном `PATH` или укажите его путь в конфигурации.

## Конфигурация

Конфигурация для Chrome WebDriver хранится в файле `chrome.json`. Ниже приведен пример структуры файла конфигурации и его описание:

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

### Описание полей конфигурации

#### 1. `options`

Словарь параметров Chrome для изменения поведения браузера:

- **log-level**: Устанавливает уровень ведения журнала. Значение `5` соответствует самому подробному уровню ведения журнала.
- **disable-dev-shm-usage**: Отключает использование `/dev/shm` в Docker контейнерах (полезно для предотвращения ошибок в контейнерных средах).
- **remote-debugging-port**: Устанавливает порт для удаленной отладки в Chrome. Значение `0` означает, что будет назначен случайный порт.
- **arguments**: Список аргументов командной строки, передаваемых в Chrome. Примеры: `--kiosk` для режима киоска и `--disable-gpu` для отключения аппаратного ускорения GPU.

#### 2. `disabled_options`

Параметры, явно отключенные. В этом случае режим `headless` отключен, что означает, что Chrome будет работать в видимом окне, а не в фоновом режиме.

#### 3. `profile_directory`

Пути к каталогам пользовательских данных Chrome для различных сред:

- **os**: Путь к каталогу пользовательских данных по умолчанию (обычно для систем Windows).
- **internal**: Внутренний путь для профиля WebDriver по умолчанию.
- **testing**: Путь к каталогу пользовательских данных, специально настроенному для тестирования.

#### 4. `binary_location`

Пути к различным двоичным файлам Chrome:

- **os**: Путь к установленному двоичному файлу Chrome для операционной системы.
- **exe**: Путь к исполняемому файлу ChromeDriver.
- **binary**: Конкретный путь к двоичному файлу Chrome для тестирования.
- **chromium**: Путь к двоичному файлу Chromium, который можно использовать в качестве альтернативы Chrome.

#### 5. `headers`

Пользовательские HTTP-заголовки, используемые в запросах браузера:

- **User-Agent**: Устанавливает строку user-agent для браузера.
- **Accept**: Устанавливает типы данных, которые браузер готов принимать.
- **Accept-Charset**: Устанавливает кодировку символов, поддерживаемую браузером.
- **Accept-Encoding**: Устанавливает поддерживаемые методы кодирования (установите значение `none`, чтобы отключить).
- **Accept-Language**: Устанавливает предпочитаемые языки.
- **Connection**: Устанавливает тип соединения, который должен использовать браузер (например, `keep-alive`).

#### 6. `proxy_enabled`

Логическое значение, указывающее, следует ли использовать прокси-сервер для WebDriver. По умолчанию `false`.

## Использование

Чтобы использовать `Chrome` WebDriver в своем проекте, просто импортируйте и инициализируйте его:

```python
from src.webdriver.chrome import Chrome

# Initialize Chrome WebDriver with user-agent settings and custom options
browser = Chrome(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Open a website
browser.get("https://www.example.com")

# Close the browser
browser.quit()
```

Класс `Chrome` автоматически загружает настройки из файла `chrome.json` и использует их для настройки WebDriver. Вы также можете указать пользовательский user-agent и передать дополнительные параметры во время инициализации WebDriver.

### Singleton Pattern

`Chrome` WebDriver использует Singleton pattern. Это означает, что будет создан только один экземпляр WebDriver. Если экземпляр уже существует, тот же экземпляр будет повторно использован, и будет открыто новое окно.

## Ведение журнала и отладка

Класс WebDriver использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации. Все проблемы, возникающие во время инициализации, конфигурации или выполнения, будут зарегистрированы для упрощения отладки.

### Пример журналов

- **Ошибка во время инициализации WebDriver**: `Error initializing Chrome WebDriver: <error details>`
- **Проблемы с конфигурацией**: `Error in chrome.json file: <issue details>`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](../../LICENSE).