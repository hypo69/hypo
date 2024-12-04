# Модуль chat_gpt

## Обзор

Данный модуль предоставляет класс `ChatGpt` для работы с файлами диалогов, хранящимися в формате HTML.

## Классы

### `ChatGpt`

**Описание**: Класс `ChatGpt` предназначен для работы с файлами диалогов чат-бота, хранящимися в каталоге `conversations`.

**Методы**:

### `yeld_conversations_htmls`

**Описание**: Метод `yeld_conversations_htmls` итерируется по HTML-файлам в директории диалогов и возвращает их содержимое.

**Возвращает**:
- `str`: Содержимое HTML-файла.


## Переменные

### `MODE`

**Описание**: Переменная `MODE` хранит режим работы (например, 'dev').


## Использование

```python
# Пример использования класса ChatGpt
from hypotez.src.suppliers.chat_gpt import chat_gpt

chat_gpt_instance = chat_gpt.ChatGpt()
for html_content in chat_gpt_instance.yeld_conversations_htmls():
    # Обработка содержимого HTML-файла
    print(html_content)
```


## Подробное описание функций и методов

### `yeld_conversations_htmls`

**Описание**: Этот метод итерируется по всем файлам `.html` в подкаталоге `conversations` внутри директории данных, указанной в `gs.path.data`.

**Возвращает**:
- `str`: Возвращает содержимое каждого найденного HTML-файла в виде строки.

**Возможные ошибки (Raises):**
- `FileNotFoundError`: Если директория `conversations` или файлы `.html` в ней не найдены.
- `IOError`: Если возникнут проблемы при чтении файла.
- `Exception`: Общий обработчик для других возможных исключений.

**Параметры**:
- Нет явных параметров.



```python
    def yeld_conversations_htmls(self) -> str:
        """
        Итерируется по HTML-файлам в директории диалогов и возвращает их содержимое.

        Returns:
            str: Содержимое HTML-файла.
            
        Raises:
          FileNotFoundError: Если директория не найдена.
          IOError: При проблемах с чтением файлов.
          Exception: Общий обработчик для других возможных ошибок.
        """
        try:
            conversation_directory = Path(gs.path.data / 'chat_gpt' / 'conversations')
            html_files = conversation_directory.glob("*.html")
            for html_file in html_files:
                try:
                    with open(html_file, 'r', encoding='utf-8') as f:
                        yield f.read()
                except IOError as ex:
                    print(f"Ошибка при чтении файла {html_file}: {ex}")
                    raise
        except FileNotFoundError as ex:
            print(f"Директория не найдена: {ex}")
            raise
        except Exception as ex:
            print(f"Произошла ошибка: {ex}")
            raise
```

##  Импорты

- `header`: Импортируется для, вероятно, дополнительных функций или конфигурации.
- `Path`: Из `pathlib` для работы с путями к файлам.
- `gs`:  Вероятно, для доступа к глобальным настройкам или переменным.
- `recursively_read_text_files`: Из `src.utils.file`, возможно, для обработки файлов.


```