# Документация модуля `src.webdriver.firefox`

## Обзор

Этот модуль содержит класс `Firefox`, который расширяет функциональность стандартного WebDriver для Firefox. Он позволяет настраивать пользовательский профиль, запускать WebDriver в киоске и устанавливать настройки прокси-сервера.

## Содержание

1. [Требования](#требования)
2. [Установка](#установка)
3. [Пример использования](#пример-использования)
4. [Описание классов и методов](#описание-классов-и-методов)
    - [Класс `Firefox`](#класс-firefox)
        - [`__init__`](#__init__)
        - [`set_proxy`](#set_proxy)
        - [`_payload`](#_payload)
5. [Дополнительные настройки](#дополнительные-настройки)
6. [Логирование](#логирование)
7. [Лицензия](#лицензия)

## Требования

- Python 3.12+
- Selenium
- Fake User-Agent
- Модуль для работы с прокси

## Установка

1. Установите все зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Убедитесь, что у вас установлены следующие компоненты:
   - **geckodriver** (для работы с WebDriver)
   - **Firefox** (поддерживаемая версия)

3. Для работы с прокси, укажите путь к файлу с прокси-серверами через параметр `proxy_file_path`.

## Пример использования

Пример использования класса `Firefox`:

```python
from src.webdriver.firefox import Firefox

if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    # Инициализация и запуск браузера
    browser = Firefox(
        profile_name=profile_name,
        geckodriver_version=geckodriver_version,
        firefox_version=firefox_version,
        proxy_file_path=proxy_file_path,
        options=["--kiosk", "--headless"]  # Добавление опций
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Описание классов и методов

### Класс `Firefox`

**Описание**:
Расширяет стандартный WebDriver для Firefox, добавляя функции:
  - Установка пользовательского профиля
  - Прокси-настройки
  - Установка пользовательского агента
  - Интеграция с JavaScript и исполнение локаторов
  - Возможность передавать опции при инициализации

#### `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             options: Optional[List[str]] = None,  # Новый параметр
             *args, **kwargs) -> None:
```

**Описание**:
Конструктор класса `Firefox`. Инициализирует параметры для запуска браузера.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
- `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Firefox (например, `["--kiosk", "--headless"]`). По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `None`: Метод не возвращает значения.

#### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
```

**Описание**:
Настраивает прокси для Firefox, выбирая случайный рабочий прокси из предоставленного файла.

**Параметры**:
- `options` (Options): Экземпляр класса `selenium.webdriver.firefox.options.Options` для настройки опций браузера.

**Возвращает**:
- `None`: Метод не возвращает значения.

#### `_payload`

```python
def _payload(self) -> None:
```

**Описание**:
Загружает необходимые исполнительные файлы для локаторов и JavaScript.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Метод не возвращает значения.

## Дополнительные настройки

- **Прокси**: Модуль автоматически выбирает доступный рабочий прокси из файла, который указывается в параметре `proxy_file_path`.
- **Профиль Firefox**: Вы можете указать путь к кастомному профилю для Firefox.
- **Пользовательский агент**: Модуль позволяет задать произвольный пользовательский агент для WebDriver.
- **Опции**: Вы можете передать дополнительные опции для Firefox через параметр `options`.

## Логирование

Модуль использует `logger` для записи логов, включая ошибки и предупреждения.

## Лицензия

Этот проект лицензируется под лицензией MIT. Подробности см. в файле [LICENSE](../../LICENCE).