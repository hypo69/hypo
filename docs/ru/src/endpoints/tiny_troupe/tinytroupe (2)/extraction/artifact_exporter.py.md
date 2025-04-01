# Модуль `artifact_exporter.py`

## Обзор

Модуль `artifact_exporter.py` предназначен для экспорта артефактов из элементов TinyTroupe, например, для создания синтетических файлов данных из симуляций. Он содержит класс `ArtifactExporter`, который отвечает за экспорт данных в различные форматы, такие как JSON, TXT и DOCX.

## Подробней

Этот модуль предоставляет функциональность для сохранения данных, сгенерированных в процессе работы TinyTroupe, в файлы различных форматов. Это полезно для анализа результатов симуляций, обмена данными с другими системами или для создания документации.

## Классы

### `ArtifactExporter`

**Описание**: Класс `ArtifactExporter` отвечает за экспорт артефактов из TinyTroupe. Он позволяет сохранять данные в различных форматах, таких как JSON, TXT и DOCX.

**Принцип работы**:
Класс инициализируется с указанием базовой папки для вывода файлов. Метод `export` принимает имя артефакта, данные, тип контента и формат экспорта. В зависимости от формата экспорта вызываются соответствующие методы для сохранения данных в файл.

**Аттрибуты**:
- `base_output_folder` (str): Базовая папка для вывода файлов.

**Методы**:
- `__init__(self, base_output_folder:str) -> None`: Инициализирует экземпляр класса `ArtifactExporter`.
- `export(self, artifact_name:str, artifact_data:Union[dict, str], content_type:str, content_format:str=None, target_format:str="txt", verbose:bool=False)`: Экспортирует данные артефакта в файл.
- `_export_as_txt(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False)`: Экспортирует данные артефакта в текстовый файл.
- `_export_as_json(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False)`: Экспортирует данные артефакта в JSON файл.
- `_export_as_docx(self, artifact_file_path:str, artifact_data:Union[dict, str], content_original_format:str, verbose:bool=False)`: Экспортирует данные артефакта в файл DOCX.
- `_compose_filepath(self, artifact_data:Union[dict, str], artifact_name:str, content_type:str, target_format:str=None, verbose:bool=False)`: Формирует путь к файлу для экспорта артефакта.

## Функции

### `__init__`

```python
def __init__(self, base_output_folder:str) -> None:
    """
    Args:
        base_output_folder (str): Базовая папка для вывода файлов.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `ArtifactExporter`.

**Параметры**:
- `base_output_folder` (str): Базовая папка для вывода файлов.

**Возвращает**:
- `None`

**Как работает функция**:
1. Присваивает значение параметра `base_output_folder` атрибуту `self.base_output_folder`.

### `export`

```python
def export(self, artifact_name:str, artifact_data:Union[dict, str], content_type:str, content_format:str=None, target_format:str="txt", verbose:bool=False):
    """
    Args:
        artifact_name (str): The name of the artifact.
        artifact_data (Union[dict, str]): The data to export. If a dict is given, it will be saved as JSON. 
            If a string is given, it will be saved as is.
        content_type (str): The type of the content within the artifact.
        content_format (str, optional): The format of the content within the artifact (e.g., md, csv, etc). Defaults to None.
        target_format (str): The format to export the artifact to (e.g., json, txt, docx, etc).
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
    ...
```

**Назначение**: Экспортирует данные артефакта в файл.

**Параметры**:
- `artifact_name` (str): Имя артефакта.
- `artifact_data` (Union[dict, str]): Данные для экспорта.
- `content_type` (str): Тип контента в артефакте.
- `content_format` (str, optional): Формат контента в артефакте (например, md, csv). По умолчанию `None`.
- `target_format` (str): Формат для экспорта артефакта (например, json, txt, docx). По умолчанию "txt".
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если `artifact_data` не является строкой или словарем.
- `ValueError`: Если `target_format` не поддерживается.

**Как работает функция**:
1. Удаляет лишние отступы из данных артефакта, если они есть.
2. Очищает имя артефакта от недопустимых символов, заменяя их на дефисы, и логирует предупреждение, если такие символы найдены.
3. Формирует путь к файлу с помощью метода `_compose_filepath`.
4. В зависимости от значения `target_format` вызывает соответствующие методы для экспорта данных в файл:
    - `json`: `_export_as_json`
    - `txt`, `text`, `md`, `markdown`: `_export_as_txt`
    - `docx`: `_export_as_docx`
5. Если `target_format` не поддерживается, выбрасывает исключение `ValueError`.

**ASCII схема работы функции**:

```
Начало
│
├──> Проверка типа artifact_data
│     │
│     ├── artifact_data - строка? → Да → Удаление лишних отступов
│     │   └─────────────── Нет
│     │
│     └── artifact_data - словарь? → Да → Удаление лишних отступов из 'content'
│         └─────────────── Нет → Выброс ValueError
│
│
└──> Очистка artifact_name от недопустимых символов
│     │
│     └──> Логирование предупреждения, если символы заменены
│
│
└──> Формирование пути к файлу (_compose_filepath)
│
│
└──> Выбор метода экспорта в зависимости от target_format
│     │
│     ├── target_format == "json"? → Да → _export_as_json
│     │   └─────────────── Нет
│     │
│     ├── target_format в ["txt", "text", "md", "markdown"]? → Да → _export_as_txt
│     │   └─────────────── Нет
│     │
│     ├── target_format == "docx"? → Да → _export_as_docx
│     │   └─────────────── Нет
│     │
│     └──> Выброс ValueError (если target_format не поддерживается)
│
│
Конец
```

**Примеры**:

```python
exporter = ArtifactExporter(base_output_folder='output')
exporter.export(artifact_name='test_artifact', artifact_data={'content': 'test data'}, content_type='test', target_format='json')
exporter.export(artifact_name='test_artifact', artifact_data='test data', content_type='test', target_format='txt')
```

### `_export_as_txt`

```python
def _export_as_txt(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
    """
    Exports the specified artifact data to a text file.
    """
    ...
```

**Назначение**: Экспортирует данные артефакта в текстовый файл.

**Параметры**:
- `artifact_file_path` (str): Путь к файлу для экспорта.
- `artifact_data` (Union[dict, str]): Данные для экспорта.
- `content_type` (str): Тип контента в артефакте.
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Открывает файл для записи в кодировке UTF-8.
2. Если `artifact_data` является словарем, извлекает содержимое из ключа `'content'`. В противном случае использует `artifact_data` как содержимое.
3. Записывает содержимое в файл.

**ASCII схема работы функции**:

```
Начало
│
├──> Открытие файла для записи (UTF-8)
│
├──> Проверка типа artifact_data
│     │
│     ├── artifact_data - словарь? → Да → Извлечение содержимого из ключа 'content'
│     │   └─────────────── Нет → Использование artifact_data как содержимого
│
│
└──> Запись содержимого в файл
│
Конец
```

**Примеры**:

```python
exporter = ArtifactExporter(base_output_folder='output')
exporter._export_as_txt(artifact_file_path='output/test.txt', artifact_data={'content': 'test data'}, content_type='test')
exporter._export_as_txt(artifact_file_path='output/test.txt', artifact_data='test data', content_type='test')
```

### `_export_as_json`

```python
def _export_as_json(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
    """
    Exports the specified artifact data to a JSON file.
    """
    ...
```

**Назначение**: Экспортирует данные артефакта в JSON файл.

**Параметры**:
- `artifact_file_path` (str): Путь к файлу для экспорта.
- `artifact_data` (Union[dict, str]): Данные для экспорта.
- `content_type` (str): Тип контента в артефакте.
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если `artifact_data` не является словарем.

**Как работает функция**:
1. Открывает файл для записи в кодировке UTF-8.
2. Если `artifact_data` является словарем, записывает его в файл в формате JSON с отступами.
3. Если `artifact_data` не является словарем, выбрасывает исключение `ValueError`.

**ASCII схема работы функции**:

```
Начало
│
├──> Открытие файла для записи (UTF-8)
│
├──> Проверка типа artifact_data
│     │
│     ├── artifact_data - словарь? → Да → Запись в файл в формате JSON
│     │   └─────────────── Нет → Выброс ValueError
│
Конец
```

**Примеры**:

```python
exporter = ArtifactExporter(base_output_folder='output')
exporter._export_as_json(artifact_file_path='output/test.json', artifact_data={'content': 'test data'}, content_type='test')
```

### `_export_as_docx`

```python
def _export_as_docx(self, artifact_file_path:str, artifact_data:Union[dict, str], content_original_format:str, verbose:bool=False):
    """
    Exports the specified artifact data to a DOCX file.
    """
    ...
```

**Назначение**: Экспортирует данные артефакта в файл DOCX.

**Параметры**:
- `artifact_file_path` (str): Путь к файлу для экспорта.
- `artifact_data` (Union[dict, str]): Данные для экспорта.
- `content_original_format` (str): Исходный формат контента (например, text, markdown).
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если `content_original_format` не поддерживается.

**Как работает функция**:
1. Проверяет, что `content_original_format` является допустимым значением (text, txt, markdown, md). Если нет, выбрасывает исключение `ValueError`.
2. Нормализует значение `content_original_format`, приводя `md` к `markdown`.
3. Извлекает содержимое из `artifact_data`. Если `artifact_data` является словарем, извлекает содержимое из ключа `'content'`. В противном случае использует `artifact_data` как содержимое.
4. Конвертирует содержимое в HTML с помощью `markdown.markdown`.
5. Конвертирует HTML в DOCX с помощью `pypandoc.convert_text`.

**ASCII схема работы функции**:

```
Начало
│
├──> Проверка content_original_format
│     │
│     ├── content_original_format допустимый? → Да → Нормализация content_original_format (md -> markdown)
│     │   └─────────────── Нет → Выброс ValueError
│
│
├──> Извлечение содержимого из artifact_data
│     │
│     ├── artifact_data - словарь? → Да → Извлечение содержимого из ключа 'content'
│     │   └─────────────── Нет → Использование artifact_data как содержимого
│
│
├──> Конвертация содержимого в HTML (markdown.markdown)
│
│
└──> Конвертация HTML в DOCX (pypandoc.convert_text)
│
Конец
```

**Примеры**:

```python
exporter = ArtifactExporter(base_output_folder='output')
exporter._export_as_docx(artifact_file_path='output/test.docx', artifact_data={'content': '# Test'}, content_original_format='markdown')
exporter._export_as_docx(artifact_file_path='output/test.docx', artifact_data='# Test', content_original_format='markdown')
```

### `_compose_filepath`

```python
def _compose_filepath(self, artifact_data:Union[dict, str], artifact_name:str, content_type:str, target_format:str=None, verbose:bool=False):
    """
    Args:
        artifact_data (Union[dict, str]): The data to export.
        artifact_name (str): The name of the artifact.
        content_type (str): The type of the content within the artifact.
        content_format (str, optional): The format of the content within the artifact (e.g., md, csv, etc). Defaults to None.
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """        
    ...
```

**Назначение**: Формирует путь к файлу для экспорта артефакта.

**Параметры**:
- `artifact_data` (Union[dict, str]): Данные для экспорта.
- `artifact_name` (str): Имя артефакта.
- `content_type` (str): Тип контента в артефакте.
- `target_format` (str, optional): Формат экспорта артефакта (например, json, txt, docx). По умолчанию `None`.
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Возвращает**:
- `str`: Путь к файлу для экспорта артефакта.

**Как работает функция**:
1. Определяет расширение файла в зависимости от `target_format` и типа `artifact_data`.
2. Определяет подпапку для сохранения файла в зависимости от `content_type`.
3. Формирует полный путь к файлу, объединяя базовую папку, подпапку, имя артефакта и расширение.
4. Создает промежуточные директории, если они не существуют.

**ASCII схема работы функции**:

```
Начало
│
├──> Определение расширения файла
│     │
│     ├── target_format указан? → Да → extension = target_format
│     │   └─────────────── Нет
│     │
│     └── artifact_data - строка? → Да → target_format == None? → Да → extension = "txt"
│         └─────────────── Нет
│
│
├──> Определение подпапки
│     │
│     ├── content_type указан? → Да → subfolder = content_type
│     │   └─────────────── Нет → subfolder = ""
│
│
└──> Формирование полного пути к файлу
│
│
└──> Создание промежуточных директорий (os.makedirs)
│
Конец
```

**Примеры**:

```python
exporter = ArtifactExporter(base_output_folder='output')
file_path = exporter._compose_filepath(artifact_data={'content': 'test data'}, artifact_name='test_artifact', content_type='test', target_format='json')
print(file_path)  # output/test/test_artifact.json

file_path = exporter._compose_filepath(artifact_data='test data', artifact_name='test_artifact', content_type='test')
print(file_path)  # output/test/test_artifact.txt