# Анализ кода модуля `src.ai.helicone`

**Качество кода**:
   - **Соответствие стандартам**: 7
   - **Плюсы**:
     - Четкое описание функциональности класса `HeliconeAI`.
     - Примеры использования методов.
     - Инструкции по установке и использованию.
     - Логирование запросов в Helicone.ai.
   - **Минусы**:
     - Отсутствуют RST-комментарии для методов и классов.
     - Не используется `from src.logger import logger` для логирования.
     - Использование двойных кавычек для вывода и строк, которые должны быть в одинарных кавычках.
     - Нет обработки ошибок.

**Рекомендации по улучшению**:
   - Добавить RST-комментарии к классу `HeliconeAI` и всем его методам.
   - Использовать одинарные кавычки для строковых литералов в Python коде, кроме `print`, `input` и `logger`.
   - Добавить обработку ошибок и логирование с использованием `logger.error` при возникновении исключений.
   - Использовать `from src.logger import logger` для логирования.
   - Избегать избыточного использования `try-except` блоков, использовать более явную обработку ошибок через логирование.
   - Переписать примеры использования методов с корректными кавычками.
   - Добавить информацию о том, что для работы с кодом необходим `API-KEY` и как его установить.
   - Разместить `API-KEY` в файле `.env`.

**Оптимизированный код**:
```python
"""
Модуль для интеграции с Helicone.ai и OpenAI.
================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия с моделями Helicone.ai и OpenAI.
Он предоставляет методы для генерации стихов, анализа тональности, суммирования и перевода текста, а также логирования.

Пример использования
----------------------
.. code-block:: python

    from src.ai.helicone import HeliconeAI

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
from helicone import Helicone  #  Импорт Helicone
from openai import OpenAI # Импорт OpenAI
from src.logger import logger # Импорт logger


class HeliconeAI:
    """
    Класс для взаимодействия с Helicone.ai и OpenAI.

    :ivar helicone: Экземпляр класса Helicone.
    :vartype helicone: Helicone
    :ivar client: Экземпляр класса OpenAI.
    :vartype client: OpenAI
    """
    def __init__(self):
        """
        Инициализирует класс HeliconeAI, создавая экземпляры Helicone и OpenAI.
        """
        self.helicone = Helicone()
        self.client = OpenAI()

    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного запроса.

        :param prompt: Запрос для генерации стихотворения.
        :type prompt: str
        :return: Сгенерированное стихотворение.
        :rtype: str
        :raises Exception: В случае ошибки при генерации стихотворения.
        
        Пример:
            >>> helicone_ai = HeliconeAI()
            >>> poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
        """
        try:
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            self.helicone.log_completion(response) # Логирование ответа
            return response.choices[0].message.content
        except Exception as e:
           logger.error(f"Ошибка при генерации стихотворения: {e}") # Логирование ошибки
           return "" # Возврат пустой строки при ошибке

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа тональности.
        :type text: str
        :return: Результат анализа тональности.
        :rtype: str
        :raises Exception: В случае ошибки при анализе тональности.
        
        Пример:
            >>> helicone_ai = HeliconeAI()
            >>> sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            self.helicone.log_completion(response) # Логирование ответа
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Ошибка при анализе тональности: {e}") # Логирование ошибки
            return "" # Возврат пустой строки при ошибке

    def summarize_text(self, text: str) -> str:
        """
        Суммирует заданный текст.

        :param text: Текст для суммирования.
        :type text: str
        :return: Суммированный текст.
        :rtype: str
        :raises Exception: В случае ошибки при суммировании текста.
        
        Пример:
            >>> helicone_ai = HeliconeAI()
            >>> summary = helicone_ai.summarize_text('Длинный текст для изложения...')
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            self.helicone.log_completion(response) # Логирование ответа
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Ошибка при суммировании текста: {e}") # Логирование ошибки
            return ""  # Возврат пустой строки при ошибке

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный язык.

        :param text: Текст для перевода.
        :type text: str
        :param target_language: Язык, на который нужно перевести текст.
        :type target_language: str
        :return: Переведенный текст.
        :rtype: str
        :raises Exception: В случае ошибки при переводе текста.

        Пример:
           >>> helicone_ai = HeliconeAI()
           >>> translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
        """
        try:
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            self.helicone.log_completion(response) # Логирование ответа
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Ошибка при переводе текста: {e}") # Логирование ошибки
            return "" # Возврат пустой строки при ошибке


def main():
    """
    Пример использования класса HeliconeAI.
    """
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print('Generated Poem:\n', poem)

    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print('Sentiment Analysis:\n', sentiment)

    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print('Summary:\n', summary)

    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print('Translation:\n', translation)

if __name__ == '__main__':
    main()
```