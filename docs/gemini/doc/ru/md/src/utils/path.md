# Модуль `hypotez/src/utils/path.py`

## Обзор

Модуль `hypotez/src/utils/path.py` определяет корневой путь к проекту. Все импорты строятся относительно этого пути.

## Функции

### `get_relative_path`

**Описание**: Возвращает часть пути начиная с указанного сегмента и до конца.

**Параметры**:
- `full_path` (str): Полный путь.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение.

**Возвращает**:
- `Optional[str]`: Относительный путь начиная с `relative_from`, или `None`, если сегмент не найден.

**Описание реализации**:
Функция принимает полный путь и сегмент пути `relative_from` в качестве входных данных. Она преобразует строки в объекты `Path` для работы с путями. Далее, находит индекс сегмента `relative_from` в списке частей пути. Если сегмент найден, функция формирует новый путь, начиная с этого сегмента, и возвращает его в формате строки (`as_posix()`). В противном случае, функция возвращает `None`.


**Примеры использования**:

```python
full_path = "/home/user/project/data/file.txt"
relative_from = "data"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: file.txt

full_path = "/home/user/project/data/file.txt"
relative_from = "not_exist"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None

```