Как использовать функции преобразования HTML в hypotez/src/utils/convertors/html.py
============================================================================================

Описание
-------------------------
Этот файл содержит функции для конвертации HTML в различные форматы, включая escape-последовательности, словари, объекты SimpleNamespace и PDF.  Он предоставляет инструменты для работы с HTML-данными, например, для обработки и вывода данных в формате HTML.

Шаги выполнения
-------------------------
1. **Импорт модуля:**  Для использования функций из этого файла необходимо импортировать его в ваш код:

   ```python
   from hypotez.src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns, html2pdf
   ```

2. **Вызов функции `html2escape`:**  Эта функция преобразует HTML-теги в escape-последовательности, например, `<` заменяется на `&lt;`.

   ```python
   html_input = "<p>Hello, <b>world!</b></p>"
   escaped_html = html2escape(html_input)
   print(escaped_html)  # Вывод: &lt;p&gt;Hello, &lt;b&gt;world!&lt;/b&gt;&lt;/p&gt;
   ```

3. **Вызов функции `escape2html`:**  Обратный процесс – конвертирует escape-последовательности обратно в HTML-теги.

   ```python
   escaped_html = "&lt;p&gt;Hello, &lt;b&gt;world!&lt;/b&gt;&lt;/p&gt;"
   unescaped_html = escape2html(escaped_html)
   print(unescaped_html)  # Вывод: <p>Hello, <b>world!</b></p>
   ```

4. **Вызов функции `html2dict`:** Преобразует HTML-строку в словарь, где ключами являются теги, а значениями – содержимое тегов.

   ```python
   html_input = "<p>Hello</p><a href='link'>World</a>"
   html_dict = html2dict(html_input)
   print(html_dict) # Вывод: {'p': 'Hello', 'a': 'World'}
   ```

5. **Вызов функции `html2ns`:**  Преобразует HTML-строку в объект SimpleNamespace, где атрибуты объекта соответствуют тегам, а значения атрибутов – содержимому тегов.

   ```python
   html_input = "<p>Hello</p><a href='link'>World</a>"
   html_ns = html2ns(html_input)
   print(html_ns.p)  # Вывод: Hello
   print(html_ns.a)  # Вывод: World
   ```

6. **Вызов функции `html2pdf`:** Преобразует HTML-строку в PDF-файл.  Необходимо указать путь к выходному PDF-файлу.


   ```python
   html_input = "<html><body><h1>Hello, world!</h1></body></html>"
   pdf_output_file = "output.pdf"
   success = html2pdf(html_input, pdf_output_file)

   if success:
       print(f"PDF успешно сгенерирован в {pdf_output_file}")
   ```



Пример использования (html2pdf):
```python
import os
from pathlib import Path

from hypotez.src.utils.convertors.html import html2pdf

# Пример использования
html_content = "<html><body><h1>Hello, World!</h1></body></html>"
output_path = Path("output.pdf")
success = html2pdf(html_content, output_path)

if success:
    print(f"PDF успешно создан по пути {output_path}")
else:
    print("Ошибка при создании PDF")
```


Обратите внимание, что для `html2pdf` необходима библиотека `WeasyPrint`.  Убедитесь, что она установлена.


```bash
pip install weasyprint
```


```
```
```
```
```

```