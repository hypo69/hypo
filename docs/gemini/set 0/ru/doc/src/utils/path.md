# Модуль hypotez/src/utils/path.py

## Обзор

Модуль `src.utils.path` определяет корневой путь к проекту.  Все импорты строятся относительно этого пути. В будущем планируется перенести определение пути в системные переменные.

## Функции

### `get_relative_path`

**Описание**: Возвращает часть пути, начиная с указанного сегмента и до конца.

**Параметры**:
- `full_path` (str): Полный путь.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение.


**Возвращает**:
- `Optional[str]`: Относительный путь начиная с `relative_from`, или `None`, если сегмент не найден.


**Пример использования**:

```python
full_path = "/home/user/project/data/file.txt"
relative_from = "data"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: file.txt
```

**Примечания**:

Функция преобразует входные строки в объекты `Path` для корректной обработки путей.

**Возможные исключения**:
- Не обнаружен указанный фрагмент пути.

```
```python
def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    Args:
        full_path (str): Полный путь.
        relative_from (str): Сегмент пути, с которого нужно начать извлечение.

    Returns:
        Optional[str]: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    """
    # Преобразуем строки в объекты Path
    path = Path(full_path)
    parts = path.parts

    # Находим индекс сегмента relative_from
    if relative_from in parts:
        start_index = parts.index(relative_from)
        # Формируем путь начиная с указанного сегмента
        relative_path = Path(*parts[start_index:])
        return relative_path.as_posix()
    else:
        return None
```
```
## Константы

### `MODE`

**Описание**: Текущий режим работы. На данный момент установлено значение 'dev'.


```
```python
MODE = 'dev'
```
```