# Клиент для модели Claude от Anthropic

## Обзор

Этот Python-модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает базовые функции для генерации текста, анализа тональности и перевода текста.

## Оглавление

1. [Установка](#Установка)
2. [Использование](#Использование)
    - [Инициализация](#Инициализация)
    - [Генерация текста](#Генерация-текста)
    - [Анализ тональности](#Анализ-тональности)
    - [Перевод текста](#Перевод-текста)
3. [Пример кода](#Пример-кода)
4. [Методы](#Методы)
    - [`generate_text`](#generate_textprompt-max_tokens_to_sample100)
    - [`analyze_sentiment`](#analyze_sentimenttext)
    - [`translate_text`](#translate_texttext-source_language-target_language)
5. [Вклад](#Вклад)
6. [Лицензия](#Лицензия)

## Установка

Для использования этого модуля вам необходимо установить библиотеку `anthropic`:

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

**Описание**: Генерирует текст на основе заданного промпта.

**Параметры**:
- `prompt` (str): Промпт для генерации текста.
- `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию `100`.

**Возвращает**:
- `str`: Сгенерированный текст.

### `analyze_sentiment(text)`

**Описание**: Анализирует тональность заданного текста.

**Параметры**:
- `text` (str): Текст для анализа.

**Возвращает**:
- `str`: Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

**Описание**: Переводит заданный текст с одного языка на другой.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Код исходного языка.
- `target_language` (str): Код целевого языка.

**Возвращает**:
- `str`: Переведенный текст.

## Вклад

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или имеете предложения по улучшению.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш реальный API-ключ от Anthropic.