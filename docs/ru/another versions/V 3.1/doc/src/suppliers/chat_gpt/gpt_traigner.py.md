# Модуль `gpt_traigner.py`

## Обзор

Модуль `gpt_traigner.py` предназначен для сбора и обработки данных из истории взаимодействий с ChatGPT с целью дальнейшего обучения моделей. Он включает в себя функциональность для извлечения текста из HTML-файлов, содержащих историю чата, и сохранения этих данных в различных форматах, таких как CSV, JSONL и простой текст.

## Подробней

Основная цель модуля - автоматизировать процесс сбора данных из истории чатов с ChatGPT, чтобы использовать эти данные для улучшения качества и релевантности ответов моделей. Модуль использует Selenium для управления браузером и извлечения данных из HTML-файлов, а также pandas для обработки и сохранения данных в структурированном формате.

## Классы

### `GPT_Traigner`

**Описание**: Класс `GPT_Traigner` отвечает за сбор, обработку и сохранение данных из истории взаимодействий с ChatGPT.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `GPT_Traigner`.
- `determine_sentiment`: Определяет сентимент для пары сообщений в разговоре (по умолчанию - "positive").
- `save_conversations_to_jsonl`: Сохраняет пары сообщений в формате JSONL.
- `dump_downloaded_conversations`: Собирает разговоры со страниц ChatGPT и сохраняет их в форматах CSV, JSONL и TXT.

**Параметры**:
- `driver` (Driver): Драйвер для управления браузером (по умолчанию `Chrome`).
- `gs` (GptGs): Экземпляр класса `GptGs` для работы с Google Storage.

**Примеры**:
```python
trainer = GPT_Traigner()
trainer.dump_downloaded_conversations()
```

## Функции

### `determine_sentiment`

```python
def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = 'positive') -> str:
    """ Determine sentiment label for a conversation pair """
    ...
```

**Описание**: Определяет сентимент для пары сообщений в разговоре.

**Параметры**:
- `conversation_pair` (dict[str, str]): Словарь, содержащий пару сообщений (вопрос-ответ).
- `sentiment` (str, optional): Предполагаемый сентимент (по умолчанию 'positive').

**Возвращает**:
- `str`: Строка, представляющая сентимент ('positive' или 'negative').

**Примеры**:
```python
trainer = GPT_Traigner()
conversation = {'user': 'Привет', 'assistant': 'Здравствуйте'}
sentiment = trainer.determine_sentiment(conversation)
print(sentiment)  # Вывод: positive
```

### `save_conversations_to_jsonl`

```python
def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
    """ Save conversation pairs to a JSONL file """
    ...
```

**Описание**: Сохраняет список пар сообщений в формате JSONL в указанный файл.

**Параметры**:
- `data` (list[dict]): Список словарей, где каждый словарь содержит пару сообщений.
- `output_file` (str): Путь к файлу, в который будут сохранены данные.

**Примеры**:
```python
trainer = GPT_Traigner()
data = [{'user': 'Привет', 'assistant': 'Здравствуйте'}]
output_file = 'conversations.jsonl'
trainer.save_conversations_to_jsonl(data, output_file)
```

### `dump_downloaded_conversations`

```python
def dump_downloaded_conversations(self):
    """ Collect conversations from the chatgpt page """
    ...
```

**Описание**: Собирает разговоры со страниц ChatGPT, извлекая текст из HTML-файлов, и сохраняет их в форматах CSV, JSONL и TXT.

**Методы**:
- `self.driver.get_url(file_uri)`: Открывает HTML файл в браузере.
- `self.driver.execute_locator(locator.user)`: Ищет элементы, содержащие сообщения пользователя.
- `self.driver.execute_locator(locator.assistant)`: Ищет элементы, содержащие сообщения ассистента.
- `pd.concat(all_data, ignore_index=True)`: Объединяет данные в один DataFrame.
- `all_data_df.to_csv(csv_file_path, index=False, encoding='utf-8')`: Сохраняет DataFrame в CSV файл.
- `all_data_df.to_json(jsonl_file_path, orient='records', lines=True, force_ascii=False)`: Сохраняет DataFrame в JSONL файл.

**Параметры**:
- `locator` (dict): Словарь с локаторами для поиска элементов на странице.

**Примеры**:
```python
trainer = GPT_Traigner()
trainer.dump_downloaded_conversations()
```