# Модуль интеграции с Helicone AI
## Обзор

Модуль `helicone.py` предназначен для интеграции с платформой Helicone AI, предоставляя инструменты для генерации текста, анализа тональности, суммаризации и перевода текста. Модуль использует библиотеки `helicone` и `openai` для взаимодействия с сервисами Helicone AI и OpenAI.

## Подробней

Модуль содержит класс `HeliconeAI`, который инкапсулирует функциональность взаимодействия с API Helicone и OpenAI. Он предоставляет методы для генерации стихов, анализа тональности текста, суммаризации текста и перевода текста на разные языки.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предоставляет интерфейс для взаимодействия с сервисами Helicone AI и OpenAI.

**Принцип работы**:
Класс инициализируется с клиентами `Helicone` и `OpenAI`. Он предоставляет методы для выполнения различных задач обработки текста, таких как генерация стихов, анализ тональности, суммаризация и перевод. Каждый метод отправляет запрос к соответствующему API и регистрирует завершение с помощью Helicone.

**Аттрибуты**:
- `helicone` (Helicone): Клиент Helicone для логирования завершений.
- `client` (OpenAI): Клиент OpenAI для выполнения запросов к API.

**Методы**:
- `generate_poem(prompt: str) -> str`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment(text: str) -> str`: Анализирует тональность текста.
- `summarize_text(text: str) -> str`: Создает краткое изложение текста.
- `translate_text(text: str, target_language: str) -> str`: Переводит текст на указанный язык.

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
```

**Назначение**: Генерация стихотворения на основе заданного текстового запроса (промпта) с использованием модели `gpt-3.5-turbo` от OpenAI.

**Параметры**:
- `prompt` (str): Текстовый запрос для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Как работает функция**:
1. **Отправка запроса к OpenAI**: Формируется и отправляется запрос к API OpenAI с использованием модели `gpt-3.5-turbo` и заданным промптом.
2. **Логирование завершения**: Результат запроса (сгенерированное стихотворение) логируется с использованием клиента Helicone.
3. **Извлечение и возврат результата**: Извлекается сгенерированное стихотворение из ответа OpenAI и возвращается.

**ASCII flowchart**:

```
Промпт --> Отправка запроса в OpenAI (gpt-3.5-turbo)
    |
    --> Получение ответа от OpenAI
    |
    --> Логирование завершения в Helicone
    |
    --> Извлечение стихотворения из ответа
    |
    --> Возврат стихотворения
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
    """
    Анализирует тональность текста.

    Аргументы:
        text (str): Текст для анализа.

    Возвращает:
        str: Результат анализа тональности.
    """
```

**Назначение**: Анализ тональности заданного текста с использованием модели `text-davinci-003` от OpenAI.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1. **Формирование промпта**: Создается промпт для анализа тональности, включающий заданный текст.
2. **Отправка запроса к OpenAI**: Отправляется запрос к API OpenAI с использованием модели `text-davinci-003` и сформированным промптом.
3. **Логирование завершения**: Результат запроса (анализ тональности) логируется с использованием клиента Helicone.
4. **Извлечение и возврат результата**: Извлекается результат анализа тональности из ответа OpenAI и возвращается.

**ASCII flowchart**:

```
Текст --> Формирование промпта для анализа тональности
    |
    --> Отправка запроса в OpenAI (text-davinci-003)
    |
    --> Получение ответа от OpenAI
    |
    --> Логирование завершения в Helicone
    |
    --> Извлечение результата анализа тональности из ответа
    |
    --> Возврат результата
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
    """
    Создает краткое изложение текста.

    Аргументы:
        text (str): Текст для изложения.

    Возвращает:
        str: Краткое изложение текста.
    """
```

**Назначение**: Создание краткого изложения заданного текста с использованием модели `text-davinci-003` от OpenAI.

**Параметры**:
- `text` (str): Текст для изложения.

**Возвращает**:
- `str`: Краткое изложение текста.

**Как работает функция**:
1. **Формирование промпта**: Создается промпт для суммаризации, включающий заданный текст.
2. **Отправка запроса к OpenAI**: Отправляется запрос к API OpenAI с использованием модели `text-davinci-003` и сформированным промптом.
3. **Логирование завершения**: Результат запроса (краткое изложение) логируется с использованием клиента Helicone.
4. **Извлечение и возврат результата**: Извлекается краткое изложение из ответа OpenAI и возвращается.

**ASCII flowchart**:

```
Текст --> Формирование промпта для суммаризации
    |
    --> Отправка запроса в OpenAI (text-davinci-003)
    |
    --> Получение ответа от OpenAI
    |
    --> Логирование завершения в Helicone
    |
    --> Извлечение краткого изложения из ответа
    |
    --> Возврат результата
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
    """
    Переводит текст на указанный язык.

    Аргументы:
        text (str): Текст для перевода.
        target_language (str): Целевой язык перевода.

    Возвращает:
        str: Переведенный текст.
    """
```

**Назначение**: Перевод заданного текста на указанный целевой язык с использованием модели `text-davinci-003` от OpenAI.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1. **Формирование промпта**: Создается промпт для перевода, включающий заданный текст и целевой язык.
2. **Отправка запроса к OpenAI**: Отправляется запрос к API OpenAI с использованием модели `text-davinci-003` и сформированным промптом.
3. **Логирование завершения**: Результат запроса (переведенный текст) логируется с использованием клиента Helicone.
4. **Извлечение и возврат результата**: Извлекается переведенный текст из ответа OpenAI и возвращается.

**ASCII flowchart**:

```
Текст, Целевой язык --> Формирование промпта для перевода
    |
    --> Отправка запроса в OpenAI (text-davinci-003)
    |
    --> Получение ответа от OpenAI
    |
    --> Логирование завершения в Helicone
    |
    --> Извлечение переведенного текста из ответа
    |
    --> Возврат результата
```

**Примеры**:
```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```

### `main`

```python
def main():
    """
    Основная функция для демонстрации работы с HeliconeAI.
    """
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\n", translation)
```

**Назначение**: Функция `main` демонстрирует использование класса `HeliconeAI` для выполнения различных задач обработки текста, таких как генерация стихов, анализ тональности, суммаризация и перевод текста.

**Как работает функция**:
1. **Создание экземпляра класса `HeliconeAI`**: Создается экземпляр класса `HeliconeAI` для взаимодействия с сервисами Helicone AI и OpenAI.
2. **Генерация стихотворения**: Вызывается метод `generate_poem` для генерации стихотворения на основе заданного промпта.
3. **Анализ тональности**: Вызывается метод `analyze_sentiment` для анализа тональности заданного текста.
4. **Суммаризация текста**: Вызывается метод `summarize_text` для создания краткого изложения заданного текста.
5. **Перевод текста**: Вызывается метод `translate_text` для перевода заданного текста на указанный язык.
6. **Вывод результатов**: Результаты каждой операции выводятся на экран.

**ASCII flowchart**:

```
Начало --> Создание экземпляра HeliconeAI
    |
    --> Генерация стихотворения (generate_poem)
    |
    --> Анализ тональности (analyze_sentiment)
    |
    --> Суммаризация текста (summarize_text)
    |
    --> Перевод текста (translate_text)
    |
    --> Вывод результатов
    |
    Конец
```

**Примеры**:

```python
if __name__ == "__main__":
    main()