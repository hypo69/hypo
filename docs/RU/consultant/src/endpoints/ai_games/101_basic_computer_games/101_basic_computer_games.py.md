# Анализ кода модуля `101_basic_games`

**Качество кода**
7
- Плюсы
    - Код использует асинхронность для выполнения задач, что позволяет повысить производительность.
    - Применяются `Pathlib` для работы с путями, что улучшает читаемость и кроссплатформенность.
    - Логика разделена на несколько методов, что делает код более модульным.
    - Код использует `j_loads_ns` для загрузки json файлов.
    - Используются docstring для описания классов и методов.
- Минусы
    - Отсутствует явная обработка ошибок в некоторых местах.
    - Комментарии не соответствуют стандарту reStructuredText.
    - Не все функции и методы имеют подробное описание.
    - Присутствует использование `time.sleep`, что может замедлить выполнение кода.
    - Не используется логирование.
    - В условных выражениях `if file_name == ('README.MD' or 'TOC.MD'):` используется `or` вместо `in`, что может привести к нежелательному поведению.
    - В функции `save_code` есть многоточие `...`, что является точкой остановки.

**Рекомендации по улучшению**

1.  **Добавить обработку ошибок**: Используйте `try-except` блоки и логирование ошибок для всех операций с файлами и API.
2.  **Привести комментарии в соответствие с reStructuredText**: Перепишите docstring и комментарии в формате reStructuredText.
3.  **Добавить логирование**: Используйте `logger` для записи ошибок и отладочной информации.
4.  **Улучшить обработку файлов**: Замените проверку `if file_name == ('README.MD' or 'TOC.MD'):` на более корректную проверку `if file_name in ('README.MD', 'TOC.MD'):`.
5.  **Удалить `time.sleep`**: По возможности, избегайте использования `time.sleep` и используйте асинхронные методы для задержки.
6.  **Заменить многоточие**: Заменить многоточие `...` на конкретный код или оператор `pass`, если это необходимо.
7.  **Переименовать переменную `lanf` на `lang`** исправить опечатку в наименовании параметра инициализатора.

**Оптимизированный код**
```python
"""
Модуль для работы с базовыми компьютерными играми.
=========================================================================================

Этот модуль содержит класс :class:`Games101Basic`, который используется для генерации и сохранения кода для базовых компьютерных игр.
Он взаимодействует с моделями Google Gemini для генерации кода на основе текстовых инструкций.

Пример использования
--------------------

Пример использования класса `Games101Basic`:

.. code-block:: python

    games = Games101Basic(lang='en')
    asyncio.run(games.generate_repository_toc())
    asyncio.run(games.generate_python_code())
"""
import asyncio
import time
from pathlib import Path
from typing import List

from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.jjson import j_loads_ns
from src.utils.file import get_filenames
from src.logger.logger import logger #  Импорт logger

class Games101Basic:
    """
    Класс для генерации и управления базовыми компьютерными играми.

    :param lang: Язык для генерации кода и документации.
    :type lang: str
    """
    lang: str
    bob: GoogleGenerativeAI
    base: str = '101_basic_computer_games'
    base_path: Path = gs.path.endpoints / 'ai_games' / base

    def __init__(self, lang: str = 'en'):
        """
        Инициализирует экземпляр класса Games101Basic.

        :param lang: Язык для генерации кода и документации.
        :type lang: str
        """
        try:
            config = j_loads_ns(self.base_path / '101_basic_computer_games.json')
            self.lang = lang
            system_instruction = Path(self.base_path / 'assets' / 'instructions' / 'fts.txt').read_text(encoding='UTF-8')
            self.bob = GoogleGenerativeAI(
                model_name=config.model_name,
                api_key=gs.credentials.gemini.onela,
                system_instruction=system_instruction,
            )
        except Exception as ex:
            logger.error('Ошибка при инициализации Games101Basic', exc_info=True)
            ...

    @property
    def games_list(self) -> List[str]:
        """
        Возвращает список имен игр, полученных из файлов в каталоге 'rules'.

        Имена игр извлекаются из имен файлов, преобразуются к верхнему регистру и подчеркивания заменяются пробелами.

        :return: Список имен игр.
        :rtype: List[str]
        """
        rules_files = get_filenames(self.base_path / self.lang / 'rules')
        games: List[str] = []
        for file_name in rules_files:
            if file_name in ('README.MD', 'TOC.MD'):
                continue
            game_name = file_name.split('_', 1)[1].split('.')[0]
            games.append(game_name.upper().replace('_', ' '))
        return games

    async def generate_python_code(self):
        """
        Генерирует Python код для каждой игры в списке.

        Код генерируется с помощью модели Gemini на основе инструкций.
        """
        for game in self.games_list:
            try:
                command_instruction: str = Path(self.base_path / 'assets' / 'instructions' / f'{self.base}_write_code.{self.lang}.md').read_text(encoding='UTF-8')
                q = command_instruction.replace('<GAME>', f'<{game}>')
                print(game)
                response = await self.bob.ask(q)
                if response.startswith(('```', '```python')) and response.endswith(('```', '```\n')):
                    response = response.lstrip('`')
                    if response.startswith('python'):
                        response = response[len('python'):].lstrip()
                    response = response.rstrip('`').rstrip()
                self.save_code(game, response)
                # time.sleep(20) #  Закоментировал time.sleep
            except Exception as ex:
                logger.error(f'Ошибка при генерации кода для игры {game}', exc_info=True)
                ...

    def save_code(self, game: str, code: str):
        """
        Сохраняет сгенерированный код в файл.

        :param game: Название игры.
        :type game: str
        :param code: Сгенерированный код.
        :type code: str
        """
        try:
            output_file: Path = self.base_path / self.lang / game / f'{game.lower().replace(" ", "_")}.py'
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(code, encoding='UTF-8')
            print('saved')
        except Exception as ex:
            logger.error(f'Ошибка при сохранении кода для игры {game}', exc_info=True)
            ...

    async def generate_repository_toc(self):
        """
        Генерирует оглавление репозитория.

        Оглавление создается на основе списка игр и сохраняется в файл 'TOC.MD'.
        """
        try:
            command_instruction = Path(self.base_path / 'assets' / 'instructions' / f'{self.base}_create_toc.{self.lang}.md').read_text(encoding='UTF-8')
            q = command_instruction + str(self.games_list)
            response = await self.bob.ask(q)
            output_file: Path = self.base_path / self.lang / 'TOC.MD'
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(response, encoding='UTF-8')
        except Exception as ex:
            logger.error('Ошибка при генерации оглавления репозитория', exc_info=True)
            ...

if __name__ == '__main__':
    langs_list: List[str] = ['ru', 'he']
    executed_langs_list: List[str] = ['en']
    for lang in langs_list:
        print(f'Start: {lang}')
        g101 = Games101Basic(lang)
        asyncio.run(g101.generate_repository_toc())
        # asyncio.run(g101.generate_python_code())
```