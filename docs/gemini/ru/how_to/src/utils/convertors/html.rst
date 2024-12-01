Как использовать модуль html конвертации
========================================================================================

Описание
-------------------------
Этот модуль предоставляет функции для конвертации HTML-кода в различные форматы: escape-последовательности, словари, объекты SimpleNamespace и PDF.  Он также включает функции для обратной конвертации из escape-последовательностей в HTML.

Шаги выполнения
-------------------------
1. **Импортирование модуля:** Импортируйте необходимый модуль.
   ```python
   from hypotez.src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns, html2pdf
   ```

2. **Вызов нужной функции:** Выберите подходящую функцию для конвертации, в зависимости от требуемого результата:
   - `html2escape(input_str)`: Конвертирует HTML-теги в escape-последовательности.
   - `escape2html(input_str)`: Конвертирует escape-последовательности обратно в HTML-теги.
   - `html2dict(html_str)`: Конвертирует HTML в словарь, где ключами являются теги, а значениями - их содержимое.
   - `html2ns(html_str)`: Конвертирует HTML в объект `SimpleNamespace`.
   - `html2pdf(html_str, pdf_file)`: Конвертирует HTML в PDF-файл.

3. **Передача аргументов:**  Передайте требуемый HTML-код или escape-последовательность в качестве аргумента функции. При конвертации в PDF, также укажите имя файла для сохранения результата.

4. **Обработка возвращаемого значения:**  Функции возвращают соответствующие результаты. При использовании `html2pdf`, функция возвращает `True` при успешной конвертации или `None` при возникновении ошибки.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns, html2pdf
    import io

    # Пример конвертации HTML в escape-последовательности
    html_code = "<p>Hello, world!</p>"
    escaped_html = html2escape(html_code)
    print(escaped_html)  # Вывод: &lt;p&gt;Hello, world!&lt;/p&gt;


    # Пример конвертации escape-последовательностей в HTML
    escaped_string = "&lt;p&gt;Hello, world!&lt;/p&gt;"
    unescaped_html = escape2html(escaped_string)
    print(unescaped_html) # Вывод: <p>Hello, world!</p>

    # Пример конвертации HTML в словарь
    html_string = "<p>Hello</p><a href='link'>World</a>"
    html_dict = html2dict(html_string)
    print(html_dict)  # Вывод: {'p': 'Hello', 'a': 'World'}

    # Пример конвертации HTML в SimpleNamespace
    html_namespace = html2ns(html_string)
    print(html_namespace.p)  # Вывод: Hello
    print(html_namespace.a)  # Вывод: World



    # Пример конвертации HTML в PDF
    html_content = "<html><body><h1>Example</h1></body></html>"
    pdf_file_path = "output.pdf"
    success = html2pdf(html_content, pdf_file_path)
    if success:
        print(f"PDF успешно сохранён в {pdf_file_path}")