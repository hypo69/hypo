# Модуль `intervention.py`

## Обзор

Модуль `intervention.py` предназначен для управления вмешательствами (interventions) в симуляции `TinyTroupe`. Он определяет класс `Intervention`, который позволяет задавать условия и эффекты вмешательств, применяемых к агентам (`TinyPerson`) или к миру (`TinyWorld`). Модуль предоставляет инструменты для определения предопределенных условий, проверки этих условий и применения соответствующих эффектов.

## Подробней

Этот модуль является частью системы управления поведением агентов в симуляции `TinyTroupe`. Он позволяет влиять на ход симуляции, изменяя состояние агентов или мира на основе заданных условий. Вмешательства могут быть основаны на анализе текста с использованием языковых моделей или на выполнении кода, проверяющего определенные условия.

## Классы

### `Intervention`

**Описание**: Класс `Intervention` представляет собой вмешательство, которое может быть применено к агентам (`TinyPerson`) или миру (`TinyWorld`) в симуляции.

**Принцип работы**:
Класс позволяет задавать цели (`targets`), условия (`preconditions`) и эффекты (`effects`) вмешательства. Условия могут быть текстовыми (анализируются языковой моделью) или функциональными (определяются кодом). Метод `execute` проверяет условия и, если они выполнены, применяет эффекты к указанным целям.

**Аттрибуты**:
- `targets` (Union[TinyPerson, TinyWorld, List[TinyPerson], List[TinyWorld]]): Цель вмешательства (агент, мир или список агентов/миров).
- `first_n` (int, optional): Количество первых взаимодействий для анализа контекста. По умолчанию `None`.
- `last_n` (int, optional): Количество последних взаимодействий для анализа контекста. По умолчанию `5`.
- `name` (str, optional): Имя вмешательства. Если не указано, генерируется автоматически.
- `text_precondition` (str, optional): Текстовое условие для проверки языковой моделью. По умолчанию `None`.
- `precondition_func` (function, optional): Функциональное условие для проверки кодом. По умолчанию `None`.
- `effect_func` (function, optional): Функция, определяющая эффект вмешательства. По умолчанию `None`.
- `_last_text_precondition_proposition` (Proposition, optional): Последнее предложение, использованное для проверки текстового условия. По умолчанию `None`.
- `_last_functional_precondition_check` (bool, optional): Результат последней проверки функционального условия. По умолчанию `None`.

**Методы**:
- `__init__`: Инициализирует объект вмешательства.
- `__call__`: Вызывает метод `execute` для выполнения вмешательства.
- `execute`: Проверяет условие и применяет эффект, если условие выполнено.
- `check_precondition`: Проверяет, выполнено ли условие для вмешательства.
- `apply_effect`: Применяет эффект вмешательства.
- `set_textual_precondition`: Устанавливает текстовое условие для вмешательства.
- `set_functional_precondition`: Устанавливает функциональное условие для вмешательства.
- `set_effect`: Устанавливает эффект вмешательства.
- `precondition_justification`: Возвращает обоснование для предопределенного условия.

## Функции

### `__init__`

```python
def __init__(self, targets: Union[TinyPerson, TinyWorld, List[TinyPerson], List[TinyWorld]], 
                 first_n:int=None, last_n:int=5,
                 name: str = None):
```

**Назначение**: Инициализирует объект вмешательства.

**Параметры**:
- `targets` (Union[TinyPerson, TinyWorld, List[TinyPerson], List[TinyWorld]]): Цель вмешательства (агент, мир или список агентов/миров).
- `first_n` (int, optional): Количество первых взаимодействий для анализа контекста. По умолчанию `None`.
- `last_n` (int, optional): Количество последних взаимодействий для анализа контекста. По умолчанию `5`.
- `name` (str, optional): Имя вмешательства. Если не указано, генерируется автоматически.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Инициализирует атрибуты объекта `Intervention`, устанавливая цели, количество первых и последних взаимодействий для анализа, а также имя вмешательства.
2. Инициализирует атрибуты для хранения текстового и функционального условий, а также функции эффекта.
3. Инициализирует атрибуты для хранения результатов последней проверки условий.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld

# Пример создания вмешательства для агента
agent = TinyPerson()
intervention_agent = Intervention(targets=agent, name="AgentIntervention")

# Пример создания вмешательства для мира
world = TinyWorld()
intervention_world = Intervention(targets=world, name="WorldIntervention")
```

### `__call__`

```python
def __call__(self):
```

**Назначение**: Позволяет вызывать объект `Intervention` как функцию.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: Возвращает `True`, если эффект вмешательства был применен, `False` в противном случае.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Вызывает метод `execute` для выполнения вмешательства.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Вызов вмешательства как функции
result = intervention()
print(f"Intervention applied: {result}")
```

### `execute`

```python
def execute(self):
```

**Назначение**: Выполняет вмешательство, проверяя условие и применяя эффект, если условие выполнено.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: Возвращает `True`, если эффект вмешательства был применен, `False` в противном случае.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Логирует начало выполнения вмешательства.
2. Вызывает метод `check_precondition` для проверки условия.
3. Если условие выполнено, вызывает метод `apply_effect` для применения эффекта и логирует это.
4. Возвращает `True`, если эффект был применен, `False` в противном случае.
5. Логирует, что условие не выполнено, и эффект не был применен.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Задание текстового условия и эффекта
intervention.set_textual_precondition("agent is happy")
intervention.set_effect(lambda x: print("Agent is now happier!"))

# Выполнение вмешательства
result = intervention.execute()
print(f"Intervention applied: {result}")
```

### `check_precondition`

```python
def check_precondition(self):
```

**Назначение**: Проверяет, выполнено ли условие для вмешательства.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: Возвращает `True`, если условие выполнено, `False` в противном случае.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Создает объект `Proposition` для проверки текстового условия с использованием языковой модели.
2. Если задана функциональное условие, выполняет его. В противном случае, функциональное условие считается выполненным по умолчанию.
3. Проверяет оба условия (текстовое и функциональное) и возвращает `True`, если оба выполнены, `False` в противном случае.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Задание текстового и функционального условий
intervention.set_textual_precondition("agent is happy")
intervention.set_functional_precondition(lambda x: True)

# Проверка условия
result = intervention.check_precondition()
print(f"Precondition met: {result}")
```

### `apply_effect`

```python
def apply_effect(self):
```

**Назначение**: Применяет эффект вмешательства.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Вызывает функцию эффекта `effect_func` с целью вмешательства в качестве аргумента. Важно отметить, что данная функция не проверяет предварительные условия; предполагается, что проверка была выполнена ранее.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Задание эффекта
intervention.set_effect(lambda x: print("Applying effect to agent!"))

# Применение эффекта
intervention.apply_effect()
```

### `set_textual_precondition`

```python
def set_textual_precondition(self, text):
```

**Назначение**: Устанавливает текстовое условие для вмешательства.

**Параметры**:
- `text` (str): Текст условия.

**Возвращает**:
- `Intervention`: Возвращает объект `Intervention` для chaining.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Устанавливает атрибут `text_precondition` объекта `Intervention` равным переданному тексту.
2. Возвращает объект `Intervention` для возможности chaining вызовов методов.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Установка текстового условия
intervention.set_textual_precondition("agent is happy")
```

### `set_functional_precondition`

```python
def set_functional_precondition(self, func):
```

**Назначение**: Устанавливает функциональное условие для вмешательства.

**Параметры**:
- `func` (function): Функция условия. Должна принимать цель вмешательства (агент, мир или список агентов/миров) в качестве аргумента и возвращать булево значение.

**Возвращает**:
- `Intervention`: Возвращает объект `Intervention` для chaining.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Устанавливает атрибут `precondition_func` объекта `Intervention` равным переданной функции.
2. Возвращает объект `Intervention` для возможности chaining вызовов методов.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Установка функционального условия
intervention.set_functional_precondition(lambda x: True)
```

### `set_effect`

```python
def set_effect(self, effect_func):
```

**Назначение**: Устанавливает эффект вмешательства.

**Параметры**:
- `effect_func` (function): Функция эффекта. Должна принимать цель вмешательства (агент, мир или список агентов/миров) в качестве аргумента.

**Возвращает**:
- `Intervention`: Возвращает объект `Intervention` для chaining.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Устанавливает атрибут `effect_func` объекта `Intervention` равным переданной функции.
2. Возвращает объект `Intervention` для возможности chaining вызовов методов.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Установка эффекта
intervention.set_effect(lambda x: print("Applying effect to agent!"))
```

### `precondition_justification`

```python
def precondition_justification(self):
```

**Назначение**: Возвращает обоснование для предопределенного условия.

**Параметры**:
- `None`

**Возвращает**:
- `str`: Возвращает строку с обоснованием для предопределенного условия.

**Вызывает исключения**:
- `None`

**Как работает функция**:
1. Проверяет, было ли установлено текстовое условие. Если да, добавляет обоснование из объекта `Proposition` и его уверенность.
2. Если текстовое условие не установлено, проверяет, было ли выполнено функциональное условие. Если да, добавляет соответствующее сообщение.
3. Если ни одно из условий не выполнено, добавляет сообщение о том, что условия не выполнены.
4. Возвращает строку с обоснованием.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson

agent = TinyPerson()
intervention = Intervention(targets=agent, name="MyIntervention")

# Задание текстового условия
intervention.set_textual_precondition("agent is happy")

# Получение обоснования
justification = intervention.precondition_justification()
print(f"Justification: {justification}")
```

## ASII flowchart функции `execute`

```
Начало
↓
Проверка условия (check_precondition)
│
├───> Условие выполнено? (True)
│     ↓
│     Применение эффекта (apply_effect)
│     ↓
│     Конец (True)
│
└───> Условие не выполнено? (False)
      ↓
      Конец (False)
```

## ASII flowchart функции `check_precondition`

```
Начало
↓
Создание объекта Proposition для текстового условия
↓
Проверка наличия функционального условия
│
├───> Функциональное условие задано? (Да)
│     ↓
│     Выполнение функционального условия
│     ↓
│     Результат выполнения функционального условия
│
└───> Функциональное условие не задано? (Нет)
│     ↓
│     Результат = True (условие выполнено по умолчанию)
│
↓
Проверка обоих условий (текстового и функционального)
↓
Возврат результата (True, если оба условия выполнены)
↓
Конец