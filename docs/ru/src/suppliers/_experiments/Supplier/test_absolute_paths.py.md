# Модуль `test_absolute_paths`

## Обзор

Модуль `test_absolute_paths.py` содержит тесты для функции `set_absolute_paths` класса `Supplier`.
Он проверяет правильность формирования абсолютных путей на основе предоставленных префиксов и имен файлов.

## Подробней

Этот модуль использует библиотеку `unittest` для автоматизированного тестирования.
Он создает тестовые случаи, которые охватывают различные сценарии использования функции `set_absolute_paths`,
включая случаи с строковыми префиксами, списочными префиксами, одним файлом, несколькими файлами и отсутствием файлов.

## Классы

### `TestSetAbsolutePaths`

**Описание**: Класс `TestSetAbsolutePaths` наследуется от `unittest.TestCase` и содержит набор тестов для функции `set_absolute_paths`.

**Как работает класс**:

1.  В методе `setUp` определяется `supplier_abs_path` как `/path/to/supplier` (абсолютный путь к поставщику) и `function` как метод `set_absolute_paths` экземпляра класса `Supplier`.
2.  Каждый метод `test_*` выполняет проверку функции `set_absolute_paths` с разными входными данными.
3.  В каждом тестовом методе вызывается функция `set_absolute_paths` с определенными параметрами и сравнивается полученный результат с ожидаемым с использованием метода `assertEqual`.

**Методы**:

*   `setUp`: Подготавливает тестовую среду, инициализируя `supplier_abs_path` и `function`.
*   `test_single_filename_with_prefix_as_string`: Тестирует случай, когда префикс задан строкой и передано одно имя файла.
*   `test_single_filename_with_prefix_as_list`: Тестирует случай, когда префикс задан списком и передано одно имя файла.
*   `test_multiple_filenames_with_prefix_as_string`: Тестирует случай, когда префикс задан строкой и передано несколько имен файлов.
*   `test_multiple_filenames_with_prefix_as_list`: Тестирует случай, когда префикс задан списком и передано несколько имен файлов.
*   `test_no_related_filenames_with_prefix_as_string`: Тестирует случай, когда префикс задан строкой и имена файлов отсутствуют.
*   `test_no_related_filenames_with_prefix_as_list`: Тестирует случай, когда префикс задан списком и имена файлов отсутствуют.

## Функции

### `setUp`

```python
def setUp(self):
    """
    Подготавливает тестовую среду перед каждым тестом.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None

    """
    ...
```

**Назначение**: Инициализирует атрибуты `supplier_abs_path` (абсолютный путь к поставщику) и `function` (метод `set_absolute_paths` класса `Supplier`) перед каждым тестовым случаем.

**Как работает функция**:

1.  `self.supplier_abs_path` устанавливается в строковое значение '/path/to/supplier', представляющее собой базовый путь для формирования абсолютных путей.
2.  `self.function` устанавливается как метод `set_absolute_paths` экземпляра класса `Supplier`. Это позволяет вызывать тестируемую функцию напрямую через `self.function`.

### `test_single_filename_with_prefix_as_string`

```python
def test_single_filename_with_prefix_as_string(self):
    """
    Тестирует функцию set_absolute_paths с префиксом в виде строки и одним именем файла.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `set_absolute_paths` правильно формирует абсолютный путь, когда префикс задан строкой, и передается одно имя файла.

**Как работает функция**:

1.  Определяется префикс `prefix` как строка 'subfolder'.
2.  Определяется имя файла `related_filenames` как строка 'file.txt'.
3.  Вычисляется ожидаемый результат `expected_result` с использованием `Path` из библиотеки `pathlib`, объединяя `self.supplier_abs_path`, `prefix` и `related_filenames`.
4.  Вызывается функция `self.function` с параметрами `prefix` и `related_filenames`, результат сохраняется в переменной `result`.
5.  Сравнивается `result` и `expected_result` с использованием `self.assertEqual`.

### `test_single_filename_with_prefix_as_list`

```python
def test_single_filename_with_prefix_as_list(self):
    """
    Тестирует функцию set_absolute_paths с префиксом в виде списка и одним именем файла.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `set_absolute_paths` правильно формирует абсолютный путь, когда префикс задан списком, и передается одно имя файла.

**Как работает функция**:

1.  Определяется префикс `prefix` как список строк \['subfolder', 'subsubfolder'].
2.  Определяется имя файла `related_filenames` как строка 'file.txt'.
3.  Вычисляется ожидаемый результат `expected_result` с использованием `Path` из библиотеки `pathlib`, объединяя `self.supplier_abs_path`, элементы списка `prefix` (распакованные с помощью `*prefix`) и `related_filenames`.
4.  Вызывается функция `self.function` с параметрами `prefix` и `related_filenames`, результат сохраняется в переменной `result`.
5.  Сравнивается `result` и `expected_result` с использованием `self.assertEqual`.

### `test_multiple_filenames_with_prefix_as_string`

```python
def test_multiple_filenames_with_prefix_as_string(self):
    """
    Тестирует функцию set_absolute_paths с префиксом в виде строки и списком имен файлов.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `set_absolute_paths` правильно формирует абсолютные пути для списка файлов, когда префикс задан строкой.

**Как работает функция**:

1.  Определяется префикс `prefix` как строка 'subfolder'.
2.  Определяется список имен файлов `related_filenames` как \['file1.txt', 'file2.txt', 'file3.txt'].
3.  Вычисляется ожидаемый результат `expected_result` как список объектов `Path`, где каждый объект представляет собой объединение `self.supplier_abs_path`, `prefix` и соответствующего имени файла из списка `related_filenames`.
4.  Вызывается функция `self.function` с параметрами `prefix` и `related_filenames`, результат сохраняется в переменной `result`.
5.  Сравнивается `result` и `expected_result` с использованием `self.assertEqual`.

### `test_multiple_filenames_with_prefix_as_list`

```python
def test_multiple_filenames_with_prefix_as_list(self):
    """
    Тестирует функцию set_absolute_paths с префиксом в виде списка и списком имен файлов.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `set_absolute_paths` правильно формирует абсолютные пути для списка файлов, когда префикс задан списком.

**Как работает функция**:

1.  Определяется префикс `prefix` как список строк \['subfolder', 'subsubfolder'].
2.  Определяется список имен файлов `related_filenames` как \['file1.txt', 'file2.txt', 'file3.txt'].
3.  Вычисляется ожидаемый результат `expected_result` как список объектов `Path`, где каждый объект представляет собой объединение `self.supplier_abs_path`, элементов списка `prefix` (распакованных с помощью `*prefix`) и соответствующего имени файла из списка `related_filenames`.
4.  Вызывается функция `self.function` с параметрами `prefix` и `related_filenames`, результат сохраняется в переменной `result`.
5.  Сравнивается `result` и `expected_result` с использованием `self.assertEqual`.

### `test_no_related_filenames_with_prefix_as_string`

```python
def test_no_related_filenames_with_prefix_as_string(self):
    """
    Тестирует функцию set_absolute_paths с префиксом в виде строки и отсутствием имен файлов.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `set_absolute_paths` правильно формирует абсолютный путь, когда префикс задан строкой, и имена файлов не переданы (None).

**Как работает функция**:

1.  Определяется префикс `prefix` как строка 'subfolder'.
2.  `related_filenames` устанавливается в `None`, что означает отсутствие имен файлов.
3.  Вычисляется ожидаемый результат `expected_result` с использованием `Path` из библиотеки `pathlib`, объединяя `self.supplier_abs_path` и `prefix`.
4.  Вызывается функция `self.function` с параметрами `prefix` и `related_filenames`, результат сохраняется в переменной `result`.
5.  Сравнивается `result` и `expected_result` с использованием `self.assertEqual`.

### `test_no_related_filenames_with_prefix_as_list`

```python
def test_no_related_filenames_with_prefix_as_list(self):
    """
    Тестирует функцию set_absolute_paths с префиксом в виде списка и отсутствием имен файлов.

    Args:
        self (TestSetAbsolutePaths): Экземпляр класса TestSetAbsolutePaths.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `set_absolute_paths` правильно формирует абсолютный путь, когда префикс задан списком, и имена файлов не переданы (None).

**Как работает функция**:

1.  Определяется префикс `prefix` как список строк \['subfolder', 'subsubfolder'].
2.  `related_filenames` устанавливается в `None`, что означает отсутствие имен файлов.
3.  Вычисляется ожидаемый результат `expected_result` с использованием `Path` из библиотеки `pathlib`, объединяя `self.supplier_abs_path` и элементы списка `prefix` (распакованные с помощью `*prefix`).
4.  Вызывается функция `self.function` с параметрами `prefix` и `related_filenames`, результат сохраняется в переменной `result`.
5.  Сравнивается `result` и `expected_result` с использованием `self.assertEqual`.