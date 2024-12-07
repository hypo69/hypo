Как использовать модуль `hypotez/src/utils/convertors`
========================================================================================

Описание
-------------------------
Этот модуль предоставляет функции для конвертации различных форматов данных, таких как CSV, JSON, XML, HTML, Markdown, Base64, работа с изображениями (PNG, WebP) и текстом.  Модуль включает утилиты для преобразования данных в словари, списки, форматы для работы с таблицами и многое другое, а также включает функции для работы с аудио (преобразование речи в текст и наоборот).

Шаги выполнения
-------------------------
1. **Импортирование нужных функций:**
   Импортируйте необходимые функции из модуля `src.utils.convertors`.  Например, для конвертации CSV в словарь:

   ```python
   from src.utils.convertors import csv2dict
   ```

2. **Вызов функции конвертации:**
   Вызовите нужную функцию, передав ей необходимые аргументы.  Например, для конвертации файла `data.csv` в словарь:

   ```python
   csv_data = csv2dict('data.csv')
   ```

3. **Обработка результата:**
   Полученный результат (словарь, список или другой формат данных) можно использовать в последующих операциях.

4. (Необязательно) **Обработка ошибок:**
   Некоторые функции могут генерировать исключения, если входные данные не соответствуют ожидаемому формату или в случае проблем с файлами.  Рекомендуется обработать потенциальные ошибки с помощью блоков `try...except`.


Пример использования
-------------------------
.. code-block:: python

    from src.utils.convertors import csv2dict, json2xls

    # Преобразование CSV в словарь
    try:
        csv_data = csv2dict('data.csv')
        print(csv_data)  # Вывод полученного словаря
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


    # Преобразование JSON в XLSX (предполагая, что 'data.json' существует)
    try:
        json_data = json2xls('data.json')
        print(f"Файл 'data.xlsx' успешно создан.")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")