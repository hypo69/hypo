# Документация модуля `test_extraction.py`

## Обзор

Этот модуль содержит unit-тесты для проверки функциональности классов `ArtifactExporter` и `Normalizer` из модуля `tinytroupe.extraction`. Тесты охватывают экспорт данных в форматы JSON, TXT и DOCX, а также нормализацию концепций.

## Оглавление
- [Фикстуры](#Фикстуры)
    - [exporter](#exporter)
- [Тесты](#Тесты)
    - [test_export_json](#test_export_json)
    - [test_export_text](#test_export_text)
    - [test_export_docx](#test_export_docx)
    - [test_normalizer](#test_normalizer)

## Фикстуры

### `exporter`

**Описание**: Фикстура для создания экземпляра `ArtifactExporter` с базовой папкой вывода `./test_exports`.

**Возвращает**:
- `ArtifactExporter`: Экземпляр `ArtifactExporter`.

## Тесты

### `test_export_json`

**Описание**: Тестирует экспорт артефактов в формате JSON.

**Параметры**:
- `exporter` (ArtifactExporter): Фикстура `exporter`.

**Проверяет**:
- Создание JSON-файла в правильной директории.
- Совпадение экспортированных данных с исходными.

### `test_export_text`

**Описание**: Тестирует экспорт артефактов в формате TXT.

**Параметры**:
- `exporter` (ArtifactExporter): Фикстура `exporter`.

**Проверяет**:
- Создание TXT-файла в правильной директории.
- Совпадение экспортированных данных с исходными.

### `test_export_docx`

**Описание**: Тестирует экспорт артефактов в формате DOCX, включая проверку сохранения форматирования Markdown.

**Параметры**:
- `exporter` (ArtifactExporter): Фикстура `exporter`.

**Проверяет**:
- Создание DOCX-файла в правильной директории.
- Наличие части исходного контента в экспортированном файле.
- Отсутствие синтаксиса Markdown в экспортированном файле.

### `test_normalizer`

**Описание**: Тестирует функциональность класса `Normalizer`.

**Проверяет**:
- Количество нормализованных элементов соответствует заданному значению.
- Изначальное состояние `normalizing_map`.
- Результат нормализации не `None`.
- Совпадение длин входного и выходного списков.
- Наличие элементов входного списка в ключах `normalizing_map`.
- Увеличение размера кеша после нормализации.