# Анализ кода модуля `magenta.py`

**Качество кода**
    
    - Соответствие требованиям: 8/10
    - Плюсы:
        - Код хорошо структурирован, разбит на классы и методы, что улучшает читаемость и повторное использование.
        - Присутствует подробное описание модуля и класса в начале файла.
        - Используются осмысленные имена переменных и функций.
        - Есть пример использования в `if __name__ == '__main__':`
    - Минусы:
        - Не используется `from src.logger.logger import logger` для логирования ошибок.
        - Отсутствуют docstring для методов класса.
        - Используется `print` для вывода информации, что не является лучшей практикой для логирования.
        - Жестко заданные значения для аккордов и барабанов.
        - Отсутствуют проверки на валидность данных.
        - Не используются  `j_loads` или `j_loads_ns` из `src.utils.jjson` 
        - Комментарии не в стиле RST.
        - Отсутствует обработка ошибок с использованием `try-except` и `logger.error`.

**Рекомендации по улучшению**

1.  Импортировать `logger` из `src.logger.logger`:
    ```python
    from src.logger.logger import logger
    ```
2.  Добавить docstring к методам класса, используя формат RST.
3.  Заменить `print` на `logger.info` для вывода информационных сообщений.
4.  Добавить обработку ошибок с использованием `try-except` и `logger.error` в методах, где это необходимо.
5.  Вынести аккорды и паттерны барабанов в переменные класса для большей гибкости.
6.  Добавить валидацию данных (например, проверка типа аргументов).
7.  Добавить обработку исключений при работе с MIDI файлами.
8.  Добавить константы для magic values
9.  Переименовать `music_sequence` в `note_sequence`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для генерации музыки с использованием Magenta
=========================================================================================

Этот модуль содержит класс :class:`MagentaMusic`, который используется для генерации музыки с помощью Magenta.

Пример использования
--------------------

Пример использования класса `MagentaMusic`:

.. code-block:: python

    music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                    temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
    music_generator.generate_full_music()
"""
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
import tensorflow as tf  # Import TensorFlow
from src.logger.logger import logger # импортируем logger
from pathlib import Path
from typing import Any

# TODO добавить костанты для magic values
_DEFAULT_CHORDS = [
    "C", "G", "Am", "F",
    "Dm", "G", "C", "G",
    "C", "F", "Dm", "G",
    "Am", "G", "F", "E"
]
_DEFAULT_DRUM_PATTERN = [36, 0, 42, 0, 38, 0, 46, 0, 36, 0, 42, 0, 38, 0, 45, 0]
_STEPS_PER_BAR = 8
_STEPS_PER_QUARTER = 8

class MagentaMusic:
    """
    Класс для генерации музыки с использованием Magenta.

    Args:
        output_dir (str): Директория для сохранения сгенерированной музыки.
        model_name (str): Название модели Magenta для генерации мелодии.
        temperature (float): Температура для генерации мелодии.
        num_steps (int): Количество шагов для генерации мелодии.
        primer_midi_file (str): Путь к MIDI файлу затравки.
        tempo (int): Темп композиции.
    """
    def __init__(self, output_dir: str = 'generated_music_advanced', model_name: str = 'attention_rnn', temperature: float = 1.2,
                 num_steps: int = 256, primer_midi_file: str = 'primer.mid', tempo: int = 100):
        """
        Инициализация класса MagentaMusic.

        Args:
            output_dir (str, optional): Директория для сохранения сгенерированной музыки. Defaults to 'generated_music_advanced'.
            model_name (str, optional): Название модели Magenta для генерации мелодии. Defaults to 'attention_rnn'.
            temperature (float, optional): Температура для генерации мелодии. Defaults to 1.2.
            num_steps (int, optional): Количество шагов для генерации мелодии. Defaults to 256.
            primer_midi_file (str, optional): Путь к MIDI файлу затравки. Defaults to 'primer.mid'.
            tempo (int, optional): Темп композиции. Defaults to 100.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.model_name = model_name
        self.temperature = temperature
        self.num_steps = num_steps
        self.primer_midi_file = primer_midi_file
        self.tempo = tempo
        self.melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
            model_name=self.model_name
        )
        self.primer_sequence = self._load_primer_sequence()
        self.chords = _DEFAULT_CHORDS
        self.drum_pattern = _DEFAULT_DRUM_PATTERN
        self.steps_per_bar = _STEPS_PER_BAR
        self.steps_per_quarter = _STEPS_PER_QUARTER


    def _load_primer_sequence(self) -> mm.NoteSequence:
        """
        Загружает MIDI-файл затравки или создает пустую NoteSequence, если файл не найден.

        Returns:
            mm.NoteSequence: NoteSequence, загруженная из файла или пустая.
        """
        try:
            if os.path.exists(self.primer_midi_file):
                primer_sequence = mm.midi_file_to_sequence_proto(self.primer_midi_file)
                logger.info(f"Используем primer из {self.primer_midi_file}")
                return primer_sequence
            else:
                logger.info("Не найдена primer, начинаем с пустой мелодии")
                return mm.NoteSequence(notes=[])
        except Exception as ex:
             logger.error(f'Ошибка загрузки primer файла {self.primer_midi_file}', exc_info=ex)
             return mm.NoteSequence(notes=[])

    def generate_melody(self) -> mm.NoteSequence:
        """
        Генерирует мелодию с заданными параметрами.

        Returns:
            mm.NoteSequence: Сгенерированная мелодия.
        """
        try:
            melody_sequence = self.melody_rnn.generate(
                temperature=self.temperature,
                steps=self.num_steps,
                primer_sequence=self.primer_sequence
            )
            return melody_sequence
        except Exception as ex:
             logger.error(f'Ошибка генерации мелодии', exc_info=ex)
             return mm.NoteSequence(notes=[])

    def add_chords(self, melody_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Добавляет аккорды к мелодии.

        Args:
            melody_sequence (mm.NoteSequence): Мелодия, к которой нужно добавить аккорды.

        Returns:
            mm.NoteSequence: Мелодия с аккордами.
        """
        try:
             chords = self.chords * (self.num_steps // 16)
             chord_sequence = mm.ChordSequence(chords)
             melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)
             return melody_with_chords_sequence
        except Exception as ex:
            logger.error(f'Ошибка добавления аккордов', exc_info=ex)
            return melody_sequence

    def add_drums(self, melody_with_chords_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
         Добавляет барабаны к мелодии.

         Args:
            melody_with_chords_sequence (mm.NoteSequence): Мелодия с аккордами, к которой нужно добавить барабаны.

         Returns:
            mm.NoteSequence: Мелодия с аккордами и барабанами.
        """
        try:
            drum_pattern = mm.DrumTrack(
                self.drum_pattern,
                start_step=0,
                steps_per_bar=self.num_steps // self.steps_per_bar,
                steps_per_quarter=self.steps_per_quarter,
            )
            note_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
            return note_sequence
        except Exception as ex:
            logger.error(f'Ошибка добавления барабанов', exc_info=ex)
            return melody_with_chords_sequence

    def set_tempo(self, note_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Устанавливает темп.

        Args:
            note_sequence (mm.NoteSequence): Музыкальная последовательность, для которой нужно установить темп.

        Returns:
            mm.NoteSequence: Музыкальная последовательность с установленным темпом.
        """
        try:
            note_sequence.tempos[0].qpm = self.tempo
            return note_sequence
        except Exception as ex:
            logger.error(f'Ошибка установки темпа', exc_info=ex)
            return note_sequence

    def save_midi(self, note_sequence: mm.NoteSequence, filename: str = 'full_music_advanced.mid') -> None:
        """
        Сохраняет готовую композицию в MIDI-файл.

        Args:
            note_sequence (mm.NoteSequence): Музыкальная последовательность для сохранения.
            filename (str, optional): Имя файла для сохранения. Defaults to 'full_music_advanced.mid'.
        """
        try:
            midi_file = os.path.join(self.output_dir, filename)
            mm.sequence_proto_to_midi_file(note_sequence, midi_file)
            logger.info(f"Полная композиция сгенерирована и сохранена в: {midi_file}")
        except Exception as ex:
            logger.error(f'Ошибка сохранения midi файла {filename}', exc_info=ex)


    def generate_full_music(self) -> None:
        """
         Объединяет все шаги в один вызов для удобства генерации полной композиции.
        """
        try:
            melody_sequence = self.generate_melody()
            melody_with_chords_sequence = self.add_chords(melody_sequence)
            note_sequence = self.add_drums(melody_with_chords_sequence)
            note_sequence = self.set_tempo(note_sequence)
            self.save_midi(note_sequence)
        except Exception as ex:
             logger.error(f'Ошибка генерации полной композиции', exc_info=ex)


if __name__ == '__main__':
    # Пример использования класса
    music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                    temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
    music_generator.generate_full_music()

    # Другой пример с другими параметрами
    music_generator2 = MagentaMusic(output_dir='my_music2', model_name='basic_rnn',
                                    temperature=0.9, num_steps=150, primer_midi_file='primer2.mid', tempo=120)
    music_generator2.generate_full_music()
```