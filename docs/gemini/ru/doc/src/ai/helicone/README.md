# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для взаимодействия с сервисом Helicone.ai и моделями OpenAI. Он предоставляет методы для генерации стихотворений, анализа настроения текста, создания изложений и перевода текста. Также класс включает логирование запросов к Helicone.ai.

## Оглавление

* [Обзор](#обзор)
* [Основные функции](#ключевые-функции)
* [Установка](#установка)
* [Использование](#использование)
* [Пример использования](#пример-использования)
* [Зависимости](#зависимости)
* [Лицензия](#лицензия)


## Основные функции

1. **Генерация стихотворения**: Генерирует стихотворение на основе заданного запроса с использованием модели `gpt-3.5-turbo`.
2. **Анализ настроения**: Анализирует настроение заданного текста с использованием модели `text-davinci-003`.
3. **Создание изложения**: Создаёт изложение заданного текста с использованием модели `text-davinci-003`.
4. **Перевод текста**: Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.
5. **Логирование запросов**: Логирует все запросы к Helicone.ai для мониторинга и анализа.

## Установка

Для использования класса `HeliconeAI` убедитесь, что установлены необходимые зависимости. Установите их с помощью pip:

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

#### `generate_poem`

Генерирует стихотворение на основе заданного запроса.

**Описание**: Генерирует стихотворение на основе предоставленного запроса.

**Параметры**:
- `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Вызывает исключения**:
- Возможные исключения, генерируемые OpenAI.

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

#### `analyze_sentiment`

Анализирует настроение заданного текста.

**Описание**: Анализирует настроение заданного текста.

**Параметры**:
- `text` (str): Текст для анализа настроения.

**Возвращает**:
- `str`: Анализ настроения (например, "positive", "negative", "neutral").

**Вызывает исключения**:
- Возможные исключения, генерируемые OpenAI.


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

(Аналогично для `summarize_text` и `translate_text`)


####  Другие методы: `summarize_text`, `translate_text`

См. определения методов в исходном коде.  Эти методы аналогично обрабатывают входные данные, используя  `text-davinci-003`  и логируют ответ.

## Пример использования

```python
def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Сгенерированное стихотворение:\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Анализ настроения:\n", sentiment)

    # ... (примеры для summarize_text и translate_text)

if __name__ == "__main__":
    main()
```

## Зависимости

- `helicone`
- `openai`

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробнее см. файл [LICENSE](LICENSE).