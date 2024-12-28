# <input code>

```python
## \file hypotez/src/goog/spreadsheet/reach_spreadsheet.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.goog.spreadsheet 
	:platform: Windows, Unix
	:synopsis:

"""



# Author: Ioann Volkov (volkov.ioann@gmail.com)
# This module uses Google Sheets API v4 (and Google Drive API v3 for sharing spreadsheets)

# (!) Disclaimer
# This is NOT a full-functional wrapper over Sheets API v4.
# This module was created just for https://telegram.me/TimeManagementBot and habrahabr article


import httplib2
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.service_account import ServiceAccountCredentials

import tempfile
import header
from src import gs
from src.utils.jjson import j_loads_ns,j_dumps
from src.utils.printer import pprint
from src.logger import logger

def htmlColorToJSON(htmlColor):
    if htmlColor.startswith("#"):
        htmlColor = htmlColor[1:]
    return {"red": int(htmlColor[0:2], 16) / 255.0, "green": int(htmlColor[2:4], 16) / 255.0, "blue": int(htmlColor[4:6], 16) / 255.0}

class SpreadsheetError(Exception):
    ...

class SpreadsheetNotSetError(SpreadsheetError):
    ...

class SheetNotSetError(SpreadsheetError):
    ...

class ReachSpreadsheet:
    def __init__(self, debugMode = False):
        # ... (Initialization logic)
        
    # Creates new spreadsheet
    def create(self, title, sheetTitle, rows = 1000, cols = 26, locale = 'en-US', timeZone = 'Etc/GMT'):
        # ... (Spreadsheet creation logic)

    def share(self, shareRequestBody):
        # ... (Spreadsheet sharing logic)

    def shareWithEmailForReading(self, email):
        # ... (Share for reading logic)

    def shareWithEmailForWriting(self, email):
        # ... (Share for writing logic)
        
    # ... (Other methods)
```

# <algorithm>

**Описание алгоритма работы кода**

Класс `ReachSpreadsheet` предназначен для работы с Google Таблицами через API.

1. **`__init__`:** Инициализирует соединение с Google Sheets API и Google Drive API. Загружает ключи доступа из файла `e-cat-346312-137284f4419e.json`.  Пример:  `self.credentials = ServiceAccountCredentials.from_json_keyfile_name('e-cat-346312-137284f4419e.json', ['https://www.googleapis.com/auth/spreadsheets'])`

2. **`create`:** Создаёт новую таблицу в Google Таблицах. Принимает на вход название таблицы, название листа, размеры и локаль. Пример вызова: `ss.create("Моя таблица", "Лист1", rows=500, cols=10)`

3. **`share`:** Общий доступ к таблице. Принимает запрос для общего доступа.

4. **`shareWithEmailForReading/Writing`:** Устанавливает уровень доступа чтения или записи для конкретного email-адреса.

5. **`getSheetURL`:** Возвращает URL для доступа к таблице в Google Таблицах.

6. **`setSpreadsheetById`:** Устанавливает текущую таблицу по её идентификатору.

7. **`runPrepared`:** Выполняет подготовленные запросы обновления таблицы (batchUpdate). Разделяет запросы по типам, чтобы оптимизировать работу.

8. **`prepare_addSheet`:** Подготавливает запрос на добавление листа.

9. **`addSheet`:** Добавляет новый лист к текущей таблице и возвращает его идентификатор.

10. **`toGridRange`:** Преобразует строковое представление диапазона ячеек в словарь, описывающий этот диапазон.

11. **`prepare_setDimensionPixelSize`:** Подготавливает запрос на изменение размера ячеек (ширина столбцов, высота строк).

12. **`prepare_setColumnsWidth/prepare_setColumnWidth/prepare_setRowsHeight/prepare_setRowHeight`:** Подготавливают запросы на изменение ширины столбцов и высоты строк.

13. **`prepare_setValues`:** Подготавливает запрос на заполнение ячеек данными.

14. **`prepare_mergeCells`:** Подготавливает запрос на слияние ячеек.

15. **`prepare_setCellStringFormatterormat/prepare_setCellStringFormatterormats`:** Подготавливают запрос на форматирование ячеек.


**Пример данных между функциями:**

`ReachSpreadsheet` получает данные из конструктора `__init__` (ключ доступа, httpAuth). Далее данные используются в методах `create`, `share`, `addSheet`, `runPrepared`.
В `runPrepared` обрабатываются `requests` и `valueRanges`


# <mermaid>

```mermaid
graph LR
    A[ReachSpreadsheet] --> B(init);
    B --> C{Load Credentials};
    C -- Success --> D[Authorize http];
    C -- Failure --> E[Error Handling];
    D --> F[Build Sheets Service];
    D --> G[Build Drive Service];
    F --> H[create];
    H --> I[Execute Spreadsheet Creation];
    I --> J{Spreadsheet ID};
    J --> K[Store Spreadsheet ID];
    K --> L(share);
    L --> M[Execute Share Request];
    ...
    A --> N(addSheet);
    N --> O[prepare_addSheet];
    O --> P[Append Request];
    P --> Q[runPrepared];
    Q --> R[Execute Batch Update];
    R --> S[Update Spreadsheet];
    
    subgraph "External Dependencies"
        F -->|Google Sheets API| Google Sheets;
        G -->|Google Drive API| Google Drive;
    end
```

**Объяснение зависимостей**:

* `httplib2`:  Библиотека для работы с HTTP протоколом.
* `googleapiclient`: Библиотека для работы с Google API.
* `oauth2client`: Библиотека для аутентификации с Google API.
* `tempfile`:  Модуль для работы с временными файлами.
* `header`, `gs`, `jjson`, `printer`, `logger`:  Локальные модули, скорее всего, части проекта, которые содержат вспомогательные функции и классы, например, для работы с файловой системой, обработки JSON, вывода сообщений, логирования.  Эти зависимости, скорее всего, находятся в директориях `src` и `src/utils`.


# <explanation>

**Импорты**:

Код импортирует необходимые библиотеки для работы с Google Sheets API: `httplib2`, `googleapiclient`, `oauth2client`.  Также импортируются модули для работы с временными файлами,  и локальные модули проекта (`header`, `gs`, `jjson`, `printer`, `logger`) которые обеспечивают дополнительные функции, такие как логирование и работу с файлами.

**Классы**:

* **`SpreadsheetError`**: Базовый класс для ошибок, связанных с таблицей.
* **`SpreadsheetNotSetError`**: Ошибка, если таблица не задана.
* **`SheetNotSetError`**: Ошибка, если лист не задан.
* **`ReachSpreadsheet`**: Класс для работы с Google Таблицами. Он содержит атрибуты:
    * `debugMode`: Флаг для включения отладочного режима.
    * `credentials`: Объект аутентификации, полученный от `ServiceAccountCredentials`.
    * `httpAuth`: Авторизованный http-клиент.
    * `service`: Объект для работы с Google Sheets API.
    * `driveService`: Объект для работы с Google Drive API (для общего доступа).
    * `spreadsheetId`, `sheetId`, `sheetTitle`: Идентификаторы и название таблицы и листа.
    * `requests`: Список запросов для `batchUpdate`.
    * `valueRanges`: Список диапазонов ячеек с данными для `values.batchUpdate`.
    Методы класса `ReachSpreadsheet` реализуют создание, добавление листов, форматирование и получение данных из Google таблиц, а так же общие методы для работы с Google Drive.


**Функции**:

* **`htmlColorToJSON`**: Преобразует строковое представление HTML цвета в JSON-представление.
* **`test*`-функции**: Тестовые функции для проверки работы класса `ReachSpreadsheet`.  Они создают экземпляры класса, выполняют действия и сравнивают результаты.

**Переменные**:

Переменные `MODE`, `GOOGLE_CREDENTIALS_FILE`, `scopes` и другие содержат константы и переменные, используемые для настройки и выполнения тестов.

**Возможные ошибки и улучшения**:

* **Обработка ошибок:**  Код содержит `try...except` блоки для обработки возможных ошибок при создании `credentials`, но обработка ошибок при работе с Google API может быть улучшена.  Необходимо добавить более подробную обработку ошибок Google API (например, `googleapiclient.errors.HttpError`).
* **Избыточность:** Необходимо пересмотреть наличие повторяющихся операций или функций (например, `create`, `share` в разных формах).
* **Документация:** Добавить подробную документацию к методам, объясняя их назначение, аргументы и возвращаемые значения.
* **Рефакторинг:**  Разделить на модули логику работы с запросами (`prepare_*`) и их выполнением (`runPrepared`).
* **Использование `dataclasses`**: Для хранения данных диапазона ячеек можно использовать dataclasses, это упростит структурирование данных.
* **Вместо `pprint`**: Используйте `logging` для более управляемого вывода в лог.

**Взаимосвязь с другими частями проекта**:

Код использует локальные модули проекта (`gs`, `jjson`, `printer`, `logger`), что указывает на его интеграцию в существующую инфраструктуру.  Неясно, какие именно части проекта взаимодействуют напрямую, но предполагается связь с системными функциями проекта.  Модули `src.utils` и `src` вероятно содержат вспомогательные классы и методы.