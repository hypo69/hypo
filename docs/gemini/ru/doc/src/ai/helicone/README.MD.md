# Модуль `src.ai.helicone`

## Обзор

Модуль `src.ai.helicone` предоставляет класс `HeliconeAI`, предназначенный для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, суммирования текста и перевода текста. Также модуль включает логирование завершений с использованием Helicone.ai.

## Подробнее

Этот модуль разработан для интеграции с сервисами Helicone.ai и OpenAI, обеспечивая удобный интерфейс для выполнения различных задач обработки текста, таких как генерация стихов, анализ тональности, суммирование и перевод. Использование этого модуля позволяет упростить взаимодействие с API OpenAI и Helicone.ai, а также автоматизировать процесс логирования запросов.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предназначен для взаимодействия с Helicone.ai и OpenAI.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `HeliconeAI`, устанавливая соединения с клиентами Helicone и OpenAI.
- `generate_poem`: Генерирует стихотворение на основе заданного запроса.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `summarize_text`: Суммирует заданный текст.
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

**Описание**: Инициализирует класс `HeliconeAI`, создавая экземпляры клиентов `Helicone` и `OpenAI`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Примеры**:
```python
helicone_ai = HeliconeAI()
```

#### `generate_poem`

**Описание**: Генерирует стихотворение на основе заданного запроса с использованием модели `gpt-3.5-turbo`.

**Параметры**:
- `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Примеры**:
```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

#### `analyze_sentiment`

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

#### `summarize_text`

**Описание**: Суммирует заданный текст с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для суммирования.

**Возвращает**:
- `str`: Суммированный текст.

**Примеры**:
```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

#### `translate_text`

**Описание**: Переводит заданный текст на указанный язык с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Язык, на который нужно перевести текст.

**Возвращает**:
- `str`: Переведенный текст.

**Примеры**:
```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```

## Функции

### `main`

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

**Описание**: Главная функция, демонстрирующая пример использования класса `HeliconeAI`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Примеры**:
```python
main()