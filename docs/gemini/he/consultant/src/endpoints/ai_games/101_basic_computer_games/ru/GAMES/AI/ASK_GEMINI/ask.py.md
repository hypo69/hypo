# Анализ кода модуля `ask.py`

**Качество кода**

*   **Соответствие требованиям к формату кода (1-10):** 7/10

    *   **Преимущества:**
        *   Код структурирован в классы и функции, что способствует его читаемости и организации.
        *   Используется docstring для документирования класса и методов.
        *   Инициализация модели происходит через конструктор класса.
    *   **Недостатки:**
        *   Отсутствует импорт необходимых модулей.
        *   Не используется `j_loads` или `j_loads_ns` для чтения файлов.
        *   Обработка ошибок не логируется с помощью `logger.error`.
        *   Не все комментарии написаны в reStructuredText (RST).
        *   Отсутствуют docstring для переменных `MODELS` и `API_KEY`.

**Рекомендации по улучшению**

1.  **Импорт модулей:** Добавить импорт модуля `src.utils.jjson` для использования `j_loads` или `j_loads_ns`.
2.  **Использование `j_loads` или `j_loads_ns`:** Заменить чтение из файлов с помощью `json.load` на `j_loads`.
3.  **Логирование ошибок:** Заменить стандартный `print` для ошибок на использование `logger.error`.
4.  **Форматирование комментариев:** Привести все комментарии и docstring к формату reStructuredText (RST).
5.  **Документирование переменных:** Добавить docstring для переменных `MODELS` и `API_KEY`.
6.  **Улучшенная обработка ошибок:** Обработать ошибки с помощью `logger.error` и возвращать более информативные сообщения.
7.  **Переименование переменных**: Заменить имя `q` на более информативное `user_query`.

**Улучшенный код**

```python
"""
Модуль для взаимодействия с моделями Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия с различными моделями
Google Gemini для выполнения текстовых задач.

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    api_key = 'YOUR_API_KEY'  # Замените на ваш ключ API
    model = GoogleGenerativeAI(api_key=api_key, system_instruction='You are helpful assistant')
    response = model.ask('What is the capital of France?')
    print(response)

"""
import google.generativeai as genai
from src.logger.logger import logger  # Импорт логгера для обработки ошибок
# from src.utils.jjson import j_loads  # TODO: добавить импорт если понадобится читать json

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к Gemini.
    :type api_key: str
    :param system_instruction: Инструкция для модели (системный промпт).
    :type system_instruction: str
    :param model_name: Название используемой модели Gemini. По умолчанию 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]
    """Список доступных моделей Gemini."""


    def __init__(self, api_key: str, system_instruction: str = '', model_name: str = 'gemini-2.0-flash-exp'):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к Gemini.
        :type api_key: str
        :param system_instruction: Инструкция для модели (системный промпт).
        :type system_instruction: str
        :param model_name: Название используемой модели Gemini. По умолчанию 'gemini-2.0-flash-exp'.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key) # Конфигурация библиотеки с API ключом
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction) # Инициализация модели с инструкцией


    def ask(self, user_query: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param user_query: Вопрос, который будет отправлен модели.
        :type user_query: str
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            response = self.model.generate_content(user_query) #  Отправляет запрос в модель
            return response.text # Возвращает текстовый ответ модели
        except Exception as ex:
            logger.error(f'Ошибка при запросе к Gemini API: {ex}') # Логирование ошибки
            return f"Error: {str(ex)}" # Возвращает сообщение об ошибке

################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY:str = input("API ключ от `gemini`")
"""API ключ от `gemini`."""
model = GoogleGenerativeAI(api_key = API_KEY)

user_query = input("Вопрос: ")
response = model.ask(user_query)
print(response)
```