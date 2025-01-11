# Конфигурация Firefox WebDriver

## Обзор

Этот файл содержит JSON-конфигурацию для настройки Firefox WebDriver. Он определяет параметры запуска браузера, пути к исполняемым файлам и заголовки HTTP.

## Содержание

- [Обзор](#обзор)
- [Параметры](#параметры)
- [Отключенные параметры](#отключенные-параметры)
- [Профиль](#профиль)
- [Пути к исполняемым файлам](#пути-к-исполняемым-файлам)
- [Заголовки](#заголовки)
- [Прокси](#прокси)

## Параметры

Данный раздел содержит массив `options`, который в текущей конфигурации пуст. Это означает, что при запуске Firefox WebDriver не будут переданы никакие дополнительные опции командной строки.
```json
 "options": [  ]
```

## Отключенные параметры

Массив `disabled_options` перечисляет параметры командной строки, которые будут отключены при запуске браузера.
В данном случае отключены следующие параметры:
- `--kiosk` (Запуск браузера в режиме киоска)
- `--headless` (Запуск браузера в режиме без графического интерфейса)
```json
"disabled_options": [ "--kiosk", "--headless"  ]
```

## Профиль

Раздел `profile_directory` задает путь к каталогу профиля Firefox.
- `os`: Путь к профилю, используемый при работе на основной операционной системе.
  - `%LOCALAPPDATA%\\Mozilla\\Firefox\\Profiles\\zojh5u5a.default-release-3`
- `internal`: Путь к профилю, который является внутренним для проекта.
  - `webdriver\\firefox\\profiles\\95c5aq3n.default-release`
- `default`: Определяет, какой путь к профилю будет использоваться по умолчанию. В данном случае используется путь `os`.
```json
"profile_directory": {
    "os": "%LOCALAPPDATA%\\\\Mozilla\\\\Firefox\\\\Profiles\\\\zojh5u5a.default-release-3",
    "internal": "webdriver\\\\firefox\\\\profiles\\\\95c5aq3n.default-release",
    "default": "os"
  }
```

## Пути к исполняемым файлам

Раздел `executable_path` содержит пути к исполняемым файлам Firefox и Geckodriver:
- `firefox_binary`: Путь к исполняемому файлу Firefox.
  - `bin\\webdrivers\\firefox\\ff\\core-127.0.2\\firefox.exe`
- `geckodriver`: Путь к исполняемому файлу Geckodriver.
  - `bin\\webdrivers\\firefox\\gecko\\33\\geckodriver.exe`
```json
"executable_path": {
    "firefox_binary": "bin\\\\webdrivers\\\\firefox\\\\ff\\\\core-127.0.2\\\\firefox.exe",
    "geckodriver": "bin\\\\webdrivers\\\\firefox\\\\gecko\\\\33\\\\geckodriver.exe"
  }
```

## Заголовки

Раздел `headers` содержит HTTP заголовки, которые будут отправляться браузером.
- `User-Agent`: Определяет строку агента пользователя.
  -  `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11`
- `Accept`: Определяет типы контента, принимаемые браузером.
  - `text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8`
- `Accept-Charset`: Определяет кодировку, принимаемую браузером.
  - `ISO-8859-1,utf-8;q=0.7,*;q=0.3`
- `Accept-Encoding`: Определяет методы сжатия, принимаемые браузером.
  - `none` (сжатие не используется)
- `Accept-Language`: Определяет языки, принимаемые браузером.
  - `en-US,en;q=0.8`
- `Connection`: Определяет параметр соединения.
  - `keep-alive` (использовать постоянное соединение)
```json
 "headers": {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  }
```

## Прокси

Поле `proxy_enabled` указывает, включен ли прокси. В данном случае прокси отключен.
```json
"proxy_enabled":false
```