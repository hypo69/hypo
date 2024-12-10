# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Модуль `HeliconeAI` предоставляет класс для взаимодействия с сервисами Helicone.ai и OpenAI, упрощая работу с генерацией текста, анализом тональности, изложением и переводом. Он включает логирование ответов Helicone.ai для мониторинга и анализа.

## Оглавление

* [HeliconeAI](#heliconeai)
* [Функции](#функции)
    * [generate_poem](#generate_poem)
    * [analyze_sentiment](#analyze_sentiment)
    * [summarize_text](#summarize_text)
    * [translate_text](#translate_text)


## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предоставляет методы для взаимодействия с Helicone.ai и моделями OpenAI.

**Методы**:

* [`generate_poem`](#generate_poem)
* [`analyze_sentiment`](#analyze_sentiment)
* [`summarize_text`](#summarize_text)
* [`translate_text`](#translate_text)


## Функции

### `generate_poem`

**Описание**: Генерирует стихотворение на основе заданного промпта с использованием модели `gpt-3.5-turbo`.

**Параметры**:

* `prompt` (str): Текст промпта для генерации стихотворения.

**Возвращает**:

* `str`: Сгенерированное стихотворение.

**Вызывает исключения**:

* Возможные исключения OpenAI (например, `openai.error.APIError`).


### `analyze_sentiment`

**Описание**: Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

**Параметры**:

* `text` (str): Текст для анализа тональности.

**Возвращает**:

* `str`: Анализ тональности текста.

**Вызывает исключения**:

* Возможные исключения OpenAI (например, `openai.error.APIError`).


### `summarize_text`

**Описание**: Создает краткое изложение заданного текста с использованием модели `text-davinci-003`.

**Параметры**:

* `text` (str): Текст для краткого изложения.

**Возвращает**:

* `str`: Краткое изложение текста.

**Вызывает исключения**:

* Возможные исключения OpenAI (например, `openai.error.APIError`).


### `translate_text`

**Описание**: Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

**Параметры**:

* `text` (str): Текст для перевода.
* `target_language` (str): Целевой язык перевода.

**Возвращает**:

* `str`: Переведенный текст.

**Вызывает исключения**:

* Возможные исключения OpenAI (например, `openai.error.APIError`).


## Пример использования

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()

    # ... (остальные методы) ...

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

## Зависимости

* `helicone`
* `openai`

## Лицензия

MIT License.