Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Этот код импортирует классы `Spreadsheet` и `ReachSpreadsheet` из модулей `spreadsheet` и `reach_spreadsheet` соответственно, которые, предположительно, содержат функционал для работы со  спредшитами Google.  Также он определяет константу `MODE`, которая, вероятно, задаёт режим работы (например, 'dev', 'prod').

Шаги выполнения
-------------------------
1. Импортирует класс `Spreadsheet` из модуля `src.goog.spreadsheet.spreadsheet`.
2. Импортирует класс `ReachSpreadsheet` из модуля `src.goog.spreadsheet.reach_spreadsheet`.
3. Определяет константу `MODE` со значением 'dev'.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet import SpreadSheet, ReachSpreadsheet

    # Пример использования класса SpreadSheet (замените на фактические параметры)
    spreadsheet_object = SpreadSheet(spreadsheet_id='your_spreadsheet_id', credentials='your_credentials')
    data = spreadsheet_object.get_data()
    print(data)

    # Пример использования класса ReachSpreadsheet (замените на фактические параметры)
    reach_spreadsheet = ReachSpreadsheet(reach_spreadsheet_id='your_reach_spreadsheet_id', credentials='your_reach_credentials')
    updated_data = reach_spreadsheet.update_data(new_data={"column1": "value1", "column2": "value2"})
    print(updated_data)