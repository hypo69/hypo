Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит класс `StringFormatter`, предоставляющий методы для форматирования строк. Методы выполняют различные операции, такие как удаление символов новой строки, HTML-тегов, нелатинских символов, специальных символов, чисел, а также экранирование HTML-тегов.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:**  Код импортирует библиотеки `re` (для регулярных выражений), `html` (для HTML-экранирования), `List`, `Dict` (типы данных из typing), `urlparse`, `parse_qs` (для работы с URL), `logger` и `html_escapes`.

2. **Определение класса `StringFormatter`:**  Класс предоставляет статические методы для форматирования строк.

3. **Метод `remove_line_breaks`:** Удаляет символы новой строки (`\n`, `\r`) из входной строки.

4. **Метод `remove_htmls`:** Удаляет HTML-теги из входной строки с помощью регулярного выражения.

5. **Метод `escape_html_tags`:** Экранирует символы `<` и `>` в строке, заменяя их на `&lt;` и `&gt;` соответственно с помощью функции `html.escape()`.

6. **Метод `escape_to_html`:** Заменяет символы на их HTML-экранированные аналоги, используя словарь `html_escapes`.

7. **Метод `remove_non_latin_characters`:** Удаляет все символы, не являющиеся латинскими буквами или пробелами.

8. **Метод `remove_special_characters`:** Удаляет все символы, не являющиеся латинскими буквами, цифрами или пробелами. Работает как для строк, так и для списков строк.

9. **Метод `clear_numbers`:** Удаляет из строки все символы, кроме цифр и точки, оставляя только числовое значение с плавающей запятой.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string.formatter import StringFormatter

    input_string = "Это строка с \\n несколькими \\rстроками. <p>Это HTML.</p>"
    formatted_string = StringFormatter.remove_line_breaks(input_string)
    print(formatted_string)  # Вывод: Это строка с несколькими строками. <p>Это HTML.</p>


    html_string = "<p><b>Текст</b></p><script>alert('XSS!')</script>"
    cleaned_string = StringFormatter.remove_htmls(html_string)
    print(cleaned_string)  # Вывод: Текст


    text_with_special = "Это строка со !#$%^ символами."
    cleaned_text = StringFormatter.remove_special_characters(text_with_special)
    print(cleaned_text) # Вывод: Это строка со символами.

    number_string = "aaa123.456 cde"
    extracted_number = StringFormatter.clear_numbers(number_string)
    print(extracted_number) # Вывод: 123.456