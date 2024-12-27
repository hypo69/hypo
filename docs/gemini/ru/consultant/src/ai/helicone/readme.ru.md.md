# Анализ кода модуля `helicone`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и понятен, с четкими разделительными заголовками и примерами использования.
    - Имеется описание функционала каждого метода.
    - Код предоставляет базовую интеграцию с `Helicone.ai` и `OpenAI`.
    - Есть пример использования в `main()`.
-  Минусы
    - Отсутствует обработка ошибок и логирование, кроме логирования через `helicone.log_completion`, что не дает понимания что происходит в случае сбоя.
    - Отсутствует описание модуля в начале файла в формате `reStructuredText`.
    - Нет docstring в формате reStructuredText.
    - Нет импортов из `src.logger.logger`, а также  `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используются одинарные кавычки в Python коде.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате reStructuredText.
2.  Добавить docstring для каждого метода в формате reStructuredText.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок и общей информации.
4.  Изменить  `json.load`  на  `j_loads` или `j_loads_ns` из `src.utils.jjson`.
5.  Использовать одинарные кавычки в Python коде.
6.  Добавить обработку ошибок с использованием `logger.error`.
7.  Использовать `f-string`  там где это уместно.

**Оптимизированный код**

```python
"""
Модуль для интеграции с Helicone.ai и OpenAI
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который обеспечивает взаимодействие с Helicone.ai и моделями OpenAI
для выполнения различных задач, таких как генерация стихов, анализ тональности, создание кратких изложений и перевод текста.
Также включает логирование завершений с использованием Helicone.ai.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from helicone import Helicone
    from openai import OpenAI
    from src.logger.logger import logger


    class HeliconeAI:
        def __init__(self):
            self.helicone = Helicone()
            self.client = OpenAI()

        def generate_poem(self, prompt: str) -> str:
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            self.helicone.log_completion(response)
            return response.choices[0].message.content

        def analyze_sentiment(self, text: str) -> str:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            self.helicone.log_completion(response)
            return response.choices[0].text.strip()

        def summarize_text(self, text: str) -> str:
             response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
             self.helicone.log_completion(response)
             return response.choices[0].text.strip()

        def translate_text(self, text: str, target_language: str) -> str:
             response = self.client.completions.create(
                 model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
             self.helicone.log_completion(response)
             return response.choices[0].text.strip()


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
"""
from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger # импорт модуля логирования

class HeliconeAI:
    """
    Класс для интеграции с Helicone.ai и OpenAI.

    Предоставляет методы для генерации стихов, анализа тональности,
    создания кратких изложений и перевода текста.
    Также включает логирование завершений с использованием Helicone.ai.
    """
    def __init__(self):
        """
        Инициализирует класс HeliconeAI, создавая экземпляры Helicone и OpenAI.
        """
        self.helicone = Helicone()
        self.client = OpenAI()

    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.

        :param prompt: Промпт для генерации стихотворения.
        :return: Сгенерированное стихотворение.
        """
        try: # Обработка ошибок
            # Выполняет запрос к OpenAI для генерации стиха
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            # Логирует завершение с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает сгенерированный текст
            return response.choices[0].message.content
        except Exception as e: # логирование ошибки
            logger.error(f'Ошибка при генерации стихотворения: {e}')
            return ''


    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа тональности.
        :return: Результат анализа тональности.
        """
        try: # Обработка ошибок
             # Выполняет запрос к OpenAI для анализа тональности
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
             # Логирует завершение с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает результат анализа
            return response.choices[0].text.strip()
        except Exception as e: # логирование ошибки
            logger.error(f'Ошибка при анализе тональности: {e}')
            return ''

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение заданного текста.

        :param text: Текст для изложения.
        :return: Краткое изложение текста.
        """
        try: # Обработка ошибок
            # Выполняет запрос к OpenAI для создания краткого изложения
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            # Логирует завершение с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает краткое изложение
            return response.choices[0].text.strip()
        except Exception as e: # логирование ошибки
            logger.error(f'Ошибка при создании краткого изложения: {e}')
            return ''

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный целевой язык.

        :param text: Текст для перевода.
        :param target_language: Целевой язык для перевода.
        :return: Переведенный текст.
        """
        try: # Обработка ошибок
            # Выполняет запрос к OpenAI для перевода текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            # Логирует завершение с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает переведенный текст
            return response.choices[0].text.strip()
        except Exception as e: # логирование ошибки
             logger.error(f'Ошибка при переводе текста: {e}')
             return ''


def main():
    """
    Пример использования класса HeliconeAI.
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