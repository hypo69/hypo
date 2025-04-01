# Документация модуля `src.ai.helicone`

## Обзор

Модуль `src.ai.helicone` предоставляет класс `HeliconeAI`, который предназначен для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, суммирования текста и перевода текста. Также он включает логирование завершений с использованием Helicone.ai.

## Подробнее

Этот модуль позволяет интегрировать функциональность Helicone.ai и OpenAI в проект `hypotez`, обеспечивая удобный интерфейс для выполнения различных задач обработки текста и логирования.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предназначен для взаимодействия с Helicone.ai и OpenAI.

**Принцип работы**:
Класс инициализируется с клиентами Helicone и OpenAI. Он предоставляет методы для генерации стихов, анализа тональности, суммирования и перевода текста, а также логирует все завершения через Helicone.

**Аттрибуты**:
- `helicone` (Helicone): Клиент Helicone для логирования завершений.
- `client` (OpenAI): Клиент OpenAI для выполнения запросов к моделям.

**Методы**:
- `__init__(self)`: Инициализирует класс `HeliconeAI`, создавая экземпляры клиентов Helicone и OpenAI.
- `generate_poem(self, prompt: str) -> str`: Генерирует стихотворение на основе заданного запроса.
- `analyze_sentiment(self, text: str) -> str`: Анализирует тональность заданного текста.
- `summarize_text(self, text: str) -> str`: Суммирует заданный текст.
- `translate_text(self, text: str, target_language: str) -> str`: Переводит заданный текст на указанный язык.

### `__init__`

**Назначение**: Инициализирует класс `HeliconeAI`, создавая экземпляры клиентов Helicone и OpenAI.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Как работает функция**:

1. Инициализируется клиент Helicone.
2. Инициализируется клиент OpenAI.

```
Инициализация Helicone -> Инициализация OpenAI
```

**Примеры**:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()

helicone_ai = HeliconeAI()
```

### `generate_poem`

```python
def generate_poem(self, prompt: str) -> str:
    """
    Генерирует стихотворение на основе заданного запроса, используя модель `gpt-3.5-turbo`.

    Args:
        prompt (str): Запрос для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.
    """
    ...
```

**Назначение**: Генерирует стихотворение на основе заданного запроса, используя модель `gpt-3.5-turbo`.

**Параметры**:
- `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Как работает функция**:

1. Отправляет запрос в OpenAI для генерации стихотворения на основе предоставленного `prompt`.
2. Логирует завершение с помощью Helicone.
3. Возвращает сгенерированное стихотворение.

```
Запрос OpenAI (prompt) -> Логирование завершения (Helicone) -> Возврат стихотворения
```

**Примеры**:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()

    def generate_poem(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        self.helicone.log_completion(response)
        return response.choices[0].message.content

helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

### `analyze_sentiment`

```python
def analyze_sentiment(self, text: str) -> str:
    """
    Анализирует тональность заданного текста, используя модель `text-davinci-003`.

    Args:
        text (str): Текст для анализа тональности.

    Returns:
        str: Результат анализа тональности.
    """
    ...
```

**Назначение**: Анализирует тональность заданного текста, используя модель `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:

1. Отправляет запрос в OpenAI для анализа тональности текста.
2. Логирует завершение с помощью Helicone.
3. Возвращает результат анализа тональности.

```
Запрос OpenAI (text) -> Логирование завершения (Helicone) -> Возврат анализа тональности
```

**Примеры**:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()

    def analyze_sentiment(self, text: str) -> str:
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Analyze the sentiment of the following text: {text}",
            max_tokens=50
        )
        self.helicone.log_completion(response)
        return response.choices[0].text.strip()

helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

### `summarize_text`

```python
def summarize_text(self, text: str) -> str:
    """
    Суммирует заданный текст, используя модель `text-davinci-003`.

    Args:
        text (str): Текст для суммирования.

    Returns:
        str: Суммированный текст.
    """
    ...
```

**Назначение**: Суммирует заданный текст, используя модель `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для суммирования.

**Возвращает**:
- `str`: Суммированный текст.

**Как работает функция**:

1. Отправляет запрос в OpenAI для суммирования текста.
2. Логирует завершение с помощью Helicone.
3. Возвращает суммированный текст.

```
Запрос OpenAI (text) -> Логирование завершения (Helicone) -> Возврат суммированного текста
```

**Примеры**:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()

    def summarize_text(self, text: str) -> str:
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Summarize the following text: {text}",
            max_tokens=100
        )
        self.helicone.log_completion(response)
        return response.choices[0].text.strip()

helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

### `translate_text`

```python
def translate_text(self, text: str, target_language: str) -> str:
    """
    Переводит заданный текст на указанный язык, используя модель `text-davinci-003`.

    Args:
        text (str): Текст для перевода.
        target_language (str): Язык, на который нужно перевести текст.

    Returns:
        str: Переведенный текст.
    """
    ...
```

**Назначение**: Переводит заданный текст на указанный язык, используя модель `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Язык, на который нужно перевести текст.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:

1. Отправляет запрос в OpenAI для перевода текста на указанный язык.
2. Логирует завершение с помощью Helicone.
3. Возвращает переведенный текст.

```
Запрос OpenAI (text, target_language) -> Логирование завершения (Helicone) -> Возврат переведенного текста
```

**Примеры**:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()

    def translate_text(self, text: str, target_language: str) -> str:
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Translate the following text to {target_language}: {text}",
            max_tokens=200
        )
        self.helicone.log_completion(response)
        return response.choices[0].text.strip()

helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)