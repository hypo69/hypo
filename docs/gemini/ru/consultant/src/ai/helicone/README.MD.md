# Анализ кода модуля src.ai.helicone

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и документирован в формате Markdown.
    - Присутствуют примеры использования и описание ключевых функций.
    - Логика работы с Helicone.ai и OpenAI достаточно проста и понятна.
- Минусы
    - Отсутствует документация в формате reStructuredText (RST) для docstring.
    - Не используется `src.logger.logger` для логирования ошибок.
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя в данном случае это и не требуется).
    - Нет обработки ошибок.
    - Не используются константы для моделей.

**Рекомендации по улучшению**

1.  **Переход на RST**: Переписать все комментарии и docstring в формате reStructuredText (RST), включая описание модуля, классов и методов.
2.  **Логирование ошибок**: Добавить логирование ошибок с использованием `from src.logger.logger import logger` и `logger.error` вместо стандартного `try-except` для отлова исключений.
3.  **Константы для моделей**: Определить константы для используемых моделей ('gpt-3.5-turbo', 'text-davinci-003').
4.  **Обработка ошибок**: Добавить обработку ошибок, возникающих при взаимодействии с OpenAI API.
5.  **Использовать j_loads**: Проверить есть ли необходимость использовать `j_loads` или `j_loads_ns`.
6. **Удалить Markdown**: Удалить описание в Markdown, оставив только RST.

**Оптимизированный код**

```python
"""
Модуль для интеграции с Helicone.ai и OpenAI
=========================================================================================

Этот модуль предоставляет класс :class:`HeliconeAI`, который обеспечивает взаимодействие
с моделями Helicone.ai и OpenAI для генерации стихов, анализа тональности,
суммирования и перевода текста.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from src.ai.helicone import HeliconeAI

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print(poem)
"""
from helicone import Helicone
from openai import OpenAI
from src.logger.logger import logger  #  Импортируем logger
# from src.utils.jjson import j_loads  #  Импорт j_loads если необходимо

class HeliconeAI:
    """
    Класс для взаимодействия с Helicone.ai и OpenAI.

    :ivar helicone: Экземпляр класса Helicone для логирования.
    :vartype helicone: Helicone
    :ivar client: Экземпляр класса OpenAI для работы с API.
    :vartype client: OpenAI
    """
    GPT_MODEL = "gpt-3.5-turbo"  # Константа для модели GPT
    DAVINCI_MODEL = "text-davinci-003"  # Константа для модели Davinci

    def __init__(self):
        """
        Инициализирует класс HeliconeAI.

        Создает экземпляры Helicone и OpenAI.
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
        """
        try:
            # Код отправляет запрос в OpenAI API для генерации стихотворения
            response = self.client.chat.completions.create(
                model=self.GPT_MODEL,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # Логирует завершение запроса с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает сгенерированный текст
            return response.choices[0].message.content
        except Exception as ex:  # Обработка исключений
            logger.error('Ошибка при генерации стихотворения', ex) #  Логируем ошибку
            return ""  #  Возвращает пустую строку в случае ошибки

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа тональности.
        :type text: str
        :return: Результат анализа тональности.
        :rtype: str
        """
        try:
            # Код отправляет запрос в OpenAI API для анализа тональности
            response = self.client.completions.create(
                model=self.DAVINCI_MODEL,
                prompt=f"Analyze the sentiment of the following text: {text}",
                max_tokens=50
            )
             # Логирует завершение запроса с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает результат анализа тональности
            return response.choices[0].text.strip()
        except Exception as ex:  # Обработка исключений
            logger.error('Ошибка при анализе тональности', ex) #  Логируем ошибку
            return ""   # Возвращает пустую строку в случае ошибки

    def summarize_text(self, text: str) -> str:
        """
        Суммирует заданный текст.

        :param text: Текст для суммирования.
        :type text: str
        :return: Суммированный текст.
        :rtype: str
        """
        try:
            # Код отправляет запрос в OpenAI API для суммирования текста
            response = self.client.completions.create(
                model=self.DAVINCI_MODEL,
                prompt=f"Summarize the following text: {text}",
                max_tokens=100
            )
            # Логирует завершение запроса с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает суммированный текст
            return response.choices[0].text.strip()
        except Exception as ex:  # Обработка исключений
            logger.error('Ошибка при суммировании текста', ex) #  Логируем ошибку
            return ""  #  Возвращает пустую строку в случае ошибки

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный язык.

        :param text: Текст для перевода.
        :type text: str
        :param target_language: Целевой язык для перевода.
        :type target_language: str
        :return: Переведенный текст.
        :rtype: str
        """
        try:
            # Код отправляет запрос в OpenAI API для перевода текста
            response = self.client.completions.create(
                model=self.DAVINCI_MODEL,
                prompt=f"Translate the following text to {target_language}: {text}",
                max_tokens=200
            )
            # Логирует завершение запроса с помощью Helicone
            self.helicone.log_completion(response)
            # Возвращает переведенный текст
            return response.choices[0].text.strip()
        except Exception as ex:  # Обработка исключений
            logger.error('Ошибка при переводе текста', ex) #  Логируем ошибку
            return ""  #  Возвращает пустую строку в случае ошибки


def main():
    """
    Пример использования класса HeliconeAI.

    Создает экземпляр класса HeliconeAI, генерирует стихотворение,
    анализирует тональность, суммирует и переводит текст, а затем выводит результаты.
    """
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\\n", translation)

if __name__ == "__main__":
    main()
```