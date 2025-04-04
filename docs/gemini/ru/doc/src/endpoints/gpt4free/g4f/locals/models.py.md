# Модуль для работы с моделями GPT4Free
=========================================

Модуль предоставляет функциональность для загрузки, форматирования, чтения и сохранения информации о моделях, используемых в проекте GPT4Free. Он также содержит функции для управления каталогом моделей.

## Обзор

Этот модуль содержит функции, необходимые для получения и обработки информации о моделях, используемых в gpt4free. Он включает в себя загрузку данных о моделях из внешнего источника, форматирование этих данных и сохранение их локально для дальнейшего использования. Модуль также предоставляет функции для работы с каталогом моделей, такие как создание каталога, если он не существует, и определение пути к нему.

## Подробнее

Модуль `models.py` отвечает за управление информацией о моделях, используемых в проекте `gpt4free`. Он загружает данные о моделях с удаленного ресурса, форматирует их, сохраняет локально и предоставляет доступ к ним. Это позволяет избежать повторной загрузки данных о моделях при каждом запуске и обеспечивает более быстрый доступ к ним.

## Функции

### `load_models`

```python
def load_models() -> dict:
    """
    Загружает данные о моделях с удаленного ресурса.

    Returns:
        dict: Словарь с информацией о моделях.

    Raises:
        requests.exceptions.HTTPError: Если запрос завершается с ошибкой HTTP.

    Как работает функция:
    1. Выполняет GET-запрос к URL "https://gpt4all.io/models/models3.json".
    2. Проверяет статус ответа с помощью `raise_for_status(response)`.
    3. Форматирует полученные данные с помощью `format_models(response.json())`.
    4. Возвращает словарь с информацией о моделях.

    ASCII flowchart:

    Запрос к API
    ↓
    Проверка статуса HTTP
    ↓
    Форматирование данных
    ↓
    Возврат словаря моделей

    Примеры:
        >>> load_models()
        {'model_name': {'path': 'model_filename', 'ram': 'ram_required', 'prompt': 'prompt_template', 'system': 'system_prompt'}, ...}
    """
    ...
```

### `get_model_name`

```python
def get_model_name(filename: str) -> str:
    """
    Извлекает имя модели из имени файла.

    Args:
        filename (str): Имя файла модели.

    Returns:
        str: Имя модели.

    Как работает функция:
    1. Разделяет имя файла на части по точке, беря первую часть.
    2. Удаляет из имени различные суффиксы, такие как "-v1_5", "-v1", "-q4_0", "_v01", "-v0", "-f16", "-gguf2", "-newbpe".
    3. Возвращает очищенное имя модели.

    ASCII flowchart:

    Имя файла
    ↓
    Разделение по точке
    ↓
    Удаление суффиксов
    ↓
    Возврат имени модели

    Примеры:
        >>> get_model_name("model-v1_5.bin")
        'model'
        >>> get_model_name("another_model-q4_0.bin")
        'another_model'
    """
    ...
```

### `format_models`

```python
def format_models(models: list) -> dict:
    """
    Форматирует список моделей в словарь, используя имя модели в качестве ключа.

    Args:
        models (list): Список моделей.

    Returns:
        dict: Словарь моделей, где ключ - имя модели.

    Как работает функция:
    1. Преобразует список моделей в словарь.
    2. Ключом словаря является имя модели, полученное с помощью `get_model_name(model["filename"])`.
    3. Значением словаря является словарь с информацией о модели, такой как путь к файлу, требуемая оперативная память, шаблон подсказки и системное сообщение.

    ASCII flowchart:

    Список моделей
    ↓
    Преобразование в словарь
    ↓
    Извлечение имени модели
    ↓
    Формирование словаря модели
    ↓
    Возврат словаря моделей

    Примеры:
        >>> models = [{"filename": "model-v1.bin", "ramrequired": "8GB", "promptTemplate": "template", "systemPrompt": "system"}]
        >>> format_models(models)
        {'model': {'path': 'model-v1.bin', 'ram': '8GB', 'prompt': 'template', 'system': 'system'}}
    """
    ...
```

### `read_models`

```python
def read_models(file_path: str) -> dict:
    """
    Читает данные о моделях из файла JSON.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        dict: Словарь с информацией о моделях.

    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: Если файл не является корректным JSON.

    Как работает функция:
    1. Открывает файл по указанному пути в режиме чтения байтов.
    2. Загружает данные из файла как JSON.
    3. Возвращает словарь с информацией о моделях.

    ASCII flowchart:

    Путь к файлу
    ↓
    Открытие файла
    ↓
    Чтение JSON
    ↓
    Возврат словаря моделей

    Примеры:
        >>> # Создайте файл models.json с данными о моделях
        >>> import json
        >>> data = {"model1": {"path": "path1"}, "model2": {"path": "path2"}}
        >>> with open("models.json", "w") as f:
        ...     json.dump(data, f)
        >>> read_models("models.json")
        {'model1': {'path': 'path1'}, 'model2': {'path': 'path2'}}
    """
    ...
```

### `save_models`

```python
def save_models(file_path: str, data: dict) -> None:
    """
    Сохраняет данные о моделях в файл JSON.

    Args:
        file_path (str): Путь к файлу.
        data (dict): Данные для сохранения.

    Raises:
        IOError: Если возникает ошибка при записи в файл.

    Как работает функция:
    1. Открывает файл по указанному пути в режиме записи.
    2. Записывает данные в файл в формате JSON с отступами для читаемости.

    ASCII flowchart:

    Путь к файлу, данные
    ↓
    Открытие файла
    ↓
    Запись JSON
    ↓
    Закрытие файла

    Примеры:
        >>> data = {"model1": {"path": "path1"}, "model2": {"path": "path2"}}
        >>> save_models("models.json", data)
        >>> # Проверьте содержимое файла models.json
    """
    ...
```

### `get_model_dir`

```python
def get_model_dir() -> str:
    """
    Определяет и возвращает путь к каталогу моделей.

    Returns:
        str: Путь к каталогу моделей.

    Как работает функция:
    1. Определяет путь к текущему файлу.
    2. Определяет путь к корневому каталогу проекта.
    3. Формирует путь к каталогу моделей как подкаталог корневого каталога проекта.
    4. Если каталог моделей не существует, он создается.
    5. Возвращает путь к каталогу моделей.

    ASCII flowchart:

    Определение пути к файлу
    ↓
    Определение пути к проекту
    ↓
    Формирование пути к каталогу моделей
    ↓
    Проверка существования каталога
    ↓
    Создание каталога (если необходимо)
    ↓
    Возврат пути к каталогу моделей

    Примеры:
        >>> get_model_dir()
        '/path/to/project/models'  # Фактический путь зависит от структуры вашего проекта
    """
    ...
```

### `get_models`

```python
def get_models() -> dict[str, dict]:
    """
    Получает данные о моделях из файла, если он существует, иначе загружает их с удаленного ресурса и сохраняет в файл.

    Returns:
        dict[str, dict]: Словарь с информацией о моделях.

    Как работает функция:
    1. Получает путь к каталогу моделей с помощью `get_model_dir()`.
    2. Формирует путь к файлу models.json в каталоге моделей.
    3. Если файл существует, читает данные о моделях из файла с помощью `read_models(file_path)`.
    4. Если файл не существует, загружает данные о моделях с помощью `load_models()`, сохраняет их в файл с помощью `save_models(file_path, models)` и возвращает загруженные данные.

    ASCII flowchart:

    Получение пути к каталогу моделей
    ↓
    Формирование пути к файлу
    ↓
    Проверка существования файла
    ├── Да → Чтение данных из файла
    └── Нет → Загрузка данных с удаленного ресурса
                ↓
                Сохранение данных в файл
                ↓
                Возврат загруженных данных
    Примеры:
        >>> get_models()
        {'model_name': {'path': 'model_filename', 'ram': 'ram_required', 'prompt': 'prompt_template', 'system': 'system_prompt'}, ...}
    """
    ...