# Анализ кода модуля `claude.py`

**Качество кода**
8
- Плюсы
    - Код соответствует основным требованиям к структуре и функциональности, предоставляет базовый интерфейс для взаимодействия с Claude API.
    - Присутствует документация для методов.
- Минусы
    - Не хватает обработки ошибок и логирования.
    - Отсутствует документация модуля в формате RST.
    - Используются двойные кавычки в коде, где должны быть одинарные.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - API key передаётся в коде напрямую.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST.
2.  Использовать одинарные кавычки в коде, где это необходимо.
3.  Импортировать `logger` из `src.logger.logger`.
4.  Добавить обработку ошибок с использованием `logger.error` вместо стандартных `try-except` блоков.
5.  Удалить прямое использование API key.
6.  Добавить docstring для класса.
7.  Добавить пример использования класса в формате RST.
8.  Переименовать переменные с использованием snake_case.
9.  Добавить проверку на наличие токенов в ответе.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для взаимодействия с Anthropic Claude API.
==================================================

Этот модуль содержит класс :class:`ClaudeClient`, который обеспечивает
интерфейс для работы с Claude API, включая генерацию текста, анализ тональности
и перевод текста.

Пример использования
--------------------

.. code-block:: python

    from src.ai.anthropic.claude import ClaudeClient

    api_key = 'your-api-key'
    claude_client = ClaudeClient(api_key)

    prompt = 'Write a short story about a robot learning to love.'
    generated_text = claude_client.generate_text(prompt)
    print("Generated Text:", generated_text)
"""
from src.logger.logger import logger # Импорт logger из src.logger.logger
import anthropic

class ClaudeClient:
    """
    Клиент для взаимодействия с Anthropic Claude API.

    Предоставляет методы для генерации текста, анализа тональности
    и перевода текста.
    """
    def __init__(self, api_key: str):
        """
        Инициализирует клиент Claude с заданным API-ключом.

        Args:
            api_key (str): API-ключ для доступа к Claude API.
        """
        # Создание клиента anthropic
        self.client = anthropic.Client(api_key)

    def generate_text(self, prompt: str, max_tokens_to_sample: int = 100) -> str:
        """
        Генерирует текст на основе заданного запроса.

        Args:
            prompt (str): Запрос для генерации текста.
            max_tokens_to_sample (int, optional): Максимальное количество токенов для генерации.
                                                  Defaults to 100.

        Returns:
            str: Сгенерированный текст.
        """
        try:
            #  Отправка запроса в Claude API для генерации текста
            response = self.client.completion(
                prompt=prompt,
                model='claude-v1',
                max_tokens_to_sample=max_tokens_to_sample,
                stop_sequences=['\n\nHuman:']
            )
            # Проверка на наличие ключа 'completion' в ответе
            if 'completion' not in response:
                logger.error(f'Отсутствует ключ `completion` в ответе API: {response=}')
                return ''
            return response['completion']
        except Exception as e:
            # Логирование ошибки при генерации текста
            logger.error('Ошибка при генерации текста:', exc_info=e)
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
            #  Отправка запроса в Claude API для анализа тональности
            response = self.client.completion(
                prompt=f'Analyze the sentiment of the following text: {text}',
                model='claude-v1',
                max_tokens_to_sample=50,
                stop_sequences=['\n\nHuman:']
            )
            # Проверка на наличие ключа 'completion' в ответе
            if 'completion' not in response:
                logger.error(f'Отсутствует ключ `completion` в ответе API: {response=}')
                return ''
            return response['completion']
        except Exception as e:
            # Логирование ошибки при анализе тональности
            logger.error('Ошибка при анализе тональности:', exc_info=e)
            return ''

    def translate_text(self, text: str, source_language: str, target_language: str) -> str:
        """
        Переводит заданный текст с исходного языка на целевой.

        Args:
            text (str): Текст для перевода.
            source_language (str): Код исходного языка.
            target_language (str): Код целевого языка.

        Returns:
            str: Переведенный текст.
        """
        try:
            #  Отправка запроса в Claude API для перевода текста
            response = self.client.completion(
                prompt=f'Translate the following text from {source_language} to {target_language}: {text}',
                model='claude-v1',
                max_tokens_to_sample=100,
                stop_sequences=['\n\nHuman:']
            )
            # Проверка на наличие ключа 'completion' в ответе
            if 'completion' not in response:
                logger.error(f'Отсутствует ключ `completion` в ответе API: {response=}')
                return ''
            return response['completion']
        except Exception as e:
            # Логирование ошибки при переводе текста
            logger.error('Ошибка при переводе текста:', exc_info=e)
            return ''


# Пример использования класса
if __name__ == '__main__':
    # TODO: api_key вынести в настройки
    api_key = 'your-api-key'
    claude_client = ClaudeClient(api_key)

    # Пример генерации текста
    prompt = 'Write a short story about a robot learning to love.'
    generated_text = claude_client.generate_text(prompt)
    print('Generated Text:', generated_text)

    # Пример анализа тональности
    text_to_analyze = 'I am very happy today!'
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print('Sentiment Analysis:', sentiment_analysis)

    # Пример перевода текста
    text_to_translate = 'Hello, how are you?'
    source_language = 'en'
    target_language = 'es'
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print('Translated Text:', translated_text)
```