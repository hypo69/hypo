# Модуль `firefox`

## Обзор

Модуль `firefox` предоставляет класс `Firefox`, который расширяет стандартный `webdriver.Firefox` из библиотеки Selenium. Он предназначен для упрощения и расширения работы с браузером Firefox, предоставляя возможности настройки пользовательского профиля, установки параметров запуска, управления прокси и выполнения JavaScript-сценариев.

## Подробней

Этот модуль предназначен для автоматизации взаимодействия с браузером Firefox в проекте `hypotez`. Он позволяет настраивать параметры запуска браузера, такие как пользовательский профиль, прокси и пользовательский агент. Класс `Firefox` наследуется от `selenium.webdriver.Firefox`, добавляя дополнительную функциональность для более удобной работы с браузером в контексте автоматизированного тестирования и сбора данных.

## Классы

### `Firefox`

**Описание**:
Класс `Firefox` расширяет функциональность стандартного `webdriver.Firefox`, предоставляя дополнительные возможности для настройки и управления браузером.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Firefox`, настраивая параметры запуска браузера.
- `set_proxy`: Настраивает прокси для браузера.
- `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
- `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Firefox. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

**Примеры**
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

    :param options: Опции Firefox, в которые добавляются настройки прокси.
    :type options: Options
    """
    ...
```

**Описание**:
Настраивает прокси для браузера Firefox на основе предоставленных опций.

**Параметры**:
- `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Возвращает**:
- `None`

**Примеры**:
```python
    options_obj = Options()
    self.set_proxy(options_obj)
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Загружает исполнителей для локаторов и JavaScript сценариев.
    """
    ...
```

**Описание**:
Загружает и устанавливает исполнителей для локаторов и JavaScript-сценариев, что позволяет выполнять действия с элементами на странице и взаимодействовать с браузером через JavaScript.

**Параметры**:
- Нет

**Возвращает**:
- `None`

**Примеры**:
```python
    self._payload()