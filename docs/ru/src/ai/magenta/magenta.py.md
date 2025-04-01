# Модуль для интеграции с Google generative AI (Magenta)

## Обзор

Модуль `magenta.py` предоставляет класс `MagentaMusic` для генерации музыки с использованием моделей Magenta от Google. Он позволяет генерировать мелодии, добавлять аккорды и барабаны, устанавливать темп и сохранять готовую композицию в MIDI-файл.

## Подробней

Этот модуль обеспечивает интеграцию с Magenta, инструментом для создания музыки с использованием машинного обучения. Он упрощает процесс создания музыкальных композиций, предоставляя удобный интерфейс для настройки параметров генерации, таких как модель, температура, количество шагов, MIDI-файл затравки и темп.

## Классы

### `MagentaMusic`

**Описание**: Класс `MagentaMusic` предназначен для генерации музыкальных композиций с использованием моделей Magenta.

**Принцип работы**:
Класс инициализируется с заданными параметрами, такими как директория вывода, название модели, температура, количество шагов, MIDI-файл затравки и темп. Он использует модель `melody_rnn_sequence_generator` из библиотеки Magenta для генерации мелодии. Затем к мелодии добавляются аккорды и барабаны. В конце устанавливается темп и сохраняется готовая композиция в MIDI-файл.

**Аттрибуты**:
- `output_dir` (str): Директория для сохранения сгенерированных MIDI-файлов. По умолчанию 'generated_music_advanced'.
- `model_name` (str): Название используемой модели. По умолчанию 'attention_rnn'.
- `temperature` (float): Параметр температуры для генерации мелодии. Влияет на случайность и креативность мелодии. По умолчанию 1.2.
- `num_steps` (int): Количество шагов для генерации мелодии. Определяет длину мелодии. По умолчанию 256.
- `primer_midi_file` (str): Путь к MIDI-файлу, используемому в качестве затравки для генерации мелодии. По умолчанию 'primer.mid'.
- `tempo` (int): Темп композиции в ударах в минуту. По умолчанию 100.
- `melody_rnn` (melody_rnn_sequence_generator.MelodyRnnSequenceGenerator): Объект генератора мелодий.
- `primer_sequence` (mm.NoteSequence): MIDI-последовательность, загруженная из файла `primer_midi_file`.

**Методы**:
- `__init__`: Инициализирует объект `MagentaMusic` с заданными параметрами.
- `_load_primer_sequence`: Загружает MIDI-файл затравки или создает пустую NoteSequence, если файл не найден.
- `generate_melody`: Генерирует мелодию с заданными параметрами.
- `add_chords`: Добавляет аккорды к мелодии.
- `add_drums`: Добавляет барабаны к мелодии.
- `set_tempo`: Устанавливает темп.
- `save_midi`: Сохраняет готовую композицию в MIDI-файл.
- `generate_full_music`: Объединяет все шаги в один вызов для удобства.

## Функции

### `_load_primer_sequence`

```python
    def _load_primer_sequence(self):
        """Загружает MIDI-файл затравки или создает пустую NoteSequence, если файл не найден.

        Args:
            self: Объект класса `MagentaMusic`.

        Returns:
            mm.NoteSequence: MIDI-последовательность, загруженная из файла `primer_midi_file` или пустая `NoteSequence`, если файл не найден.

        Как работает функция:
            1. Проверяет существование файла `primer_midi_file`.
            2. Если файл существует, загружает его в `NoteSequence` с помощью `mm.midi_file_to_sequence_proto`.
            3. Если файл не существует, создает пустую `NoteSequence`.
            4. Возвращает загруженную или пустую `NoteSequence`.

        Примеры:
            >>> music_generator = MagentaMusic(primer_midi_file='existing_primer.mid')
            Используем primer из existing_primer.mid
            >>> music_generator = MagentaMusic(primer_midi_file='non_existing_primer.mid')
            Не найдена primer, начинаем с пустой мелодии
        """
        ...
```

**Назначение**: Загружает MIDI-файл, который используется в качестве затравки, или создает пустую последовательность нот, если файл не найден.

**Параметры**:
- `self`: Ссылка на экземпляр класса `MagentaMusic`.

**Возвращает**:
- `mm.NoteSequence`: MIDI-последовательность, загруженная из файла `primer_midi_file` или пустая `NoteSequence`, если файл не найден.

**Как работает функция**:

```
Проверка существования файла затравки (primer_midi_file)
│
├───> Файл существует: Загрузка MIDI-файла в NoteSequence
│   │
│   └───> Возврат загруженной NoteSequence
│
└───> Файл не существует: Создание пустой NoteSequence
    │
    └───> Возврат пустой NoteSequence
```

**Примеры**:

```python
music_generator = MagentaMusic(primer_midi_file='existing_primer.mid')
# Используем primer из existing_primer.mid
music_generator = MagentaMusic(primer_midi_file='non_existing_primer.mid')
# Не найдена primer, начинаем с пустой мелодии
```

### `generate_melody`

```python
    def generate_melody(self):
        """Генерирует мелодию с заданными параметрами.

        Args:
            self: Объект класса `MagentaMusic`.

        Returns:
            melody_sequence: Сгенерированная мелодия.

        Как работает функция:
            1. Вызывает метод `generate` объекта `melody_rnn` для генерации мелодии.
            2. Передает параметры `temperature`, `steps` и `primer_sequence` в метод `generate`.
            3. Возвращает сгенерированную мелодию.

        Примеры:
            >>> music_generator = MagentaMusic()
            >>> melody = music_generator.generate_melody()
        """
        ...
```

**Назначение**: Генерирует мелодию с заданными параметрами.

**Параметры**:
- `self`: Ссылка на экземпляр класса `MagentaMusic`.

**Возвращает**:
- `melody_sequence`: Сгенерированная мелодия.

**Как работает функция**:

```
Вызов генератора мелодии melody_rnn.generate
│
├───> Передача параметров: temperature, steps, primer_sequence
│
└───> Возврат сгенерированной мелодии melody_sequence
```

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
```

### `add_chords`

```python
    def add_chords(self, melody_sequence):
        """Добавляет аккорды к мелодии.

        Args:
            melody_sequence: Мелодия, к которой нужно добавить аккорды.

        Returns:
            melody_with_chords_sequence: Мелодия с добавленными аккордами.

        Как работает функция:
            1. Создает список аккордов.
            2. Повторяет список аккордов нужное количество раз, чтобы он соответствовал длине мелодии.
            3. Создает объект `ChordSequence` из списка аккордов.
            4. Объединяет мелодию и последовательность аккордов с помощью `mm.sequences_lib.concatenate_sequences`.
            5. Возвращает мелодию с добавленными аккордами.

        Примеры:
            >>> music_generator = MagentaMusic()
            >>> melody = music_generator.generate_melody()
            >>> melody_with_chords = music_generator.add_chords(melody)
        """
        ...
```

**Назначение**: Добавляет аккорды к заданной мелодии.

**Параметры**:
- `melody_sequence`: Мелодия, к которой нужно добавить аккорды.

**Возвращает**:
- `melody_with_chords_sequence`: Мелодия с добавленными аккордами.

**Как работает функция**:

```
Создание списка аккордов
│
├───> Повторение списка аккордов для соответствия длине мелодии
│
├───> Создание ChordSequence из списка аккордов
│
├───> Объединение мелодии и ChordSequence
│
└───> Возврат мелодии с аккордами
```

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
melody_with_chords = music_generator.add_chords(melody)
```

### `add_drums`

```python
    def add_drums(self, melody_with_chords_sequence):
        """Добавляет барабаны к мелодии.

        Args:
            melody_with_chords_sequence: Мелодия с аккордами, к которой нужно добавить барабаны.

        Returns:
            music_sequence: Мелодия с аккордами и барабанами.

        Как работает функция:
            1. Создает объект `DrumTrack` с заданным паттерном барабанов.
            2. Объединяет мелодию с аккордами и дорожку барабанов с помощью `mm.sequences_lib.concatenate_sequences`.
            3. Возвращает мелодию с аккордами и барабанами.

        Примеры:
            >>> music_generator = MagentaMusic()
            >>> melody = music_generator.generate_melody()
            >>> melody_with_chords = music_generator.add_chords(melody)
            >>> music_sequence = music_generator.add_drums(melody_with_chords)
        """
        ...
```

**Назначение**: Добавляет барабаны к мелодии с аккордами.

**Параметры**:
- `melody_with_chords_sequence`: Мелодия с аккордами, к которой нужно добавить барабаны.

**Возвращает**:
- `music_sequence`: Мелодия с аккордами и барабанами.

**Как работает функция**:

```
Создание дорожки барабанов (DrumTrack)
│
├───> Объединение мелодии с аккордами и дорожки барабанов
│
└───> Возврат полной музыкальной последовательности
```

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
melody_with_chords = music_generator.add_chords(melody)
music_sequence = music_generator.add_drums(melody_with_chords)
```

### `set_tempo`

```python
    def set_tempo(self, music_sequence):
        """Устанавливает темп.

        Args:
            music_sequence: Музыкальная последовательность, для которой нужно установить темп.

        Returns:
            music_sequence: Музыкальная последовательность с установленным темпом.

        Как работает функция:
            1. Устанавливает темп музыкальной последовательности, изменяя значение `qpm` в `music_sequence.tempos[0]`.
            2. Возвращает музыкальную последовательность с установленным темпом.

        Примеры:
            >>> music_generator = MagentaMusic()
            >>> melody = music_generator.generate_melody()
            >>> music_sequence = music_generator.set_tempo(melody)
        """
        ...
```

**Назначение**: Устанавливает темп для музыкальной последовательности.

**Параметры**:
- `music_sequence`: Музыкальная последовательность, для которой нужно установить темп.

**Возвращает**:
- `music_sequence`: Музыкальная последовательность с установленным темпом.

**Как работает функция**:

```
Установка темпа в музыкальной последовательности (music_sequence.tempos[0].qpm)
│
└───> Возврат музыкальной последовательности с установленным темпом
```

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
music_sequence = music_generator.set_tempo(melody)
```

### `save_midi`

```python
    def save_midi(self, music_sequence, filename='full_music_advanced.mid'):
        """Сохраняет готовую композицию в MIDI-файл.

        Args:
            music_sequence: Музыкальная последовательность, которую нужно сохранить.
            filename: Имя файла для сохранения. По умолчанию 'full_music_advanced.mid'.

        Returns:
            None

        Как работает функция:
            1. Формирует путь к файлу, объединяя директорию вывода и имя файла.
            2. Сохраняет музыкальную последовательность в MIDI-файл с помощью `mm.sequence_proto_to_midi_file`.
            3. Выводит сообщение о том, куда был сохранен файл.

        Примеры:
            >>> music_generator = MagentaMusic()
            >>> melody = music_generator.generate_melody()
            >>> music_generator.save_midi(melody, filename='my_melody.mid')
            Полная композиция сгенерирована и сохранена в: generated_music_advanced/my_melody.mid
        """
        ...
```

**Назначение**: Сохраняет готовую композицию в MIDI-файл.

**Параметры**:
- `music_sequence`: Музыкальная последовательность, которую нужно сохранить.
- `filename` (str): Имя файла для сохранения. По умолчанию 'full_music_advanced.mid'.

**Возвращает**:
- `None`

**Как работает функция**:

```
Формирование пути к файлу
│
├───> Сохранение музыкальной последовательности в MIDI-файл
│
└───> Вывод сообщения о сохранении файла
```

**Примеры**:

```python
music_generator = MagentaMusic()
melody = music_generator.generate_melody()
music_generator.save_midi(melody, filename='my_melody.mid')
# Полная композиция сгенерирована и сохранена в: generated_music_advanced/my_melody.mid
```

### `generate_full_music`

```python
    def generate_full_music(self):
        """Объединяет все шаги в один вызов для удобства.

        Args:
            self: Объект класса `MagentaMusic`.

        Returns:
            None

        Как работает функция:
            1. Генерирует мелодию с помощью метода `generate_melody`.
            2. Добавляет аккорды к мелодии с помощью метода `add_chords`.
            3. Добавляет барабаны к мелодии с аккордами с помощью метода `add_drums`.
            4. Устанавливает темп с помощью метода `set_tempo`.
            5. Сохраняет готовую композицию в MIDI-файл с помощью метода `save_midi`.

        Примеры:
            >>> music_generator = MagentaMusic()
            >>> music_generator.generate_full_music()
            Полная композиция сгенерирована и сохранена в: generated_music_advanced/full_music_advanced.mid
        """
        ...
```

**Назначение**: Объединяет все шаги генерации музыки в один метод.

**Параметры**:
- `self`: Ссылка на экземпляр класса `MagentaMusic`.

**Возвращает**:
- `None`

**Как работает функция**:

```
Генерация мелодии
│
├───> Добавление аккордов к мелодии
│
├───> Добавление барабанов к мелодии с аккордами
│
├───> Установка темпа
│
└───> Сохранение готовой композиции в MIDI-файл
```

**Примеры**:

```python
music_generator = MagentaMusic()
music_generator.generate_full_music()
# Полная композиция сгенерирована и сохранена в: generated_music_advanced/full_music_advanced.mid