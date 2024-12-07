# Модуль для работы с WebDriver Firefox

## Обзор

Этот модуль предоставляет класс `Firefox`, расширяющий стандартный WebDriver для Firefox. Он позволяет настраивать пользовательский профиль, запускать WebDriver в киоске, устанавливать настройки прокси-сервера и  интегрировать работу с JavaScript и локаторами.

## Требования

- Python 3.12+
- Selenium
- Fake User-Agent
- Модуль для работы с прокси (например, для выбора прокси)


## Установка

1. Установите все зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Убедитесь, что у вас установлены следующие компоненты:
   - **geckodriver** (для работы с WebDriver).  Необходимая версия должна соответствовать версии Firefox.
   - **Firefox** (поддерживаемая версия).
3. Для работы с прокси, укажите путь к файлу с прокси-серверами через параметр `proxy_file_path`.

## Пример использования

```python
from src.webdriver.firefox import Firefox
import os

if __name__ == "__main__":
    profile_name = "custom_profile"  # Имя пользовательского профиля Firefox
    geckodriver_version = "v0.29.0" # Версия geckodriver.  Укажите актуальную.
    firefox_version = "78.0" # Версия Firefox. Укажите актуальную.
    proxy_file_path = "path/to/proxies.txt" # Путь к файлу с прокси.  Создайте файл в указанном пути и заполните его.

    # Важно:  Убедитесь, что путь к файлу с прокси корректен.
    if not os.path.exists(proxy_file_path):
        raise FileNotFoundError(f"Файл прокси не найден по пути: {proxy_file_path}")

    # Инициализация и запуск браузера
    try:
        browser = Firefox(
            profile_name=profile_name,
            geckodriver_version=geckodriver_version,
            firefox_version=firefox_version,
            proxy_file_path=proxy_file_path
        )
        browser.get("https://www.example.com")
        browser.quit()
    except Exception as ex:
        print(f"Ошибка при запуске браузера: {ex}")


```

## Описание классов и методов

### Класс `Firefox`

- Расширяет стандартный WebDriver для Firefox, добавляя функции настройки пользовательского профиля, прокси, пользовательского агента,  интеграции с JavaScript и исполнение локаторов.

#### Конструктор `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             *args, **kwargs) -> None:
    """
    Инициализирует экземпляр класса Firefox.

    Args:
        profile_name (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию None.
        geckodriver_version (Optional[str], optional): Версия geckodriver. По умолчанию None.
        firefox_version (Optional[str], optional): Версия Firefox. По умолчанию None.
        user_agent (Optional[str], optional): Пользовательский агент. По умолчанию None.
        proxy_file_path (Optional[str], optional): Путь к файлу с прокси. По умолчанию None.

    Raises:
        FileNotFoundError: Если файл прокси не найден.
        Exception: В случае других ошибок.
    """
```

#### Метод `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настроит прокси для Firefox, выбрав случайный рабочий прокси из предоставленного файла.

    Args:
        options (Options): Объект настроек Firefox.

    Raises:
        Exception: Если возникла ошибка при получении прокси.
    """
```

#### Метод `_payload`

```python
def _payload(self) -> None:
    """
    Загружает необходимые исполнительные файлы для локаторов и JavaScript.
    """
```

## Дополнительные настройки

- **Прокси**: Модуль автоматически выбирает доступный рабочий прокси из файла, указанного в `proxy_file_path`.  **Не забудьте создать файл прокси и заполнить его.**
- **Профиль Firefox**:  Вы можете указать путь к кастомному профилю Firefox.  Обратите внимание на корректность пути.
- **Пользовательский агент**: Модуль позволяет задать произвольный пользовательский агент для WebDriver.


## Логирование

Модуль использует `logging` для записи логов, включая ошибки и предупреждения.  Добавьте логирование в ваш код.

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле LICENSE.