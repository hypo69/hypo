# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module::  src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://aistudio.google.com/prompts/1WM7Hzx5RewpKpLBKUb0VlULU3XuVNsP9
   https://github.com/magenta/magenta/issues/1962
   https://colab.research.google.com/github/magenta/ddsp/blob/master/ddsp/colab/demos/timbre_transfer.ipynb#scrollTo=6wZde6CBya9k


Класс MagentaMusic:

- Все настройки вынесены в конструктор __init__, что позволяет легко создавать экземпляры класса с разными параметрами.

- Метод _load_primer_sequence загружает MIDI-файл затравки или создаёт пустую NoteSequence, если файл не найден.
- Метод generate_melody генерирует мелодию с заданными параметрами.
- Метод add_chords добавляет аккорды к мелодии.
- Метод add_drums добавляет барабаны к мелодии.
- Метод set_tempo устанавливает темп.
- Метод save_midi сохраняет готовую композицию в MIDI-файл.
- Метод generate_full_music объединяет все шаги в один вызов для удобства.

Пример использования (if __name__ == '__main__':):

Как использовать:

Создайте MIDI файлы primer.mid и primer2.mid, или оставьте их пустыми если не хотите использовать затравку.
Запустите скрипт: python magenta_music_class.py.
Сгенерированные композиции будут сохранены в папках my_music и my_music2.


"""

import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
import tensorflow as tf  # Import TensorFlow


class MagentaMusic:
    def __init__(self, output_dir='generated_music_advanced', model_name='attention_rnn', temperature=1.2,
                 num_steps=256, primer_midi_file='primer.mid', tempo=100):
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

    def _load_primer_sequence(self):
        if os.path.exists(self.primer_midi_file):
            primer_sequence = mm.midi_file_to_sequence_proto(self.primer_midi_file)
            print(f"Используем primer из {self.primer_midi_file}")
            return primer_sequence
        else:
            print("Не найдена primer, начинаем с пустой мелодии")
            return mm.NoteSequence(notes=[])


    def generate_melody(self):
        melody_sequence = self.melody_rnn.generate(
            temperature=self.temperature,
            steps=self.num_steps,
            primer_sequence=self.primer_sequence
        )
        return melody_sequence

    def add_chords(self, melody_sequence):
        chords = [
            "C", "G", "Am", "F",
            "Dm", "G", "C", "G",
            "C", "F", "Dm", "G",
            "Am", "G", "F", "E"
        ] * (self.num_steps // 16)

        chord_sequence = mm.ChordSequence(chords)
        melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)
        return melody_with_chords_sequence

    def add_drums(self, melody_with_chords_sequence):
        drum_pattern = mm.DrumTrack(
            [36, 0, 42, 0, 38, 0, 46, 0, 36, 0, 42, 0, 38, 0, 45, 0],
            start_step=0,
            steps_per_bar=self.num_steps // 8,
            steps_per_quarter=8,
        )
        music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
        return music_sequence


    def set_tempo(self, music_sequence):
        music_sequence.tempos[0].qpm = self.tempo
        return music_sequence

    def save_midi(self, music_sequence, filename='full_music_advanced.mid'):
         midi_file = os.path.join(self.output_dir, filename)
         mm.sequence_proto_to_midi_file(music_sequence, midi_file)
         print(f"Полная композиция сгенерирована и сохранена в: {midi_file}")

    def generate_full_music(self):
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