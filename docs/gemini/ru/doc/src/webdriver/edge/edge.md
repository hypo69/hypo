# Модуль `hypotez/src/webdriver/edge/edge.py`

## Обзор

Этот модуль предоставляет класс `Edge`, расширяющий функциональность стандартного драйвера Selenium для браузера Edge. Он упрощает конфигурацию драйвера, используя библиотеку `fake_useragent` для генерации случайных User-Agent строк.  Модуль также включает методы для работы с JavaScript и выполнением пользовательских команд на странице.

## Классы

### `Edge`

**Описание**: Наследуемый класс от `selenium.webdriver.Edge`, предоставляющий расширенные методы для взаимодействия с браузером Edge.

**Атрибуты**:

- `driver_name` (str): Имя драйвера, по умолчанию 'edge'.

**Методы**:

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

**Описание**: Инициализирует экземпляр класса `Edge`. Загружает настройки из файла `edge.json`, создаёт и конфигурирует `EdgeOptions`, устанавливает User-Agent.

**Параметры**:

- `user_agent` (Optional[dict], optional): Словарь с пользовательским User-Agent. Если `None`, генерируется случайный User-Agent. По умолчанию `None`.

**Возвращает**:
- `None`


#### `_payload(self) -> None`

**Описание**: Загружает исполнителей для локаторов и JavaScript сценариев.

**Возвращает**:
- `None`

#### `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`

**Описание**: Создаёт и конфигурирует параметры запуска для Edge WebDriver.

**Параметры**:

- `opts` (Optional[List[str]], optional): Список параметров для добавления к Edge WebDriver. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Объект с настроенными параметрами запуска.

**Обрабатываемые исключения**:

- `WebDriverException`:  Исключение, которое возникает, если Edge WebDriver не удалось запустить.
- `Exception`: Общее исключение, возникающее при сбоях в работе WebDriver.  В этом случае возникает критическое сообщение об ошибке.


## Функции

(В данном модуле нет функций, только класс)

```