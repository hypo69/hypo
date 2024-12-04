Как использовать функцию extract_conversations_from_html
=============================================================================================

Описание
-------------------------
Функция `extract_conversations_from_html` извлекает все блоки `<div class="conversation">` из переданного HTML-файла. Она возвращает каждый извлеченный блок в виде итератора.

Шаги выполнения
-------------------------
1. **Принимает на вход:** Путь к файлу с расширением `.html` (объект `Path`).
2. **Открывает файл:** Открывает переданный файл в режиме чтения (`'r'`) с кодировкой `utf-8`.
3. **Парсит HTML:** Использует библиотеку `BeautifulSoup` для парсинга содержимого файла в объект `soup`.
4. **Ищет блоки `<div class="conversation">`:**  Использует метод `find_all` объекта `soup` для поиска всех элементов `div` с классом `conversation`.
5. **Возвращает итератор:** Возвращает итератор, содержащий каждый найденный блок `conversation`.  Функция `yield` позволяет возвращать элементы по одному, не загружая весь результат в память сразу.

Пример использования
-------------------------
.. code-block:: python

    import header
    from src import gs
    from pathlib import Path
    from bs4 import BeautifulSoup

    from hypotez.src.suppliers.chat_gpt.converstions_parser import extract_conversations_from_html

    # Пример пути к файлу (замените на ваш путь)
    file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')

    # Используем функцию для извлечения бесед
    for conversation in extract_conversations_from_html(file_path):
        print(conversation.prettify())  # Выводим отформатированную версию каждой беседы.