# Модуль `firefox`

## Обзор

Модуль `firefox` предоставляет расширение для `webdriver.Firefox` с дополнительной функциональностью, такой как настройка пользовательского профиля, запуск в различных режимах окна (например, `windowless`, `kiosk`, `full_window`) и установка пользовательских настроек, включая прокси.

## Подробнее

Модуль содержит класс `Firefox`, который наследуется от `webdriver.Firefox`. Он позволяет настраивать параметры запуска браузера Firefox, такие как версия драйвера, версия браузера, пользовательский агент и прокси. Класс также обеспечивает возможность запуска браузера в различных режимах окна и применения пользовательских настроек.

## Классы

### `Firefox`

**Описание**: Расширение для `webdriver.Firefox` с дополнительной функциональностью.

**Как работает класс**:
Класс `Firefox` наследуется от `webdriver.Firefox` и расширяет его функциональность. При инициализации класса происходит следующее:

1.  Загружаются настройки Firefox из файла `firefox.json`.
2.  Определяются пути к `geckodriver` и бинарному файлу Firefox.
3.  Создается объект `Service` для управления `geckodriver`.
4.  Создается объект `Options` для настройки параметров Firefox.
5.  Применяются различные настройки, такие как режим окна, пользовательский агент и прокси.
6.  Инициализируется родительский класс `webdriver.Firefox` с настроенными опциями.
7.  Загружаются исполнители для локаторов и JavaScript сценариев.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `Firefox`.
*   `set_proxy`: Настраивает прокси для Firefox.
*   `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:

*   `profile_name` (Optional[str]): Имя пользовательского профиля Firefox.
*   `geckodriver_version` (Optional[str]): Версия geckodriver.
*   `firefox_version` (Optional[str]): Версия Firefox.
*   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
*   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
*   `options` (Optional[List[str]]): Список опций для Firefox.
*   `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

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

### `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 options: Optional[List[str]] = None,
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
    """"""
```

**Назначение**: Инициализация экземпляра класса `Firefox`.

**Как работает функция**:
Функция выполняет следующие шаги:

1.  Логирует информацию о запуске Firefox WebDriver.
2.  Инициализирует переменные `profile` и `options_obj` в `None`.
3.  Загружает конфигурацию Firefox из файла `firefox.json`.
4.  Определяет пути к исполняемым файлам `geckodriver` и `firefox`.
5.  Инициализирует сервис `geckodriver` с указанным путем.
6.  Создает объект `Options` для настройки Firefox.
7.  Добавляет опции из файла конфигурации, если они есть.
8.  Устанавливает режим окна, если он указан.
9.  Добавляет опции, переданные при инициализации экземпляра класса.
10. Добавляет заголовки из конфигурации, если они есть.
11. Устанавливает User-Agent, используя `fake_useragent`, если он не был передан.
12. Настраивает прокси, если это разрешено в конфигурации.
13. Определяет директорию профиля.
14. Пытается запустить Firefox WebDriver с заданными параметрами.
15. В случае успеха, загружает payload и логирует успешный запуск.
16. В случае неудачи, логирует ошибку и завершает работу.

**Параметры**:

*   `profile_name` (Optional[str]): Имя пользовательского профиля Firefox.
*   `geckodriver_version` (Optional[str]): Версия geckodriver.
*   `firefox_version` (Optional[str]): Версия Firefox.
*   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
*   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
*   `options` (Optional[List[str]]): Список опций для Firefox.
*   `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Вызывает исключения**:

*   `WebDriverException`: Если возникает ошибка при запуске WebDriver.
*   `Exception`: Если возникает любая другая ошибка.

**Примеры**:

```python
browser = Firefox(
    profile_name='custom_profile',
    geckodriver_version='v0.29.0',
    firefox_version='78.0',
    window_mode='kiosk'
)
```

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настройка прокси из словаря, возвращаемого get_proxies_dict.

    :param options: Опции Firefox, в которые добавляются настройки прокси.
    :type options: Options
    """
```

**Назначение**: Настройка прокси для Firefox.

**Как работает функция**:

1.  Получает словарь прокси из функции `get_proxies_dict`.
2.  Создает список всех прокси (socks4 и socks5).
3.  Перебирает прокси в случайном порядке, чтобы найти рабочий.
4.  Проверяет каждый прокси с помощью функции `check_proxy`.
5.  Если рабочий прокси найден, устанавливает настройки прокси в опциях Firefox в зависимости от протокола (http, socks4, socks5).
6.  Если рабочий прокси не найден, логирует предупреждение.

**Параметры**:

*   `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Примеры**:

```python
options = Options()
self.set_proxy(options)
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Загружает исполнителей для локаторов и JavaScript сценариев.
    """
```

**Назначение**: Загрузка исполнителей для локаторов и JavaScript сценариев.

**Как работает функция**:

1.  Создает экземпляр класса `JavaScript`, передавая ему текущий экземпляр `self` (WebDriver).
2.  Назначает функции из экземпляра `JavaScript` атрибутам текущего экземпляра `self`. Это позволяет вызывать JavaScript-функции напрямую из экземпляра `Firefox`.
3.  Создает экземпляр класса `ExecuteLocator`, также передавая текущий экземпляр `self`.
4.  Назначает функцию `execute_locator` из экземпляра `ExecuteLocator` атрибуту `self.execute_locator`. Это позволяет выполнять поиск элементов на странице с использованием локаторов.
5.  Также назначает другие функции для работы с веб-элементами, такие как получение скриншотов и атрибутов.

**Примеры**:

```python
self._payload()
self.get_page_lang()  # Пример вызова JavaScript-функции
self.execute_locator(locator)  # Пример вызова функции для поиска элемента
```