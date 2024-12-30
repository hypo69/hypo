# Анализ кода модуля `melody_composer.py`

**Качество кода**
  
  - **Соответствие требованиям к формату кода (1-10):** 7/10
  - **Преимущества:**
      - Код в целом выполняет поставленную задачу по генерации музыкальных произведений.
      - Используются библиотеки `magenta`, что является ключевым для генерации музыки.
      - Код структурирован в основном логично, с разделением на этапы инициализации, генерации и сохранения.
      - Предусмотрен пользовательский ввод для жанра и темпа.
      - Есть базовая поддержка аккомпанемента (барабаны и аккорды).
  - **Недостатки:**
      - Отсутствуют docstring и комментарии в стиле reStructuredText (RST).
      - Нет обработки исключений (try-except), что может привести к непредсказуемым ошибкам.
      - Не используется `j_loads` или `j_loads_ns`.
      - Не хватает проверок ввода пользователя.
      - Не используются логирование ошибок через `logger.error`.
      - Нет обработки случая, когда введенный жанр отсутствует в словаре `chord_progressions`.

**Рекомендации по улучшению**

1.  Добавить docstring в стиле reStructuredText (RST) для модуля, функций и переменных.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Обрабатывать возможные исключения с использованием `try-except` и логировать их через `logger.error`.
4.  Использовать `j_loads` или `j_loads_ns` для чтения конфигурационных файлов (если они используются).
5.  Реализовать проверки для ввода пользователя (жанр, темп).
6.  Улучшить генерацию аккомпанемента: добавить возможность выбора стиля барабанов, разнообразить аккордовую прогрессию.
7.  Добавить комментарии к коду, поясняющие сложные моменты.
8.  Переименовать переменные и функции так, чтобы они соответствовали ранее обработанным файлам (если это необходимо).
9.  Провести рефакторинг кода для улучшения читаемости и поддерживаемости.

**Улучшенный код**
```python
"""
Модуль для генерации музыкальных композиций с использованием Magenta.
=========================================================================================

Модуль позволяет генерировать музыкальные произведения на основе модели Melody RNN.
Используется пользовательский ввод для выбора жанра и темпа, а также включает аккомпанемент из барабанов и аккордов.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.AI.MELODY_COMPOSER import melody_composer

    melody_composer.generate_music()
"""
__author__ = "avinashkranjan/Amazing-Python-Scripts"

import os # Импортируем модуль os для работы с файловой системой
import magenta.music as mm # Импортируем модуль magenta.music для работы с музыкальными данными
from magenta.models.melody_rnn import melody_rnn_sequence_generator # Импортируем модуль melody_rnn_sequence_generator из magenta для генерации мелодий
from src.logger.logger import logger  # Импортируем логгер из нашего проекта


# Устанавливаем директорию для сохранения сгенерированных MIDI файлов
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)  # Создаем директорию, если она не существует

# Инициализируем модель Melody RNN
model_name = 'attention_rnn' # Указываем имя модели
try:
    melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator( # Инициализируем генератор мелодий
        model_name=model_name)
except Exception as ex:
    logger.error('Ошибка при инициализации модели Melody RNN', ex) # Логируем ошибку при инициализации модели
    raise  # Пробрасываем исключение дальше


# Устанавливаем температуру для генерации музыки (более высокие значения приводят к большей случайности)
temperature = 1.0

# Устанавливаем количество музыкальных произведений для генерации
num_music_pieces = 3

# Устанавливаем количество шагов на музыкальное произведение
steps_per_music_piece = 128

def get_user_preferences():
    """
    Получает от пользователя предпочитаемый жанр и темп.

    :return: Кортеж (preferred_genre, preferred_tempo)
    :rtype: tuple
    """
    while True:
        try:
            preferred_genre = input(
                "Введите предпочитаемый жанр (например, classical, jazz, rock): ") # Запрашиваем жанр у пользователя
            preferred_tempo = int(input("Введите предпочитаемый темп (BPM): ")) # Запрашиваем темп у пользователя
            if preferred_tempo <= 0:
                print("Темп должен быть положительным числом.") # Проверяем корректность темпа
                continue
            return preferred_genre, preferred_tempo
        except ValueError:
            print("Неверный формат ввода. Пожалуйста, введите целое число для темпа.") # Выводим ошибку если темп не число

# Получаем пользовательские предпочтения
preferred_genre, preferred_tempo = get_user_preferences()


# Аккордовые прогрессии для выбранных жанров (можно добавить больше жанров и прогрессий)
chord_progressions = {
    "classical": ["C", "Am", "F", "G"],
    "jazz": ["Cmaj7", "Dm7", "Em7", "A7"],
    "rock": ["C", "G", "Am", "F"],
}


# Базовый паттерн барабанов для аккомпанемента
drum_pattern = mm.DrumTrack( # Создаем дорожку ударных
    # Kick drum and Hi-hat pattern (настройте при необходимости)
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=steps_per_music_piece // 4,
    steps_per_quarter=4,
)

def generate_music_piece(i: int):
    """
    Генерирует одно музыкальное произведение.

    :param i: Номер музыкального произведения.
    :type i: int
    """
    try:
        # Генерируем мелодическую последовательность
        melody_sequence = melody_rnn.generate(
            temperature=temperature,
            steps=steps_per_music_piece,
            primer_sequence=None
        )

        # Получаем аккорды для мелодии в зависимости от выбранного жанра
        chords = [chord_progressions.get(preferred_genre, ["C"])[i % len( # Если жанр не найден, используем аккорды "C"
            chord_progressions.get(preferred_genre, ["C"]))] for i in range(steps_per_music_piece)]
        chord_sequence = mm.ChordSequence(chords) # Создаем последовательность аккордов
        melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences( # Соединяем мелодию и аккорды
            melody_sequence, chord_sequence)

        # Создаем MIDI-файл из мелодии с аккордами и барабанным паттерном
        music_sequence = mm.sequences_lib.concatenate_sequences( # Соединяем мелодию с аккордами и барабанами
            melody_with_chords_sequence, drum_pattern)
        music_sequence.tempos[0].qpm = preferred_tempo # Устанавливаем темп

        midi_file = os.path.join(output_dir, f'music_piece_{i + 1}.mid')  # Создаем имя файла
        mm.sequence_proto_to_midi_file(music_sequence, midi_file) # Сохраняем MIDI
        print(f'Музыкальное произведение {i + 1} сгенерировано и сохранено как {midi_file}') # Сообщаем об успехе

    except Exception as ex:
        logger.error(f'Ошибка при генерации музыкального произведения {i + 1}', ex) # Логируем ошибку генерации
        ...

def generate_music():
    """
    Генерирует несколько музыкальных произведений.
    """
    for i in range(num_music_pieces): # Генерируем нужное количество музыкальных произведений
        generate_music_piece(i)
    print('Генерация музыки завершена!') # Сообщаем о завершении генерации

if __name__ == '__main__':
    generate_music() # Запускаем функцию генерации музыки при запуске скрипта
```