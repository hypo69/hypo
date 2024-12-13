# Модуль `firefox.py`

## Обзор

Этот модуль содержит класс `Firefox`, который расширяет функционал стандартного `webdriver.Firefox`.
Он предоставляет возможность настройки пользовательского профиля, запуска в режиме киоска и установки пользовательских настроек, включая прокси.

## Оглавление

1. [Класс `Firefox`](#класс-firefox)
    - [Метод `__init__`](#__init__)
    - [Метод `set_proxy`](#set_proxy)
    - [Метод `_payload`](#_payload)

## Классы

### `Firefox`

**Описание**:
Расширение для `webdriver.Firefox` с дополнительной функциональностью.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver.
- `firefox_version` (Optional[str], optional): Версия Firefox.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси.
- `options` (Optional[List[str]], optional): Список опций для Firefox.

#### `__init__`

**Описание**:
Инициализирует экземпляр класса `Firefox`, настраивает параметры Firefox, профиль, прокси и запускает браузер.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver.
- `firefox_version` (Optional[str], optional): Версия Firefox.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси.
- `options` (Optional[List[str]], optional): Список опций для Firefox.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `WebDriverException`: Возникает, если не удается запустить WebDriver.
- `Exception`: Возникает при любых других ошибках во время инициализации WebDriver.

#### `set_proxy`

**Описание**:
Настраивает прокси из словаря, возвращаемого `get_proxies_dict`.

**Параметры**:
- `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `_payload`

**Описание**:
Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `None`: Функция не принимает параметров.

**Возвращает**:
- `None`: Функция ничего не возвращает.