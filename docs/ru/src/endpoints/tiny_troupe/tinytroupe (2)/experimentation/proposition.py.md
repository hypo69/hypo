# Модуль для определения и проверки пропозиций в контексте TinyTroupe

## Обзор

Модуль `proposition.py` определяет класс `Proposition`, который представляет собой утверждение (claim) о цели (target), которая может быть экземпляром `TinyWorld`, `TinyPerson` или их списком. Модуль также содержит функцию `check_proposition` для удобной проверки утверждений без создания объекта `Proposition`. Этот модуль используется для оценки истинности утверждений относительно поведения агентов или состояния их окружения в симуляции многоагентной среды.

## Подробнее

Этот модуль предоставляет инструменты для формализации и проверки гипотез о поведении виртуальных агентов в рамках симуляции TinyTroupe. Он позволяет задавать утверждения о целях (агентах или окружении) и проверять их истинность на основе траектории симуляции и дополнительного контекста.

## Классы

### `Proposition`

**Описание**: Класс `Proposition` представляет собой утверждение о цели (target), которое может быть экземпляром `TinyWorld`, `TinyPerson` или их списком.

**Принцип работы**:
Класс инициализируется с целью (или целями), утверждением и опциональными параметрами для указания количества первых или последних взаимодействий, которые следует учитывать в контексте. Метод `check` использует `LLMRequest` для оценки истинности утверждения на основе предоставленного контекста и возвращает результат.

**Аттрибуты**:

- `targets` (list): Список целей (экземпляры `TinyWorld` или `TinyPerson`), к которым относится утверждение.
- `claim` (str): Текст утверждения.
- `first_n` (int): Количество первых взаимодействий, которые следует учитывать в контексте.
- `last_n` (int): Количество последних взаимодействий (самых последних), которые следует учитывать в контексте.
- `value` (bool): Значение утверждения (True или False) после проверки.
- `justification` (str): Обоснование значения утверждения, предоставленное LLM.
- `confidence` (float): Уверенность LLM в значении утверждения.
- `raw_llm_response` (str): Необработанный ответ от LLM.

**Методы**:

- `__init__(self, target, claim: str, first_n: int = None, last_n: int = None)`: Инициализирует объект `Proposition`.
- `__call__(self, additional_context=None)`: Позволяет вызывать объект `Proposition` как функцию, что эквивалентно вызову метода `check`.
- `check(self, additional_context="No additional context available.")`: Проверяет утверждение на основе предоставленного контекста и возвращает результат.

### `Proposition.__init__`

```python
def __init__(self, target, claim:str, first_n:int=None, last_n:int=None):
    """ 
    Define a proposition as a (textual) claim about a target, which can be a TinyWorld, a TinyPerson or several of any.

    Args:
        target (TinyWorld, TinyPerson, list): the target or targets of the proposition
        claim (str): the claim of the proposition
        first_n (int): the number of first interactions to consider in the context
        last_n (int): the number of last interactions (most recent) to consider in the context

    """
```

**Назначение**: Инициализирует экземпляр класса `Proposition`, определяя его цель, утверждение и контекст.

**Параметры**:
- `target` (TinyWorld, TinyPerson, list): Цель или цели пропозиции. Может быть экземпляром `TinyWorld`, `TinyPerson` или списком этих экземпляров.
- `claim` (str): Текстовое утверждение, которое необходимо проверить.
- `first_n` (int, optional): Количество первых взаимодействий, которые нужно учитывать в контексте. По умолчанию `None`.
- `last_n` (int, optional): Количество последних взаимодействий, которые нужно учитывать в контексте. По умолчанию `None`.

**Как работает функция**:
1. Проверяет тип цели (`target`). Если цель является экземпляром `TinyWorld` или `TinyPerson`, она помещается в список `self.targets`. Если цель является списком, проверяется, что все элементы списка являются экземплярами `TinyWorld` или `TinyPerson`. Если цель имеет недопустимый тип, выбрасывается исключение `ValueError`.
2. Сохраняет утверждение (`claim`) в атрибуте `self.claim`.
3. Сохраняет значения `first_n` и `last_n` в соответствующих атрибутах.
4. Инициализирует атрибуты `self.value`, `self.justification` и `self.confidence` значением `None`.

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.experimentation.proposition import Proposition

# Пример с TinyWorld
world = TinyWorld(name="MyWorld")
proposition1 = Proposition(target=world, claim="The world is cold.")

# Пример с TinyPerson
person = TinyPerson(name="Alice")
proposition2 = Proposition(target=person, claim="Alice is happy.")

# Пример со списком целей
proposition3 = Proposition(target=[world, person], claim="Both are content.")
```

### `Proposition.__call__`

```python
def __call__(self, additional_context=None):
    """
    # аннотация типов
    """
    return self.check(additional_context=additional_context)
```

**Назначение**: Позволяет вызывать экземпляр класса `Proposition` как функцию.

**Параметры**:
- `additional_context` (str, optional): Дополнительный контекст для проверки утверждения. По умолчанию `None`.

**Возвращает**:
- bool: Результат проверки утверждения.

**Как работает функция**:
Вызывает метод `self.check` с переданным дополнительным контекстом и возвращает результат.

**Примеры**:
```python
from tinytroupe.agent import TinyPerson
from tinytroupe.experimentation.proposition import Proposition

person = TinyPerson(name="Alice")
proposition = Proposition(target=person, claim="Alice is happy.")

# Вызов экземпляра класса как функции
result = proposition()
print(result)  # Выведет True или False в зависимости от результата проверки
```

### `Proposition.check`

```python
def check(self, additional_context="No additional context available."):
    """
    # аннотация типов
    """

    context = ""

    for target in self.targets:
        target_trajectory = target.pretty_current_interactions(max_content_length=None, first_n=self.first_n, last_n=self.last_n)

        if isinstance(target, TinyPerson):
            context += f"## Agent \'{target.name}\' Simulation Trajectory\\n\\n"
        elif isinstance(target, TinyWorld):
            context += f"## Environment \'{target.name}\' Simulation Trajectory\\n\\n"

        context += target_trajectory + "\\n\\n"

    llm_request = LLMRequest(system_prompt="""
                                You are a system that evaluates whether a proposition is true or false with respect to a given context. This context
                                always refers to a multi-agent simulation. The proposition is a claim about the behavior of the agents or the state of their environment
                                in the simulation.
                            
                                The context you receive can contain one or more of the following:
                                - the trajectory of a simulation of one or more agents. This means what agents said, did, thought, or perceived at different times.
                                - the state of the environment at a given time.
                            
                                Your output **must**:\
                                  - necessarily start with the word "True" or "False";\
                                  - optionally be followed by a justification.\
                             
                                For example, the output could be of the form: "True, because <REASON HERE>." or merely "True" if no justification is needed.
                                """, 

                                user_prompt=f"""
                                Evaluate the following proposition with respect to the context provided. Is it True or False?

                                # Proposition

                                This is the proposition you must evaluate:
                                {self.claim}

                                # Context

                                The context you must consider is the following.

                                {context}

                                # Additional Context (if any)

                                {additional_context}   
                                """,

                                output_type=bool)
    

    self.value = llm_request()
    self.justification = llm_request.response_justification      
    self.confidence = llm_request.response_confidence

    self.raw_llm_response = llm_request.response_raw

    return self.value
```

**Назначение**: Проверяет, выполняется ли утверждение для заданных целей, используя языковую модель (LLM).

**Параметры**:
- `additional_context` (str, optional): Дополнительный контекст, который предоставляется LLM для оценки утверждения. По умолчанию "No additional context available.".

**Возвращает**:
- `bool`: `True`, если утверждение выполняется, и `False` в противном случае.

**Как работает функция**:

1. **Формирование контекста**:
   - Инициализируется пустая строка `context`.
   - Для каждой цели в `self.targets`:
     - Извлекается траектория взаимодействий цели с помощью `target.pretty_current_interactions()`. Указываются `first_n` и `last_n` для ограничения учитываемых взаимодействий.
     - Добавляется заголовок в контекст, указывающий, является ли цель агентом (`TinyPerson`) или окружением (`TinyWorld`).
     - Добавляется траектория взаимодействий цели в контекст.

2. **Формирование запроса к LLM**:
   - Создается объект `LLMRequest` с:
     - `system_prompt`: Инструкция для LLM, определяющая его роль как системы оценки истинности утверждений на основе контекста симуляции многоагентной среды. Инструкция также определяет формат вывода LLM: "True" или "False", возможно, с обоснованием.
     - `user_prompt`: Запрос к LLM, включающий:
       - Утверждение (`self.claim`), которое необходимо оценить.
       - Контекст, сформированный на основе траекторий целей.
       - Дополнительный контекст (`additional_context`), если он предоставлен.
     - `output_type`: Указывает, что ожидаемый тип вывода - `bool`.

3. **Выполнение запроса к LLM и обработка ответа**:
   - Выполняется запрос к LLM с помощью `llm_request()`.
   - Значение утверждения (`self.value`) устанавливается равным результату, возвращенному LLM.
   - Обоснование (`self.justification`) извлекается из ответа LLM с помощью `llm_request.response_justification`.
   - Уверенность (`self.confidence`) извлекается из ответа LLM с помощью `llm_request.response_confidence`.
   - Необработанный ответ LLM сохраняется в `self.raw_llm_response`.

4. **Возврат результата**:
   - Возвращается значение утверждения (`self.value`).

**ASCII Flowchart**:

```
Начало
  ↓
Формирование контекста (перебор целей)
  │
  └──> Извлечение траектории взаимодействий цели
  │
  └──> Добавление заголовка (тип цели)
  │
  └──> Добавление траектории в контекст
  ↓
Формирование запроса к LLM
  │
  └──> Определение system_prompt
  │
  └──> Определение user_prompt (утверждение, контекст, доп. контекст)
  │
  └──> Указание output_type (bool)
  ↓
Выполнение запроса к LLM
  ↓
Обработка ответа LLM
  │
  └──> Извлечение значения (True/False)
  │
  └──> Извлечение обоснования
  │
  └──> Извлечение уверенности
  │
  └──> Сохранение необработанного ответа
  ↓
Возврат значения утверждения (True/False)
Конец
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.experimentation.proposition import Proposition

# Пример с TinyPerson
person = TinyPerson(name="Alice")
proposition = Proposition(target=person, claim="Alice is happy.")
result = proposition.check()
print(f"Is the proposition true? {result}")

# Пример с TinyWorld и дополнительным контекстом
world = TinyWorld(name="MyWorld")
proposition = Proposition(target=world, claim="The world is cold.")
result = proposition.check(additional_context="The simulation was run in winter.")
print(f"Is the proposition true? {result}")

# Пример с указанием количества первых и последних взаимодействий
person = TinyPerson(name="Bob")
proposition = Proposition(target=person, claim="Bob is talkative.", first_n=5, last_n=5)
result = proposition.check()
print(f"Is the proposition true? {result}")
```

## Функции

### `check_proposition`

```python
def check_proposition(target, claim:str, additional_context="No additional context available.",
                      first_n:int=None, last_n:int=None):
    """
    Check whether a propositional claim holds for the given target(s). This is meant as a
    convenience method to avoid creating a Proposition object (which you might not need
    if you are not interested in the justification or confidence of the claim, or will
    not use it again).

    Args:
        target (TinyWorld, TinyPerson, list): the target or targets of the proposition
        claim (str): the claim of the proposition
        additional_context (str): additional context to provide to the LLM
        first_n (int): the number of first interactions to consider in the context
        last_n (int): the number of last interactions (most recent) to consider in the context

    Returns:
        bool: whether the proposition holds for the given target(s)
    """
```

**Назначение**: Проверяет, выполняется ли утверждение для заданных целей. Является удобным методом для избежания создания объекта `Proposition`.

**Параметры**:

- `target` (TinyWorld, TinyPerson, list): Цель или цели пропозиции. Может быть экземпляром `TinyWorld`, `TinyPerson` или списком этих экземпляров.
- `claim` (str): Утверждение, которое необходимо проверить.
- `additional_context` (str, optional): Дополнительный контекст, предоставляемый LLM для оценки утверждения. По умолчанию "No additional context available.".
- `first_n` (int, optional): Количество первых взаимодействий, которые следует учитывать в контексте. По умолчанию `None`.
- `last_n` (int, optional): Количество последних взаимодействий (самых последних), которые следует учитывать в контексте. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если утверждение выполняется, и `False` в противном случае.

**Как работает функция**:

1. **Создание экземпляра `Proposition`**:
   - Создается экземпляр класса `Proposition` с переданными аргументами `target`, `claim`, `first_n` и `last_n`.

2. **Проверка утверждения**:
   - Вызывается метод `check` экземпляра `Proposition` с переданным `additional_context`.

3. **Возврат результата**:
   - Возвращается результат проверки утверждения, полученный от метода `check`.

**ASCII Flowchart**:

```
Начало
  ↓
Создание экземпляра Proposition
  │
  └──> Передача target, claim, first_n, last_n
  ↓
Вызов метода check экземпляра Proposition
  │
  └──> Передача additional_context
  ↓
Возврат результата проверки утверждения (True/False)
Конец
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.experimentation.proposition import check_proposition

# Пример с TinyPerson
person = TinyPerson(name="Alice")
result = check_proposition(target=person, claim="Alice is happy.")
print(f"Is the proposition true? {result}")

# Пример с TinyWorld и дополнительным контекстом
world = TinyWorld(name="MyWorld")
result = check_proposition(target=world, claim="The world is cold.", additional_context="The simulation was run in winter.")
print(f"Is the proposition true? {result}")

# Пример с указанием количества первых и последних взаимодействий
person = TinyPerson(name="Bob")
result = check_proposition(target=person, claim="Bob is talkative.", first_n=5, last_n=5)
print(f"Is the proposition true? {result}")