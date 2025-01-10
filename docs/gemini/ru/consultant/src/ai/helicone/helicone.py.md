# Анализ кода модуля `helicone.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используются классы и функции.
    - Присутствует документация для функций в формате docstring.
    - Используется библиотека `helicone` для логирования запросов.
- Минусы
    - Не хватает обработки ошибок и логирования.
    - Используются двойные кавычки вместо одинарных для строк в коде.
    - Не импортирован `logger` из `src.logger.logger`.
    - Отсутствует описание модуля в начале файла.
    - Нет явного указания типа возвращаемых данных в docstring.
    - Не все импорты на месте, необходимо добавить `from src.logger.logger import logger` и `from pathlib import Path`.

**Рекомендации по улучшению**
- Добавить описание модуля в начале файла в формате docstring.
- Исправить использование двойных кавычек на одинарные внутри кода.
- Добавить обработку ошибок с использованием `try-except` и логирование ошибок с помощью `logger.error`.
- Добавить импорт `logger` из `src.logger.logger`.
- Добавить импорт `Path` из `pathlib`.
- Улучшить docstring, добавив тип возвращаемых данных и примеры использования.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для интеграции с Helicone и OpenAI API
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия с Helicone и OpenAI API.
Он предоставляет методы для генерации текста, анализа тональности, суммирования и перевода текста.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print(poem)
"""
from pathlib import Path
from src.logger.logger import logger
from helicone import Helicone
from openai import OpenAI


class HeliconeAI:
    """
    Класс для взаимодействия с Helicone и OpenAI API.

    Предоставляет методы для генерации текста, анализа тональности,
    суммирования и перевода текста.
    """
    def __init__(self):
        """
        Инициализирует объект HeliconeAI, устанавливает соединение с Helicone и OpenAI.
        """
        self.helicone = Helicone()
        self.client = OpenAI()

    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.

        Args:
            prompt (str): Промпт для генерации стихотворения.

        Returns:
            str: Сгенерированное стихотворение.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
            >>> print(poem)
            ...
        """
        try:
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            self.helicone.log_completion(response)
            return response.choices[0].message.content
        except Exception as ex:
            logger.error(f'Ошибка при генерации стихотворения: {ex}')
            return ''

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность текста.

        Args:
            text (str): Текст для анализа.

        Returns:
            str: Результат анализа тональности.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
            >>> print(sentiment)
            ...
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            self.helicone.log_completion(response)
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error(f'Ошибка при анализе тональности: {ex}')
            return ''

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение текста.

        Args:
            text (str): Текст для изложения.

        Returns:
            str: Краткое изложение текста.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> summary = helicone_ai.summarize_text('Длинный текст для изложения...')
            >>> print(summary)
            ...
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            self.helicone.log_completion(response)
            return response.choices[0].text.strip()
        except Exception as ex:
             logger.error(f'Ошибка при суммировании текста: {ex}')
             return ''

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит текст на указанный язык.

        Args:
            text (str): Текст для перевода.
            target_language (str): Целевой язык перевода.

        Returns:
            str: Переведенный текст.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
            >>> print(translation)
            ...
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            self.helicone.log_completion(response)
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error(f'Ошибка при переводе текста: {ex}')
            return ''

def main():
    """
    Основная функция для демонстрации работы класса HeliconeAI.
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