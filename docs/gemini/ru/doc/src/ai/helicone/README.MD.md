# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для облегчения взаимодействия с моделями Helicone.ai и OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности, обобщения текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Оглавление

- [Обзор](#обзор)
- [Ключевые особенности](#ключевые-особенности)
- [Установка](#установка)
- [Использование](#использование)
    - [Инициализация](#инициализация)
    - [Методы](#методы)
        - [Генерация стиха](#генерация-стиха)
        - [Анализ тональности](#анализ-тональности)
        - [Обобщение текста](#обобщение-текста)
        - [Перевод текста](#перевод-текста)
    - [Пример использования](#пример-использования)
- [Зависимости](#зависимости)
- [Лицензия](#лицензия)

## Ключевые особенности

1.  **Генерация стихов**:
    - Генерирует стихотворение на основе заданного запроса с использованием модели `gpt-3.5-turbo`.

2.  **Анализ тональности**:
    - Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

3.  **Обобщение текста**:
    - Обобщает заданный текст с использованием модели `text-davinci-003`.

4.  **Перевод текста**:
    - Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

5.  **Логирование завершений**:
    - Логирует все завершения с использованием Helicone.ai для мониторинга и анализа.

## Установка

Для использования класса `HeliconeAI` убедитесь, что установлены необходимые зависимости. Вы можете установить их с помощью pip:

```bash
pip install openai helicone
```

## Использование

### Инициализация

Инициализируйте класс `HeliconeAI`:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

### Методы

#### Генерация стиха

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

**Описание**: Генерирует стихотворение на основе заданного запроса.

**Параметры**:

-   `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:

-   `str`: Сгенерированное стихотворение.

#### Анализ тональности

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

**Параметры**:

-   `text` (str): Текст для анализа тональности.

**Возвращает**:

-   `str`: Результат анализа тональности.

#### Обобщение текста

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

**Описание**: Обобщает заданный текст.

**Параметры**:

-   `text` (str): Текст для обобщения.

**Возвращает**:

-   `str`: Обобщенный текст.

#### Перевод текста

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

**Параметры**:

-   `text` (str): Текст для перевода.
-   `target_language` (str): Целевой язык для перевода.

**Возвращает**:

-   `str`: Переведенный текст.

### Пример использования

Вот пример использования класса `HeliconeAI`:

```python
def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\\n", translation)

if __name__ == "__main__":
    main()
```

## Зависимости

- `helicone`
- `openai`

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробности см. в файле [LICENSE](LICENSE).

---

Для получения более подробной информации обратитесь к исходному коду и комментариям внутри класса `HeliconeAI`.