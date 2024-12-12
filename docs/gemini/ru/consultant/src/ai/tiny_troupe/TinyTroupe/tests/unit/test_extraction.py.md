## Анализ кода модуля `test_extraction.py`

**Качество кода: 7/10**

-   **Плюсы:**
    -   Код хорошо структурирован, используются фикстуры pytest для подготовки тестовых данных.
    -   Тесты покрывают основные функции модуля `extraction`: экспорт в JSON, текст и docx, а также нормализацию.
    -   Используются осмысленные имена для тестовых функций и переменных.
    -   Присутствует логирование с помощью `logger.debug`.
    -   Используется `set` для создания уникального списка концепций.

-   **Минусы:**
    -   Отсутствует docstring для модуля, классов и функций.
    -   Импорты `logging` и `json` не используются через `src.utils.jjson`.
    -   Некоторые проверки внутри тестов могут быть более точными и информативными.
    -   Не везде используется `logger.error` для обработки ошибок, вместо этого используются `assert`.
    -   Используется `print` в коде, что нежелательно для production кода.
    -   Пути к файлам хардкодированы, что может вызвать проблемы при переносе кода.
    -   Дублирование кода при проверке наличия файлов.
    -   Используется `json.load` вместо `j_loads` или `j_loads_ns`
    -   Не все комментарии соответствуют формату `reStructuredText`.

**Рекомендации по улучшению:**

1.  Добавить docstring для модуля, классов и функций в формате reStructuredText.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
3.  Использовать `logger.error` для логирования ошибок при проверках, вместо `assert` (где это уместно).
4.  Убрать `print` и заменить на `logger.debug` для отладочного вывода.
5.  Сделать пути к файлам более гибкими, например, используя `os.path.join` или переменные окружения.
6.  Убрать дублирование кода при проверке существования файлов, вынеся это в отдельную функцию.
7.  Сделать все комментарии в формате `reStructuredText`.
8.  Убрать `sys.path.append` и заменить на корректную настройку путей.
9.  Удалить неиспользуемые импорты.

**Оптимизированный код:**

```python
"""
Модуль тестирования функций извлечения и нормализации.
=========================================================================================

Этот модуль содержит тесты для проверки функциональности классов :class:`ArtifactExporter` и :class:`Normalizer`,
используемых для экспорта артефактов и нормализации текстовых данных.

Пример использования
--------------------

Примеры использования тестов:

.. code-block:: python

    pytest test_extraction.py
"""
import pytest
import os
import random
from src.utils.jjson import j_loads
from src.logger.logger import logger

import sys
# sys.path.append('../../tinytroupe/')
# sys.path.append('../../')
# sys.path.append('../')
# исправлено на добавление в `pytest.ini`
from testing_utils import *
from tinytroupe.extraction import ArtifactExporter, Normalizer
# from tinytroupe import utils #  не используется


@pytest.fixture
def exporter():
    """
    Фикстура для создания экземпляра :class:`ArtifactExporter` с базовой папкой вывода.

    :return: Экземпляр :class:`ArtifactExporter`.
    :rtype: ArtifactExporter
    """
    return ArtifactExporter(base_output_folder="./test_exports")


def _check_file_exists(file_path: str) -> bool:
    """
    Проверяет существование файла и логирует результат.

    :param file_path: Путь к файлу.
    :type file_path: str
    :return: True, если файл существует, иначе False.
    :rtype: bool
    """
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return False
    return True


def test_export_json(exporter: ArtifactExporter):
    """
    Тестирует экспорт артефакта в формате JSON.

    :param exporter: Фикстура для экспортера.
    :type exporter: ArtifactExporter
    """
    # Определяем данные для артефакта
    artifact_data = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }

    # Экспортируем артефакт в JSON
    exporter.export("test_artifact", artifact_data, content_type="record", target_format="json")

    # Проверяем, был ли файл JSON экспортирован правильно
    file_path = "./test_exports/record/test_artifact.json"
    assert _check_file_exists(file_path), "Файл JSON должен был быть экспортирован."

    # Проверяем, содержит ли файл правильные данные
    try:
        with open(file_path, "r") as f:
            exported_data = j_loads(f)
            assert exported_data == artifact_data, "Экспортированные данные JSON должны соответствовать исходным данным."
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        assert False, "Ошибка при чтении файла"


def test_export_text(exporter: ArtifactExporter):
    """
    Тестирует экспорт артефакта в формате TXT.

    :param exporter: Фикстура для экспортера.
    :type exporter: ArtifactExporter
    """
    # Определяем данные для артефакта
    artifact_data = "This is a sample text."

    # Экспортируем артефакт в текстовый файл
    exporter.export("test_artifact", artifact_data, content_type="text", target_format="txt")

    # Проверяем, был ли текстовый файл экспортирован правильно
    file_path = "./test_exports/text/test_artifact.txt"
    assert _check_file_exists(file_path), "Текстовый файл должен был быть экспортирован."

    # Проверяем, содержит ли файл правильные данные
    try:
        with open(file_path, "r") as f:
            exported_data = f.read()
            assert exported_data == artifact_data, "Экспортированные текстовые данные должны соответствовать исходным данным."
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        assert False, "Ошибка при чтении файла"

def test_export_docx(exporter: ArtifactExporter):
    """
    Тестирует экспорт артефакта в формате DOCX.

    :param exporter: Фикстура для экспортера.
    :type exporter: ArtifactExporter
    """
    # Определяем данные для артефакта, включая форматирование markdown
    artifact_data = """
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """

    # Экспортируем артефакт в файл docx
    exporter.export("test_artifact", artifact_data, content_type="Document", content_format="markdown", target_format="docx")

    # Проверяем, был ли файл docx экспортирован правильно
    file_path = "./test_exports/Document/test_artifact.docx"
    assert _check_file_exists(file_path), "Файл docx должен был быть экспортирован."

    # Проверяем, содержит ли файл правильные данные
    try:
        from docx import Document
        doc = Document(file_path)
        exported_data = ""
        for para in doc.paragraphs:
            exported_data += para.text

        assert "This is a sample markdown text" in exported_data, "Экспортированные данные docx должны содержать исходный контент."
        assert "#" not in exported_data, "Экспортированные данные docx не должны содержать Markdown."
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        assert False, "Ошибка при чтении файла"


def test_normalizer():
    """
    Тестирует функциональность класса :class:`Normalizer`.
    """
    # Определяем список концепций для нормализации
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

    assert len(normalizer.normalized_elements) == 10, "Количество нормализованных элементов должно быть равно заданному значению."

    # Создаем несколько случайных выборок из списка концепций
    random_concepts_buckets = [random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15),
                               random.sample(concepts, 15), random.sample(concepts, 15)]

    assert len(normalizer.normalizing_map.keys()) == 0, "Карта нормализации должна быть пустой в начале."

    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())

        normalized_concept = normalizer.normalize(bucket)
        assert normalized_concept is not None, "Нормализованная концепция не должна быть None."
        logger.debug(f"Нормализованная концепция: {bucket} -> {normalized_concept}")
        # print(f"Normalized concept: {bucket} -> {normalized_concept}")  # Убрали print, используем logger.debug

        next_cache_size = len(normalizer.normalizing_map.keys())

        # Проверяем, что длина нормализованной концепции совпадает с длиной входной
        assert len(normalized_concept) == len(bucket), "Нормализованная концепция должна иметь ту же длину, что и входная."

        # Проверяем, что все элементы из нормализованных концепций присутствуют в ключах карты нормализации
        for element in bucket:
            assert element in normalizer.normalizing_map.keys(), f"{element} должен быть в ключах карты нормализации."

        assert next_cache_size > 0, "Размер кеша должен быть больше 0 после нормализации новой концепции."
        assert next_cache_size >= init_cache_size, "Размер кеша не должен уменьшаться после нормализации новой концепции."