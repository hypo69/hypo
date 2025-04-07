# Документация модуля `src.ai.anthropic`

## Обзор

Модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает в себя основные функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Этот модуль позволяет интегрировать возможности Claude AI в ваши Python-приложения. Для работы требуется установить библиотеку `anthropic` и получить API-ключ.

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

Для использования этого модуля необходимо установить библиотеку `anthropic`:

```bash
pip install anthropic
```

## Использование

### Инициализация

Сначала инициализируйте `ClaudeClient` с вашим Anthropic API-ключом:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Генерируйте текст на основе заданного промпта:

```python
prompt = "Напиши короткий рассказ о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)
```

### Анализ тональности

Анализируйте тональность заданного текста:

```python
text_to_analyze = "Я сегодня очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)
```

### Перевод текста

Переводите текст с одного языка на другой:

```python
text_to_translate = "Привет, как дела?"
source_language = "en"
target_language = "es"
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
prompt = "Напиши короткий рассказ о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)

# Анализ тональности
text_to_analyze = "Я сегодня очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)

# Перевод текста
text_to_translate = "Привет, как дела?"
source_language = "en"
target_language = "es"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```

## Методы

### `generate_text(prompt, max_tokens_to_sample=100)`

Генерирует текст на основе заданного промпта.

**Параметры:**
- `prompt` (str): Промпт для генерации текста.
- `max_tokens_to_sample` (int): Максимальное количество токенов для генерации (по умолчанию 100).

**Возвращает:**
- `str`: Сгенерированный текст.

**Как работает функция:**
1. Функция принимает текстовый запрос `prompt` и максимальное количество токенов `max_tokens_to_sample` для генерации.
2. Использует API Claude для генерации текста на основе предоставленного промпта.
3. Возвращает сгенерированный текст.

```
Prompt --> Claude API --> Generated Text
```

**Примеры:**

```python
prompt = "Напиши короткое стихотворение о любви."
generated_text = claude_client.generate_text(prompt)
print(generated_text)
```

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Параметры:**
- `text` (str): Текст для анализа.

**Возвращает:**
- `str`: Результат анализа тональности.

**Как работает функция:**
1. Функция принимает текст `text` для анализа тональности.
2. Использует API Claude для анализа тональности предоставленного текста.
3. Возвращает результат анализа тональности.

```
Text --> Claude API --> Sentiment Analysis Result
```

**Примеры:**

```python
text = "Этот фильм был просто потрясающим!"
sentiment = claude_client.analyze_sentiment(text)
print(sentiment)
```

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с исходного языка на целевой язык.

**Параметры:**
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает:**
- `str`: Переведенный текст.

**Как работает функция:**
1. Функция принимает текст `text`, код исходного языка `source_language` и код целевого языка `target_language`.
2. Использует API Claude для перевода текста с указанного исходного языка на целевой язык.
3. Возвращает переведенный текст.

```
Text, Source Language, Target Language --> Claude API --> Translated Text
```

**Примеры:**

```python
text = "Hello, world!"
source_language = "en"
target_language = "fr"
translated_text = claude_client.translate_text(text, source_language, target_language)
print(translated_text)
```

## Вклад

Приветствуются вклады! Не стесняйтесь отправлять pull request или открывать issue, если у вас возникнут какие-либо проблемы или предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш фактический Anthropic API-ключ.