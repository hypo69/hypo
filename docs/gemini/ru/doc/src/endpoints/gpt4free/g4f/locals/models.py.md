# Модуль для работы с моделями

## Обзор

Модуль предоставляет функции для загрузки, форматирования, чтения и сохранения информации о моделях. Он используется для управления и организации данных о моделях, необходимых для работы проекта `hypotez`.

## Подробнее

Модуль содержит функции для загрузки информации о моделях с удаленного ресурса, форматирования этой информации, а также для чтения и сохранения данных о моделях в локальном файле. Он также предоставляет функцию для определения директории, в которой хранятся модели. Модуль используется для получения актуальной информации о доступных моделях и их параметрах.

## Функции

### `load_models`

```python
def load_models():
    """
    Загружает информацию о моделях с удаленного ресурса.

    Returns:
        dict: Отформатированный словарь с информацией о моделях.

    Raises:
        requests.exceptions.HTTPError: Если HTTP запрос завершается с ошибкой.
    
    Как работает функция:
    1. Выполняется GET-запрос к URL "https://gpt4all.io/models/models3.json".
    2. Вызывается функция `raise_for_status` для проверки статуса ответа. Если статус указывает на ошибку (например, 404, 500), выбрасывается исключение `HTTPError`.
    3. Если запрос успешен, ответ преобразуется в JSON-формат.
    4. Вызывается функция `format_models` для преобразования JSON-данных в нужный формат.

    ASCII flowchart:
    A: GET request to "https://gpt4all.io/models/models3.json"
    ↓
    B: raise_for_status(response)
    ↓
    C: response.json()
    ↓
    D: format_models(response.json())
    ↓
    E: return (форматированный словарь)

    Пример:
        >>> models = load_models()
        >>> print(type(models))
        <class 'dict'>
    """
    ...
```

### `get_model_name`

```python
def get_model_name(filename: str) -> str:
    """
    Извлекает имя модели из имени файла, удаляя лишние суффиксы.

    Args:
        filename (str): Имя файла модели.

    Returns:
        str: Имя модели без суффиксов.
    
    Как работает функция:
    1. Имя файла разделяется по первому вхождению символа ".", чтобы отделить основное имя файла от расширения.
    2. В цикле перебираются суффиксы, которые необходимо удалить из имени модели (например, "-v1_5", "-q4_0" и т.д.).
    3. Каждый из этих суффиксов удаляется из имени.
    4. Возвращается очищенное имя модели.

    ASCII flowchart:
    A: filename.split(".", 1)[0]
    ↓
    B: Loop through replace in ["-v1_5", "-v1", "-q4_0", "_v01", "-v0", "-f16", "-gguf2", "-newbpe"]
    ↓
    C: name = name.replace(replace, "")
    ↓
    D: Return name

    Пример:
        >>> get_model_name("llama-2-7b-chat-v1.1-q4_0.gguf")
        'llama-2-7b-chat'
    """
    ...
```

### `format_models`

```python
def format_models(models: list) -> dict:
    """
    Форматирует список моделей в словарь, где ключом является имя модели.

    Args:
        models (list): Список моделей в формате JSON.

    Returns:
        dict: Словарь, где ключом является имя модели, а значением - словарь с информацией о модели.
    
    Как работает функция:
    1. Проходим по каждому элементу в списке моделей.
    2. Извлекаем имя файла (`model["filename"]`) и получаем имя модели с помощью функции `get_model_name`.
    3. Создаем словарь с информацией о модели, включающий путь к файлу (`model["filename"]`), требуемый объем оперативной памяти (`model["ramrequired"]`), шаблон промпта (`model["promptTemplate"]`, если он существует) и системный промпт (`model["systemPrompt"]`, если он существует).
    4. Формируем словарь, где ключом является имя модели, а значением - созданный словарь с информацией о модели.

    ASCII flowchart:
    A: Loop through model in models
    ↓
    B: get_model_name(model["filename"])
    ↓
    C: Create model_info dictionary
    ↓
    D: Return dictionary {model_name: model_info}

    Пример:
        >>> models = [{'filename': 'llama-2-7b-chat-v1.1-q4_0.gguf', 'ramrequired': '8 GB', 'promptTemplate': '<prompt>', 'systemPrompt': '<system>'}]
        >>> format_models(models)
        {'llama-2-7b-chat': {'path': 'llama-2-7b-chat-v1.1-q4_0.gguf', 'ram': '8 GB', 'prompt': '<prompt>', 'system': '<system>'}}
    """
    ...
```

### `read_models`

```python
def read_models(file_path: str):
    """
    Читает информацию о моделях из JSON-файла.

    Args:
        file_path (str): Путь к файлу с информацией о моделях.

    Returns:
        dict: Словарь с информацией о моделях.
    
    Как работает функция:
    1. Открывает файл по указанному пути в бинарном режиме для чтения.
    2. Загружает JSON-данные из файла и преобразует их в словарь.
    3. Возвращает полученный словарь.

    ASCII flowchart:
    A: Open file_path in binary read mode
    ↓
    B: json.load(f)
    ↓
    C: Return loaded data

    Пример:
        >>> read_models('models.json')
        {'llama-2-7b-chat': {'path': 'llama-2-7b-chat-v1.1-q4_0.gguf', 'ram': '8 GB', 'prompt': '<prompt>', 'system': '<system>'}}
    """
    ...
```

### `save_models`

```python
def save_models(file_path: str, data):
    """
    Сохраняет информацию о моделях в JSON-файл.

    Args:
        file_path (str): Путь к файлу для сохранения информации о моделях.
        data (dict): Данные для сохранения.
    
    Как работает функция:
    1. Открывает файл по указанному пути в режиме записи.
    2. Преобразует данные в JSON-формат и записывает их в файл с отступом в 4 пробела для читаемости.

    ASCII flowchart:
    A: Open file_path in write mode
    ↓
    B: json.dump(data, f, indent=4)
    ↓
    C: Close file

    Пример:
        >>> data = {'llama-2-7b-chat': {'path': 'llama-2-7b-chat-v1.1-q4_0.gguf', 'ram': '8 GB', 'prompt': '<prompt>', 'system': '<system>'}}
        >>> save_models('models.json', data)
    """
    ...
```

### `get_model_dir`

```python
def get_model_dir() -> str:
    """
    Определяет путь к директории, в которой хранятся модели.

    Returns:
        str: Путь к директории с моделями.
    
    Как работает функция:
    1. Определяет путь к текущей директории, где находится файл.
    2. Определяет путь к директории проекта, поднимаясь на два уровня вверх от текущей директории.
    3. Формирует путь к директории "models", объединяя путь к директории проекта и название директории "models".
    4. Проверяет, существует ли директория "models". Если нет, создает ее.
    5. Возвращает путь к директории "models".

    ASCII flowchart:
    A: Get current file directory
    ↓
    B: Get project directory (parent of parent)
    ↓
    C: model_dir = os.path.join(project_dir, "models")
    ↓
    D: Check if model_dir exists
    ↓
    E: Create model_dir if it doesn't exist
    ↓
    F: Return model_dir

    Пример:
        >>> get_model_dir()
        '/path/to/project/models'
    """
    ...
```

### `get_models`

```python
def get_models() -> dict[str, dict]:
    """
    Получает информацию о моделях из файла или загружает ее с удаленного ресурса, если файл не существует.

    Returns:
        dict[str, dict]: Словарь с информацией о моделях.
    
    Как работает функция:
    1. Определяет путь к директории с моделями с помощью функции `get_model_dir`.
    2. Формирует полный путь к файлу "models.json" в директории с моделями.
    3. Проверяет, существует ли файл "models.json".
    4. Если файл существует, читает информацию о моделях из файла с помощью функции `read_models`.
    5. Если файл не существует, загружает информацию о моделях с удаленного ресурса с помощью функции `load_models`, сохраняет ее в файл с помощью функции `save_models`.
    6. Возвращает полученный словарь с информацией о моделях.

    ASCII flowchart:
    A: model_dir = get_model_dir()
    ↓
    B: file_path = os.path.join(model_dir, "models.json")
    ↓
    C: Check if file_path exists
    ↓
    D (If file exists): models = read_models(file_path)
    ↓
    E (If file doesn't exist): models = load_models()
    ↓
    F (If file doesn't exist): save_models(file_path, models)
    ↓
    G: Return models

    Пример:
        >>> get_models()
        {'llama-2-7b-chat': {'path': 'llama-2-7b-chat-v1.1-q4_0.gguf', 'ram': '8 GB', 'prompt': '<prompt>', 'system': '<system>'}}
    """
    ...