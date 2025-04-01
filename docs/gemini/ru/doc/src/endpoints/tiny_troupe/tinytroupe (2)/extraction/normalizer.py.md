# Модуль normalizer.py

## Обзор

Модуль `normalizer.py` предоставляет класс `Normalizer`, который используется для нормализации текстовых элементов, таких как фрагменты текста и концепции. Он использует OpenAI для преобразования элементов к стандартизированному виду, улучшая согласованность и упрощая дальнейшую обработку.

## Подробнее

Модуль содержит класс `Normalizer`, который инициализируется списком элементов для нормализации, количеством элементов для вывода и флагом verbosity. Класс использует OpenAI для генерации нормализованных элементов и предоставляет метод `normalize` для применения этих нормализованных форм к отдельным элементам или спискам элементов. Для повышения эффективности используется кэширование нормализованных элементов.

## Классы

### `Normalizer`

**Описание**: Механизм для нормализации фрагментов текста, концепций и других текстовых элементов.

**Принцип работы**:
1.  Класс инициализируется списком элементов, которые нужно нормализовать, количеством элементов для вывода (n) и флагом verbose.
2.  Удаляет дубликаты из списка элементов.
3.  Использует OpenAI для генерации нормализованных элементов, используя шаблоны mustache для составления сообщений к языковой модели.
4.  Реализует метод `normalize`, который применяет нормализованные формы к отдельным элементам или спискам элементов.
5.  Использует кэширование для повышения эффективности, сохраняя нормализованные формы в словаре `self.normalizing_map`.

**Атрибуты**:

*   `elements` (List[str]): Список элементов для нормализации.
*   `n` (int): Количество нормализованных элементов для вывода.
*   `verbose` (bool): Флаг, определяющий, нужно ли выводить отладочные сообщения.
*   `normalized_elements` (dict): JSON-структура, где каждый выходной элемент является ключом к списку входных элементов, объединенных в него.
*   `normalizing_map` (dict): Словарь, отображающий каждый входной элемент на его нормализованный вывод.

**Методы**:

*   `__init__(elements: List[str], n: int, verbose: bool = False)`: Инициализирует экземпляр класса `Normalizer`.
*   `normalize(element_or_elements: Union[str, List[str]]) -> Union[str, List[str]]`: Нормализует указанный элемент или элементы.

## Функции

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
```

**Назначение**: Инициализирует экземпляр класса `Normalizer`.

**Параметры**:

*   `elements` (List[str]): Список элементов для нормализации.
*   `n` (int): Количество нормализованных элементов для вывода.
*   `verbose` (bool, optional): Флаг, определяющий, нужно ли выводить отладочные сообщения. По умолчанию `False`.

**Как работает функция**:

1.  Удаляет дубликаты из списка `elements`, сохраняя уникальные элементы в `self.elements`.
2.  Инициализирует атрибуты `self.n` и `self.verbose` значениями, переданными в функцию.
3.  Инициализирует `self.normalized_elements` значением `None`.
4.  Инициализирует `self.normalizing_map` пустым словарем.
5.  Создает словарь `rendering_configs` с ключами `"n"` и `"elements"`, содержащими значения `n` и `self.elements` соответственно.
6.  Составляет сообщения для языковой модели (LLM), используя шаблоны mustache из файлов `normalizer.system.mustache` и `normalizer.user.mustache`.
7.  Отправляет сообщение в OpenAI, получает результат и сохраняет его в `next_message`.
8.  Извлекает JSON из содержимого сообщения и сохраняет его в `self.normalized_elements`.
9.  Выводит отладочные сообщения, если `self.verbose` имеет значение `True`.

**ASCII flowchart**:

```
A: Получение и обработка входных параметров (elements, n, verbose)
↓
B: Удаление дубликатов из elements
↓
C: Создание rendering_configs
↓
D: Композиция сообщений для LLM с использованием шаблонов mustache
↓
E: Отправка сообщения в OpenAI и получение результата
↓
F: Извлечение JSON из результата
↓
G: Сохранение результата в self.normalized_elements
```

**Примеры**:

```python
from tinytroupe.extraction.normalizer import Normalizer

elements = ["apple", "banana", "apple", "orange"]
n = 2
normalizer = Normalizer(elements, n, verbose=True)
print(normalizer.normalized_elements)
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
```

**Назначение**: Нормализует указанный элемент или элементы, используя кэширование для повышения производительности.

**Параметры**:

*   `element_or_elements` (Union[str, List[str]]): Элемент или элементы для нормализации.

**Возвращает**:

*   `str`: Нормализованный элемент, если входные данные были строкой.
*   `list`: Нормализованные элементы, если входные данные были списком, сохраняя порядок элементов во входных данных.

**Как работает функция**:

1.  Проверяет тип входных данных `element_or_elements`. Если это строка, преобразует её в список. Если это список, использует его напрямую. В противном случае вызывает исключение `ValueError`.
2.  Создает пустой список `normalized_elements` для хранения нормализованных элементов.
3.  Создает пустой список `elements_to_normalize` для хранения элементов, которые необходимо нормализовать.
4.  Проходит по каждому элементу в `denormalized_elements` и проверяет, есть ли он в `self.normalizing_map`. Если элемента нет в `self.normalizing_map`, добавляет его в `elements_to_normalize`.
5.  Если `elements_to_normalize` не пуст, создает словарь `rendering_configs` с категориями из `self.normalized_elements` и элементами для нормализации из `elements_to_normalize`.
6.  Составляет сообщения для языковой модели, используя шаблоны mustache из файлов `normalizer.applier.system.mustache` и `normalizer.applier.user.mustache`.
7.  Отправляет сообщение в OpenAI, получает результат и извлекает JSON из содержимого сообщения.
8.  Проверяет, что результат является списком и что длина списка совпадает с длиной `elements_to_normalize`.
9.  Проходит по каждому элементу в `elements_to_normalize` и сохраняет нормализованный элемент в `self.normalizing_map`.
10. Проходит по каждому элементу в `denormalized_elements` и добавляет нормализованный элемент из `self.normalizing_map` в `normalized_elements`.
11. Возвращает список нормализованных элементов.

**ASCII flowchart**:

```
A: Проверка типа входных данных (element_or_elements)
↓
B: Создание списков normalized_elements и elements_to_normalize
↓
C: Проверка наличия элементов в self.normalizing_map
↓
D: Если есть элементы для нормализации, композиция сообщений для LLM
↓
E: Отправка сообщения в OpenAI и получение результата
↓
F: Обновление self.normalizing_map
↓
G: Сборка списка normalized_elements из self.normalizing_map
↓
H: Возврат списка normalized_elements
```

**Примеры**:

```python
from tinytroupe.extraction.normalizer import Normalizer

elements = ["apple", "banana", "orange"]
n = 2
normalizer = Normalizer(elements, n, verbose=True)

# Пример нормализации одного элемента
normalized_element = normalizer.normalize("apple")
print(normalized_element)

# Пример нормализации списка элементов
normalized_elements = normalizer.normalize(["banana", "orange"])
print(normalized_elements)