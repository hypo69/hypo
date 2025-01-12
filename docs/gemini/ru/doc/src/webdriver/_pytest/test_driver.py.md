# Модуль `test_driver.py`

## Обзор

Этот модуль содержит тесты для класса `DriverBase` из `src.webdriver.driver`. Тесты проверяют корректность работы различных методов, таких как `driver_payload`, `scroll`, `locale`, `get_url`, `extract_domain`, `_save_cookies_localy`, `page_refresh`, `wait` и `delete_driver_logs`. Для проведения тестов используется `pytest` и `unittest.mock` для имитации объектов и их поведения.

## Оглавление

- [Класс `TestDriverBase`](#класс-testdriverbase)
    - [Метод `driver_base`](#метод-driver_base)
    - [Метод `test_driver_payload`](#метод-test_driver_payload)
    - [Метод `test_scroll`](#метод-test_scroll)
    - [Метод `test_locale`](#метод-test_locale)
    - [Метод `test_get_url`](#метод-test_get_url)
    - [Метод `test_extract_domain`](#метод-test_extract_domain)
    - [Метод `test_save_cookies_localy`](#метод-test_save_cookies_localy)
    - [Метод `test_page_refresh`](#метод-test_page_refresh)
    - [Метод `test_wait`](#метод-test_wait)
    - [Метод `test_delete_driver_logs`](#метод-test_delete_driver_logs)

## Классы

### `TestDriverBase`

**Описание**:
Класс, содержащий тестовые методы для проверки функциональности класса `DriverBase`.

**Методы**:
- [`driver_base`](#метод-driver_base)
- [`test_driver_payload`](#метод-test_driver_payload)
- [`test_scroll`](#метод-test_scroll)
- [`test_locale`](#метод-test_locale)
- [`test_get_url`](#метод-test_get_url)
- [`test_extract_domain`](#метод-test_extract_domain)
- [`test_save_cookies_localy`](#метод-test_save_cookies_localy)
- [`test_page_refresh`](#метод-test_page_refresh)
- [`test_wait`](#метод-test_wait)
- [`test_delete_driver_logs`](#метод-test_delete_driver_logs)

### Метод `driver_base`

**Описание**:
Фикстура для создания экземпляра `DriverBase` для тестирования.

**Возвращает**:
- `DriverBase`: Экземпляр класса `DriverBase`.

### Метод `test_driver_payload`

**Описание**:
Тестирует метод `driver_payload` класса `DriverBase`. Проверяет, что методы из `JavaScript` и `ExecuteLocator` присваиваются правильно.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_scroll`

**Описание**:
Тестирует метод `scroll` класса `DriverBase`. Проверяет корректность вызова `execute_script` для различных направлений скролла.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_locale`

**Описание**:
Тестирует свойство `locale` класса `DriverBase`. Проверяет, что локаль извлекается из метатега или из свойства `get_page_lang`.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_get_url`

**Описание**:
Тестирует метод `get_url` класса `DriverBase`. Проверяет корректность установки URL, сохранения куков и вызова метода `get`.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_extract_domain`

**Описание**:
Тестирует метод `extract_domain` класса `DriverBase`. Проверяет корректность извлечения домена из URL.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_save_cookies_localy`

**Описание**:
Тестирует метод `_save_cookies_localy` класса `DriverBase`. Проверяет корректность сохранения куков в файл.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_page_refresh`

**Описание**:
Тестирует метод `page_refresh` класса `DriverBase`. Проверяет корректность вызова `get_url` для обновления страницы.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_wait`

**Описание**:
Тестирует метод `wait` класса `DriverBase`. Проверяет корректность вызова `time.sleep`.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`

### Метод `test_delete_driver_logs`

**Описание**:
Тестирует метод `delete_driver_logs` класса `DriverBase`. Проверяет корректность удаления лог файлов из временной директории.

**Параметры**:
- `driver_base`: Экземпляр `DriverBase`, полученный через фикстуру.

**Возвращает**:
- `None`