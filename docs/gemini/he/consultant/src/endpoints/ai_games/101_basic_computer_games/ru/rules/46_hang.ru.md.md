# Анализ кода модуля `46_hang.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
  -   **Преимущества:**
        - Документ содержит подробное описание игры "Виселица" на русском языке, включая правила, пошаговые инструкции, пример работы программы, возможные ограничения и рекомендации по реализации.
        - Структура документа логичная и хорошо организована, что облегчает понимание и использование информации.
        - Есть примеры работы программы, которые помогают понять игровой процесс.
        - Описаны возможные ограничения и рекомендации по реализации, что полезно для разработчиков.
  -  **Недостатки:**
        - Документ представлен в формате `markdown`, а не в виде кода `python`.
        - Отсутствуют конкретные блоки кода, которые можно было бы проверить на соответствие требованиям.
        - Нет информации о необходимых импортах или функциях, которые следует использовать при реализации.

**Рекомендации по улучшению**

1.  Преобразовать `markdown` в `python` код, разделив его на логические блоки.
2.  Добавить docstring для модуля и функций.
3.  Реализовать функциональность, описанную в документе.
4.  Использовать `j_loads` или `j_loads_ns` для работы с файлами JSON, если это необходимо.
5.  Использовать `from src.logger.logger import logger` для логирования ошибок.
6.  Использовать `reStructuredText` для комментариев.
7.  Привести переменные и функции к общему стилю именования.
8.  Добавить обработку исключений для возможных ошибок.

**Улучшенный код**
```python
"""
Модуль для реализации игры "Виселица".
=========================================================================================

Модуль содержит функции и логику для игры "Виселица", позволяющей игроку
угадывать слово по буквам.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    from src.games.hang import HangGame

    game = HangGame()
    game.play()
"""
import random # импорт модуля random для выбора случайного слова
from src.logger.logger import logger # импорт модуля logger для логирования ошибок
from src.utils.jjson import j_loads_ns # импорт функции для загрузки json

class HangGame:
    """
    Класс, представляющий игру "Виселица".

    :ivar words: Список слов для игры.
    :vartype words: list
    :ivar max_attempts: Максимальное количество попыток.
    :vartype max_attempts: int
    :ivar guessed_word: Слово, которое нужно угадать.
    :vartype guessed_word: str
    :ivar guessed_letters: Список угаданных букв.
    :vartype guessed_letters: list
    :ivar attempts_left: Количество оставшихся попыток.
    :vartype attempts_left: int
    """
    def __init__(self, words_file='words.json', max_attempts=6):
        """
        Инициализация игры.

        :param words_file: Путь к файлу со списком слов.
        :type words_file: str
        :param max_attempts: Максимальное количество попыток.
        :type max_attempts: int
        """
        try:
            # Загрузка списка слов из json-файла #
            self.words = j_loads_ns(words_file).get('words', [])
        except Exception as e:
            logger.error(f'Ошибка при загрузке слов из файла {words_file}: {e}')
            self.words = ['слово', 'игра', 'код', 'виселица'] # Дефолтные слова если произошла ошибка

        self.max_attempts = max_attempts
        self.guessed_word = self._choose_word()
        self.guessed_letters = []
        self.attempts_left = self.max_attempts

    def _choose_word(self) -> str:
         """
         Выбирает случайное слово из списка.

         :return: Случайное слово.
         :rtype: str
         """
         return random.choice(self.words)

    def _display_word(self) -> str:
        """
        Отображает слово с угаданными буквами и прочерками.

        :return: Строка с отображением слова.
        :rtype: str
        """
        display = ''
        for letter in self.guessed_word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()

    def _get_input(self) -> str:
        """
        Получает ввод буквы от пользователя.

        :return: Введенная буква.
        :rtype: str
        """
        while True:
            letter = input('Введите букву: ').lower()
            if len(letter) == 1 and letter.isalpha():
                return letter
            else:
                print('Некорректный ввод. Введите одну букву.')

    def _check_letter(self, letter: str) -> bool:
        """
        Проверяет, есть ли буква в слове.

        :param letter: Буква для проверки.
        :type letter: str
        :return: True, если буква есть в слове, иначе False.
        :rtype: bool
        """
        if letter in self.guessed_word:
            return True
        return False

    def _update_game_state(self, letter: str) -> None:
        """
        Обновляет состояние игры.

        :param letter: Введенная буква.
        :type letter: str
        """
        if self._check_letter(letter):
            self.guessed_letters.append(letter)
        else:
            self.attempts_left -= 1
            print(f'Буквы "{letter}" нет в слове. Осталось попыток: {self.attempts_left}')

    def _is_game_won(self) -> bool:
        """
        Проверяет, выиграл ли игрок.

        :return: True, если игрок выиграл, иначе False.
        :rtype: bool
        """
        return all(letter in self.guessed_letters for letter in self.guessed_word)

    def _is_game_lost(self) -> bool:
         """
         Проверяет, проиграл ли игрок.

         :return: True, если игрок проиграл, иначе False.
         :rtype: bool
         """
         return self.attempts_left == 0

    def play(self) -> None:
        """
        Запускает игровой процесс.
        """
        print('Добро пожаловать в игру Виселица!')
        print('Угадайте слово. У вас есть 6 попыток.')

        while not self._is_game_won() and not self._is_game_lost():
            print(f'Загаданное слово: {self._display_word()}')
            letter = self._get_input()
            self._update_game_state(letter)
        if self._is_game_won():
             print(f'Поздравляем! Вы угадали слово "{self.guessed_word}"!')
        else:
             print(f'Вы проиграли! Загаданное слово было "{self.guessed_word}".')

        while True:
                play_again = input('Хотите сыграть снова? (да/нет): ').lower()
                if play_again in ['да', 'нет']:
                     break
                else:
                     print('Введите "да" или "нет".')

        if play_again == 'да':
               self.__init__()
               self.play()
        else:
               print('Спасибо за игру!')

if __name__ == '__main__':
    game = HangGame()
    game.play()
```