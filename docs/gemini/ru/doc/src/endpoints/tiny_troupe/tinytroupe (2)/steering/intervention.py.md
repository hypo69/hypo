# Модуль `intervention.py`

## Обзор

Модуль `intervention.py` предназначен для реализации механизма вмешательства (интервенции) в симуляции, проводимые в рамках проекта `hypotez`. Он содержит класс `Intervention`, который позволяет определять условия и эффекты воздействия на целевые объекты, такие как виртуальные личности (`TinyPerson`) или виртуальные миры (`TinyWorld`). Модуль предоставляет инструменты для задания предварительных условий (preconditions) в виде текста или функций, а также для определения эффектов, применяемых при выполнении этих условий.

## Подробней

Модуль `intervention.py` играет важную роль в управлении ходом экспериментов в симуляциях. Он позволяет моделировать различные сценарии, в которых необходимо вмешиваться в происходящие процессы, чтобы изменить поведение агентов или состояние окружающей среды. Это может быть полезно для изучения влияния различных факторов на систему, а также для проверки гипотез о том, как определенные действия могут привести к желаемым результатам.

## Классы

### `Intervention`

**Описание**: Класс `Intervention` представляет собой механизм вмешательства в симуляцию. Он позволяет задавать условия, при которых должно произойти вмешательство, и эффекты, которые должны быть применены при выполнении этих условий.

**Принцип работы**:
1.  При инициализации класса задаются цели вмешательства (`targets`), а также параметры контекста (`first_n`, `last_n`).
2.  Определяются предварительные условия (`text_precondition`, `precondition_func`) и эффект (`effect_func`).
3.  Метод `execute` проверяет выполнение предварительных условий и, если они выполнены, применяет эффект к целям вмешательства.

**Атрибуты**:

*   `targets` (Union[TinyPerson, TinyWorld, List[TinyPerson], List[TinyWorld]]): Цель или цели вмешательства. Это могут быть отдельные личности (`TinyPerson`), миры (`TinyWorld`) или списки личностей и миров.
*   `first_n` (int, optional): Количество первых взаимодействий, учитываемых в контексте. По умолчанию `None`.
*   `last_n` (int, optional): Количество последних взаимодействий (самых последних), учитываемых в контексте. По умолчанию `5`.
*   `name` (str, optional): Имя вмешательства. Если не указано, генерируется автоматически.
*   `text_precondition` (str, optional): Текстовое представление предварительного условия, которое интерпретируется языковой моделью. По умолчанию `None`.
*   `precondition_func` (function, optional): Функция, представляющая предварительное условие, которое должно быть выполнено. Функция должна принимать цели вмешательства в качестве аргумента и возвращать булево значение. По умолчанию `None`.
*   `effect_func` (function, optional): Функция, представляющая эффект вмешательства. Функция должна принимать цели вмешательства в качестве аргумента и применять к ним соответствующие изменения. По умолчанию `None`.
*   `_last_text_precondition_proposition` (Proposition, optional): Последнее предложение, использованное для проверки текстового предварительного условия. По умолчанию `None`.
*   `_last_functional_precondition_check` (bool, optional): Результат последней проверки функционального предварительного условия. По умолчанию `None`.

**Методы**:

*   `__init__(self, targets, first_n=None, last_n=5, name=None)`: Инициализирует объект вмешательства.
*   `__call__(self)`: Выполняет вмешательство, вызывая метод `execute`.
*   `execute(self)`: Проверяет предварительные условия и, если они выполнены, применяет эффект. Возвращает `True`, если эффект был применен, и `False` в противном случае.
*   `check_precondition(self)`: Проверяет, выполнены ли предварительные условия для вмешательства.
*   `apply_effect(self)`: Применяет эффект вмешательства к целям.
*   `set_textual_precondition(self, text)`: Устанавливает текстовое предварительное условие.
*   `set_functional_precondition(self, func)`: Устанавливает функциональное предварительное условие.
*   `set_effect(self, effect_func)`: Устанавливает эффект вмешательства.
*   `precondition_justification(self)`: Возвращает обоснование для предварительного условия.

## Функции

### `__init__`

```python
def __init__(self, targets: Union[TinyPerson, TinyWorld, List[TinyPerson], List[TinyWorld]], 
                 first_n:int=None, last_n:int=5,
                 name: str = None):
```

**Назначение**: Инициализирует объект класса `Intervention`.

**Параметры**:

*   `targets` (Union[TinyPerson, TinyWorld, List[TinyPerson], List[TinyWorld]]): Цель или цели вмешательства. Это могут быть отдельные личности (`TinyPerson`), миры (`TinyWorld`) или списки личностей и миров.
*   `first_n` (int, optional): Количество первых взаимодействий, учитываемых в контексте. По умолчанию `None`.
*   `last_n` (int, optional): Количество последних взаимодействий (самых последних), учитываемых в контексте. По умолчанию `5`.
*   `name` (str, optional): Имя вмешательства. Если не указано, генерируется автоматически.

**Как работает функция**:
1.  Функция принимает цели (`targets`), параметры контекста (`first_n`, `last_n`) и имя (`name`) в качестве аргументов.
2.  Инициализирует атрибуты класса, такие как `targets`, `first_n`, `last_n` и `name`.
3.  Инициализирует атрибуты для хранения предварительных условий (`text_precondition`, `precondition_func`) и эффекта (`effect_func`).
4.  Если имя не указано, генерирует уникальный идентификатор и использует его для имени вмешательства.

```
    Начало
    │
    ├───> Присвоение аргументов атрибутам класса
    │
    ├───> Инициализация атрибутов для предварительных условий и эффекта
    │
    └───> Проверка наличия имени
         │
         └───> Если имя не указано:
              │   Создание уникального идентификатора и присвоение его имени
              │
              └───> Если имя указано:
                  │   Присвоение имени атрибуту `name`
                  │
                  └───> Конец
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.steering.intervention import Intervention

# Пример 1: Создание вмешательства для TinyPerson
person = TinyPerson()
intervention1 = Intervention(targets=person, name="Intervention for Person")

# Пример 2: Создание вмешательства для TinyWorld с указанием first_n и last_n
world = TinyWorld()
intervention2 = Intervention(targets=world, first_n=10, last_n=3, name="Intervention for World")

# Пример 3: Создание вмешательства для списка TinyPerson и TinyWorld
targets = [TinyPerson(), TinyWorld()]
intervention3 = Intervention(targets=targets, name="Intervention for List")
```

### `__call__`

```python
def __call__(self):
```

**Назначение**: Позволяет вызывать объект класса `Intervention` как функцию.

**Возвращает**:

*   `bool`: Возвращает `True`, если эффект вмешательства был применен, и `False` в противном случае.

**Как работает функция**:

1.  Функция вызывает метод `execute` класса `Intervention`.
2.  Метод `execute` проверяет предварительные условия и, если они выполнены, применяет эффект.

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Вызов объекта Intervention как функции
result = intervention()  # Эквивалентно intervention.execute()
print(f"Intervention applied: {result}")
```

### `execute`

```python
def execute(self):
```

**Назначение**: Выполняет вмешательство. Проверяет предварительные условия и, если они выполнены, применяет эффект.

**Возвращает**:

*   `bool`: Возвращает `True`, если эффект вмешательства был применен, и `False` в противном случае.

**Как работает функция**:

1.  Логирует начало выполнения вмешательства.
2.  Вызывает метод `check_precondition` для проверки предварительных условий.
3.  Если предварительные условия выполнены, вызывает метод `apply_effect` для применения эффекта.
4.  Логирует результат применения эффекта.

```
    Начало
    │
    ├───> Логирование начала выполнения вмешательства
    │
    ├───> Проверка предварительных условий
    │    │
    │    └───> Если предварительные условия выполнены:
    │         │   Применение эффекта
    │         │   Логирование применения эффекта
    │         │   Возврат True
    │         │
    │         └───> Если предварительные условия не выполнены:
    │              │   Логирование отсутствия применения эффекта
    │              │   Возврат False
    │
    └───> Конец
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Определение предварительного условия и эффекта (примеры)
def precondition(target):
    return True  # Всегда выполняем эффект

def effect(target):
    print("Effect applied!")

intervention.set_functional_precondition(precondition)
intervention.set_effect(effect)

# Выполнение вмешательства
result = intervention.execute()
print(f"Intervention applied: {result}")
```

### `check_precondition`

```python
def check_precondition(self):
```

**Назначение**: Проверяет, выполнены ли предварительные условия для вмешательства.

**Возвращает**:

*   `bool`: Возвращает `True`, если все предварительные условия выполнены, и `False` в противном случае.

**Как работает функция**:

1.  Создает объект `Proposition` для проверки текстового предварительного условия.
2.  Проверяет, установлено ли функциональное предварительное условие.
3.  Если функциональное предварительное условие установлено, вызывает его для проверки.
4.  Если функциональное предварительное условие не установлено, устанавливает значение по умолчанию `True`.
5.  Проверяет выполнение текстового предварительного условия с помощью `llm_precondition_check`.
6.  Возвращает результат логического `И` между `llm_precondition_check` и результатом проверки функционального предварительного условия.

```
    Начало
    │
    ├───> Создание объекта Proposition для проверки текстового предварительного условия
    │
    ├───> Проверка наличия функционального предварительного условия
    │    │
    │    └───> Если функциональное предварительное условие установлено:
    │         │   Вызов функционального предварительного условия для проверки
    │         │
    │         └───> Если функциональное предварительное условие не установлено:
    │              │   Установка значения по умолчанию True
    │
    ├───> Проверка выполнения текстового предварительного условия (llm_precondition_check)
    │
    └───> Возврат результата логического И между llm_precondition_check и результатом проверки функционального предварительного условия
         │
         └───> Конец
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Определение предварительного условия (пример)
def precondition(target):
    return True  # Всегда выполняем эффект

intervention.set_functional_precondition(precondition)

# Проверка предварительного условия
result = intervention.check_precondition()
print(f"Precondition met: {result}")
```

### `apply_effect`

```python
def apply_effect(self):
```

**Назначение**: Применяет эффект вмешательства к целям.

**Как работает функция**:

1.  Вызывает функцию эффекта (`effect_func`), передавая ей цели вмешательства (`targets`).

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Определение эффекта (пример)
def effect(target):
    print("Effect applied!")

intervention.set_effect(effect)

# Применение эффекта
intervention.apply_effect()
```

### `set_textual_precondition`

```python
def set_textual_precondition(self, text):
```

**Назначение**: Устанавливает текстовое предварительное условие.

**Параметры**:

*   `text` (str): Текст предварительного условия.

**Возвращает**:

*   `self`: Возвращает объект `Intervention` для возможности chaining.

**Как работает функция**:

1.  Присваивает переданный текст атрибуту `text_precondition`.
2.  Возвращает `self`.

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Установка текстового предварительного условия
intervention.set_textual_precondition("The person is happy")
```

### `set_functional_precondition`

```python
def set_functional_precondition(self, func):
```

**Назначение**: Устанавливает функциональное предварительное условие.

**Параметры**:

*   `func` (function): Функция предварительного условия.

**Возвращает**:

*   `self`: Возвращает объект `Intervention` для возможности chaining.

**Как работает функция**:

1.  Присваивает переданную функцию атрибуту `precondition_func`.
2.  Возвращает `self`.

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Определение функционального предварительного условия
def precondition(target):
    return True

# Установка функционального предварительного условия
intervention.set_functional_precondition(precondition)
```

### `set_effect`

```python
def set_effect(self, effect_func):
```

**Назначение**: Устанавливает эффект вмешательства.

**Параметры**:

*   `effect_func` (function): Функция эффекта.

**Возвращает**:

*   `self`: Возвращает объект `Intervention` для возможности chaining.

**Как работает функция**:

1.  Присваивает переданную функцию атрибуту `effect_func`.
2.  Возвращает `self`.

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Определение эффекта
def effect(target):
    print("Effect applied!")

# Установка эффекта
intervention.set_effect(effect)
```

### `precondition_justification`

```python
def precondition_justification(self):
```

**Назначение**: Возвращает обоснование для предварительного условия.

**Возвращает**:

*   `str`: Возвращает строку с обоснованием для предварительного условия.

**Как работает функция**:

1.  Проверяет наличие `_last_text_precondition_proposition`.
2.  Если `_last_text_precondition_proposition` существует, добавляет его обоснование и уверенность в строку обоснования.
3.  Если `_last_text_precondition_proposition` не существует, проверяет значение `_last_functional_precondition_check`.
4.  Если `_last_functional_precondition_check` равно `True`, добавляет сообщение об успешном выполнении функционального предварительного условия в строку обоснования.
5.  Если `_last_functional_precondition_check` не равно `True`, добавляет сообщение о том, что предварительные условия не выполнены.
6.  Возвращает строку обоснования.

```
    Начало
    │
    ├───> Проверка наличия _last_text_precondition_proposition
    │    │
    │    └───> Если _last_text_precondition_proposition существует:
    │         │   Добавление обоснования и уверенности в строку обоснования
    │         │
    │         └───> Если _last_text_precondition_proposition не существует:
    │              │   Проверка значения _last_functional_precondition_check
    │              │   │
    │              │   └───> Если _last_functional_precondition_check равно True:
    │              │        │   Добавление сообщения об успешном выполнении функционального предварительного условия
    │              │        │
    │              │        └───> Если _last_functional_precondition_check не равно True:
    │              │             │   Добавление сообщения о том, что предварительные условия не выполнены
    │
    └───> Возврат строки обоснования
         │
         └───> Конец
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.intervention import Intervention

# Создание объекта Intervention
person = TinyPerson()
intervention = Intervention(targets=person, name="Example Intervention")

# Определение предварительного условия (пример)
def precondition(target):
    return True  # Всегда выполняем эффект

intervention.set_functional_precondition(precondition)

# Выполнение проверки предварительного условия
intervention.check_precondition()

# Получение обоснования
justification = intervention.precondition_justification()
print(f"Precondition justification: {justification}")