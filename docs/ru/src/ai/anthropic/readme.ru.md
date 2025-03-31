# Клиент для модели Claude от Anthropic

## Обзор

Этот модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает базовые функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Этот модуль позволяет разработчикам легко интегрировать функциональность Claude в свои проекты. Он предоставляет методы для генерации текста на основе заданных промптов, анализа тональности текста и перевода текста с одного языка на другой.

## Классы

### `ClaudeClient`

**Описание**: Этот класс предоставляет интерфейс для взаимодействия с API Claude от Anthropic.

**Как работает класс**:
Класс `ClaudeClient` инициализируется с API-ключом, необходимым для аутентификации при запросах к API Claude. Он включает методы для генерации текста, анализа тональности и перевода текста. Каждый метод отправляет запрос к API Claude и возвращает результат.

**Методы**:
- `generate_text(prompt, max_tokens_to_sample=100)`: Генерирует текст на основе заданного промпта.
- `analyze_sentiment(text)`: Анализирует тональность заданного текста.
- `translate_text(text, source_language, target_language)`: Переводит текст с одного языка на другой.

**Параметры**:
- `api_key` (str): API-ключ для аутентификации при запросах к API Claude.

**Примеры**
```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)
```

## Функции

### `generate_text(prompt, max_tokens_to_sample=100)`

```python
def generate_text(prompt, max_tokens_to_sample=100):
    """
    Генерирует текст на основе заданного промпта.
    
    Args:
        prompt (str): Промпт для генерации текста.
        max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.
    
    Returns:
        str: Сгенерированный текст.
    """
    ...
```

**Описание**: Генерирует текст на основе заданного промпта, используя API Claude.

**Как работает функция**:
Функция `generate_text` принимает текстовый промпт и максимальное количество токенов для генерации. Она отправляет запрос к API Claude с этими параметрами и возвращает сгенерированный текст.

**Параметры**:
- `prompt` (str): Промпт для генерации текста.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

**Возвращает**:
- `str`: Сгенерированный текст.

**Примеры**:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

prompt = "Напишите короткую историю о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)
```

### `analyze_sentiment(text)`

```python
def analyze_sentiment(text):
    """
    Анализирует тональность заданного текста.
    
    Args:
        text (str): Текст для анализа.
    
    Returns:
        str: Результат анализа тональности.
    """
    ...
```

**Описание**: Анализирует тональность заданного текста, используя API Claude.

**Как работает функция**:
Функция `analyze_sentiment` принимает текст для анализа и отправляет запрос к API Claude. Она возвращает результат анализа тональности, который может быть положительным, отрицательным или нейтральным.

**Параметры**:
- `text` (str): Текст для анализа.

**Возвращает**:
- `str`: Результат анализа тональности.

**Примеры**:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

text_to_analyze = "Сегодня я очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)
```

### `translate_text(text, source_language, target_language)`

```python
def translate_text(text, source_language, target_language):
    """
    Переводит заданный текст с одного языка на другой.
    
    Args:
        text (str): Текст для перевода.
        source_language (str): Код исходного языка.
        target_language (str): Код целевого языка.
    
    Returns:
        str: Переведенный текст.
    """
    ...
```

**Описание**: Переводит заданный текст с одного языка на другой, используя API Claude.

**Как работает функция**:
Функция `translate_text` принимает текст для перевода, код исходного языка и код целевого языка. Она отправляет запрос к API Claude с этими параметрами и возвращает переведенный текст.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:
- `str`: Переведенный текст.

**Примеры**:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

text_to_translate = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```