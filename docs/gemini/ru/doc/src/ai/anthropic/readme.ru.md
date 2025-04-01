# Документация для модуля `src.ai.anthropic`

## Обзор

Этот модуль представляет собой клиент для взаимодействия с моделью Claude от Anthropic. Он предоставляет интерфейс для генерации текста, анализа тональности и перевода текста. Модуль предназначен для упрощения работы с API Claude и интеграции его функций в другие проекты.

## Подробней

Модуль `src.ai.anthropic` предоставляет удобный способ использования API Claude от Anthropic для выполнения различных задач обработки текста. Он включает в себя класс `ClaudeClient`, который инкапсулирует логику взаимодействия с API. Для работы с модулем требуется установить библиотеку `anthropic` и получить API-ключ от Anthropic.

## Классы

Здесь описаны классы, используемые в модуле.

### `ClaudeClient`

**Описание**: Класс `ClaudeClient` предоставляет интерфейс для взаимодействия с языковой моделью Claude от Anthropic.

**Принцип работы**:

Класс инициализируется с API-ключом, который используется для аутентификации при запросах к API Claude. Он предоставляет методы для генерации текста на основе заданного промпта, анализа тональности текста и перевода текста с одного языка на другой.

**Аттрибуты**:
- `api_key` (str): API-ключ для доступа к сервисам Anthropic.

**Методы**:
- `generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str`: Генерирует текст на основе заданного промпта.
- `analyze_sentiment(text: str) -> str`: Анализирует тональность заданного текста.
- `translate_text(text: str, source_language: str, target_language: str) -> str`: Переводит текст с одного языка на другой.

## Функции

### `generate_text`

```python
def generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str:
    """Генерирует текст на основе заданного промпта.

    Args:
        prompt (str): Промпт для генерации текста.
        max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

    Returns:
        str: Сгенерированный текст.
    """
    ...
```

**Назначение**: Генерация текста на основе предоставленного промпта с ограничением на максимальное количество токенов.

**Параметры**:
- `prompt` (str): Текст запроса (промпт), на основе которого генерируется текст.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов, которое может быть сгенерировано. По умолчанию равно 100.

**Возвращает**:
- `str`: Сгенерированный текст на основе промпта.

**Как работает функция**:
1. Функция принимает текстовый промпт и максимальное количество токенов для генерации.
2. Используя API Claude, она генерирует текст на основе промпта, ограничивая длину сгенерированного текста количеством токенов, указанным в `max_tokens_to_sample`.
3. Возвращает сгенерированный текст.

**Примеры**:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

prompt = "Напишите короткую историю о кошке."
generated_text = claude_client.generate_text(prompt)
print(generated_text)

prompt = "Сочини стихотворение о любви."
generated_text = claude_client.generate_text(prompt, max_tokens_to_sample=200)
print(generated_text)
```

### `analyze_sentiment`

```python
def analyze_sentiment(text: str) -> str:
    """Анализирует тональность заданного текста.

    Args:
        text (str): Текст для анализа.

    Returns:
        str: Результат анализа тональности.
    """
    ...
```

**Назначение**: Анализ тональности заданного текста.

**Параметры**:
- `text` (str): Текст, который необходимо проанализировать на предмет тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1. Функция принимает текст в качестве входных данных.
2. Используя API Claude, она анализирует тональность текста (например, позитивную, негативную или нейтральную).
3. Возвращает результат анализа тональности.

**Примеры**:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

text = "Сегодня отличный день!"
sentiment = claude_client.analyze_sentiment(text)
print(sentiment)

text = "Я очень расстроен."
sentiment = claude_client.analyze_sentiment(text)
print(sentiment)
```

### `translate_text`

```python
def translate_text(text: str, source_language: str, target_language: str) -> str:
    """Переводит заданный текст с одного языка на другой.

    Args:
        text (str): Текст для перевода.
        source_language (str): Код исходного языка.
        target_language (str): Код целевого языка.

    Returns:
        str: Переведенный текст.
    """
    ...
```

**Назначение**: Перевод текста с одного языка на другой.

**Параметры**:
- `text` (str): Текст, который нужно перевести.
- `source_language` (str): Код языка оригинала текста (например, "en" для английского, "ru" для русского).
- `target_language` (str): Код языка, на который нужно перевести текст (например, "fr" для французского, "de" для немецкого).

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1. Функция принимает текст, код исходного языка и код целевого языка.
2. Используя API Claude, она переводит текст с исходного языка на целевой язык.
3. Возвращает переведенный текст.

**Примеры**:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

text = "Hello, how are you?"
translated_text = claude_client.translate_text(text, "en", "ru")
print(translated_text)

text = "Как дела?"
translated_text = claude_client.translate_text(text, "ru", "de")
print(translated_text)
```