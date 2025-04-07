# Модуль для загрузки примеров спецификаций агентов и фрагментов

## Обзор

Модуль предоставляет функции для загрузки и перечисления примеров спецификаций агентов и фрагментов, хранящихся в формате JSON. Эти функции полезны для демонстрации и тестирования, позволяя быстро загружать предварительно настроенные спецификации агентов и фрагментов.

## Подробней

Этот модуль предоставляет набор функций для загрузки и перечисления примеров агентов и фрагментов. Он использует функции `json.load` и `os.path.join` для загрузки JSON-файлов из соответствующих директорий (`./agents` и `./fragments`). Модуль предназначен для упрощения процесса загрузки примеров конфигураций, что полезно при разработке и тестировании.

## Функции

### `load_example_agent_specification`

```python
def load_example_agent_specification(name: str) -> dict:
    """
    Load an example agent specification.

    Args:
        name (str): The name of the agent.

    Returns:
        dict: The agent specification.
    """
```

**Назначение**: Загружает пример спецификации агента из JSON-файла.

**Параметры**:
- `name` (str): Имя агента, соответствующее имени файла (без расширения `.agent.json`).

**Возвращает**:
- `dict`: Словарь, представляющий спецификацию агента.

**Как работает функция**:
1. Функция принимает имя агента (`agent_name`).
2. Формирует путь к файлу спецификации агента (`./agents/{agent_name}.agent.json`).
3. Открывает JSON-файл и загружает его содержимое в словарь.
4. Возвращает полученный словарь.

```ascii
    Начало
    │
    ├── Получение имени агента (agent_name)
    │
    ├── Формирование пути к файлу: filename = os.path.join(os.path.dirname(__file__), f'./agents/{agent_name}.agent.json')
    │
    ├── Открытие файла: open(filename)
    │
    ├── Загрузка JSON: json.load(file)
    │
    └── Возврат словаря с данными
    │
    Конец
```

**Примеры**:

```python
agent_spec = load_example_agent_specification(name='my_agent')
print(agent_spec)
# {'name': 'my_agent', 'description': 'Пример агента'}
```

### `load_example_fragment_specification`

```python
def load_example_fragment_specification(name: str) -> dict:
    """
    Load an example fragment specification.

    Args:
        name (str): The name of the fragment.

    Returns:
        dict: The fragment specification.
    """
```

**Назначение**: Загружает пример спецификации фрагмента из JSON-файла.

**Параметры**:
- `name` (str): Имя фрагмента, соответствующее имени файла (без расширения `.fragment.json`).

**Возвращает**:
- `dict`: Словарь, представляющий спецификацию фрагмента.

**Как работает функция**:
1. Функция принимает имя фрагмента (`fragment_name`).
2. Формирует путь к файлу спецификации фрагмента (`./fragments/{fragment_name}.fragment.json`).
3. Открывает JSON-файл и загружает его содержимое в словарь.
4. Возвращает полученный словарь.

```ascii
    Начало
    │
    ├── Получение имени фрагмента (fragment_name)
    │
    ├── Формирование пути к файлу: filename = os.path.join(os.path.dirname(__file__), f'./fragments/{fragment_name}.fragment.json')
    │
    ├── Открытие файла: open(filename)
    │
    ├── Загрузка JSON: json.load(file)
    │
    └── Возврат словаря с данными
    │
    Конец
```

**Примеры**:

```python
fragment_spec = load_example_fragment_specification(name='my_fragment')
print(fragment_spec)
# {'name': 'my_fragment', 'description': 'Пример фрагмента'}
```

### `list_example_agents`

```python
def list_example_agents() -> list:
    """
    List the available example agents.

    Returns:
        list: A list of the available example agents.
    """
```

**Назначение**: Возвращает список доступных примеров агентов.

**Возвращает**:
- `list`: Список строк, содержащих имена доступных агентов (без расширения `.agent.json`).

**Как работает функция**:
1. Функция получает список файлов в директории `./agents`.
2. Удаляет расширение `.agent.json` из каждого имени файла.
3. Возвращает список имен агентов.

```ascii
    Начало
    │
    ├── Получение списка файлов в директории агентов: files = os.listdir(os.path.join(os.path.dirname(__file__), './agents'))
    │
    ├── Исключение расширений '.agent.json' из каждого файла
    │
    └── Возврат списка имен агентов
    │
    Конец
```

**Примеры**:

```python
agent_list = list_example_agents()
print(agent_list)
# ['my_agent', 'another_agent']
```

### `list_example_fragments`

```python
def list_example_fragments() -> list:
    """
    List the available example fragments.

    Returns:
        list: A list of the available example fragments.
    """
```

**Назначение**: Возвращает список доступных примеров фрагментов.

**Возвращает**:
- `list`: Список строк, содержащих имена доступных фрагментов (без расширения `.fragment.json`).

**Как работает функция**:
1. Функция получает список файлов в директории `./fragments`.
2. Удаляет расширение `.fragment.json` из каждого имени файла.
3. Возвращает список имен фрагментов.

```ascii
    Начало
    │
    ├── Получение списка файлов в директории фрагментов: files = os.listdir(os.path.join(os.path.dirname(__file__), './fragments'))
    │
    ├── Исключение расширений '.fragment.json' из каждого файла
    │
    └── Возврат списка имен фрагментов
    │
    Конец
```

**Примеры**:

```python
fragment_list = list_example_fragments()
print(fragment_list)
# ['my_fragment', 'another_fragment']