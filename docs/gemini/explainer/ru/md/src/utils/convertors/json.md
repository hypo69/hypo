# Модуль `hypotez/src/utils/convertors/json.py`

Этот модуль предоставляет функции для преобразования данных в формате JSON в различные форматы: CSV, SimpleNamespace, XML и XLS.

**Функции:**

* **`json2csv(json_data, csv_file_path)`:** Преобразует данные в формате JSON в CSV с разделителем запятая.
* **`json2ns(json_data)`:** Преобразует данные в формате JSON в объект `SimpleNamespace`.
* **`json2xml(json_data, root_tag="root")`:** Преобразует данные в формате JSON в XML.
* **`json2xls(json_data, xls_file_path)`:** Преобразует данные в формате JSON в XLS формат.

**Описание функций:**

**`json2csv`:**

* **`json_data`:** Данные в формате JSON (строка, список словарей, путь к файлу JSON или словарь).
* **`csv_file_path`:** Путь к файлу CSV, куда будут записаны данные.
* **Возвращает:** `True`, если преобразование прошло успешно, `False` в противном случае.
* **Возможные исключения:** `ValueError` (если тип `json_data` не поддерживается), `Exception` (если возникла ошибка при парсинге JSON или записи CSV).
* **Логика:** Функция загружает JSON данные и сохраняет их в CSV файл с использованием функции `save_csv_file` из модуля `src.utils.csv`.

**`json2ns`:**

* **`json_data`:** Данные в формате JSON (строка, словарь, путь к файлу JSON).
* **Возвращает:** Объект `SimpleNamespace`, содержащий данные.
* **Возможные исключения:** `ValueError` (если тип `json_data` не поддерживается), `Exception` (если возникла ошибка при парсинге JSON).
* **Логика:** Функция загружает JSON данные и преобразует их в объект `SimpleNamespace` с использованием оператора `**`.

**`json2xml`:**

* **`json_data`:** Данные в формате JSON (строка, словарь, путь к файлу JSON).
* **`root_tag` (по умолчанию "root"):** Имя тега корня XML.
* **Возвращает:** Строку XML.
* **Возможные исключения:** `ValueError` (если тип `json_data` не поддерживается), `Exception` (если возникла ошибка при парсинге JSON или преобразовании в XML).
* **Логика:** Функция использует функцию `dict2xml` из модуля `src.utils.convertors.dict` для преобразования JSON в XML.

**`json2xls`:**

* **`json_data`:** Данные в формате JSON (строка, список словарей, путь к файлу JSON или словарь).
* **`xls_file_path`:** Путь к файлу XLS, куда будут записаны данные.
* **Возвращает:** `True`, если преобразование прошло успешно, `False` в противном случае.
* **Возможные исключения:** `ValueError` (если тип `json_data` не поддерживается), `Exception` (если возникла ошибка при парсинге JSON или записи XLS).
* **Логика:** Функция использует функцию `save_xls_file` из модуля `src.utils.xls` для сохранения данных в формате XLS.

**Зависимости:**

Модуль использует модули:
* `json`
* `csv`
* `types` (для `SimpleNamespace`)
* `pathlib`
* `typing`
* `src.utils.csv`
* `src.utils.jjson`
* `src.utils.xls`
* `src.utils.convertors.dict`
* `src.logger`

**Обработка ошибок:**

Все функции содержат обработку исключений, чтобы предотвратить сбой программы при некорректных данных или ошибках.  `logger` используется для логирования ошибок.


**Важные замечания:**

* Модуль `src.utils.xls` и `src.utils.csv` должны быть определены и содержать функции `save_xls_file` и `save_csv_file`.
* Модуль `src.utils.convertors.dict` должен содержать функцию `dict2xml`.
* Модуль `src.logger` должен быть импортирован и готов к использованию.
* Важно проверить корректность входных данных и пути к файлам, чтобы избежать ошибок.