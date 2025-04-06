# Модуль для работы с Edge WebDriver
## Обзор

Модуль `src.webdriver.edge.edge` предоставляет класс `Edge`, который является пользовательским классом WebDriver для браузера Edge. Он упрощает настройку WebDriver, используя `fake_useragent` для генерации случайных User-Agent и предоставляет дополнительные методы для работы с элементами веб-страницы.

## Подробней

Этот модуль предназначен для автоматизации взаимодействия с браузером Edge. Он позволяет настраивать User-Agent, устанавливать различные параметры запуска браузера (например, kiosk, windowless, full_window) и управлять профилями пользователей. Класс `Edge` наследуется от `selenium.webdriver.Edge`, что позволяет использовать все стандартные функции WebDriver, а также добавляет новые, специфичные для данного проекта.

## Классы

### `Edge`

**Описание**: Пользовательский класс Edge WebDriver для расширенной функциональности.

**Наследует**:
- `selenium.webdriver.Edge`: Наследует функциональность стандартного WebDriver для Edge.

**Атрибуты**:
- `driver_name` (str): Имя используемого WebDriver, по умолчанию `'edge'`.

**Методы**:
- `__init__`: Инициализирует Edge WebDriver с указанным User-Agent и опциями.
- `_payload`: Загружает исполнителей для локаторов и JavaScript сценариев.
- `set_options`: Создает и настраивает параметры запуска для Edge WebDriver.

### `Edge.__init__`

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

**Назначение**: Инициализация экземпляра класса `Edge`.

**Параметры**:
- `profile_name` (Optional[str]): Имя профиля пользователя. По умолчанию `None`.
- `user_agent` (Optional[str]): User-Agent, который будет использоваться. Если `None`, генерируется случайный User-Agent.
- `options` (Optional[List[str]]): Список опций Edge, передаваемых при инициализации.
- `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `None`

**Как работает функция**:
1. **Инициализация User-Agent**:
   - Если `user_agent` не указан, генерируется случайный User-Agent с помощью `UserAgent().random`.
   - Если `user_agent` указан - он используется для работы драйвера

2. **Загрузка настроек**:
   - Загружаются настройки из файла `edge.json`, расположенного в каталоге `src/webdriver/edge`.
   - Используется `j_loads_ns` для загрузки настроек из JSON файла.

3. **Настройка опций Edge**:
   - Создается объект `EdgeOptions`.
   - Добавляется аргумент `user-agent` с указанным User-Agent.

4. **Установка режима окна**:
   - Если в настройках или параметрах указан режим окна (`window_mode`), добавляется соответствующий аргумент:
     - `--kiosk` для режима киоска.
     - `--headless` для "windowless" режима.
     - `--start-maximized` для полноэкранного режима.

5. **Добавление дополнительных опций**:
   - Добавляются пользовательские опции из параметра `options`.
   - Добавляются опции из конфигурационного файла.
   - Добавляются заголовки из конфигурационного файла.

6. **Настройка директории профиля**:
   - Определяется директория профиля пользователя на основе настроек и параметра `profile_name`.
   - Если в пути профиля встречается `%LOCALAPPDATA%`, он заменяется на значение переменной окружения `LOCALAPPDATA`.
   - Добавляется аргумент `--user-data-dir` с указанием директории профиля.

7. **Запуск WebDriver**:
   - Инициализируется Edge WebDriver с указанными опциями.
   - Вызывается метод `_payload` для загрузки исполнителей локаторов и JavaScript.

8. **Обработка исключений**:
   - Обрабатываются исключения `WebDriverException` и `Exception` при запуске WebDriver.
   - В случае ошибки, в лог записывается критическое сообщение об ошибке.

**ASII flowchart**:

```
A[Загрузка User-Agent и настроек]
  |
  V
B[Создание и настройка EdgeOptions]
  |
  V
C[Установка режима окна]
  |
  V
D[Добавление дополнительных опций и заголовков]
  |
  V
E[Настройка директории профиля]
  |
  V
F[Запуск Edge WebDriver и загрузка payload]
  |
  V
G[Обработка исключений]
```

**Примеры**:

```python
from src.webdriver.edge.edge import Edge
# Пример 1: Запуск Edge с случайным User-Agent
driver = Edge()

# Пример 2: Запуск Edge с указанным User-Agent и опциями
driver = Edge(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', options=['--disable-gpu'])

# Пример 3: Запуск Edge в полноэкранном режиме
driver = Edge(window_mode='full_window')
```

### `Edge._payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
```

**Назначение**: Загрузка исполнителей для локаторов и JavaScript сценариев.

**Параметры**:
- `self`: Экземпляр класса `Edge`.

**Возвращает**:
- `None`

**Как работает функция**:
1. **Инициализация JavaScript**:
   - Создается экземпляр класса `JavaScript`, который принимает текущий экземпляр `Edge` в качестве аргумента.

2. **Загрузка JavaScript функций**:
   - Загружаются JavaScript функции из экземпляра `JavaScript` и присваиваются атрибутам текущего экземпляра `Edge`:
     - `get_page_lang`: Получение языка страницы.
     - `ready_state`: Получение состояния готовности страницы.
     - `get_referrer`: Получение реферера страницы.
     - `unhide_DOM_element`: Отображение DOM элемента.
     - `window_focus`: Установка фокуса на окно браузера.

3. **Инициализация ExecuteLocator**:
   - Создается экземпляр класса `ExecuteLocator`, который принимает текущий экземпляр `Edge` в качестве аргумента.

4. **Загрузка методов ExecuteLocator**:
   - Загружаются методы из экземпляра `ExecuteLocator` и присваиваются атрибутам текущего экземпляра `Edge`:
     - `execute_locator`: Выполнение локатора для поиска элемента на странице.
     - `get_webelement_as_screenshot`: Получение скриншота веб-элемента.
     - `get_webelement_by_locator`: Получение веб-элемента по локатору.
     - `get_attribute_by_locator`: Получение атрибута веб-элемента по локатору.
     - `send_message`: Отправка сообщения веб-элементу (синоним `send_key_to_webelement`).

**ASII flowchart**:

```
A[Инициализация JavaScript]
  |
  V
B[Загрузка JavaScript функций]
  |
  V
C[Инициализация ExecuteLocator]
  |
  V
D[Загрузка методов ExecuteLocator]
```

**Примеры**:
```python
from src.webdriver.edge.edge import Edge
# Пример: Инициализация Edge и загрузка payload
driver = Edge()
driver._payload()

# Теперь можно использовать методы, загруженные из payload, например:
# element = driver.execute_locator(locator)
```

### `Edge.set_options`

```python
def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:  
    """  
    Create and configure launch options for the Edge WebDriver.  

    :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.  
    :return: Configured `EdgeOptions` object.  
    """
```

**Назначение**: Создание и настройка параметров запуска для Edge WebDriver.

**Параметры**:
- `opts` (Optional[List[str]]): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Сконфигурированный объект `EdgeOptions`.

**Как работает функция**:
1. **Создание объекта EdgeOptions**:
   - Создается новый объект `EdgeOptions`.

2. **Добавление опций**:
   - Если передан список опций `opts`, каждая опция добавляется в объект `EdgeOptions`.

3. **Возврат объекта EdgeOptions**:
   - Возвращается сконфигурированный объект `EdgeOptions`.

**ASII flowchart**:

```
A[Создание EdgeOptions]
  |
  V
B[Добавление опций (если есть)]
  |
  V
C[Возврат EdgeOptions]
```

**Примеры**:

```python
from src.webdriver.edge.edge import Edge
# Пример 1: Создание EdgeOptions без дополнительных опций
driver = Edge()
options = driver.set_options()

# Пример 2: Создание EdgeOptions с дополнительными опциями
driver = Edge()
options = driver.set_options(opts=['--disable-gpu', '--mute-audio'])
```

## Примеры

```python
if __name__ == "__main__":
    driver = Edge(window_mode='full_window')
    driver.get("https://www.example.com")
```

В данном примере создается экземпляр класса `Edge` в полноэкранном режиме и открывается сайт "https://www.example.com".