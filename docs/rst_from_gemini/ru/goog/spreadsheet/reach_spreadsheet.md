```markdown
# reach_spreadsheet.py - Модуль для работы с Google Spreadsheets API

Этот модуль предоставляет класс `ReachSpreadsheet` для взаимодействия с Google Spreadsheets API v4. Он упрощает создание, редактирование и совместное использование электронных таблиц.

**Установка:**

* Установите необходимые библиотеки:

```bash
pip install googleapiclient oauth2client httplib2
```


**Использование:**

```python
from hypotez.src.goog.spreadsheet.reach_spreadsheet import ReachSpreadsheet
from hypotez.src.utils import htmlColorToJSON  # Не забудьте импортировать эту функцию

# ... (ваш код) ...

# Создание экземпляра класса
ss = ReachSpreadsheet(debugMode=True)  # debugMode=True для отладки

# Создание новой электронной таблицы
try:
    ss.create("Название таблицы", "Название листа", rows=10, cols=5, locale="ru-RU", timeZone="Europe/Moscow")
    # ... (дополнительные операции) ...

    # Обновление таблицы
    ss.prepare_setValues("A1:B2", [["Значение 1", "Значение 2"], ["Значение 3", "Значение 4"]])
    ss.runPrepared()


    #Совместное использование
    ss.shareWithAnybodyForReading()
    print(ss.getSheetURL())

except Exception as e:
    print(f"Ошибка: {e}")
```


**Описание основных методов:**

* **`__init__(self, debugMode=False)`:** Инициализирует соединение с API Google Sheets.  **Важно!**  Убедитесь, что файл ключей `e-cat-346312-137284f4419e.json` расположен в правильной папке. Это файл с ключами сервисного аккаунта, который необходим для доступа к API.
* **`create(self, title, sheetTitle, rows=1000, cols=26, locale='en-US', timeZone='Etc/GMT')`:** Создает новую электронную таблицу с заданными свойствами.
* **`share(self, shareRequestBody)`:** Делит электронную таблицу.
* **`shareWithEmailForReading(self, email)`:** Делит таблицу для чтения по указанному email.
* **`shareWithEmailForWriting(self, email)`:** Делит таблицу для записи по указанному email.
* **`shareWithAnybodyForReading(self)`:** Делит таблицу для чтения всем.
* **`shareWithAnybodyForWriting(self)`:** Делит таблицу для записи всем.
* **`getSheetURL(self)`:** Возвращает URL электронной таблицы.
* **`setSpreadsheetById(self, spreadsheetId)`:** Устанавливает текущую электронную таблицу по её идентификатору.
* **`runPrepared(self, valueInputOption='USER_ENTERED')`:** Выполняет подготовленные операции (добавление листов, изменение размеров, заполнение ячеек).
* **`prepare_addSheet(self, sheetTitle, rows=1000, cols=26)`:** Подготавливает запрос на добавление нового листа.
* **`addSheet(self, sheetTitle, rows=1000, cols=26)`:** Добавляет новый лист и устанавливает его как текущий.
* **`toGridRange(self, cellsRange)`:** Преобразует строковый диапазон ячеек в словарь `GridRange`.
* **`prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`:** Подготавливает запрос на изменение размера столбца или строки.
* **`prepare_setColumnWidth(self, col, width)`:**  Устанавливает ширину столбца.
* **`prepare_setRowsHeight(self, startRow, endRow, height)`:** Устанавливает высоту строки(строк).
* **`prepare_setValues(self, cellsRange, values, majorDimension='ROWS')`:** Подготавливает запрос на заполнение ячеек значениями.
* **`prepare_mergeCells(self, cellsRange, mergeType='MERGE_ALL')`:** Подготавливает запрос на объединение ячеек.
* **`prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields='userEnteredFormat')`:** Подготавливает запрос на форматирование ячеек.
* **`prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields='userEnteredFormat')`:** Подготавливает запрос на форматирование нескольких ячеек (лучше использовать для многострочного форматирования).


**Обработка ошибок:**

Модуль содержит классы исключений `SpreadsheetError`, `SpreadsheetNotSetError`, `SheetNotSetError`, которые помогут в отслеживании и обработке ошибок.

**Тесты:**

В коде модуля есть несколько тестовых функций (`testCreateSpreadsheet`, `testSetSpreadsheet`, etc.), которые демонстрируют использование методов класса.


**Важные замечания:**

* **Ключи сервисного аккаунта:**  Файл ключей (`e-cat-346312-137284f4419e.json`) **необходимо сохранить** в правильном месте, чтобы код мог получить к нему доступ.
* **Безопасность:**  Храните секретные ключи безопасно.
* **`debugMode`:** Флаг `debugMode` может быть полезен для отладки, но не следует оставлять его `True` в продакшене.
* **Документация:** Включите комментарии внутри методов, если в этом есть необходимость.
* **Логирование:** Модуль использует `logger` для записи сообщений об ошибках. Это существенно улучшает дебаггинг и отладку.

Этот улучшенный документ предоставляет более полное описание модуля и его возможностей.
```