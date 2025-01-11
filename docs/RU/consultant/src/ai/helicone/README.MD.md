# Анализ кода модуля `src.ai.helicone`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Документация содержит подробное описание класса `HeliconeAI` и его методов.
    *   Примеры использования показывают основные сценарии использования.
    *   Код достаточно ясен и понятен для чтения.
    *   Используются асинхронные вызовы к моделям OpenAI.
-   **Минусы:**
    *   Отсутствует docstring для модуля.
    *   Нет подробных комментариев в коде.
    *   Не используются одинарные кавычки для строк в Python коде.
    *   Не используется `logger` для логирования ошибок.
    *   Нет явной обработки ошибок в методах класса.

**Рекомендации по улучшению:**

1.  Добавить docstring для модуля, описывающий его назначение и основные возможности.
2.  Добавить docstring для класса `HeliconeAI` и каждого его метода, используя формат RST.
3.  Использовать одинарные кавычки для всех строк в Python коде, кроме случаев вывода.
4.  Добавить логирование ошибок с использованием `logger` из `src.logger.logger`.
5.  Добавить обработку ошибок в методах класса с использованием `try-except` и логированием ошибок.
6.  Избегать избыточного использования `try-except` блоков, предпочитая логирование ошибок с помощью `logger.error`.
7.  Добавить комментарии к коду для пояснения логики работы.

**Оптимизированный код:**

```markdown
```rst
.. module:: src.ai.helicone

Модуль для интеграции с Helicone.ai и OpenAI
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия с Helicone.ai и моделями OpenAI, такими как
`gpt-3.5-turbo` и `text-davinci-003`, для выполнения задач генерации стихов, анализа тональности, суммирования и перевода текста.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from src.ai.helicone import HeliconeAI

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)
```
[Русский](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/readme.ru.md)
[About `helicone.ai`](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/about.ru.md)
# HeliconeAI: Integration with Helicone.ai and OpenAI

## Overview

The `HeliconeAI` class is designed to facilitate interaction with Helicone.ai and OpenAI's models. This class provides methods for generating poems, analyzing sentiment, summarizing text, and translating text. It also includes logging of completions using Helicone.ai.

## Key Features

1.  **Poem Generation**:
    -   Generates a poem based on a given prompt using the `gpt-3.5-turbo` model.

2.  **Sentiment Analysis**:
    -   Analyzes the sentiment of a given text using the `text-davinci-003` model.

3.  **Text Summarization**:
    -   Summarizes a given text using the `text-davinci-003` model.

4.  **Text Translation**:
    -   Translates a given text to a specified target language using the `text-davinci-003` model.

5.  **Completion Logging**:
    -   Logs all completions using Helicone.ai for monitoring and analysis.

## Installation

To use the `HeliconeAI` class, ensure you have the necessary dependencies installed. You can install them using pip:

```bash
pip install openai helicone
```

## Usage

### Initialization

Initialize the `HeliconeAI` class:

```python
from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger

class HeliconeAI:
    """
    Класс для взаимодействия с Helicone.ai и OpenAI.

    Этот класс предоставляет методы для генерации стихов, анализа тональности,
    суммирования текста и перевода текста, а также логирование завершений
    с использованием Helicone.ai.
    """
    def __init__(self):
        """
        Инициализация клиента Helicone и клиента OpenAI.
        """
        self.helicone = Helicone()
        self.client = OpenAI()
```

### Methods

#### Generate Poem

Generate a poem based on a given prompt:

```python
    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного запроса.

        Args:
            prompt (str): Запрос для генерации стихотворения.

        Returns:
            str: Сгенерированное стихотворение.
        
        """
        try:
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].message.content
        except Exception as ex:
            logger.error(f'Ошибка при генерации стихотворения: {ex}')
            return ''
```

#### Analyze Sentiment

Analyze the sentiment of a given text:

```python
    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        Args:
            text (str): Текст для анализа тональности.

        Returns:
            str: Результат анализа тональности.
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error(f'Ошибка при анализе тональности: {ex}')
            return ''
```

#### Summarize Text

Summarize a given text:

```python
    def summarize_text(self, text: str) -> str:
        """
        Суммирует заданный текст.

        Args:
            text (str): Текст для суммирования.

        Returns:
            str: Суммированный текст.
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error(f'Ошибка при суммировании текста: {ex}')
            return ''
```

#### Translate Text

Translate a given text to a specified target language:

```python
    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный язык.

        Args:
            text (str): Текст для перевода.
            target_language (str): Язык, на который нужно перевести текст.

        Returns:
            str: Переведенный текст.
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].text.strip()
        except Exception as ex:
           logger.error(f'Ошибка при переводе текста: {ex}')
           return ''
```

### Example Usage

Here is an example of how to use the `HeliconeAI` class:

```python
def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print('Generated Poem:\\n', poem)

    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print('Sentiment Analysis:\\n', sentiment)

    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print('Summary:\\n', summary)

    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print('Translation:\\n', translation)

if __name__ == '__main__':
    main()
```

## Dependencies

- `helicone`
- `openai`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more detailed information, refer to the source code and comments within the `HeliconeAI` class.
```
```python
"""
Модуль для интеграции с Helicone.ai и OpenAI
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия с Helicone.ai и моделями OpenAI, такими как
`gpt-3.5-turbo` и `text-davinci-003`, для выполнения задач генерации стихов, анализа тональности, суммирования и перевода текста.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from src.ai.helicone import HeliconeAI

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)
"""
from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger # Импортирует logger


class HeliconeAI:
    """
    Класс для взаимодействия с Helicone.ai и OpenAI.

    Этот класс предоставляет методы для генерации стихов, анализа тональности,
    суммирования текста и перевода текста, а также логирование завершений
    с использованием Helicone.ai.
    """
    def __init__(self):
        """
        Инициализация клиента Helicone и клиента OpenAI.
        """
        self.helicone = Helicone()
        self.client = OpenAI()


    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного запроса.

        Args:
            prompt (str): Запрос для генерации стихотворения.

        Returns:
            str: Сгенерированное стихотворение.
        
        """
        try:
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].message.content
        except Exception as ex:
            # Код регистрирует ошибку
            logger.error(f'Ошибка при генерации стихотворения: {ex}')
            return ''


    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        Args:
            text (str): Текст для анализа тональности.

        Returns:
            str: Результат анализа тональности.
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
             # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].text.strip()
        except Exception as ex:
             # Код регистрирует ошибку
            logger.error(f'Ошибка при анализе тональности: {ex}')
            return ''


    def summarize_text(self, text: str) -> str:
        """
        Суммирует заданный текст.

        Args:
            text (str): Текст для суммирования.

        Returns:
            str: Суммированный текст.
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].text.strip()
        except Exception as ex:
            # Код регистрирует ошибку
            logger.error(f'Ошибка при суммировании текста: {ex}')
            return ''


    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный язык.

        Args:
            text (str): Текст для перевода.
            target_language (str): Язык, на который нужно перевести текст.

        Returns:
            str: Переведенный текст.
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            # Код регистрирует результат в helicone
            self.helicone.log_completion(response)
            # Код возвращает текст сообщения
            return response.choices[0].text.strip()
        except Exception as ex:
            # Код регистрирует ошибку
           logger.error(f'Ошибка при переводе текста: {ex}')
           return ''


def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print('Generated Poem:\\n', poem)

    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print('Sentiment Analysis:\\n', sentiment)

    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print('Summary:\\n', summary)

    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print('Translation:\\n', translation)

if __name__ == '__main__':
    main()
```