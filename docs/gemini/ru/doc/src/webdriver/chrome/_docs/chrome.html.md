# Модуль `src.webdriver.chrome`

## Обзор

Модуль `src.webdriver.chrome` предоставляет реализацию веб-драйвера Chrome, использующего Chrome для разработчиков. Версия драйвера определяется в файле `chrome.json`.

## Содержание

- [Класс `Chrome`](#класс-chrome)
    - [Описание](#описание-класса-chrome)
    - [Метод `__init__`](#__init__)
    - [Метод `find_free_port`](#find_free_port)
    - [Метод `set_options`](#set_options)

## Класс `Chrome`

### Описание класса `Chrome`

Подкласс `selenium.webdriver.Chrome`, предоставляющий дополнительные функциональные возможности.

### `__init__`

**Описание**: Инициализирует веб-драйвер Chrome с указанными опциями и профилем.

**Параметры**:
- `user_agent` (dict, optional): Настройки user-agent для веб-драйвера Chrome. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `WebDriverException`: Если не удалось инициализировать веб-драйвер.
- `Exception`: Общая ошибка, если веб-драйвер Chrome аварийно завершил работу.

```python
def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
    """
    Args:
        user_agent (dict, optional): Настройки User-Agent для веб-драйвера Chrome. По умолчанию `None`.

    Returns:
        None: 

    Raises:
         WebDriverException:  Если не удалось инициализировать веб-драйвер.
         Exception: Общая ошибка, если веб-драйвер Chrome аварийно завершил работу.
    """
```

### `find_free_port`

**Описание**: Находит свободный порт в указанном диапазоне.

**Параметры**:
- `start_port` (int): Начальный порт диапазона.
- `end_port` (int): Конечный порт диапазона.

**Возвращает**:
- `int | None`: Свободный порт, если он доступен, или `None`, если свободный порт не найден.

```python
def find_free_port(self, start_port: int, end_port: int) -> int |  None:
    """
    Args:
         start_port (int): Начальный порт диапазона.
         end_port (int): Конечный порт диапазона.

    Returns:
        int | None:  Свободный порт, если он доступен, или `None`, если свободный порт не найден.
    """
```

### `set_options`

**Описание**: Устанавливает параметры запуска для веб-драйвера Chrome.

**Параметры**:
- `settings` (list | dict | None, optional): Настройки конфигурации для параметров Chrome. По умолчанию `None`.

**Возвращает**:
- `ChromeOptions`: Объект `ChromeOptions` с указанными параметрами запуска.

```python
def set_options(self, settings: list | dict | None = None) -> ChromeOptions:
    """
    Args:
         settings (list | dict | None, optional): Настройки конфигурации для параметров Chrome. По умолчанию `None`.

    Returns:
        ChromeOptions: Объект `ChromeOptions` с указанными параметрами запуска.
    """
```