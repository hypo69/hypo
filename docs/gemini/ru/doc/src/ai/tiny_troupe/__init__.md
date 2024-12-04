# Модуль tiny_troupe

## Обзор

Данный модуль предоставляет инструменты для работы с небольшой командой (troupe) искусственного интеллекта.  Подробности, включая ссылки на первоисточники, можно найти в комментариях.

## Оглавление

- [Модуль tiny_troupe](#модуль-tiny_troupe)
- [Обзор](#обзор)
- [Функции](#функции)


## Функции

### `get_team_size`

**Описание**: Возвращает размер команды.

**Параметры**:
- Не принимает входных параметров.

**Возвращает**:
- `int`: Размер команды.

**Вызывает исключения**:
-  Не вызывает исключения.


```
```python
def get_team_size() -> int:
    """
    Возвращает размер команды.

    Returns:
        int: Размер команды.
    """
    return 5
```


### `assign_tasks(tasks: list, team_size: int) -> dict | None`

**Описание**: Распределяет задачи между членами команды.

**Параметры**:
- `tasks` (list): Список задач.
- `team_size` (int): Размер команды.

**Возвращает**:
- `dict | None`: Словарь с распределением задач, где ключи - имена членов команды, а значения - списки задач, или `None`, если входные данные некорректны.

**Вызывает исключения**:
- `ValueError`: Если размер команды меньше 1 или если задачи не являются списком.


```python
def assign_tasks(tasks: list, team_size: int) -> dict | None:
    """
    Распределяет задачи между членами команды.

    Args:
        tasks (list): Список задач.
        team_size (int): Размер команды.

    Returns:
        dict | None: Словарь с распределением задач, или None, если входные данные некорректны.

    Raises:
        ValueError: Если размер команды меньше 1 или задачи не являются списком.
    """
    if not isinstance(tasks, list):
        raise ValueError("Задачи должны быть списком")
    if team_size < 1:
        raise ValueError("Размер команды должен быть не меньше 1")

    team_members = ["Агент" + str(i) for i in range(team_size)]
    task_per_member = len(tasks) // team_size
    remaining_tasks = len(tasks) % team_size

    task_assignment = {}
    start_index = 0
    for member in team_members:
        end_index = start_index + task_per_member
        if remaining_tasks > 0:
            end_index += 1
            remaining_tasks -= 1
        task_assignment[member] = tasks[start_index:end_index]
        start_index = end_index

    return task_assignment
```