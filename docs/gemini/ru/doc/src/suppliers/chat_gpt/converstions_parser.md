# Модуль converstions_parser

## Обзор

Этот модуль предоставляет функцию для извлечения разговоров из файлов формата HTML. Функция `extract_conversations_from_html` итеративно возвращает каждый элемент `<div class="conversation">` из переданного HTML-файла.

## Функции

### `extract_conversations_from_html`

**Описание**: Функция `extract_conversations_from_html` извлекает все элементы `<div class="conversation">` из указанного HTML-файла и возвращает их в виде итератора.

**Параметры**:

- `file_path` (Path): Путь к HTML-файлу, содержащему разговоры.

**Возвращает**:

- итератор: Возвращает итератор, каждый элемент которого представляет собой элемент `<div class="conversation">`.


**Обрабатываемые исключения**:

- Нет указанных исключений.


## Примеры использования

```python
from pathlib import Path
from bs4 import BeautifulSoup
from hypotez.src.suppliers.chat_gpt import converstions_parser

# Пример использования:
file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
for conversation in converstions_parser.extract_conversations_from_html(file_path):
    print(conversation.prettify())
```


**Примечания**:

- Необходимо установить библиотеки `beautifulsoup4` и `pathlib`.
-  Функция `extract_conversations_from_html` предполагает, что файл имеет корректную структуру, и содержит элементы `<div class="conversation">`. В противном случае поведение функции может быть непредсказуемым.
-  В предоставленном примере используется `gs.path.data`. Предполагается, что эта переменная определена в другом модуле и содержит путь к папке с данными.
-  Используется `yield` для эффективной обработки больших файлов, возвращая каждый элемент по мере необходимости.


```
```
```
```
```