# Модуль `magenta.py`

## Обзор

Модуль `magenta.py` предоставляет интеграцию с библиотекой Magenta для генерации музыки с использованием моделей машинного обучения. Он включает класс `MagentaMusic`, который позволяет генерировать мелодии, добавлять аккорды и ударные, устанавливать темп и сохранять результаты в MIDI-файлы.

## Оглавление

1.  [Класс `MagentaMusic`](#класс-magentamusic)
    *   [Метод `__init__`](#__init__)
    *   [Метод `_load_primer_sequence`](#_load_primer_sequence)
    *   [Метод `generate_melody`](#generate_melody)
    *   [Метод `add_chords`](#add_chords)
    *   [Метод `add_drums`](#add_drums)
    *   [Метод `set_tempo`](#set_tempo)
    *   [Метод `save_midi`](#save_midi)
    *   [Метод `generate_full_music`](#generate_full_music)
2.  [Пример использования](#пример-использования)

## Класс `MagentaMusic`

### **Описание**:

Класс `MagentaMusic` инкапсулирует логику генерации музыки с использованием моделей Magenta. Он позволяет настраивать параметры генерации, загружать затравки, генерировать мелодии, добавлять аккорды и ударные, а также сохранять результаты в MIDI-файлы.

### `__init__`

**Описание**:

Конструктор класса `MagentaMusic`. Инициализирует параметры генерации музыки, создает директорию для вывода, загружает модель `MelodyRnnSequenceGenerator` и затравку.

**Параметры**:
- `output_dir` (str, optional): Директория для сохранения сгенерированных MIDI-файлов. По умолчанию `'generated_music_advanced'`.
- `model_name` (str, optional): Название используемой модели. По умолчанию `'attention_rnn'`.
- `temperature` (float, optional): Параметр температуры для генерации мелодии. По умолчанию `1.2`.
- `num_steps` (int, optional): Количество шагов для генерации мелодии. По умолчанию `256`.
- `primer_midi_file` (str, optional): Путь к MIDI-файлу затравки. По умолчанию `'primer.mid'`.
- `tempo` (int, optional): Темп композиции в ударах в минуту. По умолчанию `100`.

### `_load_primer_sequence`

**Описание**:

Загружает MIDI-файл затравки или создает пустую NoteSequence, если файл не найден.

**Возвращает**:
- `mm.NoteSequence`: Загруженная затравка или пустая NoteSequence.

### `generate_melody`

**Описание**:

Генерирует мелодию с использованием модели `melody_rnn`.

**Возвращает**:
- `mm.NoteSequence`: Сгенерированная мелодия.

### `add_chords`

**Описание**:

Добавляет аккорды к мелодии.

**Параметры**:
- `melody_sequence` (`mm.NoteSequence`): Мелодия, к которой нужно добавить аккорды.

**Возвращает**:
- `mm.NoteSequence`: Мелодия с добавленными аккордами.

### `add_drums`

**Описание**:

Добавляет барабаны к мелодии с аккордами.

**Параметры**:
- `melody_with_chords_sequence` (`mm.NoteSequence`): Мелодия с аккордами.

**Возвращает**:
- `mm.NoteSequence`: Мелодия с аккордами и ударными.

### `set_tempo`

**Описание**:

Устанавливает темп для музыкальной последовательности.

**Параметры**:
- `music_sequence` (`mm.NoteSequence`): Музыкальная последовательность.

**Возвращает**:
- `mm.NoteSequence`: Музыкальная последовательность с установленным темпом.

### `save_midi`

**Описание**:

Сохраняет музыкальную последовательность в MIDI-файл.

**Параметры**:
- `music_sequence` (`mm.NoteSequence`): Музыкальная последовательность.
- `filename` (str, optional): Имя файла для сохранения. По умолчанию `'full_music_advanced.mid'`.

### `generate_full_music`

**Описание**:

Генерирует полную музыкальную композицию, объединяя все шаги (генерация мелодии, добавление аккордов, добавление ударных, установка темпа и сохранение в MIDI-файл).

## Пример использования

```python
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
**Описание**:

В примере показано, как использовать класс `MagentaMusic` для генерации двух разных музыкальных композиций с различными параметрами. Первая композиция сохраняется в папку `my_music`, а вторая — в папку `my_music2`.