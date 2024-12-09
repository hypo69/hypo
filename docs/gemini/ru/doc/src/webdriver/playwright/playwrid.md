# Модуль playwrid

## Обзор

Модуль `playwrid.py` определяет подкласс `PlaywrightCrawler`, называемый `Playwrid`. Он предоставляет дополнительную функциональность, такую как возможность устанавливать пользовательские настройки браузера, профили и параметры запуска с помощью Playwright.  Этот модуль используется для запуска веб-скрапинга с помощью Playwright, обеспечивая гибкость в настройке.

## Оглавление

- [Модуль playwrid](#модуль-playwrid)
- [Обзор](#обзор)
- [Класс Playwrid](#класс-playwrid)
    - [Метод `__init__`](#метод-init)
    - [Метод `_load_settings`](#метод-load_settings)
    - [Метод `_set_launch_options`](#метод-set_launch_options)
    - [Метод `start`](#метод-start)
    - [Свойство `current_url`](#свойство-current_url)

## Класс Playwrid

### Описание

Подкласс `PlaywrightCrawler`, предоставляющий дополнительные возможности настройки.

### Метод `__init__`

```python
def __init__(self, settings_name: Optional[str] = None, user_agent: Optional[Dict[str, Any]] = None, *args, **kwargs) -> None:
    """ Инициализирует Playwright Crawler с указанными параметрами запуска, настройками и user agent.

    Args:
        settings_name (Optional[str], optional): Имя файла настроек. По умолчанию None.
        user_agent (Optional[Dict[str, Any]], optional): Словарь настроек user agent. По умолчанию None.

    Raises:
        TypeError: Если типы аргументов не соответствуют ожидаемым.
        Exception: В случае возникновения других ошибок при загрузке настроек или инициализации.
    """
```

### Метод `_load_settings`

```python
def _load_settings(self, settings_name: Optional[str] = None) -> Any:
    """ Загружает настройки для Playwrid Crawler.

    Args:
        settings_name (Optional[str], optional): Имя файла настроек. По умолчанию None.

    Returns:
        SimpleNamespace: Объект SimpleNamespace, содержащий настройки.

    Raises:
        FileNotFoundError: Если файл настроек не найден.
        Exception: В случае других ошибок при чтении или разборе файла настроек.
    """
```

### Метод `_set_launch_options`

```python
def _set_launch_options(self, settings: SimpleNamespace) -> Dict[str, Any]:
    """ Конфигурирует параметры запуска для Playwright Crawler.

    Args:
        settings (SimpleNamespace): Объект SimpleNamespace, содержащий настройки запуска.

    Returns:
        dict: Словарь с параметрами запуска для Playwright.

    Raises:
        TypeError: Если тип `settings` не SimpleNamespace.
        Exception: В случае других ошибок.
    """
```

### Метод `start`

```python
def start(self, url: str) -> None:
    """ Запускает Playwrid Crawler и переходит к указанному URL.

    Args:
        url (str): URL для перехода.

    Raises:
        Exception: В случае возникновения ошибок во время работы с Playwright.
    """
```

### Свойство `current_url`

```python
@property
def current_url():
    """"""
    ...
```

**Описание:** Доступ к текущему URL.  Необходима реализация для возврата текущего URL.


## Функции

В этом модуле нет функций, помимо методов класса `Playwrid`.


```