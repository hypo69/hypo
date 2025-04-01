# Модуль `firefox`

## Обзор

Модуль `firefox` предоставляет класс `Firefox`, который расширяет функциональность стандартного `webdriver.Firefox` из библиотеки Selenium. Он предназначен для упрощения настройки и управления экземплярами браузера Firefox, включая установку пользовательских профилей, прокси и пользовательских настроек.

## Подробней

Этот модуль предоставляет удобный способ настройки браузера Firefox для автоматизированного тестирования или сбора данных. Он позволяет указывать пользовательский профиль, версию geckodriver и Firefox, а также настраивать прокси и другие параметры.
Расположение файла в проекте `hypotez` указывает на то, что он является частью подсистемы, отвечающей за взаимодействие с браузером Firefox через WebDriver.

## Классы

### `Firefox`

**Описание**: Класс `Firefox` наследуется от `selenium.webdriver.Firefox` и предоставляет расширенные возможности по настройке браузера Firefox.

**Принцип работы**:
1.  Загружает конфигурацию Firefox из файла `firefox.json`.
2.  Устанавливает путь к исполняемым файлам `geckodriver` и `firefox`.
3.  Создает объект `Options` и добавляет опции, указанные в конфигурационном файле и переданные при инициализации.
4.  Настраивает пользовательский агент и прокси, если это указано в конфигурации.
5.  Создает профиль Firefox с указанным именем и настройками.
6.  Инициализирует экземпляр `webdriver.Firefox` с заданными опциями и профилем.
7.  Загружает исполнителей для локаторов и JavaScript сценариев.

**Аттрибуты**:

*   `driver_name` (str): Имя драйвера (`firefox`).
*   `service` (Service): Сервис WebDriver для Firefox.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `Firefox` с заданными параметрами.
*   `set_proxy`: Настраивает прокси для Firefox.
*   `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

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

**Назначение**: Инициализирует экземпляр класса `Firefox` и настраивает WebDriver.

**Параметры**:

*   `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
*   `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
*   `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
*   `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
*   `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
*   `options` (Optional[List[str]], optional): Список опций для Firefox. По умолчанию `None`.
*   `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Как работает функция**:

1.  Инициализирует логгирование запуска Firefox WebDriver.
2.  Объявляет переменные `profile` и `options_obj` как `None`.
3.  Загружает настройки Firefox из файла `firefox.json` с использованием `j_loads_ns`.
4.  Определяет пути к `geckodriver` и бинарному файлу Firefox на основе загруженной конфигурации.
5.  Инициализирует сервис `geckodriver`.
6.  Создает объект `Options` для настройки Firefox.
7.  Добавляет опции из файла настроек, если они есть.
8.  Устанавливает режим окна браузера, если указан.
9.  Добавляет опции, переданные при инициализации.
10. Добавляет заголовки из настроек.
11. Устанавливает пользовательский агент.
12. Устанавливает прокси, если включены в конфигурации.
13. Настраивает директорию профиля.
14. Пытается запустить Firefox WebDriver с заданными параметрами.
15. Вызывает метод `_payload` для загрузки исполнителей локаторов и JavaScript.
16. Обрабатывает исключения, возникающие при запуске WebDriver, и логирует ошибки.

```
Загрузка конфига -> Определение путей -> Инициализация сервиса -> Создание Options -> Добавление опций ->
Установка UserAgent -> Установка Proxy -> Настройка Profile directory -> Запуск WebDriver -> Загрузка Payload
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

**Назначение**: Настраивает прокси для Firefox на основе данных из словаря прокси.

**Параметры**:

*   `options` (Options): Объект опций Firefox, в который будут добавлены настройки прокси.

**Как работает функция**:

1.  Получает словарь прокси, используя функцию `get_proxies_dict`.
2.  Создает список всех доступных прокси из полученного словаря (SOCKS4 и SOCKS5).
3.  Перебирает прокси в случайном порядке, чтобы найти рабочий прокси.
4.  Проверяет каждый прокси с помощью функции `check_proxy`.
5.  Если рабочий прокси найден, настраивает параметры прокси в объекте `options` в зависимости от протокола (HTTP, SOCKS4 или SOCKS5).
6.  Если рабочий прокси не найден, выводит предупреждение в лог.

```
Получение словаря прокси -> Создание списка прокси -> Поиск рабочего прокси ->
Настройка параметров прокси в Options -> Логгирование
```

### `_payload`
```python
    def _payload(self) -> None:
         """
        Загружает исполнителей для локаторов и JavaScript сценариев.
         """
```

**Назначение**: Загружает исполнителей для локаторов и JavaScript сценариев, используемых в WebDriver.

**Как работает функция**:

1.  Создает экземпляр класса `JavaScript`, передавая текущий экземпляр `Firefox` в качестве аргумента.
2.  Присваивает атрибуты экземпляра `JavaScript` (например, `get_page_lang`, `ready_state`, `get_referrer`) текущему экземпляру `Firefox`.
3.  Создает экземпляр класса `ExecuteLocator`, передавая текущий экземпляр `Firefox` в качестве аргумента.
4.  Присваивает методы экземпляра `ExecuteLocator` (например, `execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`) текущему экземпляру `Firefox`.

```
Создание экземпляра JavaScript -> Присваивание атрибутов JavaScript ->
Создание экземпляра ExecuteLocator -> Присваивание методов ExecuteLocator
```

## Примеры

Пример использования класса `Firefox`:

```python
if __name__ == "__main__":
    driver = Firefox()
    driver.get(r"https://google.com")
```
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