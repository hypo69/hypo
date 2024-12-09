# Модуль hypotez/src/webdriver/firefox/firefox.py

## Обзор

Данный модуль предоставляет класс `Firefox`, расширяющий стандартный `webdriver.Firefox` для работы с браузером Firefox. Он добавляет функциональность настройки пользовательского профиля, запуска в режиме киоска и установки пользовательских настроек, включая прокси.  Модуль использует настройки из файла `firefox.json` для конфигурации WebDriver.

## Классы

### `Firefox`

**Описание**:  Расширяет класс `selenium.webdriver.Firefox`, предоставляя дополнительные возможности для работы с Firefox WebDriver.  Включает настройку профиля, прокси, пользовательского агента и других параметров.

**Методы**

- `__init__`: Инициализирует объект `Firefox`.  Настраивает сервис, опции, профиль и загружает настройки из `firefox.json`. Обрабатывает исключения при запуске WebDriver.
- `set_proxy`: Настраивает прокси для WebDriver.  Выбирает случайный рабочий прокси из списка, полученного из `get_proxies_dict`, в зависимости от типа протокола (http, socks4, socks5). Обрабатывает возможные ошибки при настройке прокси.
- `_payload`: Вызывает методы для загрузки исполнителей для локейторов и JavaScript-сценариев.

## Функции

(Нет функций в этом модуле)

## Исключения

Класс `Firefox` обрабатывает следующие исключения:

- `WebDriverException`: Обрабатывает ошибки запуска WebDriver, предоставляя подробные сообщения об ошибках (например, обновление Firefox, отсутствие Firefox).
- `Exception`: Обрабатывает общие ошибки, возникающие во время работы с Firefox WebDriver.

## Настройки

Модуль использует файл `firefox.json` для загрузки следующих настроек:

- `executable_path`: Путь к файлам `geckodriver` и Firefox.
- `options`: Опции запуска Firefox, такие как `headless` или другие параметры.
- `headers`: Заголовки HTTP для подключения.
- `proxy_enabled`: Флаг, указывающий на использование прокси.
- `profile_directory`: Настройка профиля Firefox, указывающая на тип профиля (os или internal) и путь к профилю.

## Пример использования

```python
if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    browser = Firefox(
        profile_name=profile_name,
        geckodriver_version=geckodriver_version,
        firefox_version=firefox_version,
        proxy_file_path=proxy_file_path
    )
    browser.get("https://www.example.com")
    browser.quit()
```

```
```