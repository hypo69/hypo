# Модуль test_absolute_paths

## Обзор

Модуль `test_absolute_paths.py` содержит тесты для проверки корректности установки абсолютных путей в классе `Supplier`. Он использует библиотеку `unittest` для организации тестовых случаев и проверяет различные сценарии формирования путей на основе префиксов и имен файлов.

## Подробней

Этот модуль важен для обеспечения правильной работы класса `Supplier`, поскольку он гарантирует, что пути к файлам, формируемые этим классом, являются абсолютными и корректными. Тесты охватывают разные варианты использования, такие как передача префикса в виде строки или списка, а также обработку случаев, когда имена файлов отсутствуют.

## Классы

### `TestSetAbsolutePaths`

**Описание**: Класс `TestSetAbsolutePaths` является тестовым классом, который содержит набор тестов для метода `set_absolute_paths` класса `Supplier`.

**Как работает класс**:
1.  В методе `setUp` определяется абсолютный путь к поставщику (`supplier_abs_path`) и сохраняется ссылка на тестируемую функцию `set_absolute_paths`.
2.  Далее идут тестовые методы, каждый из которых проверяет определенный сценарий работы функции `set_absolute_paths`.

**Методы**:

*   `setUp`: Подготавливает тестовое окружение, определяя `supplier_abs_path` и функцию для тестирования.
*   `test_single_filename_with_prefix_as_string`: Тест проверяет случай, когда передается один файл и префикс в виде строки.
*   `test_single_filename_with_prefix_as_list`: Тест проверяет случай, когда передается один файл и префикс в виде списка.
*   `test_multiple_filenames_with_prefix_as_string`: Тест проверяет случай, когда передается несколько файлов и префикс в виде строки.
*   `test_multiple_filenames_with_prefix_as_list`: Тест проверяет случай, когда передается несколько файлов и префикс в виде списка.
*   `test_no_related_filenames_with_prefix_as_string`: Тест проверяет случай, когда не передаются имена файлов, а префикс задан строкой.
*   `test_no_related_filenames_with_prefix_as_list`: Тест проверяет случай, когда не передаются имена файлов, а префикс задан списком.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.
*   `supplier_abs_path` (str): Абсолютный путь к поставщику.
*   `function` (Callable): Ссылка на метод `set_absolute_paths` класса `Supplier`.
*   `prefix` (str | list[str]): Префикс пути. Может быть строкой или списком строк.
*   `related_filenames` (str | list[str] | None): Имя файла или список имен файлов. Может быть `None`.
*   `expected_result` (Path | list[Path]): Ожидаемый результат работы функции.
*   `result` (Path | list[Path]): Фактический результат работы функции.

## Функции

### `setUp`

```python
def setUp(self):
    self.supplier_abs_path = '/path/to/supplier'
    self.function = Supplier().set_absolute_paths
```

**Описание**: Метод `setUp` используется для подготовки тестового окружения перед каждым тестом.

**Как работает функция**:

1.  Определяет значение `self.supplier_abs_path` как строку '/path/to/supplier', представляющую абсолютный путь к поставщику.
2.  Получает ссылку на метод `set_absolute_paths` класса `Supplier` и сохраняет её в `self.function`. Это делается путем создания экземпляра класса `Supplier` и доступа к его методу `set_absolute_paths`.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.

### `test_single_filename_with_prefix_as_string`

```python
def test_single_filename_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = 'file.txt'
    expected_result = Path(self.supplier_abs_path, prefix, related_filenames)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Описание**: Тест проверяет случай, когда передается один файл и префикс в виде строки.

**Как работает функция**:

1.  Определяет `prefix` как строку 'subfolder'.
2.  Определяет `related_filenames` как строку 'file.txt'.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path`, `prefix` и `related_filenames`.
4.  Вызывает тестируемую функцию `self.function` с параметрами `prefix` и `related_filenames`, сохраняя результат в `result`.
5.  Использует `self.assertEqual` для сравнения `result` и `expected_result`, проверяя, что результаты совпадают.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.

### `test_single_filename_with_prefix_as_list`

```python
def test_single_filename_with_prefix_as_list(self):
    prefix = ['subfolder', 'subsubfolder']
    related_filenames = 'file.txt'
    expected_result = Path(self.supplier_abs_path, *prefix, related_filenames)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Описание**: Тест проверяет случай, когда передается один файл и префикс в виде списка.

**Как работает функция**:

1.  Определяет `prefix` как список строк `['subfolder', 'subsubfolder']`.
2.  Определяет `related_filenames` как строку 'file.txt'.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path`, распакованный `prefix` и `related_filenames`.
4.  Вызывает тестируемую функцию `self.function` с параметрами `prefix` и `related_filenames`, сохраняя результат в `result`.
5.  Использует `self.assertEqual` для сравнения `result` и `expected_result`, проверяя, что результаты совпадают.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.

### `test_multiple_filenames_with_prefix_as_string`

```python
def test_multiple_filenames_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_result = [
        Path(self.supplier_abs_path, prefix, filename)
        for filename in related_filenames
    ]

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Описание**: Тест проверяет случай, когда передается несколько файлов и префикс в виде строки.

**Как работает функция**:

1.  Определяет `prefix` как строку 'subfolder'.
2.  Определяет `related_filenames` как список строк `['file1.txt', 'file2.txt', 'file3.txt']`.
3.  Формирует ожидаемый результат `expected_result` как список объектов `Path`, объединяя `self.supplier_abs_path`, `prefix` и каждый элемент из `related_filenames`.
4.  Вызывает тестируемую функцию `self.function` с параметрами `prefix` и `related_filenames`, сохраняя результат в `result`.
5.  Использует `self.assertEqual` для сравнения `result` и `expected_result`, проверяя, что результаты совпадают.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.

### `test_multiple_filenames_with_prefix_as_list`

```python
def test_multiple_filenames_with_prefix_as_list(self):
    prefix = ['subfolder', 'subsubfolder']
    related_filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_result = [
        Path(self.supplier_abs_path, *prefix, filename)
        for filename in related_filenames
    ]

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Описание**: Тест проверяет случай, когда передается несколько файлов и префикс в виде списка.

**Как работает функция**:

1.  Определяет `prefix` как список строк `['subfolder', 'subsubfolder']`.
2.  Определяет `related_filenames` как список строк `['file1.txt', 'file2.txt', 'file3.txt']`.
3.  Формирует ожидаемый результат `expected_result` как список объектов `Path`, объединяя `self.supplier_abs_path`, распакованный `prefix` и каждый элемент из `related_filenames`.
4.  Вызывает тестируемую функцию `self.function` с параметрами `prefix` и `related_filenames`, сохраняя результат в `result`.
5.  Использует `self.assertEqual` для сравнения `result` и `expected_result`, проверяя, что результаты совпадают.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.

### `test_no_related_filenames_with_prefix_as_string`

```python
def test_no_related_filenames_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = None
    expected_result = Path(self.supplier_abs_path, prefix)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Описание**: Тест проверяет случай, когда не передаются имена файлов, а префикс задан строкой.

**Как работает функция**:

1.  Определяет `prefix` как строку 'subfolder'.
2.  Определяет `related_filenames` как `None`.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path` и `prefix`.
4.  Вызывает тестируемую функцию `self.function` с параметрами `prefix` и `related_filenames`, сохраняя результат в `result`.
5.  Использует `self.assertEqual` для сравнения `result` и `expected_result`, проверяя, что результаты совпадают.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.

### `test_no_related_filenames_with_prefix_as_list`

```python
def test_no_related_filenames_with_prefix_as_list(self):
    prefix = ['subfolder', 'subsubfolder']
    related_filenames = None
    expected_result = Path(self.supplier_abs_path, *prefix)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Описание**: Тест проверяет случай, когда не передаются имена файлов, а префикс задан списком.

**Как работает функция**:

1.  Определяет `prefix` как список строк `['subfolder', 'subsubfolder']`.
2.  Определяет `related_filenames` как `None`.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path` и распакованный `prefix`.
4.  Вызывает тестируемую функцию `self.function` с параметрами `prefix` и `related_filenames`, сохраняя результат в `result`.
5.  Использует `self.assertEqual` для сравнения `result` и `expected_result`, проверяя, что результаты совпадают.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `TestSetAbsolutePaths`.