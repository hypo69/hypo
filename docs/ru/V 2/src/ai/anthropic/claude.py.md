# Модуль `claude.py`

## Обзор

Модуль `claude.py` предоставляет интерфейс для взаимодействия с API Claude от Anthropic. Он включает класс `ClaudeClient`, который инкапсулирует функциональность для генерации текста, анализа тональности и перевода текста.

## Оглавление

1. [Классы](#классы)
   - [`ClaudeClient`](#claudeclient)
2. [Пример использования](#пример-использования)

## Классы

### `ClaudeClient`

**Описание**: Класс `ClaudeClient` предоставляет методы для взаимодействия с API Claude от Anthropic.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `ClaudeClient`.
- `generate_text`: Генерирует текст на основе заданного запроса.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `translate_text`: Переводит текст с одного языка на другой.

#### `__init__`

```python
def __init__(self, api_key):
    """
    Args:
        api_key (str): API-ключ для доступа к сервису Claude.
    """
```
**Описание**: Инициализирует экземпляр класса `ClaudeClient`, принимая API-ключ для аутентификации.

**Параметры**:
    - `api_key` (str): API-ключ для доступа к сервису Claude.

#### `generate_text`

```python
def generate_text(self, prompt, max_tokens_to_sample=100) -> str:
    """
    Generates text based on the given prompt.

    Args:
        prompt (str): The prompt to generate text from.
        max_tokens_to_sample (int, optional): The maximum number of tokens to generate. Defaults to 100.

    Returns:
        str: The generated text.
    """
```

**Описание**: Генерирует текст на основе заданного запроса.

**Параметры**:
    - `prompt` (str): Запрос, на основе которого будет сгенерирован текст.
    - `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию `100`.

**Возвращает**:
    - `str`: Сгенерированный текст.

#### `analyze_sentiment`

```python
def analyze_sentiment(self, text) -> str:
    """
    Analyzes the sentiment of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The sentiment analysis result.
    """
```

**Описание**: Анализирует тональность заданного текста.

**Параметры**:
    - `text` (str): Текст для анализа.

**Возвращает**:
    - `str`: Результат анализа тональности.

#### `translate_text`

```python
def translate_text(self, text, source_language, target_language) -> str:
    """
    Translates the given text from the source language to the target language.

    Args:
        text (str): The text to translate.
        source_language (str): The source language code.
        target_language (str): The target language code.

    Returns:
        str: The translated text.
    """
```

**Описание**: Переводит текст с исходного языка на целевой язык.

**Параметры**:
    - `text` (str): Текст для перевода.
    - `source_language` (str): Код исходного языка.
    - `target_language` (str): Код целевого языка.

**Возвращает**:
    - `str`: Переведенный текст.

## Пример использования

Пример использования класса `ClaudeClient` для генерации текста, анализа тональности и перевода текста.

```python
if __name__ == "__main__":
    api_key = "your-api-key"
    claude_client = ClaudeClient(api_key)

    # Пример генерации текста
    prompt = "Write a short story about a robot learning to love."
    generated_text = claude_client.generate_text(prompt)
    print("Generated Text:", generated_text)

    # Пример анализа тональности
    text_to_analyze = "I am very happy today!"
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print("Sentiment Analysis:", sentiment_analysis)

    # Пример перевода текста
    text_to_translate = "Hello, how are you?"
    source_language = "en"
    target_language = "es"
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print("Translated Text:", translated_text)
```
**Описание**: Пример демонстрирует, как создать экземпляр класса `ClaudeClient` и использовать его методы для генерации текста, анализа тональности и перевода. Необходимо заменить `"your-api-key"` на реальный API-ключ.