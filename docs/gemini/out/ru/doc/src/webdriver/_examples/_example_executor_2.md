# Модуль hypotez/src/webdriver/_examples/_example_executor_2.py

## Обзор

Этот модуль содержит примеры использования класса `ExecuteLocator` для выполнения различных задач тестирования с использованием Selenium WebDriver.  Примеры демонстрируют различные сценарии, включая получение элементов по XPath, обработку событий, получение атрибутов, отправку сообщений в элементы, работу со списками локаторов и оценку локаторов.  Также показаны примеры обработки исключений, возникающих при выполнении локаторов.


## Классы

### `ExecuteLocator`

**Описание**:  Класс `ExecuteLocator`, вероятно, содержит методы для выполнения локаторов, поиска элементов на странице веб-приложения и обработки событий.  Этот класс, судя по примерам,  используется для взаимодействия с веб-драйвером.


## Функции


### `execute_locator`

**Описание**:  Функция `execute_locator` выполняет заданный локатор.

**Параметры**:
- `locator (dict)`: Словарь, содержащий информацию о локаторе (например, тип селектора, XPath, время ожидания).  Ожидается, что структура соответствует используемому формату локаторов.
- `continue_on_error (bool, optional):` Если `True`, выполнение продолжит после ошибки. По умолчанию `False`.


**Возвращает**:
- `result (dict | None)`: Результат выполнения локатора. Возвращает словарь с результатом или `None` в случае ошибки.

**Вызывает исключения**:
- `ExecuteLocatorException`:  Возникает при проблемах с выполнением локатора (например, элемент не найден или ошибка во время выполнения).



### `send_message`

**Описание**: Функция `send_message`  отправляет сообщение в элемент.

**Параметры**:
- `locator (dict)`: Информация о локаторе.  Ожидается, что этот параметр соответствует формату локаторов,  определяющему элемент, в который нужно отправить сообщение.
- `message (str)`: Сообщение для отправки.
- `typing_speed (float, optional):` Скорость ввода сообщения (в секундах). По умолчанию `0.05`.
- `continue_on_error (bool, optional)`: Если `True`, выполнение продолжит после ошибки. По умолчанию `False`.


**Возвращает**:
- `result (dict | None)`: Результат отправки сообщения или `None` при ошибке.

**Вызывает исключения**:
- `ExecuteLocatorException`:  Возникает при проблемах с выполнением локатора или отправкой сообщения (например, элемент не найден).


### `evaluate_locator`

**Описание**: Функция `evaluate_locator`  оценивает локатор.

**Параметры**:
- `locator (str)`:  Идентификатор или выражение, которое должно быть оценено.


**Возвращает**:
- `result (str | None)`: Результат оценки или `None` при ошибке.


**Вызывает исключения**:
- `ExecuteLocatorException`:  Возникает при ошибках, связанных с оценкой локатора.


## Примеры

Примеры в коде демонстрируют различные варианты использования методов класса `ExecuteLocator`, включая разные типы локаторов, обработку событий, атрибутов, и работу со списками локаторов.




## Модули

Этот модуль использует модули:

- `selenium`
- `src.webdriver.executor`
- `src`
- `gs`
- `src.logger.exceptions`


## Обработка исключений


Код содержит блоки `try...except` для обработки исключения `ExecuteLocatorException`.  Это позволяет обрабатывать ошибки при выполнении локаторов, сообщая об ошибке и, при необходимости, позволяя продолжить выполнение программы.  Важно обратить внимание на значение `continue_on_error` в методах.