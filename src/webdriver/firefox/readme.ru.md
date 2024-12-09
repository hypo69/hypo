```rst
.. module: src.webdriver.firefox
```
# Модуль для работы с WebDriver Firefox

Этот модуль содержит класс `Firefox`, который расширяет функциональность стандартного WebDriver для Firefox. Он позволяет настраивать пользовательский профиль, запускать WebDriver в киоске и устанавливать настройки прокси-сервера.

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
        proxy_file_path=proxy_file_path
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Описание классов и методов

### Класс `Firefox`

- Расширяет стандартный WebDriver для Firefox, добавляя функции:
  - Установка пользовательского профиля
  - Прокси-настройки
  - Установка пользовательского агента
  - Интеграция с JavaScript и исполнение локаторов

#### Конструктор `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             *args, **kwargs) -> None:
```

- **profile_name**: Имя пользовательского профиля Firefox.
- **geckodriver_version**: Версия geckodriver.
- **firefox_version**: Версия Firefox.
- **user_agent**: Пользовательский агент.
- **proxy_file_path**: Путь к файлу с прокси.

#### Метод `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
```

- Настроит прокси для Firefox, выбрав случайный рабочий прокси из предоставленного файла.

#### Метод `_payload`

```python
def _payload(self) -> None:
```

- Загружает необходимые исполнительные файлы для локаторов и JavaScript.

## Дополнительные настройки

- **Прокси**: Модуль автоматически выбирает доступный рабочий прокси из файла, который указывается в параметре `proxy_file_path`.
- **Профиль Firefox**: Вы можете указать путь к кастомному профилю для Firefox.
- **Пользовательский агент**: Модуль позволяет задать произвольный пользовательский агент для WebDriver.

## Логирование

Модуль использует `logger` для записи логов, включая ошибки и предупреждения.

## Лицензия

Этот проект лицензируется под лицензией MIT. Подробности см. в файле LICENSE.
