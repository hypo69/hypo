# Анализ кода модуля beeper

**Качество кода**
7
 -  Плюсы
    - Код структурирован, присутствуют классы и функции.
    - Используется `Enum` для определения уровней событий.
    - Присутствуют docstring для функций и классов, что облегчает понимание кода.
    -  Реализован декоратор `silent_mode` для отключения звуков.

 -  Минусы
    -  Не используется `j_loads` или `j_loads_ns` для чтения файлов, хотя это требование инструкции.
    - Присутствуют избыточные try-except блоки.
    - Не все комментарии соответствуют формату reStructuredText.
    -  Используется `print` для вывода ошибок, вместо логирования через `logger`.
    - В коде присутствуют неиспользуемые переменные, закомментированный код, а также не все перечисления `BeepLevel` имеют описание.
    -  В `Beeper.beep` не обрабатываются все возможные `level` типа `str`
    - Есть `...` в коде.

**Рекомендации по улучшению**

1. **Использовать `j_loads` или `j_loads_ns`:** В данном файле нет операций чтения из файла, но если бы они были, следует использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2. **Логирование ошибок:** Заменить `print` на `logger.error` для логирования ошибок.
3. **Формат комментариев:** Привести все комментарии к формату reStructuredText.
4. **Обработка ошибок:** Убрать избыточные `try-except`, использовать `logger.error`.
5.  **Исправить docstring:** Добавить полное описание всех элементов перечисления BeepLevel, а так же функции  `silent_mode` и `Beeper.beep`.
6.  **Добавить обработку всех вариантов `level` в `Beeper.beep`**: Добавить проверку всех уровней `str` в `Beeper.beep`.
7. **Удалить неиспользуемый код**: Удалить закомментированные блоки кода и неиспользуемые переменные.
8. **Удалить `...`**: Заменить `...` на корректную реализацию или удалить, если он не нужен.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для генерации звуковых сигналов.
=========================================================================================

Этот модуль предоставляет классы и функции для генерации звуковых сигналов,
используемых для оповещений в системе. Включает в себя возможность настройки
уровня сигнала, частоты и длительности.

.. code-block:: python

    from src.logger.beeper import Beeper, BeepLevel

    async def main():
        await Beeper.beep(BeepLevel.SUCCESS)
        await Beeper.beep(level='error')


    if __name__ == '__main__':
        asyncio.run(main())
"""

MODE = 'dev'

import asyncio
import winsound
import time
from enum import Enum
from typing import Union
from src.logger.logger import logger #  Импорт логгера

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
    Перечисление уровней звуковых сигналов.

    :param SUCCESS: Сигнал успешного выполнения.
    :param INFO: Информационный сигнал.
    :param INFO_LONG: Длинный информационный сигнал.
    :param ATTENTION: Сигнал внимания.
    :param WARNING: Сигнал предупреждения.
    :param DEBUG: Сигнал отладки.
    :param ERROR: Сигнал ошибки.
    :param LONG_ERROR: Длинный сигнал ошибки.
    :param CRITICAL: Критический сигнал.
    :param BELL: Сигнал колокола.
    """
    SUCCESS = [('D5', 100), ('A5', 100), ('D6', 100)]
    INFO_LONG = [('C6', 150), ('E6', 150)]
    INFO = [('C6', 8)]
    ATTENTION = [ ('G5', 600) ]
    WARNING = [('F5', 100), ('G5', 100), ('A5', 100), ('F6', 100)]
    DEBUG = [('E6', 150), ('D4', 500)]
    ERROR = [ ('C7', 1000) ]
    LONG_ERROR = [('C7', 50), ('C7', 250)]
    CRITICAL = [('G5', 40), ('C7', 100)]
    BELL = [('G6', 200), ('C7', 200), ('E7', 200)]

class BeepHandler:
    """
    Класс обработчика звуковых сигналов для логгера.

    :param emit: Метод для генерации звукового сигнала на основе записи лога.
    :param beep: Метод для генерации звукового сигнала.
    """
    def emit(self, record):
        """
        Генерирует звуковой сигнал на основе записи лога.

        :param record: Запись лога.
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

    def beep(self, level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000):
        """
        Генерирует звуковой сигнал.

        :param level: Уровень сигнала или строка, представляющая уровень.
        :param frequency: Частота сигнала.
        :param duration: Длительность сигнала.
        """
        Beeper.beep(level, frequency, duration)

# ------------------------------------------------------------------------------------------------

def silent_mode(func):
    """
    Декоратор для управления режимом "беззвучия".

    Этот декоратор отключает выполнение декорируемой функции, если включен беззвучный режим.

    :param func: Функция для декорирования.

    :return: Обернутая функция, добавляющая проверку режима "беззвучия".
    """
    def wrapper(*args, **kwargs):
        """
        Внутренняя функция-обертка для проверки режима "беззвучия" перед выполнением функции.

        Если режим "беззвучия" включен, функция выводит сообщение в консоль и возвращает `None`.
        В противном случае выполняется оригинальная функция.

        :param args: Позиционные аргументы, переданные в оборачиваемую функцию.
        :param kwargs: Именованные аргументы, переданные в оборачиваемую функцию.

        :return: Результат выполнения оборачиваемой функции или `None`, если режим "беззвучия" включен.
        """
        if Beeper.silent:
            print("Silent mode is enabled. Skipping beep.")
            return
        return func(*args, **kwargs)
    return wrapper


class Beeper():
    """
    Класс для управления звуковыми сигналами.

    :param silent: Флаг, определяющий, включен ли беззвучный режим.
    :param beep: Метод для воспроизведения звукового сигнала.
    """

    silent = False

    @staticmethod
    @silent_mode
    async def beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000) -> None:
        """
        Воспроизводит звуковой сигнал.

        Даёт возможность на слух определить, что происходит в системе.

        :param level: Тип события: `info`, `attention`, `warning`, `debug`, `error`, `long_error`, `critical`, `bell`
                     или `BeepLevel.SUCCESS`, `BeepLevel.INFO`, `BeepLevel.ATTENTION`, `BeepLevel.WARNING`,
                     `BeepLevel.DEBUG`, `BeepLevel.ERROR`, `BeepLevel.LONG_ERROR`, `BeepLevel.CRITICAL`, `BeepLevel.BELL`.
        :param frequency: Частота сигнала в диапазоне от 37 до 32000.
        :param duration: Длительность сигнала.
        """
        melody = None

        if isinstance(level, str):
            if level == 'success':
                melody = BeepLevel.SUCCESS.value
            elif level == 'info':
                melody = BeepLevel.INFO.value
            elif level == 'info_long':
                 melody = BeepLevel.INFO_LONG.value
            elif level == 'attention':
                melody = BeepLevel.ATTENTION.value
            elif level == 'warning':
                melody = BeepLevel.WARNING.value
            elif level == 'debug':
                melody = BeepLevel.DEBUG.value
            elif level == 'error':
                melody = BeepLevel.ERROR.value
            elif level == 'long_error':
                melody = BeepLevel.LONG_ERROR.value
            elif level == 'critical':
                melody = BeepLevel.CRITICAL.value
            elif level == 'bell':
                melody = BeepLevel.BELL.value
        elif isinstance(level, BeepLevel):
            melody = level.value

        if not melody:
            logger.error(f'Неизвестный уровень сигнала: {level}')
            return

        for note, duration in melody:
            frequency = note_freq[note]
            try:
                winsound.Beep(int(frequency), duration)
            except Exception as ex:
                logger.error(f'''Не бибикает :|
                              Ошибка - {ex},
                              нота - {note},
                              продолжительность - {duration}
                              мелодия - {melody}
                    ''')
                return
            time.sleep(0.0)
```