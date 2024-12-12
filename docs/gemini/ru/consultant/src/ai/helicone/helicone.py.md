# Анализ кода модуля `helicone`

**Качество кода**
9
-   Плюсы
    - Код достаточно хорошо структурирован и разделен на логические блоки.
    - Присутствует документация в виде docstring для функций и методов.
    - Код следует базовым принципам Python.
    - Используется класс для инкапсуляции функциональности.
-   Минусы
    - Отсутствует модуль `header`.
    - Нет обработки ошибок при вызовах API OpenAI, что может привести к проблемам в продакшене.
    - Не используется `src.logger.logger` для логирования.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Комментарии не соответствуют формату RST.

**Рекомендации по улучшению**

1.  **Импорты:** Добавьте `from src.logger.logger import logger` для логирования ошибок и `from src.utils.jjson import j_loads, j_loads_ns` для обработки JSON. Удалите импорт `header`, так как он не используется и не существует.

2.  **Формат документации:** Перепишите все docstring в формате RST.

3.  **Логирование:** Используйте `logger.error` вместо стандартных блоков `try-except` для обработки ошибок при вызовах API OpenAI.

4.  **Обработка данных:** В данном файле не обрабатываются json файлы, но придерживаемся инструкции.

5.  **Комментарии**: Добавьте комментарии в формате RST к модулю, функциям, методам и переменным.

6.  **Удалить неиспользуемые переменные:** Удалить `MODE`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для интеграции с Helicone и OpenAI API.
=====================================================

Этот модуль содержит класс :class:`HeliconeAI`, который используется для
взаимодействия с API Helicone и OpenAI для выполнения задач,
таких как генерация текста, анализ тональности, суммирование и перевод.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)

"""

from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns # не используется, но на всякий случай оставим


class HeliconeAI:
    """
    Класс для взаимодействия с Helicone и OpenAI API.
    
    Предоставляет методы для генерации текста, анализа тональности,
    суммирования и перевода текста.
    """
    def __init__(self):
        """
        Инициализирует класс HeliconeAI.
        
        Создает экземпляры клиентов Helicone и OpenAI.
        """
        self.helicone = Helicone()
        # Код инициализирует клиент OpenAI
        self.client = OpenAI()

    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.
        
        :param prompt: Промпт для генерации стихотворения.
        :type prompt: str
        :return: Сгенерированное стихотворение.
        :rtype: str
        
        Пример использования::
        
            poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
        """
        try:
            # Код отправляет запрос в OpenAI API для генерации стихотворения
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            # Код логирует запрос в Helicone
            self.helicone.log_completion(response)
            # Код возвращает сгенерированный текст
            return response.choices[0].message.content
        except Exception as e:
            # Код логирует ошибку
            logger.error(f'Ошибка при генерации стихотворения: {e}')
            return ''
    

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность текста.
        
        :param text: Текст для анализа.
        :type text: str
        :return: Результат анализа тональности.
        :rtype: str
        
        Пример использования::
            
            sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
        """
        try:
            # Код отправляет запрос в OpenAI API для анализа тональности
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            # Код логирует запрос в Helicone
            self.helicone.log_completion(response)
            # Код возвращает результат анализа
            return response.choices[0].text.strip()
        except Exception as e:
            # Код логирует ошибку
            logger.error(f'Ошибка при анализе тональности: {e}')
            return ''

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение текста.
        
        :param text: Текст для изложения.
        :type text: str
        :return: Краткое изложение текста.
        :rtype: str
        
        Пример использования::
        
            summary = helicone_ai.summarize_text("Длинный текст для изложения...")
        """
        try:
            # Код отправляет запрос в OpenAI API для суммирования текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            # Код логирует запрос в Helicone
            self.helicone.log_completion(response)
            # Код возвращает краткое изложение
            return response.choices[0].text.strip()
        except Exception as e:
            # Код логирует ошибку
            logger.error(f'Ошибка при суммировании текста: {e}')
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
        
        Пример использования::
        
             translation = helicone_ai.translate_text("Hello, how are you?", "русский")
        """
        try:
            # Код отправляет запрос в OpenAI API для перевода текста
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            # Код логирует запрос в Helicone
            self.helicone.log_completion(response)
            # Код возвращает переведенный текст
            return response.choices[0].text.strip()
        except Exception as e:
            # Код логирует ошибку
            logger.error(f'Ошибка при переводе текста: {e}')
            return ''


def main():
    """
    Основная функция для демонстрации работы класса HeliconeAI.
    
    Создает экземпляр класса HeliconeAI и вызывает его методы
    для генерации текста, анализа тональности, суммирования и перевода.
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