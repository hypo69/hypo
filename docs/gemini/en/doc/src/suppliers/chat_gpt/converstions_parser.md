# conversations_parser.py

## Overview

This module provides functionality for parsing HTML files to extract conversation elements. It utilizes the `BeautifulSoup` library for HTML parsing and yields conversation divs.


## Functions

### `extract_conversations_from_html`

**Description**: This function reads an HTML file, parses it using BeautifulSoup, and extracts all `<div class="conversation">` elements.  It yields each conversation element.

**Parameters**:

- `file_path` (Path): The path to the HTML file to be parsed.


**Yields**:

- `BeautifulSoup.Tag`: Each `<div class="conversation">` element found in the HTML file.


**Raises**:

- `FileNotFoundError`: If the specified `file_path` does not exist.
- `UnicodeDecodeError`: If the file cannot be decoded using UTF-8 encoding.


```python
def extract_conversations_from_html(file_path: Path):
    """Генератор, который читает один .html файл и извлекает все <div class="conversation">.\n\n    :param file_path: Путь к .html файлу.\n    """
    # Открываем файл и парсим его содержимое
    with file_path.open('r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Ищем все <div class="conversation">
        conversations = soup.find_all('div', class_='conversation')
        # ... (rest of the function as provided)
    # Возвращаем каждую найденную conversation
    for conversation in conversations:
        yield conversation
```


## Usage Example

```python
# Example usage (provided in the original code):
file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())  # Печатаем содержимое каждой найденной беседы
```


**Note:** The original code contains `...` after finding conversations. This section appears to be placeholder code and is not included in the documented function.  A complete implementation would be necessary to provide the full extraction logic. Also the provided docstrings are using russian and english which is not recommended for production code. It would be better to use english only or a separate section for russian documentation.