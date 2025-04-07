# Модуль для профилирования агентов Tiny Troupe

## Обзор

Модуль `profiling.py` предоставляет механизмы для понимания характеристик популяций агентов, таких как их возрастное распределение, типичные интересы и так далее. Он содержит класс `Profiler`, который используется для анализа и визуализации данных об агентах.

## Подробнее

Этот модуль позволяет профилировать агентов на основе заданных атрибутов, вычислять распределения этих атрибутов и визуализировать их в виде графиков. Это полезно для понимания структуры и характеристик популяции агентов в симуляциях или других приложениях.

## Классы

### `Profiler`

**Описание**: Класс `Profiler` предназначен для профилирования агентов на основе заданных атрибутов. Он позволяет вычислять распределения атрибутов и визуализировать их.

**Принцип работы**:

1.  При инициализации класса задаются атрибуты для профилирования.
2.  Метод `profile` вычисляет распределения атрибутов для заданных агентов.
3.  Метод `render` визуализирует распределения атрибутов в виде графиков.

**Атрибуты**:

*   `attributes` (List[str]): Список атрибутов для профилирования. По умолчанию `["age", "occupation", "nationality"]`.
*   `attributes_distributions` (dict): Словарь, содержащий распределения атрибутов. Ключ - атрибут, значение - DataFrame с распределением.

**Методы**:

*   `__init__(attributes: List[str] = ["age", "occupation", "nationality"]) -> None`: Инициализирует класс `Profiler` с заданными атрибутами.
*   `profile(agents: List[dict]) -> dict`: Профилирует заданных агентов.
*   `render() -> None`: Визуализирует профиль агентов.
*   `_compute_attributes_distributions(agents: list) -> dict`: Вычисляет распределения атрибутов для заданных агентов.
*   `_compute_attribute_distribution(agents: list, attribute: str) -> pd.DataFrame`: Вычисляет распределение заданного атрибута для агентов.
*   `_plot_attributes_distributions() -> None`: Строит графики распределений атрибутов для агентов.
*   `_plot_attribute_distribution(attribute: str) -> pd.DataFrame`: Строит график распределения заданного атрибута для агентов.

## Функции

### `__init__`

```python
def __init__(self, attributes: List[str]=["age", "occupation", "nationality"]) -> None:
    """
    Args:
        attributes (List[str], optional): Атрибуты для профилирования. По умолчанию `["age", "occupation", "nationality"]`.
    
    Returns:
        None
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `Profiler`.

**Параметры**:

*   `attributes` (List[str], optional): Список атрибутов, которые будут использоваться для профилирования агентов. По умолчанию `["age", "occupation", "nationality"]`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Функция принимает список атрибутов для профилирования агентов. Если атрибуты не указаны, используются значения по умолчанию: `"age"`, `"occupation"` и `"nationality"`.
2.  Сохраняет список атрибутов в атрибуте `self.attributes`.
3.  Инициализирует пустой словарь `self.attributes_distributions` для хранения распределений атрибутов.

**Примеры**:

```python
# Пример 1: Инициализация Profiler с атрибутами по умолчанию
profiler = Profiler()

# Пример 2: Инициализация Profiler с пользовательскими атрибутами
profiler = Profiler(attributes=["age", "gender", "income"])
```

### `profile`

```python
def profile(self, agents: List[dict]) -> dict:
    """
    Args:
        agents (List[dict]): Агенты для профилирования.
    
    Returns:
        dict: Распределения атрибутов.
    """
    ...
```

**Назначение**: Профилирует заданных агентов.

**Параметры**:

*   `agents` (List[dict]): Список агентов для профилирования. Каждый агент представлен в виде словаря.

**Возвращает**:

*   `dict`: Словарь, содержащий распределения атрибутов для заданных агентов.

**Как работает функция**:

1.  Функция принимает список агентов, которых необходимо профилировать.
2.  Вызывает метод `_compute_attributes_distributions` для вычисления распределений атрибутов для заданных агентов.
3.  Сохраняет вычисленные распределения атрибутов в атрибуте `self.attributes_distributions`.
4.  Возвращает словарь распределений атрибутов.

**Примеры**:

```python
# Пример: Профилирование списка агентов
agents = [
    {"age": 25, "occupation": "engineer", "nationality": "US"},
    {"age": 30, "occupation": "doctor", "nationality": "UK"},
    {"age": 25, "occupation": "teacher", "nationality": "CA"},
]
profiler = Profiler()
attribute_distributions = profiler.profile(agents)
print(attribute_distributions)
```

### `render`

```python
def render(self) -> None:
    """
    Args:
        
    
    Returns:
        None
    """
    ...
```

**Назначение**: Визуализирует профиль агентов.

**Параметры**:

*   Нет

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает метод `_plot_attributes_distributions` для построения графиков распределений атрибутов.

**Примеры**:

```python
# Пример: Визуализация профиля агентов
agents = [
    {"age": 25, "occupation": "engineer", "nationality": "US"},
    {"age": 30, "occupation": "doctor", "nationality": "UK"},
    {"age": 25, "occupation": "teacher", "nationality": "CA"},
]
profiler = Profiler()
profiler.profile(agents)
profiler.render()
```

### `_compute_attributes_distributions`

```python
def _compute_attributes_distributions(self, agents: list) -> dict:
    """
    Args:
        agents (list): Агенты, для которых вычисляются распределения атрибутов.
    
    Returns:
        dict: Распределения атрибутов.
    """
    ...
```

**Назначение**: Вычисляет распределения атрибутов для заданных агентов.

**Параметры**:

*   `agents` (list): Список агентов, для которых необходимо вычислить распределения атрибутов.

**Возвращает**:

*   `dict`: Словарь, содержащий распределения атрибутов. Ключ - атрибут, значение - DataFrame с распределением.

**Как работает функция**:

1.  Инициализирует пустой словарь `distributions` для хранения распределений атрибутов.
2.  Для каждого атрибута в списке `self.attributes` вызывает метод `_compute_attribute_distribution` для вычисления распределения атрибута.
3.  Сохраняет вычисленное распределение атрибута в словаре `distributions`.
4.  Возвращает словарь распределений атрибутов.

**Примеры**:

```python
# Пример: Вычисление распределений атрибутов для списка агентов
agents = [
    {"age": 25, "occupation": "engineer", "nationality": "US"},
    {"age": 30, "occupation": "doctor", "nationality": "UK"},
    {"age": 25, "occupation": "teacher", "nationality": "CA"},
]
profiler = Profiler()
attribute_distributions = profiler._compute_attributes_distributions(agents)
print(attribute_distributions)
```

### `_compute_attribute_distribution`

```python
def _compute_attribute_distribution(self, agents: list, attribute: str) -> pd.DataFrame:
    """
    Args:
        agents (list): Агенты, для которых вычисляется распределение атрибута.
        attribute (str): Атрибут, распределение которого необходимо вычислить.
    
    Returns:
        pd.DataFrame: Данные, используемые для построения графика.
    """
    ...
```

**Назначение**: Вычисляет распределение заданного атрибута для агентов.

**Параметры**:

*   `agents` (list): Список агентов, для которых необходимо вычислить распределение атрибута.
*   `attribute` (str): Атрибут, распределение которого необходимо вычислить.

**Возвращает**:

*   `pd.DataFrame`: DataFrame, содержащий распределение атрибута.

**Как работает функция**:

1.  Извлекает значения заданного атрибута для каждого агента в списке `agents`.
2.  Создает DataFrame из извлеченных значений.
3.  Вычисляет количество каждого значения атрибута с помощью метода `value_counts`.
4.  Сортирует DataFrame по индексу (значению атрибута) с помощью метода `sort_index`.
5.  Возвращает DataFrame с распределением атрибута.

**Примеры**:

```python
# Пример: Вычисление распределения атрибута "age" для списка агентов
agents = [
    {"age": 25, "occupation": "engineer", "nationality": "US"},
    {"age": 30, "occupation": "doctor", "nationality": "UK"},
    {"age": 25, "occupation": "teacher", "nationality": "CA"},
]
profiler = Profiler()
age_distribution = profiler._compute_attribute_distribution(agents, "age")
print(age_distribution)
```

### `_plot_attributes_distributions`

```python
def _plot_attributes_distributions(self) -> None:
    """
    Args:
        
    
    Returns:
        None
    """
    ...
```

**Назначение**: Строит графики распределений атрибутов для агентов.

**Параметры**:

*   Нет

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Для каждого атрибута в списке `self.attributes` вызывает метод `_plot_attribute_distribution` для построения графика распределения атрибута.

**Примеры**:

```python
# Пример: Построение графиков распределений атрибутов для списка агентов
agents = [
    {"age": 25, "occupation": "engineer", "nationality": "US"},
    {"age": 30, "occupation": "doctor", "nationality": "UK"},
    {"age": 25, "occupation": "teacher", "nationality": "CA"},
]
profiler = Profiler()
profiler.profile(agents)
profiler._plot_attributes_distributions()
```

### `_plot_attribute_distribution`

```python
def _plot_attribute_distribution(self, attribute: str) -> pd.DataFrame:
    """
    Args:
        attribute (str): Атрибут, распределение которого необходимо построить.
    
    Returns:
        pd.DataFrame: Данные, используемые для построения графика.
    """
    ...
```

**Назначение**: Строит график распределения заданного атрибута для агентов.

**Параметры**:

*   `attribute` (str): Атрибут, распределение которого необходимо построить.

**Возвращает**:

*   `pd.DataFrame`: DataFrame, содержащий данные, используемые для построения графика.

**Как работает функция**:

1.  Извлекает DataFrame с распределением атрибута из словаря `self.attributes_distributions`.
2.  Строит столбчатый график распределения атрибута с помощью метода `plot(kind='bar')`.
3.  Добавляет заголовок к графику, содержащий название атрибута.
4.  Отображает график с помощью функции `plt.show()`.

**Примеры**:

```python
# Пример: Построение графика распределения атрибута "age" для списка агентов
agents = [
    {"age": 25, "occupation": "engineer", "nationality": "US"},
    {"age": 30, "occupation": "doctor", "nationality": "UK"},
    {"age": 25, "occupation": "teacher", "nationality": "CA"},
]
profiler = Profiler()
profiler.profile(agents)
profiler._plot_attribute_distribution("age")