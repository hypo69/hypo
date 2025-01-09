# Анализ кода модуля `BANNER_AI`

**Качество кода**
<br>
-  **Соответствие требованиям к формату кода (1-10):** 5/10
    -  **Преимущества:**
        -  Используется `Pathlib` для работы с путями, что обеспечивает кроссплатформенность.
        -  Применяется `dotenv` для управления переменными окружения, что улучшает безопасность и конфиденциальность.
        -  Код логически разбит на классы и функции, что облегчает чтение и поддержку.
    -  **Недостатки:**
        -  Отсутствуют docstring для функций, методов и классов, что снижает читаемость кода и затрудняет его понимание.
        -  Не используется логирование ошибок с помощью `logger.error`.
        -  Не используется `j_loads` или `j_loads_ns` для чтения файлов, что не соответствует требованиям.
        -  Некоторые комментарии дублируют код, вместо того чтобы пояснять логику.
        -  Используется жесткая привязка к путям в файловой системе, что затрудняет переносимость.
        -  Не все импортированные модули используются в коде.
        -  Обработка ошибок выполняется просто и не содержит дополнительных пояснений для пользователя.
        -  Код не содержит примеров использования и не описан в формате reStructuredText (RST).
        -  Переменные в `dict` заданы не в `snake_case`.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавьте docstring для всех классов, методов и функций, используя формат reStructuredText (RST).
    -   Добавьте описание модуля в начале файла в формате RST.
    -   Включите примеры использования для демонстрации возможностей.
2.  **Обработка ошибок**:
    -   Используйте `try-except` блоки для обработки исключений, возникших в коде.
    -   Используйте `logger.error` для логирования ошибок, чтобы можно было отслеживать и исправлять их.
3.  **Чтение файлов**:
    -   Используйте `j_loads` или `j_loads_ns` для загрузки JSON файлов, вместо стандартного `json.load`.
    -   Используйте `Path(...).read_text(encoding='UTF-8')` для чтения текстовых файлов.
4.  **Логирование**:
    -   Добавьте логирование критически важных этапов выполнения программы, таких как загрузка ключа API, чтение инструкций, создание объекта модели и отправка запроса.
5.  **Переменные**:
    -   Имена переменных в `dict` должны быть написаны в `snake_case`.
6.  **Структура кода**:
    -   Разбейте код на более мелкие функции или методы, чтобы улучшить читаемость и повторное использование.
7.  **Импорты**:
    -   Удалите неиспользуемые импорты.
8.  **Конфигурация**:
    -   Для улучшения переносимости, используйте относительные пути к файлам относительно корневой директории проекта.
9.  **Комментарии**:
    -   Сделайте комментарии более пояснительными и не дублируйте код.
10. **Формат**:
    -   Убедитесь, что весь код отформатирован в соответствии со стандартами PEP 8.
    -   Убедитесь, что весь docstring написан в формате RST.

**Улучшенный код**

```python
"""
Модуль для создания текстовых баннеров с использованием Google Generative AI.
=========================================================================================

Модуль :mod:`banner_ai` предоставляет функциональность для генерации текстовых баннеров
с использованием моделей Google Gemini.
Пользователь может выбрать стиль оформления баннера и отправить текст для обработки.

Примеры использования
--------------------

Пример использования модуля:

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.AI.BANNER_AI import banner_ai

    if __name__ == "__main__":
        banner_ai.main()
"""
import os
from pathlib import Path
from typing import Any

import google.generativeai as genai
from dotenv import load_dotenv, set_key

from src.logger.logger import logger
from src.utils.jjson import j_loads_ns  # Исправлено: импорт j_loads_ns
from header import __root__  # Исправлено: импорт __root__


load_dotenv()

#: Список доступных моделей Google Generative AI.
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b',
]


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделью Google Generative AI.

    :param api_key: Ключ API для доступа к Gemini.
    :type api_key: str
    :param system_instruction: Инструкция для модели (системный промпт).
    :type system_instruction: str
    :param model_name: Название используемой модели Gemini. По умолчанию 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
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
        try:
            genai.configure(api_key=self.api_key)  # Настройка библиотеки с API ключом
            self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Инициализация модели с инструкцией
            logger.debug(f'Модель {self.model_name} успешно инициализирована.') # Логирование успешной инициализации
        except Exception as ex:
            logger.error(f'Ошибка при инициализации модели: {ex}') # Логирование ошибок инициализации
            raise

    def ask(self, q: str) -> str:
        """
        Отправляет запрос модели и возвращает ответ.

        :param q: Текст запроса.
        :type q: str
        :return: Ответ модели или сообщение об ошибке.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # Отправка запроса модели
            logger.debug(f'Запрос к модели: {q}') # Логирование отправленного запроса
            return response.text  # Получение текстового ответа
        except Exception as ex:
            logger.error(f'Ошибка при запросе к модели: {ex}') # Логирование ошибок при запросе
            return f'Error: {str(ex)}'


def load_api_key() -> str:
    """
    Загружает API ключ из переменных окружения или запрашивает его у пользователя.

    :return: API ключ.
    :rtype: str
    """
    api_key: str = os.getenv('API_KEY')
    if not api_key:
        api_key = input('API ключ не найден. Введите API ключ от `gemini`: ')
        set_key('.env', 'API_KEY', api_key) # Сохранение ключа в файл .env
        logger.debug('API ключ получен от пользователя и сохранен в .env.') # Логирование получения ключа
    else:
        logger.debug('API ключ получен из переменных окружения.') # Логирование получения ключа
    return api_key


def load_system_instruction(base_path: Path, choice: str) -> str:
    """
    Загружает инструкцию для модели из файла.

    :param base_path: Базовый путь к директории инструкций.
    :type base_path: Path
    :param choice: Выбор пользователя (1, 2 или 3) для стиля баннера.
    :type choice: str
    :return: Инструкция для модели.
    :rtype: str
    """
    instructions: dict[str, str] = { # Исправлено: переменная в snake_case
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }
    if choice in instructions:
        try:
            instruction_path: Path = base_path / 'instructions' / f'{instructions[choice]}.md' # Путь к файлу инструкции
            system_instruction: str = instruction_path.read_text(encoding='UTF-8') # Чтение инструкции из файла
            logger.debug(f'Инструкция загружена из файла: {instruction_path}.') # Логирование загрузки инструкции
            return system_instruction
        except FileNotFoundError as ex:
             logger.error(f'Файл инструкции не найден: {ex}. Используется стиль по умолчанию.') # Логирование ошибки загрузки инструкции
             default_instruction_path: Path = base_path / 'instructions' / 'system_instruction_asterisk.md'
             return default_instruction_path.read_text(encoding='UTF-8')
    else:
        logger.warning(f'Неверный выбор стиля: {choice}. Используется стиль по умолчанию.') # Логирование неверного выбора стиля
        default_instruction_path: Path = base_path / 'instructions' / 'system_instruction_asterisk.md'
        return default_instruction_path.read_text(encoding='UTF-8') # Чтение инструкции по умолчанию


def get_user_text() -> str:
    """
    Запрашивает текст для баннера у пользователя.

    :return: Текст, введенный пользователем.
    :rtype: str
    """
    user_text: str = input('Введите текст для баннера: ') # Запрос текста у пользователя
    logger.debug(f'Пользователь ввел текст: {user_text}')  # Логирование ввода текста
    return user_text


def main():
    """
    Основная функция программы, запускает процесс создания баннера.
    """
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Относительный путь к директории
    base_path: Path = __root__ / relative_path  # Абсолютный путь к директории с использованием __root__

    api_key: str = load_api_key()  # Загрузка API ключа
    
    print('Добро пожаловать в игру Banner!')
    print('Введите текст, и я создам для вас текстовый баннер.')
    
    while True:
        print('Выберите стиль оформления баннера:')
        print('1. Символ \'*\'')
        print('2. Символ \'~\'')
        print('3. Символ \'#\'')
        choice: str = input('Введите номер стиля (1, 2 или 3): ') # Запрос выбора стиля у пользователя
        
        system_instruction: str = load_system_instruction(base_path, choice)  # Загрузка инструкции для модели
        model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction) # Создание экземпляра класса GoogleGenerativeAI
        
        user_text: str = get_user_text()  # Запрос текста у пользователя
        
        if user_text.strip() == '':
            print('Вы не ввели текст. Попробуйте снова.') # Сообщение об ошибке, если текст не введен
            logger.warning('Пользователь не ввел текст для баннера.') # Логирование пустой строки
        else:
            response: str = model.ask(user_text) # Отправка запроса модели
            print('\nВаш баннер готов:')
            print(response) # Вывод результата
            break

if __name__ == '__main__':
    main()

```