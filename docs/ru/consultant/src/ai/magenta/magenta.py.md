### Анализ кода модуля `magenta`

**Качество кода:**

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код разбит на функции, что повышает читаемость и упрощает поддержку.
    - Класс `MagentaMusic` хорошо структурирован и позволяет легко генерировать музыку с разными параметрами.
    - Использование `os.makedirs(self.output_dir, exist_ok=True)` гарантирует, что директория вывода существует.
- **Минусы**:
    - Отсутствует полноценная документация в формате RST.
    - Используется стандартный `print` для вывода, что не подходит для логгирования.
    - Есть импорт `tensorflow`, но он не используется в явном виде в представленном коде.
    - Не все функции имеют описание и типы параметров.
    - Отсутствует обработка исключений и ошибок.

**Рекомендации по улучшению:**

1.  **Документация**:
    - Добавить RST-документацию для класса `MagentaMusic` и всех его методов, включая описание параметров, возвращаемых значений и исключений.
2.  **Логирование**:
    - Заменить использование `print` на `logger.info`, `logger.warning` или `logger.error` для более гибкого управления выводом сообщений.
    - Импортировать `logger` из `src.logger`.
3.  **Импорты**:
    - Проверить необходимость импорта `tensorflow`. Если он не используется, удалить его.
4.  **Обработка ошибок**:
    - Добавить обработку исключений, используя `try-except` блоки. Выводить подробные ошибки в лог через `logger.error`.
5.  **Форматирование**:
    - Привести код к стандартам PEP8.
6.  **Унификация кавычек**:
    - Использовать одинарные кавычки (`'`) для строк, используемых в коде, и двойные кавычки (`"`) для строк вывода.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
"""
Модуль для генерации музыки с использованием Magenta.
=====================================================

Модуль содержит класс :class:`MagentaMusic`, который используется для генерации музыки с применением библиотеки Magenta.

Пример использования
----------------------
.. code-block:: python

    music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                    temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
    music_generator.generate_full_music()
"""
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from src.logger import logger  # Import logger from src.logger


class MagentaMusic:
    """
    Класс для генерации музыки с использованием Magenta.

    :param output_dir: Директория для сохранения сгенерированной музыки.
    :type output_dir: str
    :param model_name: Название модели Magenta для генерации.
    :type model_name: str
    :param temperature: Температура генерации (влияет на случайность).
    :type temperature: float
    :param num_steps: Количество шагов для генерации мелодии.
    :type num_steps: int
    :param primer_midi_file: Путь к MIDI-файлу для затравки.
    :type primer_midi_file: str
    :param tempo: Темп музыки в ударах в минуту.
    :type tempo: int
    """

    def __init__(self, output_dir='generated_music_advanced', model_name='attention_rnn', temperature=1.2,
                 num_steps=256, primer_midi_file='primer.mid', tempo=100):
        """
        Инициализирует класс MagentaMusic.
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
        Загружает MIDI-файл затравки или создает пустую NoteSequence.

        :return: Загруженная или пустая NoteSequence.
        :rtype: mm.NoteSequence
        """
        if os.path.exists(self.primer_midi_file):
            try:  # Добавляем try-except для обработки ошибок
                primer_sequence = mm.midi_file_to_sequence_proto(self.primer_midi_file)
                logger.info(f"Используем primer из {self.primer_midi_file}")  # Используем logger.info
                return primer_sequence
            except Exception as e:
                logger.error(f"Ошибка при загрузке primer файла {self.primer_midi_file}: {e}")
                return mm.NoteSequence(notes=[])  # В случае ошибки возвращаем пустую NoteSequence
        else:
            logger.info("Не найдена primer, начинаем с пустой мелодии")  # Используем logger.info
            return mm.NoteSequence(notes=[])

    def generate_melody(self) -> mm.NoteSequence:
        """
        Генерирует мелодию с заданными параметрами.

        :return: Сгенерированная NoteSequence мелодии.
        :rtype: mm.NoteSequence
        """
        try:  # Добавляем try-except для обработки ошибок
            melody_sequence = self.melody_rnn.generate(
                temperature=self.temperature,
                steps=self.num_steps,
                primer_sequence=self.primer_sequence
            )
            return melody_sequence
        except Exception as e:
            logger.error(f"Ошибка при генерации мелодии: {e}")
            return mm.NoteSequence(notes=[])  # В случае ошибки возвращаем пустую NoteSequence

    def add_chords(self, melody_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """
        Добавляет аккорды к мелодии.

        :param melody_sequence: NoteSequence мелодии.
        :type melody_sequence: mm.NoteSequence
        :return: NoteSequence мелодии с аккордами.
        :rtype: mm.NoteSequence
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
        Добавляет барабаны к мелодии с аккордами.

        :param melody_with_chords_sequence: NoteSequence мелодии с аккордами.
        :type melody_with_chords_sequence: mm.NoteSequence
        :return: NoteSequence музыки с барабанами.
        :rtype: mm.NoteSequence
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
        Устанавливает темп музыки.

        :param music_sequence: NoteSequence музыки.
        :type music_sequence: mm.NoteSequence
        :return: NoteSequence музыки с установленным темпом.
        :rtype: mm.NoteSequence
        """
        music_sequence.tempos[0].qpm = self.tempo
        return music_sequence

    def save_midi(self, music_sequence: mm.NoteSequence, filename='full_music_advanced.mid'):
        """
        Сохраняет сгенерированную музыку в MIDI-файл.

        :param music_sequence: NoteSequence музыки для сохранения.
        :type music_sequence: mm.NoteSequence
        :param filename: Имя файла для сохранения MIDI.
        :type filename: str
        """
        midi_file = os.path.join(self.output_dir, filename)
        try:  # Добавляем try-except для обработки ошибок
            mm.sequence_proto_to_midi_file(music_sequence, midi_file)
            logger.info(f"Полная композиция сгенерирована и сохранена в: {midi_file}")  # Используем logger.info
        except Exception as e:
            logger.error(f"Ошибка при сохранении MIDI файла {midi_file}: {e}")  # Используем logger.error

    def generate_full_music(self):
        """
        Генерирует полную музыкальную композицию, объединяя все шаги.
        """
        try: # Добавляем try-except для обработки ошибок
            melody_sequence = self.generate_melody()
            melody_with_chords_sequence = self.add_chords(melody_sequence)
            music_sequence = self.add_drums(melody_with_chords_sequence)
            music_sequence = self.set_tempo(music_sequence)
            self.save_midi(music_sequence)
        except Exception as e:
            logger.error(f"Ошибка при генерации полной музыки: {e}")


if __name__ == '__main__':
    # Пример использования класса
    music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                    temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
    music_generator.generate_full_music()

    # Другой пример с другими параметрами
    music_generator2 = MagentaMusic(output_dir='my_music2', model_name='basic_rnn',
                                    temperature=0.9, num_steps=150, primer_midi_file='primer2.mid', tempo=120)
    music_generator2.generate_full_music()