# Модуль для профилирования агентов Tiny Troupe

## Обзор

Модуль `profiling.py` предназначен для анализа и понимания характеристик популяций агентов в симуляции Tiny Troupe. Он предоставляет механизмы для определения таких параметров, как распределение возраста, типичные интересы и другие атрибуты агентов.

## Подробней

Данный модуль содержит класс `Profiler`, который позволяет вычислять и визуализировать распределения атрибутов агентов. Это полезно для понимания демографических и поведенческих особенностей моделируемой популяции.

## Классы

### `Profiler`

**Описание**: Класс для профилирования агентов. Позволяет вычислять и отображать распределения атрибутов агентов, таких как возраст, профессия и национальность.

**Атрибуты**:

- `attributes` (List[str]): Список атрибутов для анализа распределения. По умолчанию `["age", "occupation", "nationality"]`.
- `attributes_distributions` (dict): Словарь, содержащий распределения атрибутов в виде DataFrame. Ключ - название атрибута, значение - DataFrame с распределением.

**Методы**:

- `__init__(attributes: List[str]=["age", "occupation", "nationality"]) -> None`: Инициализирует объект `Profiler` с заданным списком атрибутов.
- `profile(agents: List[dict]) -> dict`: Профилирует переданных агентов, вычисляя распределения атрибутов.
- `render() -> None`: Отображает профиль агентов, визуализируя распределения атрибутов.
- `_compute_attributes_distributions(agents: list) -> dict`: Вычисляет распределения для всех указанных атрибутов агентов.
- `_compute_attribute_distribution(agents: list, attribute: str) -> pd.DataFrame`: Вычисляет распределение заданного атрибута для агентов.
- `_plot_attributes_distributions() -> None`: Отображает распределения всех атрибутов.
- `_plot_attribute_distribution(attribute: str) -> pd.DataFrame`: Отображает распределение заданного атрибута.

## Функции

### `__init__`

```python
def __init__(self, attributes: List[str]=["age", "occupation", "nationality"]) -> None:
    """
    Инициализирует объект Profiler с заданным списком атрибутов.

    Args:
        attributes (List[str], optional): Список атрибутов для анализа распределения. По умолчанию `["age", "occupation", "nationality"]`.

    Returns:
        None
    """
    ...
```

**Назначение**: Инициализирует объект `Profiler`, устанавливая атрибуты, которые будут анализироваться.

**Параметры**:

- `attributes` (List[str], optional): Список атрибутов для анализа распределения. По умолчанию `["age", "occupation", "nationality"]`.

**Как работает функция**:

1.  Сохраняет переданный список атрибутов в атрибуте экземпляра `self.attributes`.
2.  Инициализирует пустой словарь `self.attributes_distributions` для хранения вычисленных распределений атрибутов.

```ascii
A[Установка атрибутов и инициализация словаря распределений]
↓
B[Сохранение атрибутов в self.attributes]
↓
C[Инициализация self.attributes_distributions как пустого словаря]
```

**Примеры**:

```python
profiler = Profiler()  # Использует атрибуты по умолчанию
profiler = Profiler(attributes=["age", "gender"])  # Задает кастомные атрибуты
```

### `profile`

```python
def profile(self, agents: List[dict]) -> dict:
    """
    Профилирует переданных агентов, вычисляя распределения атрибутов.

    Args:
        agents (List[dict]): Список агентов для профилирования.

    Returns:
        dict: Словарь с распределениями атрибутов.
    """
    ...
```

**Назначение**: Выполняет профилирование переданного списка агентов, вычисляя распределения их атрибутов.

**Параметры**:

- `agents` (List[dict]): Список агентов для профилирования. Каждый агент представлен в виде словаря.

**Возвращает**:

- `dict`: Словарь, где ключи - это атрибуты, а значения - DataFrame с распределениями этих атрибутов.

**Как работает функция**:

1.  Вызывает метод `_compute_attributes_distributions` для вычисления распределений атрибутов переданных агентов.
2.  Сохраняет вычисленные распределения в атрибуте экземпляра `self.attributes_distributions`.
3.  Возвращает словарь `self.attributes_distributions`.

```ascii
A[Прием списка агентов]
↓
B[Вызов _compute_attributes_distributions для вычисления распределений]
↓
C[Сохранение распределений в self.attributes_distributions]
↓
D[Возврат словаря self.attributes_distributions]
```

**Примеры**:

```python
agents = [{"age": 25, "occupation": "teacher"}, {"age": 30, "occupation": "doctor"}]
profiler = Profiler()
distributions = profiler.profile(agents)
print(distributions)
```

### `render`

```python
def render(self) -> None:
    """
    Отображает профиль агентов, визуализируя распределения атрибутов.
    """
    ...
```

**Назначение**: Визуализирует профиль агентов, отображая графики распределения атрибутов.

**Параметры**:
   - Отсутствуют

**Возвращает**:
   - None

**Как работает функция**:
1. Вызывает метод `_plot_attributes_distributions` для отображения графиков распределения атрибутов агентов.

```ascii
A[Вызов метода _plot_attributes_distributions]
↓
B[Отображение графиков распределения атрибутов]
```

**Примеры**:

```python
agents = [{"age": 25, "occupation": "teacher"}, {"age": 30, "occupation": "doctor"}]
profiler = Profiler()
profiler.profile(agents)
profiler.render()
```

### `_compute_attributes_distributions`

```python
def _compute_attributes_distributions(self, agents: list) -> dict:
    """
    Вычисляет распределения для всех указанных атрибутов агентов.

    Args:
        agents (list): Список агентов, для которых нужно вычислить распределения атрибутов.

    Returns:
        dict: Словарь, содержащий распределения атрибутов.
    """
    ...
```

**Назначение**: Вычисляет распределения для всех атрибутов, указанных в `self.attributes`, на основе данных переданных агентов.

**Параметры**:

- `agents` (list): Список агентов, для которых нужно вычислить распределения атрибутов.

**Возвращает**:

- `dict`: Словарь, где ключи - это атрибуты, а значения - DataFrame с распределениями этих атрибутов.

**Как работает функция**:

1.  Инициализирует пустой словарь `distributions` для хранения вычисленных распределений.
2.  Перебирает каждый атрибут в списке `self.attributes`.
3.  Для каждого атрибута вызывает метод `_compute_attribute_distribution` для вычисления распределения.
4.  Сохраняет вычисленное распределение в словаре `distributions`.
5.  Возвращает словарь `distributions`.

```ascii
A[Прием списка агентов]
↓
B[Инициализация словаря distributions]
↓
C[Перебор атрибутов в self.attributes]
    ↓
    D[Вызов _compute_attribute_distribution для текущего атрибута]
    ↓
    E[Сохранение распределения в словаре distributions]
↓
F[Возврат словаря distributions]
```

**Примеры**:

```python
agents = [{"age": 25, "occupation": "teacher"}, {"age": 30, "occupation": "doctor"}]
profiler = Profiler(attributes=["age", "occupation"])
distributions = profiler._compute_attributes_distributions(agents)
print(distributions)
```

### `_compute_attribute_distribution`

```python
def _compute_attribute_distribution(self, agents: list, attribute: str) -> pd.DataFrame:
    """
    Вычисляет распределение заданного атрибута для агентов.

    Args:
        agents (list): Список агентов, для которых нужно вычислить распределение атрибута.
        attribute (str): Атрибут, для которого нужно вычислить распределение.

    Returns:
        pd.DataFrame: DataFrame с распределением атрибута.
    """
    ...
```

**Назначение**: Вычисляет распределение значений заданного атрибута среди переданных агентов и возвращает его в виде DataFrame.

**Параметры**:

- `agents` (list): Список агентов, представленных в виде словарей.
- `attribute` (str): Название атрибута, для которого вычисляется распределение.

**Возвращает**:

- `pd.DataFrame`: DataFrame, содержащий распределение значений атрибута. Индекс DataFrame - это уникальные значения атрибута, а столбец - количество агентов с соответствующим значением. DataFrame отсортирован по индексу (значениям атрибута).

**Как работает функция**:

1.  Извлекает значения указанного атрибута для каждого агента в списке.
2.  Создает DataFrame из списка значений атрибута.
3.  Вычисляет количество вхождений каждого значения атрибута с помощью `value_counts()`.
4.  Сортирует DataFrame по индексу (значениям атрибута) с помощью `sort_index()`.
5.  Возвращает полученный DataFrame.

```ascii
A[Получение списка агентов и атрибута]
↓
B[Извлечение значений атрибута для каждого агента]
↓
C[Создание DataFrame из списка значений]
↓
D[Вычисление количества вхождений каждого значения]
↓
E[Сортировка DataFrame по индексу (значениям атрибута)]
↓
F[Возврат DataFrame]
```

**Примеры**:

```python
import pandas as pd
agents = [{"age": 25}, {"age": 30}, {"age": 25}]
profiler = Profiler()
df = profiler._compute_attribute_distribution(agents, "age")
print(df)
```

### `_plot_attributes_distributions`

```python
def _plot_attributes_distributions(self) -> None:
    """
    Отображает распределения всех атрибутов.
    """
    ...
```

**Назначение**: Отображает графики распределения для каждого атрибута, указанного в списке `self.attributes`.

**Параметры**:
    - Отсутствуют

**Возвращает**:
    - None

**Как работает функция**:

1.  Перебирает все атрибуты в списке `self.attributes`.
2.  Для каждого атрибута вызывает метод `_plot_attribute_distribution`, который отвечает за построение графика распределения.

```ascii
A[Перебор атрибутов в self.attributes]
    ↓
    B[Вызов _plot_attribute_distribution для текущего атрибута]
```

**Примеры**:

```python
agents = [{"age": 25, "occupation": "teacher"}, {"age": 30, "occupation": "doctor"}]
profiler = Profiler(attributes=["age", "occupation"])
profiler.profile(agents)
profiler._plot_attributes_distributions()
```

### `_plot_attribute_distribution`

```python
def _plot_attribute_distribution(self, attribute: str) -> pd.DataFrame:
    """
    Отображает распределение заданного атрибута.

    Args:
        attribute (str): Атрибут, распределение которого нужно отобразить.

    Returns:
        pd.DataFrame: DataFrame с данными, использованными для построения графика.
    """
    ...
```

**Назначение**: Отображает график распределения для заданного атрибута.

**Параметры**:

- `attribute` (str): Атрибут, распределение которого нужно отобразить.

**Возвращает**:

- `pd.DataFrame`: DataFrame, содержащий данные, использованные для построения графика.

**Как работает функция**:

1.  Извлекает DataFrame с распределением атрибута из словаря `self.attributes_distributions`.
2.  Строит столбчатую диаграмму (bar plot) на основе DataFrame.
3.  Добавляет заголовок к графику, содержащий название атрибута.
4.  Отображает график с помощью `plt.show()`.
5.  Возвращает DataFrame, использованный для построения графика.

```ascii
A[Получение атрибута]
↓
B[Извлечение DataFrame с распределением атрибута из self.attributes_distributions]
↓
C[Построение столбчатой диаграммы на основе DataFrame]
↓
D[Добавление заголовка к графику]
↓
E[Отображение графика с помощью plt.show()]
↓
F[Возврат DataFrame]
```

**Примеры**:

```python
import pandas as pd
import matplotlib.pyplot as plt
agents = [{"age": 25}, {"age": 30}, {"age": 25}]
profiler = Profiler()
profiler.profile(agents)
df = profiler._plot_attribute_distribution("age")
plt.close() # Закрываем график после создания
print(df)