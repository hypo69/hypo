# Модуль `traffic_light.py`

## Обзор

Модуль `traffic_light.py` предназначен для имитации работы светофора. Подробное описание работы модуля можно найти по [ссылке](https://habr.com/ru/articles/849414/).

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
    - [`TrafficLight`](#TrafficLight)
- [Функции](#функции)
    - [`create_traffic_light`](#create_traffic_light)
    - [`get_signal_color`](#get_signal_color)
    - [`switch_signal`](#switch_signal)

## Классы

### `TrafficLight`

**Описание**:
Класс, представляющий светофор.

**Методы**:
- `__init__`: Инициализирует объект светофора.
- `set_color`: Устанавливает текущий цвет светофора.
- `get_color`: Возвращает текущий цвет светофора.
- `switch_color`: Переключает цвет светофора на следующий в последовательности.

**Параметры**:
 - `current_color` (str, optional): Начальный цвет светофора. По умолчанию `red`.

```python
class TrafficLight:
    """
    Args:
        current_color (str, optional): Начальный цвет светофора. По умолчанию `red`.
    """
    def __init__(self, current_color="red"):
        self._colors = ["red", "yellow", "green"]
        self._current_color = current_color

    def set_color(self, color: str) -> None:
        """
        Args:
            color (str): Цвет, который нужно установить.
        """
        self._current_color = color

    def get_color(self) -> str:
        """
        Returns:
            str: Текущий цвет светофора.
        """
        return self._current_color

    def switch_color(self) -> str:
        """
        Returns:
            str: Следующий цвет в последовательности.
        """
        idx = self._colors.index(self._current_color)
        self._current_color = self._colors[(idx + 1) % len(self._colors)]
        return self._current_color
```

## Функции

### `create_traffic_light`

**Описание**:
Создает экземпляр класса `TrafficLight`.

**Параметры**:
- `current_color` (str, optional): Начальный цвет светофора. По умолчанию `red`.

**Возвращает**:
- `TrafficLight`: Объект светофора.

```python
def create_traffic_light(current_color: str = "red") -> TrafficLight:
    """
    Args:
        current_color (str, optional): Начальный цвет светофора. По умолчанию `red`.

    Returns:
        TrafficLight: Объект светофора.
    """
    return TrafficLight(current_color)
```

### `get_signal_color`

**Описание**:
Возвращает текущий цвет светофора.

**Параметры**:
- `traffic_light` (TrafficLight): Объект светофора.

**Возвращает**:
- `str`: Текущий цвет светофора.

**Вызывает исключения**:
- `AttributeError`: Если передан неверный тип объекта, вызовется исключение.

```python
def get_signal_color(traffic_light: TrafficLight) -> str:
    """
    Args:
         traffic_light (TrafficLight): Объект светофора.
    Returns:
        str: Текущий цвет светофора.

    Raises:
        AttributeError: Если передан неверный тип объекта.
    """
    try:
        return traffic_light.get_color()
    except AttributeError as ex:
       raise AttributeError(f"Invalid traffic_light object: {ex}") from ex
```

### `switch_signal`

**Описание**:
Переключает цвет светофора.

**Параметры**:
- `traffic_light` (TrafficLight): Объект светофора.

**Возвращает**:
- `str`: Новый цвет светофора.

**Вызывает исключения**:
- `AttributeError`: Если передан неверный тип объекта, вызовется исключение.

```python
def switch_signal(traffic_light: TrafficLight) -> str:
    """
    Args:
        traffic_light (TrafficLight): Объект светофора.

    Returns:
         str: Новый цвет светофора.

    Raises:
        AttributeError: Если передан неверный тип объекта.
    """
    try:
        return traffic_light.switch_color()
    except AttributeError as ex:
         raise AttributeError(f"Invalid traffic_light object: {ex}") from ex
```