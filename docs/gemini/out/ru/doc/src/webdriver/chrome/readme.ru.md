# Chrome WebDriver для Selenium

## Обзор

Этот модуль предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определённые в файле `chrome.json`, такие как user-agent и настройки профиля браузера, для гибкого и автоматизированного взаимодействия с браузером.

## Оглавление

- [Chrome WebDriver для Selenium](#chrome-webdriver-для-selenium)
- [Обзор](#обзор)
- [Ключевые особенности](#ключевые-особенности)
- [Требования](#требования)
- [Конфигурация](#конфигурация)
- [Пример конфигурации (chrome.json)](#пример-конфигурации-chromejson)
- [Описание полей конфигурации](#описание-полей-конфигурации)
    - [options](#options)
    - [disabled_options](#disabled_options)
    - [profile_directory](#profile_directory)
    - [binary_location](#binary_location)
    - [headers](#headers)
    - [proxy_enabled](#proxy_enabled)
- [Использование](#использование)
- [Паттерн Singleton](#паттерн-singleton)
- [Логирование и отладка](#логирование-и-отладка)
- [Примеры логов](#примеры-логов)
- [Лицензия](#лицензия)


## Ключевые особенности

- Централизованная конфигурация (файл `chrome.json`).
- Поддержка множественных профилей браузера.
- Улучшенное логирование и обработка ошибок.


## Требования

- Python 3.x
- Selenium
- Fake User Agent
- Бинарник ChromeDriver (например, `chromedriver`).

Установите необходимые зависимости:

```bash
pip install selenium fake_useragent
```

Убедитесь, что `chromedriver` доступен в вашей системе или укажите путь к нему в конфигурации.


## Конфигурация

Конфигурация хранится в файле `chrome.json`.


## Пример конфигурации (chrome.json)

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
    "os": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
    "internal": "webdriver\\chrome\\profiles\\default",
    "testing": "%LOCALAPPDATA%\\Google\\Chrome for Testing\\User Data"
  },
  "binary_location": {
    "os": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "exe": "bin\\webdrivers\\chrome\\125.0.6422.14\\chromedriver.exe",
    "binary": "bin\\webdrivers\\chrome\\125.0.6422.14\\win64-125.0.6422.14\\chrome-win64\\chrome.exe",
    "chromium": "bin\\webdrivers\\chromium\\chrome-win\\chrome.exe"
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

## Описание полей конфигурации

### options

Словарь параметров Chrome для изменения поведения браузера.

### disabled_options

Опции, которые явно отключены.

### profile_directory

Пути к директориям с пользовательскими данными Chrome.

### binary_location

Пути к различным бинарникам Chrome.

### headers

Пользовательские HTTP-заголовки.

### proxy_enabled

Булевое значение, указывающее, использовать ли прокси.


## Использование

```python
from src.webdriver.chrome import Chrome

# Инициализация Chrome WebDriver с настройками user-agent
browser = Chrome(user_agent="Mozilla/5.0 ...")

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()
```

## Паттерн Singleton

WebDriver использует паттерн Singleton.


## Логирование и отладка

Используется `logger` из `src.logger`.


## Примеры логов

- Ошибка инициализации WebDriver.
- Проблемы с конфигурацией `chrome.json`.

## Лицензия

MIT License.  См. файл [LICENSE](LICENSE).