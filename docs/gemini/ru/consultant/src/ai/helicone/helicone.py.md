# Анализ кода модуля `helicone.py`

**Качество кода**
8/10
-  Плюсы
    - Код хорошо структурирован и читаем.
    - Присутствует базовая документация в виде docstring для функций.
    - Используется класс для организации функциональности.
    - Код выполняет поставленные задачи, связанные с запросами к API OpenAI и логированием через Helicone.
-  Минусы
    - Отсутствует обработка ошибок.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствуют логирование ошибок через `logger.error`.
    - Не все комментарии переписаны в формате RST.
    - Импорт `header` не используется и, вероятно, является ошибкой.

**Рекомендации по улучшению**
1. **Импорт `header`**: Удалить неиспользуемый импорт `header`.
2. **Использование `j_loads` или `j_loads_ns`**: В данном коде нет необходимости в `j_loads` или `j_loads_ns`, так как не происходит чтение файлов.
3. **Логирование ошибок**: Добавить логирование ошибок с использованием `logger.error` для отслеживания проблем при взаимодействии с API OpenAI.
4. **Формат документации**: Привести все комментарии и docstring к формату reStructuredText (RST).
5. **Обработка исключений**: Добавить обработку исключений для запросов к API OpenAI.
6. **Удаление неиспользуемого MODE**: Удалить неиспользуемую константу MODE.
7. **Переменные окружения**: Рассмотреть возможность использования переменных окружения для хранения ключей API.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для взаимодействия с OpenAI API через Helicone.
=========================================================================================

Этот модуль предоставляет класс :class:`HeliconeAI` для генерации текста,
анализа тональности, суммирования и перевода текста с использованием моделей OpenAI.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print(poem)
"""

from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger # Импорт logger

class HeliconeAI:
    """
    Класс для взаимодействия с OpenAI API через Helicone.

    :ivar helicone: Экземпляр класса Helicone для логирования запросов.
    :vartype helicone: Helicone
    :ivar client: Экземпляр класса OpenAI для взаимодействия с API.
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
        Генерирует стихотворение на основе заданного промпта.

        :param prompt: Промпт для генерации стихотворения.
        :type prompt: str
        :raises Exception: Если при запросе к API OpenAI возникла ошибка.
        :return: Сгенерированное стихотворение.
        :rtype: str
        """
        try:
            #  Отправка запроса в OpenAI API для генерации стихотворения.
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            #  Логирование ответа с помощью Helicone.
            self.helicone.log_completion(response)
            # Возвращение сгенерированного стихотворения.
            return response.choices[0].message.content
        except Exception as e:
            #  Логирование ошибки при генерации стихотворения.
            logger.error('Ошибка при генерации стихотворения', exc_info=True)
            return ''


    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность текста.

        :param text: Текст для анализа.
        :type text: str
        :raises Exception: Если при запросе к API OpenAI возникла ошибка.
        :return: Результат анализа тональности.
        :rtype: str
        """
        try:
            #  Отправка запроса в OpenAI API для анализа тональности.
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            #  Логирование ответа с помощью Helicone.
            self.helicone.log_completion(response)
            # Возвращение результата анализа тональности.
            return response.choices[0].text.strip()
        except Exception as e:
            #  Логирование ошибки при анализе тональности.
            logger.error('Ошибка при анализе тональности', exc_info=True)
            return ''

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение текста.

        :param text: Текст для изложения.
        :type text: str
        :raises Exception: Если при запросе к API OpenAI возникла ошибка.
        :return: Краткое изложение текста.
        :rtype: str
        """
        try:
            #  Отправка запроса в OpenAI API для создания краткого изложения.
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            #  Логирование ответа с помощью Helicone.
            self.helicone.log_completion(response)
            # Возвращение краткого изложения текста.
            return response.choices[0].text.strip()
        except Exception as e:
            # Логирование ошибки при создании краткого изложения.
            logger.error('Ошибка при создании краткого изложения', exc_info=True)
            return ''


    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит текст на указанный язык.

        :param text: Текст для перевода.
        :type text: str
        :param target_language: Целевой язык перевода.
        :type target_language: str
        :raises Exception: Если при запросе к API OpenAI возникла ошибка.
        :return: Переведенный текст.
        :rtype: str
        """
        try:
            # Отправка запроса в OpenAI API для перевода текста.
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            #  Логирование ответа с помощью Helicone.
            self.helicone.log_completion(response)
            # Возвращение переведенного текста.
            return response.choices[0].text.strip()
        except Exception as e:
            #  Логирование ошибки при переводе текста.
             logger.error('Ошибка при переводе текста', exc_info=True)
             return ''

def main():
    """
    Основная функция для демонстрации работы класса HeliconeAI.
    """
    helicone_ai = HeliconeAI()
    #  Генерация стихотворения.
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\n", poem)
    #  Анализ тональности текста.
    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\n", sentiment)
    #  Создание краткого изложения текста.
    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\n", summary)
    #  Перевод текста на русский язык.
    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\n", translation)

if __name__ == "__main__":
    main()
```