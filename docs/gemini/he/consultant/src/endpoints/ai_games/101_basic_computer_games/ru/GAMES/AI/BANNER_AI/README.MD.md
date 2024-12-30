# Анализ кода модуля `BANNER_AI`

**Качество кода**
<br>
-  **Соответствие требованиям к формату кода (1-10):** 7

 -  **Преимущества**
    -   Код хорошо структурирован и читаем.
    -   Используется объектно-ориентированный подход, что облегчает расширение и поддержку кода.
    -   Применяется загрузка переменных окружения, что позволяет хранить API-ключ в безопасном месте.
    -   Использование абсолютных путей к файлам инструкций делает код более переносимым.
    -   Программа предлагает пользователю выбор стиля оформления баннера, что делает ее интерактивной.
    -   Присутствуют базовые проверки на ввод пользователя (пустая строка).

 -  **Недостатки**
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Не используется `from src.logger.logger import logger` для регистрации ошибок.
    -   Обработка ошибок в методе `ask` слишком общая и не дает достаточно информации об ошибке.
    -   Не все функции и методы имеют документацию в формате reStructuredText (RST).
    -   Отсутствует проверка корректности API ключа.
    -   Регулярные выражения не используются, хотя библиотека `re` импортирована.
    -   Зависимости `google` и `google-generativeai` не описаны в `requirements.txt`.

**Рекомендации по улучшению**

1.  **Использование `j_loads`**: Замените `Path(file_path).read_text()` на использование `j_loads` или `j_loads_ns` для чтения файлов инструкций. Это обеспечит дополнительную гибкость при обработке файлов.
2.  **Внедрение логирования**: Добавьте `from src.logger.logger import logger` и используйте его для логирования ошибок вместо `print(f'Error: {str(ex)}')`. Это позволит более эффективно отслеживать и диагностировать проблемы.
3.  **Добавление документации**: Задокументируйте все функции, методы и классы в формате reStructuredText (RST) с использованием docstring. Это улучшит читаемость и поддерживаемость кода.
4.  **Обработка ошибок**: Уточните обработку ошибок в методе `ask`. Вместо возврата простой строки об ошибке, используйте `logger.error` для записи деталей исключения и возвращайте более информативное сообщение об ошибке.
5.  **Проверка API ключа**: Добавьте проверку на корректность введенного API ключа.
6.  **Удаление неиспользуемого импорта**: Удалите неиспользуемый импорт `re`, если он не будет использоваться в будущем.
7.  **Удаление `try`-`except`**: Уберите `try-except` из блока `if __name__ == '__main__'` и замените его на регистрацию ошибок через `logger.error`.
8.  **Добавление `requirements.txt`**: Опишите зависимости в `requirements.txt`.

**Улучшенный код**
```python
"""
Модуль для создания текстовых баннеров с использованием Google Gemini.
=========================================================================================

Этот модуль взаимодействует с моделью Google Generative AI, позволяя пользователю создавать
текстовые баннеры в разных стилях. Пользователь может выбрать стиль оформления и отправить
текст для обработки.

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI` и основной программы:

.. code-block:: python

    from pathlib import Path
    from src.utils.jjson import j_loads_ns
    from src.logger.logger import logger
    from dotenv import load_dotenv, set_key
    import os

    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')
    base_path: Path = __root__ / relative_path
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')
        set_key('.env', 'API_KEY', API_KEY)
    instructions: dict = {
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }
    choice = '1'
    system_instruction: str = j_loads_ns(Path(base_path, 'instructions', f'{instructions[choice]}.md'))
    model = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
    user_text = "Hello, World!"
    response = model.ask(user_text)
    print(response)
"""
import google.generativeai as genai  # Импорт библиотеки для работы с Gemini
# import re  # Импорт библиотеки для работы с регулярными выражениями # Удалено неиспользуемый импорт
from pathlib import Path  # Импорт для работы с путями файловой системы
from header import __root__  # Импорт объекта __root__, содержащего абсолютный путь к корню проекта
from dotenv import load_dotenv, set_key  # Импорт функций для работы с переменными окружения
import os  # Импорт для работы с переменными окружения
from src.utils.jjson import j_loads_ns # Импорт функции для чтения json файлов # Added import
from src.logger.logger import logger # Added import

load_dotenv()  # Загрузка переменных окружения из файла .env # Added comment


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделью Google Generative AI.

    :ivar MODELS: Список доступных моделей Google Generative AI.
    :vartype MODELS: list[str]
    :ivar api_key: Ключ API для доступа к Gemini.
    :vartype api_key: str
    :ivar model_name: Название используемой модели Gemini.
    :vartype model_name: str
    :ivar model: Инициализированная модель Google Generative AI.
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
        self.api_key = api_key  # Сохранение API ключа
        self.model_name = model_name  # Сохранение названия модели
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
            logger.error('Ошибка при обращении к модели Gemini', exc_info=ex)  # Регистрация ошибки с использованием logger # Changed log
            return f'Ошибка: Произошла ошибка при выполнении запроса к модели.' # changed text

if __name__ == '__main__':
    """
    Основная часть программы.

    Определение путей к файлам инструкций, чтение API ключа, выбор стиля баннера,
    и отправка запроса модели.
    """
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Относительный путь к директории
    base_path: Path = __root__ / relative_path  # Абсолютный путь к директории с использованием __root__
    API_KEY: str = os.getenv('API_KEY')  # Получение API ключа из переменных окружения
    if not API_KEY:  # Проверка наличия API ключа
        API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
        set_key('.env', 'API_KEY', API_KEY)  # Сохранение ключа в файл .env # Added comment

    instructions: dict = {  # Словарь инструкций
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }
    print('Добро пожаловать в игру Banner!')  # Приветствие пользователя
    print('Введите текст, и я создам для вас текстовый баннер.')  # Объяснение функционала программы

    while True:  # Цикл выбора стиля баннера
        print('Выберите стиль оформления баннера:') # Вывод вариантов выбора
        print('1. Символ \'\\*\'')  # Вариант 1
        print('2. Символ \'~\'')  # Вариант 2
        print('3. Символ \'#\'')  # Вариант 3
        choice = input('Введите номер стиля (1, 2 или 3): ')  # Запрос выбора пользователя

        if choice in ('1', '2', '3'):  # Проверка выбора пользователя
            try:
                # Чтение инструкции из файла с использованием j_loads_ns # Changed read_text to j_loads_ns
                system_instruction: str = j_loads_ns(Path(base_path, 'instructions', f'{instructions[choice]}.md'))
            except Exception as ex:
                logger.error('Ошибка при чтении файла с инструкцией', exc_info=ex) #  Log error
                print('Ошибка при загрузке инструкции. Используется стиль по умолчанию \'\\*\'')
                system_instruction: str = j_loads_ns(Path(base_path, 'instructions', 'system_instruction_asterisk.md'))
            break
        else:
           print('Неверный выбор. Попробуйте снова.')  # Сообщение об ошибке выбора
    try: # Added try except
        model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)  # Создание экземпляра класса
        user_text: str = input('Введите текст для баннера: ')  # Запрос текста у пользователя
        if user_text.strip() == '':  # Проверка на пустой ввод
            print('Вы не ввели текст. Попробуйте снова.')  # Сообщение об ошибке
        else:
            response = model.ask(user_text)  # Отправка запроса модели
            print('\nВаш баннер готов:')  # Вывод результата
            print(response)  # Вывод баннера
    except Exception as ex:  # Catch all errors
            logger.error('Произошла критическая ошибка', exc_info=ex) # Log error
            print('Произошла ошибка во время работы программы.') # Inform user
```