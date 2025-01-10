# Анализ кода модуля `beeper.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разделен на логические блоки.
    - Используется `Enum` для определения уровней событий, что улучшает читаемость.
    - Присутствует декоратор `silent_mode` для управления режимом "беззвучия".
    - Документация к функциям и классам в формате RST.
    - Код соответствует PEP 8 в основном.

-  Минусы
    - В коде используется стандартный `print` для логирования ошибок, следует использовать `logger.error`
    - Обработка исключений в `BeepHandler.emit` и `Beeper.beep` может быть улучшена.
    - Некоторые комментарии неполные и не дают полного представления о коде.
    - В `Beeper.beep` есть дублирование кода при выборе мелодии по строке.
    - Нет обработки случая, когда передается некорректный `level`.
    - Используется `time.sleep` вместо `asyncio.sleep`.

**Рекомендации по улучшению**
1.  **Импорты:**
    - Добавить `from src.logger.logger import logger` для логирования.
    - Уточнить импорт `Path` если используется.
2.  **Логирование ошибок:**
    - Заменить `print` на `logger.error` в блоках `except` в методах `BeepHandler.emit` и `Beeper.beep`
3.  **Обработка исключений:**
    - Улучшить обработку исключений, добавив логирование с уровнем `DEBUG`.
4.  **Улучшение `Beeper.beep`:**
    - Упростить выбор мелодии, используя словарь, где ключами будут строки, соответствующие именам `BeepLevel`.
    - Сделать обработку некорректных `level`,  выбросив исключение или используя значение по умолчанию.
5.  **Асинхронность:**
    - Заменить `time.sleep(0.0)` на `await asyncio.sleep(0.0)` для асинхронного ожидания.
6.  **Документация:**
    - Уточнить docstring для `BeepHandler.emit` и добавить пример использования.
    - Дополнить комментарии к коду.
7.  **Удаление не используемого кода:**
    - Удалить не используемые закомментированные строки кода.
8.  **Переменные:**
    - Добавить константу для значения по умолчанию `default_frequency = 400`
    - Добавить константу для значения по умолчанию `default_duration = 1000`
9.  **Форматирование кода:**
    - Исправить код в соответствии с  инструкцией по использованию одинарных кавычек.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.logger.beeper
    :platform: Windows, Unix
    :synopsis: Модуль для генерации звуковых сигналов (бипов) в приложении.

    Этот модуль предоставляет функциональность для генерации звуковых сигналов с различными уровнями важности.
    Звуковые сигналы используются для уведомления пользователя о различных событиях в системе.
    Модуль содержит классы :class:`BeepLevel`, :class:`BeepHandler` и :class:`Beeper`,
    а также декоратор :func:`silent_mode`.

    Пример использования
    --------------------

    Пример использования класса `Beeper` для воспроизведения звукового сигнала:

    .. code-block:: python

        from src.logger.beeper import Beeper, BeepLevel
        import asyncio

        async def main():
            await Beeper.beep(BeepLevel.ERROR)
            await asyncio.sleep(1)
            await Beeper.beep(level='success')
        
        if __name__ == '__main__':
            asyncio.run(main())
"""
import asyncio
import winsound
import time
from enum import Enum
from typing import Union
from src.logger.logger import logger

# Константы для значений по умолчанию
default_frequency = 400
default_duration = 1000

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
    """Класс перечислитель типов событий.

    @details Разным событиям соответствуют разные мелодии.
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
    ATTENTION = [ ('G5', 600) ]
    WARNING = [('F5', 100), ('G5', 100), ('A5', 100), ('F6', 100)]
    DEBUG = [('E6', 150), ('D4', 500)]
    ERROR = [ ('C7', 1000) ]
    LONG_ERROR = [('C7', 50), ('C7', 250)]
    CRITICAL = [('G5', 40), ('C7', 100)]
    BELL = [('G6', 200), ('C7', 200), ('E7', 200)]

class BeepHandler:
    """
    Обработчик звуковых сигналов для логгера.

    @details  Этот класс обрабатывает записи логов и воспроизводит соответствующие звуковые сигналы
    в зависимости от уровня важности события.
    """
    def emit(self, record):
        """
        Воспроизводит звук в зависимости от уровня лога.
        
        Args:
            record (dict): Запись лога, содержащая уровень события.
        
        Example:
        
        .. code-block:: python
            
            handler = BeepHandler()
            record = {"level": logging.ERROR, "msg": "Test error"}
            handler.emit(record)  # Воспроизводит звук ошибки
        
        """
        try:
            level = record['level'].name
            if level == 'ERROR':
                self.play_sound(880, 500) # Воспроизвести "бип" для ошибок
            elif level == 'WARNING':
                self.play_sound(500, 300) # Воспроизвести другой звук для предупреждений
            elif level == 'INFO':
                self.play_sound(300, 200) # И так далее...
            else:
                self.play_default_sound() # Дефолтный звук для других уровней логгирования
        except Exception as ex:
            logger.error(f'Ошибка воспроизведения звука: {ex}')

    def beep(self, level: BeepLevel | str = BeepLevel.INFO, frequency: int = default_frequency, duration: int = default_duration):
        """
        Вызывает метод beep класса Beeper.
        
        Args:
            level (BeepLevel | str): Уровень звукового сигнала или его строковое представление.
            frequency (int): Частота сигнала.
            duration (int): Длительность сигнала.
        """
        Beeper.beep(level, frequency, duration)

# ------------------------------------------------------------------------------------------------

def silent_mode(func):
    """
    Функция-декоратор для управления режимом "беззвучия".
    
    @details Принимает один аргумент - функцию, которую нужно декорировать.
    
    @param func: Функция для декорирования.
    
    @return: Обернутая функция, добавляющая проверку режима "беззвучия".
    """
    def wrapper(*args, **kwargs):
        """
        Внутренняя функция-обертка для проверки режима "беззвучия" перед выполнением функции.
        
        @details Если режим "беззвучия" включен, выводит сообщение о пропуске воспроизведения звука и завершает выполнение функции beep.
        В противном случае вызывает оригинальную функцию, переданную как аргумент (func(*args, **kwargs)).
        
        @param args: Позиционные аргументы, переданные в оборачиваемую функцию.
        @param kwargs: Именованные аргументы, переданные в оборачиваемую функцию.
        
        @return: Результат выполнения оборачиваемой функции или None, если режим "беззвучия" включен.
        """
        if Beeper.silent:
            print('Silent mode is enabled. Skipping beep.')
            return
        return func(*args, **kwargs)
    return wrapper


class Beeper():
    """Класс звуковых сигналов."""

    silent = False
    
    _level_map = {
        'success': BeepLevel.SUCCESS,
        'info': BeepLevel.INFO,
        'info_long': BeepLevel.INFO_LONG,
        'attention': BeepLevel.ATTENTION,
        'warning': BeepLevel.WARNING,
        'debug': BeepLevel.DEBUG,
        'error': BeepLevel.ERROR,
        'long_error': BeepLevel.LONG_ERROR,
        'critical': BeepLevel.CRITICAL,
        'bell': BeepLevel.BELL,
    }


    @staticmethod
    @silent_mode
    async def beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = default_frequency, duration: int = default_duration) -> None:
        """
        Звуковой сигнал оповещения.

        @details Даёт возможность на слух определить, что происходит в системе.
        @param level `BeepLevel | str`: тип события: `info`, `attention`, `warning`, `debug`, `error`, `long_error`, `critical`, `bell`
            или `Beep.SUCCESS`, `Beep.INFO`, `Beep.ATTENTION`, `Beep.WARNING`, `Beep.DEBUG`, `Beep.ERROR`, `Beep.LONG_ERROR`, `Beep.CRITICAL`, `Beep.BELL`
        @param frequency частота сигнала в значениях от 37 до 32000.
        @param duration длительность сигнала.
        """
        if isinstance(level, str):
            try:
                level = Beeper._level_map[level.lower()]
            except KeyError:
                logger.error(f'Неизвестный уровень сигнала: {level}')
                return

        if isinstance(level, BeepLevel):
             melody = level.value
        else:
             logger.error(f'Некорректный тип уровня сигнала: {type(level)}')
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
                                мелодия - {melody}''')
                return
            await asyncio.sleep(0.0)
```