# Модуль `firefox.py`

## Обзор

Модуль предназначен для расширения стандартного функционала `webdriver.Firefox` и предоставляет класс `Firefox` для настройки и управления браузером Firefox. Он включает в себя возможности для управления профилем, установки пользовательских настроек, прокси и запуска браузера в различных режимах отображения.

## Подробней

Этот модуль предоставляет класс `Firefox`, который позволяет автоматизировать управление браузером Firefox с использованием Selenium WebDriver. Он упрощает настройку параметров браузера, таких как профиль пользователя, прокси и различные опции запуска. Модуль также обрабатывает исключения, которые могут возникнуть при запуске WebDriver, и предоставляет удобные методы для выполнения JavaScript-кода и поиска элементов на веб-странице.

## Классы

### `Firefox`

**Описание**:
Класс `Firefox` расширяет `webdriver.Firefox` и предоставляет дополнительную функциональность для настройки и управления браузером Firefox.

**Как работает класс**:
Класс инициализирует WebDriver Firefox с заданными параметрами, такими как профиль, версия, пользовательский агент и прокси. Он также позволяет устанавливать различные опции запуска браузера, включая режимы отображения (например, `windowless`, `kiosk`, `full_window`). В конструкторе класса происходит загрузка конфигурации из файла `firefox.json`, настройка опций Firefox, установка пользовательского агента и прокси, а также инициализация экземпляра WebDriver.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Firefox` и настраивает WebDriver.
- `set_proxy`: Настраивает прокси для Firefox из словаря прокси.
- `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
- `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Firefox. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор `WebDriver`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор `WebDriver`.

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

    :param options: Опции Firefox, в которые добавляются настройки прокси.
    :type options: Options
    """
    ...
```

**Как работает функция**:
Функция `set_proxy` настраивает прокси для Firefox. Сначала она получает словарь прокси из функции `get_proxies_dict`. Затем она перебирает прокси, чтобы найти рабочий прокси, используя функцию `check_proxy`. Если рабочий прокси найден, функция устанавливает соответствующие настройки прокси в опциях Firefox в зависимости от протокола прокси (HTTP, SOCKS4, SOCKS5).

**Параметры**:
- `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют явные исключения, но функция логирует предупреждения, если нет доступных прокси или если тип прокси неизвестен.

**Примеры**:

```python
# Пример вызова функции set_proxy
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

**Как работает функция**:
Функция `_payload` загружает исполнителей для локаторов и JavaScript сценариев, используемых в классе `Firefox`. Она инициализирует класс `JavaScript` и присваивает его методы атрибутам экземпляра класса `Firefox`, таким как `get_page_lang`, `ready_state`, `get_referrer`, `unhide_DOM_element` и `window_focus`. Также инициализируется класс `ExecuteLocator`, и его методы, такие как `execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`, `get_attribute_by_locator` и `send_message`, присваиваются атрибутам экземпляра класса `Firefox`.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
# Пример вызова функции _payload
firefox_instance = Firefox()
firefox_instance._payload()
```