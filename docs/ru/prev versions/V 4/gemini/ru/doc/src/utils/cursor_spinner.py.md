# Модуль `cursor_spinner`

## Обзор

Модуль `cursor_spinner` предоставляет утилиту для отображения вращающегося курсора в консоли, имитируя процесс загрузки или ожидания.

## Подробней

Этот модуль полезен для визуальной индикации выполнения длительных операций в консольных приложениях. Он содержит функции для генерации символов вращающегося курсора и отображения его в течение заданного времени. В проекте `hypotez` данный модуль может использоваться для улучшения пользовательского опыта при выполнении задач, требующих времени, таких как обработка больших объемов данных или ожидание ответа от внешних сервисов.

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

**Описание**: Генератор для вращающегося курсора, который циклически перебирает символы `|`, `/`, `-`, `\`.

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

**Как работает функция**:
Функция `spinning_cursor` является генератором, который циклически перебирает символы `|`, `/`, `-`, `\` и возвращает их по одному при каждом вызове `next()`. Это позволяет создать эффект вращения курсора в консоли.

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

**Описание**: Отображает вращающийся курсор в консоли в течение заданного времени.

**Параметры**:
- `duration` (float): Как долго должен работать спиннер (в секундах). По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением (в секундах). По умолчанию 0.1.

**Примеры**:
```python
>>> show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
```

**Как работает функция**:
Функция `show_spinner` создает экземпляр генератора `spinning_cursor`, определяет время окончания работы спиннера и в цикле выводит символы спиннера в консоль с заданной задержкой. После каждого вывода символа происходит его стирание, чтобы создать эффект вращения на одном и том же месте в консоли.

```
[Flowchart]
    start --> initialize spinner and end_time
    loop: time.time() < end_time?
    loop -- yes --> print next spinner character
    print next spinner character --> flush stdout
    flush stdout --> sleep for delay
    sleep for delay --> backspace to overwrite character
    backspace to overwrite character --> loop
    loop -- no --> end
    end --> stop