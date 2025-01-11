# Анализ кода модуля `test_extraction`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используются фикстуры pytest для настройки тестов.
    - Тесты покрывают различные сценарии использования функций экспорта и нормализации.
    - Присутствует логирование для отладки.
- Минусы
    -  Используется устаревший `logging` вместо `logger` из `src.logger`.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
    -  Отсутствует документация в формате RST для модуля, классов и функций.
    -  Много дублирующегося кода при проверке результатов экспорта.
    -  Используется `print` для вывода информации в консоль, что не является лучшей практикой в тестах.
    -  В тестах не используются константы для путей, что делает их менее гибкими.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Заменить импорт `logging` и использование `logging.getLogger` на `from src.logger.logger import logger`.
    -   Использовать `from src.utils.jjson import j_loads` для загрузки JSON файлов.
    -   Добавить импорт `Path` из `pathlib`.
    -   Удалить `sys.path.append`, так как он не требуется для запуска тестов.
2.  **Документация**:
    -   Добавить описание модуля в начале файла в формате RST.
    -   Добавить docstring для всех функций и классов в формате RST.
3.  **Экспорт**:
    -   Использовать константы для путей к файлам экспорта.
    -   Рефакторить функции проверки экспорта, вынеся общую логику в отдельную функцию.
4.  **Нормализация**:
    -   Удалить `print` из тестов, оставив только `logger.debug`.
5.  **Обработка файлов**:
    - Использовать `j_loads` для чтения json файлов

**Оптимизированный код**

```python
"""
Модуль для тестирования функций экспорта и нормализации артефактов.
=================================================================

Этот модуль содержит тесты для проверки работы классов :class:`ArtifactExporter` и :class:`Normalizer`
из модуля `tinytroupe.extraction`.
Тесты проверяют корректность экспорта данных в различных форматах (JSON, TXT, DOCX) и функциональность нормализации текста.

Пример использования
--------------------

.. code-block:: python

    pytest test_extraction.py
"""

import pytest
import os
import random
from pathlib import Path
from src.logger.logger import logger
from src.utils.jjson import j_loads

from docx import Document # fix: import here

from tinytroupe.extraction import ArtifactExporter, Normalizer


# Константы для путей к файлам
TEST_EXPORTS_DIR = "./test_exports"
RECORD_DIR = Path(TEST_EXPORTS_DIR) / "record"
TEXT_DIR = Path(TEST_EXPORTS_DIR) / "text"
DOCUMENT_DIR = Path(TEST_EXPORTS_DIR) / "Document"

@pytest.fixture
def exporter():
    """
    Фикстура pytest для создания экземпляра ArtifactExporter.

    Returns:
        ArtifactExporter: Экземпляр класса ArtifactExporter.
    """
    return ArtifactExporter(base_output_folder=TEST_EXPORTS_DIR)


def _check_file_exists_and_contains(file_path: Path, expected_data, is_json: bool = False,  use_j_loads:bool=False):
    """
    Проверяет, существует ли файл и содержит ли он ожидаемые данные.

    Args:
        file_path (Path): Путь к файлу.
        expected_data: Ожидаемые данные для проверки.
        is_json (bool, optional): Флаг, указывающий, является ли файл JSON. По умолчанию False.
        use_j_loads(bool, optional): флаг для использования j_loads

    Raises:
         AssertionError: Если файл не существует или содержимое не соответствует ожидаемому.

    """
    assert os.path.exists(file_path), f"Файл {file_path} не был экспортирован."

    try:
        with open(file_path, "r") as f:
            if is_json:
                if use_j_loads:
                    exported_data = j_loads(f)
                else:
                    exported_data = json.load(f)
            else:
                exported_data = f.read()
    except Exception as e:
         logger.error(f"Ошибка при чтении файла {file_path}: {e}")
         raise AssertionError(f"Ошибка при чтении файла {file_path}: {e}")

    assert exported_data == expected_data, f"Экспортированные данные не соответствуют ожидаемым данным в файле {file_path}."


def _check_docx_contains(file_path: Path, expected_text:str, not_expected_text:str):
    """
    Проверяет, что docx файл содержит ожидаемый текст и не содержит не ожидаемый.

    Args:
        file_path (Path): Путь к файлу docx.
        expected_text (str): Текст, который должен содержаться в файле.
        not_expected_text (str): Текст, который не должен содержаться в файле.
    Raises:
         AssertionError: Если файл не существует или содержимое не соответствует ожидаемому.
    """
    assert os.path.exists(file_path), f"Файл {file_path} не был экспортирован: {file_path}."
    doc = Document(file_path)
    exported_data = ""
    for para in doc.paragraphs:
        exported_data += para.text
    assert expected_text in exported_data, f"Экспортированные данные не содержат ожидаемый текст: {expected_text}."
    assert not_expected_text not in exported_data, f"Экспортированные данные содержат не ожидаемый текст: {not_expected_text}."

def test_export_json(exporter):
    """
    Тестирует экспорт данных в формате JSON.

    Args:
        exporter (ArtifactExporter): Фикстура экземпляра ArtifactExporter.
    """
    artifact_data = {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Engineer',
        'content': 'This is a sample JSON data.'
    }

    exporter.export('test_artifact', artifact_data, content_type='record', target_format='json')
    _check_file_exists_and_contains(RECORD_DIR / "test_artifact.json", artifact_data, is_json=True, use_j_loads=True)


def test_export_text(exporter):
    """
    Тестирует экспорт данных в формате TXT.

    Args:
        exporter (ArtifactExporter): Фикстура экземпляра ArtifactExporter.
    """
    artifact_data = 'This is a sample text.'
    exporter.export('test_artifact', artifact_data, content_type='text', target_format='txt')
    _check_file_exists_and_contains(TEXT_DIR / "test_artifact.txt", artifact_data)


def test_export_docx(exporter):
    """
    Тестирует экспорт данных в формате DOCX.

    Args:
        exporter (ArtifactExporter): Фикстура экземпляра ArtifactExporter.
    """
    artifact_data = """
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """

    exporter.export("test_artifact", artifact_data, content_type="Document", content_format="markdown", target_format="docx")
    _check_docx_contains(DOCUMENT_DIR / "test_artifact.docx", "This is a sample markdown text", "#")


def test_normalizer():
    """
    Тестирует функциональность нормализации текста.
    """
    concepts = ['Antique Book Collection', 'Medical Research', 'Electrical safety', 'Reading', 'Technology',
                'Entrepreneurship', 'Multimedia Teaching Tools', 'Photography',
                'Smart home technology', 'Gardening', 'Travel', 'Outdoors', 'Hiking', 'Yoga', 'Finance',
                'Health and wellness', 'Sustainable Living', 'Barista Skills', 'Oral health education',
                'Patient care', 'Professional Development', 'Project safety', 'Coffee', 'Literature',
                'Continuous learning', 'Model trains', 'Education', 'Mental and Physical Balance', 'Kayaking',
                'Social Justice', 'National Park Exploration', 'Outdoor activities', 'Dental technology',
                'Teaching electrical skills', 'Volunteering', 'Cooking', 'Industry trends',
                'Energy-efficient systems', 'Mentoring', 'Empathetic communication', 'Medical Technology',
                'Historical Research', 'Public Speaking', 'Museum Volunteering', 'Conflict Resolution']

    unique_concepts = list(set(concepts))

    normalizer = Normalizer(concepts, n=10, verbose=True)

    assert len(normalizer.normalized_elements) == 10, "Количество нормализованных элементов должно соответствовать заданному значению."

    random_concepts_buckets = [random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15),
                             random.sample(concepts, 15), random.sample(concepts, 15)]

    assert len(normalizer.normalizing_map.keys()) == 0, "Карта нормализации должна быть пустой в начале."

    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())

        normalized_concept = normalizer.normalize(bucket)
        assert normalized_concept is not None, "Нормализованный концепт не должен быть None."
        logger.debug(f"Нормализованный концепт: {bucket} -> {normalized_concept}")

        next_cache_size = len(normalizer.normalizing_map.keys())

        assert len(normalized_concept) == len(bucket), "Длина нормализованного концепта должна быть равна длине входного концепта."

        for element in bucket:
            assert element in normalizer.normalizing_map.keys(), f"{element} должен быть в ключах карты нормализации."

        assert next_cache_size > 0, "Размер кэша должен быть больше 0 после нормализации нового концепта."
        assert next_cache_size >= init_cache_size, "Размер кэша не должен уменьшаться после нормализации нового концепта."