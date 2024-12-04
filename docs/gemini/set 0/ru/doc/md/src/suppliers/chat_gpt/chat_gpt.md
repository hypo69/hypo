# Модуль hypotez/src/suppliers/chat_gpt/chat_gpt.py

## Обзор

Этот модуль предоставляет класс `ChatGpt` для работы с данными диалогов, хранящимися в формате HTML.  Он ищет файлы HTML в определенной директории.


## Оглавление

* [Классы](#классы)
    * [ChatGpt](#chatgpt)
        * [yeld_conversations_htmls](#yeld_conversations_htmls)

## Классы

### `ChatGpt`

**Описание**: Класс для работы с файлами HTML, содержащими диалоги.

**Методы**:

### `yeld_conversations_htmls`

**Описание**: Возвращает содержимое файлов HTML, содержащих диалоги.

**Возвращает**:
- `str`: Строка содержащая содержимое всех файлов HTML в указанной директории, или `None` в случае ошибки.


**Пример использования (неполный):**

```python
from hypotez.src.suppliers.chat_gpt.chat_gpt import ChatGpt

chat_gpt_supplier = ChatGpt()
html_content = chat_gpt_supplier.yeld_conversations_htmls()

if html_content:
    # Обработка содержимого html_content
    print(html_content)
else:
    print("Ошибка при чтении файлов HTML.")
```

**Детали реализации (в формате документации Python):**

```python
    def yeld_conversations_htmls(self) -> str:
        """
        Возвращает содержимое файлов HTML, содержащих диалоги.

        Returns:
            str: Строка содержащая содержимое всех файлов HTML в указанной директории, или None в случае ошибки.
        """
        conversation_directory = Path(gs.path.data / 'chat_gpt' / 'conversations')
        html_files = conversation_directory.glob("*.html")
        # ... (дополнение логики для обработки файлов)
        return ... # результат обработки файлов
```

**Комментарии**:

* Метод `yeld_conversations_htmls` использует `Path` для работы с путями к файлам, что повышает устойчивость к изменениям в файловой системе.
* Необходимо дозаполнить логику обработки файлов HTML для получения и объединения их содержимого в одну строку.


## Константы

```
MODE = 'dev'
```

**Описание**: Переменная MODE, хранит значение конфигурации.

## Импорты

```python
import header
from pathlib import Path
from src import gs
from src.utils.file import recursively_read_text_files
```

**Описание**: Импортирует необходимые модули для работы.