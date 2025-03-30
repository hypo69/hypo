# Модуль для работы с WebDriver Chrome

## Обзор

Модуль `chrome.py` предоставляет расширение для `webdriver.Chrome` с дополнительной функциональностью, упрощающей настройку и использование Chrome WebDriver. Он позволяет настраивать профили, устанавливать пользовательские агенты, прокси и другие параметры запуска браузера.

## Подробней

Этот модуль предназначен для управления экземпляром Chrome WebDriver с возможностью настройки различных параметров, таких как пользовательский профиль, версия ChromeDriver, пользовательский агент, прокси и режим окна. Он также предоставляет методы для выполнения JavaScript-кода и работы с элементами на странице. Модуль облегчает автоматизацию задач, связанных с веб-браузером Chrome, и может использоваться для тестирования, сбора данных и других целей.

## Классы

### `Chrome`

**Описание**: Расширение для `webdriver.Chrome` с дополнительной функциональностью.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Chrome` с заданными параметрами.
- `set_proxy`: Настраивает прокси для Chrome из словаря, возвращаемого `get_proxies_dict`.
- `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Chrome. По умолчанию `None`.
- `chromedriver_version` (Optional[str], optional): Версия chromedriver. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Chrome. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

**Примеры**
```python
from src.webdriver.chrome.chrome import Chrome

# Пример инициализации Chrome WebDriver с пользовательским профилем и режимом окна
driver = Chrome(profile_name='test_profile', window_mode='full_window')
driver.get("https://www.google.com")
driver.quit()

# Пример инициализации Chrome WebDriver с прокси
driver = Chrome(proxy_file_path='path/to/proxy_file.txt')
driver.get("https://www.example.com")
driver.quit()
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
        Exception: Если возникает общая ошибка во время работы Chrome WebDriver.

    Example:
        >>> driver = Chrome(profile_name='test_profile', window_mode='full_window')
        >>> driver.get("https://www.google.com")
        >>> driver.quit()
    """
    ```

**Описание**: Инициализирует экземпляр класса `Chrome`, настраивает параметры запуска Chrome WebDriver, такие как путь к профилю, пользовательский агент, прокси и режим окна.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Chrome. По умолчанию `None`.
- `chromedriver_version` (Optional[str], optional): Версия chromedriver. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Chrome. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка при запуске WebDriver, например, из-за несовместимости версии ChromeDriver или отсутствия Chrome.
- `Exception`: Если возникает общая ошибка во время работы Chrome WebDriver.

**Примеры**:
```python
from src.webdriver.chrome.chrome import Chrome

# Пример инициализации Chrome WebDriver с пользовательским профилем и режимом окна
driver = Chrome(profile_name='test_profile', window_mode='full_window')
driver.get("https://www.google.com")
driver.quit()

# Пример инициализации Chrome WebDriver с прокси
driver = Chrome(proxy_file_path='path/to/proxy_file.txt')
driver.get("https://www.example.com")
driver.quit()
```

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Настройка прокси из словаря, возвращаемого get_proxies_dict.

    Args:
        options (Options): Опции Chrome, в которые добавляются настройки прокси.

    Example:
        >>> chrome_instance = Chrome()
        >>> options = Options()
        >>> chrome_instance.set_proxy(options)
    """
```

**Описание**: Настраивает прокси для Chrome WebDriver на основе данных, полученных из словаря прокси.

**Параметры**:
- `options` (Options): Опции Chrome, в которые добавляются настройки прокси.

**Примеры**:
```python
from selenium.webdriver.chrome.options import Options
from src.webdriver.chrome.chrome import Chrome

# Пример использования функции set_proxy
chrome_instance = Chrome()
options = Options()
chrome_instance.set_proxy(options)
# Теперь options можно использовать при создании экземпляра Chrome WebDriver
driver = chrome_instance # Chrome(options=options)
driver.get("https://www.example.com")
driver.quit()
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Загружает исполнителей для локаторов и JavaScript сценариев.
    """
```

**Описание**: Загружает исполнителей (executor) для локаторов и JavaScript сценариев, расширяя функциональность экземпляра Chrome WebDriver.

**Примеры**:
```python
from src.webdriver.chrome.chrome import Chrome

# Пример использования функции _payload
driver = Chrome()
driver._payload()
# Теперь можно использовать методы, добавленные в _payload, такие как execute_locator
driver.get("https://www.example.com")
# element = driver.execute_locator("xpath", "//h1")
driver.quit()