# Claude Anthropic Client

## Обзор

Этот Python-модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает основные функции для генерации текста, анализа тональности и перевода текста.

## Оглавление

1.  [Установка](#установка)
2.  [Использование](#использование)
    *   [Инициализация](#инициализация)
    *   [Генерация текста](#генерация-текста)
    *   [Анализ тональности](#анализ-тональности)
    *   [Перевод текста](#перевод-текста)
3.  [Пример кода](#пример-кода)
4.  [Методы](#методы)
    *   [`generate_text(prompt, max_tokens_to_sample=100)`](#generate_textprompt-max_tokens_to_sample100)
    *   [`analyze_sentiment(text)`](#analyze_sentimenttext)
    *   [`translate_text(text, source_language, target_language)`](#translate_texttext-source_language-target_language)
5.  [Вклад](#вклад)
6.  [Лицензия](#лицензия)

## Установка

Для использования этого модуля вам необходимо установить библиотеку `anthropic`:

```bash
pip install anthropic
```

## Использование

### Инициализация

Сначала инициализируйте `ClaudeClient` с вашим ключом API Anthropic:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Сгенерируйте текст на основе заданного запроса:

```python
prompt = "Write a short story about a robot learning to love."
generated_text = claude_client.generate_text(prompt)
print("Generated Text:", generated_text)
```

### Анализ тональности

Проанализируйте тональность заданного текста:

```python
text_to_analyze = "I am very happy today!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Sentiment Analysis:", sentiment_analysis)
```

### Перевод текста

Переведите текст с одного языка на другой:

```python
text_to_translate = "Hello, how are you?"
source_language = "en"
target_language = "es"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Translated Text:", translated_text)
```

## Пример кода

Вот полный пример использования `ClaudeClient`:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)

# Generate text
prompt = "Write a short story about a robot learning to love."
generated_text = claude_client.generate_text(prompt)
print("Generated Text:", generated_text)

# Analyze sentiment
text_to_analyze = "I am very happy today!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Sentiment Analysis:", sentiment_analysis)

# Translate text
text_to_translate = "Hello, how are you?"
source_language = "en"
target_language = "es"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Translated Text:", translated_text)
```

## Методы

### `generate_text(prompt, max_tokens_to_sample=100)`

Генерирует текст на основе заданного запроса.

**Параметры**:

- `prompt` (str): Запрос для генерации текста.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию `100`.

**Возвращает**:

- `str`: Сгенерированный текст.

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Параметры**:

- `text` (str): Текст для анализа.

**Возвращает**:

- `str`: Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с исходного языка на целевой.

**Параметры**:

- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:

- `str`: Переведенный текст.

## Вклад

Вклады приветствуются! Не стесняйтесь отправлять запросы на внесение изменений или открывать issue, если вы столкнулись с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для получения подробной информации.

---

**Примечание:** Замените `"your-api-key"` на ваш фактический ключ API Anthropic.