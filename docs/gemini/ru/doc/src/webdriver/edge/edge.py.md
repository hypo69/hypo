# Модуль `src.webdriver.edge.edge`

## Обзор

Модуль предоставляет класс `Edge`, который является кастомной реализацией веб-драйвера Edge с упрощенной конфигурацией, использующей `fake_useragent`.

## Подробнее

Этот модуль предназначен для создания и управления экземплярами веб-драйвера Microsoft Edge. Он использует библиотеку `selenium` для взаимодействия с браузером Edge и `fake_useragent` для генерации случайных User-Agent. Модуль предоставляет удобный способ настройки драйвера с помощью параметров, передаваемых при инициализации, а также из конфигурационного файла `edge.json`.

## Классы

### `Edge`

**Описание**: Кастомный класс веб-драйвера Edge для расширенной функциональности.

**Наследует**:
- `selenium.webdriver.Edge.WebDriver`

**Атрибуты**:
- `driver_name` (str): Имя используемого веб-драйвера, по умолчанию `'edge'`.

**Методы**:
- `__init__`: Инициализирует веб-драйвер Edge с указанным User-Agent и опциями.
- `_payload`: Загружает исполнители для локаторов и JavaScript-сценариев.
- `set_options`: Создает и конфигурирует параметры запуска для веб-драйвера Edge.

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
    ...
```

**Назначение**: Инициализирует веб-драйвер Edge с указанным User-Agent и опциями.

**Параметры**:
- `profile_name` (Optional[str]): Имя профиля пользователя. По умолчанию `None`.
- `user_agent` (Optional[str]): User-Agent, который будет использоваться. Если `None`, генерируется случайный User-Agent.
- `options` (Optional[List[str]]): Список опций Edge, которые будут переданы при инициализации.
- `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `WebDriverException`: Если не удается запустить веб-драйвер Edge.
- `Exception`: В случае общей ошибки при запуске веб-драйвера Edge.

**Как работает функция**:

1. **Инициализация User-Agent**: Если `user_agent` не указан, генерируется случайный User-Agent с использованием `fake_useragent`.
2. **Загрузка настроек**: Загружает настройки из файла `edge.json` с использованием `j_loads_ns`.
3. **Инициализация опций Edge**: Создает объект `EdgeOptions` и добавляет User-Agent.
4. **Установка режима окна**: Устанавливает режим окна из конфигурации или параметров, если они указаны (`kiosk`, `windowless`, `full_window`).
5. **Добавление пользовательских опций**: Добавляет пользовательские опции, переданные при инициализации.
6. **Добавление опций из конфигурации**: Добавляет опции из конфигурационного файла.
7. **Добавление заголовков из конфигурации**: Добавляет заголовки из конфигурационного файла.
8. **Настройка директории профиля**: Определяет директорию профиля на основе настроек и имени профиля.
9. **Запуск веб-драйвера**: Запускает веб-драйвер Edge с указанными опциями и сервисом.
10. **Загрузка исполнителей**: Вызывает метод `_payload` для загрузки исполнителей локаторов и JavaScript-сценариев.
11. **Обработка исключений**: Ловит исключения, которые могут возникнуть при запуске веб-драйвера, и логирует их с помощью `logger.critical`.

```text
UserAgent Initialization --> Load Settings from edge.json --> Initialize EdgeOptions --> Set Window Mode --> Add Custom Options --> Add Options from Configuration --> Add Headers from Configuration --> Configure Profile Directory --> Start Edge WebDriver --> Load Executors --> Exception Handling
```

**Примеры**:

```python
# Инициализация Edge с пользовательским User-Agent
driver = Edge(user_agent='My Custom User Agent')

# Инициализация Edge с опциями
driver = Edge(options=['--disable-extensions', '--mute-audio'])

# Инициализация Edge в режиме kiosk
driver = Edge(window_mode='kiosk')
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
    ...
```

**Назначение**: Загружает исполнители для локаторов и JavaScript-сценариев.

**Параметры**:
- `self`: Ссылка на экземпляр класса `Edge`.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Инициализация JavaScript**: Создает экземпляр класса `JavaScript`, передавая ему текущий веб-драйвер.
2. **Присвоение JavaScript-функций**: Присваивает атрибутам экземпляра веб-драйвера JavaScript-функции из экземпляра `JavaScript`.
3. **Инициализация ExecuteLocator**: Создает экземпляр класса `ExecuteLocator`, передавая ему текущий веб-драйвер.
4. **Присвоение функций ExecuteLocator**: Присваивает атрибутам экземпляра веб-драйвера функции из экземпляра `ExecuteLocator`.

```text
Initialize JavaScript --> Assign JavaScript Functions --> Initialize ExecuteLocator --> Assign ExecuteLocator Functions
```

**Примеры**:

```python
# Вызов метода _payload (обычно вызывается внутри __init__)
driver = Edge()
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
    ...
```

**Назначение**: Создает и конфигурирует параметры запуска для веб-драйвера Edge.

**Параметры**:
- `opts` (Optional[List[str]]): Список опций для добавления в веб-драйвер Edge. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Сконфигурированный объект `EdgeOptions`.

**Как работает функция**:

1. **Создание экземпляра EdgeOptions**: Создает новый экземпляр класса `EdgeOptions`.
2. **Добавление опций**: Если передан список опций (`opts`), добавляет каждую опцию из списка в экземпляр `EdgeOptions`.
3. **Возврат EdgeOptions**: Возвращает сконфигурированный объект `EdgeOptions`.

```text
Create EdgeOptions Instance --> Add Options (if provided) --> Return EdgeOptions
```

**Примеры**:

```python
# Создание EdgeOptions с опциями
options = Edge().set_options(opts=['--disable-extensions', '--mute-audio'])

# Создание EdgeOptions без опций
options = Edge().set_options()
```

## Примеры

```python
if __name__ == "__main__":
    driver = Edge(window_mode='full_window')
    driver.get("https://www.example.com")