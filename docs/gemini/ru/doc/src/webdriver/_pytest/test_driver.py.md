# Модуль `src.webdriver._pytest.test_driver`

## Обзор

Файл `test_driver.py` содержит тесты для методов класса `DriverBase`.
Он использует `pytest` и `unittest.mock` для изоляции тестируемого кода от реальных веб-страниц и файловой системы.

## Содержание

- [Классы](#классы)
    - [`TestDriverBase`](#testdriverbase)
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

**Описание**: Класс, содержащий набор тестов для методов класса `DriverBase`.

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

**Описание**: Тестирует метод `driver_payload` класса `DriverBase`. Проверяет, что свойства и методы из `JavaScript` и `ExecuteLocator` правильно присваиваются экземпляру `DriverBase`.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_scroll`

**Описание**: Тестирует метод `scroll` класса `DriverBase`. Проверяет корректность вызова `execute_script` с разными направлениями скролла.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_locale`

**Описание**: Тестирует свойство `locale` класса `DriverBase`. Проверяет, что свойство возвращает значение из мета-тега, если он есть, или из `get_page_lang`, если мета-тег не найден.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_get_url`

**Описание**: Тестирует метод `get_url` класса `DriverBase`. Проверяет, что метод вызывает `get` с переданным URL, сохраняет предыдущий URL и вызывает `_save_cookies_localy`.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_extract_domain`

**Описание**: Тестирует метод `extract_domain` класса `DriverBase`. Проверяет правильность извлечения доменного имени из URL.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_save_cookies_localy`

**Описание**: Тестирует метод `_save_cookies_localy` класса `DriverBase`. Проверяет, что метод сохраняет cookies в файл с помощью `pickle.dump`.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_page_refresh`

**Описание**: Тестирует метод `page_refresh` класса `DriverBase`. Проверяет, что метод вызывает `get_url` с текущим URL.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_wait`

**Описание**: Тестирует метод `wait` класса `DriverBase`. Проверяет, что метод вызывает `time.sleep` с переданным значением.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.

### `test_delete_driver_logs`

**Описание**: Тестирует метод `delete_driver_logs` класса `DriverBase`. Проверяет, что метод удаляет файлы из каталога логов.

**Параметры**:
- `driver_base` (`DriverBase`): Фикстура, предоставляющая экземпляр `DriverBase`.