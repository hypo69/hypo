# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Оглавление
1. [Обзор](#обзор)
2. [Основные возможности](#основные-возможности)
3. [Установка](#установка)
4. [Использование](#использование)
    - [Инициализация](#инициализация)
    - [Методы](#методы)
        - [Генерация стихов](#генерация-стихов)
        - [Анализ тональности](#анализ-тональности)
        - [Суммаризация текста](#суммаризация-текста)
        - [Перевод текста](#перевод-текста)
    - [Пример использования](#пример-использования)
5. [Зависимости](#зависимости)
6. [Лицензия](#лицензия)

## Обзор

Класс `HeliconeAI` предназначен для упрощения взаимодействия с моделями Helicone.ai и OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности, суммаризации текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Основные возможности

1. **Генерация стихов**:
   - Генерирует стих на основе заданного запроса, используя модель `gpt-3.5-turbo`.

2. **Анализ тональности**:
   - Анализирует тональность заданного текста, используя модель `text-davinci-003`.

3. **Суммаризация текста**:
   - Суммирует заданный текст, используя модель `text-davinci-003`.

4. **Перевод текста**:
   - Переводит заданный текст на указанный целевой язык, используя модель `text-davinci-003`.

5. **Логирование завершений**:
   - Логирует все завершения с использованием Helicone.ai для мониторинга и анализа.

## Установка

Для использования класса `HeliconeAI` убедитесь, что у вас установлены необходимые зависимости. Вы можете установить их, используя pip:

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

#### Генерация стихов

Генерирует стих на основе заданного запроса:

```python
def generate_poem(self, prompt: str) -> str:
    """
    Args:
        prompt (str): Текст запроса для генерации стиха.

    Returns:
        str: Сгенерированный стих.
    """
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    self.helicone.log_completion(response)
    return response.choices[0].message.content
```

#### Анализ тональности

Анализирует тональность заданного текста:

```python
def analyze_sentiment(self, text: str) -> str:
    """
    Args:
        text (str): Текст для анализа тональности.

    Returns:
        str: Результат анализа тональности.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

#### Суммаризация текста

Суммирует заданный текст:

```python
def summarize_text(self, text: str) -> str:
    """
    Args:
        text (str): Текст для суммаризации.

    Returns:
        str: Суммированный текст.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

#### Перевод текста

Переводит заданный текст на указанный целевой язык:

```python
def translate_text(self, text: str, target_language: str) -> str:
    """
    Args:
        text (str): Текст для перевода.
        target_language (str): Целевой язык для перевода.

    Returns:
        str: Переведенный текст.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=200
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

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

- `helicone`
- `openai`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

Для получения более подробной информации обратитесь к исходному коду и комментариям в классе `HeliconeAI`.