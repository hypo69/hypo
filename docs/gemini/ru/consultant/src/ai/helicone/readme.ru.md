# Анализ кода модуля `src.ai.helicone`

**Качество кода**
-  **Плюсы**
    -   Присутствует описание модуля в начале файла.
    -   Есть примеры использования основных методов.
    -   Документация предоставляет общее понимание работы модуля и его основных функций.
- **Минусы**
    -  Отсутствует docstring для модуля и для каждого метода.
    -  Не используются одинарные кавычки в коде python.
    -  Отсутствует импорт `logger`.
    -  Отсутствует обработка ошибок в методах `HeliconeAI`.

**Рекомендации по улучшению**
1. Добавить docstring для модуля и каждого метода для соответствия стандартам оформления docstring в Python.
2. Использовать одинарные кавычки в коде Python, например, `model='gpt-3.5-turbo'`.
3. Добавить импорт `logger` из `src.logger.logger`.
4. Обработать ошибки с помощью `logger.error` в каждом из методов для более надежной работы.
5. Заменить все двойные кавычки на одинарные для параметров `model` и `role`.
6. Предоставить более конкретные примеры в разделе "Пример использования".
7. Добавить более подробное описание методов.
8. Указать типы данных в docstring для параметров функций.
9.  Уточнить формат возвращаемых значений в docstring.
10. Привести в соответствие имена переменных, функций и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для интеграции с Helicone.ai и OpenAI.
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который упрощает взаимодействие с Helicone.ai
и моделями OpenAI для выполнения задач, таких как генерация стихов, анализ тональности текста,
создание кратких изложений и перевод текста. Также включает логирование завершений через Helicone.ai.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from src.ai.helicone import HeliconeAI

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print(f'Сгенерированное стихотворение:\\n {poem}')
"""

from helicone import Helicone # импорт класса Helicone
from openai import OpenAI # импорт класса OpenAI
from src.logger.logger import logger # импорт logger

class HeliconeAI:
    """
    Класс для интеграции с Helicone.ai и OpenAI.

    Предоставляет методы для генерации стихов, анализа тональности,
    создания кратких изложений и перевода текста.
    """
    def __init__(self):
        """
        Инициализирует класс `HeliconeAI` с клиентами Helicone и OpenAI.
        """
        self.helicone = Helicone()
        self.client = OpenAI()

    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.

        Args:
            prompt (str): Текст запроса для генерации стихотворения.

        Returns:
            str: Сгенерированное стихотворение.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
            >>> print(poem)
            "..."
        """
        try:
           # код исполняет запрос к OpenAI для генерации стиха
           response = self.client.chat.completions.create(
               model='gpt-3.5-turbo',
               messages=[
                   {'role': 'user', 'content': prompt}
               ]
           )
           # Код отправляет информацию о завершении в Helicone
           self.helicone.log_completion(response)
           # Код возвращает сгенерированное стихотворение
           return response.choices[0].message.content
        except Exception as ex:
            logger.error('Ошибка при генерации стихотворения', exc_info=ex)
            return '' # TODO: подумать над возвратом

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        Args:
            text (str): Текст для анализа тональности.

        Returns:
            str: Результат анализа тональности.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
            >>> print(sentiment)
            "..."
        """
        try:
            # Код выполняет запрос к OpenAI для анализа тональности
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            # Код отправляет информацию о завершении в Helicone
            self.helicone.log_completion(response)
            # Код возвращает результат анализа тональности
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка при анализе тональности', exc_info=ex)
            return '' # TODO: подумать над возвратом

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение заданного текста.

        Args:
            text (str): Текст для создания краткого изложения.

        Returns:
            str: Краткое изложение текста.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> summary = helicone_ai.summarize_text('Длинный текст для изложения...')
            >>> print(summary)
            "..."
        """
        try:
            # Код выполняет запрос к OpenAI для создания краткого изложения
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            # Код отправляет информацию о завершении в Helicone
            self.helicone.log_completion(response)
            # Код возвращает краткое изложение текста
            return response.choices[0].text.strip()
        except Exception as ex:
             logger.error('Ошибка при создании краткого изложения', exc_info=ex)
             return '' # TODO: подумать над возвратом

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный целевой язык.

        Args:
            text (str): Текст для перевода.
            target_language (str): Целевой язык для перевода.

        Returns:
            str: Переведенный текст.
        
        Example:
            >>> helicone_ai = HeliconeAI()
            >>> translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
            >>> print(translation)
            "..."
        """
        try:
            # Код выполняет запрос к OpenAI для перевода текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            # Код отправляет информацию о завершении в Helicone
            self.helicone.log_completion(response)
            # Код возвращает переведенный текст
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка при переводе текста', exc_info=ex)
            return ''  # TODO: подумать над возвратом

def main():
    """
    Пример использования класса `HeliconeAI`.
    """
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print(f'Generated Poem:\\n {poem}')

    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print(f'Sentiment Analysis:\\n {sentiment}')

    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print(f'Summary:\\n {summary}')

    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print(f'Translation:\\n {translation}')

if __name__ == '__main__':
    main()
```