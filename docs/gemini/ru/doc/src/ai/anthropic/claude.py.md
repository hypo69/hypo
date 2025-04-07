# Модуль для работы с Claude API
================================

Модуль содержит класс :class:`ClaudeClient`, который используется для взаимодействия с API Claude для генерации текста, анализа тональности и перевода текста.

[Документация](https://github.com/hypo69/hypo/blob/master/docs/ru/src/ai/anthropic/claude.py.md)

## Оглавление
- [Обзор](#обзор)
- [Классы](#классы)
    - [ClaudeClient](#claudeclient)
- [Пример использования](#пример-использования)

## Обзор

Этот модуль предоставляет класс `ClaudeClient` для взаимодействия с API Claude. Он включает в себя методы для генерации текста на основе запроса, анализа тональности текста и перевода текста между языками.

## Классы

### `ClaudeClient`

**Описание**:
Класс `ClaudeClient` инкапсулирует логику взаимодействия с API Claude.

**Принцип работы**:
Класс инициализируется с API-ключом, который используется для аутентификации при запросах к API Claude. Он предоставляет методы для генерации текста, анализа тональности и перевода текста.

**Аттрибуты**:
- `client` (anthropic.Client): Клиент для взаимодействия с API Claude.

**Методы**:
- `__init__(api_key: str) -> None`: Инициализирует клиент Claude с предоставленным API-ключом.
- `generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str`: Генерирует текст на основе предоставленного запроса.
- `analyze_sentiment(text: str) -> str`: Анализирует тональность предоставленного текста.
- `translate_text(text: str, source_language: str, target_language: str) -> str`: Переводит предоставленный текст с исходного языка на целевой язык.

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
    ...
```

**Назначение**:
Инициализирует экземпляр класса `ClaudeClient` с использованием предоставленного API-ключа.

**Параметры**:
- `api_key` (str): API-ключ, необходимый для аутентификации и авторизации при использовании сервисов Claude.

**Как работает функция**:
1.  Принимает API-ключ в качестве аргумента.
2.  Создает экземпляр клиента `anthropic.Client` с использованием предоставленного API-ключа.
3.  Сохраняет экземпляр клиента в атрибуте `self.client` для дальнейшего использования.

```
A[Прием API-ключа]
|
B[Создание экземпляра клиента anthropic.Client]
|
C[Сохранение экземпляра клиента в self.client]
```

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
    ...
```

**Назначение**:
Генерирует текст, используя API Claude на основе предоставленного запроса.

**Параметры**:
- `prompt` (str): Запрос, на основе которого генерируется текст.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов, которое должно быть сгенерировано. По умолчанию 100.

**Возвращает**:
- `str`: Сгенерированный текст.

**Как работает функция**:
1.  Принимает запрос (`prompt`) и максимальное количество токенов (`max_tokens_to_sample`) в качестве аргументов.
2.  Вызывает метод `completion` клиента `anthropic.Client` с предоставленными параметрами.
3.  Извлекает сгенерированный текст из ответа и возвращает его.

```
A[Прием запроса и максимального количества токенов]
|
B[Вызов метода completion клиента anthropic.Client]
|
C[Извлечение сгенерированного текста из ответа]
|
D[Возврат сгенерированного текста]
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
    ...
```

**Назначение**:
Анализирует тональность предоставленного текста с использованием API Claude.

**Параметры**:
- `text` (str): Текст, который необходимо проанализировать на предмет тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1.  Принимает текст (`text`) в качестве аргумента.
2.  Формирует запрос для анализа тональности, включая предоставленный текст.
3.  Вызывает метод `completion` клиента `anthropic.Client` с сформированным запросом.
4.  Извлекает результат анализа тональности из ответа и возвращает его.

```
A[Прием текста для анализа]
|
B[Формирование запроса для анализа тональности]
|
C[Вызов метода completion клиента anthropic.Client]
|
D[Извлечение результата анализа тональности из ответа]
|
E[Возврат результата анализа тональности]
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
    ...
```

**Назначение**:
Переводит предоставленный текст с исходного языка на целевой язык с использованием API Claude.

**Параметры**:
- `text` (str): Текст, который необходимо перевести.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1.  Принимает текст (`text`), код исходного языка (`source_language`) и код целевого языка (`target_language`) в качестве аргументов.
2.  Формирует запрос для перевода текста с указанием исходного и целевого языков.
3.  Вызывает метод `completion` клиента `anthropic.Client` с сформированным запросом.
4.  Извлекает переведенный текст из ответа и возвращает его.

```
A[Прием текста, кода исходного и целевого языков]
|
B[Формирование запроса для перевода текста]
|
C[Вызов метода completion клиента anthropic.Client]
|
D[Извлечение переведенного текста из ответа]
|
E[Возврат переведенного текста]
```

**Примеры**:
```python
claude_client.translate_text('Hello', 'en', 'es')
```

## Пример использования

В блоке `if __name__ == '__main__':` демонстрируется пример использования класса `ClaudeClient`. Он включает в себя создание экземпляра класса, генерацию текста, анализ тональности и перевод текста.
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