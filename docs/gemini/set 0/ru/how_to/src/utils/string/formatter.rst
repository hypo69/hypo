Как использовать модуль `formatter.py`
========================================================================================

Описание
-------------------------
Модуль `formatter.py` содержит набор функций для форматирования строк.  Эти функции позволяют удалять или модифицировать различные символы (пробелы, HTML-теги, специальные символы, нелатинские символы, числа) в строках.  Они также предоставляют инструменты для работы со списками строк.

Шаги выполнения
-------------------------
1. **Импортируйте модуль:**
   Импортируйте класс `StringFormatter` из файла `formatter.py`:

   ```python
   from hypotez.src.utils.string.formatter import StringFormatter
   ```

2. **Выберите нужную функцию:**
   Выберите функцию из модуля, соответствующую вашей задаче, например:
   - `remove_line_breaks()` для удаления переносов строк.
   - `remove_htmls()` для удаления HTML-тегов.
   - `remove_non_latin_characters()` для удаления символов, не являющихся латинскими.
   - `remove_special_characters()` для удаления специальных символов.
   - `clear_numbers()` для сохранения только чисел и точек.
   - и т.д.

3. **Передайте строку (или список строк) в качестве аргумента:**
   Функции принимают строку или список строк в качестве входных данных.  Обратите внимание на типы данных, ожидаемые функцией (например, `remove_special_characters` может принимать как строку, так и список строк).

4. **Получите результат:**
   Функция вернёт отформатированную строку (или список строк).


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string.formatter import StringFormatter

    input_string = "Строка\nс\nпереносами\nстрок."
    formatted_string = StringFormatter.remove_line_breaks(input_string)
    print(formatted_string)  # Выведет: Строка с переносами строк.


    input_html = "<p>Это <strong>текст</strong> с HTML-тегами.</p>"
    cleaned_text = StringFormatter.remove_htmls(input_html)
    print(cleaned_text)  # Выведет: Это текст с HTML-тегами.


    input_list = ["строка 1", "строка 2 с спец. символами!", "строка 3"]
    cleaned_list = StringFormatter.remove_special_characters(input_list)
    print(cleaned_list) # Выведет: ['строка 1', 'строка 2 с спец символами', 'строка 3']

    input_number_string = "aaa123.456 cde"
    output_number_string = StringFormatter.clear_numbers(input_number_string)
    print(output_number_string) # Выведет: 123.456