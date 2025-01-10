# Анализ кода модуля `test_extraction.py`

**Качество кода: 7/10**
-  Плюсы
    - Код имеет модульную структуру, что облегчает понимание и поддержку.
    - Присутствуют тесты для проверки основных функций `ArtifactExporter` и `Normalizer`.
    - Используется `pytest` для организации и запуска тестов.
    - Присутствуют логические проверки в тестах, которые обеспечивают надежность кода.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
    - Отсутствуют docstring для модуля и функций.
    - Используется стандартный `logging`, а не `logger` из `src.logger`.
    - Присутствуют абсолютные импорты, которые могут вызвать проблемы при перемещении кода.
    - Есть дублирование `sys.path.append`
    - Использования `print()` для отладочной печати.

**Рекомендации по улучшению**
1.  Добавить docstring для модуля и функций для улучшения читаемости и понимания кода.
2.  Заменить импорт `logging` на `from src.logger.logger import logger` и использовать его для логирования.
3.  Использовать `j_loads` из `src.utils.jjson` для чтения JSON файлов.
4.  Изменить абсолютные пути импортов на относительные.
5.  Удалить избыточные `sys.path.append`
6.  Удалить `print` заменив на `logger.debug`
7.  Добавить проверку существования директории перед созданием экспорта.
8.  Использовать `Pathlib` для управления путями к файлам.
9.  Использовать f-строки для форматирования строк.

**Оптимизированный код**

```python
"""
Модуль для тестирования функций экспорта и нормализации артефактов.
=====================================================================

Этот модуль содержит тесты для проверки корректности работы классов
:class:`ArtifactExporter` и :class:`Normalizer`, используемых
для экспорта артефактов в различные форматы (JSON, текст, docx)
и нормализации текстовых данных соответственно.

Пример использования
--------------------

Пример запуска тестов:

.. code-block:: bash

    pytest test_extraction.py
"""
import pytest
import os
import random
from pathlib import Path
# from logging import getLogger
from src.logger.logger import logger # Импортируем logger из sr.logger
from src.utils.jjson import j_loads # Импортируем j_loads
import sys
# sys.path.append('../../tinytroupe/') # удаляем дублирование
# sys.path.append('../../') # удаляем дублирование
# sys.path.append('../') # удаляем дублирование

from tests.unit.testing_utils import *
from src.ai.tiny_troupe.TinyTroupe.extraction import ArtifactExporter, Normalizer

@pytest.fixture
def exporter():
    """
    Фикстура для создания экземпляра ArtifactExporter.

    Returns:
        ArtifactExporter: Экземпляр ArtifactExporter с базовой папкой для экспорта "./test_exports".
    """
    return ArtifactExporter(base_output_folder="./test_exports")


def test_export_json(exporter):
    """
    Тестирует экспорт артефакта в формате JSON.

    Args:
        exporter (ArtifactExporter): Экземпляр ArtifactExporter, предоставленный фикстурой.
    """
    # Определяем данные артефакта
    artifact_data = {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Engineer',
        'content': 'This is a sample JSON data.'
    }
    
    # Экспортируем данные артефакта в формате JSON
    exporter.export('test_artifact', artifact_data, content_type='record', target_format='json')
    
    # Проверяем, был ли файл JSON экспортирован правильно
    file_path = Path('./test_exports/record/test_artifact.json')
    assert file_path.exists(), 'The JSON file should have been exported.'
    
    # Проверяем, содержит ли файл ожидаемые данные
    with open(file_path, 'r') as f:
        exported_data = j_loads(f) # Используем j_loads для чтения JSON
        assert exported_data == artifact_data, 'The exported JSON data should match the original data.'


def test_export_text(exporter):
    """
     Тестирует экспорт артефакта в текстовом формате.

    Args:
        exporter (ArtifactExporter): Экземпляр ArtifactExporter, предоставленный фикстурой.
    """
    # Определяем данные артефакта
    artifact_data = 'This is a sample text.'
    
    # Экспортируем данные артефакта в текстовом формате
    exporter.export('test_artifact', artifact_data, content_type='text', target_format='txt')
    
    # Проверяем, был ли текстовый файл экспортирован правильно
    file_path = Path('./test_exports/text/test_artifact.txt')
    assert file_path.exists(), 'The text file should have been exported.'
    
    # Проверяем, содержит ли файл ожидаемые данные
    with open(file_path, 'r') as f:
        exported_data = f.read()
        assert exported_data == artifact_data, 'The exported text data should match the original data.'


def test_export_docx(exporter):
    """
     Тестирует экспорт артефакта в формате docx с сохранением markdown.

    Args:
        exporter (ArtifactExporter): Экземпляр ArtifactExporter, предоставленный фикстурой.
    """
    # Определяем данные артефакта. Включаем форматирование markdown для проверки его сохранения.
    artifact_data = """
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """
    
    # Экспортируем данные артефакта в формате docx
    exporter.export('test_artifact', artifact_data, content_type='Document', content_format='markdown', target_format='docx')
    
    # Проверяем, был ли файл docx экспортирован правильно
    file_path = Path('./test_exports/Document/test_artifact.docx')
    assert file_path.exists(), 'The docx file should have been exported.'
    
    # Проверяем, содержит ли файл ожидаемые данные
    from docx import Document
    doc = Document(str(file_path))
    exported_data = ''
    for para in doc.paragraphs:
        exported_data += para.text

    assert 'This is a sample markdown text' in exported_data, 'The exported docx data should contain some of the original content.'
    assert '#' not in exported_data, 'The exported docx data should not contain Markdown.'


def test_normalizer():
    """
    Тестирует функциональность нормализатора текста.

    Проверяет, что нормализатор возвращает правильное количество нормализованных элементов
    и корректно кэширует результаты нормализации.
    """
    # Определяем концепции для нормализации
    concepts = ['Antique Book Collection', 'Medical Research', 'Electrical safety', 'Reading', 'Technology', 'Entrepreneurship', 'Multimedia Teaching Tools', 'Photography',
     'Smart home technology', 'Gardening', 'Travel', 'Outdoors', 'Hiking', 'Yoga', 'Finance', 'Health and wellness', 'Sustainable Living', 'Barista Skills', 'Oral health education',
     'Patient care', 'Professional Development', 'Project safety', 'Coffee', 'Literature', 'Continuous learning', 'Model trains', 'Education', 'Mental and Physical Balance', 'Kayaking',
     'Social Justice', 'National Park Exploration', 'Outdoor activities', 'Dental technology', 'Teaching electrical skills', 'Volunteering', 'Cooking', 'Industry trends',
     'Energy-efficient systems', 'Mentoring', 'Empathetic communication', 'Medical Technology', 'Historical Research', 'Public Speaking', 'Museum Volunteering', 'Conflict Resolution']
    
    unique_concepts = list(set(concepts))

    normalizer = Normalizer(concepts, n=10, verbose=True)
    
    assert len(normalizer.normalized_elements) == 10, 'The number of normalized elements should be equal to the specified value.'
    
    # Случайным образом выбираем элементы из concepts
    random_concepts_buckets = [random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15)]
    
    assert len(normalizer.normalizing_map.keys()) == 0, 'The normalizing map should be empty at the beginning.'
    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())
        
        normalized_concept = normalizer.normalize(bucket)
        assert normalized_concept is not None, 'The normalized concept should not be None.'
        logger.debug(f'Normalized concept: {bucket} -> {normalized_concept}') # Используем logger.debug
       

        next_cache_size = len(normalizer.normalizing_map.keys())
        
        # Проверяем длину
        assert len(normalized_concept) == len(bucket), 'The normalized concept should have the same length as the input concept.'
        
        # Проверяем, что все элементы из нормализованных концепций присутствуют в ключах карты нормализации
        for element in bucket:
            assert element in normalizer.normalizing_map.keys(), f'{element} should be in the normalizing map keys.'
        
        assert next_cache_size > 0, 'The cache size should be greater than 0 after normalizing a new concept.'
        assert next_cache_size >= init_cache_size, 'The cache size should not decrease after normalizing a new concept.'