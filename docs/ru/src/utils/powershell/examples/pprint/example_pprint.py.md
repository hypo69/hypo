# Модуль example_pprint

## Обзор

Модуль `example_pprint.py` демонстрирует использование функций `pprint` из стандартной библиотеки `pprint` и модуля `src.printer` для форматированного вывода данных.

## Подробней

Этот модуль предназначен для демонстрации возможностей форматированного вывода данных в Python. Он импортирует функцию `pprint` из стандартной библиотеки и переименовывает её в `pretty_print`, а также импортирует функцию `pprint` из модуля `src.printer`. Затем он использует функцию `pprint` для вывода строки "Hello, world!".

## Функции

### `pprint`

```python
from pprint import pprint as pretty_print
from src.printer import pprint
```

**Назначение**: Функция `pprint` используется для форматированного вывода данных. В данном модуле используются две версии этой функции: одна из стандартной библиотеки `pprint` (переименованная в `pretty_print`) и другая из модуля `src.printer`.

**Как работает функция**:
1. Импортирует функцию `pprint` из стандартной библиотеки `pprint` и переименовывает ее в `pretty_print`.
2. Импортирует функцию `pprint` из модуля `src.printer`.
3. Выводит строку "Hello, world!" с использованием функции `pprint` из модуля `src.printer`.

```
Импорт pprint из стандартной библиотеки и src.printer
↓
Вывод "Hello, world!" с использованием pprint из src.printer
```
**Примеры**:
```python
from src.printer import pprint
pprint("Hello, world!")