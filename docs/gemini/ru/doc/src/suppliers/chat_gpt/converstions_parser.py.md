# Модуль `converstions_parser`

## Обзор

Модуль `converstions_parser` предназначен для извлечения диалогов из HTML-файлов, содержащих структуру, созданную ChatGPT. Основная функциональность заключается в парсинге HTML-файла и выделении блоков с диалогами для дальнейшей обработки.

## Оглавление

1.  [Функции](#функции)
    *   [`extract_conversations_from_html`](#extract_conversations_from_html)

## Функции

### `extract_conversations_from_html`

**Описание**: Генератор, который читает один .html файл и извлекает все `<div class="conversation">`.

**Параметры**:

-   `file_path` (`Path`): Путь к .html файлу.

**Возвращает**:

-   `Iterator[bs4.element.Tag]`:  Генератор, возвращающий каждый найденный элемент `<div class="conversation">`.

**Пример использования**:

```python
file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())  # Печатаем содержимое каждой найденной беседы
```