# Модуль `src.ai.helicone`

## Обзор

Модуль предназначен для интеграции с Helicone.ai и OpenAI, предоставляя класс `HeliconeAI` для упрощения взаимодействия с этими сервисами. Класс предоставляет методы для генерации стихов, анализа тональности текста, создания краткого изложения текста и перевода текста, а также включает логирование завершений с использованием Helicone.ai.

## Подробнее

Этот модуль позволяет разработчикам легко интегрировать возможности Helicone.ai и OpenAI в свои приложения. Он предоставляет удобные методы для выполнения различных задач обработки текста, таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста.  Модуль упрощает использование API OpenAI и логирование запросов через Helicone.ai, что полезно для мониторинга и анализа использования AI в проекте.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предоставляет методы для взаимодействия с Helicone.ai и OpenAI.

**Принцип работы**: Класс инициализируется с клиентами `Helicone` и `OpenAI`. Он использует эти клиенты для выполнения различных задач, таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста. Все запросы к OpenAI логируются с использованием Helicone.ai для мониторинга и анализа.

**Аттрибуты**:

- `helicone`: Объект `Helicone` для логирования завершений.
- `client`: Объект `OpenAI` для выполнения запросов к API OpenAI.

**Методы**:

- `__init__()`: Инициализирует класс `HeliconeAI` с клиентами `Helicone` и `OpenAI`.
- `generate_poem(prompt: str) -> str`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment(text: str) -> str`: Анализирует тональность заданного текста.
- `summarize_text(text: str) -> str`: Создает краткое изложение заданного текста.
- `translate_text(text: str, target_language: str) -> str`: Переводит заданный текст на указанный целевой язык.

### `__init__`

```python
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

**Назначение**: Инициализирует класс `HeliconeAI`.

**Как работает функция**:

1.  Создает экземпляр класса `Helicone`.
2.  Создает экземпляр класса `OpenAI`.
3.  Сохраняет созданные экземпляры в атрибутах `self.helicone` и `self.client` соответственно.

```
Инициализация
│
├── Создание экземпляра Helicone (helicone)
│
└── Создание экземпляра OpenAI (client)
│
Сохранение экземпляров
│
├── self.helicone = helicone
│
└── self.client = client
```

### `generate_poem`

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

**Назначение**: Генерирует стихотворение на основе заданного промпта, используя модель `gpt-3.5-turbo`.

**Параметры**:

- `prompt` (str): Текст промпта для генерации стихотворения.

**Возвращает**:

- `str`: Сгенерированное стихотворение.

**Как работает функция**:

1.  Отправляет запрос к OpenAI API для генерации стихотворения на основе заданного промпта.
2.  Логирует завершение с использованием Helicone.ai.
3.  Возвращает сгенерированное стихотворение.

```
Запрос к OpenAI
│
└── Создание запроса к OpenAI Chat Completions API с моделью "gpt-3.5-turbo" и промптом пользователя (response)
│
Логирование завершения
│
└── Логирование завершения с использованием Helicone (self.helicone.log_completion(response))
│
Возврат результата
│
└── Извлечение и возврат сгенерированного стихотворения из ответа OpenAI (response.choices[0].message.content)
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

### `analyze_sentiment`

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

**Назначение**: Анализирует тональность заданного текста, используя модель `text-davinci-003`.

**Параметры**:

- `text` (str): Текст для анализа тональности.

**Возвращает**:

- `str`: Результат анализа тональности.

**Как работает функция**:

1.  Отправляет запрос к OpenAI API для анализа тональности заданного текста.
2.  Логирует завершение с использованием Helicone.ai.
3.  Возвращает результат анализа тональности.

```
Запрос к OpenAI
│
└── Создание запроса к OpenAI Completions API с моделью "text-davinci-003" и промптом анализа тональности (response)
│
Логирование завершения
│
└── Логирование завершения с использованием Helicone (self.helicone.log_completion(response))
│
Возврат результата
│
└── Извлечение и возврат результата анализа тональности из ответа OpenAI (response.choices[0].text.strip())
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

### `summarize_text`

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

**Назначение**: Создает краткое изложение заданного текста, используя модель `text-davinci-003`.

**Параметры**:

- `text` (str): Текст для создания краткого изложения.

**Возвращает**:

- `str`: Краткое изложение текста.

**Как работает функция**:

1.  Отправляет запрос к OpenAI API для создания краткого изложения заданного текста.
2.  Логирует завершение с использованием Helicone.ai.
3.  Возвращает краткое изложение текста.

```
Запрос к OpenAI
│
└── Создание запроса к OpenAI Completions API с моделью "text-davinci-003" и промптом создания краткого изложения (response)
│
Логирование завершения
│
└── Логирование завершения с использованием Helicone (self.helicone.log_completion(response))
│
Возврат результата
│
└── Извлечение и возврат краткого изложения текста из ответа OpenAI (response.choices[0].text.strip())
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

### `translate_text`

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

**Назначение**: Переводит заданный текст на указанный целевой язык, используя модель `text-davinci-003`.

**Параметры**:

- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:

- `str`: Переведенный текст.

**Как работает функция**:

1.  Отправляет запрос к OpenAI API для перевода заданного текста на указанный целевой язык.
2.  Логирует завершение с использованием Helicone.ai.
3.  Возвращает переведенный текст.

```
Запрос к OpenAI
│
└── Создание запроса к OpenAI Completions API с моделью "text-davinci-003" и промптом перевода текста (response)
│
Логирование завершения
│
└── Логирование завершения с использованием Helicone (self.helicone.log_completion(response))
│
Возврат результата
│
└── Извлечение и возврат переведенного текста из ответа OpenAI (response.choices[0].text.strip())
```

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

**Назначение**: Главная функция для демонстрации работы класса `HeliconeAI`.

**Как работает функция**:

1.  Создает экземпляр класса `HeliconeAI`.
2.  Генерирует стихотворение, анализирует тональность текста, создает краткое изложение текста и переводит текст с использованием методов класса `HeliconeAI`.
3.  Выводит результаты на консоль.

```
Создание экземпляра HeliconeAI
│
└── Создание экземпляра класса HeliconeAI (helicone_ai)
│
Генерация стихотворения
│
└── Вызов метода generate_poem для генерации стихотворения (poem)
│
Анализ тональности
│
└── Вызов метода analyze_sentiment для анализа тональности текста (sentiment)
│
Создание краткого изложения
│
└── Вызов метода summarize_text для создания краткого изложения текста (summary)
│
Перевод текста
│
└── Вызов метода translate_text для перевода текста (translation)
│
Вывод результатов
│
└── Вывод сгенерированного стихотворения, результата анализа тональности, краткого изложения и перевода на консоль
```

**Примеры**:

```python
if __name__ == "__main__":
    main()