# Claude Anthropic Client

## Обзор

Этот Python-модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает базовые функции для генерации текста, анализа тональности и перевода текста.

## Установка

Для использования этого модуля необходимо установить библиотеку `anthropic`:

```bash
pip install anthropic
```

## Использование

### Инициализация

Сначала инициализируйте `ClaudeClient` с вашим API-ключом Anthropic:

```python
from claude_client import ClaudeClient

api_key = "ваш-ключ-api"
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Генерирует текст на основе заданного запроса:

```python
prompt = "Напишите короткий рассказ о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)
```

### Анализ тональности

Анализирует тональность заданного текста:

```python
текст_для_анализа = "Сегодня я очень счастлив!"
анализ_тональности = claude_client.analyze_sentiment(текст_для_анализа)
print("Анализ тональности:", анализ_тональности)
```

### Перевод текста

Переводит текст из одного языка в другой:

```python
текст_для_перевода = "Привет, как дела?"
исходный_язык = "ru"
целевой_язык = "en"
переведенный_текст = claude_client.translate_text(текст_для_перевода, исходный_язык, целевой_язык)
print("Переведенный текст:", переведенный_текст)
```

## Пример кода

Вот полный пример использования `ClaudeClient`:

```python
from claude_client import ClaudeClient

api_key = "ваш-ключ-api"
claude_client = ClaudeClient(api_key)

# Генерация текста
prompt = "Напишите короткий рассказ о роботе, который учится любить."
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

Генерирует текст на основе заданного запроса.

- **Параметры:**
    - `prompt` (str): Запрос для генерации текста.
    - `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

- **Возвращает:** (str): Сгенерированный текст.

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

- **Параметры:**
    - `text` (str): Текст для анализа.

- **Возвращает:** (dict): Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

Переводит заданный текст из исходного языка на целевой.

- **Параметры:**
    - `text` (str): Текст для перевода.
    - `source_language` (str): Код исходного языка.
    - `target_language` (str): Код целевого языка.

- **Возвращает:** (str): Переведенный текст.


## Вклад

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован по MIT. Подробности см. в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"ваш-ключ-api"` своим фактическим API-ключом Anthropic.
```