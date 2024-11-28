Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `GSRender` для форматирования и рендеринга таблиц Google Sheets.  Класс предоставляет методы для создания и изменения таблиц, включая установку форматирования ячеек (цвет фона, выравнивание текста, шрифт), объединение ячеек, установку высоты строк и добавление заголовков и категорий. Код использует библиотеки `gspread`, `gspread_formatting`, и другие вспомогательные функции для работы с Google Sheets API.

Шаги выполнения
-------------------------
1. **Импортирование библиотек**: Код импортирует необходимые библиотеки, включая `gspread`, `gspread_formatting`, `json`, `typing`, и собственные вспомогательные модули.

2. **Определение класса `GSRender`**: Создается класс `GSRender`, содержащий методы для работы с таблицей.

3. **Метод `render_header`**: Метод `render_header` форматирует заголовок таблицы. Он принимает `Worksheet` объект, заголовок (`world_title`), диапазон ячеек (`range`), и тип объединения (`merge_type`). Метод устанавливает цвет фона, выравнивание и шрифт заголовка, а затем применяет форматирование к указанному диапазону ячеек и объединяет их.

4. **Метод `merge_range`**: Метод `merge_range` объединяет ячейки в таблице.  Принимает `Worksheet`, диапазон ячеек (`range`), и тип объединения.

5. **Метод `set_worksheet_direction`**: Метод `set_worksheet_direction` устанавливает направление текста в таблице. Принимает объект таблицы (`sh`), лист (`ws`), и направление (`direction`, по умолчанию 'rtl').

6. **Метод `header`**: Метод `header` добавляет заголовок в таблицу. Принимает объект таблицы (`ws`), заголовок (`ws_header`), и номер строки (`row`). Если `row` не указан, используется первая пустая строка. Заголовок добавляется в таблицу с применением форматирования.

7. **Метод `write_category_title`**: Метод аналогичен `header`, но предназначен для добавления категорий в таблицу.

8. **Метод `get_first_empty_row`**:  Метод находит первую пустую строку в листе. Принимает объект таблицы (`ws`) и, необязательно, номер столбца (`by_col`).


Пример использования
-------------------------
.. code-block:: python

    from gspread import Spreadsheet, Worksheet
    from spread.utils import ValueInputOption, ValueRenderOption
    from goog.spreadsheet.bberyakov.grender import GSRender
    import gspread


    # Предполагая, что у вас есть подключение к Google Sheets
    gc = gspread.service_account(filename='your_credentials.json')  # Замените на ваши данные
    spreadsheet = gc.open("Your Spreadsheet Title")
    worksheet = spreadsheet.get_worksheet(0)  # или используйте нужный индекс

    # Создание объекта GSRender
    renderer = GSRender()

    # Пример использования render_header
    renderer.render_header(worksheet, "Мой заголовок", "A1:C1", "MERGE_COLUMNS")

    # Пример использования header
    header_data = ["Имя", "Возраст", "Город"]
    renderer.header(worksheet, header_data)

    # Пример использования write_category_title
    category_title = "Клиенты"
    renderer.write_category_title(worksheet, category_title, 2)


    # ... (добавьте другие операции с таблицей) ...