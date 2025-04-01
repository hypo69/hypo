# Модуль для отображения вращающегося курсора

## Обзор

Этот модуль предоставляет утилиту для отображения вращающегося курсора в консоли, чтобы имитировать процесс загрузки или ожидания.

## Подробнее

Модуль содержит две основные функции: `spinning_cursor` и `show_spinner`. Функция `spinning_cursor` является генератором, который циклически перебирает символы `|`, `/`, `-`, `\` для создания анимации вращения. Функция `show_spinner` использует этот генератор для отображения вращающегося курсора в консоли в течение заданного времени.

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
        for cursor in '|/-\\':
            yield cursor
```

**Описание**: Генератор для вращающегося курсора, который циклически перебирает символы `|`, `/`, `-`, `\` .

**Как работает функция**:
Функция `spinning_cursor` — это генератор, который бесконечно выдает символы из строки `'|/-\\'`. При каждом вызове `next(spinning_cursor())` возвращается следующий символ из этой последовательности.

**Возвращает**:
- `str`: Следующий символ в последовательности курсора.

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

**Описание**: Отображает вращающийся курсор в консоли в течение заданного времени.

**Как работает функция**:

1.  Инициализирует генератор `spinning_cursor()`.
2.  Вычисляет время окончания анимации на основе заданной продолжительности `duration`.
3.  В цикле, пока текущее время меньше времени окончания:

    *   Выводит следующий символ из генератора `spinner` с помощью `sys.stdout.write()`.
    *   Принудительно выводит символ в консоль с помощью `sys.stdout.flush()`.
    *   Приостанавливает выполнение на заданное время `delay` с помощью `time.sleep()`.
    *   Использует символ возврата `\b` для перезаписи предыдущего символа, создавая эффект вращения.

**Параметры**:

*   `duration` (float): Продолжительность работы спиннера в секундах. По умолчанию 5.0.
*   `delay` (float): Задержка между каждым вращением в секундах. По умолчанию 0.1.

**Примеры**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер в течение 3 секунд
```