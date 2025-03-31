# Модуль `get_images`

## Обзор

Модуль `get_images` предназначен для получения списка изображений, сгенерированных искусственным интеллектом и расположенных в указанной директории. Он использует различные утилиты для поиска файлов и вывода информации.

## Подробней

Этот модуль является частью экспериментов Kazarinov и предназначен для работы с изображениями, полученными в результате конвертации и обработки. Он использует функции для рекурсивного поиска файлов изображений в заданной директории и вывода списка найденных файлов.

## Функции

### `recursively_get_filepath`

```python
def recursively_get_filepath(
    dir_path: str | Path,
    patterns: list[str]
) -> list[Path]:
    """
    Рекурсивно получает список путей к файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        dir_path (str | Path): Путь к директории для поиска файлов.
        patterns (list[str]): Список шаблонов файлов для поиска (например, ['*.jpeg', '*.jpg', '*.png']).

    Returns:
        list[Path]: Список объектов `Path`, представляющих пути к найденным файлам.
    """
```

**Как работает функция**:
Функция `recursively_get_filepath` принимает путь к директории и список шаблонов файлов. Она рекурсивно проходит по указанной директории и всем её поддиректориям, собирая пути ко всем файлам, имена которых соответствуют одному из предоставленных шаблонов.
- Принимает `dir_path` как путь к директории, где будет производиться поиск файлов.
- Принимает `patterns` как список шаблонов, которым должны соответствовать имена файлов.
- Возвращает список объектов `Path`, представляющих пути ко всем найденным файлам, соответствующим заданным шаблонам.

**Параметры**:
- `dir_path` (str | Path): Путь к директории для поиска файлов.
- `patterns` (list[str]): Список шаблонов файлов для поиска (например, `['*.jpeg', '*.jpg', '*.png']`).

**Возвращает**:
- `list[Path]`: Список объектов `Path`, представляющих пути к найденным файлам.

**Примеры**:

```python
from pathlib import Path
from src.utils.file import recursively_get_filepath

dir_path = Path('./images')
patterns = ['*.jpeg', '*.jpg']
image_paths = recursively_get_filepath(dir_path, patterns)
print(image_paths)
```

### `pprint`

```python
def pprint(
    obj: Any,
    color: Optional[str] = None,
    label: str = ''
) -> None:
    """
    Выводит объект в консоль с возможностью добавления цвета и метки.

    Args:
        obj (Any): Объект для вывода.
        color (Optional[str], optional): Цвет текста для вывода. Доступные цвета: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'. По умолчанию `None`.
        label (str, optional): Метка для вывода перед объектом. По умолчанию ''.
    """
```

**Как работает функция**:
Функция `pprint` выводит в консоль переданный объект с возможностью добавления цвета и метки. Это удобная утилита для отладки и логирования данных.
- Принимает `obj` как объект, который необходимо вывести в консоль.
- Принимает `color` как необязательный параметр, определяющий цвет текста при выводе.
- Принимает `label` как необязательную метку, которая будет выведена перед объектом.

**Параметры**:
- `obj` (Any): Объект для вывода.
- `color` (Optional[str], optional): Цвет текста для вывода. По умолчанию `None`.
- `label` (str, optional): Метка для вывода перед объектом. По умолчанию ''.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Примеры**:

```python
from src.utils.printer import pprint

data = {'name': 'example', 'value': 123}
pprint(data, color='green', label='Data:')
```
```python
from pathlib import Path
from src import gs
from src.utils.file import read_text_file, save_text_file, recursively_get_filepath
from src.utils.printer import pprint

images_path = recursively_get_filepath(gs.path.external_data / 'kazarinov' / 'converted_images' / 'pastel', ['*.jpeg','*.jpg','*.png'])
pprint(images_path)