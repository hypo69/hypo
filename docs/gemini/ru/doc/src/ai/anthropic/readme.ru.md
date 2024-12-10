# Клиент для модели Claude от Anthropic

## Оглавление

- [Установка](#установка)
- [Использование](#использование)
- [Методы](#методы)
    - [`generate_text`](#generate_text)
    - [`analyze_sentiment`](#analyze_sentiment)
    - [`translate_text`](#translate_text)
- [Пример кода](#пример-кода)
- [Вклад](#вклад)
- [Лицензия](#лицензия)


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

api_key = "your-api-key"  # Замените на ваш ключ
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Сгенерируйте текст на основе заданного промпта:

```python
from claude_client import ClaudeClient

def generate_text(prompt, max_tokens_to_sample=100) -> str:
    """
    Генерирует текст на основе заданного промпта.

    Args:
        prompt (str): Промпт для генерации текста.
        max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

    Returns:
        str: Сгенерированный текст.
    """
    
    try:
        return claude_client.generate_text(prompt, max_tokens_to_sample=max_tokens_to_sample)
    except Exception as ex:
      raise Exception(f"Ошибка при генерации текста: {ex}")
  

prompt = "Напишите короткую историю о роботе, который учится любить."
generated_text = generate_text(prompt)
print("Сгенерированный текст:", generated_text)

```

### Анализ тональности

Проанализируйте тональность заданного текста:

```python
from claude_client import ClaudeClient

def analyze_sentiment(text) -> dict:
    """
    Анализирует тональность заданного текста.

    Args:
        text (str): Текст для анализа.

    Returns:
        dict: Результат анализа тональности.
    """
    try:
      return claude_client.analyze_sentiment(text)
    except Exception as ex:
      raise Exception(f"Ошибка при анализе тональности: {ex}")


text_to_analyze = "Сегодня я очень счастлив!"
sentiment_analysis = analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)
```


### Перевод текста

Переведите текст с одного языка на другой:

```python
from claude_client import ClaudeClient

def translate_text(text, source_language, target_language) -> str:
    """
    Переводит заданный текст с одного языка на другой.

    Args:
        text (str): Текст для перевода.
        source_language (str): Код исходного языка.
        target_language (str): Код целевого языка.

    Returns:
        str: Переведенный текст.
    """
    try:
        return claude_client.translate_text(text, source_language, target_language)
    except Exception as ex:
        raise Exception(f"Ошибка при переводе текста: {ex}")


text_to_translate = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```


## Пример кода

```python
# ... (код инициализации и функций из предыдущих примеров)

# Пример использования всех функций
# ... (вставьте примеры использования generate_text, analyze_sentiment, translate_text)
```

## Методы

### `generate_text(prompt, max_tokens_to_sample=100)`

Генерирует текст на основе заданного промпта.

**Параметры:**

* `prompt` (str): Промпт для генерации текста.
* `max_tokens_to_sample` (int, optional): Максимальное количество токенов для генерации. По умолчанию 100.

**Возвращает:**

* str: Сгенерированный текст.


### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

**Параметры:**

* `text` (str): Текст для анализа.

**Возвращает:**

* dict: Результат анализа тональности.


### `translate_text(text, source_language, target_language)`

Переводит заданный текст с одного языка на другой.

**Параметры:**

* `text` (str): Текст для перевода.
* `source_language` (str): Код исходного языка.
* `target_language` (str): Код целевого языка.

**Возвращает:**

* str: Переведенный текст.


## Вклад

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или имеете предложения по улучшению.


## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"your-api-key"` на ваш реальный API-ключ от Anthropic.