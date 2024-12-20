# Модуль `hypotez/src/utils/cursor_spinner.py`

## Обзор

Данный модуль предоставляет утилиту для отображения вращающегося курсора в консоли, имитирующего процесс загрузки или ожидания.

## Функции

### `spinning_cursor`

**Описание**: Генератор, циклически возвращающий символы |, /, -, \ для имитации вращения курсора.

**Возвращает**:
- `str`: Следующий символ в последовательности курсора.

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
- `duration` (float): Длительность работы спиннера (в секундах). По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением (в секундах). По умолчанию 0.1.

**Пример использования**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер на 3 секунды
```

**Примечания**:
- Функция использует метод `sys.stdout.write` для вывода символа в консоль.
- `sys.stdout.flush()` используется для немедленного отображения символа в консоли.
- `\b` используется для удаления символа, чтобы спиннер отображался как вращающийся.

## Использование в скрипте

Приведенный пример демонстрирует использование функции `show_spinner` в скрипте.

```python
if __name__ == "__main__":
    print("Спиннер на 5 секунд:")
    show_spinner(duration=5.0, delay=0.1)
    print("\nГотово!")
```


```
```
```
```