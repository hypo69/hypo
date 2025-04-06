# Модуль `executor.py`

## Обзор

Модуль `executor.py` является ключевым компонентом для автоматизированного взаимодействия с веб-страницами в проекте `hypotez`. Он предоставляет функциональность для поиска веб-элементов с использованием Selenium на основе предоставленных локаторов, выполнения различных действий с этими элементами (например, клики, ввод текста), а также обработки возникающих ошибок.

## Подробней

Этот модуль позволяет находить элементы на веб-странице по различным локаторам (например, `id`, `class`, `xpath`), выполнять с ними различные действия (например, клик, ввод текста) и получать значения их атрибутов. Он также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов. Модуль использует асинхронность для выполнения операций, что повышает эффективность работы.

## Классы

### `ExecuteLocator`

**Описание**:
Класс `ExecuteLocator` предназначен для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Принцип работы**:
Класс инициализируется с драйвером Selenium и использует `ActionChains` для выполнения сложных действий, таких как ввод текста и клики. Он предоставляет методы для выполнения действий с элементами, получения атрибутов и скриншотов элементов. Все операции обрабатываются асинхронно.

**Атрибуты**:
- `driver` (Optional[object]): Драйвер Selenium, используемый для взаимодействия с веб-страницей. По умолчанию `None`.
- `actions` (ActionChains): Объект `ActionChains` для выполнения сложных действий с элементами. Инициализируется в методе `__post_init__`.
- `mode` (str): Режим работы (например, "debug"). По умолчанию "debug".

**Методы**:
- `__post_init__`: Инициализирует объект `ActionChains` после создания экземпляра класса, если передан драйвер.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `_evaluate_locator`: Выполняет обработку атрибутов локатора.
- `get_attribute_by_locator`: Получает атрибуты веб-элемента или списка веб-элементов.
- `get_webelement_by_locator`: Получает веб-элемент или список элементов на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

## Функции

### `execute_locator`

```python
    async def execute_locator(
        self,
        locator:  dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = "presence_of_element_located",
        message: Optional[str] = None,
        typing_speed: Optional[float] = 0,
    ) ->  Optional[str | list | dict | WebElement | bool]:
        """
        Executes actions on a web element based on the provided locator.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            timeout: Timeout for locating the element (seconds).
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Optional message for actions like send_keys or type.
            typing_speed: Typing speed for send_keys events (seconds).

        Returns:
            The result of the operation, which can be a string, list, dict, WebElement, bool, or None.
        """
```

**Назначение**:
Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора в виде словаря или объекта `SimpleNamespace`, содержащие информацию о том, как найти элемент.
- `timeout` (Optional[float]): Максимальное время ожидания (в секундах) для поиска элемента. По умолчанию `0`.
- `timeout_for_event` (Optional[str]): Условие ожидания элемента. Может быть `presence_of_element_located` (ожидание появления элемента) или `visibility_of_all_elements_located` (ожидание видимости всех элементов). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str]): Сообщение для действий, таких как `send_keys` или `type`. По умолчанию `None`.
- `typing_speed` (Optional[float]): Скорость печати (в секундах) для событий `send_keys`. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции. Может быть строкой, списком, словарем, объектом `WebElement`, булевым значением или `None`.

**Как работает функция**:
1. **Преобразование локатора**: Если локатор является словарем, он преобразуется в объект `SimpleNamespace` для упрощения доступа к его атрибутам.
2. **Проверка локатора**: Проверяется наличие атрибутов `attribute` и `selector` в локаторе. Если они отсутствуют, функция возвращает `None`.
3. **Внутренняя функция `_parse_locator`**: Вызывается внутренняя асинхронная функция `_parse_locator` для обработки инструкций локатора.

**Внутренние функции**:

#### `_parse_locator`

```python
            async def _parse_locator(
            locator: SimpleNamespace,
            message: Optional[str] = None,
            timeout: Optional[float] = 0,
            timeout_for_event: Optional[str] = "presence_of_element_located",
            typing_speed: Optional[float] = 0,
        ) -> Optional[str | list | dict | WebElement | bool]:
            """Parses and executes locator instructions."""
```

**Назначение**:
Анализирует и выполняет инструкции, содержащиеся в локаторе.

**Параметры**:
- `locator` (SimpleNamespace): Объект `SimpleNamespace`, содержащий данные локатора.
- `message` (Optional[str]): Сообщение для действий, таких как `send_keys` или `type`. По умолчанию `None`.
- `timeout` (Optional[float]): Максимальное время ожидания (в секундах) для поиска элемента. По умолчанию `0`.
- `timeout_for_event` (Optional[str]): Условие ожидания элемента. Может быть `presence_of_element_located` (ожидание появления элемента) или `visibility_of_all_elements_located` (ожидание видимости всех элементов). По умолчанию `"presence_of_element_located"`.
- `typing_speed` (Optional[float]): Скорость печати (в секундах) для событий `send_keys`. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции. Может быть строкой, списком, словарем, объектом `WebElement`, булевым значением или `None`.

**Как работает функция**:
1. **Проверка флага `mandatory`**: Если у локатора есть атрибуты `event` и `attribute`, но отсутствует флаг `mandatory`, локатор пропускается.
2. **Обработка атрибута `by`**:
   - Если `locator.by` является строкой, она преобразуется в нижний регистр.
   - Если `locator.attribute` существует, он обрабатывается с помощью метода `_evaluate_locator`.
   - Если `locator.by` равно `"value"`, возвращается `locator.attribute`.
   - Если `locator.by` равно `"url"`, из URL извлекается значение атрибута.
3. **Выполнение события или получение атрибута**:
   - Если `locator.event` существует, вызывается метод `execute_event`.
   - Если `locator.attribute` существует, вызывается метод `get_attribute_by_locator`.
   - В противном случае вызывается метод `get_webelement_by_locator`.
4. **Обработка списков селекторов и атрибутов**: Если `locator.selector` и `locator.by` являются списками, выполняется итерация по ним и создаются пары элементов.
5. **Обработка ошибок**: Если локатор не содержит списки `selector` и `by` или значение `sorted` недействительно, выводится предупреждение.

4. **Возврат результата**: Функция возвращает результат, полученный от `_parse_locator`.

**Примеры**:

```python
# Пример локатора в виде словаря
locator_dict = {
    "by": "id",
    "selector": "my_element",
    "attribute": "value",
    "mandatory": True,
}

# Пример локатора в виде SimpleNamespace
import types
locator_ns = types.SimpleNamespace(
    by="xpath",
    selector="//button[@id='my_button']",
    event="click()",
    mandatory=False,
)
```

**ASCII схема работы функции `execute_locator`**:

```
Начало
  │
  ├──> Преобразование locator в SimpleNamespace (если это dict)
  │
  ├──> Проверка наличия attribute и selector в locator
  │   │
  │   └──> Отсутствуют: Возврат None
  │   │
  │   └──> Присутствуют:
  │        │
  │        └──> Вызов _parse_locator(locator, message, timeout, timeout_for_event, typing_speed)
  │             │
  │             └──> _parse_locator:
  │                  │
  │                  ├──> Проверка locator.event и locator.attribute при отсутствии locator.mandatory
  │                  │   │
  │                  │   └──> True: Возврат None
  │                  │   │
  │                  │   └──> False:
  │                  │        │
  │                  │        ├──> Проверка типа locator.by (str или list)
  │                  │        │   │
  │                  │        │   └──> str:
  │                  │        │   │    │
  │                  │        │   │    ├──> Обработка locator.attribute
  │                  │        │   │    │
  │                  │        │   │    ├──> Проверка locator.by == "value" или "url"
  │                  │        │   │    │
  │                  │        │   │    ├──> Вызов execute_event или get_attribute_by_locator или get_webelement_by_locator
  │                  │        │   │    │
  │                  │        │   │    └──> Возврат результата
  │                  │        │   │
  │                  │        │   └──> list:
  │                  │        │        │
  │                  │        │        ├──> Обработка списков locator.selector и locator.by
  │                  │        │        │
  │                  │        │        └──> Возврат zipped_pairs
  │                  │        │
  │                  │        └──> Вывод предупреждения, если locator не содержит selector и by списки или sorted невалиден
  │                  │
  │                  └──> Возврат результата из _parse_locator
  │
  └──> Возврат результата
  │
Конец
```

### `_evaluate_locator`

```python
    def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Evaluates and processes locator attributes.

        Args:
            attribute: Attribute to evaluate (can be a string, list of strings, or a dictionary).

        Returns:
            The evaluated attribute, which can be a string, list of strings, or dictionary.
        """
```

**Назначение**:
Оценивает и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для оценки (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Оцененный атрибут, который может быть строкой, списком строк или словарем.

**Как работает функция**:
1. **Внутренняя функция `_evaluate`**: Определяется внутренняя функция `_evaluate`, которая принимает строку атрибута и возвращает соответствующее значение `Keys`, если атрибут соответствует паттерну `%\\w+%`, иначе возвращает исходный атрибут.
2. **Обработка атрибута**:
   - Если атрибут является списком, функция применяет `_evaluate` к каждому элементу списка и возвращает новый список.
   - Если атрибут является строкой, функция применяет `_evaluate` к строке и возвращает результат.

**Внутренние функции**:

#### `_evaluate`

```python
        def _evaluate(attr: str) -> Optional[str]:
            """Evaluates single attribute string."""
            return getattr(Keys, re.findall(r"%(\\w+)%", attr)[0], None) if re.match(r"^%\\w+%", attr) else attr
```

**Назначение**:
Оценивает отдельную строку атрибута.

**Параметры**:
- `attr` (str): Строка атрибута для оценки.

**Возвращает**:
- `Optional[str]`: Соответствующее значение `Keys`, если атрибут соответствует паттерну `%\\w+%`, иначе возвращает исходный атрибут.

**Как работает функция**:
1. **Проверка паттерна**: Проверяет, соответствует ли атрибут паттерну `^%\\w+%`.
2. **Извлечение значения**: Если атрибут соответствует паттерну, извлекает значение между `%` и использует его для получения атрибута из класса `Keys`.
3. **Возврат значения**: Возвращает полученное значение из `Keys` или исходный атрибут, если паттерн не совпадает.

**Примеры**:

```python
# Пример вызова с атрибутом в виде строки
attribute_string = "%ENTER%"
evaluated_attribute = ExecuteLocator()._evaluate_locator(attribute_string)
print(evaluated_attribute)  # Вывод: Keys.ENTER

# Пример вызова с атрибутом в виде списка
attribute_list = ["%SHIFT%", "%TAB%"]
evaluated_attribute = ExecuteLocator()._evaluate_locator(attribute_list)
print(evaluated_attribute)  # Вывод: [Keys.SHIFT, Keys.TAB]
```

**ASCII схема работы функции `_evaluate_locator`**:

```
Начало
  │
  ├──> Проверка типа attribute (str, list или dict)
  │   │
  │   └──> list:
  │   │    │
  │   │    └──> Применение _evaluate к каждому элементу списка
  │   │    │
  │   │    └──> Возврат нового списка
  │   │
  │   └──> str:
  │   │    │
  │   │    └──> Применение _evaluate к строке
  │   │    │
  │   │    └──> Возврат результата
  │   │
  │   └──> dict:
  │   │    │
  │   │    └──> Возврат attribute без изменений
  │   │
  │   └──> _evaluate:
  │        │
  │        ├──> Проверка соответствия attr паттерну ^%\w+%
  │        │   │
  │        │   └──> True:
  │        │   │    │
  │        │   │    └──> Извлечение значения между %
  │        │   │    │
  │        │   │    └──> Получение атрибута из класса Keys
  │        │   │    │
  │        │   │    └──> Возврат значения из Keys
  │        │   │
  │        │   └──> False:
  │        │        │
  │        │        └──> Возврат исходного attr
  │        │
  │   └──> Возврат результата
  │
Конец
```

### `get_attribute_by_locator`

```python
    async def get_attribute_by_locator(
        self,
        locator: SimpleNamespace | dict,
        timeout: Optional[float] = 0,
        timeout_for_event: str = "presence_of_element_located",
        message: Optional[str] = None,
        typing_speed: float = 0,
    ) -> Optional[WebElement | list[WebElement]]:
        """
        Retrieves attributes from a web element or a list of web elements.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            timeout: Timeout for locating the element (seconds).
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Not used in this function.
            typing_speed: Not used in this function.

        Returns:
            The attribute value(s) as a WebElement, list of WebElements, or None if not found.
        """
```

**Назначение**:
Извлекает атрибуты из веб-элемента или списка веб-элементов.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора в виде `SimpleNamespace` или словаря.
- `timeout` (Optional[float]): Время ожидания (в секундах) для поиска элемента. По умолчанию `0`.
- `timeout_for_event` (str): Условие ожидания элемента. Может быть `presence_of_element_located` (ожидание появления элемента) или `visibility_of_all_elements_located` (ожидание видимости всех элементов). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str]): Не используется в этой функции.
- `typing_speed` (float): Не используется в этой функции.

**Возвращает**:
- `Optional[WebElement | list[WebElement]]`: Значение атрибута(ов) в виде `WebElement`, списка `WebElement` или `None`, если элемент не найден.

**Как работает функция**:
1. **Преобразование локатора**: Преобразует локатор в `SimpleNamespace`, если он представлен в виде словаря.
2. **Получение веб-элемента**: Получает веб-элемент с помощью метода `get_webelement_by_locator`.
3. **Обработка отсутствия элемента**: Если веб-элемент не найден и `locator.mandatory` имеет значение `True`, функция записывает отладочное сообщение и возвращает `None`.
4. **Внутренняя функция `_parse_dict_string`**: Если `locator.attribute` является строкой и начинается с `{`, вызывается функция `_parse_dict_string` для преобразования строки в словарь.
5. **Внутренняя функция `_get_attributes_from_dict`**: Если атрибут является словарем, вызывается функция `_get_attributes_from_dict` для получения значений атрибутов на основе словаря.
6. **Извлечение атрибутов**: Извлекает значение атрибута из веб-элемента(ов) и возвращает его.

**Внутренние функции**:

#### `_parse_dict_string`

```python
        def _parse_dict_string(attr_string: str) -> dict | None:
            """Parses a string like \'{attr1:attr2}\' into a dictionary."""
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))
                }
            except ValueError as ex:
                logger.debug(f"Invalid attribute string format: {attr_string!r}", ex)
                return None
```

**Назначение**:
Преобразует строку вида `'{attr1:attr2}'` в словарь.

**Параметры**:
- `attr_string` (str): Строка для преобразования в словарь.

**Возвращает**:
- `dict | None`: Словарь, полученный из строки, или `None`, если строка имеет неверный формат.

**Как работает функция**:
1. **Преобразование строки**: Пытается преобразовать входную строку в словарь, разделяя строку на пары ключ-значение и удаляя лишние пробелы.
2. **Обработка ошибок**: Если строка имеет неверный формат, записывает отладочное сообщение и возвращает `None`.

#### `_get_attributes_from_dict`

```python
        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """Retrieves attribute values from a WebElement based on a dictionary."""
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = web_element.get_attribute(key)
                    attr_value = web_element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    logger.debug(f"Error retrieving attributes \'{key}\' or \'{value}\' from element.", ex)
                    return {}
            return result
```

**Назначение**:
Извлекает значения атрибутов из `WebElement` на основе словаря.

**Параметры**:
- `web_element` (WebElement): Веб-элемент, из которого нужно извлечь атрибуты.
- `attr_dict` (dict): Словарь, содержащий пары ключ-значение атрибутов.

**Возвращает**:
- `dict`: Словарь, содержащий извлеченные значения атрибутов.

**Как работает функция**:
1. **Извлечение атрибутов**: Перебирает элементы словаря `attr_dict`, извлекает значения атрибутов с помощью метода `get_attribute` и сохраняет их в словаре `result`.
2. **Обработка ошибок**: Если происходит ошибка при извлечении атрибута, записывает отладочное сообщение и возвращает пустой словарь.

**Примеры**:

```python
# Пример локатора с атрибутом в виде строки
locator_string = {
    "by": "id",
    "selector": "my_element",
    "attribute": "value",
    "mandatory": True,
}
attribute_value = await ExecuteLocator().get_attribute_by_locator(locator_string)

# Пример локатора с атрибутом в виде словаря
locator_dict = {
    "by": "xpath",
    "selector": "//input[@id='my_input']",
    "attribute": "{class:value}",
    "mandatory": False,
}
attributes = await ExecuteLocator().get_attribute_by_locator(locator_dict)
```

**ASCII схема работы функции `get_attribute_by_locator`**:

```
Начало
  │
  ├──> Преобразование locator в SimpleNamespace (если это dict)
  │
  ├──> Получение веб-элемента с помощью get_webelement_by_locator
  │
  ├──> Проверка наличия веб-элемента
  │   │
  │   └──> Отсутствует:
  │   │    │
  │   │    └──> Проверка locator.mandatory
  │   │    │
  │   │    └──> True: Логирование ошибки
  │   │    │
  │   │    └──> Возврат None
  │   │
  │   └──> Присутствует:
  │        │
  │        ├──> Проверка типа locator.attribute
  │        │   │
  │        │   └──> str и начинается с "{":
  │        │   │    │
  │        │   │    └──> Преобразование строки в словарь с помощью _parse_dict_string
  │        │   │    │
  │        │   │    └──> Получение атрибутов из веб-элемента на основе словаря с помощью _get_attributes_from_dict
  │        │   │    │
  │        │   │    └──> Возврат результата
  │        │   │
  │        │   └──> list:
  │        │   │    │
  │        │   │    └──> Извлечение атрибутов из каждого веб-элемента в списке
  │        │   │    │
  │        │   │    └──> Возврат списка атрибутов
  │        │   │
  │        │   └──> Другое:
  │        │        │
  │        │        └──> Извлечение атрибута из веб-элемента
  │        │        │
  │        │        └──> Возврат значения атрибута
  │        │
  │   └──> _parse_dict_string:
  │   │    │
  │   │    └──> Преобразование строки в словарь
  │   │    │
  │   │    └──> Обработка ошибок преобразования
  │   │    │
  │   │    └──> Возврат словаря или None
  │   │
  │   └──> _get_attributes_from_dict:
  │   │    │
  │   │    └──> Извлечение значений атрибутов из веб-элемента на основе словаря
  │   │    │
  │   │    └──> Обработка ошибок извлечения атрибутов
  │   │    │
  │   │    └──> Возврат словаря с извлеченными атрибутами
  │   │
  │   └──> Возврат результата
  │
Конец
```

### `get_webelement_by_locator`

```python
    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = "presence_of_element_located",
    ) -> Optional[WebElement | List[WebElement]]:
        """
        Retrieves a web element or list of elements based on the provided locator.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            timeout: Timeout for locating the element (seconds).
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').

        Returns:
           WebElement, list of WebElements, or None if not found.
        """
```

**Назначение**:
Извлекает веб-элемент или список элементов на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или `SimpleNamespace`).
- `timeout` (Optional[float]): Время ожидания (в секундах) для поиска элемента. По умолчанию `0`.
- `timeout_for_event` (Optional[str]): Условие ожидания элемента. Может быть `presence_of_element_located` (ожидание появления элемента) или `visibility_of_all_elements_located` (ожидание видимости всех элементов). По умолчанию `"presence_of_element_located"`.

**Возвращает**:
- `Optional[WebElement | List[WebElement]]`: `WebElement`, список `WebElement` или `None`, если элемент не найден.

**Как работает функция**:
1. **Получение таймаута**: Если `timeout` больше `0`, используется его значение, иначе используется значение атрибута `timeout` из локатора.
2. **Внутренняя функция `_parse_elements_list`**: Вызывается внутренняя функция `_parse_elements_list` для фильтрации списка веб-элементов на основе атрибута `if_list`.
3. **Получение драйвера и локатора**: Получает драйвер и преобразует локатор в `SimpleNamespace`, если он представлен в виде словаря.
4. **Поиск элементов**:
   - Если `timeout` равен `0`, элементы ищутся с помощью метода `driver.find_elements`.
   - Если `timeout` больше `0`, используется `WebDriverWait` для ожидания элемента в течение заданного времени.
5. **Обработка ошибок**: Если во время поиска элемента происходит `TimeoutException` или другое исключение, функция записывает сообщение об ошибке и возвращает `None`.
6. **Возврат элементов**: Если элементы найдены, они фильтруются с помощью `_parse_elements_list` и возвращаются.

**Внутренние функции**:

#### `_parse_elements_list`

```python
        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement], locator: SimpleNamespace
        ) ->  Optional[WebElement | List[WebElement]]:
            """Filters a list of web elements based on the if_list attribute."""
            if not isinstance(web_elements, list):\
                return web_elements\
            \
            if_list = locator.if_list\
            \
            if if_list == "all":\
                return web_elements\
            elif if_list == "first":\
                return web_elements[0]\
            elif if_list == "last":\
                return web_elements[-1]\
            elif if_list == "even":\
                return [web_elements[i] for i in range(0, len(web_elements), 2)]\
            elif if_list == "odd":\
                return [web_elements[i] for i in range(1, len(web_elements), 2)]\
            elif isinstance(if_list, list):\
                return [web_elements[i] for i in if_list]\
            elif isinstance(if_list, int):\
                return web_elements[if_list - 1]\
            \
            return web_elements
```

**Назначение**:
Фильтрует список веб-элементов на основе атрибута `if_list`.

**Параметры**:
- `web_elements` (WebElement | List[WebElement]): Веб-элемент или список веб-элементов для фильтрации.
- `locator` (SimpleNamespace): Данные локатора.

**Возвращает**:
- `Optional[WebElement | List[WebElement]]`: Отфильтрованный веб-элемент или список веб-элементов.

**Как работает функция**:
1. **Проверка типа**: Если `web_elements` не является списком, функция возвращает его без изменений.
2. **Фильтрация**: В зависимости от значения атрибута `if_list` выполняется фильтрация списка:
   - `"all"`: возвращает весь список.
   - `"first"`: возвращает первый элемент.
   - `"last"`: возвращает последний элемент.
   - `"even"`: возвращает элементы с четными индексами.
   - `"odd"`: возвращает элементы с нечетными индексами.
   - `list`: возвращает элементы с индексами, указанными в списке.
   - `int`: возвращает элемент с указанным индексом (индексация начинается с 1).
3. **Возврат элементов**: Возвращает отфильтрованный список элементов.

**Примеры**:

```python
# Пример локатора для получения всех элементов
locator_all = {
    "by": "class name",
    "selector": "my_class",
    "if_list": "all",
}
elements_all = await ExecuteLocator().get_webelement_by_locator(locator_all)

# Пример локатора для получения первого элемента
locator_first = {
    "by": "tag name",
    "selector": "div",
    "if_list": "first",
}
element_first = await ExecuteLocator().get_webelement_by_locator(locator_first)
```

**ASCII схема работы функции `get_webelement_by_locator`**:

```
Начало
  │
  ├──> Определение таймаута
  │
  ├──> Определение _parse_elements_list(web_elements, locator)
  │   │
  │   └──> Фильтрация списка веб-элементов на основе атрибута if_list
  │   │
  │   └──> Возврат отфильтрованного списка веб-элементов
  │
  ├──> Преобразование locator в SimpleNamespace (если это dict)
  │
  ├──> Поиск элементов с помощью driver.find_elements или WebDriverWait
  │   │
  │   └──> Обработка ошибок TimeoutException или Exception
  │   │
  │   └──> Возврат None в случае ошибки
  │
  ├──> Фильтрация найденных элементов с помощью _parse_elements_list
  │
  └──> Возврат отфильтрованных элементов
  │
Конец
```

### `get_webelement_as_screenshot`

```python
    async def get_webelement_as_screenshot(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = "presence_of_element_located",
        message: Optional[str] = None,
        typing_speed: float = 0,
        webelement: Optional[WebElement] = None,
    ) -> Optional[BinaryIO]:
        """
        Takes a screenshot of the located web element.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            timeout: Timeout for locating the element (seconds).
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Not used in this function.
            typing_speed: Not used in this function.
            webelement: Optional pre-fetched web element.

        Returns:
           BinaryIO stream of the screenshot or None if failed.
        """
```

**Назначение**:
Делает скриншот найденного веб-элемента.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора (словарь или `SimpleNamespace`).
- `timeout` (float): Время ожидания (в секундах) для поиска элемента. По умолчанию `5`.
- `timeout_for_event` (str): Условие ожидания элемента. Может быть `presence_of_element_located` (ожидание появления элемента) или `visibility_of_all_elements_located` (ожидание видимости всех элементов). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str]): Не используется в этой функции.
- `typing_speed` (float): Не используется в этой функции.
- `webelement` (Optional[WebElement]): Предопределенный веб-элемент. Если передан, поиск элемента не выполняется.

**Возвращает**:
- `Optional[BinaryIO]`: Поток `BinaryIO` скриншота или `None`, если не удалось сделать скриншот.

**Как работает функция**:
1. **Преобразование локатора**: Преобразует локатор в `SimpleNamespace`, если он представлен в виде словаря.
2. **Получение веб-элемента**: Если `webelement` не передан, элемент ищется с помощью метода `get_webelement_by_locator`.
3. **Создание скриншота**: Если веб-элемент найден, делается его скриншот с помощью метода `screenshot_as_png`.
4. **Обработка ошибок**: Если происходит ошибка во время создания скриншота, функция записывает сообщение об ошибке и возвращает `None`.

**Примеры**:

```python
# Пример локатора для создания скриншота элемента
locator_screenshot = {
    "by": "id",
    "selector": "my_element",
}
screenshot = await ExecuteLocator().get_webelement_as_screenshot(locator