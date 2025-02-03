## Пояснения к коду GUI Piano на Python

Данный код реализует GUI Piano на Python с использованием библиотеки Pygame. Рассмотрим код построчно, поясняя его функциональность:

```python
# Импорт необходимых библиотек для Piano на Python
import pygame
import piano_lists as pl
from pygame import mixer
```

*   **`import pygame`**: Импортирует библиотеку Pygame для создания графического интерфейса и обработки событий.
*   **`import piano_lists as pl`**: Импортирует файл `piano_lists.py`, который содержит списки нот, клавиш и другие данные для пианино.
*   **`from pygame import mixer`**:  Импортирует модуль `mixer` из Pygame, который используется для воспроизведения звуков.

```python
# Инициализация библиотеки pygame
pygame.init()
pygame.mixer.set_num_channels(50)
```

*   **`pygame.init()`**: Инициализирует все модули Pygame.
*   **`pygame.mixer.set_num_channels(50)`**: Устанавливает количество каналов для воспроизведения звуков. Это позволяет одновременно воспроизводить несколько нот.

```python
font = pygame.font.Font('assets/Terserah.ttf', 48)
medium_font = pygame.font.Font('assets/Terserah.ttf', 28)
small_font = pygame.font.Font('assets/Terserah.ttf', 16)
real_small_font = pygame.font.Font('assets/Terserah.ttf', 10)
fps = 60
```

*   Загружает шрифты различных размеров из файла `'assets/Terserah.ttf'` для отображения текста на клавишах и в интерфейсе.
*   **`fps = 60`**: Устанавливает частоту кадров (FPS) для обновления экрана.

```python
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 4
right_oct = 5
```

*   **`timer = pygame.time.Clock()`**: Создает объект Clock для управления частотой кадров.
*   **`WIDTH = 52 * 35`**: Устанавливает ширину окна.  Предположительно, `35` - ширина одной белой клавиши, а `52` - общее количество белых клавиш.
*   **`HEIGHT = 400`**: Устанавливает высоту окна.
*   **`screen = pygame.display.set_mode([WIDTH, HEIGHT])`**: Создает окно Pygame с указанной шириной и высотой.
*   **`white_sounds = []`**:  Список для хранения звуковых объектов для белых клавиш.
*   **`black_sounds = []`**: Список для хранения звуковых объектов для черных клавиш.
*   **`active_whites = []`**: Список для отслеживания нажатых белых клавиш (для подсветки).
*   **`active_blacks = []`**: Список для отслеживания нажатых черных клавиш (для подсветки).
*   **`left_oct = 4`**: Начальная октава для левой руки.
*   **`right_oct = 5`**: Начальная октава для правой руки.

```python
left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels
```

*   Извлекает списки клавиш и нот из импортированного модуля `piano_lists`.  `left_hand` и `right_hand` содержат символы, соответствующие клавишам для левой и правой руки, а `piano_notes`, `white_notes`, `black_notes` и `black_labels` содержат названия нот и соответствующие метки.

```python
for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))
```

*   Загружает звуковые файлы для каждой белой и черной клавиши из директории `'assets/notes/'` и добавляет их в списки `white_sounds` и `black_sounds`.

```python
pygame.display.set_caption("Python Piano - CopyAssignment")
```

*   Устанавливает заголовок окна Pygame.

```python
def draw_piano(whites, blacks):
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i* 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i* 35, HEIGHT - 300, 35, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i* 35 + 3, HEIGHT - 20))

    skip_count = 0
    last_skip = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i*35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i* 35) + (skip_count * 35), HEIGHT - 300, 24, 100], 0, 2)
                    blacks[q][1] -= 1
        key_label = real_small_font.render(black_labels[i], True, 'white')
        screen.blit(key_label, (25+ (i* 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)

        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks
```

*   Функция `draw_piano(whites, blacks)` рисует клавиши пианино на экране.
    *   Рисует белые клавиши, добавляет рамку и отображает метки нот.
    *   Рисует черные клавиши,  рассчитывает их положение с учетом пропусков, добавляет рамку и отображает метки нот.
    *   Подсвечивает нажатые клавиши зеленым цветом.  `whites` и `blacks` - это списки, которые содержат информацию о нажатых клавишах (индекс клавиши и продолжительность подсветки).
    *   Возвращает списки прямоугольников для белых и черных клавиш, а также обновленные списки нажатых клавиш.

```python
def draw_hands(rightOct, leftOct, rightHand, leftHand):
    pygame.draw.rect(screen, 'dark gray', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(leftHand[0], True, 'white')
    screen.blit(text, ((leftOct * 245) - 165, HEIGHT - 55))
    # ... (аналогичный код для отображения остальных клавиш левой руки)

    pygame.draw.rect(screen, 'dark gray', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(rightHand[0], True, 'white')
    screen.blit(text, ((rightOct * 245) - 165, HEIGHT - 55))
    # ... (аналогичный код для отображения остальных клавиш правой руки)
```

*   Функция `draw_hands` рисует подсказки для клавиш левой и правой руки в нижней части экрана.

```python
def draw_title_bar():
    instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
    screen.blit(instruction_text, (WIDTH - 500, 10))
    instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 500, 50))

    title_text = font.render('CopyAssignment Paino!', True, 'white')
    screen.blit(title_text, (298, 18))
    title_text = font.render('CopyAssignment Paino!', True, 'black')
    screen.blit(title_text, (300, 20))
```

*   Функция `draw_title_bar` рисует заголовок и инструкции в верхней части экрана.

```python
run = True
while run:
    left_dict = {'Z': f'C{left_oct}',
                 'S': f'C#{left_oct}',
                 'X': f'D{left_oct}',
                 'D': f'D#{left_oct}',
                 'C': f'E{left_oct}',
                 'V': f'F{left_oct}',
                 'G': f'F#{left_oct}',
                 'B': f'G{left_oct}',
                 'H': f'G#{left_oct}',
                 'N': f'A{left_oct}',
                 'J': f'A#{left_oct}',
                 'M': f'B{left_oct}'}

    right_dict = {'R': f'C{right_oct}',
                  '5': f'C#{right_oct}',
                  'T': f'D{right_oct}',
                  '6': f'D#{right_oct}',
                  'Y': f'E{right_oct}',
                  'U': f'F{right_oct}',
                  '8': f'F#{right_oct}',
                  'I': f'G{right_oct}',
                  '9': f'G#{right_oct}',
                  'O': f'A{right_oct}',
                  '0': f'A#{right_oct}',
                  'P': f'B{right_oct}'}

    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    draw_hands(right_oct, left_oct, right_hand, left_hand)
    draw_title_bar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1000)
                    black_key = True
                    active_blacks.append([i, 30])
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    active_whites.append([i, 30])
        if event.type == pygame.TEXTINPUT:
            if event.text.upper() in left_dict:
                if left_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(left_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(left_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            if event.text.upper() in right_dict:
                if right_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(right_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(right_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    right_oct -= 1
            if event.key == pygame.K_UP:
                if left_oct < 8:
                    left_oct += 1
            if event.key == pygame.K_DOWN:
                if left_oct > 0:
                    left_oct -= 1

    pygame.display.flip()

pygame.quit()
```

*   **`run = True`**: Устанавливает флаг для запуска основного цикла игры.
*   **`while run:`**: Основной цикл игры.
*   **`left_dict` и `right_dict`**: Словари, связывающие клавиши клавиатуры с нотами для левой и правой руки.  `f'C{left_oct}'` формирует строку с названием ноты на основе текущей октавы (`left_oct` и `right_oct`).
*   **`timer.tick(fps)`**: Ограничивает частоту кадров.
*   **`screen.fill('gray')`**: Заполняет экран серым цветом.
*   **`white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)`**: Вызывает функцию для рисования пианино и получает обновленные списки клавиш.
*   **`draw_hands(right_oct, left_oct, right_hand, left_hand)`**: Вызывает функцию для рисования подсказок для клавиш.
*   **`draw_title_bar()`**: Вызывает функцию для рисования заголовка.
*   **`for event in pygame.event.get():`**:  Цикл обработки событий Pygame.
    *   **`if event.type == pygame.QUIT:`**: Обрабатывает событие закрытия окна.
    *   **`if event.type == pygame.MOUSEBUTTONDOWN:`**:  Обрабатывает событие нажатия кнопки мыши.  Определяет, была ли нажата белая или черная клавиша, воспроизводит соответствующий звук и добавляет клавишу в список активных клавиш для подсветки.  `collidepoint(event.pos)` проверяет, находится ли точка нажатия мыши внутри прямоугольника клавиши.
    *   **`if event.type == pygame.TEXTINPUT:`**: Обрабатывает событие ввода текста (нажатие клавиши клавиатуры). Если введенный символ соответствует клавише из словарей `left_dict` или `right_dict`, воспроизводит соответствующий звук и добавляет клавишу в список активных клавиш.
    *   **`if event.type == pygame.KEYDOWN:`**: Обрабатывает событие нажатия клавиши.  Обрабатывает нажатие клавиш-стрелок для изменения октав.
*   **`pygame.display.flip()`**: Обновляет экран.
*   **`pygame.quit()`**: Выходит из Pygame.

### `piano_lists.py`

Этот файл содержит списки данных для пианино:

```python
#список для клавиш левой руки
left_hand = ['Z', 'S', 'X', 'D', 'C', 'V', 'G', 'B', 'H', 'N', 'J', 'M']
#список для клавиш правой руки
right_hand = ['R', '5', 'T', '6', 'Y', 'U', '8', 'I', '9', 'O', '0', 'P']

piano_notes = ['A0', 'A0#', 'B0', 'C1', 'C1#', 'D1', 'D1#', 'E1', 'F1', 'F1#', 'G1', 'G1#',
'A1', 'A1#', 'B1', 'C2', 'C2#', 'D2', 'D2#', 'E2', 'F2', 'F2#', 'G2', 'G2#',
'A2', 'A2#', 'B2', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#',
'A3', 'A3#', 'B3', 'C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#',
'A4', 'A4#', 'B4', 'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#',
'A5', 'A5#', 'B5', 'C6', 'C6#', 'D6', 'D6#', 'E6', 'F6', 'F6#', 'G6', 'G6#',
'A6', 'A6#', 'B6', 'C7', 'C7#', 'D7', 'D7#', 'E7', 'F7', 'F7#', 'G7', 'G7#',
'A7', 'A7#', 'B7', 'C8']

white_notes = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1',
'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2',
'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3',
'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6',
'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7',
'A7', 'B7', 'C8']
black_notes = ['Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
'Bb7']
black_labels = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1',
'A#1', 'C#2', 'D#2', 'F#2', 'G#2',
'A#2', 'C#3', 'D#3', 'F#3', 'G#3',
'A#3', 'C#4', 'D#4', 'F#4', 'G#4',
'A#4', 'C#5', 'D#5', 'F#5', 'G#5',
'A#5', 'C#6', 'D#6', 'F#6', 'G#6',
'A#6', 'C#7', 'D#7', 'F#7', 'G#7',
```

*   `left_hand` и `right_hand`: списки клавиш, соответствующих левой и правой руке. Используются для отображения подсказок.
*   `piano_notes`:  полный список всех нот, которые можно воспроизвести на пианино.
*   `white_notes`: список только белых клавиш.
*   `black_notes`: список только черных клавиш.
*   `black_labels`: список меток для черных клавиш.

### Общее описание

В целом, код представляет собой программу, эмулирующую пианино с графическим интерфейсом, использующую библиотеку Pygame. Он позволяет воспроизводить звуки нот, нажимая на клавиши мышью или с клавиатуры, а также изменять октавы. Данный код предполагает, что в папке `assets` находятся шрифт `Terserah.ttf` и подпапка `notes`, содержащая .wav файлы для каждой ноты, названные в соответствии со списками нот из `piano_lists.py`.
