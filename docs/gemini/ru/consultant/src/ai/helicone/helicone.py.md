# Анализ кода модуля `helicone.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, функции имеют понятные имена и назначения.
    - Присутствует базовая документация в виде docstring для каждой функции.
    - Используются асинхронные вызовы для взаимодействия с API.

- Минусы
    - Отсутствует обработка ошибок при вызовах API, что может привести к проблемам в работе программы.
    - Отсутствует явное указание типа возвращаемых данных в docstring.
    - Используется устаревший способ импорта `header`.
    - Отсутствует логгирование, что затрудняет отладку и мониторинг.
    - Нет обработки случаев, когда `response.choices` может быть пустым или отсутствовать.
    - Docstring не соответствует формату RST

**Рекомендации по улучшению**

1.  **Импорты**: Замените импорт `header` на что-то более конкретное или удалите его, если он не нужен.
2.  **Обработка ошибок**: Добавьте обработку ошибок при вызовах API, используя `try-except` блоки и логирование ошибок через `src.logger.logger`.
3.  **Документация**: Приведите docstring к формату RST, включая описания параметров и возвращаемых значений с указанием типов.
4.  **Логирование**: Добавьте логирование для отслеживания запросов и ответов API, а также для записи ошибок.
5.  **Улучшение обработки ответов**: Проверьте наличие `response.choices` и `response.choices[0].message.content` или `response.choices[0].text` перед их использованием.
6.  **Унификация методов**: Замените вызовы `client.completions.create` на более абстрактные методы, которые используют `chat.completions` в качестве основы, чтобы иметь возможность применять разные модели.
7.  **Удаление неиспользуемых переменных**: Удалите `MODE` если он не используется.

**Оптимизированный код**

```python
"""
Модуль для интеграции с Helicone и OpenAI API
=========================================================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для взаимодействия с Helicone и OpenAI API
для выполнения различных задач обработки текста, таких как генерация текста, анализ тональности,
суммирование и перевод.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

# https://docs.helicone.ai/guides/overview
# TODO: replace with concrete import or remove
# import header

from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger
from helicone import Helicone
from openai import OpenAI
from typing import Any, Dict


class HeliconeAI:
    """
    Класс для взаимодействия с Helicone и OpenAI API.
    """
    def __init__(self) -> None:
        """
        Инициализирует Helicone и OpenAI клиентов.
        """
        self.helicone = Helicone()
        self.client = OpenAI()

    def _create_chat_completion(self, model: str, messages: list, **kwargs: Any) -> Any:
        """
        Вспомогательный метод для создания запроса к OpenAI Chat Completion API.

        :param model: Имя модели для использования.
        :param messages: Список сообщений для запроса.
        :param kwargs: Дополнительные аргументы для API.
        :return: Ответ от OpenAI API.
        """
        try:
            # Код отправляет запрос к OpenAI Chat Completion API
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            self.helicone.log_completion(response)
            return response
        except Exception as ex:
            # Код логирует ошибку в случае неудачи запроса к API
            logger.error(f'Ошибка при запросе к OpenAI API: {ex}')
            return None

    def _create_completion(self, model: str, prompt: str, **kwargs: Any) -> Any:
        """
         Вспомогательный метод для создания запроса к OpenAI Completion API.

        :param model: Имя модели для использования.
        :param prompt: Текст запроса.
        :param kwargs: Дополнительные аргументы для API.
        :return: Ответ от OpenAI API.
        """
        try:
            # Код отправляет запрос к OpenAI Completion API
            response = self.client.completions.create(
                model=model,
                prompt=prompt,
                **kwargs
            )
            self.helicone.log_completion(response)
            return response
        except Exception as ex:
            # Код логирует ошибку в случае неудачи запроса к API
            logger.error(f'Ошибка при запросе к OpenAI API: {ex}')
            return None
    
    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.

        :param prompt: Промпт для генерации стихотворения.
        :type prompt: str
        :return: Сгенерированное стихотворение.
        :rtype: str
        """
        response = self._create_chat_completion(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        if response and response.choices:
            # Код возвращает сгенерированный текст стихотворения
            return response.choices[0].message.content
        # Код возвращает пустую строку в случае ошибки
        return ''

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность текста.

        :param text: Текст для анализа.
        :type text: str
        :return: Результат анализа тональности.
        :rtype: str
        """
        response = self._create_completion(
            model='text-davinci-003',
            prompt=f'Analyze the sentiment of the following text: {text}',
            max_tokens=50
        )
        if response and response.choices:
            # Код возвращает результат анализа тональности
            return response.choices[0].text.strip()
        # Код возвращает пустую строку в случае ошибки
        return ''

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение текста.

        :param text: Текст для изложения.
        :type text: str
        :return: Краткое изложение текста.
        :rtype: str
        """
        response = self._create_completion(
            model='text-davinci-003',
            prompt=f'Summarize the following text: {text}',
            max_tokens=100
        )
        if response and response.choices:
             # Код возвращает краткое изложение текста
            return response.choices[0].text.strip()
        # Код возвращает пустую строку в случае ошибки
        return ''

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит текст на указанный язык.

        :param text: Текст для перевода.
        :type text: str
        :param target_language: Целевой язык перевода.
        :type target_language: str
        :return: Переведенный текст.
        :rtype: str
        """
        response = self._create_completion(
            model='text-davinci-003',
            prompt=f'Translate the following text to {target_language}: {text}',
            max_tokens=200
        )
        if response and response.choices:
             # Код возвращает переведенный текст
            return response.choices[0].text.strip()
         # Код возвращает пустую строку в случае ошибки
        return ''

def main() -> None:
    """
    Основная функция для демонстрации работы HeliconeAI.
    """
    helicone_ai = HeliconeAI()
    # Код генерирует стихотворение
    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print('Generated Poem:\\n', poem)
    # Код анализирует тональность текста
    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print('Sentiment Analysis:\\n', sentiment)
    # Код создает краткое изложение текста
    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print('Summary:\\n', summary)
    # Код переводит текст
    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print('Translation:\\n', translation)


if __name__ == '__main__':
    main()
```