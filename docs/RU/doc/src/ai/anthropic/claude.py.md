# Модуль `claude`

## Обзор

Модуль `claude.py` предоставляет класс `ClaudeClient` для взаимодействия с API Anthropic Claude. Он позволяет генерировать текст, анализировать тональность и переводить текст между различными языками.

## Оглавление

- [Классы](#классы)
    - [`ClaudeClient`](#claudeclient)
- [Пример использования](#пример-использования)

## Классы

### `ClaudeClient`

**Описание**: Класс для взаимодействия с API Anthropic Claude.

**Методы**:
- `__init__`: Инициализирует клиент Claude с заданным API-ключом.
- `generate_text`: Генерирует текст на основе заданного запроса.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `translate_text`: Переводит текст с исходного языка на целевой.

#### `__init__`

**Описание**: Инициализирует клиент Claude с заданным API-ключом.

**Параметры**:
- `api_key` (str): API-ключ для доступа к Anthropic Claude.

**Возвращает**:
- `None`: Метод не возвращает значения.

#### `generate_text`

**Описание**: Генерирует текст на основе заданного запроса.

**Параметры**:
- `prompt` (str): Запрос, на основе которого будет генерироваться текст.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию `100`.

**Возвращает**:
- `str`: Сгенерированный текст.

#### `analyze_sentiment`

**Описание**: Анализирует тональность заданного текста.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

#### `translate_text`

**Описание**: Переводит текст с исходного языка на целевой.

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