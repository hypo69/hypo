# Документация для разработчика: `pytest`

## Обзор

Этот файл содержит инструкции и примеры для написания тестов с использованием библиотеки `pytest`. Он предназначен для QA-инженеров и разработчиков, занимающихся тестированием модулей Python.

## Содержание

- [Обзор](#обзор)
- [Подробней](#подробней)
- [Основные принципы написания тестов](#основные-принципы-написания-тестов)
    - [Анализ функциональности](#анализ-функциональности)
    - [Подготовка тестовых случаев](#подготовка-тестовых-случаев)
    - [Обработка ошибок](#обработка-ошибок)
    - [Изоляция тестов](#изоляция-тестов)
    - [Структура тестов](#структура-тестов)
- [Пример теста](#пример-теста)
- [Запуск тестов](#запуск-тестов)
- [Заключение](#заключение)

## Подробней

Этот документ предоставляет общее руководство по написанию тестов для Python-модулей с использованием библиотеки `pytest`. Он охватывает основные аспекты, такие как анализ функциональности, подготовка тестовых случаев, обработка ошибок, изоляция тестов и структура тестов. Также предоставлен пример теста с объяснениями.

## Основные принципы написания тестов

### Анализ функциональности

- Изучите функции и методы, доступные в модуле. Определите их входные данные, ожидаемые выходные данные и возможные случаи ошибок.
- Разделите тесты на основные сценарии, крайние случаи и обработку исключений.

### Подготовка тестовых случаев

- Напишите тестовые случаи для каждой функции или метода.
- Убедитесь, что тесты проверяют функции с различными типами данных, где это применимо, такими как строки, списки, словари или пустые значения.
- Рассмотрите крайние случаи, такие как пустой ввод, несуществующие пути или недопустимые значения.

### Обработка ошибок

- Смоделируйте сценарии, в которых могут возникать исключения, и убедитесь, что исключения обрабатываются и регистрируются соответствующим образом.
- Используйте `pytest.raises` для тестирования обработки исключений.

### Изоляция тестов

- Используйте `mocking` для замены реальных операций, где это возможно. Например, используйте моки вместо фактического взаимодействия с файловой системой или базами данных.
- Убедитесь, что каждый тест не зависит от других и не полагается на внешнюю среду.

### Структура тестов

- Используйте понятные и описательные имена для тестовых функций, которые отражают их назначение.
- Организуйте тестовый код для удобочитаемости и структуры.
- Используйте фикстуры `pytest` для настройки данных при необходимости.

## Пример теста

```python
import pytest
from unittest.mock import patch, mock_open

@patch('module_name.Path.open', new_callable=mock_open)
@patch('module_name.Path.mkdir')
@patch('module_name.logger')
def test_save_data_to_file(mock_logger, mock_mkdir, mock_file_open):
    """Test saving data to a file."""
    file_path = '/path/to/your/file.txt'
    data = 'Sample text'

    # Test saving a string
    result = save_data_to_file(data, file_path)
    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    mock_file_open.assert_called_once_with('w')
    mock_file_open().write.assert_called_once_with(data)
    assert result is True

    # Test exception handling
    mock_file_open.side_effect = Exception('Mocked exception')
    result = save_data_to_file(data, file_path)
    mock_logger.error.assert_called_once()
    assert result is False
```

### `test_save_data_to_file`

```python
def test_save_data_to_file(mock_logger, mock_mkdir, mock_file_open):
    """Test saving data to a file."""
    file_path = '/path/to/your/file.txt'
    data = 'Sample text'

    # Test saving a string
    result = save_data_to_file(data, file_path)
    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    mock_file_open.assert_called_once_with('w')
    mock_file_open().write.assert_called_once_with(data)
    assert result is True

    # Test exception handling
    mock_file_open.side_effect = Exception('Mocked exception')
    result = save_data_to_file(data, file_path)
    mock_logger.error.assert_called_once()
    assert result is False
```

**Описание**: Тест для проверки сохранения данных в файл.

**Как работает функция**:
1. Используются декораторы `@patch` для замены реальных операций с файловой системой и логирования на моки.
2. Определяются `file_path` и `data` для тестирования функции `save_data_to_file`.
3. Проверяется, что функция правильно вызывает методы `mkdir` и `open` с ожидаемыми аргументами.
4. Проверяется, что данные успешно записываются в файл.
5. Моделируется исключение при открытии файла, и проверяется, что ошибка логируется и функция возвращает `False`.

**Параметры**:
- `mock_logger`: Мок для логирования.
- `mock_mkdir`: Мок для создания директории.
- `mock_file_open`: Мок для открытия файла.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Моделируется исключение при открытии файла.

**Примеры**:
```python
import pytest
from unittest.mock import patch, mock_open

@patch('module_name.Path.open', new_callable=mock_open)
@patch('module_name.Path.mkdir')
@patch('module_name.logger')
def test_save_data_to_file(mock_logger, mock_mkdir, mock_file_open):
    """Test saving data to a file."""
    file_path = '/path/to/your/file.txt'
    data = 'Sample text'

    # Test saving a string
    result = save_data_to_file(data, file_path)
    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    mock_file_open.assert_called_once_with('w')
    mock_file_open().write.assert_called_once_with(data)
    assert result is True

    # Test exception handling
    mock_file_open.side_effect = Exception('Mocked exception')
    result = save_data_to_file(data, file_path)
    mock_logger.error.assert_called_once()
    assert result is False
```

**Объяснение:**

1. **Моки и изоляция:**
   - `@patch` заменяет реальные операции моками, чтобы исключить влияние внешней среды.
   - `mock_open` имитирует операции открытия и записи файла.

2. **Тестирование сценариев:**
   - **Основная проверка:** Убеждается, что файл создается и данные записываются правильно.
   - **Обработка ошибок:** Моделирует исключение во время операции с файлом, гарантируя, что оно обрабатывается, регистрируется, и функция возвращает ожидаемое значение.

## Запуск тестов

Запустите тесты, используя следующую команду:

```bash
pytest path_to_test_file.py
```

## Заключение

Этот общий подход можно применить к тестированию любого модуля, независимо от его функциональности. Убедитесь, что ваши тесты охватывают основные сценарии, крайние случаи и правильную обработку ошибок, сохраняя их изолированными и независимыми.