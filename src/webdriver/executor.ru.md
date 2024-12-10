```rst
.. module:: src.webdriver.excutor
```
[English](https://github.com/hypo69/hypo/blob/master/src/webdriver/executor.md)
# Документация по `executor.py`

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Этот модуль предоставляет гибкий и универсальный фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Основные возможности

1. **Парсинг и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локаторов.
2. **Взаимодействие с веб-элементами**: Выполняет различные действия, такие как клики, отправка сообщений, выполнение событий и извлечение атрибутов из веб-элементов.
3. **Обработка ошибок**: Поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы с нестабильными элементами или требующими особого подхода.
4. **Поддержка нескольких типов локаторов**: Обрабатывает как отдельные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

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

### Диаграммы потока

Модуль включает диаграммы потока Mermaid для иллюстрации потока выполнения ключевых методов:

- **`execute_locator`**:
  ```mermaid
  graph TD
  Start[Начало] --> CheckLocatorType[Проверка, является ли локатор SimpleNamespace или dict]
  CheckLocatorType --> IsSimpleNamespace{Является ли локатор SimpleNamespace?}
  IsSimpleNamespace -->|Да| UseLocatorAsIs[Использовать локатор как есть]
  IsSimpleNamespace -->|Нет| ConvertDictToSimpleNamespace[Преобразовать dict в SimpleNamespace]
  ConvertDictToSimpleNamespace --> UseLocatorAsIs
  UseLocatorAsIs --> DefineParseLocator[Определить асинхронную функцию _parse_locator]
  DefineParseLocator --> CheckEventAttributeMandatory[Проверить, есть ли у локатора событие, атрибут или обязательное поле]
  CheckEventAttributeMandatory -->|Нет| ReturnNone[Вернуть None]
  CheckEventAttributeMandatory -->|Да| TryMapByEvaluateAttribute[Попробовать сопоставить by и оценить атрибут]
  TryMapByEvaluateAttribute --> CatchExceptionsAndLog[Перехватить исключения и залогировать при необходимости]
  CatchExceptionsAndLog --> HasEvent{Есть ли у локатора событие?}
  HasEvent -->|Да| ExecuteEvent[Выполнить событие]
  HasEvent -->|Нет| HasAttribute{Есть ли у локатора атрибут?}
  HasAttribute -->|Да| GetAttributeByLocator[Получить атрибут по локатору]
  HasAttribute -->|Нет| GetWebElementByLocator[Получить веб-элемент по локатору]
  ExecuteEvent --> ReturnEventResult[Вернуть результат события]
  GetAttributeByLocator --> ReturnAttributeResult[Вернуть результат атрибута]
  GetWebElementByLocator --> ReturnWebElementResult[Вернуть результат веб-элемента]
  ReturnEventResult --> ReturnFinalResult[Вернуть окончательный результат _parse_locator]
  ReturnAttributeResult --> ReturnFinalResult
  ReturnWebElementResult --> ReturnFinalResult
  ReturnFinalResult --> ReturnExecuteLocatorResult[Вернуть результат execute_locator]
  ReturnExecuteLocatorResult --> End[Конец]
  ```

- **`evaluate_locator`**:
  ```mermaid
  graph TD
  Start[Начало] --> CheckIfAttributeIsList[Проверка, является ли атрибут списком]
  CheckIfAttributeIsList -->|Да| IterateOverAttributes[Итерация по каждому атрибуту в списке]
  IterateOverAttributes --> CallEvaluateForEachAttribute[Вызов _evaluate для каждого атрибута]
  CallEvaluateForEachAttribute --> ReturnGatheredResults[Вернуть собранные результаты из asyncio.gather]
  CheckIfAttributeIsList -->|Нет| CallEvaluateForSingleAttribute[Вызов _evaluate для одного атрибута]
  CallEvaluateForSingleAttribute --> ReturnEvaluateResult[Вернуть результат _evaluate]
  ReturnEvaluateResult --> End[Конец]
  ReturnGatheredResults --> End
  ```

- **`get_attribute_by_locator`**:
  ```mermaid
  graph TD
  Start[Начало] --> CheckIfLocatorIsSimpleNamespaceOrDict[Проверка, является ли локатор SimpleNamespace или dict]
  CheckIfLocatorIsSimpleNamespaceOrDict -->|Да| ConvertLocatorToSimpleNamespaceIfNeeded[Преобразовать локатор в SimpleNamespace, если необходимо]
  ConvertLocatorToSimpleNamespaceIfNeeded --> CallGetWebElementByLocator[Вызов get_webelement_by_locator]
  CallGetWebElementByLocator --> CheckIfWebElementIsFound[Проверка, найден ли web_element]
  CheckIfWebElementIsFound -->|Нет| LogDebugMessageAndReturn[Залогировать сообщение отладки и вернуть]
  CheckIfWebElementIsFound -->|Да| CheckIfAttributeIsDictionaryLikeString[Проверка, является ли locator.attribute строкой, похожей на словарь]
  CheckIfAttributeIsDictionaryLikeString -->|Да| ParseAttributeStringToDict[Разбор строки locator.attribute в словарь]
  ParseAttributeStringToDict --> CheckIfWebElementIsList[Проверка, является ли web_element списком]
  CheckIfWebElementIsList -->|Да| RetrieveAttributesForEachElementInList[Получение атрибутов для каждого элемента в списке]
  RetrieveAttributesForEachElementInList --> ReturnListOfAttributes[Вернуть список атрибутов]
  CheckIfWebElementIsList -->|Нет| RetrieveAttributesForSingleWebElement[Получение атрибутов для одного web_element]
  RetrieveAttributesForSingleWebElement --> ReturnListOfAttributes
  CheckIfAttributeIsDictionaryLikeString -->|Нет| CheckIfWebElementIsListAgain[Проверка, является ли web_element списком]
  CheckIfWebElementIsListAgain -->|Да| RetrieveAttributesForEachElementInListAgain[Получение атрибутов для каждого элемента в списке]
  RetrieveAttributesForEachElementInListAgain --> ReturnListOfAttributesOrSingleAttribute[Вернуть список атрибутов или один атрибут]
  CheckIfWebElementIsListAgain -->|Нет| RetrieveAttributeForSingleWebElementAgain[Получение атрибута для одного web_element]
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

- `selenium`: Для веб-автоматизации.
- `asyncio`: Для асинхронных операций.
- `re`: Для регулярных выражений.
- `dataclasses`: Для создания классов данных.
- `enum`: Для создания перечислений.
- `pathlib`: Для обработки путей к файлам.
- `types`: Для создания простых пространств имен.
- `typing`: Для аннотаций типов.

## Обработка ошибок

Модуль включает надежную обработку ошибок, чтобы обеспечить продолжение выполнения даже в случае, если некоторые элементы не найдены или если возникли проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.

## Вклад

Вклад в этот модуль приветствуется. Пожалуйста, убедитесь, что любые изменения хорошо документированы и включают соответствующие тесты.

## Лицензия

Этот модуль лицензирован под MIT License. Подробности смотрите в файле `LICENSE`.

---

Этот README предоставляет исчерпывающий обзор модуля `executor.py`, включая его назначение, структуру, использование и зависимости. Он предназначен для того, чтобы помочь разработчикам понять и эффективно использовать модуль.