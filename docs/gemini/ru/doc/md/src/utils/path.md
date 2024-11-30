# Модуль hypotez/src/utils/path.py

## Обзор

Модуль `path` определяет корневой путь к проекту `hypotez`. Все импорты строятся относительно этого пути.  В дальнейшем планируется перенести определение пути в системную переменную.

## Переменные

### `MODE`

**Тип**: str

**Значение**: 'dev'

**Описание**:  Текущий режим работы. В данном случае 'dev'.


## Функции

### `get_relative_path`

**Описание**: Возвращает относительный путь от заданного сегмента до конца полного пути.

**Параметры**:
- `full_path` (str): Полный путь, из которого нужно получить относительный путь.
- `relative_from` (str): Сегмент пути, относительно которого нужно вычислить относительный путь.

**Возвращает**:
- `Optional[str]`: Относительный путь начиная с `relative_from`. Возвращает `None`, если сегмент `relative_from` не найден в `full_path`.

**Примеры использования**:

```python
full_path = "/home/user/project/hypotez/src/data/file.txt"
relative_from = "hypotez/src"

relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: data/file.txt


full_path = "/home/user/project/hypotez/src/data/file.txt"
relative_from = "not_found"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path) # Вывод: None

```


**Обрабатываемые исключения**:
- Нет обрабатываемых исключений.
```