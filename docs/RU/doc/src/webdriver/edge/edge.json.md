# Конфигурация Edge Webdriver

## Обзор

Этот файл содержит конфигурацию для Edge WebDriver, включая параметры запуска, пути к профилям, исполняемому файлу и заголовки HTTP.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [Параметры запуска (`options`)](#параметры-запуска-options)
  - [Профили (`profiles`)](#профили-profiles)
  - [Путь к исполняемому файлу (`executable_path`)](#путь-к-исполняемому-файлу-executable_path)
  - [Заголовки HTTP (`headers`)](#заголовки-http-headers)

## Структура JSON

### Параметры запуска (`options`)

**Описание**:
Массив строк, содержащий параметры командной строки для запуска Edge WebDriver.

**Элементы**:
- `--disable-dev-shm-usage`: Отключает использование /dev/shm.
- `--remote-debugging-port=0`:  Назначает динамический порт для удаленной отладки.

```json
"options": [
    "--disable-dev-shm-usage",
    "--remote-debugging-port=0"
  ]
```

### Профили (`profiles`)

**Описание**:
Объект, содержащий пути к профилям Edge.

**Ключи**:
- `os` (str): Путь к профилю пользователя Edge по умолчанию в операционной системе.
- `internal` (str): Путь к внутреннему профилю Edge для WebDriver.

```json
"profiles": {
    "os": "%LOCALAPPDATA%\\\\Microsoft\\\\Edge\\\\User Data\\\\Default",
    "internal": "webdriver\\\\edge\\\\profiles\\\\default"
  }
```

### Путь к исполняемому файлу (`executable_path`)

**Описание**:
Объект, содержащий пути к исполняемому файлу Edge WebDriver.

**Ключи**:
- `default` (str): Путь к исполняемому файлу Edge WebDriver по умолчанию.

```json
 "executable_path": {
    "default": "webdrivers\\\\edge\\\\123.0.2420.97\\\\msedgedriver.exe"
  }
```

### Заголовки HTTP (`headers`)

**Описание**:
Объект, содержащий заголовки HTTP, которые будут отправляться при выполнении запросов.

**Ключи**:
- `User-Agent` (str): Заголовок User-Agent, представляющий браузер.
- `Accept` (str): Заголовок Accept, определяющий типы контента, которые браузер принимает.
- `Accept-Charset` (str): Заголовок Accept-Charset, определяющий кодировки символов, которые браузер принимает.
- `Accept-Encoding` (str): Заголовок Accept-Encoding, определяющий типы кодирования содержимого, которые браузер принимает.
- `Accept-Language` (str): Заголовок Accept-Language, определяющий языки, которые браузер принимает.
- `Connection` (str): Заголовок Connection, определяющий статус соединения.

```json
 "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  }
```