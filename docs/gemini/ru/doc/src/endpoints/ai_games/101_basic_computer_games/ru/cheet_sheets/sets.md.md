# Множества в Python

## Обзор

Этот документ описывает работу с множествами (наборами) в Python, включая их создание, основные операции и примеры использования. Множества представляют собой неупорядоченные коллекции уникальных элементов.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`create_fruit_set`](#create_fruit_set)
  - [`display_set`](#display_set)
- [Примеры использования](#примеры-использования)
- [Задания для закрепления](#задания-для-закрепления)

## Функции

### `create_fruit_set`

**Описание**: Создает множество фруктов из строки.

**Параметры**:
- `fruit_string` (str): Строка с фруктами (🍎, 🍐, 🍉, 🧺).

**Возвращает**:
- `Set[str]`: Множество уникальных фруктов.

**Вызывает исключения**:
- `ValueError`: Если строка содержит символы, отличные от 🍎, 🍐, 🍉, 🧺.

### `display_set`

**Описание**: Преобразует множество фруктов в строку для отображения.

**Параметры**:
- `fruit_set` (Set[str]): Множество фруктов.

**Возвращает**:
- `str`: Строка для отображения.

## Примеры использования

```python
from typing import Set

def create_fruit_set(fruit_string: str) -> Set[str]:
    """
    Создает множество фруктов из строки.

    Args:
        fruit_string: Строка с фруктами (🍎, 🍐, 🍉, 🧺).

    Returns:
        Множество уникальных фруктов.
    """
    if not all(fruit in ["🍎", "🍐", "🍉", "🧺"] for fruit in fruit_string):
        raise ValueError("Строка может содержать только символы 🍎, 🍐, 🍉, 🧺")
    return set(fruit_string)  # Используем set() для создания множества

def display_set(fruit_set: Set[str]) -> str:
  """
  Преобразует множество фруктов в строку для отображения.

    Args:
        fruit_set: Множество фруктов.

    Returns:
        Строка для отображения.
  """
  return "{" + ", ".join(fruit_set) + "}"


# Создаем множества фруктов
fruits_set_A = create_fruit_set("🍎🍐")  # Множество A: {🍎, 🍐}
fruits_set_B = create_fruit_set("🍐🍉")  # Множество B: {🍐, 🍉}
fruits_set_C = create_fruit_set("🍎🍐🍉")  # Множество C: {🍎, 🍐, 🍉}
fruits_set_D = create_fruit_set("🧺")  # Множество D: {🧺}

# Выводим множества
print(f"Множество A: {display_set(fruits_set_A)}")
print(f"Множество B: {display_set(fruits_set_B)}")
print(f"Множество C: {display_set(fruits_set_C)}")
print(f"Множество D: {display_set(fruits_set_D)}")

# Объединение множеств (Union)
union_result = fruits_set_A | fruits_set_B
print(f"A ∪ B: {display_set(union_result)}")  # Результат: {🍎, 🍐, 🍉}

# Пересечение множеств (Intersection)
intersection_result = fruits_set_A & fruits_set_B
print(f"A ∩ B: {display_set(intersection_result)}")  # Результат: {🍐}

# Разность множеств (Difference)
difference_result_AB = fruits_set_A - fruits_set_B
print(f"A - B: {display_set(difference_result_AB)}")  # Результат: {🍎}
difference_result_BA = fruits_set_B - fruits_set_A
print(f"B - A: {display_set(difference_result_BA)}")  # Результат: {🍉}

# Симметричная разность множеств (Symmetric Difference)
symmetric_difference_result = fruits_set_A ^ fruits_set_B
print(f"A ^ B: {display_set(symmetric_difference_result)}")  # Результат: {🍎, 🍉}

# Подмножество (Subset)
subset_result1 = fruits_set_A <= fruits_set_C
print(f"A <= C: {subset_result1}")  # Результат: True (A подмножество C)
subset_result2 = fruits_set_A <= fruits_set_B
print(f"A <= B: {subset_result2}") # Результат: False (A не подмножество B)

# Надмножество (Superset)
superset_result1 = fruits_set_C >= fruits_set_A
print(f"C >= A: {superset_result1}")  # Результат: True (C надмножество A)
superset_result2 = fruits_set_B >= fruits_set_A
print(f"B >= A: {superset_result2}")  # Результат: False (B не надмножество A)

# Проверка на наличие элемента
print(f"🍎 in A: {'🍎' in fruits_set_A}")  # Результат: True
print(f"🍉 in A: {'🍉' in fruits_set_A}")  # Результат: False

```
*   **`create_fruit_set(fruit_string)`:** Эта функция создает множество из строки с фруктами.
    *   `set(fruit_string)` превращает строку в множество, убирая дубликаты и делая порядок элементов неважным.
    *   Мы проверяем что строка состоит только из разрешенных символов юникода.
*   **`display_set(fruit_set)`:** Эта функция используется для преобразования множества в читаемую строку для вывода.
*   **Примеры:** Мы создаем несколько множеств и применяем различные операции над ними. Результаты каждой операции выводятся на экран.

## Задания для закрепления

1.  Создай свои собственные множества фруктов и попробуй все операции над ними.
2.  Реализуй функцию `is_disjoint(set1, set2)`, которая будет проверять, являются ли два множества непересекающимися (пересечение = пустое множество).
3.  Реализуй функцию `power_set(fruit_set)`, которая будет возвращать множество всех подмножеств заданного множества.
4.  Попробуй применить множества для решения реальной задачи. Например, у тебя есть два списка гостей на вечеринку, найди гостей, которые есть в обоих списках, гостей, которые есть только в первом списке и т.д.