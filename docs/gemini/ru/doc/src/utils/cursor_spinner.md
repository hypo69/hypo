# Модуль `hypotez/src/utils/cursor_spinner.py`

## Обзор

Модуль `cursor_spinner` предоставляет функцию для отображения вращающегося курсора в консоли, что позволяет имитировать процесс загрузки или ожидания.

## Функции

### `spinning_cursor`

**Описание**: Генератор, который циклически выдает символы |, /, -, \ для отображения вращающегося курсора.

**Возвращает**:
- `str`: Следующий символ в последовательности вращения курсора.


**Пример использования**:

```python
>>> cursor = spinning_cursor()
>>> next(cursor)  # '|'
>>> next(cursor)  # '/'
>>> next(cursor)  # '-'
>>> next(cursor)  # '\\'
```


### `show_spinner`

**Описание**: Отображает вращающийся курсор в консоли на заданный период времени.

**Параметры**:
- `duration` (float): Время работы спиннера в секундах. По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением спиннера в секундах. По умолчанию 0.1.


**Пример использования**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер на 3 секунды
```

**Возможные ошибки**:
(Нет указанных ошибок)


## Пример использования в скрипте

```python
print("Spinner for 5 seconds:")
show_spinner(duration=5.0, delay=0.1)
print("\nDone!")
```

Этот пример демонстрирует как использовать функцию `show_spinner` для создания спиннера, отображаемого на 5 секунд.


```