# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для облегчения взаимодействия с моделями Helicone.ai и OpenAI. Этот класс предоставляет методы для создания стихов, анализа тональности, обобщения текста и перевода текста. Он также включает в себя ведение журнала завершений с использованием Helicone.ai.

## Подробней

`HeliconeAI` упрощает работу с моделями OpenAI, предоставляя удобные методы для выполнения различных задач обработки текста, таких как создание стихов, анализ тональности, обобщение и перевод текста. Кроме того, он интегрируется с Helicone.ai для ведения журнала всех завершений, что полезно для мониторинга и анализа использования моделей.

## Классы

### `HeliconeAI`

**Описание**: Класс для взаимодействия с Helicone.ai и OpenAI.

**Как работает класс**:
Класс инициализируется с использованием клиентов `Helicone` и `OpenAI`. Он предоставляет методы для создания стихов, анализа тональности текста, обобщения текста и перевода текста на указанный язык. Каждый метод использует соответствующую модель OpenAI и регистрирует завершение с помощью Helicone.ai для мониторинга и анализа.

**Методы**:
- `generate_poem`: Создает стихотворение на основе заданного запроса.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `summarize_text`: Обобщает заданный текст.
- `translate_text`: Переводит заданный текст на указанный язык.

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

#### `__init__`

**Описание**: Инициализирует класс `HeliconeAI` с клиентами Helicone и OpenAI.

**Как работает функция**:
Создает экземпляры клиентов `Helicone` и `OpenAI` и присваивает их атрибутам `self.helicone` и `self.client` соответственно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

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

**Описание**: Создает стихотворение на основе заданного запроса, используя модель `gpt-3.5-turbo`.

**Как работает функция**:
Принимает запрос в виде строки, отправляет его в модель `gpt-3.5-turbo` через API OpenAI, получает ответ, регистрирует завершение с помощью Helicone.ai и возвращает сгенерированное стихотворение.

**Параметры**:
- `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Примеры**:

```python
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print("Generated Poem:\n", poem)
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

**Описание**: Анализирует тональность заданного текста, используя модель `text-davinci-003`.

**Как работает функция**:
Принимает текст в виде строки, формирует запрос для анализа тональности, отправляет его в модель `text-davinci-003` через API OpenAI, получает ответ, регистрирует завершение с помощью Helicone.ai и возвращает результат анализа тональности.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Примеры**:

```python
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print("Sentiment Analysis:\n", sentiment)
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

**Описание**: Обобщает заданный текст, используя модель `text-davinci-003`.

**Как работает функция**:
Принимает текст в виде строки, формирует запрос для обобщения, отправляет его в модель `text-davinci-003` через API OpenAI, получает ответ, регистрирует завершение с помощью Helicone.ai и возвращает результат обобщения.

**Параметры**:
- `text` (str): Текст для обобщения.

**Возвращает**:
- `str`: Результат обобщения.

**Примеры**:

```python
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print("Summary:\n", summary)
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

**Описание**: Переводит заданный текст на указанный язык, используя модель `text-davinci-003`.

**Как работает функция**:
Принимает текст и целевой язык в виде строк, формирует запрос для перевода, отправляет его в модель `text-davinci-003` через API OpenAI, получает ответ, регистрирует завершение с помощью Helicone.ai и возвращает результат перевода.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:
- `str`: Результат перевода.

**Примеры**:

```python
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print("Translation:\n", translation)
```