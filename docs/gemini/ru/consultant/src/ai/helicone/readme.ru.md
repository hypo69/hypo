# Анализ кода модуля `src.ai.helicone`

**Качество кода: 7/10**
- **Плюсы:**
    - Код предоставляет базовую интеграцию с Helicone.ai и OpenAI.
    - Есть примеры использования для основных методов.
    - Документация в формате Markdown.
- **Минусы:**
    - Отсутствует описание модуля в начале файла.
    - Не хватает документации в формате RST для функций и методов.
    - Используются стандартные `print` для вывода, предпочтительнее использовать `logger`.
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Не используются одинарные кавычки в коде python.
    - Нет проверки на существование токена OpenAI.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла в формате RST.
2.  Добавить документацию в формате RST для каждого метода.
3.  Использовать `logger` для логирования вместо `print`.
4.  Убрать стандартные блоки `try-except` и использовать `logger.error` для обработки ошибок.
5.  Использовать одинарные кавычки в коде python.
6.  Добавить проверку на существование токена OpenAI.
7.  Переименовать переменные `response` на более информативные (например, `chat_response`, `completion_response`).

**Оптимизированный код**

```python
"""
Модуль для интеграции с Helicone.ai и OpenAI
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия
с Helicone.ai и моделями OpenAI для выполнения различных задач,
таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from src.ai.helicone import HeliconeAI
    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print('Generated Poem:\\n', poem)
"""
from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger  # Corrected import


class HeliconeAI:
    """
    Класс для интеграции с Helicone.ai и OpenAI.

    Предоставляет методы для генерации стихов, анализа тональности,
    создания краткого изложения текста и перевода текста.
    """

    def __init__(self):
        """
        Инициализирует класс HeliconeAI, устанавливая Helicone и OpenAI клиенты.
        """
        try:
            self.helicone = Helicone()
            self.client = OpenAI()
        except Exception as ex:
            logger.error('Ошибка инициализации HeliconeAI', ex)
            ...

    def generate_poem(self, prompt: str) -> str:
        """Генерирует стихотворение на основе заданного промпта.

        Args:
            prompt (str): Текст запроса для генерации стихотворения.

        Returns:
             str: Сгенерированное стихотворение.
        """
        try:
            chat_response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            self.helicone.log_completion(chat_response)
            return chat_response.choices[0].message.content
        except Exception as ex:
            logger.error('Ошибка генерации стихотворения', ex)
            return ''

    def analyze_sentiment(self, text: str) -> str:
        """Анализирует тональность заданного текста.

        Args:
             text (str): Текст для анализа тональности.

        Returns:
            str: Результат анализа тональности.
        """
        try:
            completion_response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            self.helicone.log_completion(completion_response)
            return completion_response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка анализа тональности', ex)
            return ''

    def summarize_text(self, text: str) -> str:
        """Создает краткое изложение заданного текста.

        Args:
            text (str): Текст для краткого изложения.

        Returns:
            str: Краткое изложение текста.
        """
        try:
            completion_response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            self.helicone.log_completion(completion_response)
            return completion_response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка создания краткого изложения', ex)
            return ''

    def translate_text(self, text: str, target_language: str) -> str:
        """Переводит заданный текст на указанный целевой язык.

        Args:
            text (str): Текст для перевода.
            target_language (str): Целевой язык для перевода.

        Returns:
            str: Переведенный текст.
        """
        try:
            completion_response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            self.helicone.log_completion(completion_response)
            return completion_response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка перевода текста', ex)
            return ''


def main():
    """
    Пример использования класса `HeliconeAI`.
    """
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