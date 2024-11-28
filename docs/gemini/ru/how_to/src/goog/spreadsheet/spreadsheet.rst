Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет класс `SpreadSheet` для работы с Google Таблицами.  Он позволяет создавать новые таблицы,  авторизовываться с помощью JSON-ключа доступа, загружать данные из CSV-файла в выбранный лист.  Код включает обработку ошибок и логирование.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:**
    Код импортирует `gspread`, `pandas`, `pathlib`, `ServiceAccountCredentials` и другие модули, необходимые для работы с Google Таблицами и файлами.

2. **Создание экземпляра класса `SpreadSheet`:**
    Код создает экземпляр класса `SpreadSheet`.  Для этого требуется указать `spreadsheet_id` (идентификатор Google Таблицы).  Если `spreadsheet_id` равен `None`, то будет создана новая таблица.  Также указываются `sheet_name` (имя листа) и `spreadsheet_name` (имя новой таблицы, если создается новая).

3. **Получение доступа к Google Таблицам:**
    - Метод `_create_credentials` загружает ключ доступа из файла `e-cat-346312-137284f4419e.json`.
    - Метод `_authorize_client` авторизуется в Google Таблицах с помощью ключа доступа.
    - Метод `get_worksheet` обрабатывает ошибку `gspread.exceptions.SpreadsheetNotFound` и возвращает лист, если он существует, или создает новый при помощи `create_worksheet`, если его не было.

4. **Загрузка данных из CSV в Google Таблицы:**
    Метод `upload_data_to_sheet` выполняет следующие действия:
    - Проверяет, что указан путь к файлу (`self.data_file`) и что файл существует.
    - Читает данные из CSV-файла с помощью `pd.read_csv`.
    - Подготавливает данные для записи в Google Таблицы, добавляя заголовки в начало списка.
    - Записывает данные в Google Таблицы с помощью `self.worksheet.update('A1', data_list)`.

Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.goog.spreadsheet.spreadsheet import SpreadSheet

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на свой путь
    sheet_name = 'Sheet1'  # Замените на имя листа

    try:
        # Создаем новую таблицу, если spreadsheet_id не указан
        google_sheet_handler = SpreadSheet(
            spreadsheet_id=None,
            sheet_name=sheet_name,
            spreadsheet_name='My New Spreadsheet'
        )
        google_sheet_handler.upload_data_to_sheet()
        print("Данные успешно загружены")
    except Exception as e:
        print(f"Ошибка: {e}")