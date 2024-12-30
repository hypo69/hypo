# Анализ кода модуля `banner_ai.py`

**Качество кода**
- Соответствие требованиям к формату кода (1-10): 8
    - Преимущества:
        - Используются аннотации типов.
        - Код относительно чистый и читаемый.
        - Разбиение на функции и классы, что улучшает структуру.
    - Недостатки:
        - Не используется `j_loads` или `j_loads_ns`.
        - Отсутствует  `logger` для логирования ошибок.
        - Отсутствуют docstring у функций и класса.
        - Не используются `reStructuredText (RST)` для комментирования.
        - Некоторые переменные и функции не соответствуют соглашениям.

**Рекомендации по улучшению**

1. **Использование `j_loads`:**  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2. **Добавление логирования:** Использовать `logger` для записи ошибок вместо `print` и `Exception`.
3. **Документирование:** Добавить docstrings в формате RST ко всем классам, функциям и методам.
4. **Форматирование кода:**  Привести код в соответствие со стандартами PEP 8 и сделать его более читаемым.
5. **Обработка ошибок:** Улучшить обработку ошибок, избегая чрезмерного использования блоков `try-except`.
6. **Удаление лишнего импорта**: Удалить неиспользуемый импорт `re`.
7. **Улучшение сообщений об ошибках:** Сообщения об ошибках сделать более информативными, включая детали.
8. **Переменные и функции:** Переименовать переменные и функции по принципу snake_case.

**Улучшенный код**

```python
"""
Модуль для создания текстовых баннеров с использованием моделей Google Generative AI.
=========================================================================================

Модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с API Gemini и
создания баннеров на основе текстовых запросов пользователя.
Модуль позволяет выбирать стиль оформления баннера, используя символы `*`, `~` или `#`.

Пример использования
--------------------

Пример использования модуля `banner_ai`:

.. code-block:: python

    from pathlib import Path

    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')
    base_path: Path = __root__ / relative_path

    # Получение API ключа
    api_key: str = os.getenv('API_KEY')
    if not api_key:
        api_key = input('API ключ не найден. Введите API ключ от `gemini`: ')
        set_key('.env', 'API_KEY', api_key)

    # Выбор инструкции
    instructions: dict = {
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }
    choice = '1'  # Выбор стиля по умолчанию

    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')

    # Создание модели и отправка запроса
    model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)
    user_text: str = 'Пример текста для баннера'
    response: str = model.ask(user_text)

    print(f'Ваш баннер готов:\n{response}')
"""
import os
from pathlib import Path
from dotenv import load_dotenv, set_key
import google.generativeai as genai
from src.utils.jjson import j_loads #  Импорт j_loads из src.utils.jjson
from src.logger.logger import logger #  Импорт logger из src.logger.logger
from header import __root__


load_dotenv()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к Gemini.
    :type api_key: str
    :param system_instruction: Инструкция для модели (системный промпт).
    :type system_instruction: str
    :param model_name: Название используемой модели Gemini. По умолчанию `gemini-2.0-flash-exp`.
    :type model_name: str
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
        :param model_name: Название используемой модели Gemini. По умолчанию `gemini-2.0-flash-exp`.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key) #  Конфигурирование библиотеки с API ключом
        try:
            self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Инициализация модели с инструкцией
        except Exception as ex:
             logger.error(f'Ошибка при инициализации модели {self.model_name}: {ex}') #  Логирование ошибки при инициализации модели
             self.model = None

    def ask(self, q: str) -> str:
        """
        Отправка запроса модели и получение ответа.

        :param q: Текст запроса.
        :type q: str
        :return: Ответ модели или сообщение об ошибке.
        :rtype: str
        """
        if not self.model:
            logger.error('Модель не инициализирована')  # Логирование ошибки, если модель не инициализирована
            return 'Ошибка: Модель не инициализирована'
        try:
            response = self.model.generate_content(q) # Отправка запроса модели
            return response.text  # Получение текстового ответа
        except Exception as ex:
             logger.error(f'Ошибка при отправке запроса модели: {ex}') # Логирование ошибки при отправке запроса модели
             return f'Ошибка: {str(ex)}'


if __name__ == '__main__':
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI') # Относительный путь к директории
    base_path: Path = __root__ / relative_path # Абсолютный путь к директории с использованием __root__

    # Чтение API ключа из переменных окружения или запрос у пользователя
    api_key: str = os.getenv('API_KEY')
    if not api_key:
        api_key = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
        set_key('.env', 'API_KEY', api_key) # Сохранение введенного ключа в файл .env

    instructions: dict = {
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }

    print('Добро пожаловать в игру Banner!') # Приветствие пользователя
    print('Введите текст, и я создам для вас текстовый баннер.')

    while True:
        print('Выберите стиль оформления баннера:') # Выбор стиля оформления баннера
        print('1. Символ `*`')
        print('2. Символ `~`')
        print('3. Символ `#`')
        choice = input('Введите номер стиля (1, 2 или 3): ')

        if choice in ('1', '2', '3'):
             # Чтение инструкции из файла
            instruction_path: Path = Path(base_path, 'instructions', f'{instructions[choice]}.md')
            try:
                 system_instruction: str = instruction_path.read_text(encoding='UTF-8')
            except FileNotFoundError:
                 logger.error(f'Файл инструкции не найден: {instruction_path}') # Логирование ошибки, если файл инструкции не найден
                 system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8') # Чтение инструкции по умолчанию
            except Exception as ex:
                 logger.error(f'Ошибка при чтении файла инструкции: {instruction_path}, {ex}') # Логирование ошибки при чтении файла
                 system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8') # Чтение инструкции по умолчанию
        else:
            print('Неверный выбор. Используется стиль по умолчанию `*`')  # Сообщение об ошибке выбора стиля
            system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8') # Чтение инструкции по умолчанию
        try:
            # Создание экземпляра класса с выбранной инструкцией
            model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)
        except Exception as ex:
            logger.error(f'Ошибка при создании модели: {ex}') #  Логирование ошибки при создании модели
            continue


        user_text: str = input('Введите текст для баннера: ') # Запрос текста у пользователя

        if not user_text.strip():
            print('Вы не ввели текст. Попробуйте снова.') # Сообщение об ошибке, если текст пустой
            continue

        response: str = model.ask(user_text) # Отправка текста модели и получение оформленного баннера
        print('\nВаш баннер готов:')
        print(response)