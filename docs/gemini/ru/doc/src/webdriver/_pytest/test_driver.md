# Модуль `hypotez/src/webdriver/_pytest/test_driver.py`

## Обзор

Данный модуль содержит тесты для класса `DriverBase`, проверяющие его методы. Тесты написаны с использованием `pytest` и `unittest.mock` для имитации взаимодействий с веб-драйвером и другими зависимостями.  Это позволяет изолировать тестируемый код и избежать взаимодействия с реальными веб-страницами и файлами.

## Тесты

### `TestDriverBase`

**Описание**: Класс `TestDriverBase` содержит тесты для методов класса `DriverBase`.

**Тесты:**

#### `test_driver_payload`

**Описание**: Тест метода `driver_payload`. Проверяет, что метод правильно вызывает соответствующие методы из зависимостей (JavaScript и ExecuteLocator) и сохраняет полученные значения в атрибутах класса.

**Использует:** `patch` для мокирования зависимостей.

**Проверяемые атрибуты:** `get_page_lang`, `ready_state`, `get_referrer`, `unhide_DOM_element`, `window_focus`, `execute_locator`, `click`, `get_webelement_as_screenshot`, `get_attribute_by_locator`, `send_message`

#### `test_scroll`

**Описание**: Тест метода `scroll`. Проверяет, что метод `scroll` корректно вызывает метод `execute_script` с правильными аргументами для скроллинга вверх и вниз.

**Использует:** `unittest.mock.Mock` для мокирования метода `execute_script`.

**Проверяемые методы:** `execute_script`.


#### `test_locale`

**Описание**: Тест свойства `locale`. Проверяет, что свойство `locale` корректно получает значение из мета-тегов страницы или из свойства `get_page_lang` в случае отсутствия мета-тегов.

**Использует:** `unittest.mock.Mock` для мокирования методов `find_element` и `get_page_lang`.

**Проверяемые свойства/методы:** `locale`, `find_element`, `get_page_lang`

#### `test_get_url`

**Описание**: Тест метода `get_url`. Проверяет корректную работу метода `get_url`, в том числе сохранение кукис.

**Использует:** `unittest.mock.Mock` для мокирования методов `get`, `wait` и `_save_cookies_localy`.

**Проверяемые методы:** `get_url`, `get`, `wait`, `_save_cookies_localy`

#### `test_extract_domain`

**Описание**: Тест метода `extract_domain`. Проверяет, что метод корректно извлекает доменное имя из URL.

**Проверяемые методы:** `extract_domain`

#### `test_save_cookies_localy`

**Описание**: Тест метода `_save_cookies_localy`. Проверяет, что метод корректно сохраняет кукис в файл.

**Использует:** `patch` для мокирования методов `open` и `pickle.dump`.

**Проверяемые методы:** `_save_cookies_localy`, `get_cookies`, `extract_domain`

#### `test_page_refresh`

**Описание**: Тест метода `page_refresh`. Проверяет, что метод перегружает страницу.

**Использует:** `unittest.mock.Mock` для мокирования метода `get_url`.

**Проверяемые методы:** `page_refresh`, `get_url`

#### `test_wait`

**Описание**: Тест метода `wait`. Проверяет, что метод `wait` корректно вызывает `time.sleep`.

**Использует:** `patch` для мокирования `time.sleep`.

**Проверяемые методы:** `wait`


#### `test_delete_driver_logs`

**Описание**: Тест метода `delete_driver_logs`. Проверяет, что метод удаляет файлы логов в заданной директории.

**Использует:** `patch` для мокирования методов `Path.iterdir`, `Path.is_file`, `Path.unlink`, `Path.is_dir`.

**Проверяемые методы:** `delete_driver_logs`