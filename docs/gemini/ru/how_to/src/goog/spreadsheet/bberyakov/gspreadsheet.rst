Как использовать класс GSpreadsheet
=========================================================================================

Описание
-------------------------
Класс `GSpreadsheet` предназначен для работы с таблицами Google Sheets. Он предоставляет методы для получения, создания и управления листами.  Класс наследуется от класса `Spreadsheet`, что предполагает существование других методов для работы с таблицами.  Он использует библиотеку `gspread` для взаимодействия с API Google Sheets.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:**  Класс `GSpreadsheet` импортирует необходимые библиотеки: `gspread`, `json`, `typing`, и `global_settingspread`. Важно убедиться, что у вас установлены `gspread` и `json` (если нет, то установите их командой `pip install gspread json`).


2. **Инициализация класса `GSpreadsheet`:**  Создайте экземпляр класса `GSpreadsheet`, передав  опционально `s_id` (ID таблицы) или `s_title` (название таблицы).  Этот этап настраивает подключение к API Google Sheets используя файл ключей `goog\\onela-hypotez-1aafa5e5d1b5.json`. Если `s_id` или `s_title` указаны, то соответствующая таблица будет загружена.

3. **Получение списка таблиц:**  Метод `get_project_spreadsheets_dict()` возвращает словарь с информацией о всех таблицах, связанных с текущим аккаунтом.  Данный метод использует файл `goog\\spreadsheets.json`.


4. **Получение таблицы по ID:**  Метод `get_by_id(sh_id)` получает таблицу по ее уникальному идентификатору `sh_id`.


5. **Получение таблицы по названию:** Метод `get_by_title(sh_title)` получает таблицу по ее названию `sh_title`. Если таблица с указанным названием не найдена, метод создаст новую таблицу и добавит в неё запись для доступа к ней пользователя с адресом  `d07708766@gmail.com` с ролью "writer". 


6. **Получение всех таблиц для текущего аккаунта:** Метод `get_all_spreadsheets_for_current_account()` открывает все таблицы (spreadsheets) для текущего аккаунта.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet

    # Инициализация класса GSpreadsheet с использованием ID таблицы
    spreadsheet = GSpreadsheet(s_id='1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')

    # Получение всех таблиц аккаунта
    all_spreadsheets = spreadsheet.get_all_spreadsheets_for_current_account()

    # Получение таблицы по названию, создание если не существует
    spreadsheet.get_by_title("Моя таблица")

    # Или по ID
    spreadsheet.get_by_id('some_id_here')

    # Вывод списка названий всех таблиц
    for sheet in spreadsheet.gsh.worksheets():
        print(sheet.title)

    # Получаем словарь всех таблиц
    project_spreadsheets_dict = spreadsheet.get_project_spreadsheets_dict()
    print(project_spreadsheets_dict)