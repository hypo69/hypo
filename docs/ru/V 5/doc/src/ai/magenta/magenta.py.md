# Модуль magenta

## Обзор

Модуль `magenta.py` предоставляет класс `MagentaMusic` для генерации музыки с использованием моделей Magenta. Он включает в себя загрузку затравки MIDI, генерацию мелодии, добавление аккордов и барабанов, установку темпа и сохранение результата в MIDI-файл. Модуль предназначен для интеграции генеративных моделей ИИ в процесс создания музыки.

## Подробней

Этот модуль упрощает создание музыкальных композиций, комбинируя различные элементы, такие как мелодия, аккорды и ударные, с использованием моделей машинного обучения. Класс `MagentaMusic` предоставляет удобный интерфейс для управления параметрами генерации и сохранения сгенерированной музыки. Он позволяет настраивать параметры, такие как модель, температура, количество шагов, файл затравки и темп.

## Классы

### `MagentaMusic`

**Описание**: Класс для генерации музыки с использованием моделей Magenta.

**Как работает класс**:
Класс инициализируется с параметрами, определяющими процесс генерации музыки, такими как директория вывода, имя модели, температура, количество шагов, файл затравки MIDI и темп. Он загружает модель `melody_rnn` и затравку, если она существует. Методы класса позволяют генерировать мелодию, добавлять аккорды и ударные, устанавливать темп и сохранять результат в MIDI-файл.

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
- `output_dir` (str): Директория для сохранения сгенерированной музыки. По умолчанию 'generated_music_advanced'.
- `model_name` (str): Имя используемой модели Magenta. По умолчанию 'attention_rnn'.
- `temperature` (float): Параметр температуры для генерации мелодии. По умолчанию 1.2.
- `num_steps` (int): Количество шагов для генерации мелодии. По умолчанию 256.
- `primer_midi_file` (str): Путь к MIDI-файлу затравки. По умолчанию 'primer.mid'.
- `tempo` (int): Темп композиции в ударах в минуту. По умолчанию 100.

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

### `_load_primer_sequence`

```python
def _load_primer_sequence(self) -> mm.NoteSequence:
    """
    Загружает MIDI-файл затравки или создаёт пустую NoteSequence, если файл не найден.

    Args:
        self: Экземпляр класса MagentaMusic.

    Returns:
        mm.NoteSequence: Загруженная затравка или пустая NoteSequence.
    """
```

**Как работает функция**:
Функция проверяет наличие файла затравки MIDI по пути `self.primer_midi_file`. Если файл существует, он загружается и преобразуется в объект `NoteSequence`. Если файл не найден, создается пустая `NoteSequence`.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.

**Возвращает**:
- `mm.NoteSequence`: Загруженная затравка или пустая `NoteSequence`.

### `generate_melody`

```python
def generate_melody(self) -> mm.NoteSequence:
    """
    Генерирует мелодию с заданными параметрами.

    Args:
        self: Экземпляр класса MagentaMusic.

    Returns:
        mm.NoteSequence: Сгенерированная мелодия.
    """
```

**Как работает функция**:
Функция использует метод `generate` объекта `self.melody_rnn` для генерации мелодии на основе параметров `self.temperature`, `self.num_steps` и `self.primer_sequence`.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.

**Возвращает**:
- `mm.NoteSequence`: Сгенерированная мелодия.

### `add_chords`

```python
def add_chords(self, melody_sequence: mm.NoteSequence) -> mm.NoteSequence:
    """
    Добавляет аккорды к мелодии.

    Args:
        self: Экземпляр класса MagentaMusic.
        melody_sequence (mm.NoteSequence): Мелодия, к которой нужно добавить аккорды.

    Returns:
        mm.NoteSequence: Мелодия с добавленными аккордами.
    """
```

**Как работает функция**:
Функция создает последовательность аккордов на основе списка `chords` и объединяет её с предоставленной мелодией `melody_sequence`.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.
- `melody_sequence` (mm.NoteSequence): Мелодия, к которой нужно добавить аккорды.

**Возвращает**:
- `mm.NoteSequence`: Мелодия с добавленными аккордами.

### `add_drums`

```python
def add_drums(self, melody_with_chords_sequence: mm.NoteSequence) -> mm.NoteSequence:
    """
    Добавляет барабаны к мелодии.

    Args:
        self: Экземпляр класса MagentaMusic.
        melody_with_chords_sequence (mm.NoteSequence): Мелодия с аккордами, к которой нужно добавить барабаны.

    Returns:
        mm.NoteSequence: Мелодия с аккордами и барабанами.
    """
```

**Как работает функция**:
Функция создает барабанный паттерн и объединяет его с предоставленной мелодией с аккордами `melody_with_chords_sequence`.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.
- `melody_with_chords_sequence` (mm.NoteSequence): Мелодия с аккордами, к которой нужно добавить барабаны.

**Возвращает**:
- `mm.NoteSequence`: Мелодия с аккордами и барабанами.

### `set_tempo`

```python
def set_tempo(self, music_sequence: mm.NoteSequence) -> mm.NoteSequence:
    """
    Устанавливает темп.

    Args:
        self: Экземпляр класса MagentaMusic.
        music_sequence (mm.NoteSequence): Музыкальная последовательность, темп которой нужно установить.

    Returns:
        mm.NoteSequence: Музыкальная последовательность с установленным темпом.
    """
```

**Как работает функция**:
Функция устанавливает темп музыкальной последовательности `music_sequence` на значение `self.tempo`.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.
- `music_sequence` (mm.NoteSequence): Музыкальная последовательность, темп которой нужно установить.

**Возвращает**:
- `mm.NoteSequence`: Музыкальная последовательность с установленным темпом.

### `save_midi`

```python
def save_midi(self, music_sequence: mm.NoteSequence, filename: str = 'full_music_advanced.mid') -> None:
    """
    Сохраняет готовую композицию в MIDI-файл.

    Args:
        self: Экземпляр класса MagentaMusic.
        music_sequence (mm.NoteSequence): Музыкальная последовательность для сохранения.
        filename (str, optional): Имя файла для сохранения. По умолчанию 'full_music_advanced.mid'.
    """
```

**Как работает функция**:
Функция сохраняет музыкальную последовательность `music_sequence` в MIDI-файл с именем `filename` в директории `self.output_dir`.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.
- `music_sequence` (mm.NoteSequence): Музыкальная последовательность для сохранения.
- `filename` (str, optional): Имя файла для сохранения. По умолчанию 'full_music_advanced.mid'.

### `generate_full_music`

```python
def generate_full_music(self) -> None:
    """
    Объединяет все шаги в один вызов для удобства.

    Args:
        self: Экземпляр класса MagentaMusic.
    """
```

**Как работает функция**:
Функция выполняет все шаги генерации музыки: генерацию мелодии, добавление аккордов, добавление барабанов, установку темпа и сохранение результата в MIDI-файл.

**Параметры**:
- `self`: Экземпляр класса `MagentaMusic`.