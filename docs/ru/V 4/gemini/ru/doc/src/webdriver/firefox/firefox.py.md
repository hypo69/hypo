# Модуль `firefox`

## Обзор

Модуль `firefox` предназначен для работы с браузером Firefox через WebDriver. Он расширяет стандартный функционал `selenium.webdriver.Firefox`, предоставляя дополнительные возможности, такие как настройка пользовательского профиля, запуск в режиме киоска, установка пользовательских настроек (включая прокси) и добавление JavaScript-методов для взаимодействия со страницей.

## Подробней

Модуль предоставляет класс `Firefox`, который наследуется от `selenium.webdriver.Firefox`. Это позволяет использовать все стандартные методы и свойства WebDriver, а также добавляет новые, специфичные для данного проекта.

Класс `Firefox` позволяет настраивать различные параметры запуска браузера, такие как:

-   Имя профиля пользователя
-   Версия `geckodriver` и `firefox`
-   Пользовательский `user_agent`
-   Настройки прокси
-   Режим окна (например, `windowless`, `kiosk` или `full_window`)

Эти настройки позволяют гибко конфигурировать браузер для различных задач, таких как тестирование, сбор данных и автоматизация.

## Классы

### `Firefox`

**Описание**: Класс `Firefox` расширяет `selenium.webdriver.Firefox` и предоставляет дополнительные возможности для настройки и управления браузером Firefox.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `Firefox`, настраивает параметры запуска браузера.
-   `set_proxy`: Настраивает прокси для Firefox из словаря, полученного из `get_proxies_dict`.
-   `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:

-   `profile_name` (Optional[str]): Имя пользовательского профиля Firefox.
-   `geckodriver_version` (Optional[str]): Версия `geckodriver`.
-   `firefox_version` (Optional[str]): Версия Firefox.
-   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
-   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
-   `options` (Optional[List[str]]): Список опций для Firefox.
-   `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

**Примеры**:

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

## Функции

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настройка прокси из словаря, возвращаемого get_proxies_dict.

    Args:
        options (Options): Опции Firefox, в которые добавляются настройки прокси.

    Returns:
        None

    Raises:
        None
    """
    ...
```

**Описание**: Метод `set_proxy` настраивает прокси для браузера Firefox. Он получает словарь прокси из функции `get_proxies_dict`, выбирает случайный рабочий прокси и устанавливает его в опции браузера. Поддерживаются протоколы `http`, `socks4` и `socks5`.

**Параметры**:

-   `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Примеры**:

```python
options = Options()
firefox_instance = Firefox()
firefox_instance.set_proxy(options)
```

### `_payload`

```python
def _payload(self) -> None:
     """
    Загружает исполнителей для локаторов и JavaScript сценариев.
     """
     ...
```

**Описание**: Метод `_payload` загружает исполнителей для локаторов и JavaScript сценариев. Он инициализирует класс `JavaScript` и `ExecuteLocator`, а затем добавляет методы этих классов в экземпляр `Firefox`. Это позволяет выполнять JavaScript код и искать элементы на странице с использованием локаторов.

**Примеры**:

```python
firefox_instance = Firefox()
firefox_instance._payload()
firefox_instance.get_page_lang()