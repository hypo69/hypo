# Модуль hypotez/src/webdriver/_pytest/test_driver.py

## Обзор

Этот модуль содержит тесты для класса `DriverBase`, предназначенные для проверки корректной работы его методов. Тесты используют фреймворк `pytest` и `unittest.mock` для имитации зависимостей и изоляции тестируемого кода.


## Фикстуры

### `driver_base`

**Описание**: Фикстура для создания экземпляра класса `DriverBase` для тестирования.

**Возвращает**: Экземпляр класса `DriverBase`.


## Тесты

### `test_driver_payload`

**Описание**: Тест метода `driver_payload`.  Проверяет, что метод корректно вызывает соответствующие методы `JavaScript` и `ExecuteLocator`.

**Используемые моки**:
- `src.webdriver.javascript.js.JavaScript`:  Мок объекта `JavaScript`.
- `src.webdriver.executor.ExecuteLocator`: Мок объекта `ExecuteLocator`.

**Проверяемые утверждения**:
- Проверка корректного вызова методов mock-объектов.

### `test_scroll`

**Описание**: Тест метода `scroll`. Проверяет корректное выполнение скроллинга вверх, вниз и в обоих направлениях.

**Используемые моки**:
- `driver_base.execute_script`: Мок метода `execute_script`.
- `driver_base.wait`: Мок метода `wait`.


**Проверяемые утверждения**:
- Проверка корректных вызовов `execute_script` с правильными параметрами (сдвиг вверх и вниз).


### `test_locale`

**Описание**: Тест свойства `locale`. Проверяет получение языка страницы из мета-тега или с помощью `get_page_lang` при ошибке.

**Используемые моки**:
- `driver_base.find_element`: Мок метода `find_element`.


**Проверяемые утверждения**:
- Проверка корректного получения значения `locale` из мета-тега.
- Проверка корректного возврата значения `locale` из `get_page_lang` при отсутствии мета-тега.



### `test_get_url`

**Описание**: Тест метода `get_url`. Проверяет корректную смену URL и сохранение куки.

**Используемые моки**:
- `driver_base.get`: Мок метода `get`.
- `driver_base.ready_state`: Мок свойства `ready_state`.
- `driver_base.wait`: Мок метода `wait`.
- `driver_base._save_cookies_localy`: Мок метода `_save_cookies_localy`.


**Проверяемые утверждения**:
- Проверка корректного вызова `driver.get` с новым URL.
- Проверка корректного сохранения предыдущего URL.
- Проверка корректного вызова `_save_cookies_localy`.


### `test_extract_domain`

**Описание**: Тест метода `extract_domain`. Проверка корректного извлечения домена из URL.

**Проверяемые утверждения**:
- Проверка корректного извлечения домена из различных URL.


### `test_save_cookies_localy`

**Описание**: Тест метода `_save_cookies_localy`. Проверка сохранения куки в файл.

**Используемые моки**:
- `driver_base.get_cookies`: Мок метода `get_cookies`.
- `builtins.open`: Мок функции `open`.
- `pickle.dump`: Мок функции `dump`.
- `pathlib.Path`: Мок объекта Path


**Проверяемые утверждения**:
- Проверка корректного вызова `open` для записи куки в файл.
- Проверка корректного вызова `pickle.dump` для сериализации куки.


### `test_page_refresh`

**Описание**: Тест метода `page_refresh`. Проверка корректной перезагрузки страницы.

**Используемые моки**:
- `driver_base.current_url`: Mock текущего URL.
- `driver_base.get_url`: Мок метода `get_url`.

**Проверяемые утверждения**:
- Проверка корректного вызова `get_url` с текущим URL.


### `test_wait`

**Описание**: Тест метода `wait`. Проверка корректной работы ожидания.

**Используемые моки**:
- `time.sleep`: Mock функции `sleep`.

**Проверяемые утверждения**:
- Проверка корректного вызова `time.sleep` с заданным временем ожидания.


### `test_delete_driver_logs`

**Описание**: Тест метода `delete_driver_logs`. Проверка корректного удаления логов.

**Используемые моки**:
- `pathlib.Path.iterdir`: Мок метода `iterdir` для получения списка файлов.
- `pathlib.Path.is_file`: Мок метода `is_file`.
- `pathlib.Path.unlink`: Мок метода `unlink` для удаления файлов.
- `pathlib.Path.is_dir`: Мок метода `is_dir` для проверки существования папки.

**Проверяемые утверждения**:
- Проверка корректного удаления файлов логов в заданной папке.