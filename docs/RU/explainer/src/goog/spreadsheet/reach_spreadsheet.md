# <input code>

```python
## \file hypotez/src/goog/spreadsheet/reach_spreadsheet.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet 
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
        self.debugMode = debugMode
        # ... (rest of the code)
```

# <algorithm>

**Описание алгоритма:**

1. **Инициализация (`__init__`)**:
    * Принимает `debugMode` (флаг отладки).
    * Пытается загрузить credentials из временного файла (`jsonKeyFileName`).
    * Создает `credentials` с помощью `ServiceAccountCredentials`.
    * Авторизует `httpAuth` с помощью `credentials`.
    * Создает объекты `service` (для Google Sheets) и `driveService` (для Google Drive) с использованием авторизованного `httpAuth`.
    * Инициализирует `spreadsheetId`, `sheetId`, `sheetTitle`, `requests` и `valueRanges`.

2. **Создание нового листа (`create`)**:
    * Создает новый лист в Google Таблицах с заданными параметрами (название, количество строк/столбцов, локаль, часовой пояс).
    * Возвращает данные о созданном листе.
    * Сохраняет `spreadsheetId`, `sheetId` и `sheetTitle` в объекте.

3. **Разделение доступа (`share`)**:
    * Проверяет, установлены ли `spreadsheetId`.
    * Если да, то отправляет запрос на разделение доступа к листу с помощью `driveService`.
    * Обновляет `driveService` (возможно, если он был равен None)

4. **Делегирование доступа (`shareWithEmailForReading`, `shareWithEmailForWriting`...):**
    * Вызывают `share` с предварительно заданным телом запроса, который позволяет указать тип пользователя (`user` или `anyone`), роль (`reader` или `writer`) и электронный адрес.

5. **Получение ссылки на лист (`getSheetURL`)**:
    * Проверяет, установлены ли `spreadsheetId` и `sheetId`.
    * Возвращает ссылку на лист в Google Таблицах.

6. **Установка листа по ID (`setSpreadsheetById`)**:
    * Получает данные о листе с заданным ID.
    * Сохраняет `spreadsheetId`, `sheetId` и `sheetTitle` в объекте.

7. **Выполнение подготовленных запросов (`runPrepared`)**:
    * Выполняет подготовленные запросы (batchUpdate) для Google Sheets.
    * Сначала обрабатывает запросы `requests`, затем запросы `valueRanges`.
    * Очищает `requests` и `valueRanges` после выполнения.
    * Возвращает результаты выполнения запросов.

8. **Подготовка запросов на добавление листа (`prepare_addSheet`)**:
    * Добавляет запрос на добавление листа в список `requests`.


9. **Добавление нового листа (`addSheet`)**:
    * Готовит запрос на добавление листа (используя `prepare_addSheet`).
    * Выполняет запрос и получает id добавленного листа.
    * Обновляет `sheetId` и `sheetTitle`.
    * Возвращает `sheetId`.

10. **Преобразование диапазона ячеек в GridRange (`toGridRange`)**:
    * Преобразует строковый диапазон ячеек (например, "A1:B2") в структурированную форму для Google Sheets API.
    * Возвращает объект `GridRange`.

11. **Подготовка запросов на изменение размеров (`prepare_setDimensionPixelSize`, `prepare_setColumnWidth`, `prepare_setRowHeight`)**:
    * Готовит запросы на изменение размеров столбцов и строк.
    * Добавляет запросы в список `requests`.

12. **Подготовка запросов на заполнение значений (`prepare_setValues`)**:
    * Подготавливает запросы на заполнение значений в ячейках.
    * Добавляет запросы в `valueRanges`.


13. **Подготовка запросов на слияние ячеек (`prepare_mergeCells`)**:
    * Подготавливает запрос на слияние ячеек.
    * Добавляет запрос в `requests`.

14. **Подготовка запросов на форматирование ячеек (`prepare_setCellStringFormatterormat`, `prepare_setCellStringFormatterormats`)**:
    * Подготавливает запросы на форматирование ячеек (текст, шрифт, выравнивание, цвет фона).
    * Добавляет запросы в `requests` или `valueRanges`.

**Примеры:**
* `create()`: Создание нового листа с названием "Мой лист" и размерами 10 строк на 5 столбцов.
* `addSheet()`: Добавление нового листа "Дополнительно" в существующую таблицу.
* `prepare_setColumnWidth()`: Установка ширины столбца A в 200 пикселей.

# <mermaid>

```mermaid
graph LR
    A[ReachSpreadsheet] --> B{__init__};
    B --> C[Загрузка credentials];
    C --> D[Создание service & driveService];
    D --> E[Инициализация свойств];
    E --> F[Подготовка запросов];
    F --> G[Выполнение запросов (runPrepared)];
    G --> H[Обработка ответов];
    
    subgraph "Создание листа (create)"
        A --> I[create];
        I --> J[Запрос на создание];
        J --> K[Получение ID листа];
        K --> E;
    end
    subgraph "Добавление листа (addSheet)"
        A --> L[addSheet];
        L --> M[prepare_addSheet];
        M --> F;
        F --> O[runPrepared];
        O --> P[Получение ID добавленного листа];
        P --> E;
    end
    subgraph "Форматирование (prepare...)"
        A --> N[prepare_setColumnWidth];
        N --> F;
        A --> Q[prepare_setValues];
        Q --> F;
        A --> R[prepare_setCellStringFormatterormat];
        R --> F;
    end
    subgraph "Разделение доступа (share...)"
        A --> S[shareWithEmailForReading];
        S --> T[share];
        T --> U[Отправка запроса на разделение доступа];
    end
```

# <explanation>

**Импорты:**

* `httplib2`, `googleapiclient.discovery`, `googleapiclient.errors`: из пакета `googleapiclient`, необходимы для работы с Google API. Связь через пакет `googleapiclient`.
* `ServiceAccountCredentials`: из `oauth2client.service_account`, для авторизации приложения с помощью сервисного аккаунта. Связь через пакет `oauth2client`.
* `tempfile`: для работы с временными файлами.
* `header`: скорее всего, файл для заголовков, используемый в рамках проекта.
* `gs`: из `src.gs`, скорее всего, содержит константы или функции, связанные с Google Storage.
* `j_loads_ns`, `j_dumps`: из `src.utils.jjson`, функции для работы с JSON.
* `pprint`: из `src.utils.printer`, функция для красивого вывода данных.
* `logger`: из `src.logger`, для логирования событий.

**Классы:**

* `SpreadsheetError`, `SpreadsheetNotSetError`, `SheetNotSetError`: исключения для обработки ошибок, связанных с управлением листами.  Создают иерархию ошибок.
* `ReachSpreadsheet`: основной класс для работы с Google Sheets.
    * `debugMode`: флаг отладки.
    * `credentials`: хранит данные для авторизации.
    * `httpAuth`: авторизованный объект `httplib2.Http()`.
    * `service`: объект для работы с Google Sheets API.
    * `driveService`: объект для работы с Google Drive API.
    * `spreadsheetId`, `sheetId`, `sheetTitle`: свойства, хранящие ID и название текущей таблицы и листа.
    * `requests`, `valueRanges`: списки запросов для последующей пакетной обработки.  Используются для повышения производительности.

**Функции:**

* `htmlColorToJSON`: преобразует HTML цвет в JSON-представление.
* `create()`: создает новый лист.
* `share()`: разделяет доступ к листу.
* `getSheetURL()`: возвращает URL листа.
* `setSpreadsheetById()`: устанавливает текущую таблицу по ее ID.
* `runPrepared()`: выполняет пакетные запросы на обновление.
* `prepare_addSheet()`: подготавливает запрос на добавление листа.
* `addSheet()`: добавляет новый лист и обновляет свойства.
* `toGridRange()`: преобразует строковый диапазон в `GridRange`.
* `prepare_setDimensionPixelSize()`, `prepare_setColumnWidth()`, `prepare_setRowHeight()`, `prepare_setColumnsWidth()`, `prepare_setRowsHeight()`: подготавливают запросы на изменение размеров.
* `prepare_setValues()`: подготавливает запросы на установку значений.
* `prepare_mergeCells()`: подготавливает запросы на слияние ячеек.
* `prepare_setCellStringFormatterormat()`, `prepare_setCellStringFormatterormats()`: подготавливает запросы на форматирование ячеек.


**Переменные:**

* `MODE`: константа, указывающая режим работы (например, 'dev' или 'prod').
* `jsonKeyFileName`: путь к файлу с закрытым ключом.

**Возможные ошибки и улучшения:**

* Недостаточное тестирование.
* Отсутствие обработки особых случаев.
* Отсутствие документации к методам.
* Возможно, стоит использовать менеджер контекста для `httpAuth` и `service`, чтобы избежать утечек ресурсов.
* Проверка на корректность входных данных (например, в `toGridRange()` и других методах).
* Добавить валидацию типов для входных параметров, чтобы предотвратить ошибки.
* Улучшить обработку ошибок (более подробные сообщения об ошибках).

**Взаимосвязи с другими частями проекта:**

* `gs`: используется для доступа к путям или константам.
* `src.utils.jjson`: для работы с JSON данными.
* `src.utils.printer`: для красивого вывода.
* `src.logger`: для логирования.

Этот код является фрагментом и для полной оценки нужно посмотреть другие связанные файлы.