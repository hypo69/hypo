# Анализ кода модуля `helicone`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используется класс для инкапсуляции функциональности.
    - Присутствуют docstring для каждой функции, описывающие её назначение, аргументы и возвращаемое значение.
    - Код соответствует PEP8.
- Минусы
    - Отсутствует обработка ошибок.
    - Не используется `logger` для логирования ошибок и информации, что затрудняет отладку.
    - Не все импорты использованы (например, `header`).
    - Нет документации для модуля.
    - Не все строки соответствуют стандарту оформления docstring в Python (для Sphinx).

**Рекомендации по улучшению**

1. **Добавить описание модуля**: В начале файла добавить описание модуля в формате rst.
2. **Улучшить документацию**: Документацию для каждой функции, метода и переменной, соблюдая стандарты оформления docstring в Python (для Sphinx).
3. **Использовать logger**: Заменить `print` на `logger` для вывода информации и ошибок.
4. **Обработка ошибок**: Добавить обработку ошибок, используя `try-except` с логированием ошибок через `logger.error`.
5. **Удалить неиспользуемые импорты**: Удалить `import header`, так как он не используется в коде.
6. **Улучшить форматирование**: Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
7. **Использовать одинарные кавычки**: Всегда использовать одинарные кавычки (`'`) в коде Python, двойные только в операциях вывода.
8. **Добавить примеры использования**: Добавить примеры использования функций в docstring.
9.  **Избегать избыточного использования стандартных блоков try-except**: Предпочитать обработку ошибок с помощью `logger.error`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для взаимодействия с Helicone и OpenAI API
=================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия с Helicone API и OpenAI API для выполнения различных задач, таких как генерация текста, анализ тональности, суммирование текста и перевод.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print(f"Generated Poem:\\n {poem}")
"""
from src.logger import logger
from helicone import Helicone
from openai import OpenAI
from typing import Any

class HeliconeAI:
    """
    Класс для взаимодействия с Helicone и OpenAI API.

    Этот класс предоставляет методы для генерации текста, анализа тональности,
    суммирования текста и перевода.

    Attributes:
        helicone (Helicone): Объект для взаимодействия с Helicone API.
        client (OpenAI): Объект для взаимодействия с OpenAI API.
    """
    def __init__(self):
        """
        Инициализирует объект HeliconeAI.
        """
        # Инициализирует Helicone API
        self.helicone = Helicone()
        # Инициализирует OpenAI API
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
            >>> poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
            >>> print(poem)
            "Стихотворение про кота..."
        """
        try:
            # Код исполняет запрос к OpenAI API для генерации стихотворения
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            # Логирует результат запроса в Helicone
            self.helicone.log_completion(response)
            # Возвращает сгенерированное стихотворение
            return response.choices[0].message.content
        except Exception as e:
            # Логирует ошибку, если запрос не удался
            logger.error(f'Ошибка при генерации стихотворения: {e}')
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
           >>> sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
           >>> print(sentiment)
           "Положительный"
        """
        try:
             # Код исполняет запрос к OpenAI API для анализа тональности текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            # Логирует результат запроса в Helicone
            self.helicone.log_completion(response)
            # Возвращает результат анализа тональности
            return response.choices[0].text.strip()
        except Exception as e:
            # Логирует ошибку, если запрос не удался
            logger.error(f'Ошибка при анализе тональности: {e}')
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
           >>> summary = helicone_ai.summarize_text("Длинный текст для изложения...")
           >>> print(summary)
           "Краткое изложение текста..."
        """
        try:
            # Код исполняет запрос к OpenAI API для суммирования текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            # Логирует результат запроса в Helicone
            self.helicone.log_completion(response)
             # Возвращает краткое изложение текста
            return response.choices[0].text.strip()
        except Exception as e:
            # Логирует ошибку, если запрос не удался
            logger.error(f'Ошибка при суммировании текста: {e}')
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
            >>> translation = helicone_ai.translate_text("Hello, how are you?", "русский")
            >>> print(translation)
            "Привет, как дела?"
        """
        try:
            # Код исполняет запрос к OpenAI API для перевода текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            # Логирует результат запроса в Helicone
            self.helicone.log_completion(response)
            # Возвращает переведенный текст
            return response.choices[0].text.strip()
        except Exception as e:
            # Логирует ошибку, если запрос не удался
            logger.error(f'Ошибка при переводе текста: {e}')
            return ''


def main():
    """
    Основная функция для демонстрации работы HeliconeAI.
    """
    # Создает экземпляр класса HeliconeAI
    helicone_ai = HeliconeAI()

    # Генерирует стихотворение
    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print(f'Generated Poem:\\n {poem}')

    # Анализирует тональность текста
    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print(f'Sentiment Analysis:\\n {sentiment}')

    # Суммирует текст
    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print(f'Summary:\\n {summary}')

    # Переводит текст
    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print(f'Translation:\\n {translation}')

if __name__ == '__main__':
    # Выполняет основную функцию, если скрипт запущен напрямую
    main()
```