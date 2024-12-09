# Chrome WebDriver для Selenium

## Обзор

Этот модуль предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определённые в файле `chrome.json`, такие как user-agent и настройки профиля браузера, для гибкого и автоматизированного взаимодействия с браузером.

## Оглавление

* [Chrome WebDriver для Selenium](#chrome-webdriver-для-selenium)
* [Обзор](#обзор)
* [Ключевые особенности](#ключевые-особенности)
* [Требования](#требования)
* [Конфигурация](#конфигурация)
* [Пример конфигурации (`chrome.json`)](#пример-конфигурации-chromejson)
* [Описание полей конфигурации](#описание-полей-конфигурации)
    * [1. `options`](#1-options)
    * [2. `disabled_options`](#2-disabled_options)
    * [3. `profile_directory`](#3-profile_directory)
    * [4. `binary_location`](#4-binary_location)
    * [5. `headers`](#5-headers)
    * [6. `proxy_enabled`](#6-proxy_enabled)
* [Использование](#использование)
* [Паттерн Singleton](#паттерн-singleton)
* [Логирование и отладка](#логирование-и-отладка)
* [Примеры логов](#примеры-логов)
* [Лицензия](#лицензия)


## Ключевые особенности

- Централизованная конфигурация: Конфигурация управляется через файл `chrome.json`.
- Множественные профили браузера: Поддерживает несколько профилей браузера, позволяя настраивать различные параметры для тестирования.
- Улучшенное логирование и обработка ошибок: Предоставляет подробные логи для инициализации, проблем с конфигурацией и ошибок WebDriver.


## Требования

Перед использованием WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Бинарник ChromeDriver (например, `chromedriver`)

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Убедитесь, что `chromedriver` доступен в `PATH` или укажите его путь в конфигурации.


## Конфигурация

Конфигурация для Chrome WebDriver хранится в файле `chrome.json`.


## Пример конфигурации (`chrome.json`)

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


## Описание полей конфигурации

### 1. `options`

Словарь параметров Chrome для изменения поведения браузера.


### 2. `disabled_options`

Опции, которые явно отключены.


### 3. `profile_directory`

Пути к директориям с пользовательскими данными Chrome для различных сред.


### 4. `binary_location`

Пути к различным бинарникам Chrome.


### 5. `headers`

Пользовательские HTTP-заголовки, которые используются при запросах браузера.


### 6. `proxy_enabled`

Булевое значение, указывающее, следует ли использовать прокси-сервер.


## Использование

```python
from src.webdriver.chrome import Chrome

browser = Chrome(user_agent="Mozilla/5.0 ...")
browser.get("https://www.example.com")
browser.quit()
```


## Паттерн Singleton

WebDriver использует паттерн Singleton.


## Логирование и отладка

Используется `logger` для записи ошибок, предупреждений и информации.


## Примеры логов

- Ошибка при инициализации WebDriver: `<детали ошибки>`
- Проблемы с конфигурацией: `<детали проблемы>`


## Лицензия

Этот проект лицензирован на условиях MIT License.