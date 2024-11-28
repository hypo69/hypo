Как использовать этот блок кода для создания и форматирования Google Таблицы
============================================================================

Описание
-------------------------
Этот код демонстрирует, как создавать и форматировать Google Таблицы с использованием Google Sheets API v4. Он использует библиотеку `google-api-python-client` для взаимодействия с API.  Код предоставляет пошаговую инструкцию и примеры, как создавать таблицы, устанавливать ширину столбцов, заполнять ячейки данными,  и настраивать форматирование (выравнивание, шрифты, цвета и т.д.). Код включает класс-обёртку `Spreadsheet`, упрощающий взаимодействие с API.

Шаги выполнения
-------------------------
1. **Установка необходимых библиотек:**
   Используйте `pip` для установки библиотеки `google-api-python-client`:
   ```bash
   pip install --upgrade google-api-python-client
   ```
2. **Создание сервисного аккаунта:**
   Создайте новый проект в Google Cloud Console и включите для него API Drive и Sheets. Создайте сервисный аккаунт и сохраните закрытый ключ в файле (например, `test-proj-for-habr-article-1ab131d98a6b.json`).
3. **Импорт необходимых библиотек:**
   ```python
   import httplib2
   import apiclient.discovery
   from oauth2client.service_account import ServiceAccountCredentials
   ```
4. **Создание объекта `Service`:**
   ```python
   CREDENTIALS_FILE = 'test-proj-for-habr-article-1ab131d98a6b.json'  # путь к файлу ключа
   credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
   httpAuth = credentials.authorize(httplib2.Http())
   service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
   ```
5. **Создание нового документа (Spreadsheet):**
   ```python
   spreadsheet = service.spreadsheets().create(body={'properties': {'title': 'Название документа', 'locale': 'ru_RU'}, 'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': 'Название листа', 'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]}).execute()
   ```
6. **Назначение доступа (необходим для доступа к созданному документу):**
   ```python
   driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)
   shareRes = driveService.permissions().create(fileId=spreadsheet['spreadsheetId'], body={'type': 'anyone', 'role': 'reader'}, fields='id').execute()
   ```
7. **Настройка ширины столбцов (используя класс Spreadsheet):**
   ```python
   # ... (импорт класса Spreadsheet из Spreadsheet.py)
   ss = Spreadsheet(service, spreadsheet['spreadsheetId'])
   ss.prepare_setColumnWidth(0, 317)
   ss.prepare_setColumnWidth(1, 200)
   ss.prepare_setColumnsWidth(2, 3, 165)
   ss.prepare_setColumnWidth(4, 100)
   ss.runPrepared()
   ```
8. **Заполнение ячеек данными:**
   ```python
   ss.prepare_setValues("B2:C3", [["Значение B2", "Значение C2"], ["Значение B3", "Значение C3"]])
   ss.runPrepared()
   ```
9. **Дополнительное форматирование (объединение ячеек, шрифты, цвета):**
  См. примеры в предоставленном коде.  Используйте соответствующие методы класса `Spreadsheet` для выполнения этих задач.  Например `prepare_mergeCells`, `prepare_setCellsFormat`, `prepare_setCellsFormats`

Пример использования
-------------------------
.. code-block:: python

   # Пример использования класса Spreadsheet (предполагается, что класс импортирован)
   import httplib2
   import apiclient.discovery
   from oauth2client.service_account import ServiceAccountCredentials

   CREDENTIALS_FILE = 'path/to/your/credentials.json'
   credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
   http_auth = credentials.authorize(httplib2.Http())
   service = apiclient.discovery.build('sheets', 'v4', http=http_auth)

   # Пример заполнения данных
   spreadsheet_id = 'YOUR_SPREADSHEET_ID'
   ss = Spreadsheet(service, spreadsheet_id)
   ss.prepare_setValues("A1", [["Заголовок"]])
   ss.prepare_setValues("B1:C2", [["Значение 1", "Значение 2"], ["Значение 3", "Значение 4"]])
   ss.runPrepared()