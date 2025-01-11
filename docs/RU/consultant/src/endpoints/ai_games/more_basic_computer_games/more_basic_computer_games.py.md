# Анализ кода модуля `more_basic_computer_games`

**Качество кода**
**6/10**
- Плюсы
    - Код структурирован в класс `MoreBasicGames`, что способствует организации и переиспользованию.
    - Используются асинхронные операции `async/await`, что хорошо для работы с API.
    - Код читаем, хотя и требует некоторых улучшений в стиле.
- Минусы
    - Не все docstring соответствуют стандарту reStructuredText (RST).
    - Отсутствует логирование ошибок.
    - Используется `time.sleep` для задержки, что не является лучшей практикой в асинхронном коде.
    - Много магических строк и чисел, которые можно было бы вынести в константы.
    - Не хватает комментариев для сложных участков кода.
    - Нарушение PEP8 в именовании переменных ( `lanf` вместо `lang`).
    - Дублирование кода при удалении начальных и конечных символов ```.
    - Отсутствует обработка ошибок при чтении файлов.

**Рекомендации по улучшению**
1.  **Документация**:
    *   Переписать все docstring в формате RST.
    *   Добавить описания параметров и возвращаемых значений для всех методов.
2.  **Логирование**:
    *   Использовать `logger.error` для логирования ошибок вместо `try-except ... print`.
3.  **Асинхронность**:
    *   Заменить `time.sleep` на `asyncio.sleep` для асинхронных задержек.
4.  **Константы**:
    *   Вынести магические строки (например, `'```'`, `'python'`) в константы.
5.  **Обработка ошибок**:
    *   Добавить обработку ошибок при чтении файлов, чтобы избежать падения приложения.
6.  **Улучшение читаемости**:
    *   Добавить комментарии для сложных участков кода.
    *   Исправить опечатку в `__init__` ( `lanf` -> `lang`).
7.  **Рефакторинг**:
    *  Упростить логику удаления начальных и конечных символов ```.
8. **Соответствие PEP8**:
    *   Соблюдать PEP8 для именования переменных ( `lanf` -> `lang`).
    *   Сделать код более консистентным и читаемым.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для генерации базовых компьютерных игр.
=========================================================================================

Этот модуль содержит класс :class:`MoreBasicGames`, который используется для генерации
Python кода для различных простых компьютерных игр с использованием моделей ИИ, таких как
Google Gemini.

Пример использования
--------------------

Пример использования класса `MoreBasicGames`:

.. code-block:: python

    games = MoreBasicGames(lang='ru')
    asyncio.run(games.generate_python_code())
"""
import asyncio
import time
from pathlib import Path
# from src import gs # fixme: remove after debug
from src.ai.gemini import GoogleGenerativeAI
# from src.ai.openai import OpenAIModel # fixme: not use
from src.utils.jjson import j_loads_ns
from src.utils.file import get_filenames
# from src.utils.printer import pprint # fixme: not use
from src.logger.logger import logger
from typing import List # fixme: use typing

class MoreBasicGames:
    """
    Класс для генерации Python кода простых компьютерных игр.

    :ivar lang: Язык, на котором будут сгенерированы правила и код игр.
    :vartype lang: str
    :ivar bob: Объект GoogleGenerativeAI для взаимодействия с моделью Gemini.
    :vartype bob: GoogleGenerativeAI
    :ivar base: Базовое имя для каталогов и файлов.
    :vartype base: str
    :ivar base_path: Путь к базовой директории модуля.
    :vartype base_path: Path
    :ivar command_instruction: Инструкции для генерации кода.
    :vartype command_instruction: str
    :ivar games_list: Список имен игр.
    :vartype games_list: list
    """
    lang: str
    bob: GoogleGenerativeAI
    base: str = 'more_basic_computer_games'
    base_path: Path # fixme: add type
    command_instruction: str
    games_list: List[str] = []
    CODE_START_MARKERS = ('```', '```python')
    CODE_END_MARKERS = ('```', '```\n')

    def __init__(self, lang: str = 'en'):
        """
        Инициализирует объект MoreBasicGames.

        :param lang: Язык для генерации правил и кода игр (по умолчанию 'en').
        :type lang: str
        """
        # fixme:  gs is not import in this module
        from src import gs
        self.base_path = gs.path.endpoints / 'ai_games' / self.base
        config = j_loads_ns(self.base_path / 'more_basic_computer_games.json')
        self.lang = lang
        try:
            system_instruction = Path(self.base_path / 'assets' / 'instructions' / 'raw.txt').read_text(encoding='UTF-8')
            self.command_instruction = Path(self.base_path / 'assets' / 'instructions' / f'{self.base}_write_code.{self.lang}.md').read_text(encoding='UTF-8')
        except FileNotFoundError as e:
            logger.error(f'Ошибка чтения файла: {e}')
            raise
        except Exception as e:
            logger.error(f'Непредвиденная ошибка при чтении файлов: {e}')
            raise

        self.bob = GoogleGenerativeAI(
            model_name=config.model_name,
            api_key=gs.credentials.gemini.onela,
            system_instruction=system_instruction,
        )
        self.load_games_list()

    def load_games_list(self) -> None:
        """
        Генерирует список имен игр из файлов в каталоге 'rules'.

        Извлекает имя игры из каждого файла, приводя его к верхнему регистру и заменяя
        подчеркивания на пробелы.
        """
        try:
            rules_files = get_filenames(self.base_path / self.lang / 'rules')
            for file_name in rules_files:
                game_name = file_name.split('_', 1)[1].split('.')[0]
                self.games_list.append(game_name.upper().replace('_', ' '))
        except Exception as e:
            logger.error(f'Ошибка при загрузке списка игр: {e}')


    async def generate_python_code(self) -> None:
        """
        Генерирует Python код для каждой игры в списке.
        """
        for game in self.games_list:
            q = self.command_instruction.replace('<GAME>', f'<{game}>')
            print(game)
            try:
                response = await self.bob.ask(q)
                if response.startswith(self.CODE_START_MARKERS) and response.endswith(self.CODE_END_MARKERS):
                    response = response.lstrip('`').lstrip('python').lstrip()
                    response = response.rstrip('`').rstrip()

                self.save_code(game, response)
                await asyncio.sleep(20) # fixme: use asyncio.sleep

            except Exception as e:
                logger.error(f'Ошибка при генерации кода для игры {game}: {e}')


    def save_code(self, game: str, code: str) -> None:
        """
        Сохраняет сгенерированный Python код в файл.

        :param game: Имя игры.
        :type game: str
        :param code: Сгенерированный код.
        :type code: str
        """
        output_file: Path = self.base_path / self.lang / 'py' / f'{game.lower().replace(" ", "_")}.py'
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(code, encoding='UTF-8')
            print(f'saved {game}')
        except Exception as e:
            logger.error(f'Ошибка при сохранении кода для игры {game}: {e}')

    def create_rules_files(self) -> None:
        """
        Создает пустые файлы правил для каждой игры.
        """
        rules_files = [
            "1_artillery_3.ru.md",
            "2_baccarat.ru.md",
            "3_bible_quiz.ru.md",
            "4_big_6.ru.md",
            "5_binary.ru.md",
            "6_blackbox.ru.md",
            "7_bobstones.ru.txt",
            "8_bocce.ru.md",
            "9_boga_ii.ru.md",
            "10_bombrun.ru.md",
            "11_bridge_it.ru.md",
            "12_camel.ru.md",
            "13_chase.ru.md",
            "14_chuck_a_luck.ru.md",
            "15_close_encounters.ru.md",
            "16_column.ru.md",
            "17_concentration.ru.md",
            "18_condot.ru.md",
            "19_convoy.ru.md",
            "20_corral.ru.md",
            "21_countdown.ru.md",
            "22_cup.ru.md",
            "23_dealerx_5.ru.md",
            "24_deepspace.ru.md",
            "25_defuse.ru.md",
            "26_dodgem.ru.md",
            "27_doors.ru.md",
            "28_drag.ru.md",
            "29_eliza.ru.md",
            "30_father.ru.md",
            "31_flip.ru.md",
            "32_four_in_a_row.ru.md",
            "33_geowar.ru.md",
            "34_grand_prix.ru.md",
            "35_guess_it.ru.md",
            "36_icbm.ru.md",
            "37_inkblot.ru.md",
            "38_joust.ru.md",
            "39_jumping_balls.ru.md",
            "40_keno.ru.md",
            "41_lgame.ru.md",
            "42_life_expectancy.ru.md",
            "43_lissajous.ru.md",
            "44_magic_square.ru.md",
            "45_man_eating_rabbit.ru.md",
            "46_maneuvers.ru.md",
            "47_mastermind.ru.md",
            "48_masterbagels.ru.md",
            "49_matpuzzle.ru.md",
            "50_maze.ru.md",
            "51_minotaur.ru.md",
            "52_motorcycle_jump.ru.md",
            "53_nomad.ru.md",
            "54_not_one.ru.md",
            "55_obstacle.ru.md",
            "56_octrlx.ru.md",
            "57_pasart.ru.md",
            "58_pasart2.ru.md",
            "59_pinball.ru.md",
            "60_rabbit_chase.ru.md",
            "61_roadrace.ru.md",
            "62_rotate.ru.md",
            "63_safe.ru.md",
            "64_scales.ru.md",
            "65_schmoo.ru.md",
            "66_seabattle.ru.md",
            "67_seawar.ru.md",
            "68_shoot.ru.md",
            "69_smash.ru.md",
            "70_strike_9.ru.md",
            "71_tennis.ru.md",
            "72_tlckertape.ru.md",
            "73_tv_plot.ru.md",
            "74_twonky.ru.md",
            "75_two_to_ten.ru.md",
            "76_ufo.ru.md",
            "77_under_and_over.ru.md",
            "78_vangam.ru.md",
            "79_warflsh.ru.md",
            "80_word_search_puzzle.ru.md",
            "81_wumpus_1.ru.md",
            "82_wumpus_2.ru.md"
        ]
        for file in rules_files:
            output_file: Path = Path(self.base_path / self.lang / 'rules' / file)
            try:
                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text('', encoding='UTF-8')
            except Exception as e:
                logger.error(f'Ошибка при создании файла правил {file}: {e}')


if __name__ == '__main__':
    langs_list: List[str] = ['ru', 'he', 'en']

    for lang in langs_list:
        g = MoreBasicGames(lang)
        # g.create_rules_files()
        asyncio.run(g.generate_python_code())
```