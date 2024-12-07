# Модуль hypotez/src/webdriver/_pytest/test_driver.py

## Обзор

Этот модуль содержит тесты для класса `DriverBase` из модуля `src.webdriver.driver`. Тесты проверяют корректность работы методов класса, используя фреймворк `pytest` и `unittest.mock` для имитации взаимодействия с веб-драйвером и другими зависимостями.

## Оглавление

- [Модуль hypotez/src/webdriver/_pytest/test_driver.py](#модуль-hypotezsrcwebdriver_pytesttest_driverpy)
- [Обзор](#обзор)
- [Классы](#классы)
- [Функции](#функции)
    - [`test_driver_payload`](#test_driver_payload)
    - [`test_scroll`](#test_scroll)
    - [`test_locale`](#test_locale)
    - [`test_get_url`](#test_get_url)
    - [`test_extract_domain`](#test_extract_domain)
    - [`test_save_cookies_localy`](#test_save_cookies_localy)
    - [`test_page_refresh`](#test_page_refresh)
    - [`test_wait`](#test_wait)
    - [`test_delete_driver_logs`](#test_delete_driver_logs)


## Классы

### `TestDriverBase`

**Описание**: Класс содержит тесты для методов класса `DriverBase`.

**Методы**:

- [`test_driver_payload`](#test_driver_payload): Тест метода `driver_payload`.
- [`test_scroll`](#test_scroll): Тест метода `scroll`.
- [`test_locale`](#test_locale): Тест свойства `locale`.
- [`test_get_url`](#test_get_url): Тест метода `get_url`.
- [`test_extract_domain`](#test_extract_domain): Тест метода `extract_domain`.
- [`test_save_cookies_localy`](#test_save_cookies_localy): Тест метода `_save_cookies_localy`.
- [`test_page_refresh`](#test_page_refresh): Тест метода `page_refresh`.
- [`test_wait`](#test_wait): Тест метода `wait`.
- [`test_delete_driver_logs`](#test_delete_driver_logs): Тест метода `delete_driver_logs`.

## Функции

### `test_driver_payload`

**Описание**: Тестирует метод `driver_payload` класса `DriverBase`.  Использует `unittest.mock` для имитации зависимостей (`JavaScript`, `ExecuteLocator`). Проверяет, что метод правильно устанавливает атрибуты класса, соответствующие методам моков.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
-  Не применимо (тест утверждает корректное выполнение).

**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_scroll`

**Описание**: Тестирует метод `scroll` класса `DriverBase`. Использует `unittest.mock` для имитации `execute_script` и `wait`. Проверяет, что метод `scroll` корректным образом вызывает `execute_script` для прокрутки вверх и вниз.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- `bool`:  True, если метод отработал корректно.

**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_locale`

**Описание**: Тестирует свойство `locale` класса `DriverBase`.  Проверяет работу свойства в случае, когда тег meta найден и не найден.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.


**Возвращает**:
- `str`: Значение свойства `locale`.


**Вызывает исключения**:
- `Exception`: Если поиск элемента не удается.


### `test_get_url`

**Описание**: Тестирует метод `get_url` класса `DriverBase`.  Проверяет, что метод устанавливает `previous_url` и вызывает `get` с нужным значением.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- `bool`: True, если метод отработал корректно.


**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_extract_domain`

**Описание**: Тестирует метод `extract_domain` класса `DriverBase`. Проверяет корректное извлечение домена из URL.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- `str`: Доменное имя.

**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_save_cookies_localy`

**Описание**: Тестирует метод `_save_cookies_localy` класса `DriverBase`. Проверяет сохранение куки в файл.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- `bool`: True, если метод отработал корректно.


**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_page_refresh`

**Описание**: Тестирует метод `page_refresh` класса `DriverBase`. Проверяет, что метод вызывает `get_url` с текущим URL.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- `bool`: True, если метод отработал корректно.

**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_wait`

**Описание**: Тестирует метод `wait` класса `DriverBase`. Использует `unittest.mock` для проверки вызова `time.sleep`.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- Не применимо (тест утверждает корректный вызов `sleep`).


**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).


### `test_delete_driver_logs`

**Описание**: Тестирует метод `delete_driver_logs` класса `DriverBase`.  Проверяет удаление файлов в директории, используя патчи для `Path.iterdir`, `Path.is_file`, `Path.unlink`.

**Параметры**:
- `driver_base` (object): Экземпляр класса `DriverBase`.

**Возвращает**:
- `bool`: True, если метод отработал корректно.

**Вызывает исключения**:
- Не применимо (тест не должен вызывать исключения).