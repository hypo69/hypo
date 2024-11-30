# Анализ кода ReachSpreadsheet.py

## <input code>

```python
# ... (код из файла)
```

## <algorithm>

Этот код реализует класс `ReachSpreadsheet` для работы с Google Sheets API v4. Алгоритм работы можно представить следующей блок-схемой:

**1. Инициализация (ReachSpreadsheet.__init__)**

*   Ввод: `debugMode` (флаг отладки).
*   Обработка:
    *   Определяется путь к файлу с ключами доступа (jsonKeyFileName).
    *   Попытка получить `credentials` из файла с ключами.
    *   Если ошибка, выводится сообщение об ошибке, и выполнение останавливается.
    *   Авторизует `httpAuth` с помощью `credentials`.
    *   Создает экземпляры `service` (для Google Sheets) и `driveService` (для Google Drive).
    *   Инициализирует `spreadsheetId`, `sheetId`, `sheetTitle`, `requests` и `valueRanges` как `None`, пустой список соответственно.
*   Вывод: Экземпляр класса `ReachSpreadsheet` с авторизованным доступом к Google Sheets API.

**2. Создание нового листа (ReachSpreadsheet.create)**

*   Ввод: `title`, `sheetTitle`, `rows`, `cols`, `locale`, `timeZone`.
*   Обработка:
    *   Вызов `service.spreadsheets().create()` для создания нового листа.
    *   Если `debugMode` включен, выводит информацию о созданном листе.
    *   Извлекает `spreadsheetId`, `sheetId` и `sheetTitle` из ответа API.
*   Вывод: Установленные `spreadsheetId`, `sheetId` и `sheetTitle` в объекте.

**3. Общий алгоритм для `share`, `shareWithEmailForReading`, `shareWithEmailForWriting` etc.**

*   Ввод: `shareRequestBody` (данные для прав доступа).
*   Обработка:
    *   Проверка наличия `spreadsheetId`. Если нет - ошибка.
    *   Если `driveService` не инициализирован, инициализирует его.
    *   Вызов `driveService.permissions().create()` для установки прав доступа.
    *   Если `debugMode` включен, выводит информацию о результате.
*   Вывод: Результат вызова `driveService.permissions().create()`.


**4. Загрузка листа по ID (ReachSpreadsheet.setSpreadsheetById)**

*   Ввод: `spreadsheetId`.
*   Обработка:
    *   Получение информации о листе по ID с помощью `service.spreadsheets().get()`.
    *   Если `debugMode` включен, выводит информацию о листе.
    *   Извлекает `spreadsheetId`, `sheetId` и `sheetTitle` из ответа API.
*   Вывод: Установленные `spreadsheetId`, `sheetId` и `sheetTitle` в объекте.


**5. Выполнение подготовленных запросов (ReachSpreadsheet.runPrepared)**

*   Ввод: `valueInputOption`.
*   Обработка:
    *   Проверка наличия `spreadsheetId`. Если нет - ошибка.
    *   Вызов `service.spreadsheets().batchUpdate()` для выполнения `requests`
    *   Вызов `service.spreadsheets().values().batchUpdate()` для выполнения `valueRanges`
    *   Очистка `requests` и `valueRanges` после выполнения запросов.
*   Вывод: Кортеж из `replies` и `responses` ответов API.


**6. Подготовка и добавление новых листов (ReachSpreadsheet.prepare_addSheet, ReachSpreadsheet.addSheet)**

*   Ввод: `sheetTitle`, `rows`, `cols`.
*   Обработка:
    *   Формирование `request` для добавления листа.
    *   Вызов `runPrepared()` для добавления листа.
    *   Извлечение `sheetId` и `sheetTitle` из ответа `runPrepared`.
*   Вывод: `sheetId` добавленного листа.


**7. Преобразование диапазона ячеек (ReachSpreadsheet.toGridRange)**

*   Ввод: `cellsRange` (строковый диапазон).
*   Обработка:
    *   Разделение диапазона на начальную и конечную ячейки.
    *   Преобразование буквенной части координат в числовые индексы столбцов.
    *   Извлечение числовой части координат для строк.
    *   Устанавливает `sheetId` из текущего листа.
*   Вывод: Словарь `cellsRange` с числовыми координатами ячеек.



## <mermaid>

```mermaid
graph LR
    A[ReachSpreadsheet] --> B{__init__};
    B --> C[credentials];
    C --> D[httpAuth];
    D --> E[service];
    D --> F[driveService];
    E --> G[create];
    G --> H[spreadsheet().create];
    H --> I[spreadsheetId, sheetId, sheetTitle];
    I --> A;
    A --> J[share];
    J --> K[permissions().create];
    K --> L[shareRes];
    L --> J;
    A --> M[setSpreadsheetById];
    M --> N[spreadsheets().get];
    N --> O[spreadsheetId, sheetId, sheetTitle];
    O --> M;
    A --> P[runPrepared];
    P --> Q[spreadsheets().batchUpdate];
    P --> R[values().batchUpdate];
    Q --> S[replies];
    R --> T[responses];
    S,T --> P;
    A --> U[prepare_addSheet];
    U --> V[addSheet];
    V --> W[requests.append];
    W --> P;
    A --> X[toGridRange];
    X --> Y[cellsRange];
    Y --> X;
```

**Объяснение зависимостей:**

*   `googleapiclient`, `httplib2` и `oauth2client` - библиотеки для работы с Google API.
*   `tempfile`, `header`, `gs`, `utils`, `pprint`, `logger` - вероятно, пользовательские модули, используемые в проекте для работы с файлами, заголовками, хранением данных, выводом информации и логированием.

## <explanation>

**Импорты:**

*   `httplib2`: Библиотека для работы с HTTP. Используется для взаимодействия с API Google.
*   `googleapiclient.discovery`: Библиотека для построения объектов API Google.
*   `googleapiclient.errors`: Библиотека для обработки ошибок при работе с Google API.
*   `oauth2client.service_account`: Библиотека для аутентификации с использованием сервисных аккаунтов Google.
*   `tempfile`: Библиотека для работы с временными файлами.
*   `header`: По всей видимости, модуль для работы с заголовками (возможно, HTTP или каких-то внутренних).
*   `gs`: Вероятно, модуль для работы с Google Storage, хранением файлов.
*   `utils`: Модуль для общих задач, таких как парсинг JSON (`j_loads`, `j_dumps`), форматированный вывод (`pprint`).
*   `logger`: Модуль для логирования ошибок и информации.

**Классы:**

*   `SpreadsheetError`: Базовый класс для ошибок, связанных с работой с электронными таблицами.
*   `SpreadsheetNotSetError`, `SheetNotSetError`: Подклассы `SpreadsheetError` для конкретных ситуаций, когда лист или таблица не инициализированы.
*   `ReachSpreadsheet`: Основной класс для работы с Google Sheets.
    *   `__init__`: Инициализирует экземпляр класса, устанавливает подключение и авторизацию к Google Sheets API.
    *   `create`: Создаёт новый лист в Google Sheets.
    *   `share`: Устанавливает права доступа к листу.
    *   `shareWithEmailForReading`, `shareWithEmailForWriting`, `shareWithAnybodyForReading`, `shareWithAnybodyForWriting`: Удобно задавать права доступа к листу.
    *   `getSheetURL`: Возвращает URL для доступа к листу.
    *   `setSpreadsheetById`: Устанавливает текущий лист по ID.
    *   `runPrepared`: Выполняет подготовленные запросы к Google Sheets API.
    *   `prepare_addSheet`, `addSheet`: Подготавливает и выполняет запросы для добавления листа.
    *   `toGridRange`: Преобразует строковый диапазон ячеек в формат, понятный Google Sheets API.
    *   `prepare_setDimensionPixelSize`, `prepare_setColumnsWidth`, `prepare_setColumnWidth`, `prepare_setRowsHeight`, `prepare_setRowHeight`: Подготавливает запросы для изменения размеров ячеек.
    *   `prepare_setValues`: Подготавливает запрос для изменения значений в ячейках.
    *   `prepare_mergeCells`: Подготавливает запрос для слияния ячеек.
    *   `prepare_setCellStringFormatterormat`, `prepare_setCellStringFormatterormats`: Подготавливает запросы для форматирования ячеек.

**Функции:**

*   `htmlColorToJSON`: Преобразует HTML цвет в JSON формат.


**Переменные:**

*   `MODE`: Переменная, определяющая режим работы.


**Возможные ошибки и улучшения:**

*   Отсутствует явная обработка ошибок `googleapiclient.errors.HttpError` внутри методов. Стоит добавить обработку конкретных ошибок API Google, чтобы код не падал при возникновении проблем.
*   Недостаточная валидация входных данных. Например, проверка корректности вводимых диапазонов ячеек.
*   Отсутствие документации внутри кода (docstrings).


**Цепочка взаимосвязей:**

Код использует библиотеки `googleapiclient`, `httplib2` и `oauth2client` для взаимодействия с Google API. Внутри кода используется пользовательский код, `header`, `gs`, `utils`, `pprint`, `logger` для организации работы и вывода данных. Возможные внешние зависимости включают API Google и их библиотеки.