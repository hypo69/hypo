Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код демонстрирует, как создавать и изменять Google-таблицы с помощью Google Sheets API v4.  Он показывает, как создавать новые таблицы, устанавливать ширину столбцов, заполнять ячейки данными, объединять ячейки, настраивать форматирование (цвет фона, шрифт, выравнивание), а также как получить доступ к созданным таблицам.  Код содержит класс-обертку `Spreadsheet`, упрощающий работу с API.

Шаги выполнения
-------------------------
1. **Установка библиотек:** Установите библиотеку `google-api-python-client` с помощью pip:
   ```bash
   pip install --upgrade google-api-python-client
   ```

2. **Загрузка закрытого ключа:**  Подготовьте файл JSON с закрытым ключом для сервисного аккаунта, который будет использоваться для доступа к Google Таблицам.  Этот файл (`test-proj-for-habr-article-1ab131d98a6b.json` в примере) содержит необходимые данные для аутентификации.

3. **Импортирование необходимых библиотек:** Импортируйте необходимые модули:
   ```python
   import httplib2
   import apiclient.discovery
   from oauth2client.service_account import ServiceAccountCredentials
   ```

4. **Создание `service`-объекта:** Создайте `service`-объект, необходимый для взаимодействия с Google Sheets API:
   ```python
   CREDENTIALS_FILE = 'test-proj-for-habr-article-1ab131d98a6b.json'  # Имя файла с ключом
   credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
   httpAuth = credentials.authorize(httplib2.Http())
   service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
   ```

5. **Создание нового документа (spreadsheet):** Используйте метод `spreadsheets.create` для создания нового Google-документа (spreadsheet):
   ```python
   spreadsheet = service.spreadsheets().create(body={'properties': {'title': 'Название документа', 'locale': 'ru_RU'}, 'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': 'Название листа', 'gridProperties': {'rowCount': 8, 'columnCount': 5}}} ]}).execute()
   ```
   Обратите внимание на `spreadsheetId`, полученный в ответе. Он необходим для дальнейших операций.

6. **Получение доступа к документу:** Используйте Google Drive API, чтобы выдать доступ сервисному аккаунту к только что созданному документу:
   ```python
   driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)
   shareRes = driveService.permissions().create(fileId=spreadsheet['spreadsheetId'], body={'type': 'anyone', 'role': 'reader'}, fields='id').execute()
   ```

7. **Установка ширины столбцов:**  Используя `spreadsheets.batchUpdate`, задайте ширину столбцов.  Обратите внимание на использование `UpdateDimensionPropertiesRequest` для изменения свойств столбцов:
   ```python
    # Пример задания ширины столбцов (A, B, C, D, E) в пикселях
   # ... (код из примера) ...
   ```

8. **Заполнение ячеек данными:**  Используйте `spreadsheets.values.batchUpdate` для заполнения ячеек данными:
   ```python
   # ... (код из примера) ...
   ```

9. **Настройка форматирования:** Используйте `UpdateCellsRequest`, `MergeCellsRequest` и другие запросы, чтобы настроить форматирование ячеек (цвет фона, шрифт, объединение, границы):
   ```python
   # ... (код из примера) ...
   ```

10. **Использование класса-обертки `Spreadsheet`:**  Используйте класс `Spreadsheet` для упрощения работы с API, как показано в примере.

**Пример использования (фрагмент):**

```python
from your_spreadsheet_class import Spreadsheet

spreadsheet_id = "YOUR_SPREADSHEET_ID"  # Получите ID из предыдущего шага
sheet_title = "Название листа"

ss = Spreadsheet(service, spreadsheet_id, sheet_title)
ss.prepare_setColumnWidth(0, 317)
ss.prepare_setColumnWidth(1, 200)
ss.prepare_setColumnsWidth(2, 3, 165)
ss.runPrepared()
```

**Важно:** Замените `YOUR_SPREADSHEET_ID` на фактический ID документа.  Полный пример использования класса `Spreadsheet` и примеры настройки форматирования приведены в исходном коде.


```
```
```python
```
```
```
```
```
```
```