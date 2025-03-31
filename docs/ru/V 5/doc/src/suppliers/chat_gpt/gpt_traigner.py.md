# Модуль `gpt_traigner`

## Обзор

Модуль `gpt_traigner` предназначен для обучения моделей GPT на основе данных, собранных из переписок. Он включает в себя функциональность для извлечения данных из HTML-файлов, сохранения их в различных форматах (CSV, JSONL, TXT) и последующего использования для обучения модели.

## Подробней

Этот модуль является частью процесса подготовки данных для обучения моделей GPT. Он автоматизирует сбор данных из HTML-файлов, содержащих переписки, и предоставляет инструменты для их сохранения и дальнейшей обработки. Модуль использует веб-драйвер для извлечения данных из HTML-файлов и библиотеки `pandas` для обработки и сохранения данных в различных форматах. Собранные данные используются для обучения модели с помощью `model.stream_w`.

## Классы

### `GPT_Traigner`

**Описание**: Класс `GPT_Traigner` предназначен для сбора и обработки данных из HTML-файлов, содержащих переписки, для обучения моделей GPT.

**Как работает класс**:
Класс инициализируется с использованием драйвера `Chrome` и объекта `GptGs`. Он содержит методы для определения тональности переписки, сохранения переписок в формате JSONL и сбора переписок из HTML-файлов.

**Методы**:
- `__init__`: Инициализирует класс `GPT_Traigner`.
- `determine_sentiment`: Определяет тональность переписки.
- `save_conversations_to_jsonl`: Сохраняет переписки в формате JSONL.
- `dump_downloaded_conversations`: Собирает переписки из HTML-файлов и сохраняет их в различных форматах.

#### `__init__`

```python
def __init__(self):
    """"""
    ...
    self.gs = GptGs()
```

**Описание**: Инициализирует класс `GPT_Traigner`.

**Как работает функция**:
Метод инициализирует экземпляр класса `GPT_Traigner`. Внутри метода инициализируется объект `self.gs` класса `GptGs`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:

```python
traigner = GPT_Traigner()
```

#### `determine_sentiment`

```python
def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = 'positive') -> str:
    """ Determine sentiment label for a conversation pair """
    ...
    if sentiment:
        return "positive"
    else:
        return "negative"
```

**Описание**: Определяет тональность переписки.

**Как работает функция**:
Метод определяет тональность переписки на основе входного параметра `sentiment`. Если `sentiment` не пустой, то возвращается `"positive"`, иначе `"negative"`.

**Параметры**:
- `conversation_pair` (dict[str, str]): Словарь, представляющий пару переписки.
- `sentiment` (str, optional): Строка, указывающая тональность. По умолчанию `'positive'`.

**Возвращает**:
- `str`: Строка, представляющая тональность переписки (`"positive"` или `"negative"`).

**Вызывает исключения**:
- Нет

**Примеры**:

```python
traigner = GPT_Traigner()
conversation_pair = {'user': 'Привет', 'assistant': 'Здравствуйте'}
sentiment = 'positive'
result = traigner.determine_sentiment(conversation_pair, sentiment)
print(result)  # Вывод: positive
```

#### `save_conversations_to_jsonl`

```python
def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
    """ Save conversation pairs to a JSONL file """
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(j_dumps(clean_string(item)) + "\n")
```

**Описание**: Сохраняет переписки в формате JSONL.

**Как работает функция**:
Метод принимает список словарей `data`, где каждый словарь представляет пару переписки, и сохраняет их в формате JSONL в файл с именем `output_file`. Каждый элемент списка преобразуется в JSON-строку с помощью `j_dumps`, очищается от лишних символов с помощью `clean_string` и записывается в файл, разделяясь символом новой строки.

**Параметры**:
- `data` (list[dict]): Список словарей, представляющих переписки.
- `output_file` (str): Путь к файлу, в который нужно сохранить данные.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:

```python
traigner = GPT_Traigner()
data = [{'user': 'Привет', 'assistant': 'Здравствуйте'}]
output_file = 'conversations.jsonl'
traigner.save_conversations_to_jsonl(data, output_file)
```

#### `dump_downloaded_conversations`

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

        for user_text, assistant_text in zip_longest(user_content, assistant_content):
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

**Описание**: Собирает переписки из HTML-файлов и сохраняет их в различных форматах.

**Как работает функция**:
Метод собирает HTML-файлы из директории `gs.path.google_drive / 'chat_gpt' / 'conversation'`, извлекает из них содержимое переписок (сообщения пользователя и ассистента) с помощью веб-драйвера, и сохраняет эти переписки в формате CSV, JSONL и TXT.

1.  **Поиск HTML-файлов**:
    *   Определяется директория, в которой хранятся HTML-файлы с переписками.
    *   Используется `glob("*.html")` для получения списка всех HTML-файлов в этой директории.
2.  **Извлечение данных из HTML-файлов**:
    *   Для каждого HTML-файла:
        *   Формируется URI файла.
        *   Веб-драйвер открывает файл по URI.
        *   С использованием локаторов (`locator.user` и `locator.assistant`) находятся элементы, содержащие сообщения пользователя и ассистента.
        *   Извлекается текст из найденных элементов.
        *   Если данные не найдены, логируется ошибка.
        *   Сообщения пользователя и ассистента объединяются в пары.
        *   Для каждой пары создается словарь с ролями (`user`, `assistant`), содержимым сообщений и нейтральной тональностью.
        *   Словари добавляются в список `all_data`.
3.  **Сохранение данных**:
    *   Если были собраны какие-либо данные:
        *   Список словарей `all_data` преобразуется в DataFrame с помощью `pd.concat`.
        *   DataFrame сохраняется в CSV-файл (`all_conversations.csv`).
        *   DataFrame сохраняется в JSONL-файл (`all_conversations.jsonl`).
        *   Содержимое всех сообщений объединяется в одну строку и сохраняется в TXT-файл (`raw_conversations.txt`).

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:

```python
traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()
```

## Функции

### `model.stream_w`

```python
model = Model()
model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))
```

**Описание**: Функция для потоковой передачи данных в модель для обучения.

**Как работает функция**:
Функция `stream_w` является методом класса `Model` и предназначена для потоковой передачи данных из файла `all_conversations.csv` в модель для обучения.

**Параметры**:
- `data_file_path` (Path): Путь к файлу с данными для обучения.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:

```python
model = Model()
model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))
```