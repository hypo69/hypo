# Модуль helicone

## Обзор

Модуль `helicone` предоставляет класс `HeliconeAI` для взаимодействия с Helicone и OpenAI API. Он включает в себя функциональность для генерации стихов, анализа тональности текста, создания кратких изложений и перевода текста на другие языки.

## Подробней

Модуль предназначен для упрощения работы с AI-сервисами через Helicone и OpenAI. Класс `HeliconeAI` инкапсулирует методы для выполнения различных задач обработки текста, таких как генерация контента, анализ тональности и перевод.

## Классы

### `HeliconeAI`

**Описание**: Класс для взаимодействия с Helicone и OpenAI API.

**Методы**:
- `__init__`: Инициализирует клиент Helicone и OpenAI.
- `generate_poem`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment`: Анализирует тональность текста.
- `summarize_text`: Создает краткое изложение текста.
- `translate_text`: Переводит текст на указанный язык.

**Параметры**:
- Нет параметров для `__init__`.
- `prompt` (str) для `generate_poem`.
- `text` (str) для `analyze_sentiment` и `summarize_text`.
- `text` (str) и `target_language` (str) для `translate_text`.

**Примеры**
```python
helicone_ai = HeliconeAI()

poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print("Generated Poem:\\n", poem)

sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print("Sentiment Analysis:\\n", sentiment)

summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print("Summary:\\n", summary)

translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print("Translation:\\n", translation)
```

## Функции

### `generate_poem`

```python
def generate_poem(self, prompt: str) -> str:
    """
    Генерирует стихотворение на основе заданного промпта.

    Аргументы:
        prompt (str): Промпт для генерации стихотворения.

    Возвращает:
        str: Сгенерированное стихотворение.
    """
    ...
```

**Описание**: Генерирует стихотворение на основе заданного промпта, используя OpenAI API.

**Параметры**:
- `prompt` (str): Промпт для генерации стихотворения.

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
    Анализирует тональность текста.

    Аргументы:
        text (str): Текст для анализа.

    Возвращает:
        str: Результат анализа тональности.
    """
    ...
```

**Описание**: Анализирует тональность текста, используя OpenAI API.

**Параметры**:
- `text` (str): Текст для анализа.

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
    Создает краткое изложение текста.

    Аргументы:
        text (str): Текст для изложения.

    Возвращает:
        str: Краткое изложение текста.
    """
    ...
```

**Описание**: Создает краткое изложение текста, используя OpenAI API.

**Параметры**:
- `text` (str): Текст для изложения.

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
    Переводит текст на указанный язык.

    Аргументы:
        text (str): Текст для перевода.
        target_language (str): Целевой язык перевода.

    Возвращает:
        str: Переведенный текст.
    """
    ...
```

**Описание**: Переводит текст на указанный язык, используя OpenAI API.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Примеры**:
```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```

### `main`

```python
def main():
    ...
```

**Описание**: Основная функция для демонстрации работы класса `HeliconeAI`.

**Примеры**:
```python
if __name__ == "__main__":
    main()
```