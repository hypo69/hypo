# Модуль `edge`

## Обзор

Модуль `edge` предоставляет кастомный класс `Edge` для управления веб-драйвером Edge с расширенными возможностями. Он упрощает настройку Edge WebDriver, используя `fake_useragent` для генерации случайных user-agent, а также позволяет задавать различные параметры запуска, такие как режим окна и профиль пользователя.

## Подробнее

Этот модуль предназначен для автоматизации взаимодействия с браузером Edge в проекте `hypotez`. Он позволяет управлять экземпляром браузера Edge, задавая различные параметры запуска, такие как user-agent, режим окна (например, kiosk или headless) и профиль пользователя. Модуль использует библиотеку `selenium` для управления браузером и `fake_useragent` для генерации случайных user-agent. Конфигурация драйвера, включая путь к исполняемому файлу и дополнительные опции, загружается из JSON-файла. Класс `Edge` предоставляет методы для выполнения JavaScript на странице, поиска элементов и выполнения действий с ними.

## Классы

### `Edge`

**Описание**: Кастомный класс Edge WebDriver для расширенной функциональности.

**Методы**:
- `__init__`: Инициализирует Edge WebDriver с указанным user-agent и опциями.
- `_payload`: Загружает исполнители для локаторов и JavaScript сценариев.
- `set_options`: Создает и конфигурирует параметры запуска для Edge WebDriver.

**Параметры**:
- `driver_name` (str): Имя используемого WebDriver, по умолчанию 'edge'.

**Примеры**
```python
from src.webdriver.edge.edge import Edge
# Инициализация Edge WebDriver с режимом полного окна
driver = Edge(window_mode='full_window')
driver.get("https://www.example.com")
```

## Функции

### `__init__`

```python
def __init__(self,  profile_name: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 options: Optional[List[str]] = None,
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
    """
    Initializes the Edge WebDriver with the specified user agent and options.

    :param user_agent: The user-agent string to be used. If `None`, a random user agent is generated.
    :type user_agent: Optional[str]
    :param options: A list of Edge options to be passed during initialization.
    :type options: Optional[List[str]]
    :param window_mode: Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)
    :type window_mode: Optional[str]
    """
```

**Описание**: Инициализирует Edge WebDriver с указанным user-agent и опциями.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя профиля пользователя. По умолчанию `None`.
- `user_agent` (Optional[str], optional): User-agent, который будет использоваться. Если `None`, генерируется случайный user-agent.
- `options` (Optional[List[str]], optional): Список опций Edge, передаваемых при инициализации.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

**Примеры**:
```python
# Инициализация Edge WebDriver с user-agent и опциями
driver = Edge(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', options=['--disable-gpu', '--disable-extensions'])
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
```

**Описание**: Загружает исполнители для локаторов и JavaScript сценариев.

**Примеры**:
```python
# Загрузка исполнителей для locators и JavaScript сценариев
driver._payload()
```

### `set_options`

```python
def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:  
    """  
    Create and configure launch options for the Edge WebDriver.  

    :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.  
    :return: Configured `EdgeOptions` object.  
    """  
```

**Описание**: Создает и конфигурирует параметры запуска для Edge WebDriver.

**Параметры**:
- `opts` (Optional[List[str]], optional): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Сконфигурированный объект `EdgeOptions`.

**Примеры**:
```python
# Создание и конфигурирование параметров запуска
options = driver.set_options(opts=['--disable-gpu', '--disable-extensions'])
```