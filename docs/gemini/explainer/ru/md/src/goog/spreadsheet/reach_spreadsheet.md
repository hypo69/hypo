# Spreadsheet API Wrapper (hypotez/src/goog/spreadsheet/reach_spreadsheet.py)

Этот файл содержит класс `ReachSpreadsheet`, предназначенный для работы с Google Spreadsheets API v4.  Он предоставляет методы для создания, редактирования, заполнения и совместного использования таблиц.

**Ключевые особенности:**

* **Авторизация:** Использует `ServiceAccountCredentials` для доступа к Google Sheets API, что избавляет от необходимости ручного ввода API ключей.  Использует файл ключей `e-cat-346312-137284f4419e.json`, предполагая, что он находится в временной папке.  Важно отметить, что `gs.path.tmp` указывает на временную директорию, которая должна быть инициализирована.
* **Совместное использование:** Предоставляет методы для совместного использования таблицы с определенными пользователями (по email) и для общего доступа.
* **Методы для работы с листами:**  `create()`, `addSheet()`, `setSpreadsheetById()`, `getSheetURL()` для создания, добавления листов, установки текущей таблицы и получения ссылки на неё.
* **Форматирование:** Поддержка сложного форматирования ячеек и строк, включая:
    * Задание ширины колонок и высоты строк (`prepare_setColumnWidth()`, `prepare_setColumnsWidth()`, `prepare_setRowHeight()`, `prepare_setRowsHeight()`).
    * Заполнение ячеек данными (`prepare_setValues()`).
    * Объединение ячеек (`prepare_mergeCells()`).
    * Применение форматирования текста, выравнивания, цвета ячеек (`prepare_setCellStringFormatterormat()`, `prepare_setCellStringFormatterormats()`).
    * Установка границ ячеек (`testPureBlackBorder()`).
* **Подготовка запросов:** Запросы к API не выполняются непосредственно, а сначала собираются в `self.requests` и `self.valueRanges`.  Это позволяет выполнить несколько операций в одном запросе, что повышает эффективность.
* **Обработка ошибок:** Классы `SpreadsheetError`, `SpreadsheetNotSetError`, `SheetNotSetError` используются для обработки ошибок.
* **Отладка:** Метод `debugMode` позволяет выводить подробные данные о результатах запросов к API (например, `pprint(spreadsheet)`).


**Основные методы:**

* `__init__(self, debugMode=False)`: Инициализация класса, создание credentials.
* `create(self, title, sheetTitle, rows, cols, locale, timeZone)`: Создание новой таблицы.
* `share(self, shareRequestBody)`: Совместное использование таблицы.
* `shareWithEmailForReading(self, email)`: Совместное использование с правами чтения.
* `shareWithEmailForWriting(self, email)`: Совместное использование с правами записи.
* `getSheetURL(self)`: Получение URL таблицы.
* `setSpreadsheetById(self, spreadsheetId)`: Установка текущей таблицы по её ID.
* `runPrepared(self, valueInputOption="USER_ENTERED")`: Выполнение подготовленных запросов.
* `prepare_addSheet(self, sheetTitle, rows, cols)`: Подготовка запроса на добавление нового листа.
* `addSheet(self, sheetTitle, rows, cols)`: Добавление листа.
* `toGridRange(self, cellsRange)`: Преобразование строки диапазона ячеек в словарь.
* `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`: Подготовка запроса для установки размеров.
* `prepare_setColumnsWidth(self, startCol, endCol, width)`: Подготовка запроса для установки ширины колонок.
* ... (другие методы для форматирования и добавления данных).


**Важно:**

* Код предполагает существование модулей `header`, `gs`, `src`, `j_loads`, `j_dumps`, `pprint`, `logger` из других частей проекта.
* Для корректной работы необходимы установленные библиотеки `httplib2`, `googleapiclient`, `oauth2client`.
* Файл ключей (`e-cat-346312-137284f4419e.json`) должен быть доступен.


**Примеры использования** показаны в тестовых функциях (например, `testCreateSpreadsheet`, `testCreateTimeManagementReport`).  Эти функции демонстрируют, как использовать методы класса для создания, форматирования и заполнения таблиц.  Они также демонстрируют потенциальные ошибки и способы их обработки.


Этот код представляет собой утилиту для работы с Google Spreadsheets API. Он не предназначен для использования в больших проектах без необходимых проверок и улучшений.