# Документация `executor.py`

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействий с веб-элементами с использованием Selenium. Этот модуль предоставляет гибкий и универсальный фреймворк для обнаружения, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Ключевые особенности

1.  **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локатора.
2.  **Взаимодействие с веб-элементами**: Выполняет различные действия, такие как клики, отправка сообщений, выполнение событий и получение атрибутов из веб-элементов.
3.  **Обработка ошибок**: Поддерживает продолжение выполнения в случае ошибки, позволяя обрабатывать веб-страницы с нестабильными элементами или требующие особого подхода.
4.  **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

## Структура модуля

### Классы

#### `ExecuteLocator`

Этот класс является ядром модуля, ответственным за обработку взаимодействий веб-элементов на основе предоставленных локаторов.

**Описание**:
Класс `ExecuteLocator` предназначен для выполнения действий над веб-элементами на основе заданных локаторов. Он инициализируется с драйвером Selenium и предоставляет методы для поиска элементов, выполнения событий и получения атрибутов.

**Как работает класс**:
Класс `ExecuteLocator` принимает драйвер Selenium в качестве аргумента и использует его для поиска веб-элементов на странице. Он также поддерживает выполнение различных действий, таких как клики, отправка сообщений и получение атрибутов. Основной метод `execute_locator` принимает локатор в качестве аргумента и выполняет соответствующие действия над найденным элементом или элементами. Локатор может быть представлен как словарем, так и объектом `SimpleNamespace`. Внутри класса происходит проверка типа локатора, его преобразование при необходимости, и дальнейшее выполнение действий в зависимости от наличия атрибутов `event` и `attribute`. Класс также обрабатывает исключения и логирует ошибки при возникновении проблем.

**Атрибуты**:

*   `driver`: Экземпляр Selenium WebDriver.
*   `actions`: Объект `ActionChains` для выполнения сложных действий.
*   `by_mapping`: Словарь, отображающий типы локаторов на методы `By` Selenium.
*   `mode`: Режим выполнения (`debug`, `dev` и т.д.).

**Методы**:

*   `__post_init__`: Инициализирует объект `ActionChains`, если предоставлен драйвер.

    ```python
    def __post_init__(self) -> None:
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.

        Args:
            None

        Returns:
            None

        Raises:
            None

        Example:
            >>> executor = ExecuteLocator(driver=webdriver.Chrome())
            >>> executor.actions is not None
            True
        """
    ```

*   `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.

    ```python
    async def execute_locator(self, locator: SimpleNamespace | dict) -> Any:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        Args:
            locator (SimpleNamespace | dict): Локатор веб-элемента.

        Returns:
            Any: Результат выполнения действия.

        Raises:
            Exception: Если возникает ошибка при выполнении действия.

        Example:
            >>> locator = {'by': 'id', 'selector': 'my_element', 'event': 'click'}
            >>> result = await executor.execute_locator(locator)
            >>> print(result)
            None
        """
    ```

*   `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.

    ```python
    async def evaluate_locator(self, locator: SimpleNamespace) -> List[Any] | Any:
        """
        Оценивает и обрабатывает атрибуты локатора.

        Args:
            locator (SimpleNamespace): Локатор веб-элемента.

        Returns:
            List[Any] | Any: Результат оценки атрибутов.

        Raises:
            Exception: Если возникает ошибка при оценке атрибутов.

        Example:
            >>> locator = SimpleNamespace(attribute=['text', 'value'])
            >>> result = await executor.evaluate_locator(locator)
            >>> print(result)
            ['text_value', 'value_value']
        """
    ```

*   `get_attribute_by_locator`: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

    ```python
    async def get_attribute_by_locator(self, locator: SimpleNamespace | dict) -> List[str] | str | None:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        Args:
            locator (SimpleNamespace | dict): Локатор веб-элемента.

        Returns:
            List[str] | str | None: Список атрибутов, атрибут или None в случае ошибки.

        Raises:
            Exception: Если возникает ошибка при извлечении атрибута.

        Example:
            >>> locator = {'by': 'id', 'selector': 'my_element', 'attribute': 'text'}
            >>> result = await executor.get_attribute_by_locator(locator)
            >>> print(result)
            'element_text'
        """
    ```

*   `get_webelement_by_locator`: Извлекает веб-элементы на основе предоставленного локатора.

    ```python
    def get_webelement_by_locator(self, locator: SimpleNamespace) -> List[WebElement] | WebElement | None:
        """
        Извлекает веб-элементы на основе предоставленного локатора.

        Args:
            locator (SimpleNamespace): Локатор веб-элемента.

        Returns:
            List[WebElement] | WebElement | None: Список веб-элементов, веб-элемент или None в случае ошибки.

        Raises:
            NoSuchElementException: Если элемент не найден.

        Example:
            >>> locator = SimpleNamespace(by='id', selector='my_element')
            >>> element = executor.get_webelement_by_locator(locator)
            >>> print(element)
            <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>
        """
    ```

*   `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.

    ```python
    def get_webelement_as_screenshot(self, element: WebElement) -> bytes | None:
        """
        Делает скриншот найденного веб-элемента.

        Args:
            element (WebElement): Веб-элемент для скриншота.

        Returns:
            bytes | None: Байты изображения скриншота или None в случае ошибки.

        Raises:
            WebDriverException: Если возникает ошибка при создании скриншота.

        Example:
            >>> locator = SimpleNamespace(by='id', selector='my_element')
            >>> element = executor.get_webelement_by_locator(locator)
            >>> screenshot = executor.get_webelement_as_screenshot(element)
            >>> print(screenshot[:20])
            b'\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR'
        """
    ```

*   `execute_event`: Выполняет события, связанные с локатором.

    ```python
    def execute_event(self, element: WebElement, locator: SimpleNamespace) -> Any:
        """
        Выполняет события, связанные с локатором.

        Args:
            element (WebElement): Веб-элемент для выполнения события.
            locator (SimpleNamespace): Локатор веб-элемента.

        Returns:
            Any: Результат выполнения события.

        Raises:
            Exception: Если возникает ошибка при выполнении события.

        Example:
            >>> locator = SimpleNamespace(event='click()')
            >>> element = driver.find_element(By.ID, 'my_element')
            >>> result = executor.execute_event(element, locator)
            >>> print(result)
            None
        """
    ```

*   `send_message`: Отправляет сообщение веб-элементу.

    ```python
    def send_message(self, element: WebElement, locator: SimpleNamespace) -> None:
        """
        Отправляет сообщение веб-элементу.

        Args:
            element (WebElement): Веб-элемент для отправки сообщения.
            locator (SimpleNamespace): Локатор веб-элемента.

        Returns:
            None

        Raises:
            Exception: Если возникает ошибка при отправке сообщения.

        Example:
            >>> locator = SimpleNamespace(send_keys='hello')
            >>> element = driver.find_element(By.ID, 'my_element')
            >>> executor.send_message(element, locator)
            None
        """
    ```

### Схемы потоков

Модуль включает схемы потоков Mermaid для иллюстрации потока выполнения для ключевых методов:

*   **`execute_locator`**:

    ```mermaid
    graph TD
    Start[Start] --> CheckLocatorType[Check if locator is SimpleNamespace or dict]
    CheckLocatorType --> IsSimpleNamespace{Is locator SimpleNamespace?}
    IsSimpleNamespace -->|Yes| UseLocatorAsIs[Use locator as is]
    IsSimpleNamespace -->|No| ConvertDictToSimpleNamespace[Convert dict to SimpleNamespace]
    ConvertDictToSimpleNamespace --> UseLocatorAsIs
    UseLocatorAsIs --> DefineParseLocator[Define async function _parse_locator]
    DefineParseLocator --> CheckEventAttributeMandatory[Check if locator has event, attribute, or mandatory]
    CheckEventAttributeMandatory -->|No| ReturnNone[Return None]
    CheckEventAttributeMandatory -->|Yes| TryMapByEvaluateAttribute[Try to map by and evaluate attribute]
    TryMapByEvaluateAttribute --> CatchExceptionsAndLog[Catch exceptions and log if needed]
    CatchExceptionsAndLog --> HasEvent{Does locator have event?}
    HasEvent -->|Yes| ExecuteEvent[Execute event]
    HasEvent -->|No| HasAttribute{Does locator have attribute?}
    HasAttribute -->|Yes| GetAttributeByLocator[Get attribute by locator]
    HasAttribute -->|No| GetWebElementByLocator[Get web element by locator]
    ExecuteEvent --> ReturnEventResult[Return result of event]
    GetAttributeByLocator --> ReturnAttributeResult[Return attribute result]
    GetWebElementByLocator --> ReturnWebElementResult[Return web element result]
    ReturnEventResult --> ReturnFinalResult[Return final result of _parse_locator]
    ReturnAttributeResult --> ReturnFinalResult
    ReturnWebElementResult --> ReturnFinalResult
    ReturnFinalResult --> ReturnExecuteLocatorResult[Return result of execute_locator]
    ReturnExecuteLocatorResult --> End[End]
    ```

*   **`evaluate_locator`**:

    ```mermaid
    graph TD
    Start[Start] --> CheckIfAttributeIsList[Check if attribute is list]
    CheckIfAttributeIsList -->|Yes| IterateOverAttributes[Iterate over each attribute in list]
    IterateOverAttributes --> CallEvaluateForEachAttribute[Call _evaluate for each attribute]
    CallEvaluateForEachAttribute --> ReturnGatheredResults[Return gathered results from asyncio.gather]
    CheckIfAttributeIsList -->|No| CallEvaluateForSingleAttribute[Call _evaluate for single attribute]
    CallEvaluateForSingleAttribute --> ReturnEvaluateResult[Return result of _evaluate]
    ReturnEvaluateResult --> End[End]
    ReturnGatheredResults --> End
    ```

*   **`get_attribute_by_locator`**:

    ```mermaid
    graph TD
    Start[Start] --> CheckIfLocatorIsSimpleNamespaceOrDict[Check if locator is SimpleNamespace or dict]
    CheckIfLocatorIsSimpleNamespaceOrDict -->|Yes| ConvertLocatorToSimpleNamespaceIfNeeded[Convert locator to SimpleNamespace if needed]
    ConvertLocatorToSimpleNamespaceIfNeeded --> CallGetWebElementByLocator[Call get_webelement_by_locator]
    CallGetWebElementByLocator --> CheckIfWebElementIsFound[Check if web_element is found]
    CheckIfWebElementIsFound -->|No| LogDebugMessageAndReturn[Log debug message and return]
    CheckIfWebElementIsFound -->|Yes| CheckIfAttributeIsDictionaryLikeString[Check if locator.attribute is a dictionary-like string]
    CheckIfAttributeIsDictionaryLikeString -->|Yes| ParseAttributeStringToDict[Parse locator.attribute string to dict]
    ParseAttributeStringToDict --> CheckIfWebElementIsList[Check if web_element is a list]
    CheckIfWebElementIsList -->|Yes| RetrieveAttributesForEachElementInList[Retrieve attributes for each element in list]
    RetrieveAttributesForEachElementInList --> ReturnListOfAttributes[Return list of attributes]
    CheckIfWebElementIsList -->|No| RetrieveAttributesForSingleWebElement[Retrieve attributes for a single web_element]
    RetrieveAttributesForSingleWebElement --> ReturnListOfAttributes
    CheckIfAttributeIsDictionaryLikeString -->|No| CheckIfWebElementIsListAgain[Check if web_element is a list]
    CheckIfWebElementIsListAgain -->|Yes| RetrieveAttributesForEachElementInListAgain[Retrieve attributes for each element in list]
    RetrieveAttributesForEachElementInListAgain --> ReturnListOfAttributesOrSingleAttribute[Return list of attributes or single attribute]
    CheckIfWebElementIsListAgain -->|No| RetrieveAttributeForSingleWebElementAgain[Retrieve attribute for a single web_element]
    RetrieveAttributeForSingleWebElementAgain --> ReturnListOfAttributesOrSingleAttribute
    ReturnListOfAttributesOrSingleAttribute --> End[End]
    LogDebugMessageAndReturn --> End
    ```

## Использование

Чтобы использовать этот модуль, создайте экземпляр класса `ExecuteLocator` с экземпляром Selenium WebDriver, а затем вызовите различные методы для взаимодействия с веб-элементами на основе предоставленных локаторов.

### Пример

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

*   `selenium`: Для автоматизации веб-интерфейса.
*   `asyncio`: Для асинхронных операций.
*   `re`: Для регулярных выражений.
*   `dataclasses`: Для создания классов данных.
*   `enum`: Для создания перечислений.
*   `pathlib`: Для обработки путей к файлам.
*   `types`: Для создания простых пространств имен.
*   `typing`: Для аннотаций типов.

## Обработка ошибок

Модуль включает надежную обработку ошибок, чтобы гарантировать, что выполнение продолжается, даже если определенные элементы не найдены или если есть проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.

## Вклад

Вклад в этот модуль приветствуется. Пожалуйста, убедитесь, что любые изменения хорошо документированы и включают соответствующие тесты.

## Лицензия

Этот модуль лицензирован в соответствии с лицензией MIT. Подробности см. в файле `LICENSE`.

\---

Этот README предоставляет исчерпывающий обзор модуля `executor.py`, включая его цель, структуру, использование и зависимости. Он предназначен для того, чтобы помочь разработчикам понять и эффективно использовать модуль.