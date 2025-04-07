# Модуль `magenta.py`

## Обзор

Модуль предоставляет интеграцию с Google generative AI для создания музыки с использованием Magenta. Он включает класс `MagentaMusic`, который позволяет генерировать мелодии, добавлять аккорды и барабаны, устанавливать темп и сохранять готовую композицию в MIDI-файл.

## Подробней

Модуль предназначен для автоматической генерации музыки с использованием различных моделей машинного обучения. Он предоставляет удобный интерфейс для настройки параметров генерации и сохранения результатов. Класс `MagentaMusic` инкапсулирует все необходимые шаги для создания музыкальной композиции, начиная с загрузки затравки и заканчивая сохранением MIDI-файла.

## Классы

### `MagentaMusic`

**Описание**: Класс для генерации музыки с использованием Magenta.

**Принцип работы**:

1.  Инициализация класса с заданными параметрами, такими как выходная директория, имя модели, температура, количество шагов, MIDI-файл затравки и темп.
2.  Загрузка MIDI-файла затравки или создание пустой NoteSequence, если файл не найден.
3.  Генерация мелодии с использованием модели `melody_rnn_sequence_generator`.
4.  Добавление аккордов к мелодии.
5.  Добавление барабанов к мелодии.
6.  Установка темпа для музыкальной последовательности.
7.  Сохранение готовой композиции в MIDI-файл.

**Аттрибуты**:

*   `output_dir` (str): Директория для сохранения сгенерированной музыки.
*   `model_name` (str): Имя используемой модели.
*   `temperature` (float): Параметр температуры для генерации мелодии.
*   `num_steps` (int): Количество шагов для генерации мелодии.
*   `primer_midi_file` (str): Путь к MIDI-файлу затравки.
*   `tempo` (int): Темп композиции.
*   `melody_rnn` (melody_rnn_sequence_generator.MelodyRnnSequenceGenerator): Объект для генерации мелодии.
*   `primer_sequence` (mm.NoteSequence): Загруженная затравка.

**Методы**:

*   `__init__`: Инициализирует класс `MagentaMusic` с заданными параметрами.
*   `_load_primer_sequence`: Загружает MIDI-файл затравки или создаёт пустую NoteSequence, если файл не найден.
*   `generate_melody`: Генерирует мелодию с заданными параметрами.
*   `add_chords`: Добавляет аккорды к мелодии.
*   `add_drums`: Добавляет барабаны к мелодии.
*   `set_tempo`: Устанавливает темп.
*   `save_midi`: Сохраняет готовую композицию в MIDI-файл.
*   `generate_full_music`: Объединяет все шаги в один вызов для удобства.

## Функции

### `_load_primer_sequence`

```python
    def _load_primer_sequence(self) -> mm.NoteSequence:
        """Загружает MIDI-файл затравки или создаёт пустую NoteSequence, если файл не найден.

        Args:
            self: Экземпляр класса MagentaMusic.

        Returns:
            mm.NoteSequence: Загруженная затравка или пустая NoteSequence.
        """
        ...
```

**Назначение**: Загружает MIDI-файл затравки или создает пустую мелодию, если файл не найден.

**Параметры**:

*   `self`: Экземпляр класса `MagentaMusic`.

**Возвращает**:

*   `mm.NoteSequence`: Загруженная затравка или пустая NoteSequence.

**Как работает функция**:

1.  Проверяет наличие файла затравки (`self.primer_midi_file`).
2.  Если файл существует, загружает его и преобразует в объект `mm.NoteSequence`.
3.  Если файл не найден, создает пустую `mm.NoteSequence`.
4.  Возвращает загруженную или созданную последовательность.

**Примеры**:

```python
music_generator = MagentaMusic(output_dir='my_music', primer_midi_file='primer.mid')
primer_sequence = music_generator._load_primer_sequence()
```

### `generate_melody`

```python
    def generate_melody(self) -> mm.NoteSequence:
        """Генерирует мелодию с заданными параметрами.

        Args:
            self: Экземпляр класса MagentaMusic.

        Returns:
            mm.NoteSequence: Сгенерированная мелодия.
        """
        ...
```

**Назначение**: Генерирует мелодию с использованием модели `melody_rnn_sequence_generator`.

**Параметры**:

*   `self`: Экземпляр класса `MagentaMusic`.

**Возвращает**:

*   `mm.NoteSequence`: Сгенерированная мелодия.

**Как работает функция**:

1.  Вызывает метод `generate` объекта `self.melody_rnn` с заданными параметрами (`temperature`, `steps`, `primer_sequence`).
2.  Возвращает сгенерированную мелодию в виде объекта `mm.NoteSequence`.

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
```

### `add_chords`

```python
    def add_chords(self, melody_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """Добавляет аккорды к мелодии.

        Args:
            melody_sequence (mm.NoteSequence): Мелодия, к которой нужно добавить аккорды.

        Returns:
            mm.NoteSequence: Мелодия с добавленными аккордами.
        """
        ...
```

**Назначение**: Добавляет аккорды к заданной мелодии.

**Параметры**:

*   `melody_sequence` (mm.NoteSequence): Мелодия, к которой нужно добавить аккорды.

**Возвращает**:

*   `mm.NoteSequence`: Мелодия с добавленными аккордами.

**Как работает функция**:

1.  Определяет последовательность аккордов.
2.  Создает объект `mm.ChordSequence` на основе этой последовательности.
3.  Объединяет мелодию и аккорды с использованием `mm.sequences_lib.concatenate_sequences`.
4.  Возвращает объединенную последовательность.

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
melody_with_chords = music_generator.add_chords(melody)
```

### `add_drums`

```python
    def add_drums(self, melody_with_chords_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """Добавляет барабаны к мелодии с аккордами.

        Args:
            melody_with_chords_sequence (mm.NoteSequence): Мелодия с аккордами, к которой нужно добавить барабаны.

        Returns:
            mm.NoteSequence: Мелодия с аккордами и барабанами.
        """
        ...
```

**Назначение**: Добавляет барабаны к заданной мелодии с аккордами.

**Параметры**:

*   `melody_with_chords_sequence` (mm.NoteSequence): Мелодия с аккордами, к которой нужно добавить барабаны.

**Возвращает**:

*   `mm.NoteSequence`: Мелодия с аккордами и барабанами.

**Как работает функция**:

1.  Определяет паттерн барабанов.
2.  Создает объект `mm.DrumTrack` на основе этого паттерна.
3.  Объединяет мелодию с аккордами и барабаны с использованием `mm.sequences_lib.concatenate_sequences`.
4.  Возвращает объединенную последовательность.

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
melody_with_chords = music_generator.add_chords(melody)
music_sequence = music_generator.add_drums(melody_with_chords)
```

### `set_tempo`

```python
    def set_tempo(self, music_sequence: mm.NoteSequence) -> mm.NoteSequence:
        """Устанавливает темп для музыкальной последовательности.

        Args:
            music_sequence (mm.NoteSequence): Музыкальная последовательность, для которой нужно установить темп.

        Returns:
            mm.NoteSequence: Музыкальная последовательность с установленным темпом.
        """
        ...
```

**Назначение**: Устанавливает темп для заданной музыкальной последовательности.

**Параметры**:

*   `music_sequence` (mm.NoteSequence): Музыкальная последовательность, для которой нужно установить темп.

**Возвращает**:

*   `mm.NoteSequence`: Музыкальная последовательность с установленным темпом.

**Как работает функция**:

1.  Устанавливает значение `qpm` (количество четвертных нот в минуту) в первом элементе списка `music_sequence.tempos` равным `self.tempo`.
2.  Возвращает музыкальную последовательность с установленным темпом.

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
melody_with_chords = music_generator.add_chords(melody)
music_sequence = music_generator.add_drums(melody_with_chords)
music_sequence = music_generator.set_tempo(music_sequence)
```

### `save_midi`

```python
    def save_midi(self, music_sequence: mm.NoteSequence, filename: str = 'full_music_advanced.mid') -> None:
        """Сохраняет готовую композицию в MIDI-файл.

        Args:
            music_sequence (mm.NoteSequence): Музыкальная последовательность для сохранения.
            filename (str, optional): Имя файла для сохранения. По умолчанию 'full_music_advanced.mid'.
        """
        ...
```

**Назначение**: Сохраняет музыкальную последовательность в MIDI-файл.

**Параметры**:

*   `music_sequence` (mm.NoteSequence): Музыкальная последовательность для сохранения.
*   `filename` (str, optional): Имя файла для сохранения. По умолчанию `'full_music_advanced.mid'`.

**Как работает функция**:

1.  Формирует полный путь к файлу, объединяя `self.output_dir` и `filename`.
2.  Сохраняет музыкальную последовательность в MIDI-файл с использованием `mm.sequence_proto_to_midi_file`.

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
melody_with_chords = music_generator.add_chords(melody)
music_sequence = music_generator.add_drums(melody_with_chords)
music_sequence = music_generator.set_tempo(music_sequence)
music_generator.save_midi(music_sequence)
```

### `generate_full_music`

```python
    def generate_full_music(self) -> None:
        """Объединяет все шаги в один вызов для удобства.
        Генерирует мелодию, добавляет аккорды, барабаны, устанавливает темп и сохраняет готовую композицию в MIDI-файл.

        Args:
            self: Экземпляр класса MagentaMusic.
        """
        ...
```

**Назначение**: Генерирует полную музыкальную композицию, объединяя все шаги в один вызов.

**Параметры**:

*   `self`: Экземпляр класса `MagentaMusic`.

**Как работает функция**:

1.  Генерирует мелодию с использованием `self.generate_melody()`.
2.  Добавляет аккорды к мелодии с использованием `self.add_chords(melody_sequence)`.
3.  Добавляет барабаны к мелодии с аккордами с использованием `self.add_drums(melody_with_chords_sequence)`.
4.  Устанавливает темп для музыкальной последовательности с использованием `self.set_tempo(music_sequence)`.
5.  Сохраняет готовую композицию в MIDI-файл с использованием `self.save_midi(music_sequence)`.

**Примеры**:

```python
music_generator = MagentaMusic()
music_generator.generate_full_music()
```