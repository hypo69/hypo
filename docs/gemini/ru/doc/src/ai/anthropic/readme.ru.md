# Клиент для модели Claude от Anthropic

## Обзор

Этот модуль предоставляет интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает функции для генерации текста, анализа тональности и перевода текста.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
  - [Инициализация](#инициализация)
  - [Генерация текста](#генерация-текста)
  - [Анализ тональности](#анализ-тональности)
  - [Перевод текста](#перевод-текста)
- [Пример кода](#пример-кода)
- [Методы](#методы)
  - [`generate_text`](#generate_textprompt-max_tokens_to_sample100)
  - [`analyze_sentiment`](#analyze_sentimenttext)
  - [`translate_text`](#translate_texttext-source_language-target_language)
- [Вклад](#вклад)
- [Лицензия](#лицензия)

## Установка

Для использования модуля необходимо установить библиотеку `anthropic`:

```bash
pip install anthropic
```

## Использование

### Инициализация

Инициализируйте `ClaudeClient` с вашим API-ключом от Anthropic:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Сгенерируйте текст на основе заданного промпта:

```python
prompt = "Напишите короткую историю о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)
```

### Анализ тональности

Проанализируйте тональность заданного текста:

```python
text_to_analyze = "Сегодня я очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)
```

### Перевод текста

Переведите текст с одного языка на другой:

```python
text_to_translate = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```

## Пример кода

Полный пример использования `ClaudeClient`:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

# Генерация текста
prompt = "Напишите короткую историю о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)

# Анализ тональности
text_to_analyze = "Сегодня я очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)

# Перевод текста
text_to_translate = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```

## Методы

### `generate_text(prompt, max_tokens_to_sample=100)`

**Описание**: Генерирует текст на основе заданного промпта.

**Параметры**:
- `prompt` (str): Промпт для генерации текста.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию `100`.

**Возвращает**:
- `str`: Сгенерированный текст.

```python
def generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str:
    """
    Args:
        prompt (str): Промпт для генерации текста.
        max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

    Returns:
        str: Сгенерированный текст.
    """
    ...
```

**Примеры**:

```python
# Пример вызова функции
prompt = "Напиши стихотворение о весне."
generated_text = claude_client.generate_text(prompt)
print(generated_text)
```

### `analyze_sentiment(text)`

**Описание**: Анализирует тональность заданного текста.

**Параметры**:
- `text` (str): Текст для анализа.

**Возвращает**:
- `str`: Результат анализа тональности.

```python
def analyze_sentiment(text: str) -> str:
    """
    Args:
        text (str): Текст для анализа.

    Returns:
        str: Результат анализа тональности.
    """
    ...
```

**Примеры**:

```python
# Пример вызова функции
text = "Я очень рад видеть тебя!"
sentiment = claude_client.analyze_sentiment(text)
print(sentiment)
```

### `translate_text(text, source_language, target_language)`

**Описание**: Переводит заданный текст с одного языка на другой.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:
- `str`: Переведенный текст.

```python
def translate_text(text: str, source_language: str, target_language: str) -> str:
    """
    Args:
        text (str): Текст для перевода.
        source_language (str): Код исходного языка.
        target_language (str): Код целевого языка.

    Returns:
        str: Переведенный текст.
    """
    ...
```

**Примеры**:

```python
# Пример вызова функции
text = "Hello, how are you?"
source_language = "en"
target_language = "ru"
translated_text = claude_client.translate_text(text, source_language, target_language)
print(translated_text)
```

## Вклад

Вклад приветствуется! Отправляйте pull request или открывайте issue, если вы столкнулись с проблемами или имеете предложения по улучшению.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш реальный API-ключ от Anthropic.