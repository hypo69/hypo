# Документация по модулю `executor.py`

## Оглавление

- [Обзор](#обзор)
- [Основные возможности](#основные-возможности)
- [Структура модуля](#структура-модуля)
    - [Классы](#классы)
        - [ExecuteLocator](#executelocator)
            - [Атрибуты](#атрибуты)
            - [Методы](#методы)
                - [`__post_init__`](#__post_init__)
                - [`execute_locator`](#execute_locator)
                - [`evaluate_locator`](#evaluate_locator)
                - [`get_attribute_by_locator`](#get_attribute_by_locator)
                - [`get_webelement_by_locator`](#get_webelement_by_locator)
                - [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
                - [`execute_event`](#execute_event)
                - [`send_message`](#send_message)
    - [Диаграммы потока](#диаграммы-потока)
        - [`execute_locator`](#execute_locator-1)
        - [`evaluate_locator`](#evaluate_locator-1)
        - [`get_attribute_by_locator`](#get_attribute_by_locator-1)
- [Использование](#использование)
- [Пример](#пример)
- [Зависимости](#зависимости)

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Модуль предоставляет гибкий и универсальный фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Основные возможности

1. **Парсинг и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локаторов.
2. **Взаимодействие с веб-элементами**: Выполняет различные действия, такие как клики, отправка сообщений, выполнение событий и извлечение атрибутов из веб-элементов.
3. **Обработка ошибок**: Поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы с нестабильными элементами или требующими особого подхода.
4. **Поддержка нескольких типов локаторов**: Обрабатывает как отдельные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

## Структура модуля

### Классы

#### `ExecuteLocator`

Этот класс является ядром модуля, отвечающим за обработку взаимодействий с веб-элементами на основе предоставленных локаторов.

**Описание**:

Класс `ExecuteLocator` предназначен для выполнения действий над веб-элементами на основе предоставленных локаторов. Он использует Selenium WebDriver для поиска элементов и выполнения над ними различных операций, таких как клики, отправка сообщений и извлечение атрибутов. Класс обеспечивает гибкий и универсальный способ взаимодействия с веб-элементами, поддерживая различные типы локаторов и стратегии обработки ошибок.

**Как работает класс**:

Класс `ExecuteLocator` инициализируется с экземпляром Selenium WebDriver. Он использует этот драйвер для поиска веб-элементов на странице. Основной метод `execute_locator` принимает локатор (который может быть словарем или объектом `SimpleNamespace`) и выполняет действия, определенные в этом локаторе. Локатор указывает, как найти элемент (например, по ID, CSS-селектору или XPath) и какое действие над ним выполнить (например, кликнуть, отправить сообщение или получить атрибут). Класс также включает методы для оценки атрибутов локатора, извлечения веб-элементов и выполнения событий, связанных с локатором. Поддерживается обработка исключений для обеспечения стабильной работы даже при возникновении ошибок при взаимодействии с веб-элементами.

##### Атрибуты

- `driver`: Экземпляр Selenium WebDriver.
- `actions`: Объект `ActionChains` для выполнения сложных действий.
- `by_mapping`: Словарь, сопоставляющий типы локаторов с методами `By` Selenium.
- `mode`: Режим выполнения (`debug`, `dev` и т.д.).

##### Методы

- `__post_init__`
```python
def __post_init__(self) -> None:
    """
    Инициализирует объект `ActionChains`, если предоставлен драйвер.
    
    Args:
        self: Экземпляр класса `ExecuteLocator`.

    Returns:
        None

    """
    # Инициализирует actions только при наличии driver
    if self.driver:
        self.actions = ActionChains(self.driver)
```

    **Назначение**: Инициализирует объект `ActionChains`, если предоставлен драйвер.

    **Как работает функция**:
    Метод `__post_init__` вызывается после инициализации экземпляра класса `ExecuteLocator`. Он проверяет, был ли передан драйвер Selenium WebDriver при создании экземпляра класса. Если драйвер присутствует, метод создает экземпляр класса `ActionChains`, который используется для выполнения сложных последовательностей действий с веб-элементами (например, перемещение мыши, нажатие клавиш). Если драйвер отсутствует, `ActionChains` не инициализируется.

    **Параметры**:
    - `self`: Экземпляр класса `ExecuteLocator`.

    **Возвращает**:
    - `None`

    **Вызывает исключения**:
    - Отсутствуют.

    **Примеры**:
    Пример инициализации класса `ExecuteLocator` с драйвером:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Проверка, что actions был инициализирован
    print(executor.actions)
    ```
    Пример инициализации класса `ExecuteLocator` без драйвера:
    ```python
    from src.webdriver.executor import ExecuteLocator

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator()

    # Проверка, что actions не был инициализирован
    print(executor.actions)
    ```

- `execute_locator`
```python
async def execute_locator(self, locator: SimpleNamespace | dict | None) -> Any:
    """
    Выполняет действия над веб-элементом на основе предоставленного локатора.

    Args:
        locator (SimpleNamespace | dict | None): Объект локатора, содержащий информацию о том,
                                                  как найти и взаимодействовать с веб-элементом.
                                                  Может быть типа SimpleNamespace или dict.

    Returns:
        Any: Результат выполнения действия над веб-элементом.

    Raises:
        Exception: Если возникает ошибка при выполнении локатора.
    """
    ...
```

    **Назначение**: Выполняет действия над веб-элементом на основе предоставленного локатора.

    **Как работает функция**:
    Метод `execute_locator` принимает локатор, который может быть представлен в виде объекта `SimpleNamespace` или словаря `dict`. Сначала он проверяет тип локатора и преобразует словарь в `SimpleNamespace`, если это необходимо. Затем метод определяет асинхронную функцию `_parse_locator`, которая отвечает за обработку локатора и выполнение действий над веб-элементом. Функция `_parse_locator` проверяет наличие атрибутов `event`, `attribute` или обязательных полей в локаторе. Если такие атрибуты есть, она пытается сопоставить тип локатора (`by`) с соответствующим методом Selenium и выполнить действие над веб-элементом. Если в процессе выполнения возникают исключения, они перехватываются и логируются. В зависимости от наличия атрибутов `event` или `attribute`, выполняются соответствующие методы `execute_event` или `get_attribute_by_locator`. В конечном итоге, метод возвращает результат выполнения действия над веб-элементом.

    **Параметры**:
    - `locator` (SimpleNamespace | dict | None): Объект локатора, содержащий информацию о том, как найти и взаимодействовать с веб-элементом. Может быть типа `SimpleNamespace` или `dict`.

    **Возвращает**:
    - `Any`: Результат выполнения действия над веб-элементом.

    **Вызывает исключения**:
    - `Exception`: Если возникает ошибка при выполнении локатора.

    **Примеры**:
    Пример выполнения локатора с событием `click()`:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id", event="click()")

    async def main():
        # Выполнение локатора
        result = await executor.execute_locator(locator)
        print(result)

    asyncio.run(main())
    ```
    Пример выполнения локатора с получением атрибута:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id", attribute="text")

    async def main():
        # Выполнение локатора
        result = await executor.execute_locator(locator)
        print(result)

    asyncio.run(main())
    ```

- `evaluate_locator`
```python
async def evaluate_locator(self, locator: SimpleNamespace) -> list[Any] | Any:
    """
    Оценивает и обрабатывает атрибуты локатора.

    Args:
        locator (SimpleNamespace): Объект локатора, содержащий информацию об атрибутах, которые нужно оценить.

    Returns:
        list[Any] | Any: Результат оценки атрибутов. Если атрибут является списком, возвращается список результатов.
                         В противном случае возвращается один результат.

    Raises:
        Exception: Если возникает ошибка при оценке атрибута.
    """
    ...
```

    **Назначение**: Оценивает и обрабатывает атрибуты локатора.

    **Как работает функция**:
    Метод `evaluate_locator` принимает объект локатора типа `SimpleNamespace`, содержащий информацию об атрибутах, которые необходимо оценить. Метод проверяет, является ли атрибут списком. Если атрибут является списком, метод итерируется по каждому атрибуту в списке и вызывает асинхронную функцию `_evaluate` для каждого атрибута. Результаты оценки собираются с помощью `asyncio.gather` и возвращаются в виде списка. Если атрибут не является списком, метод вызывает `_evaluate` для одного атрибута и возвращает результат.

    **Параметры**:
    - `locator` (SimpleNamespace): Объект локатора, содержащий информацию об атрибутах, которые нужно оценить.

    **Возвращает**:
    - `list[Any] | Any`: Результат оценки атрибутов. Если атрибут является списком, возвращается список результатов. В противном случае возвращается один результат.

    **Вызывает исключения**:
    - `Exception`: Если возникает ошибка при оценке атрибута.

    **Примеры**:
    Пример оценки локатора с атрибутом в виде списка:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(attribute=["text", "value"])

    async def main():
        # Оценка локатора
        result = await executor.evaluate_locator(locator)
        print(result)

    asyncio.run(main())
    ```
    Пример оценки локатора с одним атрибутом:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(attribute="text")

    async def main():
        # Оценка локатора
        result = await executor.evaluate_locator(locator)
        print(result)

    asyncio.run(main())
    ```

- `get_attribute_by_locator`
```python
async def get_attribute_by_locator(self, locator: SimpleNamespace | dict) -> list[Any] | str | None:
    """
    Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

    Args:
        locator (SimpleNamespace | dict): Локатор элемента, атрибуты которого необходимо извлечь.
                                          Может быть представлен в виде SimpleNamespace или dict.

    Returns:
        list[Any] | str | None: Значение атрибута элемента или список значений, если элемент является списком.
                                  Возвращает None, если элемент не найден.

    Raises:
        Exception: Если возникает ошибка при извлечении атрибута.
    """
    ...
```

    **Назначение**: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

    **Как работает функция**:
    Метод `get_attribute_by_locator` принимает локатор, который может быть представлен в виде объекта `SimpleNamespace` или словаря `dict`. Сначала он преобразует локатор в `SimpleNamespace`, если это необходимо. Затем метод вызывает `get_webelement_by_locator` для получения веб-элемента на основе предоставленного локатора. Если веб-элемент не найден, метод логирует сообщение отладки и возвращает `None`. Если веб-элемент найден, метод проверяет, является ли атрибут локатора строкой, похожей на словарь. Если это так, метод разбирает строку атрибута в словарь. Затем метод проверяет, является ли веб-элемент списком. Если веб-элемент является списком, метод извлекает атрибуты для каждого элемента в списке и возвращает список атрибутов. Если веб-элемент не является списком, метод извлекает атрибут для одного веб-элемента и возвращает его.

    **Параметры**:
    - `locator` (SimpleNamespace | dict): Локатор элемента, атрибуты которого необходимо извлечь. Может быть представлен в виде `SimpleNamespace` или `dict`.

    **Возвращает**:
    - `list[Any] | str | None`: Значение атрибута элемента или список значений, если элемент является списком. Возвращает `None`, если элемент не найден.

    **Вызывает исключения**:
    - `Exception`: Если возникает ошибка при извлечении атрибута.

    **Примеры**:
    Пример извлечения атрибута из одного элемента:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id", attribute="text")

    async def main():
        # Получение атрибута по локатору
        result = await executor.get_attribute_by_locator(locator)
        print(result)

    asyncio.run(main())
    ```
    Пример извлечения атрибутов из списка элементов:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="CLASS_NAME", selector="some_class_name", attribute="text")

    async def main():
        # Получение атрибутов по локатору
        result = await executor.get_attribute_by_locator(locator)
        print(result)

    asyncio.run(main())
    ```

- `get_webelement_by_locator`
```python
async def get_webelement_by_locator(self, locator: SimpleNamespace | dict) -> WebElement | list[WebElement] | None:
    """
    Извлекает веб-элементы на основе предоставленного локатора.

    Args:
        locator (SimpleNamespace | dict): Локатор элемента, который необходимо извлечь.
                                          Может быть представлен в виде SimpleNamespace или dict.

    Returns:
        WebElement | list[WebElement] | None: Найденный веб-элемент или список веб-элементов.
                                                Возвращает None, если элемент не найден.

    Raises:
        Exception: Если возникает ошибка при извлечении веб-элемента.
    """
    ...
```

    **Назначение**: Извлекает веб-элементы на основе предоставленного локатора.

    **Как работает функция**:
    Метод `get_webelement_by_locator` принимает локатор, который может быть представлен в виде объекта `SimpleNamespace` или словаря `dict`. Он определяет тип локатора (`by`) и селектор (`selector`) для поиска веб-элементов. В зависимости от типа локатора, метод использует соответствующие методы Selenium для поиска элемента или списка элементов. Если элемент не найден, метод возвращает `None`.

    **Параметры**:
    - `locator` (SimpleNamespace | dict): Локатор элемента, который необходимо извлечь. Может быть представлен в виде `SimpleNamespace` или `dict`.

    **Возвращает**:
    - `WebElement | list[WebElement] | None`: Найденный веб-элемент или список веб-элементов. Возвращает `None`, если элемент не найден.

    **Вызывает исключения**:
    - `Exception`: Если возникает ошибка при извлечении веб-элемента.

    **Примеры**:
    Пример получения одного веб-элемента:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio
    from selenium.webdriver.remote.webdriver import WebElement

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id")

    async def main():
        # Получение веб-элемента по локатору
        result = await executor.get_webelement_by_locator(locator)
        print(type(result))

    asyncio.run(main())
    ```
    Пример получения списка веб-элементов:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio
    from selenium.webdriver.remote.webdriver import WebElement

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="CLASS_NAME", selector="some_class_name")

    async def main():
        # Получение веб-элементов по локатору
        result = await executor.get_webelement_by_locator(locator)
        print(type(result))

    asyncio.run(main())
    ```

- `get_webelement_as_screenshot`
```python
async def get_webelement_as_screenshot(self, locator: SimpleNamespace | dict) -> str | None:
    """
    Делает скриншот найденного веб-элемента.

    Args:
        locator (SimpleNamespace | dict): Локатор элемента, скриншот которого необходимо сделать.
                                          Может быть представлен в виде SimpleNamespace или dict.

    Returns:
        str | None: Путь к файлу скриншота или None, если элемент не найден.
    """
    ...
```

    **Назначение**: Делает скриншот найденного веб-элемента.

    **Как работает функция**:
    Метод `get_webelement_as_screenshot` принимает локатор, который может быть представлен в виде объекта `SimpleNamespace` или словаря `dict`. Он использует `get_webelement_by_locator` для поиска веб-элемента. Если элемент найден, метод делает скриншот элемента и сохраняет его в файл. Путь к файлу скриншота возвращается. Если элемент не найден, метод возвращает `None`.

    **Параметры**:
    - `locator` (SimpleNamespace | dict): Локатор элемента, скриншот которого необходимо сделать. Может быть представлен в виде `SimpleNamespace` или `dict`.

    **Возвращает**:
    - `str | None`: Путь к файлу скриншота или `None`, если элемент не найден.

    **Вызывает исключения**:
    - Отсутствуют явные исключения, но могут возникнуть исключения при работе с файловой системой или Selenium.

    **Примеры**:
    Пример создания скриншота веб-элемента:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id")

    async def main():
        # Получение скриншота веб-элемента по локатору
        result = await executor.get_webelement_as_screenshot(locator)
        print(result)

    asyncio.run(main())
    ```

- `execute_event`
```python
async def execute_event(self, locator: SimpleNamespace) -> Any:
    """
    Выполняет события, связанные с локатором.

    Args:
        locator (SimpleNamespace): Локатор элемента, событие которого необходимо выполнить.

    Returns:
        Any: Результат выполнения события.
    """
    ...
```

    **Назначение**: Выполняет события, связанные с локатором.

    **Как работает функция**:
    Метод `execute_event` принимает локатор типа `SimpleNamespace`, содержащий информацию о событии, которое необходимо выполнить. Метод извлекает веб-элемент с использованием `get_webelement_by_locator`. Если элемент найден, метод выполняет событие (например, клик, отправка сообщения) на этом элементе. Результат выполнения события возвращается.

    **Параметры**:
    - `locator` (SimpleNamespace): Локатор элемента, событие которого необходимо выполнить.

    **Возвращает**:
    - `Any`: Результат выполнения события.

    **Вызывает исключения**:
    - Могут возникнуть исключения при выполнении события, например, если элемент не найден или событие не может быть выполнено.

    **Примеры**:
    Пример выполнения события `click()` на веб-элементе:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id", event="click()")

    async def main():
        # Выполнение события по локатору
        result = await executor.execute_event(locator)
        print(result)

    asyncio.run(main())
    ```

- `send_message`
```python
async def send_message(self, locator: SimpleNamespace) -> Any:
    """
    Отправляет сообщение веб-элементу.

    Args:
        locator (SimpleNamespace): Локатор элемента, которому необходимо отправить сообщение.

    Returns:
        Any: Результат отправки сообщения.
    """
    ...
```

    **Назначение**: Отправляет сообщение веб-элементу.

    **Как работает функция**:
    Метод `send_message` принимает локатор типа `SimpleNamespace`, содержащий информацию о веб-элементе, которому необходимо отправить сообщение. Метод извлекает веб-элемент с использованием `get_webelement_by_locator`. Если элемент найден, метод отправляет сообщение этому элементу. Результат отправки сообщения возвращается.

    **Параметры**:
    - `locator` (SimpleNamespace): Локатор элемента, которому необходимо отправить сообщение.

    **Возвращает**:
    - `Any`: Результат отправки сообщения.

    **Вызывает исключения**:
    - Могут возникнуть исключения при отправке сообщения, например, если элемент не найден или сообщение не может быть отправлено.

    **Примеры**:
    Пример отправки сообщения веб-элементу:
    ```python
    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from types import SimpleNamespace
    import asyncio

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = SimpleNamespace(by="ID", selector="some_element_id", message="Hello, World!")

    async def main():
        # Отправка сообщения веб-элементу по локатору
        result = await executor.send_message(locator)
        print(result)

    asyncio.run(main())
    ```

### Диаграммы потока

Модуль включает диаграммы потока Mermaid для иллюстрации потока выполнения ключевых методов:

- **`execute_locator`**

  ```mermaid
  graph TD
  Start[Начало] --> CheckLocatorType[Проверка, является ли локатор SimpleNamespace или dict]
  CheckLocatorType --> IsSimpleNamespace{Является ли локатор SimpleNamespace?};
  IsSimpleNamespace -->|Да| UseLocatorAsIs[Использовать локатор как есть];
  IsSimpleNamespace -->|Нет| ConvertDictToSimpleNamespace[Преобразовать dict в SimpleNamespace];
  ConvertDictToSimpleNamespace --> UseLocatorAsIs;
  UseLocatorAsIs --> DefineParseLocator[Определить асинхронную функцию _parse_locator];
  DefineParseLocator --> CheckEventAttributeMandatory{Проверить, есть ли у локатора событие, атрибут или обязательное поле};
  CheckEventAttributeMandatory -->|Нет| ReturnNone[Вернуть None];
  CheckEventAttributeMandatory -->|Да| TryMapByEvaluateAttribute[Попробовать сопоставить by и оценить атрибут];
  TryMapByEvaluateAttribute --> CatchExceptionsAndLog[Перехватить исключения и залогировать при необходимости];
  CatchExceptionsAndLog --> HasEvent{Есть ли у локатора событие?};
  HasEvent -->|Да| ExecuteEvent[Выполнить событие];
  HasEvent -->|Нет| HasAttribute{Есть ли у локатора атрибут?};
  HasAttribute -->|Да| GetAttributeByLocator[Получить атрибут по локатору];
  HasAttribute -->|Нет| GetWebElementByLocator[Получить веб-элемент по локатору];
  ExecuteEvent --> HasEvent;
  HasEvent --> ReturnFinalResult[Вернуть окончательный результат _parse_locator];
  GetAttributeByLocator --> ReturnAttributeResult[Вернуть результат атрибута];
  GetWebElementByLocator --> ReturnWebElementResult[Вернуть результат веб-элемента];
  ReturnAttributeResult --> ReturnFinalResult;
  ReturnWebElementResult --> ReturnFinalResult;
  ReturnFinalResult --> ReturnExecuteLocatorResult[Вернуть результат execute_locator];
  ReturnExecuteLocatorResult --> End[Конец];
  ```

- **`evaluate_locator`**

  ```mermaid
  graph TD
  Start[Начало] --> CheckIfAttributeIsList[Проверка, является ли атрибут списком];
  CheckIfAttributeIsList -->|Да| IterateOverAttributes[Итерация по каждому атрибуту в списке];
  IterateOverAttributes --> CallEvaluateForEachAttribute[Вызов _evaluate для каждого атрибута];
  CallEvaluateForEachAttribute --> ReturnGatheredResults[Вернуть собранные результаты из asyncio.gather];
  CheckIfAttributeIsList -->|Нет| CallEvaluateForSingleAttribute[Вызов _evaluate для одного атрибута];
  CallEvaluateForSingleAttribute --> ReturnEvaluateResult[Вернуть результат _evaluate];
  ReturnEvaluateResult --> End[Конец];
  ReturnGatheredResults --> End;
  ```

- **`get_attribute_by_locator`**

  ```mermaid
  graph TD
  Start[Начало] --> CheckIfLocatorIsSimpleNamespaceOrDict[Проверка, является ли локатор SimpleNamespace или dict];
  CheckIfLocatorIsSimpleNamespaceOrDict -->|Да| ConvertLocatorToSimpleNamespaceIfNeeded[Преобразовать локатор в SimpleNamespace, если необходимо];
  ConvertLocatorToSimpleNamespaceIfNeeded --> CallGetWebElementByLocator[Вызов get_webelement_by_locator];
  CallGetWebElementByLocator --> CheckIfWebElementIsFound{Проверка, найден ли web_element};
  CheckIfWebElementIsFound -->|Нет| LogDebugMessageAndReturn[Залогировать сообщение отладки и вернуть];
  CheckIfWebElementIsFound -->|Да| CheckIfAttributeIsDictionaryLikeString{Проверка, является ли locator.attribute строкой, похожей на словарь};
  CheckIfAttributeIsDictionaryLikeString -->|Да| ParseAttributeStringToDict[Разбор строки locator.attribute в словарь];
  ParseAttributeStringToDict --> CheckIfWebElementIsList{Проверка, является ли web_element списком};
  CheckIfWebElementIsList -->|Да| RetrieveAttributesForEachElementInList[Получение атрибутов для каждого элемента в списке];
  RetrieveAttributesForEachElementInList --> ReturnListOfAttributes[Вернуть список атрибутов];
  CheckIfWebElementIsList -->|Нет| RetrieveAttributesForSingleWebElement[Получение атрибутов для одного web_element];
  RetrieveAttributesForSingleWebElement --> ReturnListOfAttributes;
  CheckIfAttributeIsDictionaryLikeString -->|Нет| CheckIfWebElementIsListAgain{Проверка, является ли web_element списком};
  CheckIfWebElementIsListAgain -->|Да| RetrieveAttributesForEachElementInListAgain[Получение атрибутов для каждого элемента в списке];
  RetrieveAttributesForEachElementInListAgain --> ReturnListOfAttributesOrSingleAttribute[Вернуть список атрибутов или один атрибут];
  CheckIfWebElementIsListAgain -->|Нет| RetrieveAttributeForSingleWebElementAgain[Получение атрибута для одного web_element];
  RetrieveAttributeForSingleWebElementAgain --> ReturnListOfAttributesOrSingleAttribute;
  ReturnListOfAttributesOrSingleAttribute --> End[Конец];
  LogDebugMessageAndReturn --> End;
  ```

## Использование

Для использования этого модуля создайте экземпляр класса `ExecuteLocator` с экземпляром Selenium WebDriver, а затем вызовите различные методы для взаимодействия с веб-элементами на основе предоставленных локаторов.

## Пример

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация класса ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора
locator = {
    "by": "ID",
    "selector": "some_element_id",
    "event": "click()"
}

# Выполнение локатора
result = await executor.execute_locator(locator)
print(result)
```

## Зависимости

- `selenium`: Для веб-автоматизации.
- `asyncio`: Для асинхронных операций.
- `re`: Для регулярных выражений.
- `dataclasses`: Для создания классов данных.
- `enum`: Для создания перечислений.
- `pathlib`: Для обработки путей к файлам.
- `types`: Для создания простых пространств имен.
- `typing`: Для аннотаций типов.