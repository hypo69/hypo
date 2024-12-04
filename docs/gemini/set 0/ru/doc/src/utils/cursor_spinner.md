# Модуль `hypotez/src/utils/cursor_spinner.py`

## Обзор

Модуль `cursor_spinner` предоставляет инструменты для отображения вращающегося курсора в консоли, имитируя процесс загрузки или ожидания.

## Функции

### `spinning_cursor`

**Описание**: Генератор, возвращающий символы вращающегося курсора (`|`, `/`, `-`, `\`).

**Возвращает**:
- `str`: Следующий символ в последовательности.


**Пример использования:**

```python
import cursor_spinner

cursor = cursor_spinner.spinning_cursor()
print(next(cursor))  # Вывод: |
print(next(cursor))  # Вывод: /
```


### `show_spinner`

**Описание**: Показывает вращающийся курсор в консоли на заданное время.

**Параметры**:
- `duration` (float): Время работы спиннера (в секундах). По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением (в секундах). По умолчанию 0.1.


**Пример использования:**

```python
import cursor_spinner

cursor_spinner.show_spinner(duration=3.0, delay=0.2) # Покажет спиннер в течение 3 секунд
```

**Возвращает**:
- None


## Пример использования в скрипте

```python
import cursor_spinner

print("Спиннер на 5 секунд:")
cursor_spinner.show_spinner(duration=5.0, delay=0.1)
print("\nГотово!")
```