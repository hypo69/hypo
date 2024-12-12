# Модуль hypotez/src/webdriver/_examples/_example_executor_2.py

## Обзор

Этот модуль содержит примеры использования класса `ExecuteLocator` для различных сценариев тестирования.  В нем показаны примеры создания экземпляра `ExecuteLocator`, выполнения задач с его помощью, а также обработка ошибок. Примеры охватывают различные параметры, такие как разные типы локаторов, события, атрибуты, и работу со списками локаторов.

## Импорты

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
from src.logger.exceptions import ExecuteLocatorException
```

## Классы

Не содержит классов.

## Функции

Не содержит функций.

## Примеры использования `ExecuteLocator`

### `execute_locator`

**Описание**: Выполнение заданного локатора.

**Параметры**:

- `locator (dict)`: Словарь с параметрами локатора.  Обязательно содержит ключи `by`, `selector`, `timeout`. Подробное описание параметров внутри словаря в примерах.
- `continue_on_error (bool, optional)`:  Флаг, определяющий, следует ли продолжать выполнение при ошибке. По умолчанию `False`.


**Возвращает**:

- `result (any)`: Результат выполнения локатора. В зависимости от запрошенного атрибута может быть строкой, списком, элементом Selenium и т.д., или None.


**Вызывает исключения**:

- `ExecuteLocatorException`: При возникновении ошибки при выполнении локатора.


### `send_message`

**Описание**: Отправка сообщения в элемент.

**Параметры**:

- `locator (dict)`: Словарь с параметрами локатора.  Обязательно содержит ключ `selector`.
- `message (str)`: Сообщение для отправки.
- `typing_speed (float, optional)`: Скорость ввода.  По умолчанию `0.05`.
- `continue_on_error (bool, optional)`:  Флаг, определяющий, следует ли продолжать выполнение при ошибке. По умолчанию `False`.

**Возвращает**:

- `result (any)`: Результат выполнения send_message, обычно None, но может быть информацией об успехе/ошибке.

**Вызывает исключения**:

- `ExecuteLocatorException`: При возникновении ошибки при выполнении отправки сообщения.

### `evaluate_locator`

**Описание**: Оценка локатора.

**Параметры**:

- `attribute (str)`: Атрибут для оценки.


**Возвращает**:

- `attribute_value (any)`: Значение атрибута.


**Вызывает исключения**:

- `ExecuteLocatorException`: При возникновении ошибки при оценке локатора.

## Примеры

### Создание экземпляра WebDriver и ExecuteLocator

```python
driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
driver.get("https://example.com")
locator = ExecuteLocator(driver)
```

### Простой пример использования `execute_locator`

```python
simple_locator = {
    "by": "XPATH",
    "selector": "//h1",
    "attribute": "textContent",
    # ... другие параметры
}

result = locator.execute_locator(simple_locator)
print(f"Результат выполнения простого локатора: {result}")
```

### Обработка ошибок

```python
try:
    locator.execute_locator(complex_locator)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка: {ex}")
```

### Пример `send_message`

```python
message_locator = {
    "by": "XPATH",
    "selector": "//input[@name='search']",
    "event": "%SEARCH%", # ключевое слово для отправки сообщения
    # ... другие параметры
}

message = "Купить новый телефон"
result = locator.send_message(message_locator, message)
print(f"Результат отправки сообщения: {result}")
```

### Пример с использованием списка локаторов

```python
multi_locator = {
    "by": ["XPATH", "XPATH"],
    "selector": ["//button[@id='submit']", "//input[@id='username']"],
    "event": ["click()", "send_keys('user')"],
    # ... другие параметры
}

results = locator.execute_locator(multi_locator)
print(f"Результаты выполнения множества локаторов: {results}")
```


### Пример использования `evaluate_locator`


```python
attribute_locator = {
    # ...
}

attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
print(f"Значение атрибута: {attribute_value}")
```

## Закрытие драйвера


```python
driver.quit()
```

**Важно:** Этот пример предполагает, что переменная `gs['chrome_driver_path']` содержит корректный путь к исполняемому файлу драйвера Chrome. Подставьте правильное значение.  Также убедитесь, что необходимые библиотеки (Selenium, src, etc.) установлены и доступны.