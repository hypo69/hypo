# <input code>

```python
## \file hypotez/src/utils/cursor_spinner.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: utility to show a spinning cursor

"""
MODE = 'dev'

"""
This module provides a utility to show a spinning cursor in the console 
to simulate a loading or waiting process.
"""

import time
import sys

def spinning_cursor():
    """ Generator for a spinning cursor that cycles through |, /, -, \\\\ symbols.
    
    Yields:
        str: The next symbol in the cursor sequence.
    
    Example:
        >>> cursor = spinning_cursor()
        >>> next(cursor)  # '|'
        >>> next(cursor)  # '/'
        >>> next(cursor)  # '-'
        >>> next(cursor)  # '\\'
    """
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(duration: float = 5.0, delay: float = 0.1):
    """ Shows a spinning cursor in the console for a specified duration.
    
    Args:
        duration (float): How long the spinner should run (in seconds). Defaults to 5.0.
        delay (float): Delay between each spin (in seconds). Defaults to 0.1.
    
    Example:
        >>> show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
    """
    spinner = spinning_cursor()
    end_time = time.time() + duration

    while time.time() < end_time:
        sys.stdout.write(next(spinner))   # Print the next spinner character
        sys.stdout.flush()                # Force print to console immediately
        time.sleep(delay)                 # Pause for the delay duration
        sys.stdout.write('\b')            # Backspace to overwrite the character

if __name__ == "__main__":
    # Example usage of the spinner in a script
    print("Spinner for 5 seconds:")
    show_spinner(duration=5.0, delay=0.1)
    print("\nDone!")
```

# <algorithm>

**Алгоритм работы модуля `cursor_spinner`**

1. **`spinning_cursor()`:**
   - Создает бесконечный цикл `while True`.
   - Внутри цикла, перебирает символы '|', '/', '-', '\'.
   - Для каждого символа, `yield` возвращает его, передавая управление в вызывающий код.

   **Пример:** Если вызвать `next(spinning_cursor())`, то будет возвращен символ '|'. Следующий вызов `next()` вернет '/'.


2. **`show_spinner()`:**
   - Принимает `duration` (длительность вращения) и `delay` (задержка между шагами) в качестве аргументов.
   - Создает генератор `spinner` с помощью `spinning_cursor()`.
   - Вычисляет время окончания `end_time`.
   - В цикле `while`:
     - Получает следующий символ из генератора `spinner` с помощью `next(spinner)`.
     - Выводит символ в стандартный вывод `sys.stdout.write()`.
     - Заставляет консоль отобразить символ немедленно `sys.stdout.flush()`.
     - Ожидает `delay` секунд с помощью `time.sleep()`.
     - Возвращает курсор назад с помощью `\b` для перекрытия символа.
     - Проверяет, не истекло ли время `time.time() < end_time`.

**Пример:** Если вызвать `show_spinner(duration=3, delay=0.5)`, то в течение 3 секунд будут последовательно выводиться символы '|', '/', '-', '\\', с задержкой 0.5 секунды между ними.


# <mermaid>

```mermaid
graph TD
    A[show_spinner(duration,delay)] --> B{time < end_time?};
    B -- yes --> C[spinner = spinning_cursor()];
    B -- no --> D[print "Done!"];
    C --> E[next(spinner)];
    E --> F[sys.stdout.write(next(spinner))];
    F --> G[sys.stdout.flush()];
    G --> H[time.sleep(delay)];
    H --> I[sys.stdout.write('\b')];
    I --> B;
    subgraph spinning_cursor
        J[while True] --> K[for cursor in '|/-\\'];
        K --> L{yield cursor};
        L --> J;
    end
```

# <explanation>

**Импорты:**

- `time`: Для управления временными задержками (используется в `time.sleep()` и `time.time()`).
- `sys`: Для работы со стандартным выводом (используется в `sys.stdout.write()` и `sys.stdout.flush()`).

**Классы:**

- Нет определенных классов в данном коде.

**Функции:**

- `spinning_cursor()`:  Возвращает бесконечный итератор, который поочередно генерирует символы '|', '/', '-', '\\'.
    - Аргументов нет.
    - Возвращает итератор (генератор).
- `show_spinner(duration=5.0, delay=0.1)`:  Отображает вращающийся курсор на консоли в течение заданного времени.
    - `duration`: Длительность работы (по умолчанию 5 секунд).
    - `delay`: Задержка между отображением символов (по умолчанию 0.1 секунды).
    - Возвращаемое значение:  Функция не возвращает значения.

**Переменные:**

- `MODE`: Строковая константа, хранящая значение 'dev'.
- `duration`:  Переменная, определяющая длительность отображения вращающегося курсора (в секундах).
- `delay`: Переменная, определяющая задержку между отображением символов вращающегося курсора (в секундах).
- `spinner`: Переменная, хранящая итератор (генератор), возвращаемый функцией `spinning_cursor()`.
- `end_time`: Переменная, хранящая время окончания работы.


**Возможные ошибки и улучшения:**

- **Вывод в консоль:**  Код хорошо работает, но  может быть несовместим с другими программами, которые используют стандартный поток вывода (например, если он используется для отображения чего-либо другого).

- **Управление прерыванием:** Код не обрабатывает прерывание процесса, поэтому, если программа прервется в момент работы `show_spinner`, символ, который был напечатан, не будет удалён.


**Цепочка взаимосвязей:**

Этот модуль `cursor_spinner` является утилитой, которая используется для отображения  вращающегося курсора в консоли.  Он не зависит напрямую от других частей проекта, но может использоваться в других модулях (или скриптах) для визуализации процесса загрузки.