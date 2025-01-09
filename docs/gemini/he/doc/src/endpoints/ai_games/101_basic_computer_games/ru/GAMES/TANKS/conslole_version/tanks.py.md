# Модуль `tanks.py`

## Обзор

Этот модуль реализует простую консольную игру в танки. Он содержит классы `Tank` и `SuperTank`, которые позволяют моделировать бои между танками.

## Содержание

1. [Классы](#классы)
   - [Tank](#класс-tank)
   - [SuperTank](#класс-supertank)
2. [Функции](#функции)
   - [main](#функция-main)

## Классы

### `Tank`

**Описание**:
Базовый класс для танков.

**Методы**:

- [`__init__`](#метод-__init__)
- [`calculate_damage`](#метод-calculate_damage)
- [`print_info`](#метод-print_info)
- [`health_down`](#метод-health_down)
- [`shot`](#метод-shot)

#### `__init__`

```python
def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
    """
    Args:
        model (str): Модель танка.
        armor (int): Броня танка.
        min_damage (int): Минимальный урон танка.
        max_damage (int): Максимальный урон танка.
        health (int): Здоровье танка.
    """
```

**Описание**:
Инициализация танка.

**Параметры**:
- `model` (str): Модель танка.
- `armor` (int): Броня танка.
- `min_damage` (int): Минимальный урон танка.
- `max_damage` (int): Максимальный урон танка.
- `health` (int): Здоровье танка.

**Возвращает**:
- `None`

#### `calculate_damage`

```python
def calculate_damage(self) -> int:
    """
    Returns:
        int: Случайный урон.
    """
```

**Описание**:
Вычисляет случайный урон танка в заданном диапазоне.

**Параметры**:
- Нет

**Возвращает**:
- `int`: Случайный урон.

#### `print_info`

```python
def print_info(self) -> None:
    """
    """
```

**Описание**:
Выводит информацию о танке.

**Параметры**:
- Нет

**Возвращает**:
- `None`

#### `health_down`

```python
def health_down(self, enemy_damage: int) -> None:
    """
    Args:
        enemy_damage (int): Урон, нанесенный противником.
    """
```

**Описание**:
Уменьшает здоровье танка.

**Параметры**:
- `enemy_damage` (int): Урон, нанесенный противником.

**Возвращает**:
- `None`

#### `shot`

```python
def shot(self, enemy: object) -> None:
    """
    Args:
        enemy (object): Танк-противник.
    """
```

**Описание**:
Танк стреляет по противнику.

**Параметры**:
- `enemy` (object): Танк-противник.

**Возвращает**:
- `None`

### `SuperTank`

**Описание**:
Класс для супертанка, наследуется от `Tank`.

**Методы**:

- [`__init__`](#метод-__init__-1)
- [`health_down`](#метод-health_down-1)

#### `__init__`

```python
def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
    """
    Args:
        model (str): Модель танка.
        armor (int): Броня танка.
        min_damage (int): Минимальный урон танка.
        max_damage (int): Максимальный урон танка.
        health (int): Здоровье танка.
    """
```

**Описание**:
Инициализация супертанка.

**Параметры**:
- `model` (str): Модель танка.
- `armor` (int): Броня танка.
- `min_damage` (int): Минимальный урон танка.
- `max_damage` (int): Максимальный урон танка.
- `health` (int): Здоровье танка.

**Возвращает**:
- `None`

#### `health_down`

```python
def health_down(self, enemy_damage: int) -> None:
    """
    Args:
        enemy_damage (int): Урон, нанесенный противником.
    """
```

**Описание**:
Уменьшает здоровье супертанка с учетом повышенной брони.

**Параметры**:
- `enemy_damage` (int): Урон, нанесенный противником.

**Возвращает**:
- `None`

## Функции

### `main`

```python
def main() -> None:
    """
    """
```

**Описание**:
Основная функция игры.

**Параметры**:
- Нет

**Возвращает**:
- `None`