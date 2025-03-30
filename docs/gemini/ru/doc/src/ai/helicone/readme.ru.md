# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, создания краткого изложения текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Подробнее

`HeliconeAI` разработан для интеграции с платформами Helicone.ai и OpenAI, предоставляя удобный интерфейс для выполнения различных задач обработки текста, таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста. Использование этого класса позволяет упростить взаимодействие с API OpenAI и автоматизировать процесс логирования запросов через Helicone.ai.

## Классы

### `HeliconeAI`

**Описание**: Класс для взаимодействия с Helicone.ai и OpenAI API.

**Методы**:
- `__init__`: Инициализирует класс `HeliconeAI`, создавая экземпляры `Helicone` и `OpenAI`.
- `generate_poem`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `summarize_text`: Создает краткое изложение заданного текста.
- `translate_text`: Переводит заданный текст на указанный целевой язык.

**Параметры**:
- Нет параметров для инициализации класса.

**Примеры**

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

    def analyze_sentiment(self, text: str) -> str:
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Analyze the sentiment of the following text: {text}",
            max_tokens=50
        )
        self.helicone.log_completion(response)
        return response.choices[0].text.strip()

    def summarize_text(self, text: str) -> str:
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Summarize the following text: {text}",
            max_tokens=100
        )
        self.helicone.log_completion(response)
        return response.choices[0].text.strip()

    def translate_text(self, text: str, target_language: str) -> str:
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Translate the following text to {target_language}: {text}",
            max_tokens=200
        )
        self.helicone.log_completion(response)
        return response.choices[0].text.strip()

def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\n", translation)

if __name__ == "__main__":
    main()
```

## Функции

### `generate_poem`

```python
def generate_poem(self, prompt: str) -> str:
    """
    Генерирует стихотворение на основе заданного промпта.

    Args:
        prompt (str): Текст запроса для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.
    """
    ...
```

**Описание**: Генерирует стихотворение на основе заданного промпта с использованием модели `gpt-3.5-turbo`.

**Параметры**:
- `prompt` (str): Текст запроса для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Примеры**:

```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

### `analyze_sentiment`

```python
def analyze_sentiment(self, text: str) -> str:
    """
    Анализирует тональность заданного текста.

    Args:
        text (str): Текст для анализа тональности.

    Returns:
        str: Результат анализа тональности.
    """
    ...
```

**Описание**: Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Примеры**:

```python
helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

### `summarize_text`

```python
def summarize_text(self, text: str) -> str:
    """
    Создает краткое изложение заданного текста.

    Args:
        text (str): Текст для создания краткого изложения.

    Returns:
        str: Краткое изложение текста.
    """
    ...
```

**Описание**: Создает краткое изложение заданного текста с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для создания краткого изложения.

**Возвращает**:
- `str`: Краткое изложение текста.

**Примеры**:

```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

### `translate_text`

```python
def translate_text(self, text: str, target_language: str) -> str:
    """
    Переводит заданный текст на указанный целевой язык.

    Args:
        text (str): Текст для перевода.
        target_language (str): Целевой язык для перевода.

    Returns:
        str: Переведенный текст.
    """
    ...
```

**Описание**: Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Примеры**:

```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```