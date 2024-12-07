# Модуль `test_extraction.py`

## Обзор

Этот модуль содержит тесты для модуля `extraction` из проекта `TinyTroupe`. Он проверяет функциональность класса `ArtifactExporter` для экспорта данных в различные форматы (JSON, текст, docx) и класс `Normalizer` для нормализации концепций.

## Фикстуры

### `exporter`

**Описание**: Фикстура для создания экземпляра класса `ArtifactExporter` с указанной папкой для экспорта.

**Использование**:
```python
@pytest.fixture
def exporter():
    return ArtifactExporter(base_output_folder="./test_exports")
```

## Функции

### `test_export_json`

**Описание**: Тестирует экспорт данных в формате JSON. Проверяет, что файл JSON был создан и содержит правильные данные.

**Аргументы**:
- `exporter`: Экземпляр класса `ArtifactExporter` (полученный из фикстуры).


**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `AssertionError`: Если файл JSON не был создан или данные в файле не соответствуют ожидаемым.

### `test_export_text`

**Описание**: Тестирует экспорт данных в текстовом формате. Проверяет, что файл TXT был создан и содержит правильные данные.

**Аргументы**:
- `exporter`: Экземпляр класса `ArtifactExporter` (полученный из фикстуры).

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `AssertionError`: Если файл TXT не был создан или данные в файле не соответствуют ожидаемым.

### `test_export_docx`

**Описание**: Тестирует экспорт данных в формате docx. Проверяет, что файл docx был создан и содержит правильные данные (проверяет сохранение форматирования Markdown).

**Аргументы**:
- `exporter`: Экземпляр класса `ArtifactExporter` (полученный из фикстуры).

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `AssertionError`: Если файл docx не был создан или данные в файле не соответствуют ожидаемым (отсутствие форматирования Markdown).
- `ImportError`: Если отсутствует модуль `docx`.

### `test_normalizer`

**Описание**: Тестирует класс `Normalizer` для нормализации концепций. Проверяет корректность нормализации списка концепций и сохранение размера после нормализации.

**Аргументы**:
- Не принимает аргументов.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `AssertionError`: Если количество нормализованных элементов не соответствует ожидаемому, если нормализованная концепция пустая или имеет размер не равный входному списку, или если элемент не найден в отображении нормализации.


## Модули и классы

### `ArtifactExporter`

**Описание**: Класс для экспорта данных в различные форматы файлов.

**Методы**:
- `export`: Метод для экспорта данных в заданный формат.


### `Normalizer`

**Описание**: Класс для нормализации концепций.

**Методы**:
- `normalize`: Метод для нормализации списка концепций.



## Использование

Этот модуль предназначен для тестирования функциональности классов `ArtifactExporter` и `Normalizer` при помощи тестовых фреймворка pytest. Для запуска тестов необходимо установить pytest и библиотеки, необходимые для работы с docx (например, `python-docx`).
```
pip install pytest python-docx
```
и затем запустить `pytest` в корневой директории проекта.
```bash
pytest