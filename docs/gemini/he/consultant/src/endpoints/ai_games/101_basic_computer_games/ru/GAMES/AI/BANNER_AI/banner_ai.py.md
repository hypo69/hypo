# Анализ кода модуля `banner_ai.py`

**Качество кода**
*   **Соблюдение требований к формату кода (1-10):** 7/10
    *   **Преимущества:**
        *   Используется `Pathlib` для работы с путями.
        *   Применяется `dotenv` для управления переменными окружения.
        *   Код разбит на классы и функции.
        *   Используются аннотации типов.
        *   Обработка ошибок в `ask`.
    *   **Недостатки:**
        *   Используется стандартный `json.load` (вместо `j_loads` из `src.utils.jjson`). # TODO заменить на j_loads
        *   Отсутствует логгирование ошибок. # TODO добавить логгер
        *   Не используется `j_loads` или `j_loads_ns` для чтения данных из json.
        *   Не все переменные и функции имеют docstring в формате RST. # TODO добавить docstring в формате RST
        *   Используются стандартные `try-except`, лучше использовать `logger.error`. # TODO заменить на logger.error
        *   Не все импорты отформатированы согласно стандартам PEP8 #TODO отформатировать импорты
        *   Недостаточно комментариев в коде #TODO добавить комментарии
        *   Нарушен стиль форматирования #TODO отформатировать код

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения данных.
2.  Добавить логирование ошибок с помощью `from src.logger.logger import logger`.
3.  Добавить docstring в формате RST ко всем функциям, методам и классам.
4.  Заменить стандартные блоки `try-except` на `logger.error` для обработки ошибок.
5.  Отформатировать импорты согласно PEP8.
6.  Добавить комментарии для пояснения логики кода.
7.  Использовать форматирование кода согласно PEP8.
8.  Использовать `j_loads` для чтения файла инструкций.
9.  Переписать комментарии в стиле reStructuredText.
10. Убрать использование f-string в logger.error

**Улучшенный код**
```python
"""
Модуль для создания текстовых баннеров с использованием моделей Google Generative AI.
=================================================================================

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Gemini
и создает текстовые баннеры на основе пользовательского ввода.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from pathlib import Path
    from dotenv import load_dotenv
    import os

    # Загрузка переменных окружения
    load_dotenv()

    # Получение API ключа из переменной окружения
    api_key = os.getenv('API_KEY')

    if not api_key:
        print("API ключ не найден")
        exit()

    # Определение пути к файлу с инструкциями
    base_path = Path(__file__).parent
    instruction_path = base_path / 'instructions' / 'system_instruction_asterisk.md'
    system_instruction = instruction_path.read_text(encoding='UTF-8')

    # Создание экземпляра класса
    model = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

    # Запрос текста и получение баннера
    user_text = "Hello, world!"
    banner = model.ask(user_text)
    print(banner)

"""
import os
import re  # Импорт библиотеки для работы с регулярными выражениями
from pathlib import Path
from typing import Any

from dotenv import load_dotenv, set_key  # Импорт функции для сохранения переменной в .env
import google.generativeai as genai  # Импорт библиотеки для работы с Gemini

from src.logger.logger import logger  # Импорт логгера для записи ошибок
from src.utils.jjson import j_loads  # Импорт функции для загрузки JSON
from header import __root__  # Импорт объекта __root__, содержащего абсолютный путь к корню проекта


# Загрузка переменных окружения из файла .env
load_dotenv()


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :ivar MODELS: Список доступных моделей Gemini.
    :vartype MODELS: list[str]
    :ivar api_key: API ключ для доступа к Gemini.
    :vartype api_key: str
    :ivar model_name: Название используемой модели Gemini.
    :vartype model_name: str
    :ivar model: Экземпляр модели Gemini.
    :vartype model: google.generativeai.GenerativeModel
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b'
    ]

    def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
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
        genai.configure(api_key=self.api_key)  # Конфигурация библиотеки с API ключом
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Инициализация модели с инструкцией

    def ask(self, q: str) -> str:
        """
        Отправка запроса модели и получение ответа.

        :param q: Текст запроса.
        :type q: str
        :return: Ответ модели или сообщение об ошибке.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # Отправка запроса модели
            return response.text  # Получение текстового ответа
        except Exception as ex:
            logger.error('Произошла ошибка при отправке запроса в модель', exc_info=ex) # Логирование ошибки
            return f'Error: {str(ex)}'  # Обработка и получение ошибки


# Основная часть программы
if __name__ == '__main__':
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Относительный путь к директории
    base_path: Path = __root__ / relative_path  # Абсолютный путь к директории с использованием __root__

    # Чтение API ключа из переменных окружения или запрос у пользователя
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
        # Сохранение введенного ключа в файл .env
        set_key('.env', 'API_KEY', API_KEY)

    instructions: dict = {  # Словарь с инструкциями
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }

    # Приветствие пользователя
    print('Добро пожаловать в игру Banner!')
    print('Введите текст, и я создам для вас текстовый баннер.')

    while True:
        # Выбор стиля оформления баннера
        print('Выберите стиль оформления баннера:')
        print('1. Символ \'*\'')
        print('2. Символ \'~\'')
        print('3. Символ \'#\'')
        choice = input('Введите номер стиля (1, 2 или 3): ')

        if choice in ('1', '2', '3'):
            instruction_file = Path(base_path, 'instructions', f'{instructions[choice]}.md') # Формирование пути к файлу инструкции
            try:
                system_instruction: str = instruction_file.read_text(encoding='UTF-8')  # Чтение инструкции из файла
            except Exception as ex:
                logger.error(f'Ошибка при чтении файла инструкции {instruction_file}', exc_info=ex) # Логирование ошибки
                system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8') # Чтение инструкции по умолчанию
        else:
            print('Неверный выбор. Используется стиль по умолчанию \'*\'')
            system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Чтение инструкции по умолчанию

        # Создание экземпляра класса с выбранной инструкцией
        model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)

        # Запрос текста у пользователя
        user_text: str = input('Введите текст для баннера: ')

        # Проверка, что текст не пустой
        if user_text.strip() == '':
            print('Вы не ввели текст. Попробуйте снова.')
        else:
            # Отправка текста модели и получение оформленного баннера
            response = model.ask(user_text)
            print('\nВаш баннер готов:')
            print(response)
```