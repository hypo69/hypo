# Claude Anthropic Client

## Обзор

Этот модуль Python предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает основные функции для генерации текста, анализа тональности и перевода текста.

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

## Подобней

Этот файл `README.md` предоставляет информацию о модуле `Claude Anthropic Client`, который облегчает взаимодействие с языковой моделью Claude от Anthropic. Он объясняет, как установить модуль, как его использовать для генерации текста, анализа тональности и перевода текста, а также предоставляет примеры кода и описание доступных методов. Этот модуль может быть полезен в проектах, где требуется интеграция с языковыми моделями для выполнения различных задач обработки естественного языка.

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

**Как работает функция**:
Функция `generate_text` принимает запрос (`prompt`) и максимальное количество токенов для генерации (`max_tokens_to_sample`). Она использует языковую модель Claude для создания текста на основе запроса и возвращает сгенерированный текст.

- **Параметры:**
  - `prompt`: Запрос для генерации текста.
  - `max_tokens_to_sample`: Максимальное количество токенов для генерации.
- **Возвращает:** Сгенерированный текст.

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Как работает функция**:
Функция `analyze_sentiment` принимает текст (`text`) и анализирует его тональность. Она использует языковую модель Claude для определения тональности текста и возвращает результат анализа.

- **Параметры:**
  - `text`: Текст для анализа.
- **Возвращает:** Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с исходного языка на целевой язык.

**Как работает функция**:
Функция `translate_text` принимает текст (`text`), код исходного языка (`source_language`) и код целевого языка (`target_language`). Она использует языковую модель Claude для перевода текста с исходного языка на целевой язык и возвращает переведенный текст.

- **Параметры:**
  - `text`: Текст для перевода.
  - `source_language`: Код исходного языка.
  - `target_language`: Код целевого языка.
- **Возвращает:** Переведенный текст.

## Вклад

Вклады приветствуются! Не стесняйтесь отправлять pull request или открывать issue, если у вас возникнут какие-либо проблемы или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш фактический ключ API Anthropic.