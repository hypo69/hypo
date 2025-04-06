# Документация модуля `src.ai.anthropic`

## Обзор

Этот модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает в себя основные функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Этот модуль позволяет легко интегрировать возможности Claude в ваши Python-приложения. Он предоставляет удобные функции для выполнения распространенных задач обработки текста.

## Установка

Для использования этого модуля необходимо установить библиотеку `anthropic`:

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

Вот полный пример того, как использовать `ClaudeClient`:

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

### `generate_text(prompt: str, max_tokens_to_sample: int = 100) -> str`

Генерирует текст на основе заданного запроса.

**Параметры**:
- `prompt` (str): Запрос, на основе которого генерируется текст.
- `max_tokens_to_sample` (int): Максимальное количество токенов для генерации. По умолчанию 100.

**Возвращает**:
- `str`: Сгенерированный текст.

**Как работает функция**:
1. Функция принимает текстовый запрос `prompt` и максимальное количество токенов `max_tokens_to_sample`.
2. Использует API Claude для генерации текста на основе запроса.
3. Возвращает сгенерированный текст.

```
Запрос 
   prompt, max_tokens_to_sample
   |
   | Использование API Claude
   |
   Сгенерированный текст
```

**Примеры**:

```python
# Пример генерации текста с запросом и ограничением на количество токенов
generated_text = claude_client.generate_text("Напиши короткий рассказ о коте", max_tokens_to_sample=50)
print(generated_text)

# Пример генерации текста только с запросом
generated_text = claude_client.generate_text("Напиши стихотворение о весне")
print(generated_text)
```

### `analyze_sentiment(text: str) -> str`

Анализирует тональность заданного текста.

**Параметры**:
- `text` (str): Текст для анализа.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1. Функция принимает текстовую строку `text`.
2. Использует API Claude для анализа тональности текста.
3. Возвращает результат анализа тональности.

```
Текст для анализа 
   text
   |
   | Использование API Claude
   |
   Результат анализа тональности
```

**Примеры**:

```python
# Пример анализа тональности положительного текста
sentiment_analysis = claude_client.analyze_sentiment("Я очень счастлив сегодня!")
print(sentiment_analysis)

# Пример анализа тональности отрицательного текста
sentiment_analysis = claude_client.analyze_sentiment("Я очень расстроен из-за этой новости.")
print(sentiment_analysis)
```

### `translate_text(text: str, source_language: str, target_language: str) -> str`

Переводит заданный текст с исходного языка на целевой язык.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1. Функция принимает текст `text`, код исходного языка `source_language` и код целевого языка `target_language`.
2. Использует API Claude для перевода текста.
3. Возвращает переведенный текст.

```
Текст, Исходный язык, Целевой язык
   text, source_language, target_language
   |
   | Использование API Claude
   |
   Переведенный текст
```

**Примеры**:

```python
# Пример перевода текста с английского на испанский
translated_text = claude_client.translate_text("Hello, how are you?", "en", "es")
print(translated_text)

# Пример перевода текста с французского на английский
translated_text = claude_client.translate_text("Bonjour, comment allez-vous?", "fr", "en")
print(translated_text)
```

## Вклад

Вклад приветствуется! Не стесняйтесь отправлять запросы на включение изменений или открывать проблему, если вы столкнулись с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` своим фактическим ключом API Anthropic.