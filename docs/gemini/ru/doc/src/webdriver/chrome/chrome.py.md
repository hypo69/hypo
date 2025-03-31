# Модуль `chrome`

## Обзор

Модуль `chrome` представляет собой расширение для `webdriver.Chrome` с дополнительной функциональностью. Он предназначен для упрощения и расширения возможностей управления браузером Chrome с использованием Selenium WebDriver. Модуль позволяет настраивать профили пользователей, управлять прокси, устанавливать пользовательские агенты и выполнять JavaScript-сценарии.

## Подробней

Этот модуль предоставляет класс `Chrome`, который наследуется от `selenium.webdriver.Chrome`. Он позволяет инициализировать и настраивать Chrome WebDriver с различными параметрами, такими как профиль пользователя, версия chromedriver, пользовательский агент, прокси и опции запуска. Модуль также включает функции для выполнения JavaScript-кода и работы с элементами на веб-странице. Расположение файла в проекте указывает на то, что он является частью подсистемы управления веб-драйвером, отвечающей за взаимодействие с браузером Chrome.

## Классы

### `Chrome`

**Описание**: Расширение для `webdriver.Chrome` с дополнительной функциональностью.

**Как работает класс**:

Класс `Chrome` наследуется от `selenium.webdriver.Chrome` и расширяет его функциональность. При инициализации класса происходит следующее:

1.  Загружаются настройки из файла `chrome.json`, который содержит пути к исполняемому файлу chromedriver, опции Chrome и другие параметры.
2.  Инициализируется сервис `chromedriver` с указанным путем.
3.  Создается объект `Options` для настройки опций Chrome.
4.  Устанавливаются различные опции, такие как режим окна, пользовательский агент и прокси.
5.  Настраивается директория профиля пользователя Chrome.
6.  Запускается Chrome WebDriver с заданными параметрами.
7.  Загружаются исполнители для локаторов и JavaScript сценариев.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `Chrome` с заданными параметрами.
*   `set_proxy`: Настраивает прокси для Chrome из словаря, возвращаемого `get_proxies_dict`.
*   `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:

*   `profile_name` (Optional[str]): Имя пользовательского профиля Chrome.
*   `chromedriver_version` (Optional[str]): Версия chromedriver.
*   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
*   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
*   `options` (Optional[List[str]]): Список опций для Chrome.
*   `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Запуск Chrome в полноэкранном режиме
driver = Chrome(window_mode='full_window')
driver.get("https://google.com")
```

## Функции

### `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             chromedriver_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             options: Optional[List[str]] = None,
             window_mode: Optional[str] = None,
             *args, **kwargs) -> None:
    """
    Инициализирует экземпляр класса `Chrome` с заданными параметрами.

    Args:
        profile_name (Optional[str], optional): Имя пользовательского профиля Chrome. По умолчанию `None`.
        chromedriver_version (Optional[str], optional): Версия chromedriver. По умолчанию `None`.
        user_agent (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
        proxy_file_path (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
        options (Optional[List[str]], optional): Список опций для Chrome. По умолчанию `None`.
        window_mode (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

    Raises:
        WebDriverException: Если возникает ошибка при запуске WebDriver.
        Exception: Если возникает общая ошибка при работе Chrome WebDriver.
    """
    # объявление переменных
    service = None
    options_obj = None

    # Загрузка настроек Chrome
    config = j_loads_ns(Path(gs.path.src / 'webdriver' / 'chrome' / 'chrome.json'))

    # Путь к chromedriver
    chromedriver_path: str = str(Path(gs.path.root, config.executable_path.chromedriver))

     # Инициализация сервиса
    service = Service(chromedriver_path)

    # Настройка опций Chrome
    options_obj = Options()

    #  Добавление опций из файла настроек
    if hasattr(config, 'options') and config.options:
        for option in config.options:
            options_obj.add_argument(option)

    #  Установка режима окна из конфига
    if hasattr(config, 'window_mode') and config.window_mode:
        window_mode = window_mode or config.window_mode
    #  Установка режима окна из параметров
    if window_mode:
        if window_mode == 'kiosk':
            options_obj.add_argument("--kiosk")
        elif window_mode == 'windowless':
           options_obj.add_argument("--headless")
        elif window_mode == 'full_window':
             options_obj.add_argument("--start-maximized")


    #  Добавление опций, переданных при инициализации
    if options:
        for option in options:
            options_obj.add_argument(option)


    # Установка пользовательского агента
    user_agent = user_agent or UserAgent().random
    options_obj.add_argument(f'--user-agent={user_agent}')

    # Установка прокси, если включены
    if hasattr(config, 'proxy_enabled') and config.proxy_enabled:
         self.set_proxy(options_obj)


    # Настройка директории профиля
    profile_directory = config.profile_directory.os if config.profile_directory.default == 'os' else str(Path(gs.path.src, config.profile_directory.internal))

    if profile_name:
         profile_directory = str(Path(profile_directory).parent / profile_name)
    if '%LOCALAPPDATA%' in profile_directory:
          profile_directory = Path(profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA')))
    options_obj.add_argument(f"--user-data-dir={profile_directory}")
    try:
        logger.info('Запуск Chrome WebDriver')
        super().__init__(service=service, options=options_obj)
        self._payload()
    except WebDriverException as ex:
            logger.critical("""
                ---------------------------------
                    Ошибка запуска WebDriver
                    Возможные причины:
                    - Обновление Chrome
                    - Отсутствие Chrome на ОС
                ----------------------------------""", ex)
            return  # Явный возврат при ошибке
    except Exception as ex:
        logger.critical('Ошибка работы Chrome WebDriver:', ex)
        return  # Явный возврат при ошибке
```

**Как работает функция**:

Функция инициализирует класс `Chrome`, настраивая параметры запуска браузера Chrome. Сначала загружаются параметры конфигурации из файла `chrome.json`. Затем создается объект `Service` для управления процессом `chromedriver`, и объект `Options` для установки различных параметров Chrome. Устанавливаются опции, такие как режим окна (kiosk, windowless, full\_window), пользовательский агент и прокси. Настраивается директория профиля пользователя Chrome. В случае возникновения исключений `WebDriverException` или `Exception`, они логируются с использованием `logger.critical`, и функция завершается. В конце вызывается метод `_payload` для загрузки исполнителей локаторов и JavaScript сценариев.

**Параметры**:

*   `profile_name` (Optional[str]): Имя пользовательского профиля Chrome.
*   `chromedriver_version` (Optional[str]): Версия chromedriver.
*   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
*   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
*   `options` (Optional[List[str]]): Список опций для Chrome.
*   `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

**Вызывает исключения**:

*   `WebDriverException`: Возникает, если есть проблемы с запуском Chrome WebDriver (например, несовместимая версия Chrome или Chromedriver).
*   `Exception`: Возникает при других ошибках во время настройки и запуска Chrome WebDriver.

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Инициализация Chrome WebDriver с пользовательским профилем и полноэкранным режимом
driver = Chrome(profile_name='MyProfile', window_mode='full_window')
driver.get("https://www.google.com")
```

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настраивает прокси для Chrome из словаря, возвращаемого get_proxies_dict.

    Args:
        options (Options): Опции Chrome, в которые добавляются настройки прокси.
    """
    # Получение словаря прокси
    proxies_dict = get_proxies_dict()
    # Создание списка всех прокси
    all_proxies = proxies_dict.get('socks4', []) + proxies_dict.get('socks5', [])
    # Перебор прокси для поиска рабочего
    working_proxy = None
    for proxy in random.sample(all_proxies, len(all_proxies)):
        if check_proxy(proxy):
            working_proxy = proxy
            break
     # Настройка прокси, если он найден
    if working_proxy:
        proxy = working_proxy
        protocol = proxy.get('protocol')
        # Настройка прокси в зависимости от протокола
        if protocol == 'http':
            options.add_argument(f'--proxy-server=http://{proxy["host"]}:{proxy["port"]}')
            logger.info(f"Настройка HTTP Proxy: http://{proxy['host']}:{proxy['port']}")

        elif protocol == 'socks4':
             options.add_argument(f'--proxy-server=socks4://{proxy["host"]}:{proxy["port"]}')
             logger.info(f"Настройка SOCKS4 Proxy: {proxy['host']}:{proxy['port']}")

        elif protocol == 'socks5':
            options.add_argument(f'--proxy-server=socks5://{proxy["host"]}:{proxy["port"]}')
            logger.info(f"Настройка SOCKS5 Proxy: {proxy['host']}:{proxy['port']}")
        else:
             logger.warning(f"Неизвестный тип прокси: {protocol}")
    else:
        logger.warning('Нет доступных прокси в предоставленном файле.')
```

**Как работает функция**:

Функция `set_proxy` настраивает прокси для Chrome, используя список прокси, полученный из `get_proxies_dict`. Она случайным образом выбирает прокси из списка и проверяет его работоспособность с помощью функции `check_proxy`. Если рабочий прокси найден, он добавляется в опции Chrome в зависимости от протокола (HTTP, SOCKS4, SOCKS5). Если рабочий прокси не найден, функция записывает предупреждение в лог.

**Параметры**:

*   `options` (Options): Опции Chrome, в которые добавляются настройки прокси.

**Примеры**:

```python
from selenium.webdriver.chrome.options import Options
from src.webdriver.chrome.chrome import Chrome

# Создание объекта Options и настройка прокси
options = Options()
chrome = Chrome()
chrome.set_proxy(options)

# Инициализация Chrome WebDriver с настроенными опциями
driver = Chrome(options=options)
driver.get("https://www.google.com")
```

### `_payload`

```python
def _payload(self) -> None:
     """
    Загружает исполнителей для локаторов и JavaScript сценариев.
     """
     j = JavaScript(self)
     self.get_page_lang = j.get_page_lang
     self.ready_state = j.ready_state
     self.get_referrer = j.ready_state
     self.unhide_DOM_element = j.unhide_DOM_element
     self.window_focus = j.window_focus

     execute_locator = ExecuteLocator(self)
     self.execute_locator = execute_locator.execute_locator
     self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
     self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
     self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
     self.send_message = self.send_key_to_webelement = execute_locator.send_message
```

**Как работает функция**:

Функция `_payload` загружает и присваивает методы из классов `JavaScript` и `ExecuteLocator` экземпляру класса `Chrome`. Это позволяет использовать JavaScript-сценарии и выполнять действия с элементами на веб-странице. В частности, она инициализирует экземпляр класса `JavaScript` и присваивает его методы, такие как `get_page_lang`, `ready_state`, `get_referrer`, `unhide_DOM_element` и `window_focus`, экземпляру класса `Chrome`. Затем она инициализирует экземпляр класса `ExecuteLocator` и присваивает его методы, такие как `execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator` и `get_attribute_by_locator`, экземпляру класса `Chrome`.

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Инициализация Chrome WebDriver
driver = Chrome()

# Загрузка исполнителей
driver._payload()

# Использование загруженных методов
page_lang = driver.get_page_lang()