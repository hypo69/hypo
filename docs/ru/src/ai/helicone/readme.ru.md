# Модуль `src.ai.helicone`

## Обзор

Модуль предоставляет интеграцию с Helicone.ai и OpenAI, упрощая взаимодействие с этими сервисами. Он включает класс `HeliconeAI`, который позволяет генерировать стихи, анализировать тональность текста, создавать краткие изложения и переводить текст, а также логировать завершения с использованием Helicone.ai.

## Подробнее

Этот модуль облегчает использование возможностей Helicone.ai и OpenAI для различных задач обработки текста. Он предоставляет удобный интерфейс для выполнения таких операций, как генерация стихов, анализ тональности, создание кратких изложений и перевод текста. Модуль также обеспечивает логирование всех операций через Helicone.ai для мониторинга и анализа.

## Классы

### `HeliconeAI`

**Описание**: Класс для взаимодействия с Helicone.ai и OpenAI.

**Как работает класс**:
Класс `HeliconeAI` инициализируется с использованием клиентов `Helicone` и `OpenAI`. Он предоставляет методы для выполнения различных задач, таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста. Все методы используют API OpenAI и логируют завершения с помощью Helicone.ai.

**Методы**:
- `__init__`: Инициализирует класс `HeliconeAI` с клиентами `Helicone` и `OpenAI`.
- `generate_poem`: Генерирует стихотворение на основе заданного промпта.
- `analyze_sentiment`: Анализирует тональность заданного текста.
- `summarize_text`: Создает краткое изложение заданного текста.
- `translate_text`: Переводит заданный текст на указанный целевой язык.

#### `__init__`

```python
def __init__(self):
    """
    Инициализирует класс HeliconeAI с клиентами Helicone и OpenAI.

    Args:
        self: Объект класса HeliconeAI.

    Returns:
        None

    Raises:
        None
    """
    self.helicone = Helicone()
    self.client = OpenAI()
```

**Как работает функция**:
Функция `__init__` инициализирует класс `HeliconeAI` путем создания экземпляров классов `Helicone` и `OpenAI` и присваивания их атрибутам `helicone` и `client` соответственно. Это позволяет использовать методы Helicone.ai и OpenAI для выполнения различных задач.

**Параметры**:
- `self`: Ссылка на экземпляр класса `HeliconeAI`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

#### `generate_poem`

```python
def generate_poem(self, prompt: str) -> str:
    """
    Генерирует стихотворение на основе заданного промпта с использованием модели `gpt-3.5-turbo`.

    Args:
        prompt (str): Промпт для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с OpenAI.
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

**Как работает функция**:
Функция `generate_poem` принимает текстовый промпт и использует модель `gpt-3.5-turbo` для генерации стихотворения на основе этого промпта. Она отправляет запрос к API OpenAI, получает ответ и логирует завершение с использованием Helicone.ai. Затем возвращает сгенерированное стихотворение.

**Параметры**:
- `self`: Ссылка на экземпляр класса `HeliconeAI`.
- `prompt` (str): Промпт для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при взаимодействии с OpenAI.

#### `analyze_sentiment`

```python
def analyze_sentiment(self, text: str) -> str:
    """
    Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

    Args:
        text (str): Текст для анализа тональности.

    Returns:
        str: Результат анализа тональности.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с OpenAI.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Как работает функция**:
Функция `analyze_sentiment` принимает текст и использует модель `text-davinci-003` для анализа его тональности. Она формирует промпт для OpenAI, отправляет запрос к API OpenAI, получает ответ и логирует завершение с использованием Helicone.ai. Затем возвращает результат анализа тональности.

**Параметры**:
- `self`: Ссылка на экземпляр класса `HeliconeAI`.
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при взаимодействии с OpenAI.

#### `summarize_text`

```python
def summarize_text(self, text: str) -> str:
    """
    Создает краткое изложение заданного текста с использованием модели `text-davinci-003`.

    Args:
        text (str): Текст для создания краткого изложения.

    Returns:
        str: Краткое изложение текста.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с OpenAI.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Как работает функция**:
Функция `summarize_text` принимает текст и использует модель `text-davinci-003` для создания краткого изложения этого текста. Она формирует промпт для OpenAI, отправляет запрос к API OpenAI, получает ответ и логирует завершение с использованием Helicone.ai. Затем возвращает краткое изложение текста.

**Параметры**:
- `self`: Ссылка на экземпляр класса `HeliconeAI`.
- `text` (str): Текст для создания краткого изложения.

**Возвращает**:
- `str`: Краткое изложение текста.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при взаимодействии с OpenAI.

#### `translate_text`

```python
def translate_text(self, text: str, target_language: str) -> str:
    """
    Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

    Args:
        text (str): Текст для перевода.
        target_language (str): Целевой язык для перевода.

    Returns:
        str: Переведенный текст.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с OpenAI.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=200
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Как работает функция**:
Функция `translate_text` принимает текст и целевой язык и использует модель `text-davinci-003` для перевода текста на указанный язык. Она формирует промпт для OpenAI, отправляет запрос к API OpenAI, получает ответ и логирует завершение с использованием Helicone.ai. Затем возвращает переведенный текст.

**Параметры**:
- `self`: Ссылка на экземпляр класса `HeliconeAI`.
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при взаимодействии с OpenAI.

## Функции

### `main`

```python
def main():
    """
    Пример использования класса HeliconeAI для генерации стихотворения,
    анализа тональности, создания краткого изложения и перевода текста.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка в процессе выполнения.
    """
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

**Как работает функция**:
Функция `main` является примером использования класса `HeliconeAI`. Она создает экземпляр класса `HeliconeAI`, генерирует стихотворение, анализирует тональность текста, создает краткое изложение и переводит текст. Результаты выводятся в консоль.

**Параметры**:
- Отсутствуют

**Возвращает**:
- Отсутствует

**Вызывает исключения**:
- `Exception`: Если возникает ошибка в процессе выполнения.