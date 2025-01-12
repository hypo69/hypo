# Документация модуля `executor.py`

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействий с веб-элементами с использованием Selenium. Этот модуль предоставляет гибкий и универсальный фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Основные возможности

1.  **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локатора.
2.  **Взаимодействие с веб-элементами**: Выполняет различные действия, такие как клики, отправка сообщений, выполнение событий и получение атрибутов из веб-элементов.
3.  **Обработка ошибок**: Поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы с нестабильными элементами или требующие особого подхода.
4.  **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

## Структура модуля

### Классы

#### `ExecuteLocator`

Этот класс является ядром модуля, ответственным за обработку взаимодействий с веб-элементами на основе предоставленных локаторов.

-   **Атрибуты**:
    -   `driver`: Экземпляр Selenium WebDriver.
    -   `actions`: Объект `ActionChains` для выполнения сложных действий.
    -   `by_mapping`: Словарь, сопоставляющий типы локаторов с методами `By` Selenium.
    -   `mode`: Режим выполнения (`debug`, `dev` и т. д.).

-   **Методы**:
    -   `__post_init__`: Инициализирует объект `ActionChains`, если предоставлен драйвер.
    -   `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
    -   `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
    -   `get_attribute_by_locator`: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.
    -   `get_webelement_by_locator`: Извлекает веб-элементы на основе предоставленного локатора.
    -   `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
    -   `execute_event`: Выполняет события, связанные с локатором.
    -   `send_message`: Отправляет сообщение в веб-элемент.

### Диаграммы потоков

Модуль включает диаграммы потоков Mermaid для иллюстрации хода выполнения ключевых методов:

-   **`execute_locator`**:

    ```mermaid
    graph TD
    Start[Начало] --> CheckLocatorType[Проверка типа локатора (SimpleNamespace или dict)]
    CheckLocatorType --> IsSimpleNamespace{Локатор SimpleNamespace?}
    IsSimpleNamespace -->|Да| UseLocatorAsIs[Использовать локатор как есть]
    IsSimpleNamespace -->|Нет| ConvertDictToSimpleNamespace[Преобразовать dict в SimpleNamespace]
    ConvertDictToSimpleNamespace --> UseLocatorAsIs
    UseLocatorAsIs --> DefineParseLocator[Определение асинхронной функции _parse_locator]
    DefineParseLocator --> CheckEventAttributeMandatory[Проверка наличия event, attribute или mandatory]
    CheckEventAttributeMandatory -->|Нет| ReturnNone[Возврат None]
    CheckEventAttributeMandatory -->|Да| TryMapByEvaluateAttribute[Попытка сопоставить by и оценить атрибут]
    TryMapByEvaluateAttribute --> CatchExceptionsAndLog[Перехват исключений и логирование при необходимости]
    CatchExceptionsAndLog --> HasEvent{Есть event в локаторе?}
    HasEvent -->|Да| ExecuteEvent[Выполнение event]
    HasEvent -->|Нет| HasAttribute{Есть attribute в локаторе?}
    HasAttribute -->|Да| GetAttributeByLocator[Получение атрибута по локатору]
    HasAttribute -->|Нет| GetWebElementByLocator[Получение веб-элемента по локатору]
    ExecuteEvent --> ReturnEventResult[Возврат результата event]
    GetAttributeByLocator --> ReturnAttributeResult[Возврат результата атрибута]
    GetWebElementByLocator --> ReturnWebElementResult[Возврат результата веб-элемента]
    ReturnEventResult --> ReturnFinalResult[Возврат конечного результата _parse_locator]
    ReturnAttributeResult --> ReturnFinalResult
    ReturnWebElementResult --> ReturnFinalResult
    ReturnFinalResult --> ReturnExecuteLocatorResult[Возврат результата execute_locator]
    ReturnExecuteLocatorResult --> End[Конец]
    ```

-   **`evaluate_locator`**:

    ```mermaid
    graph TD
    Start[Начало] --> CheckIfAttributeIsList[Проверка, является ли атрибут списком]
    CheckIfAttributeIsList -->|Да| IterateOverAttributes[Итерация по атрибутам в списке]
    IterateOverAttributes --> CallEvaluateForEachAttribute[Вызов _evaluate для каждого атрибута]
    CallEvaluateForEachAttribute --> ReturnGatheredResults[Возврат результатов из asyncio.gather]
    CheckIfAttributeIsList -->|Нет| CallEvaluateForSingleAttribute[Вызов _evaluate для одного атрибута]
    CallEvaluateForSingleAttribute --> ReturnEvaluateResult[Возврат результата _evaluate]
    ReturnEvaluateResult --> End[Конец]
    ReturnGatheredResults --> End
    ```

-   **`get_attribute_by_locator`**:

    ```mermaid
    graph TD
    Start[Начало] --> CheckIfLocatorIsSimpleNamespaceOrDict[Проверка типа локатора (SimpleNamespace или dict)]
    CheckIfLocatorIsSimpleNamespaceOrDict -->|Да| ConvertLocatorToSimpleNamespaceIfNeeded[Преобразование локатора в SimpleNamespace, если нужно]
    ConvertLocatorToSimpleNamespaceIfNeeded --> CallGetWebElementByLocator[Вызов get_webelement_by_locator]
    CallGetWebElementByLocator --> CheckIfWebElementIsFound[Проверка, найден ли web_element]
    CheckIfWebElementIsFound -->|Нет| LogDebugMessageAndReturn[Логирование и возврат]
    CheckIfWebElementIsFound -->|Да| CheckIfAttributeIsDictionaryLikeString[Проверка, является ли locator.attribute строкой, похожей на словарь]
    CheckIfAttributeIsDictionaryLikeString -->|Да| ParseAttributeStringToDict[Преобразование locator.attribute из строки в словарь]
    ParseAttributeStringToDict --> CheckIfWebElementIsList[Проверка, является ли web_element списком]
    CheckIfWebElementIsList -->|Да| RetrieveAttributesForEachElementInList[Получение атрибутов для каждого элемента в списке]
    RetrieveAttributesForEachElementInList --> ReturnListOfAttributes[Возврат списка атрибутов]
    CheckIfWebElementIsList -->|Нет| RetrieveAttributesForSingleWebElement[Получение атрибутов для одного web_element]
    RetrieveAttributesForSingleWebElement --> ReturnListOfAttributes
    CheckIfAttributeIsDictionaryLikeString -->|Нет| CheckIfWebElementIsListAgain[Проверка, является ли web_element списком (повторно)]
     CheckIfWebElementIsListAgain -->|Да| RetrieveAttributesForEachElementInListAgain[Получение атрибутов для каждого элемента в списке (повторно)]
    RetrieveAttributesForEachElementInListAgain --> ReturnListOfAttributesOrSingleAttribute[Возврат списка атрибутов или одного атрибута]
    CheckIfWebElementIsListAgain -->|Нет| RetrieveAttributeForSingleWebElementAgain[Получение атрибута для одного web_element (повторно)]
    RetrieveAttributeForSingleWebElementAgain --> ReturnListOfAttributesOrSingleAttribute
    ReturnListOfAttributesOrSingleAttribute --> End[Конец]
    LogDebugMessageAndReturn --> End
    ```

## Использование

Для использования этого модуля создайте экземпляр класса `ExecuteLocator` с экземпляром Selenium WebDriver, а затем вызовите различные методы для взаимодействия с веб-элементами на основе предоставленных локаторов.

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

-   `selenium`: Для автоматизации работы с веб-страницами.
-   `asyncio`: Для асинхронных операций.
-   `re`: Для регулярных выражений.
-   `dataclasses`: Для создания классов данных.
-   `enum`: Для создания перечислений.
-   `pathlib`: Для работы с путями к файлам.
-   `types`: Для создания простых пространств имен.
-   `typing`: Для аннотаций типов.

## Обработка ошибок

Модуль включает надежную обработку ошибок, чтобы обеспечить продолжение выполнения, даже если некоторые элементы не найдены или есть проблемы с веб-страницей. Это особенно полезно для работы с динамическими или нестабильными веб-страницами.

## Вклад

Вклад в этот модуль приветствуется. Пожалуйста, убедитесь, что любые изменения хорошо документированы и включают соответствующие тесты.

## Лицензия

Этот модуль лицензирован по лицензии MIT. Подробности см. в файле `LICENSE`.

---

Этот файл README предоставляет всесторонний обзор модуля `executor.py`, включая его назначение, структуру, использование и зависимости. Он предназначен для того, чтобы помочь разработчикам понять и эффективно использовать этот модуль.