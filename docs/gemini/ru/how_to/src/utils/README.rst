Как использовать модуль convertors в Tiny Utils
========================================================================================
Описание
-------------------------
Модуль `convertors` в библиотеке Tiny Utils предоставляет инструменты для конвертации данных между различными форматами, включая текст в изображение, XML в словарь, JSON и др.  Он содержит функции для работы с различными типами файлов, такими как текст, изображения, XML, JSON и т.д.

Шаги выполнения
-------------------------
1. **Импортируйте необходимый модуль:**  Определяется, какой именно модуль из `convertors` требуется для конвертации. Например, для конвертации текста в PNG изображение:

   ```python
   from tiny_utils.convertors import text2png
   ```

2. **Подготовьте входные данные:**  Задайте данные, которые необходимо конвертировать. Для `text2png` это текст, который необходимо преобразовать в изображение.  Для `xml2dict` - XML строка.

   ```python
   text_to_convert = "Hello, world!"
   xml_data = "<root><item>Hello</item></root>"
   ```

3. **Вызовите функцию конвертации:**  Используйте соответствующую функцию модуля для выполнения конвертации.  Функция `text2png.convert` принимает текст и путь к выходному изображению.

   ```python
   output_image_path = "output_image.png"
   text2png.convert(text_to_convert, output_image_path)
   ```

4. **Обработайте результат:**  В зависимости от типа конвертации, результат может быть разным.  В случае конвертации текста в изображение, результат - созданный файл изображения. В случае конвертации XML в словарь - созданный словарь.

   ```python
   # Пример для обработки результата конвертации XML в словарь
   import tiny_utils.convertors.xml2dict as xml2dict
   dictionary_result = xml2dict.convert(xml_data)
   print(dictionary_result)
   ```

Пример использования
-------------------------
.. code-block:: python

    from tiny_utils.convertors import text2png

    text_to_convert = "This is a sample text."
    output_image_path = "output_image.png"
    text2png.convert(text_to_convert, output_image_path)
    print(f"Image '{output_image_path}' created successfully.")