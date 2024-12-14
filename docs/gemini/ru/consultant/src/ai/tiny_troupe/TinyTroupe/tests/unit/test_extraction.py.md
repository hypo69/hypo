# Анализ кода модуля `test_extraction.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используются фикстуры `pytest` для настройки окружения.
    - Тесты охватывают экспорт в JSON, TXT и DOCX форматы.
    - Присутствует тест для нормализатора текста.
    - Используется `logger` для отладочного вывода.
- Минусы
    - Не все импорты выстроены в соответствии с ранее обработанными файлами.
    - Отсутствует документация в формате reStructuredText (RST) для модуля, функций, методов.
    - Используется стандартный `json.load` вместо `j_loads` из `src.utils.jjson`.
    - Избыточное использование `assert` для проверок, лучше использовать `logger.error` для более информативных сообщений об ошибках.
    - Присутствует дублирование кода в тестах (`with open(...)` для чтения файлов).

**Рекомендации по улучшению**
1.  Добавить docstring в формате RST для модуля, всех функций, классов и методов.
2.  Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load`.
3.  Избегать дублирования кода, например, вынести чтение файлов в отдельную функцию.
4.  Заменить `assert` на `logger.error` в сочетании с выбросом исключений для более информативной обработки ошибок.
5.  Добавить проверку на существование директорий перед экспортом.
6.  Импортировать `j_loads` и `logger` в начале файла.
7.  Убрать лишние `sys.path.append`, так как они не требуются для запуска тестов.
8.  Улучшить сообщения об ошибках, добавив конкретику.
9.  Переименовать переменную `exported_data` в более конкретное имя, например, `file_content`.

**Оптимизиробанный код**
```python
"""
Модуль для тестирования функций извлечения и нормализации.
=========================================================================================

Этот модуль содержит тесты для проверки корректности работы классов
:class:`ArtifactExporter` и :class:`Normalizer`, включая экспорт данных в JSON,
текстовые и DOCX форматы, а также нормализацию текстовых концепций.
"""
import pytest
import os
# import json # Заменен на j_loads
import random

# import logging # Заменен на from src.logger.logger import logger
# logger = logging.getLogger("tinytroupe")

import sys
# sys.path.append('../../tinytroupe/') # лишний импорт
# sys.path.append('../../') # лишний импорт
# sys.path.append('..') # лишний импорт

from src.logger.logger import logger
from src.utils.jjson import j_loads
from testing_utils import *
from tinytroupe.extraction import ArtifactExporter, Normalizer
# from tinytroupe import utils # не используется


@pytest.fixture
def exporter():
    """
    Фикстура для создания экземпляра класса ArtifactExporter.

    :return: Экземпляр класса ArtifactExporter с базовой папкой "./test_exports".
    :rtype: ArtifactExporter
    """
    return ArtifactExporter(base_output_folder="./test_exports")


def _read_file_content(file_path: str) -> str:
    """
    Считывает содержимое файла.

    :param file_path: Путь к файлу.
    :type file_path: str
    :return: Содержимое файла.
    :rtype: str
    :raises FileNotFoundError: Если файл не найден.
    """
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {file_path}, {e}")
        raise


def test_export_json(exporter):
    """
    Тестирует экспорт данных в JSON формат.

    :param exporter: Фикстура ArtifactExporter.
    :type exporter: ArtifactExporter
    """
    # Define the artifact data
    artifact_data = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }

    # Export the artifact data as JSON
    exporter.export("test_artifact", artifact_data, content_type="record", target_format="json")

    # check if the JSON file was exported correctly
    file_path = "./test_exports/record/test_artifact.json"
    if not os.path.exists(file_path):
        logger.error(f"Файл JSON не был экспортирован: {file_path}")
        raise FileNotFoundError(f"Файл JSON не был экспортирован: {file_path}")

    # does it contain the data?
    try:
        # with open(file_path, "r", encoding='utf-8') as f: #  Заменено на _read_file_content
        #     exported_data = j_loads(f) # Заменено на j_loads
        file_content = j_loads(_read_file_content(file_path))
        if file_content != artifact_data:
            logger.error(f"Экспортированные JSON данные не совпадают с исходными данными. Ожидалось {artifact_data}, получено {file_content}")
            raise ValueError("Экспортированные JSON данные не совпадают с исходными данными.")
    except Exception as e:
        logger.error(f"Ошибка при чтении или сравнении JSON файла: {e}")
        raise


def test_export_text(exporter):
    """
    Тестирует экспорт данных в текстовый формат.

    :param exporter: Фикстура ArtifactExporter.
    :type exporter: ArtifactExporter
    """
    # Define the artifact data
    artifact_data = "This is a sample text."

    # Export the artifact data as text
    exporter.export("test_artifact", artifact_data, content_type="text", target_format="txt")

    # check if the text file was exported correctly
    file_path = "./test_exports/text/test_artifact.txt"
    if not os.path.exists(file_path):
        logger.error(f"Текстовый файл не был экспортирован: {file_path}")
        raise FileNotFoundError(f"Текстовый файл не был экспортирован: {file_path}")

    # does it contain the data?
    try:
        # with open(file_path, "r", encoding='utf-8') as f: # Заменено на _read_file_content
        #     exported_data = f.read() # Заменено на _read_file_content
        file_content = _read_file_content(file_path)
        if file_content != artifact_data:
           logger.error(f"Экспортированные текстовые данные не совпадают с исходными данными. Ожидалось {artifact_data}, получено {file_content}")
           raise ValueError("Экспортированные текстовые данные не совпадают с исходными данными.")
    except Exception as e:
        logger.error(f"Ошибка при чтении или сравнении текстового файла: {e}")
        raise

def test_export_docx(exporter):
    """
    Тестирует экспорт данных в DOCX формат.

    :param exporter: Фикстура ArtifactExporter.
    :type exporter: ArtifactExporter
    """
    # Define the artifact data. Include some fancy markdown formatting so we can test if it is preserved.
    artifact_data = """
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """

    # Export the artifact data as a docx file
    exporter.export("test_artifact", artifact_data, content_type="Document", content_format="markdown", target_format="docx")

    # check if the docx file was exported correctly
    file_path = "./test_exports/Document/test_artifact.docx"
    if not os.path.exists(file_path):
        logger.error(f"Файл DOCX не был экспортирован: {file_path}")
        raise FileNotFoundError(f"Файл DOCX не был экспортирован: {file_path}")

    # does it contain the data?
    from docx import Document
    try:
        doc = Document(file_path)
        file_content = ""
        for para in doc.paragraphs:
            file_content += para.text

        if "This is a sample markdown text" not in file_content:
            logger.error(f"Экспортированные docx данные не содержат части исходного контента: 'This is a sample markdown text', получено {file_content}")
            raise ValueError("Экспортированные docx данные не содержат части исходного контента")
        if "#" in file_content:
            logger.error(f"Экспортированные docx данные содержат Markdown: '#', получено {file_content}")
            raise ValueError("Экспортированные docx данные содержат Markdown.")
    except Exception as e:
        logger.error(f"Ошибка при чтении или проверке DOCX файла: {e}")
        raise


def test_normalizer():
    """
    Тестирует нормализатор текста.
    """
    # Define the concepts to be normalized
    concepts = ['Antique Book Collection', 'Medical Research', 'Electrical safety', 'Reading', 'Technology', 'Entrepreneurship', 'Multimedia Teaching Tools', 'Photography',
     'Smart home technology', 'Gardening', 'Travel', 'Outdoors', 'Hiking', 'Yoga', 'Finance', 'Health and wellness', 'Sustainable Living', 'Barista Skills', 'Oral health education',
     'Patient care', 'Professional Development', 'Project safety', 'Coffee', 'Literature', 'Continuous learning', 'Model trains', 'Education', 'Mental and Physical Balance', 'Kayaking',
     'Social Justice', 'National Park Exploration', 'Outdoor activities', 'Dental technology', 'Teaching electrical skills', 'Volunteering', 'Cooking', 'Industry trends',
     'Energy-efficient systems', 'Mentoring', 'Empathetic communication', 'Medical Technology', 'Historical Research', 'Public Speaking', 'Museum Volunteering', 'Conflict Resolution']

    unique_concepts = list(set(concepts))

    normalizer = Normalizer(concepts, n=10, verbose=True)

    if len(normalizer.normalized_elements) != 10:
        logger.error(f"Количество нормализованных элементов ({len(normalizer.normalized_elements)}) не соответствует ожидаемому (10)")
        raise ValueError("Количество нормализованных элементов не соответствует ожидаемому.")

    # sample 5 random elements from concepts using standard python methods
    random_concepts_buckets = [random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15)]

    if len(normalizer.normalizing_map.keys()) != 0:
         logger.error(f"Карта нормализации не пуста в начале: {len(normalizer.normalizing_map.keys())}")
         raise ValueError("Карта нормализации не пуста в начале.")
    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())

        normalized_concept = normalizer.normalize(bucket)
        if normalized_concept is None:
            logger.error(f"Нормализованная концепция  не может быть None для bucket: {bucket}")
            raise ValueError("Нормализованная концепция не может быть None.")
        logger.debug(f"Нормализованная концепция: {bucket} -> {normalized_concept}")
        print(f"Нормализованная концепция: {bucket} -> {normalized_concept}")

        next_cache_size = len(normalizer.normalizing_map.keys())

        # check same length
        if len(normalized_concept) != len(bucket):
            logger.error(f"Нормализованная концепция ({len(normalized_concept)}) имеет не ту же длину, что и входная концепция ({len(bucket)})")
            raise ValueError("Нормализованная концепция должна иметь ту же длину, что и входная концепция.")

        # assert that all elements from normalized concepts are in normalizing map keys
        for element in bucket:
            if element not in normalizer.normalizing_map.keys():
                logger.error(f"Элемент {element} должен быть в ключах карты нормализации")
                raise ValueError(f"Элемент {element} должен быть в ключах карты нормализации")

        if next_cache_size <= 0:
            logger.error(f"Размер кэша должен быть больше 0 после нормализации новой концепции: {next_cache_size}")
            raise ValueError("Размер кэша должен быть больше 0 после нормализации новой концепции.")
        if next_cache_size < init_cache_size:
            logger.error(f"Размер кэша не должен уменьшаться после нормализации новой концепции. Текущий размер {next_cache_size}, прошлый размер {init_cache_size}")
            raise ValueError("Размер кэша не должен уменьшаться после нормализации новой концепции.")