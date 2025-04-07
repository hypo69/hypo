# Модуль `proposition.py`

## Обзор

Модуль `proposition.py` определяет класс `Proposition`, который используется для формулировки и проверки утверждений (propositional claims) о поведении агентов или состоянии среды в многоагентном моделировании. Также содержит функцию `check_proposition`, которая является удобным способом для проверки утверждений без создания объекта `Proposition`.

## Подробней

Этот модуль играет важную роль в проверке гипотез о поведении агентов и их взаимодействии со средой в симуляциях `TinyTroupe`. Он позволяет формулировать утверждения и автоматически оценивать их истинность на основе траектории симуляции с использованием языковых моделей (LLM). Класс `Proposition` инкапсулирует целевой объект (агента или среду), само утверждение и контекст, необходимый для его проверки.

## Классы

### `Proposition`

**Описание**: Класс `Proposition` представляет собой утверждение о целевом объекте, которое может быть проверено на основе контекста симуляции.

**Принцип работы**:
Класс принимает целевой объект (агента или среду), утверждение и необязательные параметры для ограничения контекста (количество первых или последних взаимодействий). При вызове метода `check`, класс формирует запрос к языковой модели, чтобы оценить истинность утверждения на основе предоставленного контекста. Результат оценки, обоснование и уверенность сохраняются в атрибутах объекта.

**Атрибуты**:
- `targets` (list): Список целевых объектов утверждения (экземпляры `TinyWorld` или `TinyPerson`).
- `claim` (str): Текст утверждения.
- `first_n` (int): Количество первых взаимодействий для включения в контекст.
- `last_n` (int): Количество последних взаимодействий для включения в контекст.
- `value` (bool): Значение истинности утверждения (True или False).
- `justification` (str): Обоснование значения истинности, предоставленное LLM.
- `confidence` (float): Уверенность LLM в оценке.
- `raw_llm_response` (str): Необработанный ответ от LLM.

**Методы**:

- `__init__(self, target, claim: str, first_n: int = None, last_n: int = None)`
- `__call__(self, additional_context=None)`
- `check(self, additional_context="No additional context available.")`

#### `__init__`

```python
def __init__(self, target, claim: str, first_n: int = None, last_n: int = None)
```

**Назначение**: Инициализирует объект `Proposition`.

**Параметры**:
- `target` (TinyWorld, TinyPerson, list): Целевой объект или список целевых объектов утверждения.
- `claim` (str): Текст утверждения.
- `first_n` (int, optional): Количество первых взаимодействий для включения в контекст. По умолчанию `None`.
- `last_n` (int, optional): Количество последних взаимодействий для включения в контекст. По умолчанию `None`.

**Как работает функция**:

1. **Проверяет тип целевого объекта**: Убеждается, что `target` является экземпляром `TinyWorld`, `TinyPerson` или списком, содержащим только экземпляры `TinyWorld` или `TinyPerson`.
2. **Устанавливает атрибуты объекта**: Присваивает значения атрибутам `targets`, `claim`, `first_n` и `last_n`.

```ascii
Проверка типа цели --> Установка атрибутов
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld

person = TinyPerson(name="Alice")
world = TinyWorld(name="Wonderland")

# Создание экземпляра Proposition с целевым объектом TinyPerson
proposition1 = Proposition(target=person, claim="Alice is happy")

# Создание экземпляра Proposition с целевым объектом TinyWorld
proposition2 = Proposition(target=world, claim="Wonderland is peaceful")

# Создание экземпляра Proposition со списком целевых объектов
proposition3 = Proposition(target=[person, world], claim="Alice is in Wonderland")
```

#### `__call__`

```python
def __call__(self, additional_context=None)
```

**Назначение**: Позволяет вызывать объект `Proposition` как функцию, что эквивалентно вызову метода `check`.

**Параметры**:
- `additional_context` (str, optional): Дополнительный контекст для предоставления LLM. По умолчанию `None`.

**Возвращает**:
- `bool`: Значение истинности утверждения.

**Как работает функция**:
Вызывает метод `check` с переданным дополнительным контекстом.

```ascii
Вызов метода check --> Возврат значения истинности
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson

person = TinyPerson(name="Alice")
proposition = Proposition(target=person, claim="Alice is happy")

# Вызов объекта Proposition как функции
result = proposition()
print(result)  # Выведет True или False в зависимости от результата проверки
```

#### `check`

```python
def check(self, additional_context="No additional context available.")
```

**Назначение**: Проверяет, выполняется ли утверждение для заданных целевых объектов.

**Параметры**:
- `additional_context` (str, optional): Дополнительный контекст для предоставления LLM. По умолчанию "No additional context available.".

**Возвращает**:
- `bool`: Значение истинности утверждения (True или False).

**Как работает функция**:

1. **Подготовка контекста**: Собирает траектории симуляции для каждого целевого объекта и формирует контекст для LLM запроса.
2. **Создание запроса к LLM**: Создает объект `LLMRequest` с системным и пользовательским запросами, включающими утверждение и контекст.
3. **Выполнение запроса**: Вызывает LLM и получает ответ.
4. **Обработка ответа**: Извлекает значение истинности, обоснование и уверенность из ответа LLM.
5. **Сохранение результатов**: Сохраняет результаты в атрибутах объекта.

```ascii
Подготовка контекста --> Создание LLMRequest --> Выполнение LLMRequest --> Обработка ответа --> Сохранение результатов --> Возврат значения истинности
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson

person = TinyPerson(name="Alice")
proposition = Proposition(target=person, claim="Alice is happy")

# Проверка утверждения
result = proposition.check()
print(result)  # Выведет True или False в зависимости от результата проверки
print(proposition.justification)  # Выведет обоснование, предоставленное LLM
print(proposition.confidence)  # Выведет уверенность LLM в оценке
```

## Функции

### `check_proposition`

```python
def check_proposition(target, claim: str, additional_context="No additional context available.",
                      first_n: int = None, last_n: int = None) -> bool:
```

**Назначение**: Проверяет, выполняется ли утверждение для заданных целевых объектов, используя класс `Proposition`. Является удобной функцией для однократной проверки утверждений без создания объекта `Proposition`.

**Параметры**:
- `target` (TinyWorld, TinyPerson, list): Целевой объект или список целевых объектов утверждения.
- `claim` (str): Текст утверждения.
- `additional_context` (str, optional): Дополнительный контекст для предоставления LLM. По умолчанию "No additional context available.".
- `first_n` (int, optional): Количество первых взаимодействий для включения в контекст. По умолчанию `None`.
- `last_n` (int, optional): Количество последних взаимодействий для включения в контекст. По умолчанию `None`.

**Возвращает**:
- `bool`: Значение истинности утверждения (True или False).

**Как работает функция**:

1. **Создание объекта `Proposition`**: Создает экземпляр класса `Proposition` с переданными параметрами.
2. **Проверка утверждения**: Вызывает метод `check` объекта `Proposition` с дополнительным контекстом.
3. **Возврат результата**: Возвращает значение истинности утверждения.

```ascii
Создание Proposition --> Вызов check --> Возврат значения истинности
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson

person = TinyPerson(name="Alice")

# Проверка утверждения с помощью функции check_proposition
result = check_proposition(target=person, claim="Alice is happy")
print(result)  # Выведет True или False в зависимости от результата проверки