# Модуль `cursor_spinner`

## Обзор

Модуль `cursor_spinner` предоставляет утилиту для отображения вращающегося курсора в консоли, чтобы имитировать процесс загрузки или ожидания.

## Подробнее

Этот модуль полезен для визуальной индикации пользователю о том, что программа выполняет какую-то задачу в фоновом режиме и не зависла. Он содержит функции для генерации символов вращающегося курсора и отображения его в консоли в течение заданного времени.

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
    ...
```

**Назначение**:
Генератор для вращающегося курсора, который циклически перебирает символы `|`, `/`, `-`, `\`.

**Параметры**:
Отсутствуют.

**Возвращает**:
- `str`: Следующий символ в последовательности курсора.

**Как работает функция**:

1. Функция `spinning_cursor` является генератором, который бесконечно циклически перебирает символы `|`, `/`, `-`, `\`.
2. При каждом вызове `next(spinner)` возвращается следующий символ из последовательности.

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
    ...
```

**Назначение**:
Отображает вращающийся курсор в консоли в течение заданного времени.

**Параметры**:
- `duration` (float): Продолжительность работы курсора в секундах. По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением в секундах. По умолчанию 0.1.

**Как работает функция**:

1. Функция `show_spinner` принимает два аргумента: `duration` (продолжительность отображения курсора) и `delay` (задержка между сменой символов).
2. Создается генератор `spinning_cursor()`, который предоставляет символы для анимации.
3. Определяется время окончания работы курсора (`end_time`).
4. В цикле, пока текущее время меньше `end_time`:
   - Выводится следующий символ из генератора `spinning_cursor()` с помощью `sys.stdout.write()`.
   - `sys.stdout.flush()` используется для немедленного отображения символа в консоли.
   - Происходит пауза на время, указанное в `delay` с помощью `time.sleep()`.
   - Символ удаляется из консоли с помощью `sys.stdout.write('\b')`, чтобы создать эффект вращения.

**Примеры**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Отображает вращающийся курсор в течение 3 секунд с задержкой 0.2 секунды