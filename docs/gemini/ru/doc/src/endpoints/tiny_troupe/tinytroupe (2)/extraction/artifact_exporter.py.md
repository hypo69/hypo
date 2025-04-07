# Модуль для экспорта артефактов
## Обзор

Модуль `artifact_exporter.py` предоставляет класс `ArtifactExporter`, предназначенный для экспорта артефактов из элементов TinyTroupe. Это может быть полезно, например, для создания файлов синтетических данных из симуляций.

## Подробнее

Класс `ArtifactExporter` позволяет сохранять данные в различных форматах, таких как JSON, TXT и DOCX. Он также обрабатывает имена артефактов, заменяя недопустимые символы, и создает необходимые подкаталоги для сохранения файлов.

## Классы

### `ArtifactExporter`

**Описание**: Класс `ArtifactExporter` отвечает за экспорт артефактов из TinyTroupe.

**Принцип работы**:
Класс инициализируется с указанием базовой папки для вывода. Метод `export` принимает имя артефакта, данные, тип контента и формат, после чего вызывает соответствующие методы для сохранения данных в нужном формате.

**Атрибуты**:
- `base_output_folder` (str): Базовая папка для сохранения экспортированных артефактов.

**Методы**:

- `__init__(self, base_output_folder: str) -> None`: Инициализирует экземпляр класса `ArtifactExporter` с указанием базовой папки для вывода.
- `export(self, artifact_name: str, artifact_data: Union[dict, str], content_type: str, content_format: str = None, target_format: str = "txt", verbose: bool = False)`: Экспортирует артефакт в файл.
- `_export_as_txt(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False)`: Экспортирует артефакт в текстовый файл.
- `_export_as_json(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False)`: Экспортирует артефакт в JSON файл.
- `_export_as_docx(self, artifact_file_path: str, artifact_data: Union[dict, str], content_original_format: str, verbose: bool = False)`: Экспортирует артефакт в файл DOCX.
- `_compose_filepath(self, artifact_data: Union[dict, str], artifact_name: str, content_type: str, target_format: str = None, verbose: bool = False)`: Формирует путь к файлу для экспортируемого артефакта.

## Функции

### `__init__`

```python
def __init__(self, base_output_folder:str) -> None:
    """
    Args:
        base_output_folder (str): Базовая папка для сохранения экспортированных артефактов.
    """
    ...
```

**Назначение**: Инициализирует класс `ArtifactExporter`, устанавливая базовую папку для вывода артефактов.

**Параметры**:
- `base_output_folder` (str): Путь к базовой папке, в которой будут сохраняться экспортированные артефакты.

**Как работает функция**:
1. Функция принимает путь к базовой папке.
2. Присваивает переданный путь атрибуту `base_output_folder` экземпляра класса.

**Примеры**:
```python
exporter = ArtifactExporter("output")
print(exporter.base_output_folder)  # Вывод: output
```

### `export`

```python
def export(self, artifact_name:str, artifact_data:Union[dict, str], content_type:str, content_format:str=None, target_format:str="txt", verbose:bool=False):
    """
    Args:
        artifact_name (str): Имя артефакта.
        artifact_data (Union[dict, str]): Данные для экспорта. Если передан словарь, он будет сохранен как JSON. Если передана строка, она будет сохранена как есть.
        content_type (str): Тип контента в артефакте.
        content_format (str, optional): Формат контента в артефакте (например, md, csv и т.д.). По умолчанию `None`.
        target_format (str): Формат, в который экспортируется артефакт (например, json, txt, docx и т.д.).
        verbose (bool, optional): Флаг, определяющий, нужно ли выводить отладочные сообщения. По умолчанию `False`.

    Raises:
        ValueError: Если `artifact_data` не является строкой или словарем.
        ValueError: Если `target_format` не поддерживается.
    """
    ...
```

**Назначение**: Экспортирует переданные данные артефакта в файл в указанном формате.

**Параметры**:
- `artifact_name` (str): Имя артефакта, которое будет использоваться в имени файла.
- `artifact_data` (Union[dict, str]): Данные для экспорта. Могут быть словарем или строкой.
- `content_type` (str): Тип контента, например, "log" или "simulation". Используется для создания подпапок.
- `content_format` (str, optional): Формат контента (например, "md" для Markdown). По умолчанию `None`.
- `target_format` (str): Целевой формат файла (например, "json", "txt", "docx"). По умолчанию "txt".
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Вызывает исключения**:
- `ValueError`: Если `artifact_data` не является ни строкой, ни словарем.
- `ValueError`: Если указан неподдерживаемый `target_format`.

**Как работает функция**:

```
На входе: artifact_name, artifact_data, content_type, content_format, target_format, verbose
│
├── Проверка типа artifact_data (строка или словарь)
│   └── Если не строка и не словарь:
│       └── Выброс ValueError("The artifact data must be either a string or a dictionary.")
│
├── Очистка artifact_name от недопустимых символов
│   └── Замена недопустимых символов на дефисы
│
├── Формирование пути к файлу с помощью _compose_filepath
│   └── artifact_file_path = self._compose_filepath(...)
│
├── Выбор метода экспорта в зависимости от target_format
│   ├── Если target_format == "json":
│   │   └── Вызов _export_as_json
│   ├── Если target_format == "txt" или "text" или "md" или "markdown":
│   │   └── Вызов _export_as_txt
│   ├── Если target_format == "docx":
│   │   └── Вызов _export_as_docx
│   └── Иначе:
│       └── Выброс ValueError(f"Unsupported target format: {target_format}.")
│
Выход: Сохраненный файл с артефактом в указанном формате
```

**Примеры**:

```python
exporter = ArtifactExporter("output")
data = {"content": "Пример данных"}
exporter.export("example", data, "text", target_format="json")  # Создаст файл output/text/example.json
```

### `_export_as_txt`

```python
def _export_as_txt(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
    """
    Exports the specified artifact data to a text file.
    """
    ...
```

**Назначение**: Экспортирует переданные данные артефакта в текстовый файл.

**Параметры**:
- `artifact_file_path` (str): Путь к файлу, в который будет сохранен артефакт.
- `artifact_data` (Union[dict, str]): Данные для экспорта. Могут быть словарем или строкой.
- `content_type` (str): Тип контента (не используется в данной функции, но передается для совместимости).
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений (не используется в данной функции, но передается для совместимости).

**Как работает функция**:

```
На входе: artifact_file_path, artifact_data, content_type, verbose
│
├── Открытие файла для записи в кодировке utf-8
│   └── with open(artifact_file_path, 'w', encoding="utf-8") as f:
│
├── Проверка типа artifact_data
│   ├── Если artifact_data - словарь:
│   │   └── Извлечение контента из словаря: content = artifact_data['content']
│   └── Иначе:
│   │   └── Контент = artifact_data
│
├── Запись контента в файл
│   └── f.write(content)
│
Выход: Текстовый файл с данными артефакта
```

**Примеры**:

```python
exporter = ArtifactExporter("output")
data = {"content": "Пример данных для текстового файла"}
exporter._export_as_txt("output/example.txt", data, "text")  # Создаст файл output/example.txt с содержимым "Пример данных для текстового файла"
```

### `_export_as_json`

```python
def _export_as_json(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
    """
    Exports the specified artifact data to a JSON file.
    """
    ...
```

**Назначение**: Экспортирует переданные данные артефакта в JSON файл.

**Параметры**:
- `artifact_file_path` (str): Путь к файлу, в который будет сохранен артефакт.
- `artifact_data` (Union[dict, str]): Данные для экспорта. Должны быть словарем.
- `content_type` (str): Тип контента (не используется в данной функции, но передается для совместимости).
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений (не используется в данной функции, но передается для совместимости).

**Вызывает исключения**:
- `ValueError`: Если `artifact_data` не является словарем.

**Как работает функция**:

```
На входе: artifact_file_path, artifact_data, content_type, verbose
│
├── Открытие файла для записи в кодировке utf-8
│   └── with open(artifact_file_path, 'w', encoding="utf-8") as f:
│
├── Проверка типа artifact_data
│   ├── Если artifact_data - словарь:
│   │   └── Запись данных в файл в формате JSON с отступами
│   │   └── json.dump(artifact_data, f, indent=4)
│   └── Иначе:
│   │   └── Выброс ValueError("The artifact data must be a dictionary to export to JSON.")
│
Выход: JSON файл с данными артефакта
```

**Примеры**:

```python
exporter = ArtifactExporter("output")
data = {"key": "value", "number": 123}
exporter._export_as_json("output/example.json", data, "data")  # Создаст файл output/example.json с JSON представлением словаря data
```

### `_export_as_docx`

```python
def _export_as_docx(self, artifact_file_path:str, artifact_data:Union[dict, str], content_original_format:str, verbose:bool=False):
    """
    Exports the specified artifact data to a DOCX file.
    """
    ...
```

**Назначение**: Экспортирует переданные данные артефакта в файл DOCX.

**Параметры**:
- `artifact_file_path` (str): Путь к файлу, в который будет сохранен артефакт.
- `artifact_data` (Union[dict, str]): Данные для экспорта. Могут быть словарем или строкой.
- `content_original_format` (str): Исходный формат контента ("text", "txt", "markdown", "md").
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений (не используется в данной функции, но передается для совместимости).

**Вызывает исключения**:
- `ValueError`: Если `content_original_format` не является одним из допустимых значений ("text", "txt", "markdown", "md").

**Как работает функция**:

```
На входе: artifact_file_path, artifact_data, content_original_format, verbose
│
├── Проверка content_original_format на допустимые значения
│   └── Если content_original_format не в ['text', 'txt', 'markdown', 'md']:
│       └── Выброс ValueError(f"The original format cannot be {content_original_format} to export to DOCX.")
│
├── Нормализация content_original_format (если 'md', то заменяется на 'markdown')
│   └── content_original_format = 'markdown' if content_original_format == 'md' else content_original_format
│
├── Извлечение контента из artifact_data (если artifact_data - словарь, то content = artifact_data['content'], иначе content = artifact_data)
│
├── Преобразование контента в HTML с помощью markdown.markdown(content)
│
├── Конвертация HTML в DOCX с помощью pypandoc.convert_text(html_content, 'docx', format='html', outputfile=artifact_file_path)
│
Выход: Файл DOCX с данными артефакта
```

**Примеры**:

```python
exporter = ArtifactExporter("output")
data = {"content": "# Заголовок\nТекст"}
exporter._export_as_docx("output/example.docx", data, "markdown")  # Создаст файл output/example.docx с отформатированным текстом
```

### `_compose_filepath`

```python
def _compose_filepath(self, artifact_data:Union[dict, str], artifact_name:str, content_type:str, target_format:str=None, verbose:bool=False):
    """
    Args:
        artifact_data (Union[dict, str]): Данные для экспорта.
        artifact_name (str): Имя артефакта.
        content_type (str): Тип контента в артефакте.
        content_format (str, optional): Формат контента в артефакте (например, md, csv и т.д.). Defaults to None.
        verbose (bool, optional): Флаг, определяющий, нужно ли выводить отладочные сообщения. Defaults to False.
    """
    ...
```

**Назначение**: Формирует путь к файлу для экспортируемого артефакта.

**Параметры**:
- `artifact_data` (Union[dict, str]): Данные для экспорта.
- `artifact_name` (str): Имя артефакта.
- `content_type` (str): Тип контента.
- `target_format` (str, optional): Целевой формат файла (например, "json", "txt", "docx"). По умолчанию `None`.
- `verbose` (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

**Как работает функция**:

```
На входе: artifact_data, artifact_name, content_type, target_format, verbose
│
├── Определение расширения файла
│   ├── Если target_format указан:
│   │   └── extension = f"{target_format}"
│   ├── Иначе, если artifact_data - строка и target_format не указан:
│   │   └── extension = "txt"
│   └── Иначе:
│   │   └── extension = None
│
├── Определение подпапки на основе content_type
│   ├── Если content_type не указан:
│   │   └── subfolder = ""
│   └── Иначе:
│   │   └── subfolder = content_type
│
├── Формирование полного пути к файлу
│   └── artifact_file_path = os.path.join(self.base_output_folder, subfolder, f"{artifact_name}.{extension}")
│
├── Создание промежуточных директорий, если необходимо
│   └── os.makedirs(os.path.dirname(artifact_file_path), exist_ok=True)
│
Выход: Полный путь к файлу артефакта
```

**Примеры**:

```python
exporter = ArtifactExporter("output")
file_path = exporter._compose_filepath({"content": "data"}, "example", "log", target_format="json")
print(file_path)  # Вывод: output/log/example.json
```
```python
exporter = ArtifactExporter("output")
file_path = exporter._compose_filepath("data", "example", "text")
print(file_path)  # Вывод: output/text/example.txt