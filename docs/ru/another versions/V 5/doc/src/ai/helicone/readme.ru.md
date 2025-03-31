# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, создания краткого изложения текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Подробней

Этот модуль предоставляет удобный интерфейс для работы с Helicone.ai и OpenAI API, позволяя легко интегрировать функциональность генерации текста, анализа тональности, создания кратких изложений и перевода в ваши приложения. Он упрощает взаимодействие с моделями OpenAI и обеспечивает логирование запросов через Helicone.ai для мониторинга и анализа использования API.

## Классы

### `HeliconeAI`

**Описание**: Класс для интеграции с Helicone.ai и OpenAI.

**Как работает класс**:
Класс инициализирует клиенты для Helicone и OpenAI. Он предоставляет методы для выполнения различных задач, таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста, используя модели OpenAI. Все запросы к OpenAI логируются через Helicone.

**Методы**:
- `__init__`: Инициализирует класс `HeliconeAI` с клиентами Helicone и OpenAI.
- `generate_poem`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `summarize_text`: Создает краткое изложение заданного текста.
- `translate_text`: Переводит заданный текст на указанный целевой язык.

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

#### `__init__`
**Описание**: Инициализирует класс `HeliconeAI`.

```python
def __init__(self):
    self.helicone = Helicone()
    self.client = OpenAI()
```

**Как работает функция**:
Метод инициализирует экземпляры классов `Helicone` и `OpenAI` и сохраняет их в атрибутах `helicone` и `client` соответственно. Это позволяет использовать API Helicone и OpenAI для выполнения различных операций.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:
```python
helicone_ai = HeliconeAI()
```

## Функции

### `generate_poem`

```python
def generate_poem(self, prompt: str) -> str:
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    self.helicone.log_completion(response)
    return response.choices[0].message.content
```

**Описание**: Генерирует стихотворение на основе заданного промпта.

**Как работает функция**:
Функция принимает текстовый промпт и использует модель `gpt-3.5-turbo` для генерации стихотворения. Она отправляет запрос к OpenAI API через клиент `self.client`, логирует завершение с помощью `self.helicone.log_completion` и возвращает сгенерированное стихотворение.

**Параметры**:
- `prompt` (str): Текст промпта для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Вызывает исключения**:
- Нет

**Примеры**:
```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

### `analyze_sentiment`

```python
def analyze_sentiment(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Описание**: Анализирует тональность заданного текста.

**Как работает функция**:
Функция принимает текст для анализа и использует модель `text-davinci-003` для определения его тональности. Она отправляет запрос к OpenAI API, логирует завершение с помощью `self.helicone.log_completion` и возвращает результат анализа тональности.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Вызывает исключения**:
- Нет

**Примеры**:
```python
helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

### `summarize_text`

```python
def summarize_text(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Описание**: Создает краткое изложение заданного текста.

**Как работает функция**:
Функция принимает текст для изложения и использует модель `text-davinci-003` для создания краткого изложения. Она отправляет запрос к OpenAI API, логирует завершение с помощью `self.helicone.log_completion` и возвращает краткое изложение текста.

**Параметры**:
- `text` (str): Текст для создания краткого изложения.

**Возвращает**:
- `str`: Краткое изложение текста.

**Вызывает исключения**:
- Нет

**Примеры**:
```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

### `translate_text`

```python
def translate_text(self, text: str, target_language: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=200
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Описание**: Переводит заданный текст на указанный целевой язык.

**Как работает функция**:
Функция принимает текст для перевода и целевой язык. Она использует модель `text-davinci-003` для перевода текста на указанный язык. Функция отправляет запрос к OpenAI API, логирует завершение с помощью `self.helicone.log_completion` и возвращает переведенный текст.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Вызывает исключения**:
- Нет

**Примеры**:
```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```