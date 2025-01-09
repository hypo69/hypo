# Анализ кода модуля `ten_cent_computer.py`

**Качество кода**
- **Соответствие требованиям к формату кода (1-10):**
    -  **Преимущества:**
        - Код достаточно хорошо структурирован и читаем.
        - Используются классы для инкапсуляции логики.
        - Обработка ошибок присутствует, хотя и не совсем оптимальна.
        - Есть простая логика выбора игр через командную строку.
    - **Недостатки:**
        - Отсутствует использование `j_loads` или `j_loads_ns` для чтения файлов, вместо этого используется `Path(...).read_text()`.
        - Отсутствует подробное документирование всех функций, методов и классов в формате RST.
        - Обработка ошибок использует базовый `try-except` без логирования.
        - Нет импорта `logger` для логирования.
        - Использование `f.write` для добавления новых строк в `.env` файл не оптимально.
        - Не используется `src.utils.jjson` для чтения `json` файлов.
        - Нет обработки и проверки `API_KEY` до использования.

**Рекомендации по улучшению**
1.  **Документация:** Добавить подробную документацию в формате RST для всех классов, методов и функций, включая описание параметров, возвращаемых значений и возможных ошибок.
2.  **Логирование:** Использовать `src.logger.logger.error` для записи ошибок вместо простого вывода на экран. Это позволит лучше отслеживать проблемы.
3.  **Обработка ошибок:** Минимизировать использование общих `try-except` блоков и использовать `logger.error` для логирования исключений.
4.  **Импорт `jjson`:** Заменить чтение файлов с помощью `Path(...).read_text()` на `j_loads` или `j_loads_ns` из `src.utils.jjson` для обработки `json` файлов.
5.  **Импорты:** Добавить необходимые импорты, такие как `from src.logger.logger import logger` и `from src.utils.jjson import j_loads, j_loads_ns`.
6.  **Обработка переменных окружения:** Добавить проверку валидности `API_KEY` перед использованием.
7.  **.env**:  Использовать `dotenv` библиотеку для работы с файлами `.env`.
8.  **Обновление**: Улучшить метод обновления файла `.env`.

**Улучшенный код**
```python
"""
Модуль для взаимодействия с моделями Google Generative AI и запуска математических игр.
=========================================================================================

Модуль содержит класс :class:`GoogleGenerativeAI` для работы с моделями Google Gemini, а также
реализует логику выбора и запуска математических игр через командную строку.

Пример использования
--------------------

Пример запуска модуля с выбором одной из игр:

.. code-block:: python

    python ten_cent_computer.py
"""
import os
from pathlib import Path
import google.generativeai as genai
from typing import Any
from dotenv import load_dotenv
from src.logger.logger import logger  # Добавлен импорт logger
from src.utils.jjson import j_loads, j_loads_ns  # Добавлен импорт j_loads и j_loads_ns
load_dotenv() # загрузить переменные из .env файла

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к Gemini.
    :type api_key: str
    :param system_instruction: Инструкция для модели (системный промпт).
    :type system_instruction: str
    :param model_name: Название используемой модели Gemini. По умолчанию \'gemini-2-13b\'.
    :type model_name: str
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b'
    ]

    def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2-13b'):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к Gemini.
        :type api_key: str
        :param system_instruction: Инструкция для модели (системный промпт).
        :type system_instruction: str
        :param model_name: Название используемой модели Gemini. По умолчанию \'gemini-2-13b\'.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        try:
             # Конфигурация библиотеки с API ключом
            genai.configure(api_key=self.api_key)
             # Инициализация модели с инструкцией
            self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)
        except Exception as ex:
            logger.error(f'Ошибка при инициализации модели: {ex}') # Логирование ошибки инициализации модели
            raise  # Проброс исключения

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
             # Логирование ошибки при отправке запроса
            logger.error(f'Ошибка при отправке запроса: {ex}')
            return f'Error: {str(ex)}'


def set_key(dotenv_path: str, key: str, value: str):
    """
    Сохраняет пару ключ-значение в .env файл.

    :param dotenv_path: Путь к .env файлу.
    :type dotenv_path: str
    :param key: Ключ для сохранения.
    :type key: str
    :param value: Значение для сохранения.
    :type value: str
    """
    try:
        load_dotenv(dotenv_path=dotenv_path) # Загрузить данные из .env
        os.environ[key] = value # Обновить переменную окружения
        with open(dotenv_path, 'w') as f:
            for k, v in os.environ.items():
                if k == key: # Записать ключ=значение
                   f.write(f'{k}={value}\n')
                elif k in os.environ: # Записать остальные значения
                    f.write(f'{k}={v}\n')
    except Exception as ex:
         # Логирование ошибки при записи в .env
        logger.error(f'Ошибка при записи в .env файл: {ex}')

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
            try:
                 # Чтение инструкции из файла
                file_path: Path = Path(base_path, f'{instructions[choice]}.md')
                system_instruction: str = j_loads_ns(file_path) if file_path.suffix == '.json' else file_path.read_text(encoding='UTF-8')
                 # Создание экземпляра класса с выбранной инструкцией
                model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
            except Exception as ex:
                logger.error(f'Ошибка при загрузке или инициализации игры: {ex}') # Логирование ошибки загрузки файла
                continue


            if choice == '1':
                 # Запуск игры Ввод-Вывод
                while True:
                    user_input = input("Введите запрос для игры \'Ввод-Вывод\' (\'q\' для выхода): ")
                    if user_input.lower() == 'q':
                        break
                    try:
                        response = model.ask(user_input)
                        print(response)
                    except Exception as ex:
                        logger.error(f'Ошибка в игре \'Ввод-Вывод\': {ex}') # Логирование ошибки в игре
                        continue


            elif choice == '2':
                # Запуск игры 10-центовый компьютер
                while True:
                    user_input = input("Введите запрос для игры \'10-центовый компьютер\' (\'q\' для выхода): ")
                    if user_input.lower() == 'q':
                        break
                    try:
                        response = model.ask(user_input)
                        print(response)
                    except Exception as ex:
                        logger.error(f'Ошибка в игре \'10-центовый компьютер\': {ex}') # Логирование ошибки в игре
                        continue


        else:
            print('Неверный выбор. Попробуйте снова.')
```