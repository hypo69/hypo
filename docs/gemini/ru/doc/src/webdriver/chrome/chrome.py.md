# Модуль `chrome`

## Обзор

Модуль `chrome` предназначен для работы с веб-драйвером Chrome, предоставляя расширенные функциональности, такие как управление профилем, настройка прокси и выполнение JavaScript.

## Подробнее

Модуль расширяет стандартный `webdriver.Chrome` из библиотеки Selenium, добавляя возможность настройки пользовательского профиля, установки прокси и выполнения JavaScript-сценариев. Он также обрабатывает исключения, возникающие при запуске и работе веб-драйвера Chrome.

## Классы

### `Chrome`

**Описание**: Класс `Chrome` наследуется от `selenium.webdriver.Chrome` и предоставляет расширенные возможности для управления браузером Chrome.

**Принцип работы**:

1.  **Инициализация**: При инициализации класса загружаются конфигурации Chrome из файла `chrome.json`, устанавливаются параметры chromedriver, настраиваются опции Chrome, устанавливается пользовательский агент и прокси, а также настраивается директория профиля.

2.  **Настройка прокси**: Если в конфигурационном файле включена опция `proxy_enabled`, вызывается метод `set_proxy` для настройки прокси.

3.  **Запуск WebDriver**: В блоке `try` запускается WebDriver с заданными параметрами. В случае возникновения исключений `WebDriverException` или `Exception`, они логируются, и выполнение функции прекращается.

4.  **Загрузка исполнителей**: После успешного запуска WebDriver вызывается метод `_payload` для загрузки исполнителей локаторов и JavaScript-сценариев.

**Наследует**:

*   `selenium.webdriver.Chrome`

**Атрибуты**:

*   `driver_name` (str): Имя драйвера, установлено как `'chrome'`.
*   `profile_name` (Optional[str]): Имя пользовательского профиля Chrome.
*   `chromedriver_version` (Optional[str]): Версия chromedriver.
*   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
*   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
*   `options` (Optional[List[str]]): Список опций для Chrome.
*   `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `Chrome` с заданными параметрами.
*   `set_proxy`: Настраивает прокси из словаря, возвращаемого функцией `get_proxies_dict`.
*   `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

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
    Инициализирует экземпляр класса Chrome с заданными параметрами.

    Args:
        profile_name (Optional[str], optional): Имя пользовательского профиля Chrome. По умолчанию None.
        chromedriver_version (Optional[str], optional): Версия chromedriver. По умолчанию None.
        user_agent (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию None.
        proxy_file_path (Optional[str], optional): Путь к файлу с прокси. По умолчанию None.
        options (Optional[List[str]], optional): Список опций для Chrome. По умолчанию None.
        window_mode (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию None.
        *args: Произвольные позиционные аргументы.
        **kwargs: Произвольные именованные аргументы.
    """
```

**Назначение**: Инициализация экземпляра класса `Chrome`.

**Параметры**:

*   `profile_name` (Optional[str]): Имя пользовательского профиля Chrome.
*   `chromedriver_version` (Optional[str]): Версия chromedriver.
*   `user_agent` (Optional[str]): Пользовательский агент в формате строки.
*   `proxy_file_path` (Optional[str]): Путь к файлу с прокси.
*   `options` (Optional[List[str]]): Список опций для Chrome.
*   `window_mode` (Optional[str]): Режим окна браузера.
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Как работает функция**:

1.  **Загрузка конфигурации**: Загружает конфигурацию Chrome из файла `chrome.json` с использованием `j_loads_ns`.
2.  **Определение путей**: Определяет путь к исполняемому файлу chromedriver на основе конфигурации.
3.  **Инициализация сервиса и опций**: Инициализирует сервис Chrome и опции Chrome.
4.  **Настройка опций**: Добавляет опции из конфигурационного файла и переданные при инициализации. Устанавливает режим окна браузера (kiosk, windowless, full_window).
5.  **Установка User-Agent**: Устанавливает User-Agent, либо случайный, либо переданный при инициализации.
6.  **Настройка прокси**: Если включена опция `proxy_enabled` в конфигурации, настраивает прокси.
7.  **Настройка профиля**: Настраивает директорию профиля пользователя Chrome.
8.  **Инициализация WebDriver**: Запускает WebDriver с заданными параметрами.
9.  **Обработка исключений**: Обрабатывает исключения, которые могут возникнуть при запуске WebDriver, логирует их и завершает выполнение.
10. **Загрузка исполнителей**: Если WebDriver успешно запущен, вызывает метод `_payload` для загрузки исполнителей.

**ASII flowchart**:

```
Загрузка конфигурации --> Определение путей --> Инициализация сервиса и опций --> Настройка опций
    ↓
Установка User-Agent --> Настройка прокси (если включено) --> Настройка профиля --> Инициализация WebDriver
    ↓
Обработка исключений --> Загрузка исполнителей (если успешно)
```

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Инициализация Chrome с параметрами по умолчанию
driver = Chrome()

# Инициализация Chrome с указанием профиля и режима окна
driver = Chrome(profile_name='MyProfile', window_mode='kiosk')

# Инициализация Chrome с дополнительными опциями
options = ['--disable-extensions', '--mute-audio']
driver = Chrome(options=options)
```

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настраивает прокси из словаря, возвращаемого get_proxies_dict.

    Args:
        options (Options): Опции Chrome, в которые добавляются настройки прокси.
    """
```

**Назначение**: Настройка прокси для Chrome.

**Параметры**:

*   `options` (Options): Опции Chrome, в которые добавляются настройки прокси.

**Как работает функция**:

1.  **Получение словаря прокси**: Получает словарь прокси, используя функцию `get_proxies_dict`.
2.  **Объединение прокси**: Объединяет прокси из `socks4` и `socks5` в один список.
3.  **Поиск рабочего прокси**: Перебирает прокси, проверяя их работоспособность с помощью функции `check_proxy`.
4.  **Настройка прокси**: Если рабочий прокси найден, добавляет аргументы в опции Chrome в зависимости от протокола (`http`, `socks4`, `socks5`).
5.  **Логирование**: Логирует информацию о настроенном прокси или предупреждение, если прокси не найден.

**ASII flowchart**:

```
Получение словаря прокси --> Объединение прокси --> Поиск рабочего прокси --> Настройка прокси (если найден)
    ↓
Логирование
```

**Примеры**:

```python
from selenium.webdriver.chrome.options import Options
from src.webdriver.chrome.chrome import Chrome

# Создание инстанса Chrome
driver = Chrome()

# Создание инстанса Options
options = Options()

# Настройка прокси
driver.set_proxy(options)
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

1.  **Инициализация JavaScript**: Создает экземпляр класса `JavaScript`, передавая текущий экземпляр `Chrome` в качестве аргумента.
2.  **Присвоение методов JavaScript**: Присваивает методы из экземпляра `JavaScript` текущему экземпляру `Chrome`.
3.  **Инициализация ExecuteLocator**: Создает экземпляр класса `ExecuteLocator`, передавая текущий экземпляр `Chrome` в качестве аргумента.
4.  **Присвоение методов ExecuteLocator**: Присваивает методы из экземпляра `ExecuteLocator` текущему экземпляру `Chrome`.

**ASII flowchart**:

```
Инициализация JavaScript --> Присвоение методов JavaScript --> Инициализация ExecuteLocator --> Присвоение методов ExecuteLocator
```

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Создание инстанса Chrome
driver = Chrome()

# Загрузка исполнителей
driver._payload()
```

## Примеры

Пример использования класса `Chrome`:

```python
from src.webdriver.chrome.chrome import Chrome

# Создание инстанса драйвера (пример с Chrome)
driver = Chrome(window_mode='full_window')
driver.get("https://google.com")