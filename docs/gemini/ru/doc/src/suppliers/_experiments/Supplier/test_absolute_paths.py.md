# Модуль `test_absolute_paths`

## Обзор

Модуль `test_absolute_paths` предназначен для тестирования функции `set_absolute_paths` класса `Supplier`. Он содержит набор тестов, проверяющих правильность формирования абсолютных путей на основе предоставленных префиксов и имен файлов.

## Подробнее

Модуль использует библиотеку `unittest` для организации и запуска тестов. Каждый тестовый метод проверяет определенный сценарий использования функции `set_absolute_paths`, сравнивая полученный результат с ожидаемым.

## Классы

### `TestSetAbsolutePaths`

**Описание**: Класс `TestSetAbsolutePaths` содержит набор тестов для проверки функции `set_absolute_paths` класса `Supplier`.

**Наследует**:
- `unittest.TestCase`: Класс наследует `unittest.TestCase`, предоставляя методы для определения и запуска тестов.

**Атрибуты**:
- `supplier_abs_path` (str): Абсолютный путь к директории поставщика.
- `function` (Callable): Ссылка на функцию `set_absolute_paths` класса `Supplier`, которая будет тестироваться.

**Методы**:

- `setUp()`: Метод, выполняющийся перед каждым тестом. Инициализирует `supplier_abs_path` и получает ссылку на функцию `set_absolute_paths`.
- `test_single_filename_with_prefix_as_string()`: Тест проверяет случай, когда передается один файл и префикс в виде строки.
- `test_single_filename_with_prefix_as_list()`: Тест проверяет случай, когда передается один файл и префикс в виде списка.
- `test_multiple_filenames_with_prefix_as_string()`: Тест проверяет случай, когда передается несколько файлов и префикс в виде строки.
- `test_multiple_filenames_with_prefix_as_list()`: Тест проверяет случай, когда передается несколько файлов и префикс в виде списка.
- `test_no_related_filenames_with_prefix_as_string()`: Тест проверяет случай, когда не передаются имена файлов, а префикс передан в виде строки.
- `test_no_related_filenames_with_prefix_as_list()`: Тест проверяет случай, когда не передаются имена файлов, а префикс передан в виде списка.

### `setUp`

```python
def setUp(self):
    self.supplier_abs_path = '/path/to/supplier'
    self.function = Supplier().set_absolute_paths
```

**Назначение**: Подготовка к каждому тесту.

**Как работает функция**:
1. Инициализирует атрибут `self.supplier_abs_path` абсолютным путем к директории поставщика (в данном случае `/path/to/supplier`).
2. Получает ссылку на функцию `set_absolute_paths` экземпляра класса `Supplier` и сохраняет её в атрибуте `self.function`.

### `test_single_filename_with_prefix_as_string`

```python
def test_single_filename_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = 'file.txt'
    expected_result = Path(self.supplier_abs_path, prefix, related_filenames)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Назначение**: Тестирование формирования абсолютного пути с одним именем файла и префиксом в виде строки.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Как работает функция**:

1. Определяет `prefix` как строку `'subfolder'`.
2. Определяет `related_filenames` как строку `'file.txt'`.
3. Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path`, `prefix` и `related_filenames`.
4. Вызывает тестируемую функцию `self.function` с аргументами `prefix` и `related_filenames`, сохраняя результат в `result`.
5. Сравнивает полученный `result` с ожидаемым `expected_result` с помощью метода `assertEqual`.

**Примеры**:

```python
# Пример вызова
test_instance = TestSetAbsolutePaths()
test_instance.setUp()
test_instance.test_single_filename_with_prefix_as_string()
```

### `test_single_filename_with_prefix_as_list`

```python
def test_single_filename_with_prefix_as_list(self):
    prefix = ['subfolder', 'subsubfolder']
    related_filenames = 'file.txt'
    expected_result = Path(self.supplier_abs_path, *prefix, related_filenames)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Назначение**: Тестирование формирования абсолютного пути с одним именем файла и префиксом в виде списка.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Как работает функция**:

1. Определяет `prefix` как список строк `['subfolder', 'subsubfolder']`.
2. Определяет `related_filenames` как строку `'file.txt'`.
3. Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path`, элементы списка `prefix` (распакованные через `*prefix`) и `related_filenames`.
4. Вызывает тестируемую функцию `self.function` с аргументами `prefix` и `related_filenames`, сохраняя результат в `result`.
5. Сравнивает полученный `result` с ожидаемым `expected_result` с помощью метода `assertEqual`.

**Примеры**:

```python
# Пример вызова
test_instance = TestSetAbsolutePaths()
test_instance.setUp()
test_instance.test_single_filename_with_prefix_as_list()
```

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

**Назначение**: Тестирование формирования абсолютных путей с несколькими именами файлов и префиксом в виде строки.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Как работает функция**:

1. Определяет `prefix` как строку `'subfolder'`.
2. Определяет `related_filenames` как список строк `['file1.txt', 'file2.txt', 'file3.txt']`.
3. Формирует ожидаемый результат `expected_result` как список объектов `Path`, каждый из которых объединяет `self.supplier_abs_path`, `prefix` и соответствующее имя файла из списка `related_filenames`. Используется генератор списка для создания списка путей.
4. Вызывает тестируемую функцию `self.function` с аргументами `prefix` и `related_filenames`, сохраняя результат в `result`.
5. Сравнивает полученный `result` с ожидаемым `expected_result` с помощью метода `assertEqual`.

**Примеры**:

```python
# Пример вызова
test_instance = TestSetAbsolutePaths()
test_instance.setUp()
test_instance.test_multiple_filenames_with_prefix_as_string()
```

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

**Назначение**: Тестирование формирования абсолютных путей с несколькими именами файлов и префиксом в виде списка.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Как работает функция**:

1. Определяет `prefix` как список строк `['subfolder', 'subsubfolder']`.
2. Определяет `related_filenames` как список строк `['file1.txt', 'file2.txt', 'file3.txt']`.
3. Формирует ожидаемый результат `expected_result` как список объектов `Path`, каждый из которых объединяет `self.supplier_abs_path`, элементы списка `prefix` (распакованные через `*prefix`) и соответствующее имя файла из списка `related_filenames`. Используется генератор списка для создания списка путей.
4. Вызывает тестируемую функцию `self.function` с аргументами `prefix` и `related_filenames`, сохраняя результат в `result`.
5. Сравнивает полученный `result` с ожидаемым `expected_result` с помощью метода `assertEqual`.

**Примеры**:

```python
# Пример вызова
test_instance = TestSetAbsolutePaths()
test_instance.setUp()
test_instance.test_multiple_filenames_with_prefix_as_list()
```

### `test_no_related_filenames_with_prefix_as_string`

```python
def test_no_related_filenames_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = None
    expected_result = Path(self.supplier_abs_path, prefix)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Назначение**: Тестирование формирования абсолютного пути без имен файлов, с префиксом в виде строки.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Как работает функция**:

1. Определяет `prefix` как строку `'subfolder'`.
2. Определяет `related_filenames` как `None`.
3. Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path` и `prefix`.
4. Вызывает тестируемую функцию `self.function` с аргументами `prefix` и `related_filenames`, сохраняя результат в `result`.
5. Сравнивает полученный `result` с ожидаемым `expected_result` с помощью метода `assertEqual`.

**Примеры**:

```python
# Пример вызова
test_instance = TestSetAbsolutePaths()
test_instance.setUp()
test_instance.test_no_related_filenames_with_prefix_as_string()
```

### `test_no_related_filenames_with_prefix_as_list`

```python
def test_no_related_filenames_with_prefix_as_list(self):
    prefix = ['subfolder', 'subsubfolder']
    related_filenames = None
    expected_result = Path(self.supplier_abs_path, *prefix)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Назначение**: Тестирование формирования абсолютного пути без имен файлов, с префиксом в виде списка.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Как работает функция**:

1. Определяет `prefix` как список строк `['subfolder', 'subsubfolder']`.
2. Определяет `related_filenames` как `None`.
3. Формирует ожидаемый результат `expected_result` с использованием `Path` из `pathlib`, объединяя `self.supplier_abs_path` и элементы списка `prefix` (распакованные через `*prefix`).
4. Вызывает тестируемую функцию `self.function` с аргументами `prefix` и `related_filenames`, сохраняя результат в `result`.
5. Сравнивает полученный `result` с ожидаемым `expected_result` с помощью метода `assertEqual`.

**Примеры**:

```python
# Пример вызова
test_instance = TestSetAbsolutePaths()
test_instance.setUp()
test_instance.test_no_related_filenames_with_prefix_as_list()
```

## Функции

В модуле `test_absolute_paths` нет отдельных функций, только методы класса `TestSetAbsolutePaths`.

```python
if __name__ == '__main__':
    unittest.main()
```

**Назначение**: Обеспечивает запуск тестов при непосредственном вызове файла.

**Как работает функция**:
1. Проверяет, является ли текущий модуль главным (`__name__ == '__main__'`).
2. Если да, то запускает все тесты, определенные в модуле, с помощью `unittest.main()`.

**Примеры**:

```python
# Запуск тестов из командной строки
python test_absolute_paths.py