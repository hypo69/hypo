# Анализ кода модуля `magenta`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки, что облегчает понимание и поддержку.
    - Используются осмысленные имена переменных и функций.
    - Параметры модели вынесены в конструктор, что обеспечивает гибкость настройки.
    - Присутствует документация модуля и комментарии.
- Минусы
    - Отсутствует импорт `from src.logger.logger import logger`.
    - Не все методы и переменные имеют docstring.
    - Использованы двойные кавычки в print.
    - Нет обработки исключений, например, при вызове функций `generate`, `sequence_proto_to_midi_file`.
    - Нет обработки ошибок, связанных с некорректными данными (например, пустой `primer`).

**Рекомендации по улучшению**

1.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
2.  Заменить двойные кавычки на одинарные в коде, где это требуется.
3.  Добавить docstring для каждого метода, включая аргументы, возвращаемые значения и возможные исключения.
4.  Реализовать обработку исключений в ключевых методах с использованием `try-except` и логированием ошибок через `logger.error`.
5.  Обеспечить проверку входных данных, таких как `primer_sequence`, и обработать ситуации с некорректными или отсутствующими данными.
6.  Избегать избыточного использования `print` и перейти к использованию `logger.info` или `logger.debug`.
7.  Документировать все переменные в конструкторе класса.
8.  Добавить примеры использования в docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с генерацией музыки с помощью Magenta.
=========================================================================================

Этот модуль содержит класс :class:`MagentaMusic`, который использует Magenta для генерации музыкальных композиций.
Он позволяет загружать MIDI-файлы в качестве затравки, генерировать мелодии, добавлять аккорды и ударные,
а также устанавливать темп и сохранять результат в MIDI-файл.

Пример использования
--------------------

Пример использования класса `MagentaMusic`:

.. code-block:: python

    music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                    temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
    music_generator.generate_full_music()

"""

import os
from pathlib import Path
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
import tensorflow as tf  # Import TensorFlow
from src.logger.logger import logger
from typing import Any


class MagentaMusic:
    """
    Класс для генерации музыки с использованием Magenta.

    Args:
        output_dir (str): Папка для сохранения сгенерированных MIDI файлов.
        model_name (str): Имя модели для генерации мелодии (например, 'attention_rnn' или 'basic_rnn').
        temperature (float): Параметр температуры для контроля случайности генерации.
        num_steps (int): Количество шагов для генерации мелодии.
        primer_midi_file (str): Путь к MIDI-файлу затравки.
        tempo (int): Темп композиции в ударах в минуту.
    """
    def __init__(self, output_dir: str = 'generated_music_advanced', model_name: str = 'attention_rnn', temperature: float = 1.2,
                 num_steps: int = 256, primer_midi_file: str = 'primer.mid', tempo: int = 100) -> None:
        """
        Инициализирует объект класса MagentaMusic.

        Args:
            output_dir (str): Папка для сохранения сгенерированных MIDI файлов.
            model_name (str): Имя модели для генерации мелодии (например, 'attention_rnn' или 'basic_rnn').
            temperature (float): Параметр температуры для контроля случайности генерации.
            num_steps (int): Количество шагов для генерации мелодии.
            primer_midi_file (str): Путь к MIDI-файлу затравки.
            tempo (int): Темп композиции в ударах в минуту.
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

    def _load_primer_sequence(self) -> mm.NoteSequence:
        """
        Загружает MIDI-файл затравки или создает пустую NoteSequence, если файл не найден.

        Returns:
             mm.NoteSequence: Загруженная NoteSequence или пустая NoteSequence.
        """
        if os.path.exists(self.primer_midi_file):
            try:
                primer_sequence = mm.midi_file_to_sequence_proto(self.primer_midi_file)
                logger.info(f'Используем primer из {self.primer_midi_file}')
                return primer_sequence
            except Exception as ex:
                logger.error(f'Ошибка загрузки primer из файла {self.primer_midi_file}: {ex}')
                return mm.NoteSequence(notes=[])
        else:
            logger.info('Не найдена primer, начинаем с пустой мелодии')
            return mm.NoteSequence(notes=[])

    def generate_melody(self) -> mm.NoteSequence:
        """
        Генерирует мелодию с заданными параметрами.

        Returns:
            mm.NoteSequence: Сгенерированная мелодия в виде NoteSequence.
        """
        try:
            melody_sequence = self.melody_rnn.generate(
                temperature=self.temperature,
                steps=self.num_steps,
                primer_sequence=self.primer_sequence
            )
            return melody_sequence
        except Exception as ex:
            logger.error(f'Ошибка при генерации мелодии: {ex}')
            return mm.NoteSequence(notes=[])

    def add_chords(self, melody_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Добавляет аккорды к мелодии.

        Args:
            melody_sequence (mm.NoteSequence): Мелодия, к которой нужно добавить аккорды.

        Returns:
            mm.NoteSequence: Мелодия с добавленными аккордами в виде NoteSequence.
        """
        chords = [
            'C', 'G', 'Am', 'F',
            'Dm', 'G', 'C', 'G',
            'C', 'F', 'Dm', 'G',
            'Am', 'G', 'F', 'E'
        ] * (self.num_steps // 16)

        chord_sequence = mm.ChordSequence(chords)
        melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)
        return melody_with_chords_sequence

    def add_drums(self, melody_with_chords_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Добавляет барабаны к мелодии.

        Args:
            melody_with_chords_sequence (mm.NoteSequence): Мелодия с аккордами, к которой нужно добавить барабаны.

        Returns:
            mm.NoteSequence: Мелодия с аккордами и барабанами в виде NoteSequence.
        """
        drum_pattern = mm.DrumTrack(
            [36, 0, 42, 0, 38, 0, 46, 0, 36, 0, 42, 0, 38, 0, 45, 0],
            start_step=0,
            steps_per_bar=self.num_steps // 8,
            steps_per_quarter=8,
        )
        music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
        return music_sequence

    def set_tempo(self, music_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Устанавливает темп композиции.

        Args:
            music_sequence (mm.NoteSequence): Композиция, для которой нужно установить темп.

        Returns:
            mm.NoteSequence: Композиция с установленным темпом в виде NoteSequence.
        """
        music_sequence.tempos[0].qpm = self.tempo
        return music_sequence

    def save_midi(self, music_sequence: mm.NoteSequence, filename: str = 'full_music_advanced.mid') -> None:
        """
        Сохраняет готовую композицию в MIDI-файл.

        Args:
            music_sequence (mm.NoteSequence): Композиция для сохранения.
            filename (str): Имя файла для сохранения.
        """
        midi_file = os.path.join(self.output_dir, filename)
        try:
            mm.sequence_proto_to_midi_file(music_sequence, midi_file)
            logger.info(f'Полная композиция сгенерирована и сохранена в: {midi_file}')
        except Exception as ex:
            logger.error(f'Ошибка при сохранении MIDI файла {midi_file}: {ex}')


    def generate_full_music(self) -> None:
        """
        Генерирует полную музыкальную композицию, объединяя все шаги.
        """
        melody_sequence = self.generate_melody()
        melody_with_chords_sequence = self.add_chords(melody_sequence)
        music_sequence = self.add_drums(melody_with_chords_sequence)
        music_sequence = self.set_tempo(music_sequence)
        self.save_midi(music_sequence)


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