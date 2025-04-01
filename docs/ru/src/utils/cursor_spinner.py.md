# Модуль для отображения вращающегося курсора
## Обзор

Модуль `cursor_spinner.py` предоставляет утилиту для отображения вращающегося курсора в консоли, имитируя процесс загрузки или ожидания. Он включает функции для генерации символов вращения и отображения курсора в течение заданного времени.
## Подробнее

Этот модуль полезен для визуальной индикации пользователю о том, что программа выполняет длительную операцию, такую как загрузка данных или ожидание ответа от сервера. Он использует символы `|`, `/`, `-`, `\` для создания эффекта вращения.
## Функции

### `spinning_cursor`

```python
def spinning_cursor():
    """ Generator for a spinning cursor that cycles through |, /, -, \\ symbols.
    
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
        for cursor in '|/-\\|':
            yield cursor
```

**Назначение**:
Генератор, который циклически перебирает символы `|`, `/`, `-`, `\` для создания эффекта вращающегося курсора.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Следующий символ в последовательности курсора.

**Как работает функция**:

1.  Функция `spinning_cursor` является генератором, который бесконечно выдает символы `|`, `/`, `-`, `\`.
2.  При каждом вызове `next(spinning_cursor())` возвращается следующий символ из последовательности.

**Примеры**:

```python
>>> cursor = spinning_cursor()
>>> next(cursor)
'|'
>>> next(cursor)
'/'
>>> next(cursor)
'-'
>>> next(cursor)
'\\'
```

### `show_spinner`

```python
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
```

**Назначение**:
Отображает вращающийся курсор в консоли в течение указанного времени.

**Параметры**:
-   `duration` (float): Продолжительность отображения курсора в секундах. По умолчанию 5.0.
-   `delay` (float): Задержка между каждым шагом вращения в секундах. По умолчанию 0.1.

**Возвращает**:
-   None

**Как работает функция**:

1.  Инициализируется генератор `spinning_cursor`.
2.  Определяется время окончания работы курсора на основе заданной продолжительности.
3.  В цикле, пока не истекло заданное время:
    *   Выводится следующий символ из генератора курсора.
    *   Буфер вывода принудительно сбрасывается, чтобы символ сразу отобразился в консоли.
    *   Происходит задержка на заданное время.
    *   Символ удаляется из консоли символом возврата (`\b`).

```
spinner_cursor
      │
      │ Создание генератора символов
      │
      ▼
Определение времени окончания работы курсора
      │
      │ Цикл пока не истекло заданное время
      │
      ▼
Вывод следующего символа из генератора
      │
      │ Сброс буфера вывода
      │
      ▼
Задержка на заданное время
      │
      │ Удаление символа из консоли
      │
      ▼
Конец цикла
```

**Примеры**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Отображает курсор в течение 3 секунд с задержкой 0.2 секунды