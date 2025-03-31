# Модуль `firefox.py`

## Обзор

Модуль `firefox.py` предоставляет класс `Firefox`, который является расширением стандартного `webdriver.Firefox` из Selenium. Он добавляет функциональность для настройки пользовательского профиля Firefox, запуска в режиме киоска, установки пользовательских настроек и прокси. Модуль использует настройки из файла `firefox.json`, позволяя гибко конфигурировать браузер.

## Содержание

1.  [Классы](#классы)
    *   [Firefox](#firefox)
2.  [Функции](#функции)
    *   [set_proxy](#set_proxy)
    *   [_payload](#_payload)

## Классы

### `Firefox`

**Описание**: Расширение для `webdriver.Firefox` с дополнительной функциональностью.

**Параметры**:
* `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
* `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
* `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
* `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
* `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
* `options` (Optional[List[str]], optional): Список опций для Firefox. По умолчанию `None`.
* `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

**Методы**:
* `__init__`: Инициализирует драйвер Firefox с заданными параметрами.
* `set_proxy`: Настраивает прокси для Firefox.
* `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

## Функции

### `set_proxy`

**Описание**: Настройка прокси из словаря, возвращаемого `get_proxies_dict`.

**Параметры**:
- `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Возвращает**:
- `None`

### `_payload`

**Описание**: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `None`

**Возвращает**:
- `None`