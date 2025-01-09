# Анализ кода модуля MusicMath

**Качество кода**
    
-   **Преимущества**
    - Код хорошо структурирован и разбит на логические функции, что облегчает его понимание и использование.
    -  Функции документированы с использованием docstring, что повышает читаемость и упрощает использование модуля.
    -  Присутствует обработка крайних случаев (например, ограничение знаменателя при расчете интервальных отношений).
    -  Используются `math.pow` и `math.log2` для точных расчетов, что является хорошей практикой.
-   **Недостатки**
    - В коде не используется `src.logger.logger` для логирования ошибок, что может затруднить отладку и мониторинг.
    -  Некоторые docstring не полностью соответствуют стандарту RST (отсутствуют некоторые типы параметров, например).
    - В `print_musical_examples` используются `print` для вывода, что не является гибким решением для логгирования, а также не соответствует заданию.
    - Отсутствует обработка некорректных входных данных в функции `note_name_to_number` (исключение `ValueError` не обрабатывается).

**Рекомендации по улучшению**

1.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок и отладочной информации.
2.  **Документация:** Привести все docstring к стандарту RST, указав все типы параметров и возвращаемых значений.
3.  **Обработка ошибок:** Добавить обработку ошибок в функцию `note_name_to_number` и другие функции, где это необходимо, с использованием `logger.error`.
4.  **Гибкость вывода:** Заменить `print` на `logger.info` для вывода примеров, чтобы можно было контролировать вывод.
5.  **Типизация:** Добавить аннотации типов для параметров и возвращаемых значений функций.
6.  **Улучшение `note_name_to_number`:** Добавить проверку на корректность ввода в `note_name_to_number`, например, с помощью try-except.

**Улучшенный код**

```python
# @title Модуль MusicMath: примеры связи математики и музыки.
"""
Модуль MusicMath: примеры связи математики и музыки.
======================================================

Модуль предоставляет набор функций для исследования и демонстрации
математических концепций, лежащих в основе музыки. Он позволяет вычислять
частоты нот, интервальные отношения, длительность нот, а также анализировать
различные музыкальные параметры.

Примеры использования
---------------------

.. code-block:: python

    import music_math

    # Пример использования функции calculate_frequency
    frequency = music_math.calculate_frequency(3)  # частота C5
    print(f"Частота ноты C5: {frequency:.2f} Hz")
"""
import math
from fractions import Fraction
import re
from typing import List, Tuple, Optional, Any # исправлены импорты #
from src.logger.logger import logger # Добавлен импорт логгера #


def calculate_frequency(note_number: int, concert_a_freq: float = 440.0) -> float:
    """
    Вычисляет частоту ноты, зная её номер в хроматической гамме.

    :param note_number: Номер ноты относительно A4 (A4 = 0).
    :type note_number: int
    :param concert_a_freq: Частота ноты A4.
    :type concert_a_freq: float
    :return: Частота ноты в герцах.
    :rtype: float
    """
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
    """
    freq1 = calculate_frequency(note1_number)
    freq2 = calculate_frequency(note2_number)
    ratio = freq2 / freq1 if freq2 > freq1 else freq1 / freq2
    fraction_ratio = Fraction(ratio).limit_denominator(100)  # Limit to reasonable denominators
    return str(fraction_ratio)


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
    """
    return beat_length * beats


def calculate_note_duration(tempo: int, note_value: float) -> float:
    """
    Вычисляет длительность ноты в секундах.

    :param tempo: Темп в ударах в минуту.
    :type tempo: int
    :param note_value: Длительность ноты относительно целой ноты (1.0 = целая, 0.5 = половинная, 0.25 = четвертная и т.д.).
    :type note_value: float
    :return: Длительность ноты в секундах.
    :rtype: float
    """
    beat_duration = 60 / tempo
    return beat_duration * note_value


def calculate_rhythm_pattern(bar_length: float, note_values: List[float]) -> float:
    """
    Рассчитывает общую продолжительность ритмического паттерна в секундах.

    :param bar_length: Длительность такта в количестве целых нот.
    :type bar_length: float
    :param note_values: Список длительностей нот (относительно целой ноты).
    :type note_values: List[float]
    :return: Общая длительность ритмического паттерна в секундах.
    :rtype: float
    """
    pattern_duration = 0
    for value in note_values:
        pattern_duration += bar_length * value
    return pattern_duration


def calculate_note_number(frequency: float, concert_a_freq: float = 440.0) -> int:
    """
    Вычисляет номер ноты в хроматической гамме на основе частоты.

    :param frequency: Частота ноты в герцах.
    :type frequency: float
    :param concert_a_freq: Частота ноты A4.
    :type concert_a_freq: float
    :return: Номер ноты относительно A4 (A4 = 0).
    :rtype: int
    """
    return round(12 * math.log2(frequency / concert_a_freq))


def generate_scale_frequencies(root_note_number: int, scale_pattern: List[int], concert_a_freq: float = 440.0) -> List[float]:
    """
    Генерирует частоты нот заданной гаммы.

    :param root_note_number: Номер корневой ноты.
    :type root_note_number: int
    :param scale_pattern: Шаблон гаммы (последовательность полутонов).
    :type scale_pattern: List[int]
    :param concert_a_freq: Частота ноты A4.
    :type concert_a_freq: float
    :return: Список частот нот в гамме.
    :rtype: List[float]
    """
    frequencies = []
    current_note = root_note_number
    for interval in scale_pattern:
        frequencies.append(calculate_frequency(current_note, concert_a_freq))
        current_note += interval
    return frequencies


def calculate_tuning_deviation(target_frequency: float, actual_frequency: float) -> float:
    """
    Вычисляет отклонение частоты от целевой в процентах.

    :param target_frequency: Целевая частота.
    :type target_frequency: float
    :param actual_frequency: Фактическая частота.
    :type actual_frequency: float
    :return: Процент отклонения.
    :rtype: float
    """
    return ((actual_frequency - target_frequency) / target_frequency) * 100


def get_note_name(note_number: int) -> str:
    """
    Возвращает название ноты по её номеру в хроматической гамме.

    :param note_number: Номер ноты относительно A4 (A4 = 0).
    :type note_number: int
    :return: Название ноты (например, "A4", "C#5", "Bb3").
    :rtype: str
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    octave = (note_number // 12) + 4  # A4 является 0, поэтому добавляем 4
    note_index = note_number % 12
    return f"{notes[note_index]}{octave}"


def get_note_info_from_freq(freq: float) -> None:
    """
    Выводит информацию о ноте по её частоте.

    :param freq: Частота ноты в герцах.
    :type freq: float
    """
    note_num = calculate_note_number(freq)
    note_name = get_note_name(note_num)
    logger.info(f"Частота {freq:.2f} Hz, соответствует ноте {note_name}, номер {note_num}") # Замена print на logger.info #


def tune_instrument(target_freq: float, actual_freq: float) -> None:
    """
    Выводит информацию о том, насколько инструмент отклоняется от целевой частоты.

    :param target_freq: Целевая частота.
    :type target_freq: float
    :param actual_freq: Фактическая частота.
    :type actual_freq: float
    """
    dev = calculate_tuning_deviation(target_freq, actual_freq)
    if dev > 0:
        logger.info(f"Завышение на {dev:.2f}%. Нужно понизить") # Замена print на logger.info #
    elif dev < 0:
        logger.info(f"Занижение на {abs(dev):.2f}%. Нужно повысить") # Замена print на logger.info #
    else:
        logger.info("Идеально настроено!") # Замена print на logger.info #


def note_name_to_number(note_name: str) -> Optional[int]:
    """
    Преобразует название ноты (например, "A4") в её номер относительно A4 (A4 = 0).

    :param note_name: Название ноты (например, "A4", "C#5", "Bb3").
    :type note_name: str
    :return: Номер ноты относительно A4 (A4 = 0), или None, если ввод некорректен.
    :rtype: Optional[int]
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    match = re.match(r"([A-Ga-g]#?)(-?\d+)", note_name)
    if not match:
        logger.error(f"Некорректный ввод ноты: {note_name}") # Логирование ошибки ввода #
        return None
    note = match.group(1).upper()
    octave = int(match.group(2))

    try:
        note_index = notes.index(note)
    except ValueError as e: # Добавлена обработка исключения
        logger.error(f"Некорректное название ноты: {note}, ошибка: {e}") # Логирование ошибки #
        return None

    return (octave - 4) * 12 + note_index


def find_nearest_notes(frequency: float, concert_a_freq: float = 440.0) -> Tuple[str, str]:
    """
    Находит две ближайшие ноты (сверху и снизу) к заданной частоте.

    :param frequency: Частота ноты в герцах.
    :type frequency: float
    :param concert_a_freq: Частота ноты A4.
    :type concert_a_freq: float
    :return: кортеж (имя нижней ноты, имя верхней ноты).
    :rtype: Tuple[str, str]
    """
    note_number = 12 * math.log2(frequency / concert_a_freq)
    lower_note_num = math.floor(note_number)
    upper_note_num = math.ceil(note_number)

    lower_note_name = get_note_name(lower_note_num)
    upper_note_name = get_note_name(upper_note_num)
    return lower_note_name, upper_note_name


def print_musical_examples() -> None:
    """
    Выводит примеры использования функций.
    """
    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("Примеры вычисления частот нот:") # Замена print на logger.info #
    logger.info(f"Частота ноты A4: {calculate_frequency(0):.2f} Hz") # Замена print на logger.info #
    logger.info(f"Частота ноты C5: {calculate_frequency(3):.2f} Hz")  # C5 на 3 полутона выше A4 # Замена print на logger.info #
    logger.info(f"Частота ноты A3: {calculate_frequency(-12):.2f} Hz")  # A3 на 12 полутона ниже A4 # Замена print на logger.info #
    logger.info("---------------------------------------------------------")  # Замена print на logger.info #
    logger.info("Примеры вычисления интервалов:")  # Замена print на logger.info #
    logger.info(f"Отношение частот между A4 и C5: {calculate_interval_ratio(0, 3)}") # Замена print на logger.info #
    logger.info(f"Отношение частот между A4 и A5: {calculate_interval_ratio(0, 12)}") # Замена print на logger.info #
    logger.info(f"Отношение частот между C4 и G4: {calculate_interval_ratio(-9, -2)}") # Замена print на logger.info #
    logger.info("---------------------------------------------------------")  # Замена print на logger.info #
    logger.info("Примеры расчета длительности нот:")  # Замена print на logger.info #
    logger.info(f"Длительность четвертной ноты при темпе 120 BPM: {calculate_note_duration(120, 0.25):.3f} сек.") # Замена print на logger.info #
    logger.info(f"Длительность половинной ноты при темпе 60 BPM: {calculate_note_duration(60, 0.5):.3f} сек.") # Замена print на logger.info #
    logger.info(f"Длительность целой ноты при темпе 100 BPM: {calculate_note_duration(100, 1):.3f} сек.") # Замена print на logger.info #
    logger.info("---------------------------------------------------------")  # Замена print на logger.info #
    logger.info("Пример расчета общей длительности музыкального фрагмента:")  # Замена print на logger.info #
    logger.info(f"Длительность 4х тактов по 4/4 при 120BPM: {calculate_tempo_duration(120, 0.5, 16):.3f} сек") # Замена print на logger.info #
    logger.info("---------------------------------------------------------")  # Замена print на logger.info #
    logger.info("Пример расчета продолжительности ритмического паттерна:") # Замена print на logger.info #
    logger.info(f"Длительность ритма 4/4 с нотами [0.25, 0.25, 0.5]: {calculate_rhythm_pattern(1, [0.25, 0.25, 0.5]):.2f} целых нот") # Замена print на logger.info #
    logger.info(f"Длительность ритма 2/4 с нотами [0.125, 0.125, 0.25]: {calculate_rhythm_pattern(0.5, [0.125, 0.125, 0.25]):.2f} целых нот") # Замена print на logger.info #
    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("Пример определения номера ноты по частоте:")  # Замена print на logger.info #
    freq_example = 440.0
    note_number_example = calculate_note_number(freq_example)
    logger.info(f"Номер ноты для частоты {freq_example:.2f} Hz: {note_number_example} (A4=0)") # Замена print на logger.info #
    freq_example = 261.63
    note_number_example = calculate_note_number(freq_example)
    logger.info(f"Номер ноты для частоты {freq_example:.2f} Hz: {note_number_example} (C4=-9)") # Замена print на logger.info #
    logger.info("---------------------------------------------------------")  # Замена print на logger.info #

    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("Пример генерации частот гаммы:")  # Замена print на logger.info #
    major_scale = [2, 2, 1, 2, 2, 2, 1]  # Шаблон мажорной гаммы # Замена print на logger.info #
    c_major_freqs = generate_scale_frequencies(-9, major_scale)  # C4 = -9 # Замена print на logger.info #
    logger.info("Частоты нот мажорной гаммы от C4 (C, D, E, F, G, A, B):") # Замена print на logger.info #
    for freq in c_major_freqs:
        logger.info(f"{freq:.2f} Hz", end=", ")  # Замена print на logger.info #
    logger.info("\n---------------------------------------------------------") # Замена print на logger.info #

    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("Пример расчета отклонения от целевой частоты:") # Замена print на logger.info #
    target_freq = 440.0
    actual_freq = 442.0
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    logger.info(f"Отклонение {actual_freq:.2f} Hz от {target_freq:.2f} Hz: {deviation:.2f}%")  # Замена print на logger.info #
    target_freq = 261.63
    actual_freq = 260
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    logger.info(f"Отклонение {actual_freq:.2f} Hz от {target_freq:.2f} Hz: {deviation:.2f}%") # Замена print на logger.info #
    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("Пример определения информации о ноте:") # Замена print на logger.info #
    get_note_info_from_freq(440.0)
    get_note_info_from_freq(329.63)
    logger.info("---------------------------------------------------------") # Замена print на logger.info #
    logger.info("Пример использования тюнера:") # Замена print на logger.info #
    tune_instrument(440.0, 438.0)
    tune_instrument(261.63, 262.0)
    tune_instrument(440.0, 440.0)
    logger.info("---------------------------------------------------------") # Замена print на logger.info #


if __name__ == "__main__":
    print_musical_examples() #  Замена print на logger.info #
    # Примеры с вводом пользователя (вне print_musical_examples): #
    logger.info("\n--- Примеры с вводом пользователя ---")  # Замена print на logger.info #
```