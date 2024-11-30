Как использовать модуль convertors (Tiny Utils)
========================================================================================

Описание
-------------------------
Модуль `convertors` из библиотеки Tiny Utils предоставляет набор инструментов для преобразования данных между различными форматами.  Включает в себя функции для преобразования текста в изображение PNG, XML в словарь Python, JSON в словарь Python и другие.

Шаги выполнения
-------------------------
1. **Импортирование нужного модуля:** Найдите в библиотеке Tiny Utils модуль, отвечающий за нужное преобразование (например, `text2png`, `xml2dict`, `json`). Импортируйте его в ваш скрипт.  Пример:
   ```python
   from tiny_utils.convertors import text2png
   ```
2. **Подготовьте входные данные:**  Сформируйте данные, которые нужно преобразовать. Это может быть строка текста, XML-документ, JSON-строка и т.д. Пример:
   ```python
   text_to_convert = "Привет, мир!"
   xml_data = "<root><name>John</name></root>"
   json_data = '{"name": "Alice", "age": 30}'
   ```
3. **Вызовите функцию преобразования:** Используйте функцию, предоставляемую модулем, для преобразования данных. Функции обычно принимают входные данные и опционально путь к выходному файлу (для преобразования в файл).  Пример для преобразования текста в PNG:
   ```python
   output_path = "output_image.png"
   text2png.convert(text_to_convert, output_path)
   ```
4. **Обработайте результат:**  Полученный результат (преобразованные данные) можно сохранить в переменную или использовать в дальнейшем в вашем коде.  Пример для XML в словарь:
   ```python
   dictionary = xml2dict.convert(xml_data)
   print(dictionary)
   ```
5. **Укажите путь к выходному файлу (необязательно):**  В некоторых случаях, например, при преобразовании текста в изображение, нужно указать, куда сохранить результат.  Пример:
   ```python
   text2png.convert(text_to_convert, "my_image.png")
   ```

Пример использования
-------------------------
.. code-block:: python

    from tiny_utils.convertors import text2png
    
    text_data = "This is a sample text."
    output_filename = "output.png"
    
    try:
        text2png.convert(text_data, output_filename)
        print(f"Image '{output_filename}' created successfully.")
    except Exception as e:
        print(f"Error during conversion: {e}")