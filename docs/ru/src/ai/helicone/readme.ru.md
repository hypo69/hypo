# Модуль `src.ai.helicone`

## Обзор

Модуль содержит класс `HeliconeAI`, предназначенный для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, создания краткого изложения текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Подробнее

Этот модуль предоставляет удобный интерфейс для выполнения различных задач обработки текста с использованием API OpenAI и логирования с помощью Helicone.ai. Он упрощает процесс интеграции и позволяет легко выполнять такие операции, как генерация стихов, анализ тональности, создание кратких изложений и перевод текста.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предназначен для взаимодействия с Helicone.ai и моделями OpenAI.

**Принцип работы**:
Класс инициализирует клиентов Helicone и OpenAI, что позволяет использовать методы для генерации стихов, анализа тональности, создания краткого изложения текста и перевода текста. Также, он логирует все завершения, используя Helicone.ai.

**Аттрибуты**:

-   `helicone` (Helicone): Экземпляр класса `Helicone` для логирования завершений.
-   `client` (OpenAI): Экземпляр класса `OpenAI` для взаимодействия с API OpenAI.

**Методы**:

-   `__init__`: Инициализирует класс `HeliconeAI`, создавая экземпляры `Helicone` и `OpenAI`.
-   `generate_poem`: Генерирует стихотворение на основе заданного промпта.
-   `analyze_sentiment`: Анализирует тональность заданного текста.
-   `summarize_text`: Создает краткое изложение заданного текста.
-   `translate_text`: Переводит заданный текст на указанный целевой язык.

### `HeliconeAI.__init__`

```python
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

**Назначение**: Инициализирует экземпляр класса `HeliconeAI`.

**Параметры**:

-   Отсутствуют.

**Возвращает**:

-   Отсутствует.

**Как работает функция**:

1.  Создает экземпляр класса `Helicone` и присваивает его атрибуту `self.helicone`.
2.  Создает экземпляр класса `OpenAI` и присваивает его атрибуту `self.client`.

```
Инициализация HeliconeAI
│
├── Создание экземпляра Helicone (self.helicone)
│
└── Создание экземпляра OpenAI (self.client)
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
```

### `HeliconeAI.generate_poem`

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

-   `prompt` (str): Текст запроса (промпт) для генерации стихотворения.

**Возвращает**:

-   `str`: Сгенерированное стихотворение.

**Как работает функция**:

1.  Использует клиент OpenAI для создания завершения чата с моделью `gpt-3.5-turbo`.
2.  Передает промпт в сообщении пользователю.
3.  Логирует завершение с использованием Helicone.
4.  Возвращает сгенерированное стихотворение из ответа.

```
Генерация стихотворения
│
├── Создание запроса к OpenAI (chat.completions.create)
│   └── Модель: gpt-3.5-turbo
│   └── Сообщение: prompt
│
├── Логирование завершения с использованием Helicone (helicone.log_completion)
│
└── Извлечение и возврат сгенерированного стихотворения (response.choices[0].message.content)
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

### `HeliconeAI.analyze_sentiment`

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

-   `text` (str): Текст, для которого требуется провести анализ тональности.

**Возвращает**:

-   `str`: Результат анализа тональности.

**Как работает функция**:

1.  Использует клиент OpenAI для создания завершения с моделью `text-davinci-003`.
2.  Формирует промпт для анализа тональности заданного текста.
3.  Логирует завершение с использованием Helicone.
4.  Возвращает результат анализа тональности.

```
Анализ тональности текста
│
├── Создание запроса к OpenAI (completions.create)
│   └── Модель: text-davinci-003
│   └── Промпт: Analyze the sentiment of the following text: text
│   └── max_tokens: 50
│
├── Логирование завершения с использованием Helicone (helicone.log_completion)
│
└── Извлечение и возврат результата анализа тональности (response.choices[0].text.strip())
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

### `HeliconeAI.summarize_text`

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

-   `text` (str): Текст, для которого требуется создать краткое изложение.

**Возвращает**:

-   `str`: Краткое изложение текста.

**Как работает функция**:

1.  Использует клиент OpenAI для создания завершения с моделью `text-davinci-003`.
2.  Формирует промпт для создания краткого изложения заданного текста.
3.  Логирует завершение с использованием Helicone.
4.  Возвращает краткое изложение текста.

```
Создание краткого изложения текста
│
├── Создание запроса к OpenAI (completions.create)
│   └── Модель: text-davinci-003
│   └── Промпт: Summarize the following text: text
│   └── max_tokens: 100
│
├── Логирование завершения с использованием Helicone (helicone.log_completion)
│
└── Извлечение и возврат краткого изложения текста (response.choices[0].text.strip())
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

### `HeliconeAI.translate_text`

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

-   `text` (str): Текст, который требуется перевести.
-   `target_language` (str): Целевой язык для перевода.

**Возвращает**:

-   `str`: Переведенный текст.

**Как работает функция**:

1.  Использует клиент OpenAI для создания завершения с моделью `text-davinci-003`.
2.  Формирует промпт для перевода заданного текста на указанный целевой язык.
3.  Логирует завершение с использованием Helicone.
4.  Возвращает переведенный текст.

```
Перевод текста
│
├── Создание запроса к OpenAI (completions.create)
│   └── Модель: text-davinci-003
│   └── Промпт: Translate the following text to target_language: text
│   └── max_tokens: 200
│
├── Логирование завершения с использованием Helicone (helicone.log_completion)
│
└── Извлечение и возврат переведенного текста (response.choices[0].text.strip())
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

**Назначение**: Главная функция, демонстрирующая использование класса `HeliconeAI`.

**Параметры**:

-   Отсутствуют.

**Возвращает**:

-   Отсутствует.

**Как работает функция**:

1.  Создает экземпляр класса `HeliconeAI`.
2.  Генерирует стихотворение, анализирует тональность текста, создает краткое изложение текста и переводит текст.
3.  Выводит результаты на консоль.

```
Главная функция (main)
│
├── Создание экземпляра HeliconeAI (helicone_ai)
│
├── Генерация стихотворения (generate_poem)
│   └── Вывод сгенерированного стихотворения на консоль
│
├── Анализ тональности (analyze_sentiment)
│   └── Вывод результата анализа тональности на консоль
│
├── Создание краткого изложения текста (summarize_text)
│   └── Вывод краткого изложения текста на консоль
│
└── Перевод текста (translate_text)
    └── Вывод переведенного текста на консоль
```

**Примеры**:

```python
if __name__ == "__main__":
    main()