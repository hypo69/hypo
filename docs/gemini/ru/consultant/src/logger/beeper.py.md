# Анализ кода модуля beeper

**Качество кода**
8
- Плюсы
    - Код имеет хорошую структуру, использует `Enum` для определения уровней событий, что делает его более читаемым и поддерживаемым.
    - Присутствует декоратор `@silent_mode`, который позволяет отключать звуковые сигналы, что является полезной функцией.
    - Используются константы для частот нот, что облегчает понимание кода.

- Минусы
    - Используется стандартный `print` для вывода ошибок, что не соответствует рекомендациям по использованию `logger.error`.
    - В блоке `try-except` внутри `BeepHandler.emit` не обрабатываются ошибки.
    - Не все функции и методы имеют docstring в формате RST.
    - Используются magic strings в `BeepHandler.emit`, лучше использовать Enum `BeepLevel`
    - Не используется `asyncio.sleep` вместо `time.sleep` в асинхронном коде.
    - Обработка мелодии выполняется не оптимально, проигрывается только первый элемент.
    - Отсутствует импорт `logger`.

**Рекомендации по улучшению**
1.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
2.  Заменить `print` на `logger.error` в блоках `try-except` для правильного логирования ошибок.
3.  Добавить docstring в формате RST для всех функций, методов и классов.
4.  Использовать `asyncio.sleep` вместо `time.sleep` в асинхронных функциях.
5.  В `Beeper.beep` переработать логику проигрывания мелодии, чтобы проигрывать все ноты из `BeepLevel.value`.
6.  Избавиться от `try-except` внутри цикла в `Beeper.beep` и перенести его за цикл
7.  Улучшить проверку типа `level` в `Beeper.beep`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.logger.beeper
    :platform: Windows, Unix
    :synopsis: Модуль для управления звуковыми сигналами.

    Этот модуль предоставляет классы и функции для воспроизведения звуковых сигналов
    различных уровней важности, а также для управления режимом беззвучия.
"""

import asyncio
import winsound
from enum import Enum
from typing import Union
from src.logger.logger import logger  # Импорт logger

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

class BeepLevel(Enum):
    """
    Класс перечислитель типов событий.

    :details: Разным событиям соответствуют разные мелодии.
    Уровни событий:
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
    INFO_LONG = [('C6', 150), ('E6', 150)]
    INFO = [('C6', 8)]
    ATTENTION = [('G5', 600)]
    WARNING = [('F5', 100), ('G5', 100), ('A5', 100), ('F6', 100)]
    DEBUG = [('E6', 150), ('D4', 500)]
    ERROR = [('C7', 1000)]
    LONG_ERROR = [('C7', 50), ('C7', 250)]
    CRITICAL = [('G5', 40), ('C7', 100)]
    BELL = [('G6', 200), ('C7', 200), ('E7', 200)]

class BeepHandler:
    """
    Класс для обработки звуковых сигналов на основе уровней логирования.
    """
    def emit(self, record):
        """
        Воспроизводит звуковой сигнал в зависимости от уровня логирования.

        :param record: Запись лога, содержащая уровень логирования.
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

    def beep(self, level: Union[BeepLevel, str] = BeepLevel.INFO, frequency: int = 400, duration: int = 1000):
        """
        Вызывает статический метод beep класса Beeper.

        :param level: Уровень сигнала (BeepLevel или строка).
        :param frequency: Частота сигнала.
        :param duration: Длительность сигнала.
        """
        Beeper.beep(level, frequency, duration)


def silent_mode(func):
    """
    Функция-декоратор для управления режимом "беззвучия".

    :param func: Функция для декорирования.
    :return: Обернутая функция, добавляющая проверку режима "беззвучия".
    """
    def wrapper(*args, **kwargs):
        """
        Внутренняя функция-обертка для проверки режима "беззвучия" перед выполнением функции.

        :param args: Позиционные аргументы, переданные в оборачиваемую функцию.
        :param kwargs: Именованные аргументы, переданные в оборачиваемую функцию.
        :return: Результат выполнения оборачиваемой функции или None, если режим "беззвучия" включен.
        """
        if Beeper.silent:
            logger.debug("Silent mode is enabled. Skipping beep.")
            return
        return func(*args, **kwargs)
    return wrapper


class Beeper:
    """Класс звуковых сигналов."""

    silent = False

    @staticmethod
    @silent_mode
    async def beep(level: Union[BeepLevel, str] = BeepLevel.INFO, frequency: int = 400, duration: int = 1000) -> None:
        """
        Звуковой сигнал оповещения.

        :details: Позволяет на слух определить, что происходит в системе.
        :param level: Тип события: `info`, `attention`, `warning`, `debug`, `error`, `long_error`, `critical`, `bell`
                      или `Beep.SUCCESS`, `Beep.INFO`, `Beep.ATTENTION`, `Beep.WARNING`, `Beep.DEBUG`, `Beep.ERROR`, `Beep.LONG_ERROR`, `Beep.CRITICAL`, `Beep.BELL`.
        :param frequency: Частота сигнала в значениях от 37 до 32000.
        :param duration: Длительность сигнала.
        """
        if isinstance(level, str):
            try:
                level = BeepLevel[level.upper()]
            except KeyError:
                logger.error(f'Неизвестный уровень сигнала: {level}')
                return

        if isinstance(level, BeepLevel):
             melody = level.value
        else:
            logger.error(f"Неверный тип уровня: {level}")
            return
        try:
            for note, duration in melody:
                frequency = note_freq[note]
                winsound.Beep(int(frequency), duration)
                await asyncio.sleep(0.0)
        except Exception as ex:
            logger.error(f'''Не бибикает :|
                             Ошибка - {ex},
                             нота - {note},
                             продолжительность - {duration}
                              мелодия - {melody}''')
            return
```