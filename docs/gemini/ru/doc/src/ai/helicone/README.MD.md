# Документация модуля `src.ai.helicone`

## Обзор

Модуль `src.ai.helicone` предоставляет класс `HeliconeAI`, предназначенный для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс включает методы для генерации стихов, анализа тональности текста, суммирования текста и его перевода, а также для логирования завершений с использованием Helicone.ai.

## Подробней

Модуль предназначен для интеграции с сервисами Helicone.ai и OpenAI, позволяя разработчикам легко использовать возможности искусственного интеллекта для различных задач, таких как создание контента, анализ текста и перевод. Он предоставляет удобный интерфейс для работы с моделями OpenAI и обеспечивает логирование всех запросов через Helicone.ai.

## Классы

### `HeliconeAI`

**Описание**: Класс `HeliconeAI` предназначен для взаимодействия с Helicone.ai и OpenAI. Он предоставляет методы для генерации стихов, анализа тональности, суммирования и перевода текста, а также логирует все завершения с использованием Helicone.ai.

**Принцип работы**:

1.  **Инициализация**: При инициализации создаются экземпляры клиентов `Helicone` и `OpenAI`.
2.  **Методы**: Класс содержит методы для выполнения различных задач обработки текста с использованием моделей OpenAI. Каждый метод отправляет запрос в OpenAI и логирует завершение через Helicone.ai.

**Аттрибуты**:

*   `helicone` (Helicone): Экземпляр клиента Helicone для логирования завершений.
*   `client` (OpenAI): Экземпляр клиента OpenAI для выполнения запросов к моделям.

**Методы**:

*   `generate_poem(prompt: str) -> str`: Генерирует стихотворение на основе заданного запроса.
*   `analyze_sentiment(text: str) -> str`: Анализирует тональность заданного текста.
*   `summarize_text(text: str) -> str`: Суммирует заданный текст.
*   `translate_text(text: str, target_language: str) -> str`: Переводит заданный текст на указанный язык.

## Функции

### `generate_poem`

```python
def generate_poem(self, prompt: str) -> str:
    """Генерирует стихотворение на основе заданного запроса.

    Args:
        prompt (str): Запрос для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.
    """
```

**Назначение**: Генерирует стихотворение на основе заданного запроса, используя модель `gpt-3.5-turbo` от OpenAI.

**Параметры**:

*   `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:

*   `str`: Сгенерированное стихотворение.

**Как работает функция**:

1.  Отправка запроса: Функция отправляет запрос в OpenAI с использованием модели `gpt-3.5-turbo` и заданным запросом.
2.  Логирование завершения: Результат запроса логируется с использованием `self.helicone.log_completion(response)`.
3.  Возврат результата: Функция возвращает сгенерированное стихотворение.

```
Запрос в OpenAI
    ↓
Логирование завершения через Helicone
    ↓
Возврат сгенерированного стихотворения
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
    """Анализирует тональность заданного текста.

    Args:
        text (str): Текст для анализа тональности.

    Returns:
        str: Результат анализа тональности текста.
    """
```

**Назначение**: Анализирует тональность заданного текста, используя модель `text-davinci-003` от OpenAI.

**Параметры**:

*   `text` (str): Текст для анализа тональности.

**Возвращает**:

*   `str`: Результат анализа тональности текста.

**Как работает функция**:

1.  Отправка запроса: Функция отправляет запрос в OpenAI с использованием модели `text-davinci-003` и заданным текстом.
2.  Логирование завершения: Результат запроса логируется с использованием `self.helicone.log_completion(response)`.
3.  Возврат результата: Функция возвращает результат анализа тональности текста.

```
Запрос в OpenAI
    ↓
Логирование завершения через Helicone
    ↓
Возврат результата анализа тональности
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
    """Суммирует заданный текст.

    Args:
        text (str): Текст для суммирования.

    Returns:
        str: Суммированный текст.
    """
```

**Назначение**: Суммирует заданный текст, используя модель `text-davinci-003` от OpenAI.

**Параметры**:

*   `text` (str): Текст для суммирования.

**Возвращает**:

*   `str`: Суммированный текст.

**Как работает функция**:

1.  Отправка запроса: Функция отправляет запрос в OpenAI с использованием модели `text-davinci-003` и заданным текстом.
2.  Логирование завершения: Результат запроса логируется с использованием `self.helicone.log_completion(response)`.
3.  Возврат результата: Функция возвращает суммированный текст.

```
Запрос в OpenAI
    ↓
Логирование завершения через Helicone
    ↓
Возврат суммированного текста
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
    """Переводит заданный текст на указанный язык.

    Args:
        text (str): Текст для перевода.
        target_language (str): Язык, на который нужно перевести текст.

    Returns:
        str: Переведенный текст.
    """
```

**Назначение**: Переводит заданный текст на указанный язык, используя модель `text-davinci-003` от OpenAI.

**Параметры**:

*   `text` (str): Текст для перевода.
*   `target_language` (str): Язык, на который нужно перевести текст.

**Возвращает**:

*   `str`: Переведенный текст.

**Как работает функция**:

1.  Отправка запроса: Функция отправляет запрос в OpenAI с использованием модели `text-davinci-003` и заданным текстом и языком перевода.
2.  Логирование завершения: Результат запроса логируется с использованием `self.helicone.log_completion(response)`.
3.  Возврат результата: Функция возвращает переведенный текст.

```
Запрос в OpenAI
    ↓
Логирование завершения через Helicone
    ↓
Возврат переведенного текста
```

**Примеры**:

```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```