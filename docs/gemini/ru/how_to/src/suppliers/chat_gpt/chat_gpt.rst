Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный код из файла `hypotez/src/suppliers/chat_gpt/chat_gpt.py` определяет класс `ChatGpt`, содержащий метод `yeld_conversations_htmls`.  Метод  `yeld_conversations_htmls` предназначен для получения списка путей к файлам в формате HTML, расположенных в подкаталоге `conversations` внутри каталога, указанного в переменной `gs.path.data`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**: Код импортирует модули `header`, `Path` из `pathlib`, `gs` из `src`, и `recursively_read_text_files` из `src.utils.file`.

2. **Определение класса `ChatGpt`**: Определяется класс `ChatGpt`.

3. **Определение метода `yeld_conversations_htmls`**: Определяется метод `yeld_conversations_htmls`, принимающий данные типа `str`.

4. **Получение пути к каталогу с HTML файлами**:  Создается объект `Path` для указанного каталога `conversations` в подкаталоге `chat_gpt` внутри каталога, заданного переменной `gs.path.data`.  Это переменная `gs.path.data`, вероятно, определена в другом модуле (`src.gs`) и содержит путь к основному каталогу данных.

5. **Поиск файлов в формате HTML**: Используется метод `glob("*.html")` для поиска всех файлов с расширением ".html" в указанном каталоге. Результат – итерируемый объект, содержащий `Path` объекты к искомым файлам.


Пример использования
-------------------------
.. code-block:: python

    import gs
    from hypotez.src.suppliers.chat_gpt.chat_gpt import ChatGpt

    # Предполагая, что gs.path.data содержит путь к каталогу данных
    # ... (код для инициализации gs.path.data) ...

    chat_gpt_instance = ChatGpt()
    html_files = chat_gpt_instance.yeld_conversations_htmls()

    # Проверка результатов
    for file_path in html_files:
        print(file_path)