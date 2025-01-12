# Документация модуля Claude Anthropic Client

## Оглавление

1.  [Обзор](#обзор)
2.  [Установка](#установка)
3.  [Использование](#использование)
    *   [Инициализация](#инициализация)
    *   [Генерация текста](#генерация-текста)
    *   [Анализ тональности](#анализ-тональности)
    *   [Перевод текста](#перевод-текста)
4.  [Пример кода](#пример-кода)
5.  [Методы](#методы)
    *   [`generate_text`](#generate_textprompt-max_tokens_to_sample100)
    *   [`analyze_sentiment`](#analyze_sentimenttext)
    *   [`translate_text`](#translate_texttext-source_language-target_language)
6.  [Участие](#участие)
7.  [Лицензия](#лицензия)

## Обзор

Этот модуль Python предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает основные функции для генерации текста, анализа тональности и перевода текста.

## Установка

Для использования этого модуля вам необходимо установить библиотеку `anthropic`:

```bash
pip install anthropic
```

## Использование

### Инициализация

Сначала инициализируйте `ClaudeClient` вашим ключом API Anthropic:

```python
from claude_client import ClaudeClient

api_key = "your-api-key"
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Сгенерируйте текст на основе заданного запроса:

```python
prompt = "Напиши короткий рассказ о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)
```

### Анализ тональности

Проанализируйте тональность заданного текста:

```python
text_to_analyze = "Я сегодня очень счастлив!"
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
prompt = "Напиши короткий рассказ о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)

# Анализ тональности
text_to_analyze = "Я сегодня очень счастлив!"
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

Генерирует текст на основе заданного запроса.

**Параметры**:
-   `prompt` (str): Запрос для генерации текста.
-   `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

**Возвращает**:
-   `str`: Сгенерированный текст.

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Параметры**:
-   `text` (str): Текст для анализа.

**Возвращает**:
-   `str`: Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с исходного языка на целевой.

**Параметры**:
-   `text` (str): Текст для перевода.
-   `source_language` (str): Код исходного языка.
-   `target_language` (str): Код целевого языка.

**Возвращает**:
-   `str`: Переведенный текст.

## Участие

Приветствуются любые вклады! Не стесняйтесь отправлять запросы на внесение изменений (pull request) или открывать issue, если вы столкнулись с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш фактический ключ API Anthropic.