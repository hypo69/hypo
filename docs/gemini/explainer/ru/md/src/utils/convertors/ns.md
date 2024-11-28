# Модуль `hypotez/src/utils/convertors/ns.py`

Этот модуль предоставляет функции для конвертации объектов `SimpleNamespace` в различные форматы: `dict`, `JSON`, `CSV`, `XML` и `XLS`.

## Функции:

* **`ns2dict(ns_obj: SimpleNamespace) -> dict`**:
    Преобразует объект `SimpleNamespace` в словарь.

    * **Аргументы:**
        * `ns_obj`: Объект `SimpleNamespace`, который необходимо преобразовать.

    * **Возвращает:**
        * Словарь, представляющий содержимое объекта `SimpleNamespace`.

* **`ns2json(ns_obj: SimpleNamespace, json_file_path: str | Path = None) -> str | bool`**:
    Преобразует объект `SimpleNamespace` в формат JSON.

    * **Аргументы:**
        * `ns_obj`: Объект `SimpleNamespace`, который необходимо преобразовать.
        * `json_file_path` (необязательный): Путь к файлу, в который необходимо сохранить JSON-строку. Если не указан, функция возвращает JSON-строку.

    * **Возвращает:**
        * JSON-строку, если путь к файлу не указан.
        * `True`, если JSON-данные успешно сохранены в указанный файл.
        * Возможна ошибка `Exception`, которая обрабатывается с помощью `logger.error()`.

* **`ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool`**:
    Преобразует объект `SimpleNamespace` в формат CSV.

    * **Аргументы:**
        * `ns_obj`: Объект `SimpleNamespace`, который необходимо преобразовать.
        * `csv_file_path`: Путь к файлу, в который необходимо сохранить CSV-данные.

    * **Возвращает:**
        * `True`, если CSV-данные успешно сохранены в указанный файл.
        * Возможна ошибка `Exception`, которая обрабатывается с помощью `logger.error()`.

* **`ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str`**:
    Преобразует объект `SimpleNamespace` в формат XML.

    * **Аргументы:**
        * `ns_obj`: Объект `SimpleNamespace`, который необходимо преобразовать.
        * `root_tag` (необязательный): Имя корневого тега XML. По умолчанию "root".

    * **Возвращает:**
        * XML-строку, представляющую содержимое объекта.
        * Возможна ошибка `Exception`, которая обрабатывается с помощью `logger.error()`.


* **`ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool`**:
    Преобразует объект `SimpleNamespace` в формат XLS (Excel).

    * **Аргументы:**
        * `data`: Объект `SimpleNamespace` для преобразования.
        * `xls_file_path`: Путь к файлу, в который необходимо сохранить XLS-данные.

    * **Возвращает:**
        * `True`, если XLS-данные успешно сохранены в указанный файл.
        * Возможна ошибка `Exception`, которая обрабатывается с помощью `logger.error()`.

**Обратите внимание:** Функции `ns2csv` и `ns2xls` полагаются на функции `save_csv_file` и `save_xls_file` из других модулей (`src.utils.csv` и `src.utils.xls`).  Функция `ns2xml` использует функцию `xml2dict` из `src.utils.convertors`. Важно, чтобы эти зависимости были доступны.  Также, присутствует `logger`, что предполагает использование  модуля для логирования ошибок.