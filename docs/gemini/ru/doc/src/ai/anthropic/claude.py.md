# Модуль `claude.py`

## Обзор

Модуль `claude.py` предоставляет клиент для взаимодействия с API Anthropic Claude. Он включает в себя класс `ClaudeClient` с методами для генерации текста, анализа тональности и перевода текста.

## Оглавление

1.  [Классы](#классы)
    -   [`ClaudeClient`](#claudeclient)
2.  [Пример использования](#пример-использования)

## Классы

### `ClaudeClient`

**Описание**:
Класс для взаимодействия с API Anthropic Claude.

**Методы**:

*   `__init__(self, api_key)`:
    -   **Описание**: Инициализирует клиент Anthropic Claude с заданным API ключом.
    -   **Параметры**:
        -   `api_key` (str): API ключ для доступа к Anthropic Claude.
    
*   `generate_text(self, prompt, max_tokens_to_sample=100)`:
    -   **Описание**: Генерирует текст на основе заданного промпта.
    -   **Параметры**:
        -   `prompt` (str): Текст промпта для генерации.
        -   `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.
    -   **Возвращает**:
        -   `str`: Сгенерированный текст.

*   `analyze_sentiment(self, text)`:
    -   **Описание**: Анализирует тональность заданного текста.
    -   **Параметры**:
        -   `text` (str): Текст для анализа тональности.
    -   **Возвращает**:
        -   `str`: Результат анализа тональности.

*   `translate_text(self, text, source_language, target_language)`:
    -   **Описание**: Переводит текст с исходного языка на целевой.
    -   **Параметры**:
        -   `text` (str): Текст для перевода.
        -   `source_language` (str): Код исходного языка.
        -   `target_language` (str): Код целевого языка.
    -   **Возвращает**:
        -   `str`: Переведенный текст.

## Пример использования

В блоке `if __name__ == "__main__":` представлен пример использования класса `ClaudeClient`:

1.  Создается экземпляр класса `ClaudeClient` с API ключом (замените `"your-api-key"` на ваш фактический API ключ).
2.  Демонстрируется генерация текста на основе промпта.
3.  Показывается анализ тональности заданного текста.
4.  Представлен пример перевода текста с одного языка на другой.

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