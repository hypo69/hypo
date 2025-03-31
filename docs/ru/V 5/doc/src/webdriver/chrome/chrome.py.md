# Модуль `chrome`

## Обзор

Модуль `chrome` предоставляет расширение для `webdriver.Chrome` с дополнительной функциональностью. Он позволяет настраивать Chrome WebDriver с использованием различных опций, таких как профили пользователей, прокси и пользовательские агенты. Модуль также включает функции для выполнения JavaScript и работы с элементами DOM.

## Подробней

Этот модуль предназначен для упрощения настройки и управления Chrome WebDriver в проекте `hypotez`. Он автоматизирует процесс установки опций Chrome, таких как пользовательские профили, прокси и пользовательские агенты, что позволяет легко настраивать браузер для различных задач. Модуль также предоставляет функции для выполнения JavaScript и работы с элементами DOM, что упрощает автоматизацию веб-сайтов.

## Классы

### `Chrome`

**Описание**: Расширение для `webdriver.Chrome` с дополнительной функциональностью.

**Как работает класс**:
Класс `Chrome` наследуется от `selenium.webdriver.Chrome` и добавляет дополнительную функциональность для настройки и управления Chrome WebDriver. Он принимает различные параметры, такие как имя профиля, версия chromedriver, пользовательский агент, путь к файлу прокси и опции Chrome. Класс также настраивает прокси, если они включены, и устанавливает директорию профиля.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Chrome`.
- `set_proxy`: Настраивает прокси из словаря, возвращаемого `get_proxies_dict`.
- `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `profile_name` (Optional[str]): Имя пользовательского профиля Chrome.
- `chromedriver_version` (Optional[str]): Версия chromedriver.
- `user_agent` (Optional[str]): Пользовательский агент в формате строки.
- `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
- `options` (Optional[List[str]]): Список опций для Chrome.
- `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Инициализация Chrome WebDriver с пользовательским профилем
driver = Chrome(profile_name='my_profile', window_mode='full_window')
driver.get("https://www.google.com")
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
    Инициализирует экземпляр класса `Chrome`.

    Args:
        profile_name (Optional[str], optional): Имя пользовательского профиля Chrome. По умолчанию `None`.
        chromedriver_version (Optional[str], optional): Версия chromedriver. По умолчанию `None`.
        user_agent (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
        proxy_file_path (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
        options (Optional[List[str]], optional): Список опций для Chrome. По умолчанию `None`.
        window_mode (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

    Returns:
        None

    Raises:
        WebDriverException: Если возникает ошибка при запуске WebDriver.
        Exception: Если возникает общая ошибка при работе Chrome WebDriver.

    Example:
        >>> driver = Chrome(profile_name='my_profile', window_mode='full_window')
    """
```

**Описание**: Инициализирует экземпляр класса `Chrome`.

**Как работает функция**:
1. **Инициализация переменных**: Объявляются переменные `service` и `options_obj` для хранения сервиса и опций Chrome соответственно.
2. **Загрузка конфигурации Chrome**: Загружаются настройки Chrome из файла `chrome.json` с использованием функции `j_loads_ns`.
3. **Путь к ChromeDriver**: Формируется путь к исполняемому файлу ChromeDriver на основе конфигурации.
4. **Инициализация сервиса**: Создается экземпляр сервиса ChromeDriver с использованием указанного пути.
5. **Настройка опций Chrome**: Создается объект опций Chrome.
6. **Добавление опций из конфигурации**: Если в конфигурации указаны опции, они добавляются к объекту опций.
7. **Установка режима окна**: Устанавливается режим окна из конфигурации или параметров, переданных при инициализации. Поддерживаются режимы `kiosk`, `windowless` и `full_window`.
8. **Добавление опций из параметров**: Если при инициализации переданы дополнительные опции, они добавляются к объекту опций.
9. **Установка пользовательского агента**: Устанавливается пользовательский агент из параметров, переданных при инициализации, или генерируется случайный пользовательский агент с использованием библиотеки `fake_useragent`.
10. **Установка прокси**: Если в конфигурации включены прокси, вызывается метод `set_proxy` для настройки прокси.
11. **Настройка директории профиля**: Настраивается директория профиля на основе конфигурации и параметров, переданных при инициализации.
12. **Запуск WebDriver**: Запускается Chrome WebDriver с использованием настроенного сервиса и опций.
13. **Обработка исключений**: Обрабатываются исключения, которые могут возникнуть при запуске WebDriver или работе Chrome WebDriver. В случае ошибки регистрируется критическое сообщение и возвращается `None`.
14. **Загрузка payload**: Вызывается метод `_payload` для загрузки исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Chrome. По умолчанию `None`.
- `chromedriver_version` (Optional[str], optional): Версия chromedriver. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Chrome. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, которые будут переданы в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, которые будут переданы в конструктор родительского класса.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка при запуске WebDriver.
- `Exception`: Если возникает общая ошибка при работе Chrome WebDriver.

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Инициализация Chrome WebDriver с пользовательским профилем и режимом окна
driver = Chrome(profile_name='my_profile', window_mode='full_window')
```

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настраивает прокси из словаря, возвращаемого get_proxies_dict.

    Args:
        options (Options): Опции Chrome, в которые добавляются настройки прокси.

    Returns:
        None

    Example:
        >>> chrome_instance = Chrome()
        >>> options = Options()
        >>> chrome_instance.set_proxy(options)
    """
```

**Описание**: Настраивает прокси из словаря, возвращаемого `get_proxies_dict`.

**Как работает функция**:
1. **Получение словаря прокси**: Получает словарь прокси с использованием функции `get_proxies_dict`.
2. **Создание списка всех прокси**: Создает список всех прокси из словаря, объединяя прокси socks4 и socks5.
3. **Перебор прокси для поиска рабочего**: Перебирает прокси в случайном порядке для поиска рабочего прокси с использованием функции `check_proxy`.
4. **Настройка прокси, если он найден**: Если рабочий прокси найден, настраивает прокси в зависимости от протокола (http, socks4, socks5) и добавляет соответствующие аргументы в опции Chrome.
5. **Логирование**: Логирует информацию о настроенном прокси или предупреждение, если прокси не найден.

**Параметры**:
- `options` (Options): Опции Chrome, в которые добавляются настройки прокси.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
from selenium.webdriver.chrome.options import Options
from src.webdriver.chrome.chrome import Chrome

# Создание экземпляра Chrome и настройка прокси
chrome_instance = Chrome()
options = Options()
chrome_instance.set_proxy(options)
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Загружает исполнителей для локаторов и JavaScript сценариев.

    Returns:
        None

    Example:
        >>> chrome_instance = Chrome()
        >>> chrome_instance._payload()
    """
```

**Описание**: Загружает исполнителей для локаторов и JavaScript сценариев.

**Как работает функция**:
1. **Инициализация JavaScript**: Создает экземпляр класса `JavaScript`, передавая текущий экземпляр `Chrome` в качестве аргумента.
2. **Присвоение JavaScript функций**: Присваивает методы экземпляра `JavaScript` текущему экземпляру `Chrome`, чтобы их можно было вызывать напрямую.
3. **Инициализация ExecuteLocator**: Создает экземпляр класса `ExecuteLocator`, передавая текущий экземпляр `Chrome` в качестве аргумента.
4. **Присвоение методов ExecuteLocator**: Присваивает методы экземпляра `ExecuteLocator` текущему экземпляру `Chrome`, чтобы их можно было вызывать напрямую.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Создание экземпляра Chrome и загрузка payload
chrome_instance = Chrome()
chrome_instance._payload()
```