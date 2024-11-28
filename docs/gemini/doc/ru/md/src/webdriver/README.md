# Модуль `webdriver`

## Обзор

Модуль `webdriver` предоставляет фреймворк для выполнения действий на веб-страницах с помощью WebDriver. Он обрабатывает скрипты и локеры для автоматизации взаимодействия с веб-элементами.

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` отвечает за выполнение навигации и взаимодействия с веб-страницей на основе данных локатора, предоставляемых в виде словаря.

**Атрибуты**:

- `driver`: Экземпляр WebDriver для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий с веб-элементами.
- `by_mapping`: Словарь, отображающий строковые представления локаторов на объекты Selenium `By`.

**Методы**:

#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Конструктор класса. Инициализирует экземпляр WebDriver и `ActionChains`.

**Аргументы**:

- `driver`: Экземпляр WebDriver.

**Возвращает**:
-  `None`


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Описание**: Основной метод для выполнения действий на основе локатора.

**Аргументы**:

- `locator` (dict): Словарь с параметрами для выполнения действий.
- `message` (str, опционально): Сообщение для отправки, если необходимо.
- `typing_speed` (float, опционально): Скорость ввода для отправки сообщений. По умолчанию 0.
- `continue_on_error` (bool, опционально): Флаг, указывающий, продолжать ли выполнение, если произошла ошибка. По умолчанию `True`.


**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия.

**Вызывает исключения**:
- `WebDriverException`: Описание ситуации, в которой возникает исключение `WebDriverException`.
- `ExecuteLocatorException`: Описание ситуации, в которой возникает исключение `ExecuteLocatorException`.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**: Возвращает веб-элементы, найденные по локатору.

**Аргументы**:

- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с параметрами локатора.
- `message` (str, опционально): Сообщение для логов.


**Возвращает**:
- `WebElement | List[WebElement] | bool`: Найденный элемент(ы) или `False`, если не найден.

**Вызывает исключения**:
- `NoSuchElementException`: Описание ситуации, когда элемент не найден.
- `TimeoutException`: Описание ситуации, когда поиск элемента превысил заданное время.



#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Описание**: Возвращает атрибут найденного веб-элемента по локатору.

**Аргументы**:

- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с параметрами локатора.
- `message` (str, опционально): Сообщение для логов.

**Возвращает**:
- `str | list | dict | bool`: Значение атрибута или `False`, если элемент не найден.

**Вызывает исключения**:
- `NoSuchElementException`: Описание ситуации, когда элемент не найден.
- `TimeoutException`: Описание ситуации, когда поиск элемента превысил заданное время.


#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool`

**Описание**: Отправляет сообщение веб-элементу.

**Аргументы**:

- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с параметрами локатора.
- `message` (str): Сообщение для отправки.
- `typing_speed` (float): Скорость ввода.
- `continue_on_error` (bool): Флаг, продолжать ли выполнение при ошибке.

**Возвращает**:
- `bool`: `True`, если сообщение отправлено успешно, `False` иначе.


### `Driver`

**Описание**: Класс, обеспечивающий взаимодействие с WebDriver. Наследует от `DriverBase`.

**Атрибуты** (см. описание в исходном коде):
- `previous_url`: Предыдущий URL.
- `referrer`: Referrer URL.
- `page_lang`: Язык страницы.
- ... (другие атрибуты)

**Методы** (см. описание в исходном коде):
- `scroll`: Прокрутка страницы.
- `locale`: Определение языка страницы.
- `get_url`: Загрузка URL.
- `extract_domain`: Извлечение домена из URL.
- `_save_cookies_localy`: Сохранение куки.
- ... (другие методы)


## Функции

(Описание функций, если таковые имеются, в данном формате)


## Примеры использования

(Примеры использования классов и методов в markdown формате)


## Примечания

(Дополнительные замечания, как в исходном коде)