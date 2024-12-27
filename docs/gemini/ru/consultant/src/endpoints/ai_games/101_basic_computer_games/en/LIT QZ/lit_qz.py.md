# Анализ кода модуля `lit_qz.py`

**Качество кода: 7/10**
-  Плюсы
    - Код достаточно прост для понимания и соответствует базовым требованиям игры "викторина".
    -  Используется регистронезависимое сравнение ответов, что делает игру более удобной для пользователя.
    -  Структура кода логична и соответствует описанному алгоритму игры.
-  Минусы
    - Отсутствует обработка ошибок.
    - Нет документации в формате reStructuredText (RST).
    - Код не использует логирование.
    - Имена переменных и функций не приведены в соответствие со стилем ранее обработанных файлов.

**Рекомендации по улучшению**
1. **Документация**: Необходимо добавить docstring в формате reStructuredText (RST) для модуля, функций и переменных, чтобы улучшить читаемость и документирование кода.
2. **Логирование**: Вместо `print` следует использовать `logger` для вывода сообщений, а также добавить обработку возможных ошибок с помощью `try-except` и `logger.error`.
3. **Структура кода**: Необходимо добавить константы для сообщений, чтобы сделать код более читаемым и поддерживаемым.
4. **Стиль кода**: Следует использовать нижний регистр для переменных и добавить snake_case для наименования переменных.

**Оптимизированный код**
```python
"""
Модуль для реализации простой викторины.
=========================================================================================

Этот модуль содержит реализацию игры "LIT QZ", в которой пользователю задаются вопросы и он должен на них ответить.
Игра предназначена для проверки знаний пользователя.

Пример использования
--------------------

.. code-block:: python

   python lit_qz.py

"""
import logging
from src.logger.logger import logger  # Импорт модуля для логирования

__author__ = 'hypo69 (hypo69@davidka.net)'

# Константы для сообщений
RIGHT_ANSWER_MESSAGE = "RIGHT"
WRONG_ANSWER_MESSAGE = "WRONG"
END_GAME_MESSAGE = "THAT'S ALL FOLKS!"

# Список вопросов и ответов
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the chemical symbol for water?", "H2O"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci")
]
#  Инициализация индекса текущего вопроса
question_index = 0


def ask_question(question: str) -> str:
    """
    Выводит вопрос на экран и запрашивает ответ от пользователя.

    :param question: Текст вопроса.
    :return: Ответ пользователя.
    """
    try:
        print(question)
        user_answer = input("Your answer: ")
        return user_answer
    except Exception as ex:
        logger.error(f"Ошибка при запросе ответа пользователя: {ex}")
        return ""


def check_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Сравнивает ответ пользователя с правильным ответом (без учета регистра).

    :param user_answer: Ответ пользователя.
    :param correct_answer: Правильный ответ.
    :return: True если ответ верен, False если нет.
    """
    try:
        return user_answer.lower() == correct_answer.lower()
    except Exception as ex:
        logger.error(f"Ошибка при проверке ответа: {ex}")
        return False


def display_result(is_correct: bool):
    """
    Выводит сообщение о правильности ответа.

    :param is_correct: True если ответ верен, False если нет.
    """
    if is_correct:
        print(RIGHT_ANSWER_MESSAGE)
    else:
        print(WRONG_ANSWER_MESSAGE)


def game_loop():
    """
    Основной игровой цикл.

    Итерирует по списку вопросов, запрашивает ответ пользователя и проверяет его на правильность.
    """
    global question_index #  Указывает, что используется глобальная переменная question_index
    while question_index < len(questions):
        try:
            current_question, correct_answer = questions[question_index] #  Извлекает текущий вопрос и правильный ответ из списка вопросов
            user_answer = ask_question(current_question)  # Запрашивает ввод ответа пользователя
            is_correct = check_answer(user_answer, correct_answer) # Проверяет правильность ответа
            display_result(is_correct) # Выводит результат
            question_index += 1 # Увеличивает индекс вопроса
        except Exception as ex:
            logger.error(f"Ошибка в основном игровом цикле: {ex}")
            break


def end_game():
    """
    Выводит сообщение об окончании игры.
    """
    print(END_GAME_MESSAGE)


if __name__ == "__main__":
    """
    Основная точка входа в программу.
    """
    game_loop()
    end_game()
```