Как использовать модуль bberyakov
========================================================================================

Описание
-------------------------
Модуль `bberyakov` предоставляет классы для работы с Google Spreadsheets. Он импортирует классы `GSpreadsheet`, `GWorksheet` и `GSRenderr` из соответствующих модулей.  Модуль также определяет константу `MODE`, которая имеет значение 'dev'.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей:** Модуль импортирует классы `GSpreadsheet`, `GWorksheet` и `GSRenderr`.
2. **Определение константы `MODE`:** Устанавливает значение переменной `MODE` в 'dev'. Это, вероятно, конфигурационное значение для режима работы.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet.bberyakov import GSpreadsheet, GWorksheet, GSRenderr

    # Пример использования класса GSpreadsheet
    spreadsheet = GSpreadsheet(spreadsheet_id='your_spreadsheet_id', credentials='your_credentials')

    # Пример использования класса GWorksheet (требует объект GSpreadsheet)
    worksheet = GWorksheet(spreadsheet, worksheet_id='your_worksheet_id')

    # Пример использования класса GSRenderr (требует объект GSpreadsheet или GWorksheet)
    # Предполагается, что у вас есть метод для получения данных из объекта GSpreadsheet или GWorksheet
    data = spreadsheet.get_data()  # или worksheet.get_data()
    renderer = GSRenderr(data)
    rendered_output = renderer.render()

    print(rendered_output)