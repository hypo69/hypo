Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот фрагмент кода из файла `hypotez/src/suppliers/chat_gpt/chat_gpt.py` определяет класс `ChatGpt` и метод `yeld_conversations_htmls`.  Метод предназначен для получения списка HTML-файлов из директории `conversations` внутри директории данных, заданной в переменной `gs.path.data`.

Шаги выполнения
-------------------------
1. **Импортирует необходимые модули:**  `header`, `Path` из `pathlib`, `gs` из `src`, `recursively_read_text_files` из `src.utils.file`.
2. **Определяет константу `MODE`:**  Присваивает значение 'dev' переменной `MODE`.
3. **Определяет класс `ChatGpt`:**  Определяет класс для работы с данными чат-ботов.
4. **Определяет метод `yeld_conversations_htmls`:**  Этот метод предназначен для итерации по HTML-файлам в указанной директории.
5. **Определяет переменную `conversation_directory`:** Создает объект `Path` для указания директории `conversations` внутри директории данных.
6. **Использует `conversation_directory.glob("*.html")`:**  Находит все файлы с расширением `.html` в указанной директории.

Пример использования
-------------------------
.. code-block:: python

    import sys
    sys.path.append("src")  # Добавляем путь к папке src в PYTHONPATH
    import gs
    from suppliers.chat_gpt.chat_gpt import ChatGpt

    # Предполагается, что gs.path.data содержит путь к директории данных.
    # Если нет, замените на корректный путь.
    gs.path.data = "/путь/к/папке/данных"

    chat_gpt_instance = ChatGpt()
    for html_file in chat_gpt_instance.yeld_conversations_htmls():
        # Обработка каждого найденного HTML-файла
        print(f"Обрабатываю файл: {html_file}")
        # ... ваш код для работы с содержимым файла