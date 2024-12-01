Как использовать функцию extract_conversations_from_html
========================================================================================

Описание
-------------------------
Функция `extract_conversations_from_html` извлекает все элементы `<div class="conversation">` из заданного HTML-файла и возвращает их в виде генератора.  Она обрабатывает один файл за раз.

Шаги выполнения
-------------------------
1. **Открытие и парсинг HTML-файла:** Функция открывает переданный файл с указанным путем (`file_path`) в режиме чтения (`'r'`) с кодировкой `utf-8`. Она использует библиотеку `BeautifulSoup` для парсинга содержимого файла.
2. **Поиск элементов `<div class="conversation">`:**  Найденное содержимое HTML-файла анализируется, и функция ищет все элементы `<div>` с атрибутом `class="conversation"`.
3. **Возврат элементов в генераторе:**  Функция возвращает каждый найденный элемент `<div class="conversation">` в виде генератора. Это позволяет обрабатывать большие объемы данных по частям, не загружая все данные сразу в память.
4. **Итерация по генератору:** В примере используется цикл `for` для итерации по генератору и вывода содержимого каждого элемента.


Пример использования
-------------------------
.. code-block:: python

    import header
    from src import gs
    from pathlib import Path
    from bs4 import BeautifulSoup

    def extract_conversations_from_html(file_path: Path):
        """Генератор, который читает один .html файл и извлекает все <div class="conversation">."""
        with file_path.open('r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            conversations = soup.find_all('div', class_='conversation')
        for conversation in conversations:
            yield conversation

    # Пример использования
    file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
    for conversation in extract_conversations_from_html(file_path):
        print(conversation.prettify())