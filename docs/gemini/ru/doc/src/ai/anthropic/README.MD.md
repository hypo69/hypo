# Документация модуля `src.ai.anthropic`

## Обзор

Этот модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает в себя базовые функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Модуль `src.ai.anthropic` предоставляет интерфейс для работы с API Claude от Anthropic, позволяя выполнять такие задачи, как генерация текста на основе заданного запроса, анализ тональности текста и перевод текста с одного языка на другой. Этот модуль упрощает интеграцию с Claude для выполнения различных задач обработки естественного языка.

## Классы

### `ClaudeClient`

**Описание**: Класс `ClaudeClient` предоставляет методы для взаимодействия с языковой моделью Claude от Anthropic. Он позволяет генерировать текст, анализировать тональность и переводить текст.

**Принцип работы**:
Класс инициализируется с использованием API-ключа Anthropic. Затем он предоставляет методы для выполнения различных операций, таких как генерация текста, анализ тональности и перевод текста, используя API Claude.

**Атрибуты**:
- `api_key` (str): API-ключ для аутентификации в Anthropic.

**Методы**:
- `generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str`: Генерирует текст на основе заданного запроса.
- `analyze_sentiment(text: str) -> str`: Анализирует тональность заданного текста.
- `translate_text(text: str, source_language: str, target_language: str) -> str`: Переводит заданный текст с одного языка на другой.

## Функции

### `generate_text`

```python
def generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str:
    """Генерирует текст на основе заданного запроса.

    Args:
        prompt (str): Запрос для генерации текста.
        max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

    Returns:
        str: Сгенерированный текст.
    """
    ...
```

**Назначение**: Функция `generate_text` генерирует текст на основе предоставленного запроса (`prompt`), используя языковую модель Claude. Максимальное количество токенов, которые должны быть сгенерированы, можно указать с помощью параметра `max_tokens_to_sample`.

**Параметры**:
- `prompt` (str): Запрос, на основе которого генерируется текст.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов, которое может быть сгенерировано. По умолчанию равно 100.

**Возвращает**:
- `str`: Сгенерированный текст на основе предоставленного запроса.

**Как работает функция**:
1.  Функция принимает запрос `prompt` и максимальное количество токенов `max_tokens_to_sample`.
2.  Запрос передается языковой модели Claude, которая генерирует текст на основе запроса.
3.  Сгенерированный текст возвращается.

```
Запрос -> Claude -> Сгенерированный текст
```

**Примеры**:

```python
# Пример генерации текста с использованием запроса
prompt = "Напиши короткий рассказ о коте, который учится летать."
generated_text = claude_client.generate_text(prompt)
print(generated_text)

# Пример генерации текста с ограничением на количество токенов
prompt = "Напиши короткое стихотворение о звездах."
generated_text = claude_client.generate_text(prompt, max_tokens_to_sample=50)
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

**Назначение**: Функция `analyze_sentiment` анализирует тональность предоставленного текста (`text`), используя языковую модель Claude.

**Параметры**:
- `text` (str): Текст, который необходимо проанализировать.

**Возвращает**:
- `str`: Результат анализа тональности текста.

**Как работает функция**:
1.  Функция принимает текст `text` для анализа.
2.  Текст передается языковой модели Claude, которая анализирует тональность текста.
3.  Результат анализа тональности возвращается.

```
Текст -> Claude -> Анализ тональности
```

**Примеры**:

```python
# Пример анализа тональности положительного текста
text_to_analyze = "Я очень счастлив сегодня!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print(sentiment_analysis)

# Пример анализа тональности отрицательного текста
text_to_analyze = "Я очень расстроен из-за этой новости."
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print(sentiment_analysis)
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

**Назначение**: Функция `translate_text` переводит предоставленный текст (`text`) с исходного языка (`source_language`) на целевой язык (`target_language`), используя языковую модель Claude.

**Параметры**:
- `text` (str): Текст, который необходимо перевести.
- `source_language` (str): Код исходного языка (например, "en" для английского).
- `target_language` (str): Код целевого языка (например, "es" для испанского).

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1.  Функция принимает текст `text`, код исходного языка `source_language` и код целевого языка `target_language`.
2.  Текст и коды языков передаются языковой модели Claude, которая переводит текст.
3.  Переведенный текст возвращается.

```
Текст, Исходный язык, Целевой язык -> Claude -> Переведенный текст
```

**Примеры**:

```python
# Пример перевода текста с английского на испанский
text_to_translate = "Hello, how are you?"
source_language = "en"
target_language = "es"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print(translated_text)

# Пример перевода текста с французского на английский
text_to_translate = "Bonjour, comment allez-vous?"
source_language = "fr"
target_language = "en"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print(translated_text)
```