# Модуль для работы с WebDriver Firefox

## Обзор

Этот модуль предоставляет класс `Firefox`, расширяющий стандартный WebDriver для Firefox. Он позволяет настраивать пользовательский профиль, работать с прокси-серверами и устанавливать пользовательский User-Agent.

## Требования

- Python 3.12+
- Selenium
- Fake User-Agent
- Модуль для работы с прокси (например, `requests`)

## Установка

1. Установите все зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Убедитесь, что у вас установлены следующие компоненты:
   - **geckodriver**: (для работы с WebDriver) Скачайте и добавьте в PATH.
   - **Firefox**: (поддерживаемая версия)

3. Для работы с прокси, укажите путь к файлу с прокси-серверами через параметр `proxy_file_path`. Файл должен содержать по одному прокси на каждой строке (например, `http://user:pass@proxy_ip:port`).

## Пример использования

```python
from src.webdriver.firefox import Firefox
import os

if __name__ == "__main__":
    # Замените путями на реальные
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    # Важно! Проверьте, что файл proxies.txt существует и содержит валидные прокси.
    if not os.path.exists(proxy_file_path):
        raise FileNotFoundError(f"Файл прокси {proxy_file_path} не найден.")
    
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
  - Установка пользовательского профиля.
  - Настройка прокси-сервера, выбирая случайный рабочий прокси из файла.
  - Установка пользовательского User-Agent.
  - Загрузка необходимых файлов для работы с локаторами и JavaScript.


#### Метод `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             *args, **kwargs) -> None:
    """
    Инициализирует WebDriver для Firefox с опциональными параметрами.

    Args:
        profile_name (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию None.
        geckodriver_version (Optional[str], optional): Версия geckodriver. По умолчанию None.
        firefox_version (Optional[str], optional): Версия Firefox. По умолчанию None.
        user_agent (Optional[str], optional): Пользовательский User-Agent. По умолчанию None.
        proxy_file_path (Optional[str], optional): Путь к файлу с прокси. По умолчанию None.
        *args: Дополнительные аргументы для конструктора WebDriver.
        **kwargs: Дополнительные ключевые аргументы для конструктора WebDriver.

    Raises:
        FileNotFoundError: Если файл с прокси не найден.
        Exception: В случае других ошибок при инициализации.

    """
    # Здесь должна быть реализация инициализации WebDriver
    # с обработкой ошибок
```

#### Метод `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настроит прокси для Firefox, выбрав случайный рабочий прокси из предоставленного файла.

    Args:
        options (Options): Опции для браузера.

    Raises:
        Exception: В случае проблем с чтением или обработкой файла прокси.
    """
    # Здесь должна быть реализация настройки прокси
```

#### Метод `_payload`

```python
def _payload(self) -> None:
    """
    Загружает необходимые исполнительные файлы для локаторов и JavaScript.
    """
    # Здесь должна быть реализация загрузки файлов
```

## Дополнительные настройки

- **Прокси**: Модуль автоматически выбирает доступный рабочий прокси из файла, указанного в параметре `proxy_file_path`.  Необходимо правильно проверить наличие и формат файла.
- **Профиль Firefox**: Вы можете указать путь к кастомному профилю для Firefox, если он отличается.
- **Пользовательский агент**: Модуль позволяет задать произвольный пользовательский агент для WebDriver, используя параметр `user_agent`.

## Логирование

Модуль использует `logging` для записи логов, включая ошибки и предупреждения.  Обязательно реализуйте логирование.

## Лицензия

Этот проект лицензируется под лицензией MIT. Подробности см. в файле LICENSE.