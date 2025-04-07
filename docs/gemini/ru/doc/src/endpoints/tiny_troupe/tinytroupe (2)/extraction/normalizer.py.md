# Модуль normalizer.py

## Обзор

Модуль `normalizer.py` предназначен для нормализации текстовых элементов, таких как фрагменты текста и концепции. Он содержит класс `Normalizer`, который использует языковую модель для объединения схожих элементов в один нормализованный элемент. Модуль включает механизмы кэширования для повышения производительности и обеспечивает сохранение порядка элементов при нормализации.

## Подробнее

Этот модуль играет важную роль в процессе извлечения информации, обеспечивая единообразие представления текстовых данных. Он использует шаблоны `mustache` для формирования запросов к языковой модели, что позволяет гибко настраивать процесс нормализации.

## Классы

### `Normalizer`

**Описание**: Класс `Normalizer` предназначен для нормализации текстовых элементов.

**Принцип работы**:
1.  **Инициализация**: При инициализации класса происходит настройка параметров нормализации, таких как количество выходных элементов (`n`) и список элементов для нормализации (`elements`). Также происходит создание структуры `normalized_elements`, которая хранит соответствия между нормализованными элементами и исходными элементами.
2.  **Нормализация**: Метод `normalize` выполняет нормализацию элементов, используя кэширование для повышения производительности. Если элемент уже был нормализован, он извлекается из кэша. В противном случае происходит обращение к языковой модели для нормализации элемента.

**Атрибуты**:

*   `elements` (List[str]): Список элементов для нормализации.
*   `n` (int): Количество нормализованных элементов для вывода.
*   `verbose` (bool): Флаг, определяющий, нужно ли выводить отладочные сообщения. По умолчанию `False`.
*   `normalized_elements` (dict): JSON-структура, где каждый выходной элемент является ключом к списку входных элементов, объединенных в него.
*   `normalizing_map` (dict): Словарь, который сопоставляет каждый входной элемент с его нормализованным выводом.

**Методы**:

*   `__init__(elements: List[str], n: int, verbose: bool = False)`: Инициализирует экземпляр класса `Normalizer`.
*   `normalize(element_or_elements: Union[str, List[str]]) -> Union[str, List[str]]`: Нормализует указанный элемент или элементы.

### `__init__`

```python
def __init__(self, elements:List[str], n:int, verbose:bool=False):
    """
    Normalizes the specified elements.

    Args:
        elements (list): The elements to normalize.
        n (int): The number of normalized elements to output.
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
    ...
```

**Назначение**: Инициализирует класс `Normalizer`, подготавливая данные и отправляя запрос к языковой модели для получения нормализованных элементов.

**Параметры**:

*   `elements` (List[str]): Список элементов для нормализации.
*   `n` (int): Количество нормализованных элементов, которые необходимо получить на выходе.
*   `verbose` (bool, optional): Флаг для включения/выключения отладочного режима. По умолчанию `False`.

**Как работает функция**:

1.  Удаляет дубликаты из списка элементов для нормализации, чтобы обеспечить уникальность обрабатываемых данных.
2.  Инициализирует атрибуты `n` и `verbose` значениями, переданными в аргументах.
3.  Создает словарь `rendering_configs`, содержащий элементы и количество нормализованных элементов, который будет использован для рендеринга шаблонов сообщений.
4.  Формирует сообщения для языковой модели, используя шаблоны `normalizer.system.mustache` и `normalizer.user.mustache`. Шаблоны рендерятся с использованием `rendering_configs`.
5.  Отправляет сообщение в языковую модель с использованием `openai_utils.client().send_message`, устанавливая температуру 0.1 для получения более детерминированных результатов.
6.  Извлекает JSON из ответа языковой модели, используя `utils.extract_json`.
7.  Сохраняет результат нормализации в атрибут `normalized_elements`.

```
Начало
  ↓
Удаление дубликатов из `elements`
  ↓
Инициализация атрибутов `n` и `verbose`
  ↓
Создание `rendering_configs`
  ↓
Формирование сообщений с использованием шаблонов Mustache
  ↓
Отправка сообщения в языковую модель
  ↓
Извлечение JSON из ответа
  ↓
Сохранение результата в `normalized_elements`
  ↓
Конец
```

### `normalize`

```python
def normalize(self, element_or_elements:Union[str, List[str]]) -> Union[str, List[str]]:
    """
    Normalizes the specified element or elements.

    This method uses a caching mechanism to improve performance. If an element has been normalized before, 
    its normalized form is stored in a cache (self.normalizing_map). When the same element needs to be 
    normalized again, the method will first check the cache and use the stored normalized form if available, 
    instead of normalizing the element again.

    The order of elements in the output will be the same as in the input. This is ensured by processing 
    the elements in the order they appear in the input and appending the normalized elements to the output 
    list in the same order.

    Args:
        element_or_elements (Union[str, List[str]]): The element or elements to normalize.

    Returns:
        str: The normalized element if the input was a string.
        list: The normalized elements if the input was a list, preserving the order of elements in the input.
    """
    ...
```

**Назначение**: Нормализует один или несколько элементов, используя кэширование для повышения производительности.

**Параметры**:

*   `element_or_elements` (Union[str, List[str]]): Элемент или список элементов для нормализации.

**Возвращает**:

*   `Union[str, List[str]]`: Нормализованный элемент или список нормализованных элементов.

**Как работает функция**:

1.  Определяет, является ли входной параметр строкой или списком. Если это строка, преобразует её в список для единообразной обработки.
2.  Проверяет, есть ли элементы, требующие нормализации, в кэше `self.normalizing_map`.
3.  Если есть элементы, отсутствующие в кэше, формирует запрос к языковой модели для их нормализации, используя шаблоны `normalizer.applier.system.mustache` и `normalizer.applier.user.mustache`.
4.  Обновляет кэш `self.normalizing_map` нормализованными элементами, полученными от языковой модели.
5.  Собирает список нормализованных элементов, используя кэш, и возвращает его.

```
Начало
  ↓
Определение типа входного параметра
  ↓
Проверка элементов в кэше
  ├──> Элемент найден в кэше: использовать кэшированное значение
  │
  └──> Элемент отсутствует в кэше:
       │  ↓
       │  Формирование запроса к языковой модели
       │  ↓
       │  Обновление кэша
  ↓
Сборка списка нормализованных элементов
  ↓
Конец
```
```python
#Примеры
normalizer = Normalizer(elements=['алгоритм', 'машинное обучение'], n = 2)

element = 'алгоритм'
normalizer.normalize(element)

elements = ['алгоритм', 'машинное обучение']
normalizer.normalize(elements)