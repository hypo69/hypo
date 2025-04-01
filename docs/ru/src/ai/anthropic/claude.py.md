# Модуль для работы с Claude API
================================

Модуль содержит класс `ClaudeClient`, который предоставляет интерфейс для взаимодействия с API Claude для генерации текста, анализа тональности и перевода текста.

[Документация](https://github.com/hypo69/hypo/blob/master/docs/ru/src/ai/anthropic/claude.py.md)

## Оглавление
- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [ClaudeClient](#claudeclient)
- [Примеры использования](#примеры-использования)

## Обзор

Модуль `claude.py` предоставляет класс `ClaudeClient` для взаимодействия с API Claude. Он позволяет генерировать текст на основе запроса, анализировать тональность текста и переводить текст с одного языка на другой. Модуль использует библиотеку `anthropic` для взаимодействия с API Claude.

## Подробнее

Этот модуль предназначен для упрощения работы с API Claude, предоставляя удобный интерфейс для выполнения основных задач, таких как генерация текста, анализ тональности и перевод. Класс `ClaudeClient` инкапсулирует логику взаимодействия с API Claude, что позволяет разработчикам легко интегрировать функциональность Claude в свои приложения.

## Классы

### `ClaudeClient`

**Описание**: Класс для взаимодействия с API Claude.

**Принцип работы**:
1.  При инициализации класса создается клиент `anthropic.Client` с использованием переданного API-ключа.
2.  Методы класса используют этот клиент для выполнения запросов к API Claude.

**Атрибуты**:
- `client` (anthropic.Client): Клиент для взаимодействия с API Claude.

**Методы**:
- `__init__(self, api_key: str) -> None`: Инициализирует клиент Claude с предоставленным API-ключом.
- `generate_text(self, prompt: str, max_tokens_to_sample: int = 100) -> str`: Генерирует текст на основе предоставленного запроса.
- `analyze_sentiment(self, text: str) -> str`: Анализирует тональность предоставленного текста.
- `translate_text(self, text: str, source_language: str, target_language: str) -> str`: Переводит предоставленный текст с исходного языка на целевой язык.

#### `__init__`
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
**Назначение**: Инициализация экземпляра класса `ClaudeClient`.

**Параметры**:
- `api_key` (str): API-ключ для доступа к сервисам Claude.

**Как работает функция**:
1.  Принимает API-ключ в качестве аргумента.
2.  Создает экземпляр класса `anthropic.Client` с использованием переданного API-ключа и присваивает его атрибуту `self.client`.

**Примеры**:
```python
claude_client = ClaudeClient('your_api_key')
```
#### `generate_text`
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
**Назначение**: Генерация текста на основе предоставленного запроса с использованием API Claude.

**Параметры**:
- `prompt` (str): Запрос для генерации текста.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

**Возвращает**:
- `str`: Сгенерированный текст.

**Как работает функция**:

1.  Принимает запрос (`prompt`) и максимальное количество токенов (`max_tokens_to_sample`) в качестве аргументов.
2.  Вызывает метод `completion` клиента `anthropic.Client` для генерации текста на основе запроса.
3.  Извлекает сгенерированный текст из ответа API Claude и возвращает его.

```
Запрос --> Вызов API Claude (completion) --> Получение ответа --> Извлечение текста
```

**Примеры**:
```python
claude_client.generate_text('Write a short story.')
```
#### `analyze_sentiment`
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
**Назначение**: Анализ тональности предоставленного текста с использованием API Claude.

**Параметры**:
- `text` (str): Текст для анализа.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:

1.  Принимает текст для анализа (`text`) в качестве аргумента.
2.  Формирует запрос к API Claude с инструкцией проанализировать тональность текста.
3.  Вызывает метод `completion` клиента `anthropic.Client` для выполнения запроса.
4.  Извлекает результат анализа тональности из ответа API Claude и возвращает его.

```
Текст --> Формирование запроса --> Вызов API Claude (completion) --> Получение ответа --> Извлечение результата
```

**Примеры**:
```python
claude_client.analyze_sentiment('I am very happy!')
```
#### `translate_text`
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
**Назначение**: Перевод текста с одного языка на другой с использованием API Claude.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:

1.  Принимает текст для перевода (`text`), код исходного языка (`source_language`) и код целевого языка (`target_language`) в качестве аргументов.
2.  Формирует запрос к API Claude с инструкцией перевести текст с исходного языка на целевой язык.
3.  Вызывает метод `completion` клиента `anthropic.Client` для выполнения запроса.
4.  Извлекает переведенный текст из ответа API Claude и возвращает его.

```
Текст, исходный язык, целевой язык --> Формирование запроса --> Вызов API Claude (completion) --> Получение ответа --> Извлечение переведенного текста
```

**Примеры**:
```python
claude_client.translate_text('Hello', 'en', 'es')
```
## Примеры использования

```python
if __name__ == '__main__':
    api_key = 'your-api-key'
    claude_client = ClaudeClient(api_key)

    # Пример генерации текста
    prompt = 'Write a short story about a robot learning to love.'
    generated_text = claude_client.generate_text(prompt)
    print('Generated Text:', generated_text)

    # Пример анализа тональности
    text_to_analyze = 'I am very happy today!'
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print('Sentiment Analysis:', sentiment_analysis)

    # Пример перевода текста
    text_to_translate = 'Hello, how are you?'
    source_language = 'en'
    target_language = 'es'
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print('Translated Text:', translated_text)
```

**Описание**:
В данном разделе представлен пример использования класса `ClaudeClient`. Вначале создается экземпляр класса `ClaudeClient` с использованием API-ключа. Затем демонстрируется использование методов `generate_text`, `analyze_sentiment` и `translate_text` для выполнения различных задач обработки текста. Результаты выполнения методов выводятся на экран.