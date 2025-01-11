# `executor.py`

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Этот модуль предоставляет гибкий и универсальный фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Основные характеристики

1. **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локаторов.
2. **Взаимодействие с веб-элементами**: Выполняет различные действия, такие как клики, отправка сообщений, выполнение событий и получение атрибутов из веб-элементов.
3. **Обработка ошибок**: Поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы с нестабильными элементами или требующие особого подхода.
4. **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

## Структура модуля

### Классы

#### `ExecuteLocator`

Этот класс является ядром модуля, отвечающим за обработку взаимодействий с веб-элементами на основе предоставленных локаторов.

- **Атрибуты**:
    - `driver`: Экземпляр Selenium WebDriver.
    - `actions`: Объект `ActionChains` для выполнения сложных действий.
    - `by_mapping`: Словарь, сопоставляющий типы локаторов с методами `By` Selenium.
    - `mode`: Режим выполнения (`debug`, `dev` и т.д.).

- **Методы**:
    - `__post_init__`: Инициализирует объект `ActionChains`, если предоставлен драйвер.
    - `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
    - `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
    - `get_attribute_by_locator`: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.
    - `get_webelement_by_locator`: Извлекает веб-элементы на основе предоставленного локатора.
    - `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
    - `execute_event`: Выполняет события, связанные с локатором.
    - `send_message`: Отправляет сообщение веб-элементу.

### Функции

#### `_parse_locator`

**Описание**: Асинхронная функция, предназначенная для извлечения данных из веб-элементов на основе заданного локатора.

**Параметры**:
- `locator` (types.SimpleNamespace): Локатор для поиска и взаимодействия с веб-элементами.
- `executor` (ExecuteLocator): Экземпляр класса `ExecuteLocator`, который используется для выполнения действий над веб-элементами.

**Возвращает**:
- `Any`: Возвращает результат выполненных действий с веб-элементом. Зависит от того, какой тип данных запрашивается (атрибут, текст, событие и т.д.). Может вернуть `None`, если не было найдено данных для извлечения или если произошла ошибка.

**Вызывает исключения**:
- `Exception`: Вызывает исключение, если возникает ошибка в процессе поиска или взаимодействия с веб-элементом. Ошибки перехватываются и обрабатываются, а результат выполнения возвращается, в некоторых случаях с `None`.

#### `_evaluate`

**Описание**: Асинхронная функция, предназначенная для обработки и получения значения конкретного атрибута веб-элемента.

**Параметры**:
- `locator` (types.SimpleNamespace): Локатор для поиска и взаимодействия с веб-элементами.
- `executor` (ExecuteLocator): Экземпляр класса `ExecuteLocator`, который используется для выполнения действий над веб-элементами.
- `attribute` (str): Название атрибута, который необходимо получить от веб-элемента.

**Возвращает**:
- `Any | None`: Возвращает значение атрибута веб-элемента. Может вернуть `None`, если не удалось получить значение атрибута, или если атрибут не существует.

**Вызывает исключения**:
- `Exception`: Вызывает исключение, если возникает ошибка в процессе получения атрибута веб-элемента. Ошибки перехватываются и обрабатываются, а результат выполнения возвращается, в некоторых случаях с `None`.

### Диаграммы потоков

Модуль включает диаграммы потоков Mermaid для иллюстрации процесса выполнения ключевых методов:

- **`execute_locator`**:
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

- **`evaluate_locator`**:
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

- **`get_attribute_by_locator`**:
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

Для использования этого модуля создайте экземпляр класса `ExecuteLocator` с экземпляром Selenium WebDriver, а затем вызывайте различные методы для взаимодействия с веб-элементами на основе предоставленных локаторов.

### Пример

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

# Initialize the WebDriver
driver = webdriver.Chrome()

# Initialize the ExecuteLocator class
executor = ExecuteLocator(driver=driver)

# Define a locator
locator = {
    "by": "ID",
    "selector": "some_element_id",
    "event": "click()"
}

# Execute the locator
result = await executor.execute_locator(locator)
print(result)
```

## Зависимости

- `selenium`: Для автоматизации веб-приложений.
- `asyncio`: Для асинхронных операций.
- `re`: Для регулярных выражений.
- `dataclasses`: Для создания классов данных.
- `enum`: Для создания перечислений.
- `pathlib`: Для обработки путей к файлам.
- `types`: Для создания простых пространств имен.
- `typing`: Для аннотаций типов.

## Обработка ошибок

Модуль включает надежную обработку ошибок, чтобы гарантировать, что выполнение продолжается, даже если определенные элементы не найдены или есть проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.

## Вклад

Вклад в этот модуль приветствуется. Пожалуйста, убедитесь, что любые изменения хорошо задокументированы и включают соответствующие тесты.

## Лицензия

Этот модуль распространяется под лицензией MIT. Подробности см. в файле `LICENSE`.

---

Этот документ предоставляет исчерпывающий обзор модуля `executor.py`, включая его назначение, структуру, использование и зависимости. Он предназначен для того, чтобы помочь разработчикам понять и эффективно использовать модуль.