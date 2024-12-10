# Модуль converstions_parser

## Обзор

Модуль `converstions_parser` предназначен для извлечения данных о беседах из файлов формата HTML.  Он предоставляет функцию `extract_conversations_from_html` для парсинга HTML-кода и извлечения всех элементов `<div class="conversation">`.

## Функции

### `extract_conversations_from_html`

**Описание**: Функция `extract_conversations_from_html` извлекает все элементы `<div class="conversation">` из указанного HTML-файла. Она возвращает генератор, который последовательно выдает найденные элементы.

**Параметры**:

- `file_path` (Path): Путь к файлу HTML, содержащий данные о беседах.

**Возвращает**:

- генератор: Генератор, возвращающий каждый найденный элемент `<div class="conversation">`.


**Пример использования**:

```python
from pathlib import Path
# ... (импорт модуля converstions_parser)

file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())
```

**Примечания**:

- Для работы функции требуется библиотека `BeautifulSoup`.
- Функция предполагает, что файлы HTML закодированы в формате UTF-8.
- Возвращаемые элементы `<div>` можно дополнительно обработать для извлечения нужных данных.



## Использование

Модуль `converstions_parser` может быть использован для извлечения информации о беседах из файлов HTML.  Пример использования показан в блоке "Пример использования".


```
```
```python
# Пример использования
file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())  # Печатаем содержимое каждой найденной беседы
```