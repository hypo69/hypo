# Модуль `src.ai.anthropic`

## Обзор

Этот модуль предоставляет клиент для взаимодействия с языковой моделью Claude от Anthropic. Он включает в себя функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Этот модуль облегчает интеграцию с моделью Claude от Anthropic, предоставляя готовые методы для выполнения различных задач обработки текста. Модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает базовые функции для генерации текста, анализа тональности и перевода текста.

## Установка

Для использования этого модуля необходимо установить библиотеку `anthropic`:

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

**Как работает функция:**
Функция принимает промпт и максимальное количество токенов для генерации. Затем она отправляет запрос к модели Claude и возвращает сгенерированный текст.

**Параметры:**
- `prompt`: Промпт для генерации текста.
- `max_tokens_to_sample`: Максимальное количество токенов для генерации.

**Возвращает:**
- Сгенерированный текст.

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Как работает функция:**
Функция принимает текст для анализа и отправляет запрос к модели Claude для анализа тональности. Она возвращает результат анализа тональности.

**Параметры:**
- `text`: Текст для анализа.

**Возвращает:**
- Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с одного языка на другой.

**Как работает функция:**
Функция принимает текст для перевода, код исходного языка и код целевого языка. Затем она отправляет запрос к модели Claude для перевода текста и возвращает переведенный текст.

**Параметры:**
- `text`: Текст для перевода.
- `source_language`: Код исходного языка.
- `target_language`: Код целевого языка.

**Возвращает:**
- Переведенный текст.

## Вклад

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или имеете предложения по улучшению.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш реальный API-ключ от Anthropic.