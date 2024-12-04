Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код импортирует классы `Spreadsheet` и `ReachSpreadsheet` из модуля `spreadsheet`. Он также определяет константу `MODE` со значением 'dev'.

Шаги выполнения
-------------------------
1. Определяет константу `MODE` и присваивает ей строковое значение 'dev'.
2. Импортирует класс `Spreadsheet` из подмодуля `spreadsheet`.
3. Импортирует класс `ReachSpreadsheet` из подмодуля `reach_spreadsheet`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet import SpreadSheet, ReachSpreadsheet

    # Пример использования класса Spreadsheet
    spreadsheet_object = SpreadSheet()
    # Здесь вы можете вызвать методы класса Spreadsheet,
    # например, методы для работы с Google Таблицами.

    # Пример использования класса ReachSpreadsheet
    reach_spreadsheet_object = ReachSpreadsheet()
    # Здесь вы можете вызвать методы класса ReachSpreadsheet,
    # например, методы для взаимодействия с Google Таблицами
    # через другой API.

    #  Например, если вы хотите проверить константу MODE:
    if MODE == 'dev':
        print("Сейчас используется режим разработки")