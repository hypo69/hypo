# Модуль `cursor_spinner`

## Обзор

Модуль `cursor_spinner` предоставляет утилиту для отображения вращающегося курсора в консоли, чтобы имитировать процесс загрузки или ожидания. Он включает в себя генератор для циклического перебора символов `|`, `/`, `-`, `\\` и функцию для отображения курсора в течение заданного времени.

## Подробней

Этот модуль полезен для визуальной индикации активности программы, когда выполнение занимает некоторое время, и пользователю необходимо показать, что процесс выполняется, а не завис. Он может быть использован в различных скриптах и приложениях, работающих в консоли.

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
```

**Описание**: Генератор для вращающегося курсора, который циклически перебирает символы `|`, `/`, `-`, `\`.

**Возвращает**:
- `str`: Следующий символ в последовательности курсора.

**Примеры**:

```python
>>> cursor = spinning_cursor()
>>> next(cursor)  # '|'
>>> next(cursor)  # '/'
>>> next(cursor)  # '-'
>>> next(cursor)  # '\\'
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
```

**Описание**: Отображает вращающийся курсор в консоли в течение указанного времени.

**Параметры**:
- `duration` (float): Как долго должен работать спиннер (в секундах). По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением (в секундах). По умолчанию 0.1.

**Примеры**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
```
```python
    # Example usage of the spinner in a script
    print("Spinner for 5 seconds:")
    show_spinner(duration=5.0, delay=0.1)
    print("\nDone!")