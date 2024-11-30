Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет класс `SpreadSheet` для работы с Google Таблицами.  Он позволяет создавать новые таблицы, загружать данные из CSV файла в существующую таблицу, и управлять листами.  Код использует библиотеку `gspread` для взаимодействия с API Google Таблиц.  Он требует наличия файла с ключами доступа (`e-cat-346312-137284f4419e.json`), который должен быть расположен в папке `secrets` внутри директории, заданной в переменной `gs.path.secrets`.  Также код использует `pandas` для чтения CSV-файлов.

Шаги выполнения
-------------------------
1. **Импорт необходимых библиотек:** Код импортирует `gspread`, `ServiceAccountCredentials`, `pandas`, `Path`, `logger` и другие необходимые модули из указанных библиотек.

2. **Создание объекта `SpreadSheet`:** Создается экземпляр класса `SpreadSheet`, передавая ему ID таблицы в Google Таблицах (`spreadsheet_id`) и имя листа (`sheet_name`).  Если `spreadsheet_id` равен `None`, то будет создана новая таблица с именем, указанным в `spreadsheet_name`.

3. **Установка пути к файлу данных:** Устанавливается путь к CSV файлу с помощью `data_file = Path(\'/mnt/data/google_extracted/your_data_file.csv\')`.  Этот путь должен быть изменен на фактический путь к вашему файлу.

4. **Установка имени листа:** Устанавливается имя листа в Google Таблицах с помощью `sheet_name = \'Sheet1\'`.  Этот параметр должен быть изменен на фактическое имя вашего листа.

5. **Загрузка данных в таблицу:** Метод `upload_data_to_sheet()` загружает данные из CSV файла в указанный лист.  Эта функция предварительно читает данные из CSV файла с помощью `pandas.read_csv()`, а затем использует `worksheet.update('A1', data_list)` для записи в таблицу.

6. **Обработка ошибок:** Код содержит обработку ошибок (`try...except`), чтобы справиться с возможными проблемами, такими как отсутствие файла, ошибка доступа к API или некорректные данные.

Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.goog.spreadsheet.spreadsheet import SpreadSheet

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на фактический путь
    sheet_name = 'Sheet1'  # Замените на фактическое имя листа
    spreadsheet_id = None  # Укажите ID таблицы или None для создания новой
    spreadsheet_name = 'My New Spreadsheet'  # Название новой таблицы (если spreadsheet_id = None)

    try:
        google_sheet_handler = SpreadSheet(
            spreadsheet_id=spreadsheet_id,
            sheet_name=sheet_name,
            spreadsheet_name=spreadsheet_name
        )
        google_sheet_handler.data_file = data_file
        google_sheet_handler.upload_data_to_sheet()
        print("Данные успешно загружены в Google Таблицы.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")