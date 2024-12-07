Как использовать модуль file.py
========================================================================================

Описание
-------------------------
Модуль `file.py` предоставляет функции для работы с файлами, включая чтение, запись, поиск и обработку файлов в каталогах.  Он поддерживает чтение файлов в различных форматах (строки, списки строк, JSON) и обработку ошибок.  Модуль также умеет обрабатывать каталоги и рекурсивно искать файлы, фильтруя их по расширениям.

Шаги выполнения
-------------------------
1. **Импортирование модуля:**  Для использования функций модуля, импортируйте его в ваш скрипт:

   ```python
   from hypotez.src.utils.file import save_text_file, read_text_file, get_filenames, recursively_yield_file_path, recursively_read_text_files, get_directory_names, read_files_content, remove_bom, traverse_and_clean
   ```

2. **Функция `save_text_file`:**  Сохраняет данные в текстовый файл.

   - Принимает данные (строка, список строк или словарь).
   - Принимает путь к файлу.
   - Может работать в режиме добавления (`mode='a'`).
   - Обрабатывает исключения и регистрирует ошибки в логгер.

3. **Функция `read_text_file`:** Читает содержимое файла.

   - Принимает путь к файлу.
   - Принимает `as_list=True` для чтения файла построчно.
   - Может считывать файлы в каталоге, задавая список расширений.
   - Обрабатывает исключения и регистрирует ошибки в логгер.

4. **Функция `get_filenames`:** Возвращает список имен файлов в указанном каталоге (опционально, фильтруя по расширению).


5. **Функции `recursively_yield_file_path`, `recursively_get_file_path`, `recursively_read_text_files`:** Рекурсивно обрабатывают файлы в каталоге, работая со списком файлов, генерирующим или собирающим пути к файлам, соответствующим заданному шаблону(ам).


6. **Функция `get_directory_names`:** Получает список всех подкаталогов в заданном каталоге.

7. **Функция `read_files_content`:** Читает содержимое файлов, которые соответствуют шаблону, в заданном каталоге рекурсивно.

8. **Функция `remove_bom`:** Удаляет BOM (Byte Order Mark) из текстового файла.

9. **Функция `traverse_and_clean`:** Обрабатывает все файлы .py в каталоге, удаляя BOM.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.file import save_text_file, read_text_file, recursively_read_text_files
    import os

    # Сохранение данных в файл
    data_to_save = {"key": "value"}
    file_path = "my_file.json"
    save_text_file(data_to_save, file_path)

    # Чтение содержимого файла
    content = read_text_file(file_path)
    print(content)

    # Рекурсивное чтение файлов в каталоге
    root_dir = "/path/to/your/directory"
    patterns = ["*.txt", "*.log"]
    file_contents = recursively_read_text_files(root_dir, patterns, as_list=True)
    for line in file_contents:
      print(line)