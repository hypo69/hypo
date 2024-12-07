# Модуль Firefox WebDriver

## Обзор

Данный модуль содержит класс `Firefox`, расширяющий функциональность стандартного Firefox WebDriver. Он позволяет настраивать пользовательский профиль, запускать WebDriver в режиме киоска и устанавливать настройки прокси.

## Требования

- Python 3.12+
- Selenium
- Fake User-Agent
- Модуль обработки прокси

## Установка

1. Установите все зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Убедитесь, что установлены следующие компоненты:
   - **geckodriver** (для поддержки WebDriver)
   - **Firefox** (поддерживаемая версия)

3. Для работы с прокси укажите путь к файлу прокси с помощью параметра `proxy_file_path`.


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
        proxy_file_path=proxy_file_path
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Описание класса и методов

### Класс `Firefox`

- Расширяет стандартный Firefox WebDriver, добавляя функциональность:
  - Настройка пользовательского профиля
  - Настройки прокси
  - Настройка пользовательского user-agent
  - Интеграция с JavaScript и выполнение локеров

#### Конструктор `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             *args, **kwargs) -> None:
```

- **profile_name**: Название пользовательского профиля Firefox.
- **geckodriver_version**: Версия geckodriver.
- **firefox_version**: Версия Firefox.
- **user_agent**: Строка user-agent.
- **proxy_file_path**: Путь к файлу прокси.


#### Метод `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
```

- Настраивает прокси для Firefox, выбирая случайный рабочий прокси из предоставленного файла прокси.


#### Метод `_payload`

```python
def _payload(self) -> None:
```

- Загружает необходимые исполнители для локеров и JavaScript.


## Дополнительная настройка

- **Прокси**: Модуль автоматически выбирает доступный рабочий прокси из предоставленного файла, указанного параметром `proxy_file_path`.
- **Профиль Firefox**: Вы можете указать путь к пользовательскому профилю Firefox.
- **User Agent**: Модуль позволяет установить пользовательский user-agent для WebDriver.

## Логирование

Модуль использует `logger` для логирования ошибок и предупреждений.

## Лицензия

Данный проект лицензирован по MIT. См. файл LICENSE для получения дополнительной информации.