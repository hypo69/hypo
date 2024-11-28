Как использовать модуль jjson
========================================================================================

Описание
-------------------------
Модуль `jjson` предоставляет функции для работы с JSON и CSV файлами. Он позволяет загружать, сохранять, объединять данные в JSON формате, конвертировать их в объекты `SimpleNamespace` для удобной работы, а также обрабатывать Markdown-строки, содержащие JSON.  Модуль обрабатывает различные аспекты работы с JSON и CSV данными, обеспечивая эффективную загрузку, сохранение и объединение данных.  Он включает функции для сохранения данных (dump), загрузки данных (load) и замены ключей в JSON.

Шаги выполнения
-------------------------
1. **Импортирование модуля:**
   Для использования функций модуля `jjson` необходимо импортировать его.  Например:

   ```python
   from hypotez.src.utils.jjson import j_dumps, j_loads, replace_key_in_json
   ```

2. **Сохранение JSON данных (j_dumps):**
   Функция `j_dumps` позволяет сохранить JSON-совместимые данные (словари, объекты `SimpleNamespace`, списки словарей или списки объектов `SimpleNamespace`) в файл или вернуть их в виде словаря.

   ```python
   # Сохранение в файл:
   data = {'name': 'John Doe', 'age': 30}
   j_dumps(data, file_path='data.json')

   # Возврат данных в виде словаря:
   data_dict = j_dumps(data) 
   ```

3. **Загрузка JSON данных (j_loads):**
   Функция `j_loads` загружает JSON или CSV данные из файла, директории или строки. Она может преобразовать JSON из файла в словарь или список словарей.

   ```python
   # Загрузка из файла:
   loaded_data = j_loads('data.json')

   # Загрузка из директории:
   loaded_data = j_loads(Path('/path/to/directory'))
   # Принимает пути к каталогам и ищет в нём файлы json. Объединяет их в один объект
   ```

4. **Конвертация в SimpleNamespace (j_loads_ns):**
   Функция `j_loads_ns` загружает данные JSON или CSV и преобразует их в объекты `SimpleNamespace` или список таких объектов. Это удобно для доступа к данным по атрибутам.

   ```python
   loaded_ns = j_loads_ns('data.json')
   print(loaded_ns.name)  # Доступ к атрибуту 'name'
   ```


5. **Замена ключей в JSON (replace_key_in_json):**
   Функция `replace_key_in_json` рекурсивно заменяет ключ в словаре или списке словарей.

   ```python
   data = {'name': 'John Doe', 'age': 30}
   new_data = replace_key_in_json(data, 'name', 'userName')
   print(new_data)  # Вывод: {'userName': 'John Doe', 'age': 30}
   ```
6. **Обработка Markdown-строк (extract_json_from_string):**
    Функция `extract_json_from_string` извлекает JSON из Markdown-строки, которая содержит JSON, заключенный в теги `````json `````.
    
    ```python
    markdown_string = """
    Some text...
    ```json
    {"name": "John Doe"}
    ```
    More text...
    """
    json_string = extract_json_from_string(markdown_string)
    print(json_string) # Вывод: {"name": "John Doe"}
    ```
7. **Обработка CSV (j_loads):**
   Функция `j_loads` способна загрузить данные из CSV-файла.

8. **Рекурсивный обход и обработка JSON файлов в каталоге (recursive_process_json_files):**
   Функция `recursive_process_json_files` позволяет рекурсивно пройти по всем подкаталогам и заменить ключ `name` на `category_name` во всех JSON-файлах.
   
   ```python
   directory = Path('/path/to/directory')
   recursive_process_json_files(directory)
   ```



Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.jjson import j_dumps, j_loads, j_loads_ns
    from pathlib import Path

    # Пример сохранения данных
    data = {'name': 'Петя', 'age': 25}
    j_dumps(data, file_path='my_data.json')

    # Пример загрузки данных из файла
    loaded_data = j_loads('my_data.json')
    print(loaded_data)

    # Пример конвертации в SimpleNamespace
    loaded_ns = j_loads_ns('my_data.json')
    print(loaded_ns.name)