# Модуль magenta.py

## Обзор

Модуль `magenta.py` предназначен для интеграции с Google generative AI и создания музыкальных композиций с использованием библиотеки Magenta. Он предоставляет класс `MagentaMusic`, который позволяет генерировать мелодии, добавлять аккорды и барабаны, устанавливать темп и сохранять готовую композицию в MIDI-файл.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за создание музыки с использованием Magenta. Он использует различные AI-модели для генерации мелодий и позволяет настраивать параметры генерации, такие как температура, количество шагов и темп. Модуль также предоставляет возможность использовать MIDI-файл в качестве затравки для генерации мелодии.

## Классы

### `MagentaMusic`

**Описание**: Класс для генерации музыкальных композиций с использованием Magenta.

**Методы**:
- `__init__`: Инициализирует объект класса `MagentaMusic` с заданными параметрами.
- `_load_primer_sequence`: Загружает MIDI-файл затравки или создаёт пустую `NoteSequence`, если файл не найден.
- `generate_melody`: Генерирует мелодию с заданными параметрами.
- `add_chords`: Добавляет аккорды к мелодии.
- `add_drums`: Добавляет барабаны к мелодии.
- `set_tempo`: Устанавливает темп.
- `save_midi`: Сохраняет готовую композицию в MIDI-файл.
- `generate_full_music`: Объединяет все шаги в один вызов для удобства.

**Параметры**:
- `output_dir` (str): Директория для сохранения сгенерированных MIDI-файлов. По умолчанию `'generated_music_advanced'`.
- `model_name` (str): Название модели Magenta для генерации мелодии. По умолчанию `'attention_rnn'`.
- `temperature` (float): Параметр temperature для генерации мелодии. По умолчанию `1.2`.
- `num_steps` (int): Количество шагов для генерации мелодии. По умолчанию `256`.
- `primer_midi_file` (str): Путь к MIDI-файлу затравки. По умолчанию `'primer.mid'`.
- `tempo` (int): Темп композиции в ударах в минуту. По умолчанию `100`.

**Примеры**

```python
# Пример использования класса
music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
music_generator.generate_full_music()

# Другой пример с другими параметрами
music_generator2 = MagentaMusic(output_dir='my_music2', model_name='basic_rnn',
                                 temperature=0.9, num_steps=150, primer_midi_file='primer2.mid', tempo=120)
music_generator2.generate_full_music()
```

## Функции

### `__init__`

```python
def __init__(self, output_dir='generated_music_advanced', model_name='attention_rnn', temperature=1.2,
             num_steps=256, primer_midi_file='primer.mid', tempo=100):
    """
    Args:
        output_dir (str): Директория для сохранения сгенерированных MIDI-файлов. По умолчанию 'generated_music_advanced'.
        model_name (str): Название модели Magenta для генерации мелодии. По умолчанию 'attention_rnn'.
        temperature (float): Параметр temperature для генерации мелодии. По умолчанию 1.2.
        num_steps (int): Количество шагов для генерации мелодии. По умолчанию 256.
        primer_midi_file (str): Путь к MIDI-файлу затравки. По умолчанию 'primer.mid'.
        tempo (int): Темп композиции в ударах в минуту. По умолчанию 100.
    """
    ...
```

**Описание**: Инициализирует объект класса `MagentaMusic` с заданными параметрами.

**Параметры**:
- `output_dir` (str): Директория для сохранения сгенерированных MIDI-файлов. По умолчанию `'generated_music_advanced'`.
- `model_name` (str): Название модели Magenta для генерации мелодии. По умолчанию `'attention_rnn'`.
- `temperature` (float): Параметр temperature для генерации мелодии. По умолчанию `1.2`.
- `num_steps` (int): Количество шагов для генерации мелодии. По умолчанию `256`.
- `primer_midi_file` (str): Путь к MIDI-файлу затравки. По умолчанию `'primer.mid'`.
- `tempo` (int): Темп композиции в ударах в минуту. По умолчанию `100`.

**Примеры**:
```python
music_generator = MagentaMusic(output_dir='my_music', model_name='attention_rnn',
                                temperature=1.1, num_steps=200, primer_midi_file='primer.mid', tempo=110)
```

### `_load_primer_sequence`

```python
def _load_primer_sequence(self):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.

    Returns:
        magenta.music.NoteSequence: MIDI sequence.

    Raises:
        FileNotFoundError: Если MIDI файл не найден.
    """
    ...
```

**Описание**: Загружает MIDI-файл затравки или создаёт пустую `NoteSequence`, если файл не найден.

**Возвращает**:
- `magenta.music.NoteSequence`: MIDI sequence.

**Вызывает исключения**:
- `FileNotFoundError`: Если MIDI файл не найден.

### `generate_melody`

```python
def generate_melody(self):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.

    Returns:
        magenta.music.NoteSequence: MIDI sequence.
    """
    ...
```

**Описание**: Генерирует мелодию с заданными параметрами.

**Возвращает**:
- `magenta.music.NoteSequence`: MIDI sequence.

### `add_chords`

```python
def add_chords(self, melody_sequence):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.
        melody_sequence (magenta.music.NoteSequence): MIDI sequence.

    Returns:
        magenta.music.NoteSequence: MIDI sequence.
    """
    ...
```

**Описание**: Добавляет аккорды к мелодии.

**Параметры**:
- `melody_sequence` (magenta.music.NoteSequence): MIDI sequence.

**Возвращает**:
- `magenta.music.NoteSequence`: MIDI sequence.

### `add_drums`

```python
def add_drums(self, melody_with_chords_sequence):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.
        melody_with_chords_sequence (magenta.music.NoteSequence): MIDI sequence.

    Returns:
        magenta.music.NoteSequence: MIDI sequence.
    """
    ...
```

**Описание**: Добавляет барабаны к мелодии.

**Параметры**:
- `melody_with_chords_sequence` (magenta.music.NoteSequence): MIDI sequence.

**Возвращает**:
- `magenta.music.NoteSequence`: MIDI sequence.

### `set_tempo`

```python
def set_tempo(self, music_sequence):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.
        music_sequence (magenta.music.NoteSequence): MIDI sequence.

    Returns:
        magenta.music.NoteSequence: MIDI sequence.
    """
    ...
```

**Описание**: Устанавливает темп.

**Параметры**:
- `music_sequence` (magenta.music.NoteSequence): MIDI sequence.

**Возвращает**:
- `magenta.music.NoteSequence`: MIDI sequence.

### `save_midi`

```python
def save_midi(self, music_sequence, filename='full_music_advanced.mid'):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.
        music_sequence (magenta.music.NoteSequence): MIDI sequence.
        filename (str, optional): Имя файла для сохранения. По умолчанию 'full_music_advanced.mid'.
    """
    ...
```

**Описание**: Сохраняет готовую композицию в MIDI-файл.

**Параметры**:
- `music_sequence` (magenta.music.NoteSequence): MIDI sequence.
- `filename` (str, optional): Имя файла для сохранения. По умолчанию `'full_music_advanced.mid'`.

### `generate_full_music`

```python
def generate_full_music(self):
    """
    Args:
        self (MagentaMusic): Экземпляр класса MagentaMusic.
    """
    ...
```

**Описание**: Объединяет все шаги в один вызов для удобства.