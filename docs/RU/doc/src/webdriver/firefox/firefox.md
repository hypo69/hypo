# Модуль `hypotez/src/webdriver/firefox/firefox.py`

## Обзор

Этот модуль предоставляет класс `Firefox`, расширяющий стандартный `webdriver.Firefox`. Он позволяет настраивать пользовательский профиль, запускать браузер в режиме киоска и устанавливать пользовательские настройки, включая прокси.

## Классы

### `Firefox`

**Описание**: Расширенный класс для работы с WebDriver Firefox, предоставляющий дополнительные возможности настройки и функциональности.

**Параметры инициализации**:

- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
- `geckodriver_version` (Optional[str], optional): Версия `geckodriver`. По умолчанию `None`.
- `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент (строка). По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.


**Методы**:

- `__init__(self, profile_name: Optional[str] = None, geckodriver_version: Optional[str] = None, firefox_version: Optional[str] = None, user_agent: Optional[str] = None, proxy_file_path: Optional[str] = None, *args, **kwargs) -> None`:
    **Описание**: Инициализирует драйвер WebDriver Firefox. Загружает настройки из `firefox.json`, настраивает прокси и профиль, устанавливает пользовательский агент.
    **Возвращает**: `None`
    **Обрабатывает исключения**:
    - `WebDriverException`: Возникает при ошибках запуска WebDriver (обновление Firefox, отсутствие Firefox на ОС).
    - `Exception`: Возникает при других ошибках во время работы с WebDriver.
- `set_proxy(self, options: Options) -> None`:
    **Описание**: Настраивает прокси в соответствии с полученным словарем прокси.
    **Параметры**:
      - `options (Options)`: Объект настроек Firefox.
    **Возвращает**: `None`


- `_payload(self) -> None`:
    **Описание**: Загружает исполнители для локейторов и JavaScript-сценариев.
    **Возвращает**: `None`



## Функции

(Здесь описываются функции, если они есть в файле, кроме `__init__` и `set_proxy`).


## Константы

(Если есть)


## Модули

(Если есть)


## Использование

(Пример использования класса `Firefox`)

```python
if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    browser = Firefox(
        profile_name=profile_name,
        geckodriver_version=geckodriver_version,
        firefox_version=firefox_version,
        proxy_file_path=proxy_file_path
    )
    browser.get("https://www.example.com")
    browser.quit()
```