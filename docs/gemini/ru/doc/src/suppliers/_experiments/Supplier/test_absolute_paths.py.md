# Модуль `test_absolute_paths.py`

## Обзор

Модуль `test_absolute_paths.py` содержит набор тестов для проверки корректности формирования абсолютных путей на основе заданной директории поставщика, префикса и связанных имен файлов. Он использует библиотеку `unittest` для организации и запуска тестов, а также библиотеку `pathlib` для работы с путями.

## Подробнее

Этот модуль важен для проверки правильности работы функции `set_absolute_paths` класса `Supplier`, которая отвечает за создание абсолютных путей к файлам поставщика на основе переданных параметров. Тесты охватывают различные сценарии, включая использование префикса в виде строки и списка, наличие или отсутствие связанных имен файлов, а также обработку одного или нескольких связанных имен файлов. Корректное формирование абсолютных путей необходимо для дальнейшей работы с файлами поставщика, например, для их обработки или загрузки.

## Классы

### `TestSetAbsolutePaths`

**Описание**: Класс `TestSetAbsolutePaths` содержит набор тестов для проверки функциональности `set_absolute_paths` класса `Supplier`.

**Наследует**:
- `unittest.TestCase`: Класс наследуется от `unittest.TestCase`, что позволяет использовать функциональность для создания и запуска тестов.

**Атрибуты**:
- `supplier_abs_path` (str): Абсолютный путь к директории поставщика, используемый в тестах.
- `function` (Callable): Ссылка на функцию `set_absolute_paths` класса `Supplier`, которую необходимо протестировать.

**Методы**:
- `setUp()`: Метод, выполняемый перед каждым тестом. Инициализирует атрибуты `supplier_abs_path` и `function`.
- `test_single_filename_with_prefix_as_string()`: Тест проверяет формирование абсолютного пути для одного имени файла с префиксом в виде строки.
- `test_single_filename_with_prefix_as_list()`: Тест проверяет формирование абсолютного пути для одного имени файла с префиксом в виде списка.
- `test_multiple_filenames_with_prefix_as_string()`: Тест проверяет формирование абсолютных путей для нескольких имен файлов с префиксом в виде строки.
- `test_multiple_filenames_with_prefix_as_list()`: Тест проверяет формирование абсолютных путей для нескольких имен файлов с префиксом в виде списка.
- `test_no_related_filenames_with_prefix_as_string()`: Тест проверяет формирование абсолютного пути без связанных имен файлов с префиксом в виде строки.
- `test_no_related_filenames_with_prefix_as_list()`: Тест проверяет формирование абсолютного пути без связанных имен файлов с префиксом в виде списка.

## Функции

### `setUp`

```python
def setUp(self):
    self.supplier_abs_path = '/path/to/supplier'
    self.function = Supplier().set_absolute_paths
```

**Назначение**: Метод `setUp` выполняется перед каждым тестом и инициализирует необходимые атрибуты для тестирования функции `set_absolute_paths`.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Устанавливает значение атрибута `self.supplier_abs_path` в строку '/path/to/supplier', представляющую собой абсолютный путь к директории поставщика.
2.  Устанавливает значение атрибута `self.function` в метод `set_absolute_paths` класса `Supplier`, создавая экземпляр класса `Supplier`.

```
setUp
│
├── Установка supplier_abs_path = '/path/to/supplier'
│
└── Установка function = Supplier().set_absolute_paths
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

    def test_single_filename_with_prefix_as_string(self):
        prefix = 'subfolder'
        related_filenames = 'file.txt'
        expected_result = Path(self.supplier_abs_path, prefix, related_filenames)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)
```

### `test_single_filename_with_prefix_as_string`

```python
def test_single_filename_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = 'file.txt'
    expected_result = Path(self.supplier_abs_path, prefix, related_filenames)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Назначение**: Метод `test_single_filename_with_prefix_as_string` проверяет, что функция `set_absolute_paths` корректно формирует абсолютный путь к файлу, когда задан префикс в виде строки и одно имя файла.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет `prefix` как строку 'subfolder'.
2.  Определяет `related_filenames` как строку 'file.txt'.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path`, объединяя `self.supplier_abs_path`, `prefix` и `related_filenames`.
4.  Вызывает функцию `self.function` (т.е. `set_absolute_paths`) с параметрами `prefix` и `related_filenames` и сохраняет результат в `result`.
5.  Использует `self.assertEqual` для сравнения полученного `result` с ожидаемым `expected_result`.

```
test_single_filename_with_prefix_as_string
│
├── Определение prefix = 'subfolder'
│
├── Определение related_filenames = 'file.txt'
│
├── Формирование expected_result = Path(self.supplier_abs_path, prefix, related_filenames)
│
├── Вызов result = self.function(prefix, related_filenames)
│
└── Сравнение self.assertEqual(result, expected_result)
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

    def test_single_filename_with_prefix_as_string(self):
        prefix = 'subfolder'
        related_filenames = 'file.txt'
        expected_result = Path(self.supplier_abs_path, prefix, related_filenames)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)
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

**Назначение**: Метод `test_single_filename_with_prefix_as_list` проверяет, что функция `set_absolute_paths` корректно формирует абсолютный путь к файлу, когда задан префикс в виде списка и одно имя файла.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет `prefix` как список ['subfolder', 'subsubfolder'].
2.  Определяет `related_filenames` как строку 'file.txt'.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path`, объединяя `self.supplier_abs_path`, распакованный `prefix` (`*prefix`) и `related_filenames`.
4.  Вызывает функцию `self.function` (т.е. `set_absolute_paths`) с параметрами `prefix` и `related_filenames` и сохраняет результат в `result`.
5.  Использует `self.assertEqual` для сравнения полученного `result` с ожидаемым `expected_result`.

```
test_single_filename_with_prefix_as_list
│
├── Определение prefix = ['subfolder', 'subsubfolder']
│
├── Определение related_filenames = 'file.txt'
│
├── Формирование expected_result = Path(self.supplier_abs_path, *prefix, related_filenames)
│
├── Вызов result = self.function(prefix, related_filenames)
│
└── Сравнение self.assertEqual(result, expected_result)
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

    def test_single_filename_with_prefix_as_list(self):
        prefix = ['subfolder', 'subsubfolder']
        related_filenames = 'file.txt'
        expected_result = Path(self.supplier_abs_path, *prefix, related_filenames)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)
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

**Назначение**: Метод `test_multiple_filenames_with_prefix_as_string` проверяет, что функция `set_absolute_paths` корректно формирует список абсолютных путей к файлам, когда задан префикс в виде строки и несколько имен файлов.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет `prefix` как строку 'subfolder'.
2.  Определяет `related_filenames` как список ['file1.txt', 'file2.txt', 'file3.txt'].
3.  Формирует ожидаемый результат `expected_result` как список объектов `Path`, используя генератор списка. Каждый объект `Path` объединяет `self.supplier_abs_path`, `prefix` и имя файла из `related_filenames`.
4.  Вызывает функцию `self.function` (т.е. `set_absolute_paths`) с параметрами `prefix` и `related_filenames` и сохраняет результат в `result`.
5.  Использует `self.assertEqual` для сравнения полученного `result` с ожидаемым `expected_result`.

```
test_multiple_filenames_with_prefix_as_string
│
├── Определение prefix = 'subfolder'
│
├── Определение related_filenames = ['file1.txt', 'file2.txt', 'file3.txt']
│
├── Формирование expected_result = [Path(self.supplier_abs_path, prefix, filename) for filename in related_filenames]
│
├── Вызов result = self.function(prefix, related_filenames)
│
└── Сравнение self.assertEqual(result, expected_result)
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

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

**Назначение**: Метод `test_multiple_filenames_with_prefix_as_list` проверяет, что функция `set_absolute_paths` корректно формирует список абсолютных путей к файлам, когда задан префикс в виде списка и несколько имен файлов.

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет `prefix` как список ['subfolder', 'subsubfolder'].
2.  Определяет `related_filenames` как список ['file1.txt', 'file2.txt', 'file3.txt'].
3.  Формирует ожидаемый результат `expected_result` как список объектов `Path`, используя генератор списка. Каждый объект `Path` объединяет `self.supplier_abs_path`, распакованный `prefix` (`*prefix`) и имя файла из `related_filenames`.
4.  Вызывает функцию `self.function` (т.е. `set_absolute_paths`) с параметрами `prefix` и `related_filenames` и сохраняет результат в `result`.
5.  Использует `self.assertEqual` для сравнения полученного `result` с ожидаемым `expected_result`.

```
test_multiple_filenames_with_prefix_as_list
│
├── Определение prefix = ['subfolder', 'subsubfolder']
│
├── Определение related_filenames = ['file1.txt', 'file2.txt', 'file3.txt']
│
├── Формирование expected_result = [Path(self.supplier_abs_path, *prefix, filename) for filename in related_filenames]
│
├── Вызов result = self.function(prefix, related_filenames)
│
└── Сравнение self.assertEqual(result, expected_result)
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

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

### `test_no_related_filenames_with_prefix_as_string`

```python
def test_no_related_filenames_with_prefix_as_string(self):
    prefix = 'subfolder'
    related_filenames = None
    expected_result = Path(self.supplier_abs_path, prefix)

    result = self.function(prefix, related_filenames)

    self.assertEqual(result, expected_result)
```

**Назначение**: Метод `test_no_related_filenames_with_prefix_as_string` проверяет, что функция `set_absolute_paths` корректно формирует абсолютный путь, когда задан префикс в виде строки и отсутствуют связанные имена файлов (None).

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет `prefix` как строку 'subfolder'.
2.  Определяет `related_filenames` как `None`.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path`, объединяя `self.supplier_abs_path` и `prefix`.
4.  Вызывает функцию `self.function` (т.е. `set_absolute_paths`) с параметрами `prefix` и `related_filenames` и сохраняет результат в `result`.
5.  Использует `self.assertEqual` для сравнения полученного `result` с ожидаемым `expected_result`.

```
test_no_related_filenames_with_prefix_as_string
│
├── Определение prefix = 'subfolder'
│
├── Определение related_filenames = None
│
├── Формирование expected_result = Path(self.supplier_abs_path, prefix)
│
├── Вызов result = self.function(prefix, related_filenames)
│
└── Сравнение self.assertEqual(result, expected_result)
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

    def test_no_related_filenames_with_prefix_as_string(self):
        prefix = 'subfolder'
        related_filenames = None
        expected_result = Path(self.supplier_abs_path, prefix)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)
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

**Назначение**: Метод `test_no_related_filenames_with_prefix_as_list` проверяет, что функция `set_absolute_paths` корректно формирует абсолютный путь, когда задан префикс в виде списка и отсутствуют связанные имена файлов (None).

**Параметры**:
- `self` (TestSetAbsolutePaths): Экземпляр класса `TestSetAbsolutePaths`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет `prefix` как список ['subfolder', 'subsubfolder'].
2.  Определяет `related_filenames` как `None`.
3.  Формирует ожидаемый результат `expected_result` с использованием `Path`, объединяя `self.supplier_abs_path` и распакованный `prefix` (`*prefix`).
4.  Вызывает функцию `self.function` (т.е. `set_absolute_paths`) с параметрами `prefix` и `related_filenames` и сохраняет результат в `result`.
5.  Использует `self.assertEqual` для сравнения полученного `result` с ожидаемым `expected_result`.

```
test_no_related_filenames_with_prefix_as_list
│
├── Определение prefix = ['subfolder', 'subsubfolder']
│
├── Определение related_filenames = None
│
├── Формирование expected_result = Path(self.supplier_abs_path, *prefix)
│
├── Вызов result = self.function(prefix, related_filenames)
│
└── Сравнение self.assertEqual(result, expected_result)
```

**Примеры**:

```python
import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

    def test_no_related_filenames_with_prefix_as_list(self):
        prefix = ['subfolder', 'subsubfolder']
        related_filenames = None
        expected_result = Path(self.supplier_abs_path, *prefix)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)
```

### `if __name__ == '__main__':`

```python
if __name__ == '__main__':
    unittest.main()
```

**Назначение**: Этот блок кода позволяет запускать тесты, определенные в модуле, при его непосредственном выполнении.

**Как работает функция**:

1.  Проверяет, является ли текущий модуль главным (`__name__ == '__main__'`).
2.  Если условие выполняется, запускает все тесты, определенные в модуле, с помощью `unittest.main()`.

**Примеры**:

Чтобы запустить тесты, необходимо выполнить этот файл напрямую:

```bash
python test_absolute_paths.py