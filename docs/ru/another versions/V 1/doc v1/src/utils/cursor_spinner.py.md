# Модуль `cursor_spinner`

## Обзор

Модуль `cursor_spinner` предоставляет утилиту для отображения вращающегося курсора в консоли, чтобы имитировать процесс загрузки или ожидания.

## Подробней

Этот модуль предназначен для визуальной индикации выполнения длительных операций в консольных приложениях. Он использует генератор `spinning_cursor` для создания последовательности символов, которые отображаются в консоли с заданной задержкой, создавая эффект вращения. Это может быть полезно для улучшения пользовательского опыта, предоставляя обратную связь о том, что программа все еще работает.

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

**Описание**: Генератор для вращающегося курсора, который циклически перебирает символы |, /, -, \.

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
    ...
```

**Описание**: Отображает вращающийся курсор в консоли в течение указанного времени.

**Параметры**:
- `duration` (float): Как долго должен работать спиннер (в секундах). По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением (в секундах). По умолчанию 0.1.

**Примеры**:
   ```python
   >>> show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер в течение 3 секунд
   ```