# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для облегчения взаимодействия с моделями Helicone.ai и OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности, суммирования текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Основные особенности

1. **Генерация стихов**:
   - Генерирует стихотворение на основе заданного запроса с использованием модели `gpt-3.5-turbo`.

2. **Анализ тональности**:
   - Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

3. **Суммирование текста**:
   - Суммирует заданный текст с использованием модели `text-davinci-003`.

4. **Перевод текста**:
   - Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

5. **Логирование завершений**:
   - Регистрирует все завершения с использованием Helicone.ai для мониторинга и анализа.

## Установка

Чтобы использовать класс `HeliconeAI`, убедитесь, что у вас установлены необходимые зависимости. Вы можете установить их с помощью pip:

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

Генерирует стихотворение на основе заданного запроса:

```python
def generate_poem(self, prompt: str) -> str:
    """Генерирует стихотворение на основе заданного запроса.

    Args:
        prompt (str): Запрос для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.
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
Функция `generate_poem` принимает строку `prompt` в качестве аргумента, который служит запросом для генерации стихотворения. Она использует клиент OpenAI для создания завершения чата с моделью `gpt-3.5-turbo`. Затем функция регистрирует это завершение с помощью Helicone и возвращает сгенерированное стихотворение из ответа OpenAI.

Внутри функции происходят следующие действия и преобразования:
A. Клиент OpenAI отправляет запрос на генерацию стихотворения с использованием модели `gpt-3.5-turbo`.
|
B. Helicone регистрирует завершение, полученное от OpenAI.
|
C. Функция возвращает сгенерированное стихотворение.

#### `analyze_sentiment`

Анализирует тональность заданного текста:

```python
def analyze_sentiment(self, text: str) -> str:
    """Анализирует тональность заданного текста.

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

**Как работает функция**:
Функция `analyze_sentiment` принимает строку `text` в качестве аргумента, который представляет собой текст для анализа тональности. Она использует клиент OpenAI для создания завершения с моделью `text-davinci-003`, запрашивая анализ тональности предоставленного текста. Затем функция регистрирует это завершение с помощью Helicone и возвращает результат анализа тональности.

Внутри функции происходят следующие действия и преобразования:
A. Клиент OpenAI отправляет запрос на анализ тональности с использованием модели `text-davinci-003`.
|
B. Helicone регистрирует завершение, полученное от OpenAI.
|
C. Функция возвращает результат анализа тональности.

#### `summarize_text`

Суммирует заданный текст:

```python
def summarize_text(self, text: str) -> str:
    """Суммирует заданный текст.

    Args:
        text (str): Текст для суммирования.

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

**Как работает функция**:
Функция `summarize_text` принимает строку `text` в качестве аргумента, который представляет собой текст для суммирования. Она использует клиент OpenAI для создания завершения с моделью `text-davinci-003`, запрашивая суммирование предоставленного текста. Затем функция регистрирует это завершение с помощью Helicone и возвращает суммированный текст.

Внутри функции происходят следующие действия и преобразования:
A. Клиент OpenAI отправляет запрос на суммирование текста с использованием модели `text-davinci-003`.
|
B. Helicone регистрирует завершение, полученное от OpenAI.
|
C. Функция возвращает суммированный текст.

#### `translate_text`

Переводит заданный текст на указанный целевой язык:

```python
def translate_text(self, text: str, target_language: str) -> str:
    """Переводит заданный текст на указанный целевой язык.

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

**Как работает функция**:
Функция `translate_text` принимает две строки в качестве аргументов: `text`, который представляет собой текст для перевода, и `target_language`, который представляет собой целевой язык для перевода. Она использует клиент OpenAI для создания завершения с моделью `text-davinci-003`, запрашивая перевод предоставленного текста на указанный язык. Затем функция регистрирует это завершение с помощью Helicone и возвращает переведенный текст.

Внутри функции происходят следующие действия и преобразования:
A. Клиент OpenAI отправляет запрос на перевод текста с использованием модели `text-davinci-003`.
|
B. Helicone регистрирует завершение, полученное от OpenAI.
|
C. Функция возвращает переведенный текст.

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