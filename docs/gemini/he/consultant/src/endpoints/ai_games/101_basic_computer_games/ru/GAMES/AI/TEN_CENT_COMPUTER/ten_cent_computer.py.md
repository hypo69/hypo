# Анализ кода модуля `ten_cent_computer.py`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
  -   **Преимущества:**
        -   Код структурирован и относительно легко читаем.
        -   Используется класс `GoogleGenerativeAI` для работы с моделями Gemini, что способствует модульности.
        -   Есть базовая обработка ошибок при работе с моделью.
        -   Используется `.env` файл для хранения API-ключа.
  -   **Недостатки:**
        -   Отсутствует использование `j_loads` или `j_loads_ns` для чтения файлов.
        -   Нет подробных docstring'ов в формате reStructuredText (RST).
        -   Используется `Exception` в `try-except` блоке, что не рекомендуется.
        -   Отсутствует логирование ошибок.
        -   Не хватает аннотации типов.
        -   Не все имена переменных и функций соответствуют предыдущим файлам.
        -   Отсутствуют комментарии, описывающие логику работы кода в блоке `if __name__ == '__main__'`

**Рекомендации по улучшению**

1.  **Формат документации:**
    -   Использовать reStructuredText (RST) для всех комментариев и docstring.
2.  **Обработка данных:**
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов, если они появятся в дальнейшем.
3.  **Импорты:**
    -   Добавить импорты, если они будут нужны.
4.  **Структура кода:**
    -   Добавить аннотации типов.
    -   Переименовать переменные и функции для соответствия предыдущим файлам, если требуется.
5.  **Улучшения:**
    -   Добавить docstring'и в формате RST для всех функций, методов и классов.
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
    -   Избегать использования общих `try-except` блоков, использовать `logger.error` для обработки исключений.
6.  **Комментарии:**
    -   Добавить подробные комментарии, поясняющие логику работы кода.

**Улучшенный код**

```python
"""
Модуль для взаимодействия с моделями Google Generative AI и запуска математических игр.
=========================================================================================

Модуль содержит класс :class:`GoogleGenerativeAI` для взаимодействия с моделями Google Gemini,
а также логику для запуска игр "Ввод-Вывод" и "10-центовый компьютер".

Пример использования
--------------------

.. code-block:: python

    # Пример использования:
    # 1. Настройте API_KEY в файле .env или через переменную окружения.
    # 2. Запустите скрипт.
    # 3. Выберите игру, следуя инструкциям в консоли.
    # 4. Вводите запросы для выбранной игры.
"""
import os
from pathlib import Path
from typing import Any

import google.generativeai as genai

from src.logger.logger import logger # Импорт logger
# from src.utils.jjson import j_loads, j_loads_ns #TODO: Временно закомментирован, пока не используется


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b'
    ]

    def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2-13b') -> None:
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к Gemini.
        :type api_key: str
        :param system_instruction: Инструкция для модели (системный промпт).
        :type system_instruction: str
        :param model_name: Название используемой модели Gemini. По умолчанию 'gemini-2-13b'.
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
            logger.error(f'Ошибка при отправке запроса: {ex}') # Логирование ошибки
            return f'Error: {str(ex)}'  # Обработка и получение ошибки


def set_key(dotenv_path: str, key: str, value: str) -> None:
    """
    Сохраняет пару ключ-значение в .env файл.

    :param dotenv_path: Путь к файлу .env.
    :type dotenv_path: str
    :param key: Ключ для сохранения.
    :type key: str
    :param value: Значение для сохранения.
    :type value: str
    """
    if os.path.exists(dotenv_path):
        with open(dotenv_path, 'r') as f:
            lines = f.readlines()
        with open(dotenv_path, 'w') as f:
            updated = False
            for line in lines:
                if line.strip().startswith(f'{key}='):
                    f.write(f'{key}={value}\n')
                    updated = True
                else:
                    f.write(line)
            if not updated:
                f.write(f'{key}={value}\n')
    else:
        with open(dotenv_path, 'w') as f:
            f.write(f'{key}={value}\n')


if __name__ == '__main__':

    __root__ = Path(__file__).resolve().parent
    relative_path: Path = Path('games', 'ai')  # Относительный путь к директории с играми
    base_path: Path = __root__ / relative_path  # Абсолютный путь к директории

    # Чтение API ключа из переменных окружения или запрос у пользователя
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
        # Сохранение введенного ключа в файл .env
        set_key('.env', 'API_KEY', API_KEY)

    instructions: dict = {
        '1': 'input_output',
        '2': 'ten_cent_computer',
    }

    # Приветствие пользователя
    print('Добро пожаловать в мир математических игр!')
    print('Выберите, в какую игру вы хотите поиграть:')

    while True:
        # Выбор игры
        print('1. Игра "Ввод-Вывод"')
        print('2. Игра "10-центовый компьютер"')
        choice = input('Введите номер игры (1 или 2, или "q" для выхода): ')

        if choice == 'q':
            print('До свидания!')
            break

        if choice in ('1', '2'):
            system_instruction: str = Path(base_path, f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Чтение инструкции из файла
            # Создание экземпляра класса с выбранной инструкцией
            model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
            if choice == '1':
                # Запуск игры Ввод-Вывод
                while True:
                    user_input = input("Введите запрос для игры 'Ввод-Вывод' ('q' для выхода): ")
                    if user_input.lower() == 'q':
                        break
                    response = model.ask(user_input)
                    print(response)

            elif choice == '2':
                # Запуск игры 10-центовый компьютер
                while True:
                    user_input = input("Введите запрос для игры '10-центовый компьютер' ('q' для выхода): ")
                    if user_input.lower() == 'q':
                        break
                    response = model.ask(user_input)
                    print(response)

        else:
            print('Неверный выбор. Попробуйте снова.')
```