# Модуль `chat_gpt`

## Обзор

Модуль `chat_gpt` предоставляет класс `ChatGpt`, который предназначен для работы с беседами в формате HTML, хранящимися в директории `conversations` внутри каталога `data/chat_gpt`.

## Подробней

Основная задача данного кода заключается в организации доступа к HTML-файлам, содержащим историю бесед. Это может использоваться для анализа, визуализации или дальнейшей обработки данных, полученных из чат-ботов. Класс `ChatGpt` предназначен для упрощения доступа к этим данным.

## Классы

### `ChatGpt`

**Описание**: Класс для обработки HTML-файлов бесед из директории `conversations`.

**Методы**:
- `yeld_conversations_htmls`: Предоставляет HTML-файлы бесед.

#### `yeld_conversations_htmls`

**Описание**: Предоставляет HTML-файлы бесед из директории `conversations`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: HTML-файлы бесед.

**Примеры**:

```python
from pathlib import Path
from src import gs
from src.suppliers.chat_gpt.chat_gpt import ChatGpt

# Предположим, что gs.path.data указывает на корневой каталог данных
# Создаем экземпляр класса ChatGpt
chat_gpt_instance = ChatGpt()

# Получаем HTML-файлы бесед
html_files = chat_gpt_instance.yeld_conversations_htmls()

# Выводим HTML-файлы бесед
print(html_files)