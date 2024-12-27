# Анализ кода модуля src.ai.anthropic

**Качество кода**

-   Соответствие требованиям по оформлению кода: 5/10
    -   Плюсы:
        -   Документ содержит подробное описание модуля, его функций и примеров использования.
        -   Присутствует информация об установке и лицензии.
    -   Минусы:
        -   Документ написан на Markdown, а не на reStructuredText (RST), как требуется в инструкции.
        -   Отсутствуют импорты, которые необходимы для работы модуля (хотя это и README, но по логике должны быть примеры кода)
        -   Формат документации не соответствует RST стандартам (отсутствуют роли, директивы и пр.)

**Рекомендации по улучшению**

1.  **Переписать документацию в RST:** Необходимо переписать весь текст в формате reStructuredText, включая заголовки, списки, блоки кода и таблицы.
2.  **Добавить примеры RST:** Включить примеры использования ролей, директив и других элементов RST.
3.  **Улучшить docstring:** Добавить docstring к функциям с описанием параметров и возвращаемых значений в формате RST.
4.  **Добавить описание модуля:** Включить в начало файла описание модуля в формате RST.
5.  **Привести в соответствие:**  Импортировать `logger` из `src.logger.logger`, перенести примеры кода в отдельный файл с расширением `.py`.
6.  **Создать отдельный файл с примерами:**  Создать файл `example.py` и перенести туда все примеры кода.

**Оптимизированный код**

```rst
.. module:: src.ai.anthropic
   :synopsis: Модуль для взаимодействия с Claude API от Anthropic.

=========================================================================================

Этот модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic.
Включает основные функции для генерации текста, анализа тональности и перевода текста.

.. note::
    Этот модуль требует установки библиотеки ``anthropic``.
    Для работы с модулем требуется API ключ от Anthropic.

.. contents:: Содержание
    :depth: 2

Установка
--------

Для использования этого модуля необходимо установить библиотеку ``anthropic``:

.. code-block:: bash

   pip install anthropic

Использование
------------

Инициализация
^^^^^^^^^^^^^

Сначала инициализируйте ``ClaudeClient`` с вашим API ключом Anthropic:

.. code-block:: python

   from src.ai.anthropic.claude_client import ClaudeClient

   api_key = "your-api-key"
   claude_client = ClaudeClient(api_key)

Генерация текста
^^^^^^^^^^^^^^^^

Сгенерируйте текст на основе заданного запроса:

.. code-block:: python

   prompt = "Напиши короткий рассказ о роботе, который учится любить."
   generated_text = claude_client.generate_text(prompt)
   print("Сгенерированный текст:", generated_text)

Анализ тональности
^^^^^^^^^^^^^^^^^^^

Проанализируйте тональность заданного текста:

.. code-block:: python

   text_to_analyze = "Я очень счастлив сегодня!"
   sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
   print("Анализ тональности:", sentiment_analysis)

Перевод текста
^^^^^^^^^^^^^^

Переведите текст с одного языка на другой:

.. code-block:: python

   text_to_translate = "Привет, как дела?"
   source_language = "ru"
   target_language = "en"
   translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
   print("Переведенный текст:", translated_text)


Примеры
-------
Полный пример использования ``ClaudeClient`` можно посмотреть в файле :file:`example.py`.

Методы
------

.. autoclass:: src.ai.anthropic.claude_client.ClaudeClient
   :members: generate_text
   :members: analyze_sentiment
   :members: translate_text

   .. automethod:: generate_text
   .. automethod:: analyze_sentiment
   .. automethod:: translate_text


Вклад
------

Приветствуются вклады! Не стесняйтесь отправлять запросы на извлечение или открывать вопрос, если у вас возникнут какие-либо проблемы или предложения по улучшению.

Лицензия
--------

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле `LICENSE`.

.. note::
   Замените ``"your-api-key"`` на свой фактический API ключ Anthropic.
```
```python
# example.py
"""
Примеры использования ClaudeClient.
=========================================================================================

Этот файл содержит примеры использования класса ClaudeClient.

Пример использования
--------------------

Пример использования класса `ClaudeClient`:

.. code-block:: python

    from src.ai.anthropic.claude_client import ClaudeClient

    api_key = "your-api-key"
    claude_client = ClaudeClient(api_key)

    # Generate text
    prompt = "Write a short story about a robot learning to love."
    generated_text = claude_client.generate_text(prompt)
    print("Generated Text:", generated_text)

    # Analyze sentiment
    text_to_analyze = "I am very happy today!"
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print("Sentiment Analysis:", sentiment_analysis)

    # Translate text
    text_to_translate = "Hello, how are you?"
    source_language = "en"
    target_language = "es"
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print("Translated Text:", translated_text)
"""
from src.ai.anthropic.claude_client import ClaudeClient
from src.logger.logger import logger # импортируем logger

def main():
    """
    Основная функция для демонстрации работы с ClaudeClient.
    """
    try:
        api_key = "your-api-key" # TODO: Заменить на фактический API ключ
        claude_client = ClaudeClient(api_key)

        # Generate text
        prompt = "Write a short story about a robot learning to love."
        generated_text = claude_client.generate_text(prompt)
        print("Generated Text:", generated_text)

        # Analyze sentiment
        text_to_analyze = "I am very happy today!"
        sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
        print("Sentiment Analysis:", sentiment_analysis)

        # Translate text
        text_to_translate = "Hello, how are you?"
        source_language = "en"
        target_language = "es"
        translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
        print("Translated Text:", translated_text)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
```python
"""
Модуль для взаимодействия с Claude API от Anthropic.
=========================================================================================

Этот модуль предоставляет простой интерфейс для взаимодействия с языковой моделью Claude от Anthropic.
Включает основные функции для генерации текста, анализа тональности и перевода текста.
"""
from anthropic import Anthropic # импортируем библиотеку anthropic
from src.logger.logger import logger # импортируем logger

class ClaudeClient:
    """
    Клиент для взаимодействия с API Claude от Anthropic.

    :param api_key: API ключ для доступа к Anthropic API.
    :type api_key: str
    """
    def __init__(self, api_key: str):
        """
        Инициализирует клиента Claude с предоставленным API ключом.

        :param api_key: API ключ для доступа к Anthropic API.
        :type api_key: str
        """
        self.client = Anthropic(api_key=api_key)
    def generate_text(self, prompt: str, max_tokens_to_sample: int = 100) -> str:
        """
        Генерирует текст на основе заданного запроса.

        :param prompt: Запрос для генерации текста.
        :type prompt: str
        :param max_tokens_to_sample: Максимальное количество токенов для генерации.
        :type max_tokens_to_sample: int
        :return: Сгенерированный текст.
        :rtype: str
        """
        try:
            # код исполняет вызов API Claude для генерации текста
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=max_tokens_to_sample,
                messages=[{"role": "user", "content": prompt}]
            )
            # Код возвращает сгенерированный текст
            return response.content[0].text
        except Exception as ex:
            logger.error(f"Error generating text: {ex}") # Логируем ошибку
            return ""
    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа.
        :type text: str
        :return: Результат анализа тональности.
        :rtype: str
        """
        try:
            # код исполняет вызов API Claude для анализа тональности
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=100,
                messages=[{"role": "user", "content": f"Analyze the sentiment of the following text: {text}"}]
            )
            # Код возвращает результат анализа тональности
            return response.content[0].text
        except Exception as ex:
            logger.error(f"Error analyzing sentiment: {ex}") # Логируем ошибку
            return ""
    def translate_text(self, text: str, source_language: str, target_language: str) -> str:
        """
        Переводит текст с одного языка на другой.

        :param text: Текст для перевода.
        :type text: str
        :param source_language: Код исходного языка.
        :type source_language: str
        :param target_language: Код целевого языка.
        :type target_language: str
        :return: Переведенный текст.
        :rtype: str
        """
        try:
            # код исполняет вызов API Claude для перевода текста
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=100,
                messages=[{"role": "user", "content": f"Translate the following text from {source_language} to {target_language}: {text}"}]
            )
            # Код возвращает переведенный текст
            return response.content[0].text
        except Exception as ex:
            logger.error(f"Error translating text: {ex}") # Логируем ошибку
            return ""
```