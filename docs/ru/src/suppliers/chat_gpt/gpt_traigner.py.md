# Модуль для обучения GPT модели

## Обзор

Модуль `gpt_traigner.py` предназначен для обучения модели GPT на основе данных, собранных из чатов. Он включает в себя функциональность для извлечения данных из HTML файлов, сохранения их в различных форматах (CSV, JSONL, TXT) и последующего использования этих данных для обучения модели.

## Подробней

Этот модуль является частью процесса обучения AI моделей, используемых в проекте `hypotez`. Он автоматизирует сбор и обработку данных из чатов для дальнейшего улучшения качества работы моделей.

## Классы

### `GPT_Traigner`

**Описание**: Класс `GPT_Traigner` предназначен для сбора и подготовки данных из HTML файлов с беседами для обучения модели GPT. Он включает методы для извлечения данных, определения тональности и сохранения данных в различных форматах.

**Как работает класс**:

1.  Инициализируется драйвер Chrome для взаимодействия с веб-страницами.
2.  Метод `dump_downloaded_conversations` извлекает данные из HTML файлов, содержащих историю переписки.
3.  Данные сохраняются в форматах CSV, JSONL и TXT для дальнейшего использования в обучении модели.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `GPT_Traigner` и создает экземпляр класса `GptGs`.
-   `determine_sentiment`: Определяет тональность пары сообщений.
-   `save_conversations_to_jsonl`: Сохраняет пары сообщений в файл JSONL.
-   `dump_downloaded_conversations`: Собирает сообщения со страниц ChatGPT, обрабатывает их и сохраняет в файлы.

## Функции

### `__init__`

```python
    def __init__(self):
        """"""
        ...
        self.gs = GptGs()
```

**Назначение**: Инициализирует экземпляр класса `GPT_Traigner`.

**Как работает функция**:

1.  Инициализирует экземпляр класса `GPT_Traigner`.
2.  Создает экземпляр класса `GptGs` и сохраняет его в атрибуте `gs`.

### `determine_sentiment`

```python
    def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = 'positive') -> str:
        """ Determine sentiment label for a conversation pair """
        ...
        if sentiment:
            return "positive"
        else:
            return "negative"
```

**Назначение**: Определяет тональность пары сообщений. В текущей реализации всегда возвращает "positive", если sentiment не пустой, и "negative" в противном случае.

**Параметры**:

-   `conversation_pair` (dict[str, str]): Словарь, содержащий пару сообщений.
-   `sentiment` (str, optional): Строка, определяющая тональность. По умолчанию 'positive'.

**Возвращает**:

-   `str`: "positive", если `sentiment` не пустой, и "negative" в противном случае.

**Как работает функция**:

1.  Проверяет, является ли значение переменной `sentiment` истинным (не пустым).
2.  Если `sentiment` истинно, возвращает строку "positive".
3.  В противном случае возвращает строку "negative".

**Примеры**:

```python
traigner = GPT_Traigner()
conversation_pair = {"user": "Hello", "assistant": "Hi"}
sentiment = "positive"
result = traigner.determine_sentiment(conversation_pair, sentiment)
print(result)  # Вывод: positive

sentiment = ""
result = traigner.determine_sentiment(conversation_pair, sentiment)
print(result)  # Вывод: negative
```

### `save_conversations_to_jsonl`

```python
    def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
        """ Save conversation pairs to a JSONL file """
        with open(output_file, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(j_dumps(clean_string(item)) + "\n")
```

**Назначение**: Сохраняет список словарей с беседами в файл JSONL.

**Параметры**:

-   `data` (list[dict]): Список словарей, где каждый словарь представляет собой пару сообщений.
-   `output_file` (str): Путь к файлу, в который будут сохранены данные.

**Как работает функция**:

1.  Открывает файл с именем `output_file` для записи в кодировке UTF-8.
2.  Итерируется по списку `data`.
3.  Для каждого элемента в списке, который представляет собой словарь, выполняет следующие действия:
    *   Очищает строки в словаре с помощью функции `clean_string()`.
    *   Преобразует словарь в JSON строку с помощью функции `j_dumps()`.
    *   Записывает JSON строку в файл, добавляя символ новой строки (`\n`) в конце каждой записи.

**Примеры**:

```python
from pathlib import Path
from src.utils.jjson import j_dumps

# Пример данных для сохранения
data = [
    {'role': ['user', 'assistant'], 'content': ['Привет', 'Здравствуйте']},
    {'role': ['user', 'assistant'], 'content': ['Как дела?', 'Все хорошо!']}
]

# Путь к файлу для сохранения данных
output_file = Path('conversations.jsonl')

# Сохранение данных в файл
traigner = GPT_Traigner()
traigner.save_conversations_to_jsonl(data, str(output_file))

# После выполнения этого кода будет создан файл conversations.jsonl с содержимым:
# {"role": ["user", "assistant"], "content": ["Привет", "Здравствуйте"]}
# {"role": ["user", "assistant"], "content": ["Как дела?", "Все хорошо!"]}
```

### `dump_downloaded_conversations`

```python
    def dump_downloaded_conversations(self):
        """ Collect conversations from the chatgpt page """
        ...
        conversation_directory = Path(gs.path.google_drive / 'chat_gpt' / 'conversation')
        html_files = conversation_directory.glob("*.html")

        all_data = []
        counter: int = 0  # <- counter

        for local_file_path in html_files:
            # Get the HTML content
            file_uri = local_file_path.resolve().as_uri()
            self.driver.get_url(file_uri)
            
            user_elements = self.driver.execute_locator(locator.user)
            assistant_elements = self.driver.execute_locator(locator.assistant)
            
            user_content = [element.text for element in user_elements] if isinstance(user_elements, list) else [user_elements.text] if user_elements  else None
            assistant_content = [element.text for element in assistant_elements] if isinstance(assistant_elements, list) else [assistant_elements.text] if assistant_elements  else None

            if not user_content and not assistant_content:
                logger.error(f"Где данные?")
                continue

            for user_text, assistant_text in zip_longest(user_content, assistant_content):\
                if user_text and assistant_text:
                    data = {
                        'role': ['user', 'assistant'],
                        'content': [clean_string(user_text), clean_string(assistant_text)],
                        'sentiment': ['neutral', 'neutral']
                    }
                    all_data.append(pd.DataFrame(data))
                    print(f'{counter} - {local_file_path}')
                    counter += 1

        if all_data:
            all_data_df = pd.concat(all_data, ignore_index=True)

            # Save all accumulated results to a single CSV file
            csv_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
            all_data_df.to_csv(csv_file_path, index=False, encoding='utf-8')

            # Save all accumulated results to a single JSONL file
            jsonl_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
            all_data_df.to_json(jsonl_file_path, orient='records', lines=True, force_ascii=False)
            
            # Save raw conversations to a single line without formatting
            raw_conversations = ' '.join(all_data_df['content'].dropna().tolist())
            raw_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
            with open(raw_file_path, 'w', encoding='utf-8') as raw_file:
                raw_file.write(raw_conversations)
```

**Назначение**: Собирает данные бесед со страниц ChatGPT, извлекает сообщения пользователя и ассистента, и сохраняет их в форматах CSV, JSONL и TXT.

**Как работает функция**:

1.  Определяет директорию, в которой хранятся HTML файлы с беседами, и получает список всех HTML файлов в этой директории.
2.  Инициализирует пустой список `all_data` для хранения извлеченных данных и счетчик `counter` для отслеживания количества обработанных файлов.
3.  Итерируется по списку HTML файлов. Для каждого файла выполняет следующие действия:
    *   Преобразует путь к файлу в URI и открывает его в браузере с помощью `self.driver.get_url(file_uri)`.
    *   Ищет элементы, соответствующие сообщениям пользователя и ассистента, используя локаторы `locator.user` и `locator.assistant`.
    *   Извлекает текст из найденных элементов и сохраняет его в списках `user_content` и `assistant_content`.
    *   Если не удается извлечь контент пользователя или ассистента, логирует ошибку и переходит к следующему файлу.
    *   Итерируется по парам сообщений пользователя и ассистента, используя `zip_longest`.
    *   Для каждой пары создает словарь с ролями (user, assistant), контентом (сообщения пользователя и ассистента) и тональностью (neutral).
    *   Добавляет данные в список `all_data` в виде DataFrame.
    *   Увеличивает счетчик обработанных файлов и выводит информацию о текущем файле.
4.  После обработки всех файлов, если в списке `all_data` есть данные, выполняет следующие действия:
    *   Объединяет все DataFrame в один DataFrame `all_data_df`.
    *   Сохраняет DataFrame в CSV файл (`all_conversations.csv`).
    *   Сохраняет DataFrame в JSONL файл (`all_conversations.jsonl`).
    *   Извлекает контент из столбца 'content', удаляет пропущенные значения и объединяет все сообщения в одну строку.
    *   Сохраняет строку с сырыми сообщениями в TXT файл (`raw_conversations.txt`).

**Примеры**:

```python
from pathlib import Path
from src.utils.jjson import j_dumps

# Пример данных для сохранения
# Пример не рабочий. Для тестов необходимы html файлы
# в директории google_drive / 'chat_gpt' / 'conversation'
# test_file = Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv')

# Вызов функции
# traigner = GPT_Traigner()
# traigner.dump_downloaded_conversations()

# После выполнения этого кода будут созданы файлы all_conversations.csv, all_conversations.jsonl и raw_conversations.txt
# в директории google_drive / 'chat_gpt' / 'conversation'
```