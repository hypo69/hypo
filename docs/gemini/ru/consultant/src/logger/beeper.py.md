# Анализ кода модуля beeper.py

**Качество кода**
7
-   Плюсы
    -   Код структурирован и разбит на классы и функции, что улучшает читаемость.
    -   Используется `Enum` для определения уровней событий, что делает код более понятным.
    -   Есть базовая обработка ошибок.
    -   Используется декоратор `silent_mode` для управления режимом беззвучия.
-   Минусы
    -   Не все функции и классы документированы в соответствии со стандартами docstring.
    -   Используется `print` вместо `logger` для вывода ошибок.
    -   Некорректное обращение к константам `BeepLevel`, в примере `melody = BeepLevel.SUCCESS.value[0]` ,  не обрабатываются все  ноты в мелодии а только первая, так как  `BeepLevel.SUCCESS.value` это `[('D5', 100), ('A5', 100), ('D6', 100)]` нужно перебрать все ноты.
    -   Много повторений кода в `if` ветке функции `beep`.
    -   Не используются константы для магических чисел (например, частоты и длительности звуков по умолчанию).

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring в формате RST ко всем классам, методам и функциям.
2.  **Логирование:** Заменить `print` на `logger.error` для вывода ошибок, а `logger.debug`  для отладочной информации.
3.  **Обработка ошибок:** Вместо общего `try-except` с `print`, использовать `logger.error` для более информативного логирования ошибок.
4.  **Константы:** Вынести значения по умолчанию (например, частоту и длительность) в константы.
5.  **Рефакторинг:** Упростить код в функции `beep` путем устранения дублирования.
6.  **Итерация мелодии:** В функции `beep` необходимо перебирать все ноты в мелодии, а не только первую.

**Оптимизированный код**

```python
"""
Модуль для генерации звуковых сигналов.
=========================================================================================

Этот модуль содержит класс :class:`Beeper` и :class:`BeepHandler`, которые используются для генерации звуковых сигналов
оповещения в зависимости от уровня важности события.

Пример использования
--------------------

Пример использования класса `Beeper`:

.. code-block:: python

    await Beeper.beep(level=BeepLevel.ERROR)
    await Beeper.beep(level='success')

Пример использования класса `BeepHandler`:

.. code-block:: python

    handler = BeepHandler()
    record = {"level": "ERROR"}
    handler.emit(record)
"""

import asyncio
import winsound
import time
from enum import Enum
from typing import Union
from src.logger.logger import logger #  импортируем logger

# Константы для частот
DEFAULT_FREQUENCY = 400
DEFAULT_DURATION = 1000

# Ноты и частоты
note_freq = {
    'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81, 'F3': 174.61,
    'F#3': 185.00, 'G3': 196.00, 'G#3': 207.65, 'A3': 220.00, 'A#3': 233.08, 'B3': 246.94,

    'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63, 'F4': 349.23,
    'F#4': 369.99, 'G4': 392.00, 'G#4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'B4': 493.88,

    'C5': 523.25, 'C#5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'E5': 659.26, 'F5': 698.46,
    'F#5': 739.99, 'G5': 783.99, 'G#5': 830.61, 'A5': 880.00, 'A#5': 932.33, 'B5': 987.77,

    'C6': 1046.50, 'C#6': 1108.73, 'D6': 1174.66, 'D#6': 1244.51, 'E6': 1318.51, 'F6': 1396.91,
    'F#6': 1479.98, 'G6': 1567.98, 'G#6': 1661.22, 'A6': 1760.00, 'A#6': 1864.66, 'B6': 1975.53,

    'C7': 2093.00, 'C#7': 2217.46, 'D7': 2349.32, 'D#7': 2489.02, 'E7': 2637.02, 'F7': 2793.83,
    'F#7': 2959.96, 'G7': 3135.96, 'G#7': 3322.44, 'A7': 3520.00, 'A#7': 3729.31, 'B7': 3951.07,
}
...
class BeepLevel(Enum):
    """   Класс перечислитель типов событий

    @details разным событиям соответствуют разные мелодии
    Уровни событий
    - SUCCESS
    - INFO
    - ATTENTION
    - WARNING
    - DEBUG
    - ERROR
    - LONG_ERROR
    - CRITICAL
    - BELL
    """
    SUCCESS = [('D5', 100), ('A5', 100), ('D6', 100)]
    #INFO = [('C6', 150), ('E6', 150), ('G6', 150), ('C7', 150)],
    INFO_LONG = [('C6', 150), ('E6', 150)],
    INFO = [('C6', 8)],
    #ATTENTION = [('G5', 120), ('F5', 120), ('E5', 120), ('D5', 120), ('C5', 120)],
    ATTENTION = [ ('G5', 600) ],
    WARNING = [('F5', 100), ('G5', 100), ('A5', 100), ('F6', 100)],
    DEBUG = [('E6', 150), ('D4', 500)],
    #ERROR = [('G5', 40), ('C7', 100)],
    ERROR = [ ('C7', 1000) ],
    LONG_ERROR = [('C7', 50), ('C7', 250)],
    CRITICAL = [('G5', 40), ('C7', 100)],
    BELL = [('G6', 200), ('C7', 200), ('E7', 200)],
...

class BeepHandler:
    """
    Класс для обработки звуковых сигналов на основе уровня логгирования.
    """
    def emit(self, record):
        """
        Выводит звуковой сигнал на основе уровня логгирования.

        Args:
            record (dict): Запись лога, содержащая уровень.
        """
        try:
            level = record["level"].name
            if level == 'ERROR':
                self.play_sound(880, 500)  # Проиграть "бип" для ошибок
            elif level == 'WARNING':
                self.play_sound(500, 300)  # Проиграть другой звук для предупреждений
            elif level == 'INFO':
                self.play_sound(300, 200)  # И так далее...
            else:
                self.play_default_sound()  # Дефолтный звук для других уровней логгирования
        except Exception as ex:
            logger.error(f'Ошибка воспроизведения звука: {ex}')

    def beep(self, level: BeepLevel | str = BeepLevel.INFO, frequency: int = DEFAULT_FREQUENCY, duration: int = DEFAULT_DURATION):
        """
        Вызывает метод beep класса Beeper для воспроизведения звукового сигнала.

        Args:
            level (BeepLevel | str, optional): Уровень звукового сигнала. Defaults to BeepLevel.INFO.
            frequency (int, optional): Частота звукового сигнала. Defaults to DEFAULT_FREQUENCY.
            duration (int, optional): Длительность звукового сигнала. Defaults to DEFAULT_DURATION.
        """
        Beeper.beep(level, frequency, duration)

...

# ------------------------------------------------------------------------------------------------

def silent_mode(func):
    """
    Функция-декоратор для управления режимом "беззвучия".

    Args:
        func (callable): Функция для декорирования.

    Returns:
        callable: Обернутая функция, добавляющая проверку режима "беззвучия".
    """
    def wrapper(*args, **kwargs):
        """
        Внутренняя функция-обертка для проверки режима "беззвучия" перед выполнением функции.

        Если режим "беззвучия" включен, выводит сообщение о пропуске воспроизведения звука и завершает выполнение функции beep.
        В противном случае вызывает оригинальную функцию, переданную как аргумент (func(*args, **kwargs)).

        Args:
            args: Позиционные аргументы, переданные в оборачиваемую функцию.
            kwargs: Именованные аргументы, переданные в оборачиваемую функцию.

        Returns:
            Результат выполнения оборачиваемой функции или None, если режим "беззвучия" включен.
        """
        if Beeper.silent:
            logger.debug("Silent mode is enabled. Skipping beep.")
            return
        return func(*args, **kwargs)
    return wrapper
...

class Beeper():
    """ класс звуковых сигналов """

    silent = False

    @staticmethod
    @silent_mode
    async def beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = DEFAULT_FREQUENCY, duration: int = DEFAULT_DURATION) -> None:
        """
        Звуковой сигнал оповещения.

        @details дает возможность на слух определить, что происходит в системе
        Args:
           level (BeepLevel | str, optional): тип события: `info`, `attention`, `warning`, `debug`, `error`, `long_error`, `critical`, `bell`
            или `Beep.SUCCESS`, `Beep.INFO`, `Beep.ATTENTION`, `Beep.WARNING`, `Beep.DEBUG`, `Beep.ERROR`, `Beep.LONG_ERROR`, `Beep.CRITICAL`, `Beep.BELL`.
           frequency (int, optional): частота сигнала в значениях от 37 до 32000. Defaults to 400.
           duration (int, optional): длительность сигнала. Defaults to 1000.
        """

        if isinstance(level, str):
            try:
                melody = BeepLevel[level.upper()].value
            except KeyError:
                logger.error(f'Неизвестный уровень звука: {level}')
                return
        elif isinstance(level, BeepLevel):
            melody = level.value
        else:
            logger.error(f'Неверный тип уровня звука: {level}')
            return

        for note, duration in melody:
            frequency = note_freq.get(note)
            if not frequency:
                logger.error(f'Неизвестная нота: {note}')
                continue
            try:
                winsound.Beep(int(frequency), duration)
            except Exception as ex:
                logger.error(f'Не бибикает :| \n                              Ошибка - {ex}, \n                              нота - {note},\n                              продолжительность - {duration}\n                                мелодия - {melody}')
                return
            time.sleep(0.0)

...
```