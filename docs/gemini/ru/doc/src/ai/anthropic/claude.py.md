# Модуль `claude`

## Обзор

Модуль `claude` предоставляет класс `ClaudeClient` для взаимодействия с API Claude от Anthropic. Этот класс позволяет генерировать текст, анализировать тональность текста и переводить текст с одного языка на другой.

## Подробней

Модуль предназначен для интеграции с сервисами Claude, предоставляемыми Anthropic, и обеспечивает удобный интерфейс для выполнения различных задач обработки естественного языка. Он включает в себя методы для генерации текста на основе заданных запросов, анализа тональности текста и перевода текста между различными языками.

## Классы

### `ClaudeClient`

**Описание**: Класс `ClaudeClient` предоставляет интерфейс для взаимодействия с API Claude.

**Методы**:
- `__init__`: Инициализирует клиент Claude с предоставленным API-ключом.
- `generate_text`: Генерирует текст на основе предоставленного запроса.
- `analyze_sentiment`: Анализирует тональность предоставленного текста.
- `translate_text`: Переводит предоставленный текст с исходного языка на целевой язык.

**Параметры**:
- `api_key` (str): API-ключ для доступа к сервисам Claude.

**Примеры**
```python
    claude_client = ClaudeClient('your_api_key')
    prompt = 'Write a short story about a robot learning to love.'
    generated_text = claude_client.generate_text(prompt)
    print('Generated Text:', generated_text)
    text_to_analyze = 'I am very happy today!'
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print('Sentiment Analysis:', sentiment_analysis)
    text_to_translate = 'Hello, how are you?'
    source_language = 'en'
    target_language = 'es'
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print('Translated Text:', translated_text)
```

## Функции

### `__init__`

```python
    def __init__(self, api_key: str) -> None:
        """
        Инициализирует клиент Claude с предоставленным API-ключом.

        Args:
            api_key (str): API-ключ для доступа к сервисам Claude.

        Example:
            >>> claude_client = ClaudeClient('your_api_key')
        """
        self.client = anthropic.Client(api_key)
```

**Описание**: Инициализирует клиент Claude с использованием предоставленного API-ключа. Этот метод создает экземпляр клиента `anthropic.Client` и сохраняет его для дальнейшего использования.

**Параметры**:
- `api_key` (str): API-ключ, необходимый для аутентификации и доступа к сервисам Claude.

**Примеры**:
```python
claude_client = ClaudeClient('your_api_key')
```

### `generate_text`

```python
    def generate_text(self, prompt: str, max_tokens_to_sample: int = 100) -> str:
        """
        Генерирует текст на основе предоставленного запроса.

        Args:
            prompt (str): Запрос для генерации текста.
            max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

        Returns:
            str: Сгенерированный текст.

        Example:
            >>> claude_client.generate_text('Write a short story.')
            'A short story about...'
        """
        response = self.client.completion(
            prompt=prompt,
            model='claude-v1',
            max_tokens_to_sample=max_tokens_to_sample,
            stop_sequences=['\n\nHuman:']
        )
        return response['completion']
```

**Описание**: Генерирует текст, используя API Claude, на основе предоставленного запроса (prompt).

**Параметры**:
- `prompt` (str): Запрос, используемый для генерации текста.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов, которое API должен сгенерировать. По умолчанию равно 100.

**Возвращает**:
- `str`: Сгенерированный текст.

**Примеры**:
```python
claude_client = ClaudeClient('your_api_key')
generated_text = claude_client.generate_text('Write a short story.')
print(generated_text)
```

### `analyze_sentiment`

```python
    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность предоставленного текста.

        Args:
            text (str): Текст для анализа.

        Returns:
            str: Результат анализа тональности.

        Example:
            >>> claude_client.analyze_sentiment('I am very happy!')
            'Positive'
        """
        response = self.client.completion(
            prompt=f'Analyze the sentiment of the following text: {text}',
            model='claude-v1',
            max_tokens_to_sample=50,
            stop_sequences=['\n\nHuman:']
        )
        return response['completion']
```

**Описание**: Анализирует тональность предоставленного текста с использованием API Claude.

**Параметры**:
- `text` (str): Текст, который необходимо проанализировать на предмет тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Примеры**:
```python
claude_client = ClaudeClient('your_api_key')
sentiment = claude_client.analyze_sentiment('I am very happy!')
print(sentiment)
```

### `translate_text`

```python
    def translate_text(self, text: str, source_language: str, target_language: str) -> str:
        """
        Переводит предоставленный текст с исходного языка на целевой язык.

        Args:
            text (str): Текст для перевода.
            source_language (str): Код исходного языка.
            target_language (str): Код целевого языка.

        Returns:
            str: Переведенный текст.

        Example:
            >>> claude_client.translate_text('Hello', 'en', 'es')
            'Hola'
        """
        response = self.client.completion(
            prompt=f'Translate the following text from {source_language} to {target_language}: {text}',
            model='claude-v1',
            max_tokens_to_sample=100,
            stop_sequences=['\n\nHuman:']
        )
        return response['completion']
```

**Описание**: Переводит текст с одного языка на другой, используя API Claude.

**Параметры**:
- `text` (str): Текст, который необходимо перевести.
- `source_language` (str): Код языка оригинала текста.
- `target_language` (str): Код языка, на который требуется перевести текст.

**Возвращает**:
- `str`: Переведенный текст.

**Примеры**:
```python
claude_client = ClaudeClient('your_api_key')
translated_text = claude_client.translate_text('Hello', 'en', 'es')
print(translated_text)