# Модуль executor

## Обзор

Данный модуль предоставляет набор функций для взаимодействия с веб-элементами на основе предоставленного локатора.  Функции позволяют выполнять различные действия, такие как поиск элементов, отправка сообщений, получение атрибутов и извлечение HTML-контента.  Модуль обеспечивает гибкость и контролируемую скорость выполнения операций.

## Функции

### `execute_locator`

**Описание**: Выполняет действия на веб-элементе, используя указанный локатор.  Поддерживает отправку сообщений с регулируемой скоростью ввода.

**Параметры**:

- `locator` (dict): Словарь или объект с информацией о локаторе (например, тип поиска и селектор).  Необходим.
- `message` (str, optional): Сообщение для отправки элементу (например, текст для ввода). По умолчанию пустая строка.
- `typing_speed` (float, optional): Скорость ввода, если отправляется сообщение (в секундах между нажатиями клавиш). По умолчанию 0.0.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения в случае ошибки. По умолчанию `True`.

**Возвращает**:

- `any`: Результат выполнения локатора, который может быть веб-элементом, списком элементов, значением атрибута или результатом действия.


### `get_webelement_by_locator`

**Описание**: Находит и возвращает веб-элемент(ы) на странице, используя локатор.

**Параметры**:

- `locator` (dict): Словарь или объект с информацией о локаторе.  Необходим.

**Возвращает**:

- `any`: Один или несколько веб-элементов, найденных по локатору. Возвращает None, если элементы не найдены.


### `get_attribute_by_locator`

**Описание**: Получает значение атрибута веб-элемента, найденного по локатору.

**Параметры**:

- `locator` (dict): Словарь или объект с информацией о локаторе.  Необходим.
- `message` (str, optional): Сообщение для отправки элементу перед получением атрибута. По умолчанию пустая строка.

**Возвращает**:

- `any`: Значение атрибута веб-элемента. Возвращает `None`, если элемент не найден или произошла ошибка.


### `send_message`

**Описание**: Отправляет сообщение (например, текст) веб-элементу, используя локатор.

**Параметры**:

- `locator` (dict): Словарь или объект с информацией о локаторе.  Необходим.
- `message` (str): Сообщение для отправки элементу. Необходим.
- `typing_speed` (float, optional): Скорость ввода, если сообщение отправляется по частям. По умолчанию 0.0.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения в случае ошибки. По умолчанию `True`.

**Возвращает**:

- `bool`: `True`, если сообщение успешно отправлено, или `False`, если произошла ошибка.


### `get_url`

**Описание**: Загружает HTML-контент с указанного URL-адреса или локального файла.

**Параметры**:

- `url` (str): URL-адрес или путь к файлу для получения HTML-контента.  Необходим.
- `protocol` (str, optional): Протокол для URL (по умолчанию `https://`).

**Возвращает**:

- `bool`: `True`, если контент успешно загружен, или `False`, если произошла ошибка.


## Обработка исключений

В функциях модуля `executor` используется обработка исключений с помощью ключевого слова `except`.

```
...
except SomeError as ex:
    # Обработка ошибки
    ...
```

Обработка ошибок основана на концепции `continue_on_error`, которая позволяет продолжить выполнение, даже если произошла ошибка в одной из функций.
```