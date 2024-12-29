# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` разработан для облегчения взаимодействия с моделями Helicone.ai и OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности, суммирования текста и перевода текста. Он также включает в себя логирование завершений с использованием Helicone.ai.

## Оглавление

1.  [Обзор](#обзор)
2.  [Основные возможности](#основные-возможности)
3.  [Установка](#установка)
4.  [Использование](#использование)
    -   [Инициализация](#инициализация)
    -   [Методы](#методы)
        -   [Генерация стиха](#генерация-стиха)
        -   [Анализ тональности](#анализ-тональности)
        -   [Суммирование текста](#суммирование-текста)
        -   [Перевод текста](#перевод-текста)
    -   [Пример использования](#пример-использования)
5.  [Зависимости](#зависимости)
6.  [Лицензия](#лицензия)

## Основные возможности

1.  **Генерация стихов**:
    -   Генерирует стих на основе заданного запроса с использованием модели `gpt-3.5-turbo`.

2.  **Анализ тональности**:
    -   Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

3.  **Суммирование текста**:
    -   Суммирует заданный текст с использованием модели `text-davinci-003`.

4.  **Перевод текста**:
    -   Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

5.  **Логирование завершений**:
    -   Логирует все завершения с использованием Helicone.ai для мониторинга и анализа.

## Установка

Для использования класса `HeliconeAI` убедитесь, что у вас установлены необходимые зависимости. Вы можете установить их с помощью pip:

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

**Описание**: Генерирует стих на основе заданного запроса.

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

**Параметры**:
-   `prompt` (str): Запрос для генерации стиха.

**Возвращает**:
-   `str`: Сгенерированный стих.

#### Анализ тональности

**Описание**: Анализирует тональность заданного текста.

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

**Параметры**:
-   `text` (str): Текст для анализа тональности.

**Возвращает**:
-   `str`: Результат анализа тональности.

#### Суммирование текста

**Описание**: Суммирует заданный текст.

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

**Параметры**:
-   `text` (str): Текст для суммирования.

**Возвращает**:
-   `str`: Суммированный текст.

#### Перевод текста

**Описание**: Переводит заданный текст на указанный целевой язык.

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

**Параметры**:
-   `text` (str): Текст для перевода.
-   `target_language` (str): Целевой язык для перевода.

**Возвращает**:
-   `str`: Переведенный текст.

### Пример использования

Вот пример того, как использовать класс `HeliconeAI`:

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

-   `helicone`
-   `openai`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

Для получения более подробной информации обратитесь к исходному коду и комментариям внутри класса `HeliconeAI`.