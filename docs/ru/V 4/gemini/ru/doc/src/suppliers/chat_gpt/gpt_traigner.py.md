# Модуль gpt_traigner.py

## Обзор

Модуль `gpt_traigner.py` предназначен для обучения моделей GPT на основе данных, собранных из истории взаимодействий с ChatGPT. Он включает в себя функциональность для извлечения данных из HTML-файлов, сохранения этих данных в различных форматах (CSV, JSONL и TXT), а также для подготовки данных к обучению моделей.

## Подорбней

Этот модуль играет важную роль в процессе улучшения и адаптации моделей GPT. Он автоматизирует сбор и обработку данных из истории чатов, что позволяет использовать эти данные для дальнейшего обучения и улучшения качества ответов модели. Собранные данные могут включать в себя вопросы пользователей и ответы ассистента, что позволяет модели лучше понимать контекст и генерировать более релевантные ответы.

## Классы

### `GPT_Traigner`

**Описание**: Класс `GPT_Traigner` предназначен для сбора и обработки данных из истории взаимодействий с ChatGPT.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `GPT_Traigner`.
- `determine_sentiment`: Определяет сентимент для пары сообщений в разговоре.
- `save_conversations_to_jsonl`: Сохраняет пары сообщений в формате JSONL.
- `dump_downloaded_conversations`: Собирает сообщения из HTML-файлов, содержащих историю чатов ChatGPT.

**Параметры**:
- `driver` (Driver): Драйвер для управления браузером (Chrome).

**Примеры**
```python
traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()
```

## Функции

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

**Описание**: Определяет сентимент (положительный или отрицательный) для пары сообщений в разговоре.

**Параметры**:
- `conversation_pair` (dict[str, str]): Словарь, содержащий пару сообщений (вопрос пользователя и ответ ассистента).
- `sentiment` (str, optional): Предполагаемый сентимент. По умолчанию 'positive'.

**Возвращает**:
- `str`: "positive", если сентимент положительный, и "negative" в противном случае.

**Примеры**:
```python
traigner = GPT_Traigner()
conversation = {'user': 'Hello', 'assistant': 'Hi'}
sentiment = traigner.determine_sentiment(conversation)
print(sentiment) # Вывод: positive
```

### `save_conversations_to_jsonl`

```python
def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
    """ Save conversation pairs to a JSONL file """
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(j_dumps(clean_string(item)) + "\n")
```

**Описание**: Сохраняет список пар сообщений в формате JSONL в указанный файл.

**Параметры**:
- `data` (list[dict]): Список словарей, где каждый словарь содержит пару сообщений (вопрос пользователя и ответ ассистента).
- `output_file` (str): Путь к файлу, в который будут сохранены данные.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.

**Примеры**:
```python
traigner = GPT_Traigner()
data = [{'user': 'Hello', 'assistant': 'Hi'}, {'user': 'How are you?', 'assistant': 'I am fine.'}]
output_file = 'conversations.jsonl'
traigner.save_conversations_to_jsonl(data, output_file)
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

**Описание**: Собирает данные из HTML-файлов, содержащих историю чатов ChatGPT, и сохраняет их в форматах CSV, JSONL и TXT.

**Параметры**:
- Отсутствуют.

**Вызывает исключения**:
- `FileNotFoundError`: Если HTML-файлы не найдены.
- `Exception`: При возникновении ошибок в процессе обработки HTML-файлов.

**Примеры**:
```python
traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()