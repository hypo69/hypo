# Модуль `hypotez/src/webdriver/firefox/firefox.py`

## Обзор

Модуль `hypotez/src/webdriver/firefox/firefox.py` определяет подкласс `webdriver.Firefox`, называемый `Firefox`. Он предоставляет дополнительную функциональность, такую как запуск Firefox в режиме киоска и настройку профиля Firefox для WebDriver.

## Классы

### `Firefox`

**Описание**: Подкласс `webdriver.Firefox`, предоставляющий расширенные возможности для работы с браузером Firefox.

**Атрибуты**:

- `driver_name` (str): Имя используемого WebDriver, по умолчанию 'firefox'.


**Методы**:

#### `__init__`

**Описание**: Инициализирует Firefox WebDriver со заданными параметрами запуска, профилем, версией geckodriver и Firefox.

**Параметры**:

- `profile_name` (Optional[str], optional): Имя профиля Firefox для использования.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver для использования.
- `firefox_version` (Optional[str], optional): Версия Firefox для использования.
- `user_agent` (Optional[dict], optional): Словарь с настройками user-agent.

**Возвращает**:
- `None`

**Вызывает исключения**:

- `WebDriverException`: Исключение, если не удалось запустить драйвер. Возможные причины: проблемы с обновлением Firefox или его отсутствием в системе.
- `Exception`: Общее исключение, если произошла ошибка при инициализации Firefox WebDriver.


#### `_payload`

**Описание**: Загружает исполнители для локеров и сценариев JavaScript.

**Параметры**:

- Нет.

**Возвращает**:
- `None`

**Вызывает исключения**:

- Нет.


## Функции

(Нет функций в данном модуле, только класс)