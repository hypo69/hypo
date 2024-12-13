# Модуль `converstions_parser`

## Обзор

Модуль `converstions_parser.py` предназначен для извлечения бесед из HTML-файлов, содержащих разметку чата. Он использует библиотеку `BeautifulSoup` для парсинга HTML и возвращает генератор, который итерируется по найденным элементам `<div class="conversation">`.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [`extract_conversations_from_html`](#extract_conversations_from_html)

## Функции

### `extract_conversations_from_html`

**Описание**: Генератор, который читает один .html файл и извлекает все `<div class="conversation">`.

**Параметры**:
- `file_path` (Path): Путь к .html файлу.

**Возвращает**:
- `generator`: Генератор, который возвращает каждый найденный элемент `<div class="conversation">`.

```python
def extract_conversations_from_html(file_path: Path):
    """
    Генератор, который читает один .html файл и извлекает все <div class="conversation">.

    Args:
        file_path (Path): Путь к .html файлу.
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