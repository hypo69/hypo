# Модуль для взаимодействия с веб-элементами с использованием Playwright
=====================================================================

Модуль `src.webdriver.playwright.executor` предоставляет функциональные возможности для взаимодействия с веб-элементами, используя Playwright, на основе предоставленных локаторов.
Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

Пример использования
----------------------

```python
from src.webdriver.playwright.executor import PlaywrightExecutor
import asyncio

async def main():
    executor = PlaywrightExecutor()
    await executor.start()
    # <Здесь примеры вызовов функций executor.execute_locator>
    await executor.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

## Обзор

Этот модуль содержит класс `PlaywrightExecutor`, который используется для выполнения команд на основе локаторов в стиле executor, используя Playwright. Он обеспечивает методы для запуска и остановки браузера, выполнения локаторов, получения атрибутов веб-элементов, выполнения событий и навигации по URL-адресам.

## Подробнее

Этот модуль является частью системы автоматизации тестирования и веб-скрейпинга, где требуется взаимодействие с веб-страницами с использованием Playwright. Он предоставляет удобный интерфейс для выполнения различных действий с веб-элементами на основе их локаторов.

## Классы

### `PlaywrightExecutor`

**Описание**:
Класс `PlaywrightExecutor` предназначен для выполнения команд на основе executor-style locator commands с использованием Playwright.

**Принцип работы**:
Класс инициализирует Playwright и запускает экземпляр браузера. Он предоставляет методы для выполнения действий с веб-элементами, получения атрибутов, выполнения событий и навигации по URL-адресам.

**Методы**:

- `__init__(self, browser_type: str = 'chromium', **kwargs)`: Инициализирует экземпляр класса `PlaywrightExecutor`.
- `start(self) -> None`: Запускает Playwright и запускает экземпляр браузера.
- `stop(self) -> None`: Закрывает браузер Playwright и останавливает его экземпляр.
- `execute_locator(self, locator: Union[dict, SimpleNamespace], message: Optional[str] = None, typing_speed: float = 0, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = 'presence_of_element_located') -> Union[str, list, dict, Locator, bool, None]`: Выполняет действия с веб-элементом на основе предоставленного локатора.
- `evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`: Вычисляет и обрабатывает атрибуты локатора.
- `get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]`: Получает указанный атрибут из веб-элемента.
- `get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]`: Получает веб-элемент, используя локатор.
- `get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]`: Делает снимок экрана найденного веб-элемента.
- `execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]`: Выполняет событие, связанное с локатором.
- `send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool`: Отправляет сообщение веб-элементу.
- `goto(self, url: str) -> None`: Переходит по указанному URL-адресу.

## Функции

### `__init__`

```python
def __init__(self, browser_type: str = 'chromium', **kwargs):
    """
    Initializes the Playwright executor.

    Args:
        browser_type: Type of browser to launch (e.g., 'chromium', 'firefox', 'webkit').
    """
    self.driver = None
    self.browser_type = browser_type
    self.page: Optional[Page] = None
    self.config: SimpleNamespace = j_loads_ns(
        Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
    )
```

**Назначение**:
Инициализирует экземпляр класса `PlaywrightExecutor`.

**Параметры**:
- `browser_type` (str): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `**kwargs`: Дополнительные аргументы.

**Как работает функция**:
1. Инициализирует драйвер `self.driver` значением `None`.
2. Устанавливает тип браузера `self.browser_type` в соответствии с переданным параметром `browser_type`.
3. Инициализирует `self.page` значением `None`.
4. Загружает конфигурацию из файла `playwrid.json` и сохраняет ее в `self.config`.

```
Инициализация PlaywrightExecutor
│
├── Установка типа браузера
│
├── Загрузка конфигурации
│
└── Конец
```

**Примеры**:

```python
executor = PlaywrightExecutor(browser_type='firefox')
```

### `start`

```python
async def start(self) -> None:
    """
    Initializes Playwright and launches a browser instance.
    """
    try:
        self.driver = await async_playwright().start()
        browser = await getattr(self.driver, self.browser_type).launch(headless=True, args=self.config.options)
        self.page = await browser.new_page()
    except Exception as ex:
        logger.critical('Playwright failed to start browser', ex)
```

**Назначение**:
Запускает Playwright и запускает экземпляр браузера.

**Как работает функция**:
1. Пытается запустить Playwright и получить драйвер.
2. Запускает браузер указанного типа (из `self.browser_type`) в режиме headless с использованием опций из конфигурации (`self.config.options`).
3. Создает новую страницу в браузере и сохраняет ее в `self.page`.
4. В случае возникновения ошибки логирует критическую ошибку.

```
Запуск Playwright
│
├── Запуск Playwright
│
├── Запуск браузера
│
├── Создание новой страницы
│
└── Обработка ошибок
```

**Примеры**:

```python
async def main():
    executor = PlaywrightExecutor()
    await executor.start()
    await executor.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

### `stop`

```python
async def stop(self) -> None:
    """
    Closes Playwright browser and stops its instance.
    """
    try:
        if self.page:
            await self.page.close()
        if self.driver:
            await self.driver.stop()
            self.driver = None
        logger.info('Playwright stopped')
    except Exception as ex:
        logger.error(f'Playwright failed to close browser: {ex}')
```

**Назначение**:
Закрывает браузер Playwright и останавливает его экземпляр.

**Как работает функция**:
1. Проверяет, существует ли страница (`self.page`) и закрывает ее, если она существует.
2. Проверяет, существует ли драйвер (`self.driver`) и останавливает его, если он существует.
3. Устанавливает `self.driver` в `None`.
4. Логирует информационное сообщение об остановке Playwright.
5. В случае возникновения ошибки логирует ошибку.

```
Остановка Playwright
│
├── Закрытие страницы
│
├── Остановка драйвера
│
├── Сброс драйвера
│
├── Логирование информации
│
└── Обработка ошибок
```

**Примеры**:

```python
async def main():
    executor = PlaywrightExecutor()
    await executor.start()
    await executor.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

### `execute_locator`

```python
async def execute_locator(
        self,
        locator: Union[dict, SimpleNamespace],
        message: Optional[str] = None,
        typing_speed: float = 0,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
) -> Union[str, list, dict, Locator, bool, None]:
    """
    Executes actions on a web element based on the provided locator.

    Args:
        locator: Locator data (dict or SimpleNamespace).
        message: Optional message for events.
        typing_speed: Optional typing speed for events.
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').

    Returns:
         The result of the operation, which can be a string, list, dict, Locator, bool, or None.
    """
    if isinstance(locator, dict):
        locator = SimpleNamespace(**locator)

    if not getattr(locator, "attribute", None) and not getattr(locator, "selector", None):
        logger.debug("Empty locator provided.")
        return None

    async def _parse_locator(
            locator: SimpleNamespace, message: Optional[str]
    ) -> Union[str, list, dict, Locator, bool, None]:
        """Parses and executes locator instructions."""
        if locator.event and locator.attribute and locator.mandatory is None:
            logger.debug("Locator with event and attribute but missing mandatory flag. Skipping.")
            return None

        if isinstance(locator.attribute, str) and isinstance(locator.by, str):
            try:
                if locator.attribute:
                    locator.attribute = await self.evaluate_locator(locator.attribute)
                    if locator.by == "VALUE":
                        return locator.attribute
            except Exception as ex:
                logger.debug(f"Error getting attribute by \'VALUE\': {locator}, error: {ex}")
                return None

            if locator.event:
                return await self.execute_event(locator, message, typing_speed)

            if locator.attribute:
                return await self.get_attribute_by_locator(locator)

            return await self.get_webelement_by_locator(locator)

        elif isinstance(locator.selector, list) and isinstance(locator.by, list):
            if locator.sorted == "pairs":
                elements_pairs = []

                for attribute, by, selector, event, timeout, timeout_for_event, locator_description in zip(
                    locator.attribute,
                    locator.by,
                    locator.selector,
                    locator.event,
                    locator.timeout,
                    locator.timeout_for_event,
                    locator.locator_description,
                ):
                    l = SimpleNamespace(
                        **{\
                            "attribute": attribute,
                            "by": by,
                            "selector": selector,
                            "event": event,
                            "timeout": timeout,
                            "timeout_for_event": timeout_for_event,
                            "locator_description": locator_description,
                        }\
                    )
                    elements_pairs.append(await _parse_locator(l, message))

                from itertools import zip_longest
                zipped_pairs = list(zip_longest(*elements_pairs, fillvalue=None))
                return zipped_pairs

        else:
            logger.warning("Locator does not contain \'selector\' and \'by\' lists or invalid \'sorted\' value.")

    return await _parse_locator(locator, message)
```

**Назначение**:
Выполняет действия с веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора (словарь или SimpleNamespace).
- `message` (Optional[str]): Необязательное сообщение для событий.
- `typing_speed` (float): Необязательная скорость набора текста для событий.
- `timeout` (Optional[float]): Время ожидания для поиска элемента (в секундах).
- `timeout_for_event` (Optional[str]): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, Locator, булевым значением или None.

**Как работает функция**:
1. Преобразует локатор в `SimpleNamespace`, если он является словарем.
2. Проверяет, что локатор не пустой (содержит `attribute` или `selector`).
3. Определяет внутреннюю асинхронную функцию `_parse_locator`, которая выполняет разбор и выполнение инструкций локатора.
4. В `_parse_locator` проверяется наличие атрибутов `event`, `attribute` и `mandatory` и, в зависимости от их значений, выполняет различные действия:
    - Если `locator.attribute` и `locator.by` являются строками, пытается получить атрибут элемента.
    - Если `locator.by` равен "VALUE", возвращает значение атрибута.
    - Если есть событие (`locator.event`), выполняет его с помощью `self.execute_event`.
    - Если есть атрибут (`locator.attribute`), получает его с помощью `self.get_attribute_by_locator`.
    - В противном случае получает веб-элемент с помощью `self.get_webelement_by_locator`.
5. Если `locator.selector` и `locator.by` являются списками, обрабатывает их как пары и выполняет рекурсивный вызов `_parse_locator` для каждой пары.
6. Если локатор не содержит списков `selector` и `by` или значение `sorted` неверно, выводит предупреждение.
7. Возвращает результат выполнения `_parse_locator`.

**Внутренние функции**:

- `_parse_locator(locator: SimpleNamespace, message: Optional[str]) -> Union[str, list, dict, Locator, bool, None]`:
    **Назначение**: Разбирает и выполняет инструкции локатора.

    **Параметры**:
    - `locator` (SimpleNamespace): Данные локатора.
    - `message` (Optional[str]): Необязательное сообщение для событий.

    **Возвращает**:
    - `Union[str, list, dict, Locator, bool, None]`: Результат операции.

    **Как работает функция**:
    1. Проверяет наличие атрибутов `event`, `attribute` и `mandatory` и, в зависимости от их значений, выполняет различные действия.
    2. Если `locator.attribute` и `locator.by` являются строками, пытается получить атрибут элемента.
    3. Если есть событие (`locator.event`), выполняет его с помощью `self.execute_event`.
    4. Если есть атрибут (`locator.attribute`), получает его с помощью `self.get_attribute_by_locator`.
    5. В противном случае получает веб-элемент с помощью `self.get_webelement_by_locator`.
    6. Если `locator.selector` и `locator.by` являются списками, обрабатывает их как пары и выполняет рекурсивный вызов `_parse_locator` для каждой пары.
    7. Если локатор не содержит списков `selector` и `by` или значение `sorted` неверно, выводит предупреждение.

```
Выполнение локатора
│
├── Преобразование локатора в SimpleNamespace (если это словарь)
│
├── Проверка на пустой локатор
│
├── _parse_locator (Внутренняя функция)
│   │
│   ├── Проверка атрибутов event, attribute и mandatory
│   │
│   ├── Если locator.attribute и locator.by - строки
│   │   ├── Получение атрибута элемента
│   │   ├── Если locator.by == "VALUE"
│   │   │   └── Возврат значения атрибута
│   │   ├── Если есть событие
│   │   │   └── Выполнение события
│   │   ├── Если есть атрибут
│   │   │   └── Получение атрибута
│   │   └── Получение веб-элемента
│   │
│   ├── Если locator.selector и locator.by - списки
│   │   └── Обработка как пары и рекурсивный вызов _parse_locator
│   │
│   └── Если локатор не содержит списков selector и by или значение sorted неверно
│       └── Вывод предупреждения
│
└── Возврат результата выполнения _parse_locator
```

**Примеры**:

```python
locator_data = {
    "by": "XPATH",
    "selector": "//button[@id='myButton']",
    "event": "click()"
}
result = await executor.execute_locator(locator_data)

locator_data = {
    "by": "XPATH",
    "selector": "//input[@id='myInput']",
    "attribute": "value"
}
result = await executor.execute_locator(locator_data)
```

### `evaluate_locator`

```python
async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Evaluates and processes locator attributes.

    Args:
        attribute: Attribute to evaluate (can be a string, list of strings, or a dictionary).

    Returns:
        The evaluated attribute, which can be a string, list of strings, or dictionary.
    """

    async def _evaluate(attr: str) -> Optional[str]:
        return attr

    if isinstance(attribute, list):
        return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
    return await _evaluate(str(attribute))
```

**Назначение**:
Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для вычисления (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Как работает функция**:
1. Определяет внутреннюю асинхронную функцию `_evaluate`, которая возвращает переданный атрибут.
2. Если атрибут является списком, применяет функцию `_evaluate` к каждому элементу списка и возвращает список результатов.
3. Если атрибут не является списком, преобразует его в строку и возвращает результат `_evaluate`.

**Внутренние функции**:

- `_evaluate(attr: str) -> Optional[str]`:
    **Назначение**: Возвращает переданный атрибут.

    **Параметры**:
    - `attr` (str): Атрибут.

    **Возвращает**:
    - `Optional[str]`: Атрибут.

```
Вычисление атрибута локатора
│
├── Определение внутренней функции _evaluate
│
├── Если атрибут - список
│   └── Применение _evaluate к каждому элементу списка
│
└── Если атрибут не список
    └── Преобразование атрибута в строку и применение _evaluate
```

**Примеры**:

```python
attribute = "id"
result = await executor.evaluate_locator(attribute)

attribute = ["id", "name"]
result = await executor.evaluate_locator(attribute)
```

### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
    """
    Gets the specified attribute from the web element.

    Args:
        locator: Locator data (dict or SimpleNamespace).

    Returns:
        Attribute or None.
    """
    locator = (
        locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator, dict) else None
    )
    element = await self.get_webelement_by_locator(locator)

    if not element:
        logger.debug(f"Element not found: {locator=}")
        return None

    def _parse_dict_string(attr_string: str) -> dict | None:
        """Parses a string like '{attr1:attr2}' into a dictionary."""
        try:
            return {k.strip(): v.strip() for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))}\
        except ValueError as ex:
            logger.debug(f"Invalid attribute string format: {attr_string}", ex)
            return None

    async def _get_attribute(el: Locator, attr: str) -> Optional[str]:
        """Retrieves a single attribute from a Locator."""
        try:
            return await el.get_attribute(attr)
        except Exception as ex:
            logger.debug(f"Error getting attribute '{attr}' from element: {ex}")
            return None

    async def _get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict:
        """Retrieves multiple attributes based on a dictionary."""
        result = {}
        for key, value in attr_dict.items():
            result[key] = await _get_attribute(element, key)
            result[value] = await _get_attribute(element, value)

        return result

    if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
        attr_dict = _parse_dict_string(locator.attribute)
        if attr_dict:
            if isinstance(element, list):
                return await asyncio.gather(*[_get_attributes_from_dict(el, attr_dict) for el in element])
            return await _get_attributes_from_dict(element, attr_dict)

    if isinstance(element, list):
         return await asyncio.gather(*[_get_attribute(el, locator.attribute) for el in element])

    return await _get_attribute(element, locator.attribute)
```

**Назначение**:
Получает указанный атрибут из веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Атрибут или None.

**Как работает функция**:
1. Преобразует локатор в `SimpleNamespace`, если он является словарем.
2. Получает веб-элемент с помощью `self.get_webelement_by_locator`.
3. Если элемент не найден, логирует отладочное сообщение и возвращает None.
4. Определяет внутреннюю функцию `_parse_dict_string`, которая преобразует строку типа '{attr1:attr2}' в словарь.
5. Определяет внутреннюю асинхронную функцию `_get_attribute`, которая получает значение атрибута из элемента.
6. Определяет внутреннюю асинхронную функцию `_get_attributes_from_dict`, которая получает несколько атрибутов на основе словаря.
7. Если `locator.attribute` является строкой и начинается с "{", преобразует строку в словарь и получает атрибуты на основе этого словаря.
8. Если элемент является списком, получает атрибуты для каждого элемента списка.
9. В противном случае получает атрибут из элемента.

**Внутренние функции**:

- `_parse_dict_string(attr_string: str) -> dict | None`:
    **Назначение**: Преобразует строку типа '{attr1:attr2}' в словарь.

    **Параметры**:
    - `attr_string` (str): Строка для преобразования.

    **Возвращает**:
    - `dict | None`: Словарь или None в случае ошибки.

    **Как работает функция**:
    1. Пытается преобразовать строку в словарь, разделяя ее по символам ":" и ",".
    2. В случае ошибки логирует отладочное сообщение и возвращает None.

- `_get_attribute(el: Locator, attr: str) -> Optional[str]`:
    **Назначение**: Получает значение атрибута из элемента.

    **Параметры**:
    - `el` (Locator): Элемент.
    - `attr` (str): Атрибут.

    **Возвращает**:
    - `Optional[str]`: Значение атрибута или None в случае ошибки.

    **Как работает функция**:
    1. Пытается получить значение атрибута из элемента.
    2. В случае ошибки логирует отладочное сообщение и возвращает None.

- `_get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict`:
    **Назначение**: Получает несколько атрибутов на основе словаря.

    **Параметры**:
    - `element` (Locator): Элемент.
    - `attr_dict` (dict): Словарь атрибутов.

    **Возвращает**:
    - `dict`: Словарь значений атрибутов.

    **Как работает функция**:
    1. Получает значение каждого атрибута из словаря и сохраняет его в результирующем словаре.

```
Получение атрибута по локатору
│
├── Преобразование локатора в SimpleNamespace (если это словарь)
│
├── Получение веб-элемента
│
├── Если элемент не найден
│   └── Логирование отладочного сообщения и возврат None
│
├── _parse_dict_string (Внутренняя функция)
│   └── Преобразование строки типа '{attr1:attr2}' в словарь
│
├── _get_attribute (Внутренняя функция)
│   └── Получение значения атрибута из элемента
│
├── _get_attributes_from_dict (Внутренняя функция)
│   └── Получение нескольких атрибутов на основе словаря
│
├── Если locator.attribute является строкой и начинается с "{"
│   └── Преобразование строки в словарь и получение атрибутов на основе этого словаря
│
├── Если элемент является списком
│   └── Получение атрибутов для каждого элемента списка
│
└── Получение атрибута из элемента
```

**Примеры**:

```python
locator_data = {
    "by": "XPATH",
    "selector": "//input[@id='myInput']",
    "attribute": "value"
}
result = await executor.get_attribute_by_locator(locator_data)

locator_data = {
    "by": "XPATH",
    "selector": "//div[@class='myDiv']",
    "attribute": "{title:aria-label}"
}
result = await executor.get_attribute_by_locator(locator_data)
```

### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
    """
    Gets a web element using the locator.

    Args:
        locator: Locator data (dict or SimpleNamespace).

    Returns:
        Playwright Locator
    """
    locator = (
        SimpleNamespace(**locator)\
        if isinstance(locator, dict)\
        else locator
    )
    if not locator:
        logger.error("Invalid locator provided.")
        return None
    try:
         if locator.by.upper() == "XPATH":
            elements = self.page.locator(f'xpath={locator.selector}')
         else:
             elements = self.page.locator(locator.selector)

         if locator.if_list == 'all':
            return await elements.all()
         elif locator.if_list == 'first':
             return elements.first
         elif locator.if_list == 'last':
            return elements.last
         elif locator.if_list == 'even':
            list_elements = await elements.all()
            return [list_elements[i] for i in range(0, len(list_elements), 2)]
         elif locator.if_list == 'odd':
            list_elements = await elements.all()
            return [list_elements[i] for i in range(1, len(list_elements), 2)]
         elif isinstance(locator.if_list, list):
             list_elements = await elements.all()
             return [list_elements[i] for i in locator.if_list]
         elif isinstance(locator.if_list, int):
             list_elements = await elements.all()
             return list_elements[locator.if_list - 1]
         else:
             return elements
    except Exception as ex:
        logger.error(f'Ошибка поиска элемента: {locator=}', ex)
        return None
```

**Назначение**:
Получает веб-элемент, используя локатор.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).

**Возвращает**:
- `Optional[Locator | List[Locator]]`: Playwright Locator.

**Как работает функция**:
1. Преобразует локатор в `SimpleNamespace`, если он является словарем.
2. Проверяет, что локатор не пустой.
3. В зависимости от значения `locator.by` ищет элементы на странице:
    - Если `locator.by` равен "XPATH", использует XPath для поиска элементов.
    - В противном случае использует CSS-селектор для поиска элементов.
4. В зависимости от значения `locator.if_list` возвращает:
    - Все элементы, если `locator.if_list` равен "all".
    - Первый элемент, если `locator.if_list` равен "first".
    - Последний элемент, если `locator.if_list` равен "last".
    - Четные элементы, если `locator.if_list` равен "even".
    - Нечетные элементы, если `locator.if_list` равен "odd".
    - Элементы по индексам из списка, если `locator.if_list` является списком.
    - Элемент по индексу, если `locator.if_list` является целым числом.
    - Все найденные элементы, если `locator.if_list` не указан.
5. В случае ошибки логирует ошибку и возвращает None.

```
Получение веб-элемента по локатору
│
├── Преобразование локатора в SimpleNamespace (если это словарь)
│
├── Проверка на пустой локатор
│
├── В зависимости от значения locator.by
│   ├── Если locator.by == "XPATH"
│   │   └── Поиск элементов с использованием XPath
│   └── Поиск элементов с использованием CSS-селектора
│
├── В зависимости от значения locator.if_list
│   ├── Если locator.if_list == "all"
│   │   └── Возврат всех элементов
│   ├── Если locator.if_list == "first"
│   │   └── Возврат первого элемента
│   ├── Если locator.if_list == "last"
│   │   └── Возврат последнего элемента
│   ├── Если locator.if_list == "even"
│   │   └── Возврат четных элементов
│   ├── Если locator.if_list == "odd"
│   │   └── Возврат нечетных элементов
│   ├── Если locator.if_list - список
│   │   └── Возврат элементов по индексам из списка
│   ├── Если locator.if_list - целое число
│   │   └── Возврат элемента по индексу
│   └── Возврат всех найденных элементов
│
└── Обработка ошибок
```

**Примеры**:

```python
locator_data = {
    "by": "XPATH",
    "selector": "//button[@id='myButton']"
}
element = await executor.get_webelement_by_locator(locator_data)

locator_data = {
    "by": "CSS",
    "selector": ".myClass",
    "if_list": "all"
}
elements = await executor.get_webelement_by_locator(locator_data)
```

### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
    """
    Takes a screenshot of the located web element.

    Args:
        locator: Locator data (dict or SimpleNamespace).
        webelement: The web element Locator.

    Returns:
         Screenshot in bytes or None.
    """
    locator = (
        locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator, dict) else None
    )

    if not webelement:
        webelement = await self.get_webelement_by_locator(locator)

    if not webelement:
        logger.debug(f"Element not found for screenshot: {locator=}")
        return None
    try:
         return await webelement.screenshot()
    except Exception as ex:
        logger.error(f"Failed to take screenshot: {locator=}", ex)
        return None
```

**Назначение**:
Делает снимок экрана найденного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
- `webelement` (Optional[Locator]): Веб-элемент Locator.

**Возвращает**:
- `Optional[bytes]`: Снимок экрана в байтах или None.

**Как работает функция**:
1. Преобразует локатор в `SimpleNamespace`, если он является словарем.
2. Если `webelement` не передан, получает его с помощью `self.get_webelement_by_locator`.
3. Если элемент не найден, логирует отладочное сообщение и возвращает None.
4. Пытается сделать снимок экрана элемента и возвращает его в байтах.
5. В случае ошибки логирует ошибку и возвращает None.

```
Получение снимка экрана веб-элемента
│
├── Преобразование локатора в SimpleNamespace (если это словарь)
│
├── Если webelement не передан
│   └── Получение веб-элемента
│
├── Если элемент не найден
│   └── Логирование отладочного сообщения и возврат None
│
├── Попытка сделать снимок экрана элемента
│
└── Обработка ошибок
```

**Примеры**:

```python
locator_data = {
    "by": "XPATH",
    "selector": "//div[@id='myDiv']"
}
screenshot = await executor.get_webelement_as_screenshot(locator_data)
```

### `execute_event`

```python
async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]: