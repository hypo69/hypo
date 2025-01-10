# Анализ кода модуля `claude.py`

**Качество кода**
    6
 -  Плюсы
        - Код функционален и выполняет поставленные задачи.
        - Используется класс для организации работы с API Anthropic Claude.
        - Есть пример использования класса.
 -  Минусы
    -  Не хватает документации в формате RST.
    -  Используется print для вывода, что не подходит для продакшн кода.
    -  Нет обработки ошибок, в том числе для API ключа.
    -  Отсутствует логирование.
    -  Используются двойные кавычки вместо одинарных в некоторых местах.
    -  Не используется `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**
1.  Добавить документацию в формате RST для модуля и каждого метода.
2.  Заменить использование `print` на `logger.info` для вывода информации и `logger.error` для ошибок.
3.  Реализовать обработку исключений для API запросов и других потенциальных ошибок.
4.  Использовать одинарные кавычки для строк в коде, кроме операций вывода.
5.  Добавить импорт `logger` из `src.logger`.
6.  Добавить обработку ошибок при инициализации клиента.
7.  Реализовать возможность задания модели через параметр.
8.  Добавить docstring с примерами использования для всех методов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для взаимодействия с API Anthropic Claude.
=========================================================================================

Этот модуль содержит класс :class:`ClaudeClient`, который используется для взаимодействия с API Anthropic Claude для генерации текста,
анализа тональности и перевода текста.

Пример использования
--------------------

Пример использования класса `ClaudeClient`:

.. code-block:: python

    from src.ai.anthropic.claude import ClaudeClient
    from src.logger import logger

    api_key = 'your-api-key'
    claude_client = ClaudeClient(api_key)

    prompt = 'Write a short story about a robot learning to love.'
    generated_text = claude_client.generate_text(prompt)
    logger.info(f'Generated Text: {generated_text}')

    text_to_analyze = 'I am very happy today!'
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    logger.info(f'Sentiment Analysis: {sentiment_analysis}')

    text_to_translate = 'Hello, how are you?'
    source_language = 'en'
    target_language = 'es'
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    logger.info(f'Translated Text: {translated_text}')
"""
import anthropic
from src.logger import logger  # Импорт логгера

class ClaudeClient:
    """
    Клиент для взаимодействия с API Anthropic Claude.

    :param api_key: Ключ API для доступа к сервису Anthropic Claude.
    :type api_key: str
    """
    def __init__(self, api_key, model='claude-v1'): #добавлена возможность выбора модели
        """
        Инициализирует клиент Claude с заданным API ключом.

        :param api_key: Ключ API для доступа к сервису Anthropic Claude.
        :type api_key: str
        :raises ValueError: Если api_key не предоставлен.
        """
        if not api_key:
            logger.error('API key is required')
            raise ValueError('API key is required') # обработка отсутствия api_key
        try:
           # Код инициализирует клиента anthropic
            self.client = anthropic.Client(api_key)
            self.model = model
        except Exception as e:
            logger.error(f'Ошибка инициализации клиента Anthropic: {e}')
            raise  # Пробрасываем исключение дальше для обработки на верхнем уровне

    def generate_text(self, prompt, max_tokens_to_sample=100):
        """
        Генерирует текст на основе заданного запроса.

        :param prompt: Запрос для генерации текста.
        :type prompt: str
        :param max_tokens_to_sample: Максимальное количество токенов для генерации.
        :type max_tokens_to_sample: int
        :return: Сгенерированный текст.
        :rtype: str
        :raises Exception: При возникновении ошибки в процессе запроса к API.

        Example:
            >>> from src.ai.anthropic.claude import ClaudeClient
            >>> api_key = 'your-api-key'
            >>> claude_client = ClaudeClient(api_key)
            >>> prompt = 'Write a short story about a robot learning to love.'
            >>> generated_text = claude_client.generate_text(prompt)
            >>> print(generated_text)

        """
        try:
             # Код отправляет запрос в API для генерации текста
            response = self.client.completion(
                prompt=prompt,
                model=self.model,
                max_tokens_to_sample=max_tokens_to_sample,
                stop_sequences=['\\n\\nHuman:']
            )
            return response['completion']
        except Exception as e:
            logger.error(f'Ошибка при генерации текста: {e}')
            raise  # Пробрасываем исключение дальше для обработки на верхнем уровне

    def analyze_sentiment(self, text):
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа.
        :type text: str
        :return: Результат анализа тональности.
        :rtype: str
        :raises Exception: При возникновении ошибки в процессе запроса к API.

        Example:
            >>> from src.ai.anthropic.claude import ClaudeClient
            >>> api_key = 'your-api-key'
            >>> claude_client = ClaudeClient(api_key)
            >>> text_to_analyze = 'I am very happy today!'
            >>> sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
            >>> print(sentiment_analysis)
        """
        try:
             # Код отправляет запрос в API для анализа тональности текста
            response = self.client.completion(
                prompt=f'Analyze the sentiment of the following text: {text}',
                model=self.model,
                max_tokens_to_sample=50,
                stop_sequences=['\\n\\nHuman:']
            )
            return response['completion']
        except Exception as e:
            logger.error(f'Ошибка при анализе тональности: {e}')
            raise  # Пробрасываем исключение дальше для обработки на верхнем уровне

    def translate_text(self, text, source_language, target_language):
        """
        Переводит заданный текст с исходного языка на целевой.

        :param text: Текст для перевода.
        :type text: str
        :param source_language: Код исходного языка.
        :type source_language: str
        :param target_language: Код целевого языка.
        :type target_language: str
        :return: Переведенный текст.
        :rtype: str
        :raises Exception: При возникновении ошибки в процессе запроса к API.

         Example:
            >>> from src.ai.anthropic.claude import ClaudeClient
            >>> api_key = 'your-api-key'
            >>> claude_client = ClaudeClient(api_key)
            >>> text_to_translate = 'Hello, how are you?'
            >>> source_language = 'en'
            >>> target_language = 'es'
            >>> translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
            >>> print(translated_text)
        """
        try:
             # Код отправляет запрос в API для перевода текста
            response = self.client.completion(
                prompt=f'Translate the following text from {source_language} to {target_language}: {text}',
                model=self.model,
                max_tokens_to_sample=100,
                stop_sequences=['\\n\\nHuman:']
            )
            return response['completion']
        except Exception as e:
             # Логирование ошибки, если запрос не удался
            logger.error(f'Ошибка при переводе текста: {e}')
            raise  # Пробрасываем исключение дальше для обработки на верхнем уровне

# Пример использования класса
if __name__ == '__main__':
    api_key = 'your-api-key'
    try:
       # Код инициализирует клиента Claude
        claude_client = ClaudeClient(api_key)

        # Пример генерации текста
        prompt = 'Write a short story about a robot learning to love.'
        generated_text = claude_client.generate_text(prompt)
        logger.info(f'Generated Text: {generated_text}')

        # Пример анализа тональности
        text_to_analyze = 'I am very happy today!'
        sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
        logger.info(f'Sentiment Analysis: {sentiment_analysis}')

        # Пример перевода текста
        text_to_translate = 'Hello, how are you?'
        source_language = 'en'
        target_language = 'es'
        translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
        logger.info(f'Translated Text: {translated_text}')
    except Exception as e:
         # Логирование ошибки, если что-то пошло не так на верхнем уровне
        logger.error(f'Ошибка в основном блоке: {e}')
```