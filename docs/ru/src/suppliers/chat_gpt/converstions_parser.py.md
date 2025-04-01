# Модуль `converstions_parser`

## Обзор

Модуль `converstions_parser` предназначен для извлечения бесед из HTML-файлов, содержащих записи чатов, с использованием библиотеки `BeautifulSoup`. Он предоставляет функциональность для чтения и парсинга HTML-файлов, поиска элементов `<div class="conversation">` и возврата их содержимого.

## Подробней

Модуль используется для обработки файлов, содержащих историю переписки из чатов, например, сгенерированных ChatGPT. Он позволяет извлекать отдельные блоки переписки для дальнейшего анализа или обработки. Модуль предназначен для работы с HTML-файлами, имеющими определенную структуру, где каждая беседа заключена в элемент `div` с классом `conversation`.

## Функции

### `extract_conversations_from_html`

```python
def extract_conversations_from_html(file_path: Path):
    """Генератор, который читает один .html файл и извлекает все <div class="conversation">.

    :param file_path: Путь к .html файлу.
    """
    # Открываем файл и парсим его содержимое
    with file_path.open('r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Ищем все <div class="conversation">
        conversations = soup.find_all('div', class_='conversation')
        ...
    # Возвращаем каждую найденную conversation
    for conversation in conversations:
        yield conversation
```

**Назначение**: Извлекает беседы из HTML-файла.

**Параметры**:
- `file_path` (Path): Путь к HTML-файлу.

**Возвращает**:
- Генератор, который выдает каждый элемент `<div class="conversation">`, найденный в HTML-файле.

**Как работает функция**:

1.  **Открытие файла**: Функция открывает HTML-файл, указанный в `file_path`, в режиме чтения с кодировкой UTF-8.
2.  **Парсинг HTML**: Использует `BeautifulSoup` для парсинга содержимого файла.
3.  **Поиск элементов**: Ищет все элементы `<div class="conversation">` в структуре HTML.
4.  **Генерация результатов**: Возвращает каждый найденный элемент `conversation` с использованием генератора.

**Примеры**:

```python
from pathlib import Path
from src import gs

file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())