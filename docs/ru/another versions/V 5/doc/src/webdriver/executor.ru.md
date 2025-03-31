# Документация по модулю `executor.py`

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Модуль предоставляет гибкий и универсальный фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Оглавление

- [Обзор](#обзор)
- [Основные возможности](#основные-возможности)
- [Структура модуля](#структура-модуля)
    - [Классы](#классы)
        - [ExecuteLocator](#ExecuteLocator)
            - [Параметры класса `ExecuteLocator`](#-параметры--если-есть-параметры)
            - [Методы класса `ExecuteLocator`](#-методы--если-есть-методы)
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
- [Зависимости](#зависимости)

## Основные возможности

1. **Парсинг и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локаторов.
2. **Взаимодействие с веб-элементами**: Выполняет различные действия, такие как клики, отправка сообщений, выполнение событий и извлечение атрибутов из веб-элементов.
3. **Обработка ошибок**: Поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы с нестабильными элементами или требующими особого подхода.
4. **Поддержка нескольких типов локаторов**: Обрабатывает как отдельные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

## Структура модуля

### Классы

#### `ExecuteLocator`

**Описание**: Этот класс является ядром модуля, отвечающим за обработку взаимодействий с веб-элементами на основе предоставленных локаторов.

**Как работает класс**: Класс `ExecuteLocator` принимает экземпляр Selenium WebDriver и использует его для поиска веб-элементов на странице. Он предоставляет методы для выполнения различных действий над этими элементами, таких как клики, отправка сообщений и извлечение атрибутов. Класс также обрабатывает возможные ошибки, возникающие в процессе взаимодействия с веб-элементами.

##### Параметры:
- `driver`: Экземпляр Selenium WebDriver.
- `actions`: Объект `ActionChains` для выполнения сложных действий.
- `by_mapping`: Словарь, сопоставляющий типы локаторов с методами `By` Selenium.
- `mode`: Режим выполнения (`debug`, `dev` и т.д.).

##### Методы:
- `__post_init__`: Инициализирует объект `ActionChains`, если предоставлен драйвер.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.
- `get_webelement_by_locator`: Извлекает веб-элементы на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет события, связанные с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

##### `__post_init__`

```python
    def __post_init__(self) -> None:
        """Инициализирует объект ActionChains, если предоставлен драйвер."""
        ...
```

**Описание**: Инициализирует объект `ActionChains`, если предоставлен драйвер.

**Как работает функция**: Метод `__post_init__` вызывается после инициализации экземпляра класса. Если драйвер был передан при создании экземпляра `ExecuteLocator`, этот метод инициализирует объект `ActionChains`, который позволяет выполнять сложные последовательности действий с веб-элементами.

##### `execute_locator`

```python
    async def execute_locator(self, locator: SimpleNamespace | dict) -> Any:
        """Выполняет действия над веб-элементом на основе предоставленного локатора."""
        ...
```

**Описание**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Как работает функция**: 
1. Проверяет, является ли локатор `SimpleNamespace` или `dict`.
2. Преобразует `dict` в `SimpleNamespace`, если необходимо.
3. Определяет асинхронную функцию `_parse_locator`.
4. Проверяет, есть ли у локатора событие, атрибут или обязательное поле.
5. Пытается сопоставить `by` и оценить атрибут.
6. Перехватывает исключения и логирует их при необходимости.
7. Проверяет наличие события у локатора. Если есть, выполняет событие.
8. Проверяет наличие атрибута у локатора. Если есть, получает атрибут по локатору.
9. Если нет атрибута, получает веб-элемент по локатору.
10. Возвращает окончательный результат `_parse_locator`.
11. Возвращает результат `execute_locator`.

##### `evaluate_locator`

```python
    async def evaluate_locator(self, locator: SimpleNamespace) -> list[Any] | Any:
        """Оценивает и обрабатывает атрибуты локатора."""
        ...
```

**Описание**: Оценивает и обрабатывает атрибуты локатора.

**Как работает функция**: 
1. Проверяет, является ли атрибут списком.
2. Если атрибут является списком, итерируется по каждому атрибуту в списке и вызывает `_evaluate` для каждого атрибута. Затем возвращает собранные результаты из `asyncio.gather`.
3. Если атрибут не является списком, вызывает `_evaluate` для одного атрибута и возвращает результат.

##### `get_attribute_by_locator`

```python
    async def get_attribute_by_locator(self, locator: SimpleNamespace | dict) -> list[str | None] | str | None:
        """Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору."""
        ...
```

**Описание**: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

**Как работает функция**:
1. Проверяет, является ли локатор `SimpleNamespace` или `dict`.
2. Преобразует локатор в `SimpleNamespace`, если необходимо.
3. Вызывает `get_webelement_by_locator`.
4. Проверяет, найден ли `web_element`. Если не найден, логирует сообщение отладки и возвращает.
5. Проверяет, является ли `locator.attribute` строкой, похожей на словарь. Если да, разбирает строку `locator.attribute` в словарь.
6. Проверяет, является ли `web_element` списком.
7. Если `web_element` является списком, получает атрибуты для каждого элемента в списке и возвращает список атрибутов.
8. Если `web_element` не является списком, получает атрибуты для одного `web_element` и возвращает список атрибутов.

##### `get_webelement_by_locator`

```python
    async def get_webelement_by_locator(self, locator: SimpleNamespace | dict) -> WebElement | list[WebElement] | None:
        """Извлекает веб-элементы на основе предоставленного локатора."""
        ...
```

**Описание**: Извлекает веб-элементы на основе предоставленного локатора.

**Как работает функция**: <Описание работы функции.>

##### `get_webelement_as_screenshot`

```python
    async def get_webelement_as_screenshot(self, locator: SimpleNamespace | dict) -> str | None:
        """Делает скриншот найденного веб-элемента."""
        ...
```

**Описание**: Делает скриншот найденного веб-элемента.

**Как работает функция**: <Описание работы функции.>

##### `execute_event`

```python
    async def execute_event(self, locator: SimpleNamespace) -> None:
        """Выполняет события, связанные с локатором."""
        ...
```

**Описание**: Выполняет события, связанные с локатором.

**Как работает функция**: <Описание работы функции.>

##### `send_message`

```python
    async def send_message(self, locator: SimpleNamespace) -> None:
        """Отправляет сообщение веб-элементу."""
        ...
```

**Описание**: Отправляет сообщение веб-элементу.

**Как работает функция**: <Описание работы функции.>

### Диаграммы потока

Модуль включает диаграммы потока Mermaid для иллюстрации потока выполнения ключевых методов:

- **`execute_locator`**:
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

- **`evaluate_locator`**:
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

- **`get_attribute_by_locator`**:
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