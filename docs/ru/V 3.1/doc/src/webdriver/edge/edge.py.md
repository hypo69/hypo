# Модуль `edge`

## Обзор

Модуль `edge` предоставляет кастомный класс `Edge` для управления веб-драйвером Microsoft Edge с расширенными возможностями конфигурации, такими как установка случайного User-Agent и управление профилями пользователей. Он упрощает настройку WebDriver, используя библиотеку `fake_useragent` для генерации User-Agent и позволяет настраивать различные параметры запуска Edge, включая режим окна и профили пользователей.

## Подробнее

Этот модуль предназначен для автоматизации тестирования и сбора данных с использованием веб-браузера Edge. Он обеспечивает более гибкую настройку WebDriver по сравнению со стандартным, позволяя эмулировать различных пользователей и управлять поведением браузера. Класс `Edge` наследуется от `selenium.webdriver.Edge`, что позволяет использовать все стандартные функции WebDriver, а также добавляет новые методы для упрощения работы с элементами DOM и выполнения JavaScript. Модуль использует конфигурационный файл `edge.json` для получения дополнительных параметров запуска Edge.

## Классы

### `Edge`

**Описание**: Кастомный класс WebDriver для Edge с расширенными функциями.

**Методы**:
- `__init__`: Инициализирует экземпляр веб-драйвера Edge с заданными параметрами.
- `_payload`: Загружает исполнителей для локаторов и сценариев JavaScript.
- `set_options`: Создает и настраивает параметры запуска для Edge WebDriver.

#### `__init__`

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
    ...
```

**Описание**: Инициализирует веб-драйвер Edge с заданным user-agent и другими параметрами.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя профиля пользователя. По умолчанию `None`.
- `user_agent` (Optional[str], optional): User-agent для использования. Если `None`, генерируется случайный user-agent. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций Edge для передачи при инициализации. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
- `*args`: Дополнительные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые в конструктор родительского класса.

**Примеры**:
```python
# Инициализация Edge WebDriver с пользовательским user-agent и опциями
driver = Edge(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Инициализация Edge WebDriver в режиме kiosk
driver = Edge(window_mode='kiosk')

# Инициализация Edge WebDriver с использованием определенного профиля
driver = Edge(profile_name='MyProfile')
```

#### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
    ...
```

**Описание**: Загружает исполнителей для локаторов и JavaScript-сценариев.

**Примеры**:
```python
# Этот метод вызывается внутри __init__, поэтому прямого примера вызова нет.
```

#### `set_options`

```python
def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:
    """
    Create and configure launch options for the Edge WebDriver.

    :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.
    :return: Configured `EdgeOptions` object.
    """
    ...
```

**Описание**: Создает и настраивает параметры запуска для Edge WebDriver.

**Параметры**:
- `opts` (Optional[List[str]], optional): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Настроенный объект `EdgeOptions`.

**Примеры**:
```python
# Создание Edge WebDriver с дополнительными опциями
options = ['--disable-extensions', '--mute-audio']
driver = Edge()
edge_options = driver.set_options(options)
```

## Функции

В данном модуле функции отсутствуют.