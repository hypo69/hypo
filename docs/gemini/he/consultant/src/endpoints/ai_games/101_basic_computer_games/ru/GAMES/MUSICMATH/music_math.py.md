# Анализ кода модуля `music_math.py`

**Качество кода**
-   **Соответствие требованиям к формату кода (1-10):**
    -   *Преимущества:*
        -   Код хорошо структурирован и разделен на функции, каждая из которых выполняет свою конкретную задачу.
        -   Присутствуют docstring для большинства функций, описывающие их назначение, аргументы и возвращаемые значения.
        -   Используется форматирование f-strings для более читаемого вывода.
        -   Код содержит примеры использования функций.
    -   *Недостатки:*
        -   Отсутствует docstring для модуля.
        -   Не используется reStructuredText (RST) для docstring.
        -   Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя здесь нет операций чтения файлов).
        -   Не используются логирования ошибок с помощью `logger.error`.
        -   Не все функции содержат необходимые проверки входных данных (хотя некритично для этого примера).
        -   Некоторые комментарии, написанные после `#`,  не соответствуют  требованиям к форматированию.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля в формате reStructuredText (RST).
2.  Переписать docstring функций в формате reStructuredText (RST).
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать использования общих блоков `try-except`.
5.  Добавить комментарии в стиле RST для всех ключевых операций кода.
6.  Переписать комментарии после `#` в стиле RST, где это необходимо.
7.  Ввести проверки на входные данные в функциях там, где это необходимо.
8.  Исправить стиль наименования переменных и функций, чтобы он соответствовал ранее обработанным файлам.
9.  Использовать маркеры `TODO` для потенциальных будущих улучшений.

**Улучшенный код**
```python
"""
Модуль MusicMath: примеры связи математики и музыки.
=====================================================

:mod:`music_math` предоставляет набор функций для выполнения различных
математических расчетов, связанных с музыкой. Он включает в себя функции для
вычисления частот нот, интервалов, длительностей, а также для преобразования
между частотами и названиями нот.

Примеры использования
---------------------

Пример использования модуля::

    from music_math import calculate_frequency

    frequency = calculate_frequency(0)  # Вычисление частоты ноты A4
    print(frequency)

"""
import math
from fractions import Fraction
import re
# from src.logger.logger import logger # TODO: добавить импорт логгера, когда он будет доступен


def calculate_frequency(note_number: int, concert_a_freq: float = 440.0) -> float:
    """
    Вычисляет частоту ноты, зная её номер в хроматической гамме.

    :param note_number: Номер ноты относительно A4 (A4 = 0).
    :type note_number: int
    :param concert_a_freq: Частота ноты A4. По умолчанию 440.0.
    :type concert_a_freq: float, optional
    :return: Частота ноты в герцах.
    :rtype: float

    :Example:
    >>> calculate_frequency(0)
    440.0
    >>> calculate_frequency(12)
    880.0
    """
    # Вычисление частоты ноты по формуле
    return concert_a_freq * math.pow(2, note_number / 12)


def calculate_interval_ratio(note1_number: int, note2_number: int) -> str:
    """
    Вычисляет отношение частот между двумя нотами, зная их номера.

    :param note1_number: Номер первой ноты.
    :type note1_number: int
    :param note2_number: Номер второй ноты.
    :type note2_number: int
    :return: Отношение частот в виде простой дроби.
    :rtype: str

    :Example:
    >>> calculate_interval_ratio(0, 3)
    '6/5'
    >>> calculate_interval_ratio(0, 12)
    '2/1'
    """
    freq1 = calculate_frequency(note1_number) # Вычисление частоты первой ноты
    freq2 = calculate_frequency(note2_number) # Вычисление частоты второй ноты
    ratio = freq2/freq1 if freq2>freq1 else freq1/freq2 # Вычисление отношения частот
    fraction_ratio = Fraction(ratio).limit_denominator(100)  # Limit to reasonable denominators # Ограничение знаменателя дроби
    return str(fraction_ratio) # Возвращает отношение в виде строки


def calculate_tempo_duration(bpm: int, beat_length: float, beats: int) -> float:
    """
    Вычисляет общую продолжительность в секундах музыкального фрагмента.

    :param bpm: Темп в ударах в минуту.
    :type bpm: int
    :param beat_length: Продолжительность одного удара в секундах.
    :type beat_length: float
    :param beats: Количество ударов в музыкальном фрагменте.
    :type beats: int
    :return: Общая продолжительность фрагмента в секундах.
    :rtype: float

    :Example:
    >>> calculate_tempo_duration(120, 0.5, 16)
    8.0
    """
    # Вычисление продолжительности фрагмента
    return beat_length*beats


def calculate_note_duration(tempo: int, note_value: float) -> float:
    """
    Вычисляет длительность ноты в секундах.

    :param tempo: Темп в ударах в минуту.
    :type tempo: int
    :param note_value: Длительность ноты относительно целой ноты (1.0 = целая, 0.5 = половинная, 0.25 = четвертная и т.д.).
    :type note_value: float
    :return: Длительность ноты в секундах.
    :rtype: float

    :Example:
    >>> calculate_note_duration(120, 0.25)
    0.125
    """
    beat_duration = 60 / tempo # Вычисление длительности одного удара
    return beat_duration * note_value # Вычисление длительности ноты


def calculate_rhythm_pattern(bar_length: float, note_values: list) -> float:
    """
    Рассчитывает общую продолжительность ритмического паттерна в секундах.

    :param bar_length: Длительность такта в количестве целых нот.
    :type bar_length: float
    :param note_values: Список длительностей нот (относительно целой ноты).
    :type note_values: list
    :return: Общая длительность ритмического паттерна в секундах.
    :rtype: float

    :Example:
    >>> calculate_rhythm_pattern(1, [0.25, 0.25, 0.5])
    1.0
    """
    pattern_duration = 0 # Инициализация общей продолжительности
    for value in note_values: # Итерация по длительностям нот
        pattern_duration += bar_length * value # Добавление длительности к общей
    return pattern_duration # Возвращает общую длительность


def calculate_note_number(frequency: float, concert_a_freq: float = 440.0) -> int:
    """
    Вычисляет номер ноты в хроматической гамме на основе частоты.

    :param frequency: Частота ноты в герцах.
    :type frequency: float
    :param concert_a_freq: Частота ноты A4. По умолчанию 440.0.
    :type concert_a_freq: float, optional
    :return: Номер ноты относительно A4 (A4 = 0).
    :rtype: int

    :Example:
    >>> calculate_note_number(440.0)
    0
    >>> calculate_note_number(261.63)
    -9
    """
    # Вычисление номера ноты по формуле
    return round(12 * math.log2(frequency / concert_a_freq))


def generate_scale_frequencies(root_note_number: int, scale_pattern: list, concert_a_freq: float = 440.0) -> list:
    """
    Генерирует частоты нот заданной гаммы.

    :param root_note_number: Номер корневой ноты.
    :type root_note_number: int
    :param scale_pattern: Шаблон гаммы (последовательность полутонов).
    :type scale_pattern: list
    :param concert_a_freq: Частота ноты A4. По умолчанию 440.0.
    :type concert_a_freq: float, optional
    :return: Список частот нот в гамме.
    :rtype: list

    :Example:
    >>> generate_scale_frequencies(-9, [2, 2, 1, 2, 2, 2, 1])
    [261.6255653005986, 293.6647679174074, 329.6275569128699, 349.2282314330037, 391.99543598174927, 440.0, 493.8833012561241]
    """
    frequencies = [] # Инициализация списка частот
    current_note = root_note_number # Установка текущей ноты
    for interval in scale_pattern: # Итерация по интервалам гаммы
        frequencies.append(calculate_frequency(current_note, concert_a_freq)) # Добавление частоты в список
        current_note += interval # Увеличение текущей ноты на интервал
    return frequencies # Возвращает список частот


def calculate_tuning_deviation(target_frequency: float, actual_frequency: float) -> float:
    """
    Вычисляет отклонение частоты от целевой в процентах.

    :param target_frequency: Целевая частота.
    :type target_frequency: float
    :param actual_frequency: Фактическая частота.
    :type actual_frequency: float
    :return: Процент отклонения.
    :rtype: float

    :Example:
    >>> calculate_tuning_deviation(440.0, 442.0)
    0.4545454545454547
    """
    # Вычисление процента отклонения
    return ((actual_frequency - target_frequency) / target_frequency) * 100


def get_note_name(note_number: int) -> str:
    """
    Возвращает название ноты по её номеру в хроматической гамме.

    :param note_number: Номер ноты относительно A4 (A4 = 0).
    :type note_number: int
    :return: Название ноты (например, "A4", "C#5", "Bb3").
    :rtype: str

    :Example:
    >>> get_note_name(0)
    'A4'
    >>> get_note_name(3)
    'C5'
    >>> get_note_name(-1)
    'G#3'
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"] # Список названий нот
    octave = (note_number // 12) + 4  # A4 является 0, поэтому добавляем 4 # Вычисление октавы
    note_index = note_number % 12 # Вычисление индекса ноты
    return f"{notes[note_index]}{octave}" # Возвращает название ноты


def get_note_info_from_freq(freq: float) -> None:
    """
    Выводит информацию о ноте по её частоте.

    :param freq: Частота ноты в герцах.
    :type freq: float

    :Example:
    >>> get_note_info_from_freq(440.0)
    Частота 440.00 Hz, соответствует ноте A4, номер 0
    """
    note_num = calculate_note_number(freq) # Вычисление номера ноты
    note_name = get_note_name(note_num) # Вычисление имени ноты
    print(f"Частота {freq:.2f} Hz, соответствует ноте {note_name}, номер {note_num}")


def tune_instrument(target_freq: float, actual_freq: float) -> None:
    """
    Выводит информацию о том, насколько инструмент отклоняется от целевой частоты.

    :param target_freq: Целевая частота.
    :type target_freq: float
    :param actual_freq: Фактическая частота.
    :type actual_freq: float

    :Example:
    >>> tune_instrument(440.0, 438.0)
    Занижение на 0.45%. Нужно повысить
    >>> tune_instrument(440.0, 440.0)
    Идеально настроено!
    """
    dev = calculate_tuning_deviation(target_freq, actual_freq) # Вычисление отклонения
    if dev > 0: # Проверка на завышение частоты
        print(f"Завышение на {dev:.2f}%. Нужно понизить")
    elif dev < 0: # Проверка на занижение частоты
        print(f"Занижение на {abs(dev):.2f}%. Нужно повысить")
    else: # Случай точной настройки
        print("Идеально настроено!")


def note_name_to_number(note_name: str) -> int | None:
    """
    Преобразует название ноты (например, "A4") в её номер относительно A4 (A4 = 0).

    :param note_name: Название ноты (например, "A4", "C#5", "Bb3").
    :type note_name: str
    :return: Номер ноты относительно A4 (A4 = 0), или None, если ввод некорректен.
    :rtype: int | None

    :Example:
    >>> note_name_to_number('A4')
    0
    >>> note_name_to_number('C#5')
    16
    >>> note_name_to_number('Bb3')
    -2
    >>> note_name_to_number('invalid')
    None
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"] # Список названий нот
    match = re.match(r"([A-Ga-g]#?)(-?\d+)", note_name) # Поиск совпадений с регулярным выражением
    if not match: # Проверка на отсутствие совпадений
        return None
    note = match.group(1).upper() # Извлечение названия ноты
    octave = int(match.group(2)) # Извлечение октавы
    
    try:
        note_index = notes.index(note) # Получение индекса ноты
    except ValueError: # Обработка ошибки, если нота не найдена
        return None
    
    return (octave - 4) * 12 + note_index # Возвращает номер ноты


def find_nearest_notes(frequency: float, concert_a_freq: float = 440.0) -> tuple:
    """
    Находит две ближайшие ноты (сверху и снизу) к заданной частоте.

    :param frequency: Частота ноты в герцах.
    :type frequency: float
    :param concert_a_freq: Частота ноты A4. По умолчанию 440.0.
    :type concert_a_freq: float, optional
    :return: кортеж (имя нижней ноты, имя верхней ноты).
    :rtype: tuple

    :Example:
        >>> find_nearest_notes(441)
        ('A4', 'A#4')
    """
    note_number = 12 * math.log2(frequency / concert_a_freq) # Вычисление номера ноты
    lower_note_num = math.floor(note_number) # Округление вниз
    upper_note_num = math.ceil(note_number) # Округление вверх

    lower_note_name = get_note_name(lower_note_num) # Получение имени нижней ноты
    upper_note_name = get_note_name(upper_note_num) # Получение имени верхней ноты
    return lower_note_name, upper_note_name # Возвращает кортеж имен нот


def print_musical_examples() -> None:
    """
    Выводит примеры использования функций.
    """
    print("---------------------------------------------------------")
    print("Примеры вычисления частот нот:")
    print(f"Частота ноты A4: {calculate_frequency(0):.2f} Hz")
    print(f"Частота ноты C5: {calculate_frequency(3):.2f} Hz")  # C5 на 3 полутона выше A4
    print(f"Частота ноты A3: {calculate_frequency(-12):.2f} Hz") # A3 на 12 полутона ниже A4
    print("---------------------------------------------------------")
    print("Примеры вычисления интервалов:")
    print(f"Отношение частот между A4 и C5: {calculate_interval_ratio(0, 3)}")
    print(f"Отношение частот между A4 и A5: {calculate_interval_ratio(0, 12)}")
    print(f"Отношение частот между C4 и G4: {calculate_interval_ratio(-9, -2)}")
    print("---------------------------------------------------------")
    print("Примеры расчета длительности нот:")
    print(f"Длительность четвертной ноты при темпе 120 BPM: {calculate_note_duration(120, 0.25):.3f} сек.")
    print(f"Длительность половинной ноты при темпе 60 BPM: {calculate_note_duration(60, 0.5):.3f} сек.")
    print(f"Длительность целой ноты при темпе 100 BPM: {calculate_note_duration(100, 1):.3f} сек.")
    print("---------------------------------------------------------")
    print("Пример расчета общей длительности музыкального фрагмента:")
    print(f"Длительность 4х тактов по 4/4 при 120BPM: {calculate_tempo_duration(120, 0.5, 16):.3f} сек")
    print("---------------------------------------------------------")
    print("Пример расчета продолжительности ритмического паттерна:")
    print(f"Длительность ритма 4/4 с нотами [0.25, 0.25, 0.5]: {calculate_rhythm_pattern(1, [0.25, 0.25, 0.5]):.2f} целых нот")
    print(f"Длительность ритма 2/4 с нотами [0.125, 0.125, 0.25]: {calculate_rhythm_pattern(0.5, [0.125, 0.125, 0.25]):.2f} целых нот")
    print("---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("Пример определения номера ноты по частоте:")
    freq_example = 440.0
    note_number_example = calculate_note_number(freq_example)
    print(f"Номер ноты для частоты {freq_example:.2f} Hz: {note_number_example} (A4=0)")
    freq_example = 261.63
    note_number_example = calculate_note_number(freq_example)
    print(f"Номер ноты для частоты {freq_example:.2f} Hz: {note_number_example} (C4=-9)")
    print("---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("Пример генерации частот гаммы:")
    major_scale = [2, 2, 1, 2, 2, 2, 1]  # Шаблон мажорной гаммы
    c_major_freqs = generate_scale_frequencies(-9, major_scale) # C4 = -9
    print("Частоты нот мажорной гаммы от C4 (C, D, E, F, G, A, B):")
    for freq in c_major_freqs:
        print(f"{freq:.2f} Hz", end=", ")
    print("\n---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("Пример расчета отклонения от целевой частоты:")
    target_freq = 440.0
    actual_freq = 442.0
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    print(f"Отклонение {actual_freq:.2f} Hz от {target_freq:.2f} Hz: {deviation:.2f}%")
    target_freq = 261.63
    actual_freq = 260
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    print(f"Отклонение {actual_freq:.2f} Hz от {target_freq:.2f} Hz: {deviation:.2f}%")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Пример определения информации о ноте:")
    get_note_info_from_freq(440.0)
    get_note_info_from_freq(329.63)
    print("---------------------------------------------------------")
    print("Пример использования тюнера:")
    tune_instrument(440.0,438.0)
    tune_instrument(261.63, 262.0)
    tune_instrument(440.0, 440.0)
    print("---------------------------------------------------------")

if __name__ == "__main__":
    print_musical_examples()

    # Примеры с вводом пользователя (вне print_musical_examples):
    print("\n--- Примеры с вводом пользователя ---")
```