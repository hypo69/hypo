# Анализ кода модуля beeper.py

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, используется класс `Beeper` для управления звуковыми сигналами.
    - Применяется `Enum` для определения уровней событий, что улучшает читаемость кода.
    - Используется декоратор `silent_mode` для управления режимом беззвучия.
    - Присутствуют docstring для функций и классов, хоть и требуют доработки в стиле RST.

- Минусы
    -  Используется `print` для логирования ошибок в блоках `try-except`, что не соответствует рекомендациям использовать `logger.error`.
    -  Не все docstring оформлены в формате reStructuredText (RST).
    -  Не хватает обработки ошибок при определении мелодии.
    -  Использование `time.sleep(0.0)` внутри цикла не имеет смысла.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить импорт `logger` из `src.logger.logger`.
2.  **Логирование**: Заменить `print` на `logger.error` для логирования ошибок.
3.  **RST Docstrings**: Переписать все docstring в формате reStructuredText (RST).
4.  **Обработка ошибок**: Улучшить обработку ошибок при выборе мелодии.
5.  **Удаление `time.sleep(0.0)`**: Удалить бессмысленный `time.sleep(0.0)`.
6.  **Оформление кода**: Привести в порядок форматирование кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для генерации звуковых сигналов.
=========================================================================================

Этот модуль содержит классы и функции для воспроизведения звуковых сигналов
различных уровней важности.

Используется для уведомления пользователя о различных событиях в системе.

Пример использования
--------------------

Пример использования класса `Beeper`:

.. code-block:: python

    from src.logger.beeper import Beeper, BeepLevel
    import asyncio

    async def main():
        await Beeper.beep(BeepLevel.SUCCESS)
        await Beeper.beep(BeepLevel.ERROR)

    if __name__ == "__main__":
        asyncio.run(main())
"""



import asyncio
import winsound
import time
from enum import Enum
from typing import Union
from src.logger.logger import logger  # импортируем logger


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
    """
    Перечисление уровней событий для звуковых сигналов.

    Каждому уровню соответствуют определенные мелодии.

    :ivar SUCCESS: Успешное завершение операции.
    :vartype SUCCESS: list
    :ivar INFO: Информационное сообщение.
    :vartype INFO: list
    :ivar INFO_LONG: Длинное информационное сообщение.
    :vartype INFO_LONG: list
    :ivar ATTENTION: Привлечение внимания.
    :vartype ATTENTION: list
    :ivar WARNING: Предупреждение.
    :vartype WARNING: list
    :ivar DEBUG: Отладочное сообщение.
    :vartype DEBUG: list
    :ivar ERROR: Ошибка.
    :vartype ERROR: list
    :ivar LONG_ERROR: Длинная ошибка.
    :vartype LONG_ERROR: list
    :ivar CRITICAL: Критическая ошибка.
    :vartype CRITICAL: list
    :ivar BELL: Звонок.
    :vartype BELL: list
    """
    SUCCESS = [('D5', 100), ('A5', 100), ('D6', 100)]
    # INFO = [('C6', 150), ('E6', 150), ('G6', 150), ('C7', 150)],
    INFO_LONG = [('C6', 150), ('E6', 150)],
    INFO = [('C6', 8)],
    # ATTENTION = [('G5', 120), ('F5', 120), ('E5', 120), ('D5', 120), ('C5', 120)],
    ATTENTION = [('G5', 600)],
    WARNING = [('F5', 100), ('G5', 100), ('A5', 100), ('F6', 100)],
    DEBUG = [('E6', 150), ('D4', 500)],
    # ERROR = [('G5', 40), ('C7', 100)],
    ERROR = [('C7', 1000)],
    LONG_ERROR = [('C7', 50), ('C7', 250)],
    CRITICAL = [('G5', 40), ('C7', 100)],
    BELL = [('G6', 200), ('C7', 200), ('E7', 200)],
...

class BeepHandler:
    """
    Обработчик звуковых сигналов для логгера.

    Используется для воспроизведения звуков в зависимости от уровня логгирования.
    """
    def emit(self, record):
        """
        Воспроизводит звук на основе уровня логгирования.

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
            logger.error(f'Ошибка воспроизведения звука: {ex}') # логируем ошибку

    def beep(self, level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000):
        """
        Вызывает метод beep класса Beeper.

        :param level: Уровень сигнала (BeepLevel или строка).
        :param frequency: Частота сигнала.
        :param duration: Длительность сигнала.
        """
        Beeper.beep(level, frequency, duration)

...

# ------------------------------------------------------------------------------------------------


def silent_mode(func):
    """
    Декоратор для управления режимом беззвучия.

    Если режим беззвучия включен, функция не будет воспроизводить звук.

    :param func: Функция, которую нужно обернуть.
    :return: Обернутая функция.
    """
    def wrapper(*args, **kwargs):
        """
        Обертка для проверки режима беззвучия.

        :param args: Позиционные аргументы.
        :param kwargs: Именованные аргументы.
        :return: Результат выполнения функции или None, если режим беззвучия включен.
        """
        if Beeper.silent:
            print("Silent mode is enabled. Skipping beep.")
            return
        return func(*args, **kwargs)
    return wrapper
...

class Beeper():
    """
    Класс для управления звуковыми сигналами.

    Содержит методы для воспроизведения звуковых сигналов.
    """
    silent = False

    @staticmethod
    @silent_mode
    async def beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000) -> None:
        """
        Воспроизводит звуковой сигнал.

        :param level: Уровень сигнала (BeepLevel или строка).
        :param frequency: Частота сигнала.
        :param duration: Длительность сигнала.
        """
        melody = None # Инициализация переменной melody
        if isinstance(level, str):
            try:
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
               else:
                   logger.error(f'Неизвестный уровень сигнала: {level}') # логируем ошибку
                   return
            except Exception as ex:
                logger.error(f'Ошибка при выборе мелодии: {ex}')  # логируем ошибку
                return
        elif isinstance(level, BeepLevel):
            melody = level.value
        
        if melody is None:
            logger.error(f'Не удалось определить мелодию для уровня: {level}') # логируем ошибку
            return

        for note, duration in melody:
            try:
                frequency = note_freq[note]
                winsound.Beep(int(frequency), duration)
            except Exception as ex:
                logger.error(f'Не удалось воспроизвести звук: {ex}, нота: {note}, продолжительность: {duration}, мелодия: {melody}')  # логируем ошибку
                return
            # time.sleep(0.0) # удалили неиспользуемый sleep
...
```