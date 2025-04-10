# Модуль для интеграции с HeliconeAI
## Обзор

Модуль `helicone.py` предоставляет интеграцию с платформой HeliconeAI для работы с моделями OpenAI. Он содержит класс `HeliconeAI`, который упрощает взаимодействие с API OpenAI и логирование запросов через Helicone.

## Подробней

Этот модуль предназначен для упрощения работы с AI-сервисами, предоставляемыми OpenAI, через интеграцию с Helicone. Helicone позволяет логировать и анализировать запросы к API, что полезно для отслеживания использования, отладки и оптимизации затрат. Модуль предоставляет удобный интерфейс для выполнения различных задач, таких как генерация стихов, анализ тональности текста, создание кратких изложений и перевод текста на другие языки.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предоставляет методы для взаимодействия с OpenAI API и логирования запросов через Helicone.

**Принцип работы**:
Класс инициализируется с использованием клиентов `Helicone` и `OpenAI`. Методы класса используют эти клиенты для выполнения запросов к OpenAI API и логирования результатов с помощью Helicone. Это позволяет отслеживать и анализировать использование API.

**Аттрибуты**:
- `helicone`: Объект класса `Helicone` для логирования запросов.
- `client`: Объект класса `OpenAI` для взаимодействия с OpenAI API.

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

    Args:
        prompt (str): Промпт для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.
    """
```

**Назначение**: Генерация стихотворения на основе заданного текстового промпта с использованием модели `gpt-3.5-turbo` от OpenAI.

**Параметры**:
- `prompt` (str): Текст запроса, на основе которого генерируется стихотворение.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Как работает функция**:
1. Функция принимает текстовый `prompt` в качестве аргумента.
2. Использует клиент `OpenAI` для отправки запроса к модели `gpt-3.5-turbo` с ролью "user" и содержанием, равным `prompt`.
3. Получает ответ от модели в виде сгенерированного стихотворения.
4. Логирует завершение запроса с помощью `self.helicone.log_completion(response)`.
5. Извлекает текст стихотворения из ответа и возвращает его.

**ASCII Flowchart**:

```
   Промпт
   ↓
   OpenAI API (gpt-3.5-turbo)
   ↓
   Сгенерированное стихотворение
   ↓
   Логирование через Helicone
   ↓
   Возврат стихотворения
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

    Args:
        text (str): Текст для анализа.

    Returns:
        str: Результат анализа тональности.
    """
```

**Назначение**: Анализ тональности заданного текста с использованием модели `text-davinci-003` от OpenAI.

**Параметры**:
- `text` (str): Текст, для которого необходимо определить тональность.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1. Функция принимает текст `text` в качестве аргумента.
2. Формирует промпт для анализа тональности, добавляя текст в запрос к модели `text-davinci-003`.
3. Отправляет запрос к OpenAI API с использованием сформированного промпта и модели `text-davinci-003`.
4. Логирует завершение запроса с помощью `self.helicone.log_completion(response)`.
5. Извлекает результат анализа тональности из ответа, удаляет лишние пробелы и возвращает его.

**ASCII Flowchart**:

```
   Текст
   ↓
   Формирование промпта
   ↓
   OpenAI API (text-davinci-003)
   ↓
   Результат анализа тональности
   ↓
   Логирование через Helicone
   ↓
   Возврат результата
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

    Args:
        text (str): Текст для изложения.

    Returns:
        str: Краткое изложение текста.
    """
```

**Назначение**: Создание краткого изложения заданного текста с использованием модели `text-davinci-003` от OpenAI.

**Параметры**:
- `text` (str): Текст, для которого необходимо создать краткое изложение.

**Возвращает**:
- `str`: Краткое изложение текста.

**Как работает функция**:
1. Функция принимает текст `text` в качестве аргумента.
2. Формирует промпт для создания краткого изложения, добавляя текст в запрос к модели `text-davinci-003`.
3. Отправляет запрос к OpenAI API с использованием сформированного промпта и модели `text-davinci-003`.
4. Логирует завершение запроса с помощью `self.helicone.log_completion(response)`.
5. Извлекает краткое изложение текста из ответа, удаляет лишние пробелы и возвращает его.

**ASCII Flowchart**:

```
   Текст
   ↓
   Формирование промпта
   ↓
   OpenAI API (text-davinci-003)
   ↓
   Краткое изложение текста
   ↓
   Логирование через Helicone
   ↓
   Возврат изложения
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

    Args:
        text (str): Текст для перевода.
        target_language (str): Целевой язык перевода.

    Returns:
        str: Переведенный текст.
    """
```

**Назначение**: Перевод заданного текста на указанный целевой язык с использованием модели `text-davinci-003` от OpenAI.

**Параметры**:
- `text` (str): Текст, который необходимо перевести.
- `target_language` (str): Язык, на который необходимо перевести текст.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1. Функция принимает текст `text` и целевой язык `target_language` в качестве аргументов.
2. Формирует промпт для перевода текста на указанный язык, добавляя текст и язык в запрос к модели `text-davinci-003`.
3. Отправляет запрос к OpenAI API с использованием сформированного промпта и модели `text-davinci-003`.
4. Логирует завершение запроса с помощью `self.helicone.log_completion(response)`.
5. Извлекает переведенный текст из ответа, удаляет лишние пробелы и возвращает его.

**ASCII Flowchart**:

```
   Текст, Язык
   ↓
   Формирование промпта
   ↓
   OpenAI API (text-davinci-003)
   ↓
   Переведенный текст
   ↓
   Логирование через Helicone
   ↓
   Возврат перевода
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
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\\n", translation)
```

**Назначение**: Функция `main` демонстрирует использование класса `HeliconeAI` для выполнения различных задач, таких как генерация стихов, анализ тональности текста, создание кратких изложений и перевод текста.

**Как работает функция**:
1. Создает экземпляр класса `HeliconeAI`.
2. Вызывает метод `generate_poem` для генерации стихотворения на основе заданного промпта.
3. Выводит сгенерированное стихотворение на экран.
4. Вызывает метод `analyze_sentiment` для анализа тональности текста.
5. Выводит результат анализа тональности на экран.
6. Вызывает метод `summarize_text` для создания краткого изложения текста.
7. Выводит краткое изложение на экран.
8. Вызывает метод `translate_text` для перевода текста на русский язык.
9. Выводит переведенный текст на экран.

**ASCII Flowchart**:

```
   Создание HeliconeAI
   ↓
   Генерация стихотворения
   ↓
   Анализ тональности
   ↓
   Создание изложения
   ↓
   Перевод текста
   ↓
   Вывод результатов
```

**Примеры**:

```python
if __name__ == "__main__":
    main()