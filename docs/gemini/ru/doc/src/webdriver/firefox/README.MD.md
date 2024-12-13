# Модуль Firefox WebDriver

## Обзор

Этот модуль содержит класс `Firefox`, который расширяет функциональность стандартного Firefox WebDriver. Он позволяет настраивать пользовательский профиль, запускать WebDriver в режиме киоска и задавать параметры прокси.

## Оглавление

- [Требования](#требования)
- [Установка](#установка)
- [Пример использования](#пример-использования)
- [Описание классов и методов](#класс-и-метод-описания)
    - [Класс `Firefox`](#firefox-класс)
        - [`__init__` Конструктор](#__init__-конструктор)
        - [`set_proxy` Метод](#set_proxy-метод)
        - [`_payload` Метод](#_payload-метод)
- [Дополнительная конфигурация](#дополнительная-конфигурация)
- [Логирование](#логирование)
- [Лицензия](#лицензия)

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

2. Убедитесь, что установлены следующие компоненты:
   - **geckodriver** (для поддержки WebDriver)
   - **Firefox** (поддерживаемая версия)

3. Для работы с прокси укажите путь к файлу с прокси через параметр `proxy_file_path`.

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
        options=["--kiosk", "--headless"]  # Добавление параметров
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Описание классов и методов

### `Firefox` Класс

- Расширяет стандартный Firefox WebDriver, добавляя функциональность, такую как:
  - Настройка пользовательского профиля
  - Настройка прокси
  - Установка пользовательского агента
  - Интеграция с JavaScript и выполнение локаторов
  - Возможность передачи параметров при инициализации

#### `__init__` Конструктор

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             options: Optional[List[str]] = None,  # Новый параметр
             *args, **kwargs) -> None:
```

**Описание**: Конструктор класса `Firefox`.

**Параметры**:
- `profile_name` (Optional[str], optional): Название пользовательского профиля Firefox. По умолчанию `None`.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
- `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Строка пользовательского агента. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список параметров Firefox (например, `["--kiosk", "--headless"]`). По умолчанию `None`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `set_proxy` Метод

```python
def set_proxy(self, options: Options) -> None:
```

**Описание**: Настраивает прокси для Firefox, выбирая случайный рабочий прокси из предоставленного файла.

**Параметры**:
- `options` (Options): Объект настроек WebDriver.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `_payload` Метод

```python
def _payload(self) -> None:
```

**Описание**: Загружает необходимые исполнители для локаторов и JavaScript.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция ничего не возвращает.

## Дополнительная конфигурация

- **Прокси**: Модуль автоматически выбирает доступный рабочий прокси из предоставленного файла, указанного параметром `proxy_file_path`.
- **Профиль Firefox**: Вы можете указать путь к пользовательскому профилю Firefox.
- **Пользовательский агент**: Модуль позволяет установить пользовательский агент для WebDriver.
- **Параметры**: Вы можете передать дополнительные параметры для Firefox через параметр `options`.

## Логирование

Модуль использует `logger` для регистрации ошибок и предупреждений.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE(../../LICENSE).