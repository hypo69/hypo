# Анализ кода модуля ask.py

**Качество кода**
-  **Соответствие требованиям к формату кода (1-10):** 8/10
    -  **Преимущества:**
        - Код структурирован и легко читаем.
        - Используется класс для инкапсуляции логики работы с Google Gemini.
        - Есть базовая обработка ошибок.
        - Присутствуют docstrings, описывающие назначение класса и методов.
    -  **Недостатки:**
        - Не используется `j_loads` или `j_loads_ns`.
        - Отсутствует импорт логгера.
        - Docstrings не соответствуют стандарту reStructuredText (RST).
        - Не все части кода прокомментированы.
        - Присутствуют лишние комментарии (например, `# INSERT YOUR GEMINI API KEY`).
        - Переменная `API_KEY` должна быть константой и быть вынесена в `.env` файл, но это не входит в задачу, поэтому я это игнорирую.
        - Не используются константы для модели.

**Рекомендации по улучшению**
1. **Форматирование документации:**
   - Переписать docstrings в формате RST.
   - Добавить описания типов параметров и возвращаемых значений в docstrings.

2. **Обработка данных:**
   - Не используется `j_loads` или `j_loads_ns`, но это не требуется в данном коде.

3. **Логирование:**
   - Добавить импорт и использование логгера для записи ошибок.
   - Заменить общую обработку ошибок на запись в лог.

4. **Структура кода:**
    - Добавить константы для используемых моделей.

5. **Комментарии:**
    - Уточнить комментарии, добавить пояснения к каждому шагу кода.

**Улучшенный код**
```python
"""
Модуль для взаимодействия с моделями Google Generative AI.
=========================================================================================

Модуль содержит класс :class:`GoogleGenerativeAI`, который позволяет взаимодействовать с моделями
Google Gemini для обработки текстовых запросов.

Пример использования
--------------------

Пример создания экземпляра класса `GoogleGenerativeAI` и отправки запроса:

.. code-block:: python

    api_key = "YOUR_API_KEY"
    model = GoogleGenerativeAI(api_key=api_key)
    response = model.ask("Какой сегодня день?")
    print(response)
"""
import google.generativeai as genai  # Импорт библиотеки google.generativeai
from src.logger.logger import logger # Импорт логгера

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к Gemini.
    :type api_key: str
    :param system_instruction: Инструкция для модели (системный промпт), по умолчанию пустая строка.
    :type system_instruction: str, optional
    :param model_name: Название используемой модели Gemini, по умолчанию 'gemini-2.0-flash-exp'.
    :type model_name: str, optional
    """

    MODELS = [ # Список доступных моделей
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]
    DEFAULT_MODEL = "gemini-2.0-flash-exp" # Модель по умолчанию

    def __init__(self, api_key: str, system_instruction: str = '', model_name: str = DEFAULT_MODEL):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к Gemini.
        :type api_key: str
        :param system_instruction: Инструкция для модели (системный промпт).
        :type system_instruction: str
        :param model_name: Название используемой модели Gemini. По умолчанию 'gemini-2.0-flash-exp'.
        :type model_name: str
        """
        self.api_key = api_key # Сохраняем ключ API
        self.model_name = model_name # Сохраняем имя модели
        try:
           genai.configure(api_key=self.api_key)  # Конфигурация библиотеки с API ключом
           self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Инициализация модели с инструкцией
        except Exception as ex: # Обработка ошибок при инициализации
            logger.error('Ошибка при инициализации модели Google Gemini', exc_info=True) # Логгируем ошибку
            raise # Перевыбрасываем исключение для информирования вызывающего кода

    def ask(self, q: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q) # Отправляем запрос
            return response.text # Возвращаем текст ответа
        except Exception as ex:
            logger.error(f'Ошибка при запросе к модели: {str(ex)}', exc_info=True) # Логгируем ошибку
            return f"Error: {str(ex)}" # Возвращаем сообщение об ошибке

################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################
# TODO: Move API_KEY to .env
API_KEY: str = input("API ключ от `gemini`")  # Запрос API ключа у пользователя
model = GoogleGenerativeAI(api_key = API_KEY) # Создание экземпляра класса с API ключом

q = input("Вопрос: ") # Запрос вопроса у пользователя
response = model.ask(q) # Получение ответа от модели
print(response) # Вывод ответа
```