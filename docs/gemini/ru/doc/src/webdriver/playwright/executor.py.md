# Модуль playwright.executor

## Обзор

Модуль `playwright.executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Playwright на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробней

Этот модуль предназначен для выполнения действий над веб-элементами с использованием библиотеки Playwright. Он предоставляет класс `PlaywrightExecutor`, который инициализирует Playwright, запускает браузер и предоставляет методы для выполнения различных действий, таких как клики, ввод текста, получение атрибутов и создание скриншотов элементов.
Модуль использует `SimpleNamespace` для хранения и передачи данных локаторов, что обеспечивает гибкость и удобство в работе с различными типами локаторов и атрибутов.

## Классы

### `PlaywrightExecutor`

**Описание**:
Класс `PlaywrightExecutor` выполняет команды на основе команд локатора в стиле исполнителя, используя Playwright.

**Как работает класс**:
Класс инициализируется с типом браузера (по умолчанию 'chromium') и дополнительными аргументами. Он предоставляет методы для запуска и остановки Playwright, выполнения действий с локаторами, оценки атрибутов локаторов, получения веб-элементов и выполнения событий, связанных с локаторами.

**Методы**:

- `__init__(self, browser_type: str = 'chromium', **kwargs)`: Инициализирует экземпляр класса `PlaywrightExecutor`.
- `start(self) -> None`: Запускает Playwright и инициализирует браузер.
- `stop(self) -> None`: Закрывает браузер Playwright и останавливает его экземпляр.
- `execute_locator(self, locator: Union[dict, SimpleNamespace], message: Optional[str] = None, typing_speed: float = 0, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = 'presence_of_element_located') -> Union[str, list, dict, Locator, bool, None]`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]`: Получает указанный атрибут из веб-элемента.
- `get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]`: Получает веб-элемент, используя локатор.
- `get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]`: Делает скриншот найденного веб-элемента.
- `execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]`: Выполняет событие, связанное с локатором.
- `send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool`: Отправляет сообщение веб-элементу.
- `goto(self, url: str) -> None`: Переходит по указанному URL.

### `__init__`

```python
    def __init__(self, browser_type: str = 'chromium', **kwargs):
        """
        Initializes the Playwright executor.

        Args:
            browser_type: Type of browser to launch (e.g., \'chromium\', \'firefox\', \'webkit\').
        """
        self.driver = None
        self.browser_type = browser_type
        self.page: Optional[Page] = None
        self.config: SimpleNamespace = j_loads_ns(
            Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        )
```

**Назначение**:
Инициализирует класс `PlaywrightExecutor`.

**Как работает функция**:
Функция инициализирует драйвер Playwright, устанавливает тип браузера, создает экземпляр страницы и загружает конфигурацию Playwright из файла `playwrid.json`.

**Параметры**:
- `browser_type` (str): Тип запускаемого браузера (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `**kwargs`:  Дополнительные аргументы.

**Возвращает**:
- None

**Вызывает исключения**:
- None

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
Запускает Playwright и инициализирует браузер.

**Как работает функция**:
Функция запускает асинхронный Playwright, запускает указанный тип браузера (headless mode) и создает новую страницу. В случае ошибки логирует критическое сообщение об ошибке.

**Параметры**:
- None

**Возвращает**:
- None

**Вызывает исключения**:
- Exception: Если не удается запустить браузер Playwright.

**Примеры**:
```python
await executor.start()
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
Функция закрывает текущую страницу, останавливает драйвер Playwright и устанавливает его в `None`. В случае ошибки логирует сообщение об ошибке.

**Параметры**:
- None

**Возвращает**:
- None

**Вызывает исключения**:
- Exception: Если не удается закрыть браузер Playwright.

**Примеры**:
```python
await executor.stop()
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').

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
                            **{
                                "attribute": attribute,
                                "by": by,
                                "selector": selector,
                                "event": event,
                                "timeout": timeout,
                                "timeout_for_event": timeout_for_event,
                                "locator_description": locator_description,
                            }
                        )
                        elements_pairs.append(await _parse_locator(l, message))

                    zipped_pairs = list(zip_longest(*elements_pairs, fillvalue=None))
                    return zipped_pairs

            else:
                logger.warning("Locator does not contain \'selector\' and \'by\' lists or invalid \'sorted\' value.")

        return await _parse_locator(locator, message)
```

**Назначение**:
Выполняет действия над веб-элементом на основе предоставленного локатора.

**Как работает функция**:
Функция принимает локатор в виде словаря или `SimpleNamespace`, преобразует его в `SimpleNamespace`, если это словарь. Затем проверяет наличие атрибута и селектора в локаторе. Если локатор не содержит атрибута или селектора, возвращает `None`.
Внутренняя асинхронная функция `_parse_locator` выполняет разбор инструкций локатора. Если локатор содержит событие и атрибут, но отсутствует обязательный флаг, возвращает `None`. Если атрибут и `by` являются строками, пытается получить атрибут элемента. Если `by` равен "VALUE", возвращает атрибут. Если указано событие, выполняет событие с помощью `execute_event`. Если атрибут присутствует, получает атрибут с помощью `get_attribute_by_locator`. В противном случае получает веб-элемент с помощью `get_webelement_by_locator`.
Если селектор и `by` являются списками и `sorted` равен "pairs", создает пары элементов и выполняет рекурсивный разбор для каждой пары. Если локатор не содержит списки селекторов и `by` или значение `sorted` неверно, записывает предупреждение в лог.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора.
- `message` (Optional[str]): Опциональное сообщение для событий.
- `typing_speed` (float): Опциональная скорость печати для событий.
- `timeout` (Optional[float]): Время ожидания для поиска элемента (в секундах).
- `timeout_for_event` (Optional[str]): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located').

**Возвращает**:
- Union[str, list, dict, Locator, bool, None]: Результат операции, который может быть строкой, списком, словарем, локатором, булевым значением или `None`.

**Вызывает исключения**:
- None

**Примеры**:
```python
locator_data = {'selector': '//button', 'by': 'xpath', 'event': 'click()'}
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

        if isinstance(attribute, list):\
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(str(attribute))
```

**Назначение**:
Оценивает и обрабатывает атрибуты локатора.

**Как работает функция**:
Функция принимает атрибут, который может быть строкой, списком строк или словарем. Внутренняя асинхронная функция `_evaluate` просто возвращает переданный атрибут. Если атрибут является списком, функция использует `asyncio.gather` для параллельной оценки каждого атрибута в списке.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для оценки.

**Возвращает**:
- Optional[str | List[str] | dict]: Оцененный атрибут, который может быть строкой, списком строк или словарем.

**Вызывает исключения**:
- None

**Примеры**:
```python
attribute = 'text'
evaluated_attribute = await executor.evaluate_locator(attribute)
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
            """Parses a string like \'{attr1:attr2}\' into a dictionary."""
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
                logger.debug(f"Error getting attribute \'{attr}\' from element: {ex}")
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

**Как работает функция**:
Функция принимает локатор, преобразует его в `SimpleNamespace`, если это необходимо, и получает веб-элемент с помощью `get_webelement_by_locator`. Если элемент не найден, возвращает `None`.
Внутренняя функция `_parse_dict_string` разбирает строку типа '{attr1:attr2}' в словарь. Асинхронная функция `_get_attribute` получает один атрибут из локатора. Асинхронная функция `_get_attributes_from_dict` получает несколько атрибутов на основе словаря.
Если атрибут локатора является строкой и начинается с '{', разбирает строку в словарь и получает атрибуты на основе словаря. Если элемент является списком, получает атрибуты для каждого элемента в списке. В противном случае получает атрибут для одного элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:
- Optional[str | List[str] | dict]: Атрибут или `None`.

**Вызывает исключения**:
- None

**Примеры**:
```python
locator_data = {'selector': '//input', 'by': 'xpath', 'attribute': 'value'}
attribute = await executor.get_attribute_by_locator(locator_data)
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
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
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

**Как работает функция**:
Функция принимает локатор, преобразует его в `SimpleNamespace`, если это необходимо. Если локатор недействителен, записывает ошибку в лог и возвращает `None`. В зависимости от значения `locator.by` использует `xpath` или `locator.selector` для поиска элементов. Если `locator.if_list` равен 'all', возвращает все элементы. Если `locator.if_list` равен 'first', возвращает первый элемент. Если `locator.if_list` равен 'last', возвращает последний элемент. Если `locator.if_list` равен 'even', возвращает элементы с четными индексами. Если `locator.if_list` равен 'odd', возвращает элементы с нечетными индексами. Если `locator.if_list` является списком, возвращает элементы с индексами из списка. Если `locator.if_list` является целым числом, возвращает элемент с указанным индексом.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:
- Optional[Locator | List[Locator]]: Playwright Locator.

**Вызывает исключения**:
- Exception: Если происходит ошибка при поиске элемента.

**Примеры**:
```python
locator_data = {'selector': '//button', 'by': 'xpath'}
element = await executor.get_webelement_by_locator(locator_data)
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
Делает скриншот найденного веб-элемента.

**Как работает функция**:
Функция принимает локатор и опциональный веб-элемент. Если веб-элемент не предоставлен, пытается получить его с помощью `get_webelement_by_locator`. Если элемент не найден, записывает отладочное сообщение в лог и возвращает `None`. В противном случае делает скриншот элемента и возвращает его в виде байтов.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `webelement` (Optional[Locator]): Веб-элемент Locator.

**Возвращает**:
- Optional[bytes]: Скриншот в виде байтов или `None`.

**Вызывает исключения**:
- Exception: Если не удается сделать скриншот.

**Примеры**:
```python
locator_data = {'selector': '//div', 'by': 'xpath'}
screenshot = await executor.get_webelement_as_screenshot(locator_data)
```

### `execute_event`

```python
    async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]:
        """
        Executes the event associated with the locator.

         Args:
            locator: Locator data (dict or SimpleNamespace).
            message: Optional message for events.
            typing_speed: Optional typing speed for events.

        Returns:
           Execution status.
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )
        events = str(locator.event).split(";")
        result: list = []
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f"Element for event not found: {locator=}")
            return False

        element = element[0] if isinstance(element, list) else element

        for event in events:
            if event == "click()":
                try:
                    await element.click()
                    continue
                except Exception as ex:
                     logger.error(f"Error during click event: {locator=}", ex)
                     return False

            elif event.startswith("pause("):
                match = re.match(r"pause\\((\\d+)\\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    continue
                logger.debug(f"Pause event parsing failed: {locator=}")
                return False

            elif event == "upload_media()":
                if not message:
                    logger.debug(f"Message is required for upload_media event: {message!r}")
                    return False
                try:
                    await element.set_input_files(message)
                    continue
                except Exception as ex:
                     logger.error(f"Error during file upload: {locator=}, {message=}", ex)
                     return False

            elif event == "screenshot()":
                 try:
                     result.append(await self.get_webelement_as_screenshot(locator, webelement=element))
                 except Exception as ex:
                      logger.error(f"Error during taking screenshot: {locator=}", ex)
                      return False

            elif event == "clear()":
                 try:
                     await element.clear()
                     continue
                 except Exception as ex:
                      logger.error(f"Error during clearing field: {locator=}", ex)
                      return False

            elif event.startswith("send_keys("):\
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                    for key in keys_to_send:
                        key = key.strip().strip("\'")
                        if key:
                            await element.type(key)
                except Exception as ex:
                    logger.error(f"Error sending keys: {locator=}", ex)
                    return False

            elif event.startswith("type("):
                message = event.replace("type(", "").replace(")", "")
                if typing_speed:
                     for character in message:
                         await element.type(character)
                         await asyncio.sleep(typing_speed)
                else:
                    await element.type(message)
        return result if result else True
```

**Назначение**:
Выполняет событие, связанное с локатором.

**Как работает функция**:
Функция принимает локатор, опциональное сообщение и скорость печати. Преобразует локатор в `SimpleNamespace`, если это необходимо. Разбивает строку `locator.event` на список событий. Получает веб-элемент с помощью `get_webelement_by_locator`. Если элемент не найден, записывает отладочное сообщение в лог и возвращает `False`. Для каждого события выполняет соответствующее действие:
- "click()": Кликает на элемент.
- "pause(duration)": Приостанавливает выполнение на указанное время.
- "upload_media()": Загружает медиафайл, используя сообщение.
- "screenshot()": Делает скриншот элемента.
- "clear()": Очищает поле элемента.
- "send_keys(keys)": Отправляет клавиши элементу.
- "type(message)": Вводит сообщение в элемент.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str]): Опциональное сообщение для событий.
- `typing_speed` (float): Опциональная скорость печати для событий.

**Возвращает**:
- Union[str, List[str], bytes, List[bytes], bool]: Статус выполнения.

**Вызывает исключения**:
- Exception: Если происходит ошибка во время выполнения события.

**Примеры**:
```python
locator_data = {'selector': '//button', 'by': 'xpath', 'event': 'click()'}
result = await executor.execute_event(locator_data)
```

### `send_message`

```python
    async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
        """Sends a message to a web element.

        Args:
             locator: Information about the element\'s location on the page.
             message: The message to be sent to the web element.
             typing_speed: Speed of typing the message in seconds.

        Returns:
            Returns `True` if the message was sent successfully, `False` otherwise.
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )
        element = await self.get_webelement_by_locator(locator)
        if not element or (isinstance(element, list) and len(element) == 0):
             logger.debug(f"Element for send message not found: {locator=}")
             return False
        element = element[0] if isinstance(element, list) else element

        if typing_speed:
            for character in message:
                await element.type(character)
                await asyncio.sleep(typing_speed)
        else:
             await element.type(message)

        return True
```

**Назначение**:
Отправляет сообщение веб-элементу.

**Как работает функция**:
Функция принимает локатор, сообщение и скорость печати. Преобразует локатор в `SimpleNamespace`, если это необходимо. Получает веб-элемент с помощью `get_webelement_by_locator`. Если элемент не найден, записывает отладочное сообщение в лог и возвращает `False`. Если указана скорость печати, вводит сообщение посимвольно с задержкой. В противном случае вводит сообщение целиком.

**Параметры**:
- `locator` (dict | SimpleNamespace): Информация о местоположении элемента на странице.
- `message` (str): Сообщение для отправки веб-элементу.
- `typing_speed` (float): Скорость печати сообщения в секундах.

**Возвращает**:
- bool: `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Вызывает исключения**:
- None

**Примеры**:
```python
locator_data = {'selector': '//input', 'by': 'xpath'}
result = await executor.send_message(locator_data, 'Hello, World!')
```

### `goto`

```python
    async def goto(self, url: str) -> None:
        """
        Navigates to a specified URL.

        Args:
            url: URL to navigate to.
        """
        if self.page:
            try:
                 await self.page.goto(url)
            except Exception as ex:
                   logger.error(f'Error during navigation to {url=}', ex)
```

**Назначение**:
Переходит по указанному URL.

**Как работает функция**:
Функция принимает URL и переходит по нему, используя метод `goto` объекта `self.page`. В случае ошибки записывает сообщение об ошибке в лог.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- None

**Вызывает исключения**:
- Exception: Если происходит ошибка во время навигации.

**Примеры**:
```python
await executor.goto('https://www.example.com')
```