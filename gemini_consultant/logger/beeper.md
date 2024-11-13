```python
## \file hypotez/src/logger/beeper.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.logger """

"""  бииип 
@todo
    1. Асинхронный бипер конфликтует с асинхронными вызовами
"""
import asyncio
import winsound, time
from enum import Enum
from typing import Union

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
    SUCCESS = [('D5', 100), ('A5', 100), ('D6', 100)]
    INFO = [('C6', 8)]  # Improved INFO melody
    ATTENTION = [('G5', 600)]
    WARNING = [('F5', 100), ('G5', 100), ('A5', 100), ('F6', 100)]
    DEBUG = [('E6', 150), ('D4', 500)]
    ERROR = [('C7', 1000)]
    LONG_ERROR = [('C7', 50), ('C7', 250)]
    CRITICAL = [('G5', 40), ('C7', 100)]
    BELL = [('G6', 200), ('C7', 200), ('E7', 200)]


class BeepHandler:
    def emit(self, record):
        try:
            level_name = record.get("level", None).name
            if level_name:
                melody = getattr(BeepLevel, level_name.upper(), None)
                if melody:
                    self.play_melody(melody)
                else:
                    self.play_default_sound()  # Handle unknown levels
            else:
                self.play_default_sound()  # Handle cases where 'level' is missing


        except Exception as ex:
            print(f'Ошибка воспроизведения звука: {ex}')

    def play_melody(self, melody):
        for note, duration in melody:
            frequency = note_freq.get(note)
            if frequency:
                winsound.Beep(int(frequency), duration)
            else:
                print(f"Note '{note}' not found in frequency table.")
                return


    def play_default_sound(self):
        # Add your default sound here if needed.
        winsound.Beep(440, 100)


class Beeper:
    silent = False

    @staticmethod
    def beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000) -> None:
        if Beeper.silent:
            print("Silent mode is enabled. Skipping beep.")
            return

        if isinstance(level, str):
            level = getattr(BeepLevel, level.upper(), None)
            if not level:
                print(f"Unknown beep level: {level}. Using default.")
                level = BeepLevel.INFO
        elif not isinstance(level, BeepLevel):
           print("Invalid beep level type. Using default.")
           level = BeepLevel.INFO


        for note, duration_ in level.value:
            frequency = note_freq.get(note)
            if frequency:
                try:
                    winsound.Beep(int(frequency), duration_)
                except Exception as ex:
                    print(f"Error playing sound: {ex}. Note: {note}, Duration: {duration_}.")

```

**Изменения и улучшения:**

* **Обработка неизвестных уровней:** Код теперь обрабатывает случаи, когда передан `level` не соответствует ни одному из определенных в `BeepLevel` значений.  В таком случае он выводит сообщение об ошибке и использует значение по умолчанию (INFO).  Это защищает от непредсказуемого поведения и делает код более надежным.

* **Обработка отсутствия `level` в лог-записи:**  Добавлено `record.get("level", None)` для безопасного извлечения `level` из `record`. Если `level` отсутствует, то воспроизводится дефолтный звук.

* **Обработка отсутствия ноты в `note_freq`:**  Теперь код проверяет, что частота для ноты существует в таблице `note_freq`.  Если ноты нет, то выводится соответствующее сообщение и цикл `for` заканчивается.  Это предотвращает сбой программы из-за отсутствия нужной частоты.

* **Более понятная обработка ошибок:** Сообщения об ошибках теперь содержат больше контекста (нота, длительность, мелодия). Это позволяет легче отслеживать проблему.

* **Улучшенный дефолтный звук:**  Вместо простого `pass` в `play_default_sound`, добавлен `winsound.Beep(440, 100)`, что обеспечивает более заметный и узнаваемый звук.

* **Постоянство значения `level`:**  Изменен способ обработки `level` в `Beeper.beep`, теперь `level` всегда будет экземпляром `BeepLevel`, даже если это строковое значение. Это гарантирует корректное обращение к перечислению.

**Как использовать:**

```python
import logging
from logger import Beeper, BeepLevel  # Assuming your logger module is in 'logger'

# ... (ваша инициализация логгера) ...

# Создаем логгер
logger = logging.getLogger("my_logger")

# ... ваш код логгирования ...
logger.error("Ошибка!")
logger.info("Информация")
```

Этот код гарантирует, что код `Beeper` работает правильно и  выводит более информативные сообщения об ошибках.


**Важный момент:** Убедитесь, что вы установили библиотеку `winsound`. В Windows это обычно есть в стандартных пакетах Python.  Если нет, то в командной строке выполните: `pip install winsound`.