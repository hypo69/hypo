# Анализ кода модуля `anagram.py`

**Качество кода**
*   **Соответствие требованиям к формату кода (1-10):**
    *   **Преимущества:**
        *   Код структурирован и использует классы для организации функциональности.
        *   Используются комментарии для пояснения основных блоков кода.
        *   Включены примеры использования.
    *   **Недостатки:**
        *   Отсутствует docstring для модуля.
        *   Используется `json.load` вместо `j_loads` или `j_loads_ns`.
        *   Не все функции имеют docstring.
        *   Используется `try-except` без логирования ошибок.
        *   Нет явных импортов для используемых модулей, таких как `src.utils.jjson`.
        *   В комментариях не используется reStructuredText (RST).
        *   Используются русские комментарии и docstring.

**Рекомендации по улучшению**

1.  **Документирование:** Добавить docstring для модуля, класса и методов, используя reStructuredText (RST).
2.  **Обработка данных:** Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок, и избегать `try-except` без логирования.
4.  **Импорты:** Добавить необходимые импорты, например, `from src.utils.jjson import j_loads`.
5.  **Форматирование комментариев:** Все комментарии должны быть переписаны в формате RST.
6.  **Переименования:** Переименовать переменные и функции в соответствии с общими правилами (если требуется).
7.  **Язык:** Перевести комментарии и docstring на русский.

**Улучшенный код**

```python
"""
Модуль для работы с Google Generative AI для создания анаграмм.
====================================================================

Модуль предоставляет класс :class:`GoogleGenerativeAI` для взаимодействия с моделями Google Gemini
с целью генерации анаграмм на основе заданного набора букв.

Пример использования
--------------------

Пример создания экземпляра класса `GoogleGenerativeAI` и использования метода `ask`:

.. code-block:: python

    api_key = input("API ключ от `gemini`: ")
    model = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)
    user_input = input("Введите буквы: ")
    response = model.ask(user_input)
    print(response)
"""
import google.generativeai as genai # Импортируем библиотеку для работы с Gemini
import re # Импортируем библиотеку для работы с регулярными выражениями
from src.logger.logger import logger # Импортируем logger для логирования ошибок
# from src.utils.jjson import j_loads  # TODO: Import j_loads if needed

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к Gemini.
    :type api_key: str
    :param system_instruction: Инструкция для модели (системный промпт).
    :type system_instruction: str
    :param model_name: Название используемой модели Gemini.
    :type model_name: str
    """
    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, system_instruction: str = "", model_name: str = "gemini-2.0-flash-exp"):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к Gemini.
        :type api_key: str
        :param system_instruction: Инструкция для модели (системный промпт).
        :type system_instruction: str
        :param model_name: Название используемой модели Gemini.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # Конфигурируем библиотеку с API ключом
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction) # Инициализируем модель с инструкцией

    def ask(self, q: str) -> str:
        """
        Отправляет запрос модели и возвращает ответ.

        :param q: Текст запроса.
        :type q: str
        :return: Ответ модели или сообщение об ошибке.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # Отправляем запрос модели
            return response.text  # Возвращаем текстовый ответ
        except Exception as ex:
            logger.error(f'Ошибка при запросе к модели: {ex}')  # Логируем ошибку
            return f"Error: {str(ex)}"  # Обрабатываем и возвращаем ошибку

# Инструкция для Gemini (системный промпт)
system_instruction = """
Ты — генератор анаграмм. Твоя задача — по заданному набору букв найти существующее слово русского языка, составленное из этих букв (используя все или часть из них).

Правила:

1. Игнорируй любые символы, кроме русских букв. Цифры и другие символы не учитываются.
2. Если из заданных букв можно составить несколько слов, верни одно из них.
3. Если из заданных букв невозможно составить ни одного слова русского языка, верни ответ "Нет анаграмм".
4. Не генерируй неологизмы или выдуманные слова. Используй только существующие слова русского языка.
5. Не объясняй процесс, просто возвращай слово или "Нет анаграмм".
"""

API_KEY: str = input("API ключ от `gemini`: ")  # Запрашиваем API ключ у пользователя
model = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction) # Создаем экземпляр класса, передавая API ключ и инструкцию

if __name__ == "__main__":
    while True:  # Бесконечный цикл для ввода запросов
        q = input("Введите буквы, по которым Gemini подберет анаграмму (для выхода нажмите Ctrl+C): ")
        # Очистка ввода от не кириллических символов
        q = re.sub(r"[^а-яА-ЯёЁ]", "", q) # Удаляем все символы, кроме русских букв
        if not q: # Проверяем, осталась ли строка пустой после очистки
            print("Введены некорректные символы. Введите русские буквы.")
            continue # Переходим к следующей итерации цикла
        response = model.ask(q) # Отправляем запрос модели
        print(response) # Выводим ответ модели
```