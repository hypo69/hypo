# Модуль src.ai.anthropic.claude

## Обзор

Модуль `src.ai.anthropic.claude` предоставляет класс `ClaudeClient` для взаимодействия с API Anthropic Claude.  Он определяет корневой путь к проекту для корректных импортов и содержит примеры использования.

## Оглавление

- [Модуль src.ai.anthropic.claude](#модуль-src-ai-anthropic-claude)
- [Обзор](#обзор)
- [Классы](#классы)
    - [`ClaudeClient`](#claudeclient)
        - [`__init__`](#init)
        - [`generate_text`](#generate_text)
        - [`analyze_sentiment`](#analyze_sentiment)
        - [`translate_text`](#translate_text)
- [Пример использования](#пример-использования)


## Классы

### `ClaudeClient`

**Описание**: Класс для взаимодействия с API Anthropic Claude.

**Методы**:

#### `__init__`

```python
def __init__(self, api_key):
    """
    Инициализирует клиент Claude.

    Args:
        api_key (str): Ключ API Anthropic Claude.
    """
    self.client = anthropic.Client(api_key)
```

#### `generate_text`

```python
def generate_text(self, prompt, max_tokens_to_sample=100):
    """
    Генерирует текст на основе заданного запроса.

    Args:
        prompt (str): Запрос для генерации текста.
        max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

    Returns:
        str: Сгенерированный текст.

    """
    response = self.client.completion(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=max_tokens_to_sample,
        stop_sequences=["\n\nHuman:"]
    )
    return response['completion']
```

#### `analyze_sentiment`

```python
def analyze_sentiment(self, text):
    """
    Анализирует тональность заданного текста.

    Args:
        text (str): Текст для анализа.

    Returns:
        str: Результат анализа тональности.
    """
    response = self.client.completion(
        prompt=f"Analyze the sentiment of the following text: {text}",
        model="claude-v1",
        max_tokens_to_sample=50,
        stop_sequences=["\n\nHuman:"]
    )
    return response['completion']
```

#### `translate_text`

```python
def translate_text(self, text, source_language, target_language):
    """
    Переводит текст из исходного языка на целевой.

    Args:
        text (str): Текст для перевода.
        source_language (str): Код исходного языка.
        target_language (str): Код целевого языка.

    Returns:
        str: Переведенный текст.
    """
    response = self.client.completion(
        prompt=f"Translate the following text from {source_language} to {target_language}: {text}",
        model="claude-v1",
        max_tokens_to_sample=100,
        stop_sequences=["\n\nHuman:"]
    )
    return response['completion']
```

## Пример использования

```python
# Пример использования класса
if __name__ == "__main__":
    api_key = "your-api-key"  # Замените на ваш ключ API
    claude_client = ClaudeClient(api_key)

    # Пример генерации текста
    prompt = "Напишите короткую историю о роботе, который учится любить."
    generated_text = claude_client.generate_text(prompt)
    print("Сгенерированный текст:", generated_text)

    # Пример анализа тональности
    text_to_analyze = "Сегодня я очень счастлив!"
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print("Анализ тональности:", sentiment_analysis)

    # Пример перевода текста
    text_to_translate = "Привет, как дела?"
    source_language = "ru"
    target_language = "en"
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print("Переведенный текст:", translated_text)
```

**Примечание**:  Замените `"your-api-key"` на ваш фактический ключ API Anthropic Claude.