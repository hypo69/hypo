# Модуль `src.ai.helicone`

## Обзор

Модуль предоставляет класс `HeliconeAI`, предназначенный для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Он включает методы для генерации стихов, анализа тональности текста, создания краткого изложения и перевода текста, а также логирование всех взаимодействий через Helicone.ai.

## Подробнее

Этот модуль позволяет интегрировать возможности Helicone.ai и OpenAI в проекты, предоставляя удобный интерфейс для выполнения различных задач обработки текста. Класс `HeliconeAI` абстрагирует сложность прямого взаимодействия с API, обеспечивая простой и понятный способ использования моделей для генерации, анализа и перевода текста.

## Классы

### `HeliconeAI`

**Описание**: Класс для взаимодействия с Helicone.ai и OpenAI.

**Принцип работы**: Класс инициализирует клиенты для Helicone и OpenAI, что позволяет использовать их методы для выполнения различных задач, таких как генерация стихов, анализ тональности, создание краткого изложения текста и перевод текста. Все запросы логируются через Helicone для мониторинга и анализа.

**Аттрибуты**:
- `helicone` (Helicone): Экземпляр класса `Helicone` для логирования завершений.
- `client` (OpenAI): Экземпляр класса `OpenAI` для взаимодействия с моделями OpenAI.

**Методы**:
- `__init__`: Инициализирует класс `HeliconeAI`, создавая экземпляры клиентов `Helicone` и `OpenAI`.
- `generate_poem`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `summarize_text`: Создает краткое изложение заданного текста.
- `translate_text`: Переводит заданный текст на указанный целевой язык.

#### `__init__`
```python
def __init__(self):
    self.helicone = Helicone()
    self.client = OpenAI()
```

**Назначение**: Инициализирует экземпляры классов `Helicone` и `OpenAI`.

**Как работает функция**:
1. Создает экземпляр класса `Helicone` и присваивает его атрибуту `self.helicone`.
2. Создает экземпляр класса `OpenAI` и присваивает его атрибуту `self.client`.

**Примеры**:
```python
helicone_ai = HeliconeAI()
```

#### `generate_poem`
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

**Назначение**: Генерирует стихотворение на основе заданного промпта с использованием модели `gpt-3.5-turbo`.

**Параметры**:
- `prompt` (str): Текст запроса для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Как работает функция**:
1. Отправляет запрос в OpenAI API для генерации стихотворения на основе заданного промпта.
2. Логирует завершение с использованием `self.helicone.log_completion(response)`.
3. Извлекает сгенерированное стихотворение из ответа и возвращает его.

**Примеры**:
```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

#### `analyze_sentiment`
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

**Назначение**: Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1. Отправляет запрос в OpenAI API для анализа тональности заданного текста.
2. Логирует завершение с использованием `self.helicone.log_completion(response)`.
3. Извлекает результат анализа тональности из ответа и возвращает его.

**Примеры**:
```python
helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

#### `summarize_text`
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

**Назначение**: Создает краткое изложение заданного текста с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для создания краткого изложения.

**Возвращает**:
- `str`: Краткое изложение текста.

**Как работает функция**:
1. Отправляет запрос в OpenAI API для создания краткого изложения заданного текста.
2. Логирует завершение с использованием `self.helicone.log_completion(response)`.
3. Извлекает краткое изложение текста из ответа и возвращает его.

**Примеры**:
```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

#### `translate_text`
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

**Назначение**: Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1. Отправляет запрос в OpenAI API для перевода заданного текста на указанный целевой язык.
2. Логирует завершение с использованием `self.helicone.log_completion(response)`.
3. Извлекает переведенный текст из ответа и возвращает его.

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

**Назначение**: Пример использования класса `HeliconeAI` для генерации стихов, анализа тональности, создания краткого изложения и перевода текста.

**Как работает функция**:
1. Создает экземпляр класса `HeliconeAI`.
2. Использует методы `generate_poem`, `analyze_sentiment`, `summarize_text` и `translate_text` для выполнения соответствующих задач.
3. Выводит результаты выполнения каждой задачи.

**Примеры**:
```python
main()