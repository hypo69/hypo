# Модуль тестирования функций извлечения данных

## Обзор

Модуль содержит набор юнит-тестов для проверки корректности работы функций извлечения и нормализации данных, реализованных в модуле `tinytroupe.extraction`. В частности, тестируются возможности экспорта артефактов в различных форматах (JSON, TXT, DOCX) и нормализации текстовых данных.

## Подробней

Этот модуль предназначен для автоматизированной проверки функциональности классов `ArtifactExporter` и `Normalizer` из модуля `tinytroupe.extraction`. Тесты охватывают экспорт данных в различных форматах и проверку сохранения структуры и содержимого данных при экспорте. Также тестируется функциональность нормализации данных, включая проверку размера кэша и корректности работы механизма нормализации.

## Функции

### `exporter`

```python
@pytest.fixture
def exporter():
    """
    Создает и возвращает экземпляр класса `ArtifactExporter` для использования в тестах.

    Returns:
        ArtifactExporter: Экземпляр класса `ArtifactExporter` с базовой папкой для экспорта `EXPORT_BASE_FOLDER`.
    """
    ...
```

**Назначение**:
Создает и конфигурирует фикстуру `exporter`, которая является экземпляром класса `ArtifactExporter`. Эта фикстура используется для предоставления чистого и готового к использованию объекта `ArtifactExporter` в каждом тесте, который в ней нуждается.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `ArtifactExporter`: Объект класса `ArtifactExporter`, сконфигурированный с базовой папкой для экспорта `EXPORT_BASE_FOLDER`.

**Как работает функция**:

1.  Создает экземпляр класса `ArtifactExporter` с указанием базовой папки для экспорта (`EXPORT_BASE_FOLDER`).
2.  Возвращает созданный экземпляр `ArtifactExporter`.

```
Создание ArtifactExporter
↓
Возврат ArtifactExporter
```

**Примеры**:
```python
def test_export_json(exporter):
    # Используем фикстуру exporter для теста
    ...
```

### `test_export_json`

```python
def test_export_json(exporter):
    """
    Тестирует экспорт данных в формате JSON с использованием класса `ArtifactExporter`.

    Args:
        exporter: Фикстура `ArtifactExporter`, предоставляющая экземпляр класса для экспорта.
    """
    ...
```

**Назначение**:
Проверяет корректность экспорта данных в формате JSON с использованием класса `ArtifactExporter`. Тест определяет артефактные данные, экспортирует их в формате JSON, а затем проверяет, был ли JSON-файл экспортирован правильно и содержит ли он исходные данные.

**Параметры**:
- `exporter`: Фикстура `ArtifactExporter`, предоставляющая экземпляр класса для экспорта.

**Как работает функция**:

1.  Определяет артефактные данные в виде словаря `artifact_data`.
2.  Вызывает метод `export` объекта `exporter` для экспорта данных в формате JSON.
3.  Проверяет, существует ли экспортированный JSON-файл в указанной директории.
4.  Открывает экспортированный JSON-файл и загружает данные из него.
5.  Сравнивает экспортированные данные с исходными данными `artifact_data` для проверки их идентичности.

```
Определение артефактных данных
↓
Экспорт данных в JSON
↓
Проверка существования файла
↓
Загрузка данных из файла
↓
Сравнение данных
```

**Примеры**:
```python
def test_export_json(exporter):
    # Define the artifact data
    artifact_data = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }
    
    # Export the artifact data as JSON
    exporter.export("test_artifact", artifact_data, content_type="record", target_format="json")
    
    #check if the JSON file was exported correctly
    assert os.path.exists(f"{EXPORT_BASE_FOLDER}/record/test_artifact.json"), "The JSON file should have been exported."

    # does it contain the data?
    with open(f"{EXPORT_BASE_FOLDER}/record/test_artifact.json", "r") as f:
        exported_data = json.load(f)
        assert exported_data == artifact_data, "The exported JSON data should match the original data."
```

### `test_export_text`

```python
def test_export_text(exporter):
    """
    Тестирует экспорт данных в формате TXT с использованием класса `ArtifactExporter`.

    Args:
        exporter: Фикстура `ArtifactExporter`, предоставляющая экземпляр класса для экспорта.
    """
    ...
```

**Назначение**:
Проверяет корректность экспорта данных в формате TXT с использованием класса `ArtifactExporter`. Тест определяет артефактные данные в виде текстовой строки, экспортирует их в формате TXT, а затем проверяет, был ли TXT-файл экспортирован правильно и содержит ли он исходные данные.

**Параметры**:
- `exporter`: Фикстура `ArtifactExporter`, предоставляющая экземпляр класса для экспорта.

**Как работает функция**:

1.  Определяет артефактные данные в виде текстовой строки `artifact_data`.
2.  Вызывает метод `export` объекта `exporter` для экспорта данных в формате TXT.
3.  Проверяет, существует ли экспортированный TXT-файл в указанной директории.
4.  Открывает экспортированный TXT-файл и считывает данные из него.
5.  Сравнивает экспортированные данные с исходными данными `artifact_data` для проверки их идентичности.

```
Определение артефактных данных
↓
Экспорт данных в TXT
↓
Проверка существования файла
↓
Чтение данных из файла
↓
Сравнение данных
```

**Примеры**:
```python
def test_export_text(exporter):
    # Define the artifact data
    artifact_data = "This is a sample text."
    
    # Export the artifact data as text
    exporter.export("test_artifact", artifact_data, content_type="text", target_format="txt")
    
    # check if the text file was exported correctly
    assert os.path.exists(f"{EXPORT_BASE_FOLDER}/text/test_artifact.txt"), "The text file should have been exported."

    # does it contain the data?
    with open(f"{EXPORT_BASE_FOLDER}/text/test_artifact.txt", "r") as f:
        exported_data = f.read()
        assert exported_data == artifact_data, "The exported text data should match the original data."
```

### `test_export_docx`

```python
def test_export_docx(exporter):
    """
    Тестирует экспорт данных в формате DOCX с использованием класса `ArtifactExporter`.

    Args:
        exporter: Фикстура `ArtifactExporter`, предоставляющая экземпляр класса для экспорта.
    """
    ...
```

**Назначение**:
Проверяет корректность экспорта данных в формате DOCX с использованием класса `ArtifactExporter`. Тест определяет артефактные данные в формате Markdown, экспортирует их в формате DOCX, а затем проверяет, был ли DOCX-файл экспортирован правильно и содержит ли он исходные данные. Также проверяется, что Markdown-форматирование было преобразовано в формат DOCX.

**Параметры**:
- `exporter`: Фикстура `ArtifactExporter`, предоставляющая экземпляр класса для экспорта.

**Как работает функция**:

1.  Определяет артефактные данные в формате Markdown в виде многострочной строки `artifact_data`.
2.  Вызывает метод `export` объекта `exporter` для экспорта данных в формате DOCX с указанием формата содержимого как Markdown.
3.  Проверяет, существует ли экспортированный DOCX-файл в указанной директории.
4.  Открывает экспортированный DOCX-файл с использованием библиотеки `docx`.
5.  Считывает текст из каждого абзаца DOCX-файла и объединяет его в одну строку `exported_data`.
6.  Проверяет, содержит ли экспортированные данные часть исходного содержимого (например, "This is a sample markdown text").
7.  Проверяет, что экспортированные данные не содержат Markdown-форматирования (например, "#").

```
Определение артефактных данных в Markdown
↓
Экспорт данных в DOCX
↓
Проверка существования файла
↓
Чтение данных из DOCX файла
↓
Проверка содержимого и форматирования
```

**Примеры**:
```python
def test_export_docx(exporter):
    # Define the artifact data. Include some fancy markdown formatting so we can test if it is preserved.
    artifact_data ="""
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """
    
    # Export the artifact data as a docx file
    exporter.export("test_artifact", artifact_data, content_type="Document", content_format="markdown", target_format="docx")
    
    # check if the docx file was exported correctly
    assert os.path.exists(f"{EXPORT_BASE_FOLDER}/Document/test_artifact.docx"), "The docx file should have been exported."

    # does it contain the data?
    from docx import Document
    doc = Document(f"{EXPORT_BASE_FOLDER}/Document/test_artifact.docx")
    exported_data = ""
    for para in doc.paragraphs:
        exported_data += para.text

    assert "This is a sample markdown text" in exported_data, "The exported docx data should contain some of the original content."
    assert "#" not in exported_data, "The exported docx data should not contain Markdown."
```

### `test_normalizer`

```python
def test_normalizer():
    """
    Тестирует функциональность нормализации текста с использованием класса `Normalizer`.
    """
    ...
```

**Назначение**:
Проверяет функциональность нормализации текста с использованием класса `Normalizer`. Тест определяет набор концепций, создает экземпляр класса `Normalizer`, нормализует случайные подмножества концепций и проверяет, что нормализация работает корректно, включая проверку размера кэша и соответствие длины нормализованных концепций исходным.

**Как работает функция**:

1.  Определяет список концепций `concepts`, которые будут нормализованы.
2.  Создает экземпляр класса `Normalizer` с указанием списка концепций, размера нормализованных элементов (`n=10`) и включенным режимом отладки (`verbose=True`).
3.  Проверяет, что количество нормализованных элементов равно указанному значению (`10`).
4.  Создает несколько случайных подмножеств (корзин) концепций с использованием `random.sample`.
5.  Для каждой корзины:
    *   Получает начальный размер кэша нормализации.
    *   Нормализует корзину концепций с использованием метода `normalize` объекта `normalizer`.
    *   Проверяет, что нормализованная концепция не равна `None`.
    *   Выводит отладочную информацию о нормализации.
    *   Получает конечный размер кэша нормализации.
    *   Проверяет, что длина нормализованной концепции соответствует длине исходной корзины.
    *   Проверяет, что все элементы из нормализованной концепции присутствуют в ключах кэша нормализации.
    *   Проверяет, что размер кэша увеличился после нормализации новой концепции.

```
Определение списка концепций
↓
Создание экземпляра Normalizer
↓
Проверка размера нормализованных элементов
↓
Создание случайных подмножеств концепций
↓
Для каждой корзины:
    ↓
    Нормализация корзины
    ↓
    Проверки (длина, наличие в кэше, размер кэша)
```

**Примеры**:
```python
def test_normalizer():
    # Define the concepts to be normalized
    concepts = ['Antique Book Collection', 'Medical Research', 'Electrical safety', 'Reading', 'Technology', 'Entrepreneurship', 'Multimedia Teaching Tools', 'Photography', 
     'Smart home technology', 'Gardening', 'Travel', 'Outdoors', 'Hiking', 'Yoga', 'Finance', 'Health and wellness', 'Sustainable Living', 'Barista Skills', 'Oral health education',
     'Patient care', 'Professional Development', 'Project safety', 'Coffee', 'Literature', 'Continuous learning', 'Model trains', 'Education', 'Mental and Physical Balance', 'Kayaking',
     'Social Justice', 'National Park Exploration', 'Outdoor activities', 'Dental technology', 'Teaching electrical skills', 'Volunteering', 'Cooking', 'Industry trends', 
     'Energy-efficient systems', 'Mentoring', 'Empathetic communication', 'Medical Technology', 'Historical Research', 'Public Speaking', 'Museum Volunteering', 'Conflict Resolution']
    
    unique_concepts = list(set(concepts))

    normalizer = Normalizer(concepts, n=10, verbose=True)

    assert len(normalizer.normalized_elements) == 10, "The number of normalized elements should be equal to the specified value."

    # sample 5 random elements from concepts using standard python methods
    
    random_concepts_buckets = [random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15)]


    assert len(normalizer.normalizing_map.keys()) == 0, "The normalizing map should be empty at the beginning."
    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())
        
        normalized_concept = normalizer.normalize(bucket)
        assert normalized_concept is not None, "The normalized concept should not be None."
        logger.debug(f"Normalized concept: {bucket} -> {normalized_concept}")
        print(f"Normalized concept: {bucket} -> {normalized_concept}")

        next_cache_size = len(normalizer.normalizing_map.keys())

        # check same length
        assert len(normalized_concept) == len(bucket), "The normalized concept should have the same length as the input concept."

        # assert that all elements from normalized concepts are in normalizing map keys
        for element in bucket:
            assert element in normalizer.normalizing_map.keys(), f"{element} should be in the normalizing map keys."

        assert next_cache_size > 0, "The cache size should be greater than 0 after normalizing a new concept."
        assert next_cache_size >= init_cache_size, "The cache size should not decrease after normalizing a new concept."