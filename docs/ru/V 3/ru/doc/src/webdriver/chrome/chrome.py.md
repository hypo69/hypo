# Модуль `chrome`

## Обзор

Модуль `src.webdriver.chrome` предназначен для работы с веб-драйвером Chrome, предоставляя расширенные возможности по сравнению со стандартным `webdriver.Chrome` из библиотеки Selenium. Он позволяет настраивать параметры запуска Chrome, такие как профиль пользователя, user-agent, прокси и режим отображения окна.

## Подробней

Этот модуль предоставляет класс `Chrome`, который наследуется от `selenium.webdriver.Chrome`. Он автоматически загружает настройки из конфигурационного файла `chrome.json`, расположенного в каталоге `src/webdriver/chrome`. Это позволяет упростить настройку веб-драйвера, централизованно управляя параметрами запуска. Модуль поддерживает установку пользовательского профиля, прокси-серверов, user-agent, а также различные режимы отображения окна браузера (kiosk, windowless, full_window). Кроме того, он предоставляет методы для выполнения JavaScript-сценариев и работы с элементами DOM.

## Классы

### `Chrome`

**Описание**: Расширение для класса `webdriver.Chrome` с дополнительной функциональностью.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Chrome`, настраивает параметры запуска браузера.
- `set_proxy`: Настраивает прокси-сервер для Chrome на основе предоставленных данных.
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

# Пример инициализации Chrome с пользовательским профилем и в полноэкранном режиме
driver = Chrome(profile_name='my_profile', window_mode='full_window')
driver.get("https://www.google.com")

# Пример инициализации Chrome с использованием пользовательского user-agent
driver = Chrome(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver.get("https://www.google.com")
```

## Функции

### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Args:
        options (Options): Опции Chrome, в которые добавляются настройки прокси.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при настройке прокси.

    Example:
        >>> from selenium.webdriver.chrome.options import Options
        >>> options = Options()
        >>> chrome_instance = Chrome()
        >>> chrome_instance.set_proxy(options)
    """
```

**Описание**: Настраивает прокси-сервер для Chrome на основе словаря прокси, полученного из `get_proxies_dict`.

**Параметры**:
- `options` (Options): Опции Chrome, в которые добавляются настройки прокси.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют явные исключения, но возможны исключения при работе с прокси.

**Примеры**:

```python
from selenium.webdriver.chrome.options import Options
from src.webdriver.chrome.chrome import Chrome

# Пример использования функции set_proxy
options = Options()
chrome_instance = Chrome()
chrome_instance.set_proxy(options)

# Теперь Chrome будет использовать прокси, если он доступен и настроен правильно.
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Args:
        self: Экземпляр класса Chrome.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при загрузке исполнителей.

    Example:
        >>> chrome_instance = Chrome()
        >>> chrome_instance._payload()
    """
```

**Описание**: Загружает исполнителей для локаторов и JavaScript сценариев, добавляя их как атрибуты экземпляра класса `Chrome`.

**Параметры**:
- `self`: Экземпляр класса `Chrome`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют явные исключения, но возможны исключения при выполнении JavaScript.

**Примеры**:

```python
from src.webdriver.chrome.chrome import Chrome

# Пример использования функции _payload
chrome_instance = Chrome()
chrome_instance._payload()

# Теперь можно использовать execute_locator и другие функции, добавленные в _payload.