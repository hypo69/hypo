# Документация модуля `src.ai.anthropic`

## Обзор

Данный модуль предоставляет клиент для взаимодействия с моделью Claude от Anthropic. Он включает в себя функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Этот модуль предназначен для упрощения работы с API Claude от Anthropic. Он предоставляет удобный интерфейс для выполнения основных задач, таких как генерация текста на основе промпта, анализ тональности текста и перевод текста между различными языками. Модуль разработан для интеграции в проект `hypotez` и предоставляет инструменты для использования возможностей AI-модели Claude.

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

Сначала инициализируйте `ClaudeClient` с вашим API-ключом от Anthropic:

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

Вот полный пример использования `ClaudeClient`:

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

Генерирует текст на основе заданного промпта.

**Параметры:**
- `prompt` (str): Промпт для генерации текста.
- `max_tokens_to_sample` (int): Максимальное количество токенов для генерации (по умолчанию 100).

**Возвращает:**
- `str`: Сгенерированный текст.

**Как работает функция:**
1. Функция принимает на вход текстовый промпт и максимальное количество токенов для генерации.
2. Использует API Claude для генерации текста на основе заданного промпта и ограничений по количеству токенов.
3. Возвращает сгенерированный текст.

```
A[Промпт]
|
B[Вызов API Claude]
|
C[Возврат сгенерированного текста]
```

**Примеры:**

```python
# Пример генерации текста с использованием промпта
prompt = "Напишите короткий рассказ о кошке, которая умеет говорить."
generated_text = claude_client.generate_text(prompt)
print(generated_text)

# Пример генерации текста с ограничением на количество токенов
prompt = "Составьте список покупок для приготовления пиццы."
generated_text = claude_client.generate_text(prompt, max_tokens_to_sample=50)
print(generated_text)
```

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Параметры:**
- `text` (str): Текст для анализа.

**Возвращает:**
- `str`: Результат анализа тональности.

**Как работает функция:**
1. Функция принимает на вход текст для анализа тональности.
2. Использует API Claude для анализа тональности заданного текста.
3. Возвращает результат анализа тональности.

```
A[Текст для анализа]
|
B[Вызов API Claude для анализа тональности]
|
C[Возврат результата анализа тональности]
```

**Примеры:**

```python
# Пример анализа тональности положительного текста
text = "Я очень рад сегодня!"
sentiment = claude_client.analyze_sentiment(text)
print(sentiment)

# Пример анализа тональности отрицательного текста
text = "Я очень расстроен из-за этой новости."
sentiment = claude_client.analyze_sentiment(text)
print(sentiment)
```

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с одного языка на другой.

**Параметры:**
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает:**
- `str`: Переведенный текст.

**Как работает функция:**
1. Функция принимает на вход текст для перевода, код исходного языка и код целевого языка.
2. Использует API Claude для перевода заданного текста с одного языка на другой.
3. Возвращает переведенный текст.

```
A[Текст для перевода, Исходный язык, Целевой язык]
|
B[Вызов API Claude для перевода]
|
C[Возврат переведенного текста]
```

**Примеры:**

```python
# Пример перевода текста с русского на английский
text = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = claude_client.translate_text(text, source_language, target_language)
print(translated_text)

# Пример перевода текста с английского на французский
text = "Hello, how are you?"
source_language = "en"
target_language = "fr"
translated_text = claude_client.translate_text(text, source_language, target_language)
print(translated_text)
```

## Вклад

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или имеете предложения по улучшению.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш реальный API-ключ от Anthropic.