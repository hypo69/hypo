"""
Модуль MusicMath: примеры связи математики и музыки.
"""
import math

def calculate_frequency(note_number, concert_a_freq=440.0):
    """
    Вычисляет частоту ноты, зная её номер в хроматической гамме.
    
    Args:
        note_number (int): Номер ноты относительно A4 (A4 = 0).
        concert_a_freq (float, optional): Частота ноты A4. Defaults to 440.0.
    
    Returns:
        float: Частота ноты в герцах.
    """
    return concert_a_freq * math.pow(2, note_number / 12)

def calculate_interval_ratio(note1_number, note2_number):
    """
    Вычисляет отношение частот между двумя нотами, зная их номера.
    
    Args:
        note1_number (int): Номер первой ноты.
        note2_number (int): Номер второй ноты.
    
    Returns:
         float: Отношение частот (частота более высокой ноты/частоту более низкой ноты)
    """
    freq1 = calculate_frequency(note1_number)
    freq2 = calculate_frequency(note2_number)
    return freq2/freq1 if freq2>freq1 else freq1/freq2

def calculate_tempo_duration(bpm, beat_length, beats):
     """
    Вычисляет общую продолжительность в секундах музыкального фрагмента.

    Args:
         bpm (int): Темп в ударах в минуту.
         beat_length(float): Продолжительность одного удара в секундах.
         beats (int): Количество ударов в музыкальном фрагменте.

    Returns:
        float: Общая продолжительность фрагмента в секундах.
    """
     return beat_length*beats

def calculate_note_duration(tempo, note_value):
    """
    Вычисляет длительность ноты в секундах.
    
    Args:
        tempo (int): Темп в ударах в минуту.
        note_value (float): Длительность ноты относительно целой ноты (1.0 = целая, 0.5 = половинная, 0.25 = четвертная и т.д.).

    Returns:
        float: Длительность ноты в секундах.
    """
    beat_duration = 60 / tempo
    return beat_duration * note_value


def calculate_rhythm_pattern(bar_length, note_values):
    """
    Рассчитывает общую продолжительность ритмического паттерна в секундах.
    
    Args:
         bar_length (float): Длительность такта в количестве целых нот.
         note_values (list): Список длительностей нот (относительно целой ноты)
    
    Returns:
         float: Общая длительность ритмического паттерна в секундах.
    """
    pattern_duration = 0
    for value in note_values:
       pattern_duration += bar_length * value
    return pattern_duration


def print_musical_examples():
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
    print(f"Отношение частот между A4 и C5: {calculate_interval_ratio(0, 3):.2f}")
    print(f"Отношение частот между A4 и A5: {calculate_interval_ratio(0, 12):.2f}")
    print(f"Отношение частот между C4 и G4: {calculate_interval_ratio(-9, -2):.2f}")
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

if __name__ == "__main__":
    print_musical_examples()