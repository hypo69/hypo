## Анализ кода модуля `magenta.py`

**Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Код разбит на логические блоки, что облегчает понимание структуры.
  - Имеется пример использования класса `MagentaMusic` в блоке `if __name__ == '__main__':`.
- **Минусы**:
  - Отсутствует подробная документация для методов и классов.
  - Не указаны типы данных для аргументов и возвращаемых значений функций.
  - Не обрабатываются возможные исключения.
  - Не используется модуль `logger` для логирования.

**Рекомендации по улучшению**:

1. **Добавить документацию**:
   - Добавить подробные docstring к классам и методам, описывающие их назначение, параметры и возвращаемые значения.
   - Использовать `Args:`, `Returns:`, `Raises:` для четкого описания параметров, возвращаемых значений и возможных исключений.

2. **Типизация данных**:
   - Добавить аннотации типов для всех аргументов и возвращаемых значений функций.

3. **Обработка исключений**:
   - Добавить блоки `try...except` для обработки возможных исключений, особенно при работе с файлами и внешними библиотеками.
   - Использовать `logger.error` для логирования ошибок с трассировкой.

4. **Логирование**:
   - Заменить `print` на `logger.info` для информационных сообщений.
   - Логировать важные этапы работы программы, такие как загрузка primer-файлов, начало и окончание генерации музыки, сохранение MIDI-файлов.

5. **Использование `j_loads` или `j_loads_ns`**:
   - В данном коде не используются JSON файлы, поэтому замена `json.load` не требуется.

6. **Соответствие PEP8**:
   - Проверить код на соответствие стандартам PEP8 и исправить все нарушения.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для работы с Magenta Music
=====================================

Модуль содержит класс :class:`MagentaMusic`, который используется для генерации музыки с использованием Magenta.

Пример использования
----------------------

>>> music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
...                                 temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
>>> music_generator.generate_full_music()
"""

import os
from pathlib import Path
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
import tensorflow as tf  # Import TensorFlow
from typing import Optional
from src.logger import logger


class MagentaMusic:
    """
    Класс для генерации музыки с использованием Magenta.
    """

    def __init__(
        self,
        output_dir: str = 'generated_music_advanced',
        model_name: str = 'attention_rnn',
        temperature: float = 1.2,
        num_steps: int = 256,
        primer_midi_file: str = 'primer.mid',
        tempo: int = 100
    ) -> None:
        """
        Инициализация класса MagentaMusic.

        Args:
            output_dir (str): Директория для сохранения сгенерированной музыки.
            model_name (str): Название модели Magenta для генерации мелодии.
            temperature (float): Параметр temperature для генерации мелодии.
            num_steps (int): Количество шагов для генерации мелодии.
            primer_midi_file (str): Путь к MIDI-файлу затравки.
            tempo (int): Темп музыки в ударах в минуту.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.model_name = model_name
        self.temperature = temperature
        self.num_steps = num_steps
        self.primer_midi_file = primer_midi_file
        self.tempo = tempo
        try:
            self.melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
                model_name=self.model_name
            )
            self.primer_sequence = self._load_primer_sequence()
        except Exception as e:
            logger.error(f'Error initializing MagentaMusic: {e}', exc_info=True)
            raise

    def _load_primer_sequence(self) -> mm.NoteSequence:
        """
        Загружает MIDI-файл затравки или создаёт пустую NoteSequence, если файл не найден.

        Returns:
            mm.NoteSequence: Объект NoteSequence, представляющий затравку.
        """
        try:
            if os.path.exists(self.primer_midi_file):
                primer_sequence = mm.midi_file_to_sequence_proto(self.primer_midi_file)
                logger.info(f"Используем primer из {self.primer_midi_file}")
                return primer_sequence
            else:
                logger.info("Не найдена primer, начинаем с пустой мелодии")
                return mm.NoteSequence(notes=[])
        except Exception as e:
            logger.error(f'Error loading primer sequence: {e}', exc_info=True)
            return mm.NoteSequence(notes=[])

    def generate_melody(self) -> mm.NoteSequence:
        """
        Генерирует мелодию с заданными параметрами.

        Returns:
            mm.NoteSequence: Объект NoteSequence, представляющий сгенерированную мелодию.
        """
        try:
            melody_sequence = self.melody_rnn.generate(
                temperature=self.temperature,
                steps=self.num_steps,
                primer_sequence=self.primer_sequence
            )
            return melody_sequence
        except Exception as e:
            logger.error(f'Error generating melody: {e}', exc_info=True)
            return mm.NoteSequence(notes=[])

    def add_chords(self, melody_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Добавляет аккорды к мелодии.

        Args:
            melody_sequence (mm.NoteSequence): Объект NoteSequence, представляющий мелодию.

        Returns:
            mm.NoteSequence: Объект NoteSequence, представляющий мелодию с аккордами.
        """
        try:
            chords = [
                'C', 'G', 'Am', 'F',
                'Dm', 'G', 'C', 'G',
                'C', 'F', 'Dm', 'G',
                'Am', 'G', 'F', 'E'
            ] * (self.num_steps // 16)

            chord_sequence = mm.ChordSequence(chords)
            melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)
            return melody_with_chords_sequence
        except Exception as e:
            logger.error(f'Error adding chords: {e}', exc_info=True)
            return melody_sequence

    def add_drums(self, melody_with_chords_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Добавляет барабаны к мелодии с аккордами.

        Args:
            melody_with_chords_sequence (mm.NoteSequence): Объект NoteSequence, представляющий мелодию с аккордами.

        Returns:
            mm.NoteSequence: Объект NoteSequence, представляющий мелодию с аккордами и барабанами.
        """
        try:
            drum_pattern = mm.DrumTrack(
                [36, 0, 42, 0, 38, 0, 46, 0, 36, 0, 42, 0, 38, 0, 45, 0],
                start_step=0,
                steps_per_bar=self.num_steps // 8,
                steps_per_quarter=8,
            )
            music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
            return music_sequence
        except Exception as e:
            logger.error(f'Error adding drums: {e}', exc_info=True)
            return melody_with_chords_sequence

    def set_tempo(self, music_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Устанавливает темп для музыкальной последовательности.

        Args:
            music_sequence (mm.NoteSequence): Объект NoteSequence, представляющий музыкальную последовательность.

        Returns:
            mm.NoteSequence: Объект NoteSequence, представляющий музыкальную последовательность с установленным темпом.
        """
        try:
            music_sequence.tempos[0].qpm = self.tempo
            return music_sequence
        except Exception as e:
            logger.error(f'Error setting tempo: {e}', exc_info=True)
            return music_sequence

    def save_midi(self, music_sequence: mm.NoteSequence, filename: str = 'full_music_advanced.mid') -> None:
        """
        Сохраняет музыкальную последовательность в MIDI-файл.

        Args:
            music_sequence (mm.NoteSequence): Объект NoteSequence, представляющий музыкальную последовательность.
            filename (str): Имя файла для сохранения MIDI.
        """
        try:
            midi_file = os.path.join(self.output_dir, filename)
            mm.sequence_proto_to_midi_file(music_sequence, midi_file)
            logger.info(f"Полная композиция сгенерирована и сохранена в: {midi_file}")
        except Exception as e:
            logger.error(f'Error saving MIDI file: {e}', exc_info=True)

    def generate_full_music(self) -> None:
        """
        Генерирует полную музыкальную композицию, объединяя все шаги.
        """
        try:
            melody_sequence = self.generate_melody()
            melody_with_chords_sequence = self.add_chords(melody_sequence)
            music_sequence = self.add_drums(melody_with_chords_sequence)
            music_sequence = self.set_tempo(music_sequence)
            self.save_midi(music_sequence)
        except Exception as e:
            logger.error(f'Error generating full music: {e}', exc_info=True)


if __name__ == '__main__':
    # Пример использования класса
    music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                    temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
    music_generator.generate_full_music()

    # Другой пример с другими параметрами
    music_generator2 = MagentaMusic(output_dir='my_music2', model_name='basic_rnn',
                                    temperature=0.9, num_steps=150, primer_midi_file='primer2.mid', tempo=120)
    music_generator2.generate_full_music()