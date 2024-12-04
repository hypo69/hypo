# Модуль hypotez/src/_examples/get_relative_path.py

## Обзор

Этот модуль демонстрирует использование функции `get_relative_path` для получения относительного пути к директории. Он использует абсолютный путь к текущему файлу и искомую директорию 'hypotez'. Результат выводится на консоль.

## Функции

### `get_relative_path`

**Описание**: Функция `get_relative_path` возвращает относительный путь к целевой папке, относительно исходного пути.

**Параметры**:

- `base_path` (Path): Абсолютный путь к исходной директории.
- `target_path` (str): Имя целевой директории.

**Возвращает**:

- `Path`: Относительный путь к целевой директории, либо None, если путь не может быть сформирован.

**Вызывает исключения**:

- Нет.

## Использование

```python
from pathlib import Path
from src.utils.path import get_relative_path

# Пример использования (изнутри файла get_relative_path.py)
relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)
```

**Пример вывода**:

```
../../hypotez
```

**Примечание**:  В примере предполагается, что директория `hypotez` находится над директорией, где находится файл `get_relative_path.py`. Вывод может изменяться в зависимости от фактического расположения файлов.


```python
# Остальной код (используемый в примере).
MODE = 'dev'
import header
from src.utils.path import get_relative_path

relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)
```
```